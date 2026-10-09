import pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(__file__).resolve().parents[4]
page_path = root/'benchtest'/'diagrams'/'lionguard-explained.html'
out = pathlib.Path(__file__).resolve().parent
JS = r"""() => { const res=[]; document.querySelectorAll('svg').forEach((svg,si)=>{ const ts=[...svg.querySelectorAll('text')].map(t=>({t:t.textContent,b:t.getBBox()})); for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){const a=ts[i].b,b=ts[j].b; if(a.x<b.x+b.width&&b.x<a.x+a.width&&a.y<b.y+b.height&&b.y<a.y+a.height) res.push([si,ts[i].t,ts[j].t]);} }); return res; }"""
with sync_playwright() as p:
    b = p.chromium.launch()
    for scheme in ['light','dark']:
        ctx = b.new_context(viewport={'width':1280,'height':900}, color_scheme=scheme, device_scale_factor=1)
        pg = ctx.new_page(); pg.goto(page_path.as_uri()); pg.wait_for_timeout(1500)
        if scheme=='light': print('text overlaps', pg.evaluate(JS))
        for i,f in enumerate(pg.query_selector_all('figure')):
            f.screenshot(path=str(out/f'fig{i}_{scheme}.png'))
        for i,t in enumerate(pg.query_selector_all('.tablewrap')):
            t.screenshot(path=str(out/f'table{i}_{scheme}.png'))
        ctx.close()
    ctx = b.new_context(viewport={'width':375,'height':900}, color_scheme='dark'); pg=ctx.new_page(); pg.goto(page_path.as_uri()); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(out/'phone_dark_top.png'))
    b.close()
