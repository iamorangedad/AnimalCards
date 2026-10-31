import json, urllib.parse, urllib.request, sys, pathlib, re
UA = {"User-Agent": "AnimalCards/1.0 (iamorangedad@users.noreply.github.com)"}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30))
for i in sys.argv[1:]:
    t = pathlib.Path(f"src4/{i}.title").read_text().strip()
    a = get(f"https://en.wikipedia.org/w/api.php?action=query&prop=langlinks&lllang=zh&format=json&titles={urllib.parse.quote(t)}")
    pg = next(iter(a["query"]["pages"].values())); ll = pg.get("langlinks")
    if not ll: print(i, "no zh"); continue
    zt = ll[0]["*"]
    b = get(f"https://zh.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&redirects=1&format=json&variant=zh-cn&titles={urllib.parse.quote(zt)}")
    x = next(iter(b["query"]["pages"].values())).get("extract", "")
    pathlib.Path(f"src4/{i}.zh.txt").write_text(x); print(i, zt, len(x))
