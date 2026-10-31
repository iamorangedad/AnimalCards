"""用 Playwright（Chromium）打开页面并截图，收集控制台错误。
用法: python tests/screenshots.py http://127.0.0.1:8000 输出目录 [chromium 路径]"""
import sys, json, time
from playwright.sync_api import sync_playwright
base, out = sys.argv[1].rstrip("/"), sys.argv[2]
exe = sys.argv[3] if len(sys.argv) > 3 else None
errors = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe, args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    def page(vp, mobile=False):
        ctx = b.new_context(viewport=vp, device_scale_factor=1, is_mobile=mobile, has_touch=mobile)
        pg = ctx.new_page()
        pg.on("console", lambda m: m.type in ("error", "warning") and errors.append(f"[{m.type}] {m.text}"))
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("requestfailed", lambda r: errors.append(f"[requestfailed] {r.url}"))
        return pg
    pg = page({"width": 1440, "height": 900})
    pg.goto(base + "/", wait_until="networkidle"); pg.wait_for_function("window.__app && document.querySelector('#loading').classList.contains('done')", timeout=60000)
    time.sleep(4); pg.screenshot(path=f"{out}/01_globe.png")
    n = pg.evaluate("document.querySelectorAll('.cl,.mk').length"); print("elements on globe:", n)
    # 放大到非洲，展开标注
    pg.evaluate("__app.world.controls().autoRotate=false; void __app.world.pointOfView({lat:-2,lng:30,altitude:0.5},0)"); time.sleep(2.5)
    pg.screenshot(path=f"{out}/02_zoom_africa.png")
    # 点击一个可见的单个标注
    mk = pg.evaluate("""(() => { const els=[...document.querySelectorAll('.mk')].filter(e=>getComputedStyle(e).opacity!=='0');
        const r=els.map(e=>e.getBoundingClientRect()).find(r=>r.x>300&&r.x<1000&&r.y>150&&r.y<800); return r?[r.x+r.width/2,r.y+r.height/2]:null })()""")
    print("marker at", mk)
    if mk: pg.mouse.move(*mk); time.sleep(.5); pg.screenshot(path=f"{out}/03_hover.png"); pg.mouse.click(*mk)
    time.sleep(2); pg.screenshot(path=f"{out}/04_marker_click_panel.png")
    print("panel:", pg.evaluate("document.querySelector('#panel').hidden ? 'hidden' : document.querySelector('.p-name')?.textContent"))
    # 搜索
    pg.click("#panelClose"); pg.fill("#q", "雪豹"); time.sleep(.6); pg.screenshot(path=f"{out}/05_search_suggest.png")
    pg.keyboard.press("Enter"); time.sleep(3); pg.screenshot(path=f"{out}/06_search_flyto.png")
    # 筛选：只看海洋（shift 点击）+ IUCN
    pg.click("#panelClose"); pg.evaluate("void __app.world.pointOfView({lat:10,lng:150,altitude:2.2},0)")
    pg.click("[data-cat='海洋']", modifiers=["Shift"]); time.sleep(.3); pg.click("[data-iucn='LC']"); time.sleep(2)
    pg.screenshot(path=f"{out}/07_filter_ocean.png"); print("shown:", pg.inner_text("#shown"))
    # 灯箱（高清 PNG）
    pg.click("#resetBtn"); time.sleep(1); pg.evaluate("void __app.flyTo(__app.state.byId['giant-panda'])"); time.sleep(3)
    pg.click("#pCard"); time.sleep(2.5); pg.screenshot(path=f"{out}/08_lightbox_png.png"); pg.click("#lbClose")
    # 同地点列表
    pg.click("#panelClose"); pg.evaluate("void __app.world.pointOfView({lat:0,lng:22,altitude:0.45},0)"); time.sleep(2)
    c = pg.evaluate("""(() => { const els=[...document.querySelectorAll('.cl')].filter(e=>getComputedStyle(e).opacity!=='0'); const r=els.map(e=>e.getBoundingClientRect()).find(r=>r.x>320&&r.x<900&&r.y>120&&r.y<800); return r?[r.x+r.width/2,r.y+r.height/2]:null })()""")
    if c: pg.mouse.click(*c); time.sleep(1.2); pg.screenshot(path=f"{out}/09_cluster_list.png"); print("list panel:", pg.evaluate("document.querySelector('#panelBody').innerText.slice(0,60)"))
    # 手机
    m = page({"width": 390, "height": 844}, mobile=True)
    m.goto(base + "/#a=snow-leopard", wait_until="networkidle"); m.wait_for_function("window.__app", timeout=60000); time.sleep(4)
    m.screenshot(path=f"{out}/10_mobile_panel.png")
    m.click("#panelClose"); time.sleep(.5); m.click("#filterToggle"); time.sleep(1); m.screenshot(path=f"{out}/11_mobile_filters.png")
    b.close()
print("console errors/warnings:", len(errors))
for e in errors[:40]: print(" ", e)
