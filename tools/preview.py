import sys, importlib, pathlib
from playwright.sync_api import sync_playwright
import art
importlib.reload(art)
W, H = 940, 600
FIT = open('card.html.j2').read().split('<script>')[1].split('</script>')[0]
FIT = '<script>' + FIT + '</script>'
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/usr/bin/google-chrome"); p = b.new_page(viewport={"width": W, "height": H})
    for k in sys.argv[1:]:
        html = f'<html><body style="margin:0;background:#fff;background-image:linear-gradient(rgba(31,35,40,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(31,35,40,.06) 1px,transparent 1px);background-size:24px 24px">{art.ART[k](W, H)}'+FIT+'</body></html>'
        p.set_content(html); p.screenshot(path=f"/tmp/ac_{k}.png")
    if len(sys.argv) > 2:
        from PIL import Image
        ks = sys.argv[1:]; n = len(ks); cols = 3
        im = Image.new("RGB", (cols * 470, ((n + cols - 1) // cols) * 300), "white")
        for j, k in enumerate(ks): im.paste(Image.open(f"/tmp/ac_{k}.png").resize((470, 300)), ((j % cols) * 470, (j // cols) * 300))
        import time; pth = f"/tmp/ac_sheet_{int(time.time())}.png"; im.save(pth); print(pth)
    b.close()
