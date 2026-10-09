import os, json, sys
from playwright.sync_api import sync_playwright
ROOT = "C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research"
D = ROOT + "/benchtest/diagrams/"
OUT = ROOT + "/benchtest/scratchpad/verifier/presidio_diagram/"
FIXLINE = ".wrap > *, .stage > *, .grid2 > * { min-width: 0; }"
CLIP_JS = """() => {
  const bad = [];
  document.querySelectorAll('svg').forEach((s, si) => {
    const vb = s.viewBox.baseVal;
    s.querySelectorAll('text').forEach(t => {
      const bb = t.getBBox();
      if (bb.x < -1 || bb.x + bb.width > vb.width + 1 || bb.y < -1 || bb.y + bb.height > vb.height + 1)
        bad.push([si, 'outside-viewbox', t.textContent]);
      const cx = bb.x + bb.width/2, cy = bb.y + bb.height/2;
      let best = null, area = 1e9;
      s.querySelectorAll('rect').forEach(r => {
        if (r.classList.contains('zone')) return;
        const x=+r.getAttribute('x'), y=+r.getAttribute('y'), w=+r.getAttribute('width'), h=+r.getAttribute('height');
        if (cx>=x && cx<=x+w && cy>=y && cy<=y+h && w*h<area) { best=[x,y,w,h]; area=w*h; }
      });
      if (best && (bb.x < best[0]+3 || bb.x+bb.width > best[0]+best[2]-3 || bb.y < best[1]+1 || bb.y+bb.height > best[1]+best[3]-1))
        bad.push([si, 'tight/clipped', t.textContent, Math.round(bb.x), Math.round(bb.width), best]);
    });
  });
  return bad;
}"""
OVER_JS = """() => { const out=[]; document.querySelectorAll('.wrap *').forEach(el => { const r = el.getBoundingClientRect(); if (r.right > window.innerWidth + 1) { let a = el, inS=false; while (a) { if (a.tagName==='FIGURE' || (a.classList && a.classList.contains('tablewrap'))) { inS=true; break; } a=a.parentElement; } if (!inS) out.push(el.tagName+'.'+el.className+' right='+Math.round(r.right)); } }); return out.slice(0,12); }"""
RECTS_JS = """() => Array.from(document.querySelectorAll('.wrap *')).map(e => { const r=e.getBoundingClientRect(); return [Math.round(r.x),Math.round(r.y),Math.round(r.width),Math.round(r.height)]; })"""
def load(page, html, wrap):
    if wrap:
        html = '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>' + html + '</body></html>'
    page.set_content(html, wait_until="networkidle")
    page.wait_for_timeout(400)
res = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    src = open(D + "presidio-explained.html", encoding="utf-8").read()
    assert FIXLINE in src
    nofix = src.replace(FIXLINE, "")
    for scheme in ("light", "dark"):
        for w in (1280, 375):
            for wrap in (False, True):
                ctx = b.new_context(color_scheme=scheme, viewport={"width": w, "height": 900})
                pg = ctx.new_page(); msgs=[]; pg.on("console", lambda m: msgs.append(m.text)); pg.on("pageerror", lambda e: msgs.append(str(e)))
                load(pg, src, wrap)
                sw = pg.evaluate("[document.documentElement.scrollWidth, window.innerWidth, document.compatMode]")
                clip = pg.evaluate(CLIP_JS)
                over = pg.evaluate(OVER_JS)
                bg = pg.evaluate("getComputedStyle(document.body).backgroundColor")
                print(scheme, w, "wrapped" if wrap else "fragment", "scroll", sw, "bg", bg, "over", over, "clip", json.dumps(clip)[:900], "console", msgs[:3])
                if not wrap:
                    pg.screenshot(path=OUT + f"presidio_{scheme}_{w}.png", full_page=True)
                    r_fix = pg.evaluate(RECTS_JS)
                    load(pg, nofix, False)
                    sw2 = pg.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
                    r_nofix = pg.evaluate(RECTS_JS)
                    ndiff = sum(1 for a, c in zip(r_fix, r_nofix) if a != c)
                    print("   without min-width addition: scroll", sw2, "elements whose box changes:", ndiff, "of", len(r_fix))
                ctx.close()
    # reference pages at 375
    for f in ("sentinel-explained.html", "llama-guard-explained.html", "nemo-rails-explained.html", "sdp-explained.html"):
        ctx = b.new_context(viewport={"width": 375, "height": 900}); pg = ctx.new_page()
        load(pg, open(D + f, encoding="utf-8").read(), False)
        print("ref", f, pg.evaluate("[document.documentElement.scrollWidth, window.innerWidth]"), pg.evaluate(OVER_JS)[:3]); ctx.close()
    b.close()
