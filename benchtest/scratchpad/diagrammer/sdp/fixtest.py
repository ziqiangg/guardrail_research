import os
from playwright.sync_api import sync_playwright
base = os.path.abspath("benchtest/diagrams")
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for f in ("sentinel-explained.html", "sdp-explained.html"):
        ctx = b.new_context(viewport={"width": 375, "height": 800}, color_scheme="light")
        pg = ctx.new_page(); pg.goto("file:///" + (base + "/" + f).replace("\\", "/")); pg.wait_for_timeout(300)
        pg.add_style_tag(content=".wrap > * { min-width: 0; }")
        print(f, "with min-width:0 fix:", pg.evaluate("document.documentElement.scrollWidth"))
        ctx.close()
    b.close()
