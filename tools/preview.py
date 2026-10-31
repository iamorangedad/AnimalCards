import sys, importlib, pathlib
from playwright.sync_api import sync_playwright
import art
importlib.reload(art)
W, H = 940, 600
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/usr/bin/google-chrome"); p = b.new_page(viewport={"width": W, "height": H})
    for k in sys.argv[1:]:
        html = f'<html><body style="margin:0;background:#fff;background-image:linear-gradient(rgba(31,35,40,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(31,35,40,.06) 1px,transparent 1px);background-size:24px 24px">{art.ART[k](W, H)}</body></html>'
        p.set_content(html); p.screenshot(path=f"/tmp/ac_{k}.png")
    b.close()
