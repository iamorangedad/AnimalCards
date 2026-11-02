import json, urllib.parse, urllib.request, time, pathlib, sys
from roster5 import R5 as R4
UA={"User-Agent":"AnimalCards/1.0 (iamorangedad@users.noreply.github.com)"}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))
out=pathlib.Path("src5"); out.mkdir(exist_ok=True)
for i,cn,t,c,n in R4:
    if (out/f"{i}.wiki").exists() and (out/f"{i}.txt").stat().st_size>500: continue
    q=urllib.parse.quote(t)
    for k in range(3):
        try:
            a=get(f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&redirects=1&format=json&titles={q}")
            pg=next(iter(a["query"]["pages"].values())); (out/f"{i}.txt").write_text(pg.get("extract",""))
            b=get(f"https://en.wikipedia.org/w/api.php?action=parse&prop=wikitext&redirects=1&format=json&page={q}")
            (out/f"{i}.wiki").write_text(b["parse"]["wikitext"]["*"]); (out/f"{i}.title").write_text(pg.get("title",""))
            print(i, pg.get("title"), len(pg.get("extract","")), flush=True); break
        except Exception as e: print("ERR",i,e, flush=True); time.sleep(3)
    time.sleep(0.2)
