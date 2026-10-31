"""生成卡片缩略图（WebP）：thumbs/{id}_400.webp（宽 400，面板预览）和 thumbs/{id}_120.webp（120×120，取插画区域，做标注头像）。
读取仓库 动物/<类别>/<名称>.png，不复制原图。用法: python build_thumbs.py [--force]"""
import json, os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); WEB = os.path.join(HERE, ".."); ROOT = os.path.join(WEB, "..")
OUT = os.path.join(WEB, "thumbs"); os.makedirs(OUT, exist_ok=True)
force = "--force" in sys.argv
A = json.load(open(os.path.join(WEB, "data", "animals.json"), encoding="utf-8"))["animals"]
n = 0
for a in A:
    t400 = os.path.join(OUT, f"{a['id']}_400.webp"); t120 = os.path.join(OUT, f"{a['id']}_120.webp")
    if not force and os.path.exists(t400) and os.path.exists(t120): continue
    im = Image.open(os.path.join(ROOT, a["card_png"])).convert("RGB")
    w, h = im.size
    im.resize((400, round(h * 400 / w)), Image.LANCZOS).save(t400, "WEBP", quality=78, method=6)
    cx, cy, r = w * 0.5, h * 0.305, w * 0.27   # 插画区域（卡片上部）
    im.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((120, 120), Image.LANCZOS).save(t120, "WEBP", quality=80, method=6)
    n += 1
print("generated", n, "of", len(A))
