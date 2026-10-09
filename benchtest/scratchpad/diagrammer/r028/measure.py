"""R028 measurement: python measure.py <tag> ; writes <tag>_<page>.json and <tag>_summary.json; screenshots to /tmp (not committed)."""
import json, os, sys
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.abspath(os.path.join(HERE, "..", "..", "..", "diagrams"))
PAGES = ["nemo-rails", "llama-guard", "sentinel", "presidio", "sdp", "modelarmor"]
tag = sys.argv[1]
shots = tag == "after"
BOXES = r"""() => [...document.querySelectorAll('body, body *')].map((e,i) => {
  const r = e.getBoundingClientRect();
  return [i, e.tagName, e.id||'', (e.getAttribute('class')||'').toString(), +r.x.toFixed(2), +(r.y+scrollY).toFixed(2), +r.width.toFixed(2), +r.height.toFixed(2)];
})"""
CLIP = r"""() => { const out=[];
 document.querySelectorAll('svg').forEach((svg,si)=>{ const vb=svg.viewBox.baseVal;
  svg.querySelectorAll('text').forEach(t=>{ const b=t.getBBox();
   if (b.x<0||b.x+b.width>vb.width||b.y<0||b.y+b.height>vb.height) out.push([si,t.textContent,Math.round(b.x),Math.round(b.x+b.width),vb.width]);
   const cx=b.x+b.width/2, cy=b.y+b.height/2; let best=null;
   svg.querySelectorAll('rect').forEach(r=>{const q=r.getBBox(); if(cx>=q.x&&cx<=q.x+q.width&&cy>=q.y&&cy<=q.y+q.height&&!(r.getAttribute('class')||'').includes('zone')){ if(!best||q.width*q.height<best.w*best.h) best={x:q.x,w:q.width,h:q.height};}});
   if (best && (b.x<best.x+3 || b.x+b.width>best.x+best.w-3)) out.push([si,'rectclip:'+t.textContent,Math.round(b.x),Math.round(b.x+b.width),Math.round(best.x),Math.round(best.x+best.w)]);
  });}); return out; }"""
summary = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for pg in PAGES:
        url = "file:///" + os.path.join(D, pg + "-explained.html").replace("\\", "/")
        for scheme in ("light", "dark"):
            for w in (1280, 375):
                if scheme == "dark" and tag == "before": continue
                ctx = b.new_context(color_scheme=scheme, viewport={"width": w, "height": 900})
                page = ctx.new_page(); page.goto(url); page.wait_for_load_state("networkidle"); page.wait_for_timeout(400)
                sw = page.evaluate("document.documentElement.scrollWidth"); iw = page.evaluate("window.innerWidth")
                clip = page.evaluate(CLIP)
                summary[f"{pg}|{scheme}|{w}"] = {"scrollW": sw, "innerW": iw, "svg_text_issues": len(clip)}
                if w == 1280 and scheme == "light":
                    json.dump(page.evaluate(BOXES), open(os.path.join(HERE, f"{tag}_{pg}_1280_boxes.json"), "w"))
                if shots:
                    page.screenshot(path=f"/tmp/r028_{pg}_{scheme}_{w}.png", full_page=True)
                ctx.close()
    b.close()
json.dump(summary, open(os.path.join(HERE, f"{tag}_summary.json"), "w"), indent=1)
for k, v in summary.items(): print(k, v)
