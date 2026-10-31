import sys, json, time, subprocess, pathlib
from PIL import Image
ids = sys.argv[2:]; tag = sys.argv[1]
fs = [json.load(open(f"data/{i}.json"))["file"] for i in ids]
W, H, cols = 432, 768, 5
rows = (len(fs) + cols - 1) // cols
im = Image.new("RGB", (cols * (W + 10) + 10, rows * (H + 10) + 10), "white")
for j, f in enumerate(fs):
    im.paste(Image.open(f"out/{f}.png").resize((W, H), Image.LANCZOS), (10 + (j % cols) * (W + 10), 10 + (j // cols) * (H + 10)))
    pg = subprocess.run(["pdfinfo", f"out/{f}.pdf"], capture_output=True, text=True).stdout
    n = [l for l in pg.splitlines() if l.startswith("Pages")][0].split()[-1]
    if n != "1": print("PDF PAGES", f, n)
p = f"/tmp/ac_contact_{tag}_{int(time.time())}.png"; im.save(p); print(p)
