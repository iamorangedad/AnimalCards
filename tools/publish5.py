import json, shutil, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent; R = pathlib.Path("/tmp/animalcards")
def king(d): return d.get("kingdom", "动物")
ids = set(sys.argv[1:])
for p in (HERE / "data").glob("*.json"):
    if p.stem not in ids: continue
    d = json.loads(p.read_text()); dst = R / king(d) / d["cat"]; dst.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "pdf"): shutil.copy(HERE / "out" / f"{d['file']}.{ext}", dst / f"{d['file']}.{ext}")
    shutil.copy(p, R / "tools" / "data" / p.name)
t = R / "tools"
for f in ("card.html.j2", "render_card.py", "art.py", "art2.py", "art3.py", "art4.py", "art5.py", "art6.py", "icons.py", "iso.py", "preview.py", "preview5.py", "sheet.py",
          "roster.py", "roster2.py", "roster4.py", "roster5.py", "fetch4.py", "fetch5.py", "fetchzh.py", "dig5.py", "fx.py", "ibox.py", "publish5.py"):
    if (HERE / f).exists(): shutil.copy(HERE / f, t / f)
for p in (HERE / "cards").glob("*.py"): shutil.copy(p, t / "cards" / p.name)
n = sum(1 for _ in (t / "data").glob("*.json")); print("published", len(ids), "total data", n)
