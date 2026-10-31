"""生成 webapp/data/animals.json。
数据来源：仓库 tools/data/*.json（每张卡的数据，含分布文字 range、IUCN、来源）。
位置 = 在卡片“分布”文字（取自维基百科/IUCN）里匹配到的国家/区域名称的代表点：
  - 国家：Natural Earth 国家标注点（data/gazetteer_ne.json）
  - 区域/海域：scripts/regions_manual.py 里人工设定的大致中心点
所有点都是近似代表点（approx=true），不是精确分布范围。
人工补充的位置（卡片分布文字里没有可用地名时）见 data/locations_manual.json，每条带来源。"""
import json, glob, os, re, math, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from regions_manual import R, ALIAS, WIDE, WIDE_LAND, WIDE_SEA, WIDE_TROPIC
GAZ = json.load(open(os.path.join(HERE, "..", "data", "gazetteer_ne.json"), encoding="utf-8"))
MANUAL = json.load(open(os.path.join(HERE, "..", "data", "locations_manual.json"), encoding="utf-8"))
CATS = ["宠物", "农场", "高原草原", "森林", "海洋", "鸟类", "爬行两栖", "昆虫",
        "花卉", "树木", "农作物", "水果蔬菜", "沙漠植物", "水生植物", "蘑菇", "霉菌酵母"]
KINGDOMS = {"动物": CATS[:8], "植物": CATS[8:14], "真菌": CATS[14:]}
SEAGRASS = {"eelgrass", "posidonia"}  # 海草：按海域定位
NONNATIVE = re.compile(r"引入|引种|养殖|入侵|传到|遍布|已被|现已|饲养|栽培|驯化后|随人类|带到|扩散到")
names = {}
for k, v in GAZ.items(): names[k] = (v["lat"], v["lon"], "land", "Natural Earth 国家标注点")
for k, v in ALIAS.items():
    if v in GAZ: names[k] = (GAZ[v]["lat"], GAZ[v]["lon"], "land", "Natural Earth 国家标注点")
names["蒙古"] = names["蒙古国"]
names.pop("英国", None); names["英国"] = (GAZ["英国"]["lat"], GAZ["英国"]["lon"], "land", "Natural Earth 国家标注点"); names["刚果"] = names["刚果民主共和国"]
for k, (la, lo, kind) in R.items(): names[k] = (la, lo, kind, "人工设定区域代表点")
KEYS = sorted(names, key=len, reverse=True)
DIRRE = re.compile(r"(东南|东北|西南|西北|中东|中西|中南|中北|东|西|南|北|中)部")
GENERIC_OCEAN = {"太平洋", "大西洋", "印度洋"}
def clean(text):
    text = re.sub(r"（[^）]*除外）", "", text)
    return re.sub(r"除[^，；。、]*?外", "", text)
def find(text, marine):
    """返回 [(显示名, lat, lon, kind, basis)]，按在文字中出现的顺序。"""
    hits, used = [], [False] * len(text)
    for k in KEYS:
        for m in re.finditer(re.escape(k), text):
            if any(used[m.start():m.end()]): continue
            end = m.end(); la, lo, kind, basis = names[k]; label = k
            if not marine and k in GENERIC_OCEAN and text[end:end + 2] in ("沿岸", "沿海", "海岸"): continue
            dm = DIRRE.match(text, end)
            gk = ALIAS.get(k, k)
            if dm and gk in GAZ:
                la, lo = GAZ[gk]["dirs"][dm.group(1)]; label = k + dm.group(0); basis = "Natural Earth 国界按方位推算"; end = dm.end()
            for i in range(m.start(), end): used[i] = True
            hits.append((m.start(), (label, la, lo, kind, basis)))
    return [h for _, h in sorted(hits)]
def dist(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    return 6371 * math.acos(min(1, math.sin(la1) * math.sin(la2) + math.cos(la1) * math.cos(la2) * math.cos(lo1 - lo2)))
def wiki_url(sources):
    for s in sources:
        m = re.match(r"Wikipedia「(.+)」", s)
        if m: return "https://en.wikipedia.org/wiki/" + urllib.parse.quote(m.group(1).replace(" ", "_"))
    for s in sources:
        m = re.match(r"维基百科「(.+)」", s)
        if m: return "https://zh.wikipedia.org/wiki/" + urllib.parse.quote(m.group(1))
    return ""
out, stats = [], {"total": 0, "from_range_text": 0, "manual": 0, "wide": 0, "pending": 0}
for f in sorted(glob.glob(os.path.join(ROOT, "tools", "data", "*.json"))):
    d = json.load(open(f, encoding="utf-8")); aid = os.path.basename(f)[:-5]
    rng = d.get("range", ""); cat = d["cat"]; marine = cat == "海洋" or aid in SEAGRASS
    kingdom = d.get("kingdom", "动物")
    rng_n = re.sub(r"（[^）]*引入[^）]*）", "", rng)  # 括号里的“重引入点”不影响原生地名
    segs = [s for s in re.split(r"[；;。，,]", rng_n) if s.strip()]
    native = [s for s in segs if not NONNATIVE.search(s)] or []
    locs, method, note = [], None, ""
    if aid in MANUAL:
        m = MANUAL[aid]; method = "manual"; note = m["range_note"]
        for p in m["points"]:
            locs.append({"lat": p[0], "lon": p[1], "label": p[2], "approx": True, "kind": "manual"})
        src = m["source"]
    else:
        src = wiki_url(d.get("sources", []))
        keys = find(clean("；".join(native)), marine)
        if marine:  # 海洋动物优先用海域点
            sea = [k for k in keys if k[3] == "sea"]
            keys = sea or keys
        else:  # 陆地动物优先用陆地点
            land = [k for k in keys if k[3] == "land"]
            keys = land or keys
        for label, la, lo, kind, basis in keys:
            if any(dist((la, lo), (l["lat"], l["lon"])) < 400 for l in locs): continue
            locs.append({"lat": la, "lon": lo, "label": label, "approx": True, "kind": basis})
            if len(locs) == 3: break
        if locs: method = "range_text"; note = rng
        elif not marine and "热带" in rng and "温带" not in rng:
            method = "wide"; note = "热带广泛分布：" + rng
            for la, lo, lab in WIDE_TROPIC:
                locs.append({"lat": la, "lon": lo, "label": lab, "approx": True, "kind": "热带广泛分布代表点"})
        elif any(w in rng for w in WIDE):
            method = "wide"; note = "广泛分布：" + rng
            for la, lo, lab in (WIDE_SEA if marine else WIDE_LAND):
                locs.append({"lat": la, "lon": lo, "label": lab, "approx": True, "kind": "广泛分布代表点"})
    sub = d["iucn"].get("sub", "")
    domestic = "家养" in sub
    cultivated = "栽培" in sub  # 栽培植物 / 栽培食用菌：点位表示原产地或起源，不是全部种植区
    if domestic and method == "wide":  # 家养动物不能用“全世界”代替驯化起源
        note = "驯化起源待核；" + rng
    if domestic and method == "range_text":
        note = "原产地/驯化起源（据卡片分布文字）：" + rng
    if cultivated and method == "range_text":
        note = "原产地/起源（据卡片分布文字；现已广泛栽培）：" + rng
    if cultivated and method == "wide":
        note = "广泛栽培，原产地待核；" + rng
    pending = method is None or ((domestic or cultivated) and method == "wide")
    stats["total"] += 1; stats[{"range_text": "from_range_text", "manual": "manual", "wide": "wide", None: "pending"}[method]] += 1
    stats["pending_flag"] = stats.get("pending_flag", 0) + (1 if pending else 0)
    folder = f"{kingdom}/{cat}/{d['file']}"
    out.append({"id": aid, "number": int(d["no"]), "name_zh": d["name_cn"], "name_en": d["name_en"], "latin": d["latin"],
                "kingdom": kingdom, "category": cat, "iucn": d["iucn"]["code"], "iucn_note": d["iucn"].get("sub", ""), "range_text": rng,
                "diet": d.get("diet", ""), "intro": d.get("intro", []), "fact": d.get("fact", ""),
                "locations": locs, "range_note": note or "待核：卡片分布文字中没有可定位的地名", "location_method": method or "pending",
                "location_pending": pending, "domestic": domestic, "cultivated": cultivated, "source": src, "sources_card": d.get("sources", []),
                "card_png": folder + ".png", "card_pdf": folder + ".pdf",
                "thumb": f"thumbs/{aid}_400.webp", "avatar": f"thumbs/{aid}_120.webp"})
out.sort(key=lambda a: a["number"])
meta = {"generated_by": "webapp/scripts/build_data.py", "count": len(out), "stats": stats, "categories": CATS, "kingdoms": KINGDOMS,
        "note": "位置为根据卡片分布文字匹配的国家/区域代表点（近似）；栽培植物/食用菌标的是原产地或起源，微生物多为“广泛分布”代表点，由 AI 辅助生成，需人工复核。"}
json.dump({"meta": meta, "animals": out}, open(os.path.join(HERE, "..", "data", "animals.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(stats)
for a in out:
    if a["location_method"] == "pending": print("PENDING", a["id"], a["name_zh"], "|", a["range_text"])
