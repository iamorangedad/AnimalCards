"""检查 API 返回 400 种动物，且每个卡片 PNG / PDF / 缩略图 URL 都能访问（HEAD 200）。
用法: python tests/check_urls.py [http://127.0.0.1:8000]"""
import json, sys, urllib.request, concurrent.futures as cf
base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000").rstrip("/")
d = json.load(urllib.request.urlopen(base + "/api/animals?limit=1000"))
items = d["items"]; print("animals:", d["count"])
urls = [base + a[k] for a in items for k in ("card_png_url", "card_pdf_url", "thumb_url", "avatar_url")]
def head(u):
    try: return urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=20).status
    except Exception as e: return str(e)
bad = []
with cf.ThreadPoolExecutor(16) as ex:
    for u, s in zip(urls, ex.map(head, urls)):
        if s != 200: bad.append((u, s))
nloc = sum(len(a["locations"]) for a in items)
print("urls checked:", len(urls), "bad:", len(bad), "| animals with markers:", sum(1 for a in items if a["locations"]), "markers:", nloc)
for b in bad[:20]: print("BAD", b)
assert d["count"] == 400 and not bad
print("OK")
