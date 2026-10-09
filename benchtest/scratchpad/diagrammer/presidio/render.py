import os, re, sys, json
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PAGE = "file:///" + os.path.join(ROOT, "benchtest", "diagrams", "presidio-explained.html").replace("\\", "/")
OUTDIR = os.path.dirname(os.path.abspath(__file__))
TMP = os.environ.get("SHOT_DIR", OUTDIR)

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for scheme in ("light", "dark"):
        for name, w in (("desktop", 1280), ("phone", 375)):
            ctx = b.new_context(color_scheme=scheme, viewport={"width": w, "height": 900})
            page = ctx.new_page()
            msgs = []
            page.on("console", lambda m: msgs.append(m.text))
            page.goto(PAGE)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500)
            overflow = page.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
            # clipped text: any svg text whose bbox is outside its viewBox, or text wider than its enclosing rect
            clipped = page.evaluate("""() => {
              const bad = [];
              document.querySelectorAll('svg').forEach((s, si) => {
                const vb = s.viewBox.baseVal;
                s.querySelectorAll('text').forEach(t => {
                  const bb = t.getBBox();
                  if (bb.x < -1 || bb.x + bb.width > vb.width + 1 || bb.y < -1 || bb.y + bb.height > vb.height + 1)
                    bad.push([si, 'outside-viewbox', t.textContent, Math.round(bb.x), Math.round(bb.width)]);
                  // find the smallest rect containing the text centre
                  const cx = bb.x + bb.width / 2, cy = bb.y + bb.height / 2;
                  let best = null, area = 1e9;
                  s.querySelectorAll('rect').forEach(r => {
                    const x = +r.getAttribute('x'), y = +r.getAttribute('y'), rw = +r.getAttribute('width'), rh = +r.getAttribute('height');
                    if (cx >= x && cx <= x + rw && cy >= y && cy <= y + rh && rw * rh < area) { best = [x, y, rw, rh]; area = rw * rh; }
                  });
                  if (best && (bb.x < best[0] + 4 || bb.x + bb.width > best[0] + best[2] - 4))
                    bad.push([si, 'wider-than-box', t.textContent, Math.round(bb.width), best[2]]);
                });
              });
              return bad;
            }""")
            print(scheme, name, "overflow", overflow, "clipped", json.dumps(clipped)[:1500], "console", msgs[:3])
            page.screenshot(path=os.path.join(TMP, f"presidio_{scheme}_{name}.png"), full_page=True)
            ctx.close()
    b.close()
