import sys, os
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
name = sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    ctx = b.new_context(viewport={"width": 375, "height": 900})
    pg = ctx.new_page()
    pg.goto("file:///" + os.path.join(ROOT, "benchtest", "diagrams", name).replace("\\", "/"))
    pg.wait_for_load_state("networkidle")
    print(name, pg.evaluate("[document.documentElement.scrollWidth, innerWidth]"))
    res = pg.evaluate("""() => { const out=[]; document.querySelectorAll('body *').forEach(e=>{const r=e.getBoundingClientRect(); if(r.right>376 && !e.closest('figure') && !e.closest('.tablewrap')) out.push([e.tagName, e.className && e.className.baseVal===undefined ? e.className : '', Math.round(r.right), (e.textContent||'').slice(0,40)]);}); return out.slice(0,15);}""")
    for r in res: print(r)
    b.close()
