import json, pathlib, sys as _s
OUT = pathlib.Path(__file__).resolve().parent.parent / "data"
_s.path.insert(0, str(OUT.parent))
from roster5 import R5 as R4, N5 as N4, kingdom
from mk import S, K
_R = {r[0]: r for r in R4}
DOM = ("NE", "家养动物")
CULT = ("NE", "栽培植物")
import re as _re, unicodedata as _u
def _w(s): return sum(2 if _u.east_asian_width(c) in 'WF' else 1 for c in s)
BAD = []
def c5(id, en, latin, typ, hab, diet, note, iucn, sub, stats, skills, intro, fact, rng, src, foot, warn=None, iucn_cn=None, short=None, cn=None):
    m = _re.match(r"IUCN 红色名录（(.+) (\d{4})）$", sub)
    if m:
        sub = f"IUCN {m.group(2)}"; s_ = IU(m.group(1), m.group(2))
        if s_ not in src: src = list(src) + [s_]
    sub = {"维基百科未列 IUCN 评估（待核）": "未见评估（待核）", "亚种未单独评估": "亚种未单独评估"}.get(sub, sub)
    if sub.startswith("维基百科列 NatureServe"): sub = "未见评估（待核）"
    for st in stats:
        if _w(st["label"]) > 11: BAD.append((id, "label", st["label"]))
        if _w(st["value"]) > 18: BAD.append((id, "value", st["value"]))
    for k in skills:
        if _w(k["name"]) > 16: BAD.append((id, "skill", k["name"]))
    if _w(sub) > 16: BAD.append((id, "sub", sub))
    r = _R[id]; cat = r[3]; cn = cn or r[1]
    d = dict(file=cn, no=f"{N4[id]:03d}", cat=cat, kingdom=kingdom(cat), name_cn=cn, name_en=en, latin=latin, short=short or cn, type=typ, habitat=hab,
             diet=diet, diet_note=note, iucn=dict(code=iucn, sub=sub, **({"cn": iucn_cn} if iucn_cn else {})), stats=stats, skills=skills, intro=intro,
             fact=fact, range=rng, sources=src, footnote=foot, **({"warn": warn} if warn else {}))
    assert len(cn) <= 11 and len(stats) == 4 and len(skills) == 2 and len(intro) in (2, 3), id
    (OUT / f"{id}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
WK = lambda t: f"Wikipedia「{t}」"
IU = lambda a, y: f"IUCN 红色名录（{a} {y}）"

import atexit as _ax
_ax.register(lambda: BAD and print("TOO LONG:", *BAD, sep="\n  "))
