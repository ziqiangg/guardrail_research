import sys, pathlib, json
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[4]
page_path = root/'benchtest'/'diagrams'/'sdp-explained.html'
out = pathlib.Path(__file__).resolve().parent
JS = r"""() => {
 const res = {sw: document.documentElement.scrollWidth, iw: window.innerWidth, fonts: document.fonts.status};
 // text overflow: each svg text inside the nearest preceding rect it sits in
 const issues = [];
 document.querySelectorAll('svg').forEach((svg, si) => {
   const rects = [...svg.querySelectorAll('rect')].map(r => r.getBBox());
   svg.querySelectorAll('text').forEach(t => {
     const b = t.getBBox(); const cx = b.x + b.width/2, cy = b.y + b.height/2;
     const host = rects.filter(r => cx>=r.x && cx<=r.x+r.width && cy>=r.y && cy<=r.y+r.height)
                       .sort((a,b)=>a.width*a.height-b.width*b.height)[0];
     if (host && (b.x < host.x-0.5 || b.x+b.width > host.x+host.width+0.5)) issues.push({svg: si, text: t.textContent, over: [Math.round(host.x-b.x), Math.round(b.x+b.width-host.x-host.width)]});
     const vb = svg.viewBox.baseVal; if (b.x < vb.x || b.x+b.width > vb.x+vb.width) issues.push({svg: si, text: t.textContent, outside_viewbox: true});
   });
 });
 res.issues = issues;
 const wide = [];
 document.querySelectorAll('body *').forEach(e => { const r = e.getBoundingClientRect(); if (r.right > window.innerWidth + 1 && !e.closest('figure') && !e.closest('.tablewrap')) wide.push(e.tagName + '.' + e.className + ' ' + Math.round(r.right)); });
 res.wide = wide.slice(0, 15);
 return res; }"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for scheme in ['light', 'dark']:
        for w in [1280, 375]:
            ctx = b.new_context(viewport={'width': w, 'height': 900}, color_scheme=scheme)
            pg = ctx.new_page(); pg.goto(page_path.as_uri()); pg.wait_for_timeout(1500)
            r = pg.evaluate(JS)
            print(scheme, w, json.dumps(r, ensure_ascii=False))
            pg.screenshot(path=str(out/f'sdp_{scheme}_{w}.png'), full_page=True)
            ctx.close()
    b.close()
