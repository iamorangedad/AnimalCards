"""从 Natural Earth 1:50m 国家数据（公有领域）生成国家代表点。
- 国家代表点：LABEL_X/LABEL_Y（Natural Earth 自带的标注点）
- 方位点（如“中国南部”“美国东南部”）：在该国最大多边形的外接框内按方位取点，
  纬度按方位取外接框的上/下部，经度取该纬线与国界交出的最长线段上的对应位置（保证在国界内）。仅为近似代表点。
用法: python build_gazetteer.py ne_50m_admin_0_countries.geojson
数据来源: https://github.com/nvkelso/natural-earth-vector (Public Domain)"""
import json, sys, os
DIRS = {"北": (.78, .5), "南": (.22, .5), "东": (.5, .78), "西": (.5, .22), "中": (.5, .5), "东北": (.75, .75), "东南": (.25, .75),
        "西北": (.75, .25), "西南": (.25, .25), "中东": (.5, .68), "中西": (.5, .32), "中南": (.35, .5), "中北": (.65, .5)}
def area(r):
    return abs(sum(r[i][0] * r[i + 1][1] - r[i + 1][0] * r[i][1] for i in range(len(r) - 1))) / 2
def inside(pt, ring):
    x, y = pt; c = False
    for i in range(len(ring) - 1):
        (x1, y1), (x2, y2) = ring[i], ring[i + 1]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: c = not c
    return c
src = sys.argv[1]
d = json.load(open(src, encoding="utf-8"))
out = {}
for f in d["features"]:
    p = f["properties"]; zh = (p.get("NAME_ZH") or "").strip()
    if not zh: continue
    g = f["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    ring = max((pl[0] for pl in polys), key=area)
    xs = [c[0] for c in ring]; ys = [c[1] for c in ring]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    lab = (p["LABEL_X"], p["LABEL_Y"])
    dirs = {}
    for k, (fy, fx) in DIRS.items():
        y = y0 + fy * (y1 - y0)
        xs_ = sorted((ax + (y - ay) * (bx - ax) / (by - ay)) for (ax, ay), (bx, by) in zip(ring, ring[1:]) if (ay > y) != (by > y))
        iv = [(xs_[i], xs_[i + 1]) for i in range(0, len(xs_) - 1, 2)]
        if iv:
            a, b = max(iv, key=lambda t: t[1] - t[0]); dirs[k] = [round(y, 2), round(a + fx * (b - a), 2)]
        else:
            dirs[k] = [round(lab[1], 2), round(lab[0], 2)]
    out[zh] = {"lat": round(lab[1], 3), "lon": round(lab[0], 3), "en": p["NAME"], "kind": "land", "dirs": dirs}
dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "gazetteer_ne.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "countries ->", dst)
