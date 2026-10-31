import json, pathlib, sys as _s
OUT = pathlib.Path(__file__).resolve().parent.parent / "data"
_s.path.insert(0, str(OUT.parent))
from roster4 import R4, N4, kingdom
from mk import S, K
_R = {r[0]: r for r in R4}
DOM = ("NE", "家养动物")
CULT = ("NE", "栽培植物")
def c4(id, en, latin, typ, hab, diet, note, iucn, sub, stats, skills, intro, fact, rng, src, foot, warn=None, iucn_cn=None, short=None, cn=None):
    r = _R[id]; cat = r[3]; cn = cn or r[1]
    d = dict(file=cn, no=f"{N4[id]:03d}", cat=cat, kingdom=kingdom(cat), name_cn=cn, name_en=en, latin=latin, short=short or cn, type=typ, habitat=hab,
             diet=diet, diet_note=note, iucn=dict(code=iucn, sub=sub, **({"cn": iucn_cn} if iucn_cn else {})), stats=stats, skills=skills, intro=intro,
             fact=fact, range=rng, sources=src, footnote=foot, **({"warn": warn} if warn else {}))
    assert len(cn) <= 11 and len(stats) == 4 and len(skills) == 2 and len(intro) in (2, 3), id
    (OUT / f"{id}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
WK = lambda t: f"Wikipedia「{t}」"
IU = lambda a, y: f"IUCN 红色名录（{a} {y}）"
