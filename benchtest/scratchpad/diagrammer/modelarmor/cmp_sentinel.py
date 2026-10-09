import os
from playwright.sync_api import sync_playwright
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..","..",".."))
with sync_playwright() as p:
    b=p.chromium.launch(headless=True)
    for name in ("sentinel-explained.html","llama-guard-explained.html","nemo-rails-explained.html","modelarmor-explained.html"):
        ctx=b.new_context(viewport={"width":375,"height":800})
        pg=ctx.new_page()
        pg.goto("file:///"+os.path.join(ROOT,"benchtest","diagrams",name).replace("\\","/"))
        pg.wait_for_timeout(300)
        print(name, pg.evaluate("document.documentElement.scrollWidth"))
        ctx.close()
    b.close()
