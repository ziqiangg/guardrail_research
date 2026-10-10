import os, sys, json
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PAGE = os.path.join(ROOT, "benchtest", "diagrams", "purplellama-explained.html")
URL = "file:///" + PAGE.replace("\\", "/")

CHECK_JS = r"""
() => {
  const res = {};
  res.scrollW = document.documentElement.scrollWidth;
  res.innerW = window.innerWidth;
  // svg text clipping: every text must sit inside the smallest rect that contains its anchor
  const clipped = [];
  document.querySelectorAll('svg').forEach((svg, si) => {
    const vb = svg.viewBox.baseVal;
    const rects = Array.from(svg.querySelectorAll('rect')).map(r => ({
      x: r.x.baseVal.value, y: r.y.baseVal.value, w: r.width.baseVal.value, h: r.height.baseVal.value,
      cls: r.getAttribute('class')
    }));
    svg.querySelectorAll('text').forEach(t => {
      const bb = t.getBBox();
      const cx = bb.x + bb.width / 2, cy = bb.y + bb.height / 2;
      // outside viewBox
      if (bb.x < vb.x - 0.5 || bb.x + bb.width > vb.x + vb.width + 0.5 || bb.y < -0.5 || bb.y + bb.height > vb.height + 0.5) {
        clipped.push({svg: si, text: t.textContent, why: 'outside viewBox', bb: [bb.x, bb.y, bb.width, bb.height].map(Math.round)});
      }
      // find containing rect (smallest) for text anchor point
      const ax = bb.x + 1, ay = cy;
      let best = null;
      rects.forEach(r => {
        if (cx >= r.x && cx <= r.x + r.w && cy >= r.y && cy <= r.y + r.h && r.cls !== 'zone') {
          if (!best || r.w * r.h < best.w * best.h) best = r;
        }
      });
      if (best) {
        if (bb.x < best.x + 3 || bb.x + bb.width > best.x + best.w - 3 || bb.y < best.y || bb.y + bb.height > best.y + best.h) {
          clipped.push({svg: si, text: t.textContent, why: 'exceeds rect', rect: [best.x, best.y, best.w, best.h], bb: [bb.x, bb.y, bb.width, bb.height].map(Math.round)});
        }
      }
    });
  });
  res.clipped = clipped;
  // page-level overflow culprits at current width
  const culprits = [];
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.right > window.innerWidth + 1) {
      // is it inside a scroller?
      let p = el, scroll = false;
      while (p && p !== document.body) {
        const cs = getComputedStyle(p);
        if (p.tagName === 'FIGURE' || p.classList.contains('tablewrap')) { scroll = true; break; }
        p = p.parentElement;
      }
      if (!scroll) culprits.push(el.tagName + '.' + el.className + ' right=' + Math.round(r.right));
    }
  });
  res.culprits = culprits.slice(0, 10);
  return res;
}
"""

def run():
    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        for scheme in ("light", "dark"):
            for (w, h, tag) in ((1280, 900, "1280"), (375, 800, "375")):
                ctx = b.new_context(color_scheme=scheme, viewport={"width": w, "height": h})
                page = ctx.new_page()
                page.goto(URL)
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(500)
                r = page.evaluate(CHECK_JS)
                out["%s-%s" % (scheme, tag)] = r
                path = os.path.join(HERE, "purplellama-%s-%s.png" % (scheme, tag))
                page.screenshot(path=path, full_page=True)
                ctx.close()
        b.close()
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    run()
