#!/usr/bin/env python3
"""Animal trading cards: data/<id>.json -> out/<id>.{html,png,pdf}. Art from art.py (ART[id](w, h))."""
import json, math, pathlib, subprocess, sys
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from playwright.sync_api import sync_playwright
import icons
import art
import art5
art.ART.update(art5.ART5)
import art6
art.ART.update(art6.ART6)

HERE = pathlib.Path(__file__).resolve().parent
W, H = 1080, 1920
ART_W, ART_H = 1080 - 2 * 22 - 2 * 16 - 2 * 30 - 4, 600
TYPE = {"陆地": ("#5f8f5a", "#e1efda"), "水中": ("#2f7de1", "#dceafb"), "天空": ("#3a9fc9", "#dcf1f9"), "两栖": ("#2a9d8f", "#d9f2ef"), "植物": ("#4f9a3a", "#e3f2d6"), "水生": ("#2a8ab0", "#d8eef6"), "沙漠": ("#c9862e", "#fbecd2"), "菌类": ("#8a5a3a", "#f3e6da"), "地衣": ("#6f8a5a", "#e8eedc")}
IUCN = {"EX": ("#000000", "#ffffff", "灭绝"), "EW": ("#542344", "#ffffff", "野外灭绝"), "CR": ("#d81e05", "#fde4e0", "极危"),
        "EN": ("#fc7f3f", "#fff0e6", "濒危"), "VU": ("#e0a800", "#fff7d6", "易危"), "NT": ("#9aa83b", "#f2f6dc", "近危"),
        "LC": ("#60c659", "#e6f7e4", "无危"), "DD": ("#6b7075", "#eeeeee", "数据缺乏"), "NE": ("#6b7075", "#ffffff", "未评估")}
SCALES = {"abyss": ("lin", 0, 3000, [1000, 2000]), "min_l": ("lin", 0, 120, [30, 60, 90]), "min": ("lin", 0, 20, [5, 10, 15]), "yield": ("log", 100, 100000, [1000, 10000]), "ton": ("log", 1000, 1e7, [1e4, 1e5, 1e6]), "mass": ("log", 0.1, 10000, [1, 10, 100, 1000]), "mass_s": ("log", 1e-6, 10, [1e-3, 1]), "mass_xl": ("log", 1, 200000, [100, 10000]),
          "len": ("log", 0.1, 10, [1]), "len_s": ("log", 0.001, 1, [0.01, 0.1]), "len_xl": ("log", 1, 40, [10]),
          "life": ("lin", 0, 80, [20, 40, 60]), "life_xl": ("lin", 0, 200, [50, 100, 150]),
          "hours": ("lin", 0, 24, [6, 12, 18]), "depth": ("lin", 0, 600, [200, 400]), "depth_xl": ("lin", 0, 2000, [500, 1000, 1500]),
          "speed": ("lin", 0, 120, [30, 60, 90]), "food": ("lin", 0, 200, [50, 100, 150]), "days": ("lin", 0, 400, [100, 200, 300]),
          "alt": ("lin", 0, 6000, [2000, 4000]), "km": ("log", 1, 10000, [10, 100, 1000]), "temp": ("lin", 0, 50, [10, 20, 30, 40]), "n400": ("lin", 0, 400, [100, 200, 300]), "months": ("lin", 0, 24, [6, 12, 18]),
          "n100": ("lin", 0, 100, [25, 50, 75]), "eggs": ("log", 1, 1e7, [100, 1e4, 1e6]), "km_xl": ("log", 1, 100000, [10, 1000]),
          "len_xs": ("log", 0.001, 100, [0.1, 10]), "pct": ("lin", 0, 100, [25, 50, 75]), "sec": ("lin", 0, 20, [5, 10, 15]),
          "len_xxl": ("log", 1, 150, [10, 100]), "yrs": ("log", 1, 10000, [10, 100, 1000]), "um": ("log", 1, 1000, [10, 100]), "rain": ("lin", 0, 4000, [1000, 2000, 3000]),
          "tempw": ("lin", -50, 50, [-25, 0, 25]), "tha": ("lin", 0, 20, [5, 10, 15]), "ph": ("lin", 0, 14, [4, 7, 10]), "mt": ("log", 0.1, 1000, [1, 10, 100]), "n1000": ("log", 1, 1000, [10, 100]), "dia": ("log", 0.01, 10, [0.1, 1]), "cnt": ("log", 1, 1e9, [1e3, 1e6]), "myr": ("log", 1, 1000, [10, 100])}
SDESC = {"min": "时间 0–20 分钟", "yield": "产量 100 kg–100 t（对数）", "ton": "产量 1000 吨–1000 万吨（对数）", "mass": "体重 0.1 kg–10 t（对数）", "mass_s": "体重 1 mg–10 kg（对数）", "mass_xl": "体重 1 kg–200 t（对数）",
         "abyss": "水深 0–3000 m", "min_l": "时长 0–120 分钟", "len": "长度 10 cm–10 m（对数）", "len_s": "长度 1 mm–1 m（对数）", "len_xl": "长度 1–40 m（对数）",
         "life": "寿命 0–80 年", "life_xl": "寿命 0–200 年", "hours": "时长 0–24 小时", "depth": "水深 0–600 m", "depth_xl": "水深 0–2000 m",
         "speed": "速度 0–120 km/h", "food": "食量 0–200 kg", "days": "天数 0–400 天", "alt": "海拔 0–6000 m", "km": "距离 1–10000 km（对数）", "temp": "温度 0–50 °C", "n400": "数量 0–400", "months": "月数 0–24 个月", "n100": "数量 0–100", "eggs": "数量 1–1000 万（对数）", "km_xl": "距离 1–10 万 km（对数）", "len_xs": "长度 1 mm–100 m（对数）", "pct": "比例 0–100%", "sec": "时间 0–20 秒", "len_xxl": "高度 1–150 m（对数）", "yrs": "年数 1–1 万年（对数）", "um": "大小 1–1000 µm（对数）", "rain": "降水 0–4000 mm", "tempw": "温度 −50–50 °C", "tha": "产量 0–20 t/公顷", "ph": "pH 0–14", "mt": "产量 0.1–1000 百万吨（对数）", "n1000": "数量 1–1000（对数）", "dia": "直径 1 cm–10 m（对数）", "cnt": "数量 1–10 亿（对数）", "myr": "时间 1–1000 百万年（对数）"}


def note(stats):
    seen = []
    for st in stats:
        if st["scale"] not in seen:
            seen.append(st["scale"])
    return "刻度：" + "；".join(SDESC[k] for k in seen) + "。实心 = 0 到下限，条纹 = 范围。"


def pos(kind, v):
    m, a, b, _ = SCALES[kind]
    f = (math.log10(v) - math.log10(a)) / (math.log10(b) - math.log10(a)) if m == "log" else (v - a) / (b - a)
    return max(0.0, min(100.0, f * 100))


def bar(s):
    a, b = pos(s["scale"], s["lo"]), pos(s["scale"], s.get("hi", s["lo"]))
    ticks = [round(pos(s["scale"], t), 2) for t in SCALES[s["scale"]][3]]
    return dict(s, a=round(a, 2), b=round(a, 2), w=round(max(b - a, 1.8), 2), ticks=ticks)


def render(ids, pdf=True):
    env = Environment(loader=FileSystemLoader(HERE), autoescape=True)
    env.globals["chipicon"] = lambda k: Markup(icons.chip(k))
    env.globals["skillicon"] = lambda k: Markup(icons.skill(k))
    out = HERE / "out"; out.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        for i in ids:
            d = json.loads((HERE / "data" / f"{i}.json").read_text(encoding="utf-8"))
            assert len(d["name_cn"]) <= 11
            d.setdefault("stat_title", {"植物": "植物数据", "真菌": "真菌数据"}.get(d.get("kingdom"), "身体数据"))
            acc, accl = TYPE[d["type"]]
            ic, ib, icn = IUCN[d["iucn"]["code"]]
            d["iucn"].setdefault("cn", icn)
            html = env.get_template("card.html.j2").render(d=d, acc=acc, accl=accl, iucn_col=ic, iucn_bg=ib, art_h=ART_H,
                                                          art=Markup(art.ART[i](ART_W, ART_H)), stats=[bar(s) for s in d["stats"]], scale_note=note(d["stats"]))
            hp = out / f"{d['file']}.html"; hp.write_text(html, encoding="utf-8")
            pg.goto(hp.as_uri()); pg.evaluate("document.fonts.ready")
            info = pg.evaluate("""() => { const P=document.querySelector('.poster').getBoundingClientRect();
              const clipped=[...document.querySelectorAll('.poster *')].filter(e=>!(e instanceof SVGElement)&&e.children.length===0&&e.scrollWidth>e.clientWidth+1).map(e=>e.className||e.tagName);
              const f=document.querySelector('.foot').getBoundingClientRect(); const r=document.querySelector('.range').getBoundingClientRect();
              return {clipped, slack: f.top - r.bottom, footBottom: P.bottom - f.bottom}; }""")
            chars = sorted({c for c in hp.read_text() if ord(c) > 0x7f})
            tofu = [c for c in chars if not subprocess.run(["fc-list", f":family=Noto Sans CJK SC:charset={ord(c):x}", "family"], capture_output=True, text=True).stdout.strip()]
            pg.screenshot(path=str(out / f"{d['file']}.png"), clip={"x": 0, "y": 0, "width": W, "height": H})
            if int(d["no"]) >= 401:
                from PIL import Image
                q = Image.open(out / f"{d['file']}.png").convert("RGB").quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
                q.save(out / f"{d['file']}.png", optimize=True)
            if pdf:
                pg.pdf(path=str(out / f"{d['file']}.pdf"), width=f"{W}px", height=f"{H}px", print_background=True, page_ranges="1")
            print(i, info, "tofu", tofu)
        br.close()


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    render(ids or [p.stem for p in sorted((HERE / "data").glob("*.json"))], pdf="--no-pdf" not in sys.argv)
