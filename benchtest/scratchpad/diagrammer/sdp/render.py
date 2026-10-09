import json
import os
import sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.abspath(os.path.join(HERE, "..", "..", "..", "diagrams", "sdp-explained.html"))
URL = "file:///" + PAGE.replace("\\", "/")

CHECK_JS = r"""
() => {
  const out = {overflow: [], clipped: [], ids: {}, urlrefs: [], bad_attrs: []};
  out.scrollW = document.documentElement.scrollWidth; out.innerW = window.innerWidth;
  // text vs containing rect
  document.querySelectorAll('svg').forEach((svg, si) => {
    const rects = [...svg.querySelectorAll('rect')].map(r => {
      const b = r.getBBox(); return {x:b.x, y:b.y, w:b.width, h:b.height, cls:r.getAttribute('class')};
    });
    svg.querySelectorAll('text').forEach(t => {
      const b = t.getBBox();
      const cx = b.x + b.width/2, cy = b.y + b.height/2;
      // smallest rect containing the text centre
      let best = null;
      rects.forEach(r => {
        if (cx >= r.x && cx <= r.x + r.w && cy >= r.y && cy <= r.y + r.h && !(r.cls||'').includes('zone')) {
          if (!best || r.w*r.h < best.w*best.h) best = r;
        }
      });
      if (best && (b.x < best.x + 3 || b.x + b.width > best.x + best.w - 3)) {
        out.clipped.push({svg: si, text: t.textContent, tx: [Math.round(b.x), Math.round(b.x+b.width)], rect: [Math.round(best.x), Math.round(best.x+best.w)]});
      }
      const vb = svg.viewBox.baseVal;
      if (b.x < 0 || b.x + b.width > vb.width || b.y < 0 || b.y + b.height > vb.height) {
        out.overflow.push({svg: si, text: t.textContent, bbox: [Math.round(b.x), Math.round(b.y), Math.round(b.x+b.width), Math.round(b.y+b.height)], vb: [vb.width, vb.height]});
      }
    });
    // forbidden attrs
    svg.querySelectorAll('*').forEach(el => {
      ['fill','stroke','style','width','height'].forEach(a => {
        if (el.tagName.toLowerCase() === 'rect' && (a === 'width' || a === 'height')) return;
        if (el.hasAttribute(a)) out.bad_attrs.push({svg: si, tag: el.tagName, attr: a});
      });
    });
    if (svg.hasAttribute('width') || svg.hasAttribute('height') || svg.querySelector('title')) out.bad_attrs.push({svg: si, tag: 'svg', attr: 'width/height/title'});
  });
  return out;
}
"""

results = {}
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for scheme in ("light", "dark"):
        for name, width in (("desktop", 1280), ("phone", 375)):
            ctx = browser.new_context(color_scheme=scheme, viewport={"width": width, "height": 900})
            page = ctx.new_page()
            page.goto(URL)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500)
            shot = os.path.join(HERE, "sdp-%s-%s.png" % (scheme, name))
            page.screenshot(path=shot, full_page=True)
            res = page.evaluate(CHECK_JS)
            res["bodyBg"] = page.evaluate("getComputedStyle(document.body).backgroundColor")
            results["%s-%s" % (scheme, name)] = res
            ctx.close()
    browser.close()

for k, v in results.items():
    print(k, "scrollW", v["scrollW"], "innerW", v["innerW"], "bg", v["bodyBg"],
          "clipped", len(v["clipped"]), "svgtext_outside_viewbox", len(v["overflow"]), "bad_attrs", len(v["bad_attrs"]))
if "--detail" in sys.argv:
    r = results["light-desktop"]
    for key in ("clipped", "overflow", "bad_attrs"):
        for item in r[key]:
            print(key, json.dumps(item))
