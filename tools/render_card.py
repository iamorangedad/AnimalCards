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
SCALES = {"mass": ("log", 0.1, 10000, [1, 10, 100, 1000]), "len": ("log", 0.1, 10, [1]), "life": ("lin", 0, 80, [20, 40, 60]),
          "hours": ("lin", 0, 24, [6, 12, 18]), "depth": ("lin", 0, 600, [200, 400]), "speed": ("lin", 0, 120, [30, 60, 90]),
          "food": ("lin", 0, 200, [50, 100, 150])}
NOTE = "条长：体重 0.1 kg–10 t、体长 10 cm–10 m 为对数刻度；寿命 0–80 年等为线性刻度。条纹段 = 数据范围。"


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
                                                          art=Markup(art.ART[i](ART_W, ART_H)), stats=[bar(s) for s in d["stats"]], scale_note=NOTE)
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
