#!/usr/bin/env python3
"""Animal trading cards: data/<id>.json -> out/<id>.{html,png,pdf}. Art from art.py (ART[id](w, h))."""
import json, math, pathlib, subprocess, sys
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from playwright.sync_api import sync_playwright
import icons
import art

HERE = pathlib.Path(__file__).resolve().parent
W, H = 1080, 1920
ART_W, ART_H = 1080 - 2 * 22 - 2 * 16 - 2 * 30 - 4, 600
TYPE = {"陆地": ("#5f8f5a", "#e1efda"), "水中": ("#2f7de1", "#dceafb"), "天空": ("#3a9fc9", "#dcf1f9"), "两栖": ("#2a9d8f", "#d9f2ef")}
IUCN = {"EX": ("#000000", "#ffffff", "灭绝"), "EW": ("#542344", "#ffffff", "野外灭绝"), "CR": ("#d81e05", "#fde4e0", "极危"),
        "EN": ("#fc7f3f", "#fff0e6", "濒危"), "VU": ("#e0a800", "#fff7d6", "易危"), "NT": ("#9aa83b", "#f2f6dc", "近危"),
        "LC": ("#60c659", "#e6f7e4", "无危"), "DD": ("#6b7075", "#eeeeee", "数据缺乏"), "NE": ("#6b7075", "#ffffff", "未评估")}
SCALES = {"mass": ("log", 0.1, 10000, [1, 10, 100, 1000]), "mass_s": ("log", 1e-6, 10, [1e-3, 1]), "mass_xl": ("log", 1, 200000, [100, 10000]),
          "len": ("log", 0.1, 10, [1]), "len_s": ("log", 0.001, 1, [0.01, 0.1]), "len_xl": ("log", 1, 40, [10]),
          "life": ("lin", 0, 80, [20, 40, 60]), "life_xl": ("lin", 0, 200, [50, 100, 150]),
          "hours": ("lin", 0, 24, [6, 12, 18]), "depth": ("lin", 0, 600, [200, 400]), "depth_xl": ("lin", 0, 2000, [500, 1000, 1500]),
          "speed": ("lin", 0, 120, [30, 60, 90]), "food": ("lin", 0, 200, [50, 100, 150]), "days": ("lin", 0, 400, [100, 200, 300]),
          "alt": ("lin", 0, 6000, [2000, 4000]), "km": ("log", 1, 10000, [10, 100, 1000]), "temp": ("lin", 0, 50, [10, 20, 30, 40]), "n400": ("lin", 0, 400, [100, 200, 300]), "months": ("lin", 0, 24, [6, 12, 18]),
          "n100": ("lin", 0, 100, [25, 50, 75])}
SDESC = {"mass": "体重 0.1 kg–10 t（对数）", "mass_s": "体重 1 mg–10 kg（对数）", "mass_xl": "体重 1 kg–200 t（对数）",
         "len": "长度 10 cm–10 m（对数）", "len_s": "长度 1 mm–1 m（对数）", "len_xl": "长度 1–40 m（对数）",
         "life": "寿命 0–80 年", "life_xl": "寿命 0–200 年", "hours": "时长 0–24 小时", "depth": "水深 0–600 m", "depth_xl": "水深 0–2000 m",
         "speed": "速度 0–120 km/h", "food": "食量 0–200 kg", "days": "天数 0–400 天", "alt": "海拔 0–6000 m", "km": "距离 1–10000 km（对数）", "temp": "温度 0–50 °C", "n400": "数量 0–400", "months": "月数 0–24 个月", "n100": "数量 0–100"}


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
            if pdf:
                pg.pdf(path=str(out / f"{d['file']}.pdf"), width=f"{W}px", height=f"{H}px", print_background=True, page_ranges="1")
            print(i, info, "tofu", tofu)
        br.close()


if __name__ == "__main__":
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    render(ids or [p.stem for p in sorted((HERE / "data").glob("*.json"))], pdf="--no-pdf" not in sys.argv)
