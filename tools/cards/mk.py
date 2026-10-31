import json, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "data"
def S(label, value, lo, hi=None, scale="mass", approx=False):
    return dict(label=label, value=value, lo=lo, hi=lo if hi is None else hi, scale=scale, approx=approx)
def K(name, icon, desc):
    return dict(name=name, icon=icon, desc=desc)
def card(id, no, cat, cn, en, latin, typ, hab, diet, note, iucn, sub, stats, skills, intro, fact, rng, src, foot, iucn_cn=None):
    d = dict(file=cn, no=f"{no:03d}", cat=cat, name_cn=cn, name_en=en, latin=latin, short=cn, type=typ, habitat=hab, diet=diet, diet_note=note,
             iucn=dict(code=iucn, sub=sub, **({"cn": iucn_cn} if iucn_cn else {})), stats=stats, skills=skills, intro=intro, fact=fact, range=rng,
             sources=src, footnote=foot)
    assert len(cn) <= 11 and len(stats) == 4 and len(skills) == 2, id
    (OUT / f"{id}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
DOM = dict(iucn="NE", sub="家养动物", iucn_cn="未评估")
import sys as _s; _s.path.insert(0, str(OUT.parent))
from roster2 import R3 as _R3
N3 = {r[0]: 106 + k for k, r in enumerate(_R3)}
def c3(id, *a, **k):
    cat = next(r[3] for r in _R3 if r[0] == id)
    return card(id, N3[id], cat, *a, **k)
NE = ("NE", "家养动物")
