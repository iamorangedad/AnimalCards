"""AnimalCards Globe 后端（FastAPI）。
- 提供前端静态页面、/api/animals、/api/animals/{id}、/api/meta、/healthz
- /cards/... 直接读取仓库里的 动物/ 文件夹（PNG/PDF，不复制）
- /thumbs/... 预生成的 WebP 缩略图
环境变量见 .env.example。"""
import json, os, time
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

WEBAPP = Path(os.environ.get("WEBAPP_DIR", Path(__file__).resolve().parent.parent))
REPO = Path(os.environ.get("ANIMALCARDS_ROOT", WEBAPP.parent))
CARDS_DIR = Path(os.environ.get("CARDS_DIR", REPO / "动物"))
DATA_FILE = Path(os.environ.get("DATA_FILE", WEBAPP / "data" / "animals.json"))
THUMBS_DIR = Path(os.environ.get("THUMBS_DIR", WEBAPP / "thumbs"))
FRONTEND = WEBAPP / "frontend"
STATIC_MAX_AGE = int(os.environ.get("STATIC_MAX_AGE", 7 * 24 * 3600))
API_MAX_AGE = int(os.environ.get("API_MAX_AGE", 300))

from urllib.parse import quote
def _enc(p: str) -> str:
    return "/".join(quote(x) for x in p.split("/"))

def load_data():
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    items = []
    for a in raw["animals"]:
        a = dict(a)
        a["card_png_url"] = "/cards/" + _enc(a["card_png"].removeprefix("动物/"))
        a["card_pdf_url"] = "/cards/" + _enc(a["card_pdf"].removeprefix("动物/"))
        a["thumb_url"] = "/" + a["thumb"]; a["avatar_url"] = "/" + a["avatar"]
        items.append(a)
    return raw["meta"], items, {a["id"]: a for a in items}

META, ITEMS, BY_ID = load_data()
STARTED = time.time()
app = FastAPI(title="AnimalCards Globe", version="1.0", docs_url="/api/docs", openapi_url="/api/openapi.json")
app.add_middleware(GZipMiddleware, minimum_size=800)

@app.middleware("http")
async def cache_headers(request: Request, call_next):
    resp = await call_next(request)
    p = request.url.path
    if p.startswith(("/cards/", "/thumbs/", "/vendor/", "/img/")):
        resp.headers.setdefault("Cache-Control", f"public, max-age={STATIC_MAX_AGE}")
    elif p.startswith("/api/"):
        resp.headers.setdefault("Cache-Control", f"public, max-age={API_MAX_AGE}")
    elif p in ("/", "/index.html") or p.endswith((".js", ".css")):
        resp.headers.setdefault("Cache-Control", "no-cache")
    resp.headers.setdefault("X-Content-Type-Options", "nosniff")
    return resp

def _in_bbox(a, bbox):
    w, s, e, n = bbox
    for l in a["locations"]:
        lon_ok = (w <= l["lon"] <= e) if w <= e else (l["lon"] >= w or l["lon"] <= e)  # 支持跨日界线
        if lon_ok and s <= l["lat"] <= n: return True
    return False

@app.get("/healthz")
def healthz():
    ok = CARDS_DIR.is_dir() and THUMBS_DIR.is_dir()
    return JSONResponse({"status": "ok" if ok else "degraded", "animals": len(ITEMS), "cards_dir": CARDS_DIR.is_dir(),
                         "thumbs_dir": THUMBS_DIR.is_dir(), "uptime_s": round(time.time() - STARTED)}, status_code=200 if ok else 503,
                        headers={"Cache-Control": "no-store"})

@app.get("/api/meta")
def meta():
    cats = {}; iucn = {}
    for a in ITEMS:
        cats[a["category"]] = cats.get(a["category"], 0) + 1; iucn[a["iucn"]] = iucn.get(a["iucn"], 0) + 1
    return {**META, "category_counts": cats, "iucn_counts": iucn}

@app.get("/api/animals")
def animals(category: Optional[str] = Query(None, description="类别，多个用逗号分隔"),
            iucn: Optional[str] = Query(None, description="IUCN 代码，多个用逗号分隔，如 CR,EN"),
            q: Optional[str] = Query(None, description="按名称搜索（中/英/学名/id）"),
            bbox: Optional[str] = Query(None, description="minLon,minLat,maxLon,maxLat"),
            limit: int = Query(1000, ge=1, le=1000), offset: int = Query(0, ge=0)):
    res = ITEMS
    if category: cs = set(category.split(",")); res = [a for a in res if a["category"] in cs]
    if iucn: ic = set(x.upper() for x in iucn.split(",")); res = [a for a in res if a["iucn"] in ic]
    if q:
        t = q.strip().lower().replace(" ", "")
        res = [a for a in res if any(t in (a.get(k) or "").lower().replace(" ", "") for k in ("name_zh", "name_en", "latin", "id"))]
    if bbox:
        try:
            bb = [float(x) for x in bbox.split(",")]; assert len(bb) == 4
        except Exception:
            raise HTTPException(400, "bbox 格式应为 minLon,minLat,maxLon,maxLat")
        res = [a for a in res if _in_bbox(a, bb)]
    return {"count": len(res), "offset": offset, "items": res[offset:offset + limit]}

@app.get("/api/animals/{aid}")
def animal(aid: str):
    a = BY_ID.get(aid)
    if not a: raise HTTPException(404, "没有这个动物")
    return a

app.mount("/cards", StaticFiles(directory=CARDS_DIR, check_dir=False), name="cards")
app.mount("/thumbs", StaticFiles(directory=THUMBS_DIR, check_dir=False), name="thumbs")
app.mount("/data", StaticFiles(directory=WEBAPP / "data"), name="data")
app.mount("/", StaticFiles(directory=FRONTEND, html=True), name="frontend")
