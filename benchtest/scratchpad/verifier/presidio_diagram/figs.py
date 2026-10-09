from playwright.sync_api import sync_playwright
ROOT = "C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research"
OUT = ROOT + "/benchtest/scratchpad/verifier/presidio_diagram/"
src = open(ROOT + "/benchtest/diagrams/presidio-explained.html", encoding="utf-8").read()
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for scheme in ("dark", "light"):
        ctx = b.new_context(color_scheme=scheme, viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
        pg.set_content(src, wait_until="networkidle"); pg.wait_for_timeout(300)
        for i, f in enumerate(pg.query_selector_all("figure svg")):
            f.screenshot(path=OUT + f"fig_{scheme}_{i:02d}.png")
        ctx.close()
    ctx = b.new_context(color_scheme="light", viewport={"width": 375, "height": 1400}); pg = ctx.new_page()
    pg.set_content(src, wait_until="networkidle"); pg.wait_for_timeout(300)
    pg.screenshot(path=OUT + "phone_top.png")
    ctx.close(); b.close()
