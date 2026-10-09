import os, sys
from playwright.sync_api import sync_playwright
base = os.path.abspath("benchtest/diagrams")
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for f in ("sentinel-explained.html", "sdp-explained.html"):
        ctx = b.new_context(viewport={"width": 375, "height": 800}, color_scheme="light")
        pg = ctx.new_page(); pg.goto("file:///" + (base + "/" + f).replace("\\", "/")); pg.wait_for_timeout(400)
        print(f, pg.evaluate("document.documentElement.scrollWidth"))
        res = pg.evaluate("""() => { const out=[]; document.querySelectorAll('body *').forEach(el => { const r = el.getBoundingClientRect(); if (r.right > window.innerWidth + 1) { let anc = el.parentElement, inScroll=false; while (anc) { const cs = getComputedStyle(anc); if (['FIGURE'].includes(anc.tagName) || anc.classList.contains('tablewrap')) { inScroll = true; break; } anc = anc.parentElement; } if (!inScroll) out.push(el.tagName + '.' + el.className + ' ' + Math.round(r.right)); } }); return out.slice(0,15); }""")
        print(res)
        ctx.close()
    b.close()
