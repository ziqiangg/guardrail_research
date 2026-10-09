import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[4]
page_path = root/'benchtest'/'diagrams'/'modelarmor-explained.html'
out = pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    b = p.chromium.launch()
    for scheme in ['light', 'dark']:
        ctx = b.new_context(viewport={'width': 1280, 'height': 900}, color_scheme=scheme)
        pg = ctx.new_page(); pg.goto(page_path.as_uri()); pg.wait_for_timeout(1200)
        for i, f in enumerate(pg.query_selector_all('figure')):
            f.screenshot(path=str(out/f'fig_{scheme}_{i:02d}.png'))
        for i, t in enumerate(pg.query_selector_all('.tablewrap')):
            t.screenshot(path=str(out/f'tab_{scheme}_{i:02d}.png'))
        ctx.close()
    ctx = b.new_context(viewport={'width': 375, 'height': 800}, color_scheme='dark')
    pg = ctx.new_page(); pg.goto(page_path.as_uri()); pg.wait_for_timeout(1200)
    pg.screenshot(path=str(out/'phone_top_dark.png'))
    b.close()
