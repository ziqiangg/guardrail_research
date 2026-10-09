"""Mechanical checklist for modelarmor-explained.html (gr-verifier, P10)."""
import re, pathlib, collections
root = pathlib.Path(__file__).resolve().parents[4]
html = (root / 'benchtest/diagrams/modelarmor-explained.html').read_text(encoding='utf-8')
drafts = ''.join((root / 'benchtest/drafts' / f).read_text(encoding='utf-8')
                 for f in ['modelarmor_two_level.md', 'modelarmor_inventory_final.md'])

print('starts:', repr(html[:40]))
for bad in ['<!doctype', '<html', '<head', '<body', 'lang=', 'viewport', '<script', '<img', 'javascript:']:
    print('forbidden', bad, bad.lower() in html.lower())
print('stylesheet links:', re.findall(r'<link [^>]*>', html))

svgs = re.findall(r'<svg[^>]*>.*?</svg>', html, re.S)
print('svg count', len(svgs))
for i, s in enumerate(svgs):
    head = re.match(r'<svg[^>]*>', s).group(0)
    ok = 'viewBox' in head and 'role="img"' in head and 'aria-label=' in head
    attrs = re.findall(r'\s(fill|stroke|style|width|height)=', re.sub(r'<(rect|marker)[^>]*>', '', s))
    rect_bad = re.findall(r'<rect[^>]*\s(fill|stroke|style)=', s)
    vb = re.search(r'viewBox="([^"]+)"', head).group(1)
    print(f'svg{i} vb={vb} head_ok={ok} bad_attrs={attrs} rect_bad={rect_bad} title={"<title" in s}')

ids = re.findall(r'<marker id="([^"]+)"', html)
dup = [k for k, v in collections.Counter(ids).items() if v > 1]
used = re.findall(r'url\(#([^)]+)\)', html)
print('markers', ids)
print('dup markers', dup, '| unresolved', sorted(set(used) - set(ids)), '| unused', sorted(set(ids) - set(used)))

h3 = re.findall(r'<h3>([^<]*)</h3>', html)
print('h3:', h3)
print('eyebrows:', re.findall(r'<div class="eyebrow">([^<]*)</div>', html))
print('diagram refs:', sorted(set(re.findall(r'diagrams? \d+(?: and \d+)?', html))))
classes = collections.Counter(re.findall(r'class="([^"]+)"', html))
print('svg role classes:', {k: v for k, v in classes.items() if k.split()[0] in ('gate', 'ok', 'no', 'ed', 'part', 'na', 'lna', 'box', 'zone') or 'dev' in k})
print('legend:', re.findall(r'<i class="sw ([^"]+)"></i>([^<]*)', html))
print('pills:', collections.Counter(re.findall(r'pill (yes|partly|no)', html)))
print('limits items:', len(re.findall(r'<li><b>', html)))

hrefs = re.findall(r'href="([^"]+)"', html)
ext = [h for h in hrefs if h.startswith('http') and 'fonts.g' not in h]
print('footer/body URLs:', len(ext))
for h in ext:
    if h not in drafts:
        print('  NOT IN DRAFTS:', h)
print('internal links:', [h for h in hrefs if not h.startswith('http')])
(pathlib.Path(__file__).parent / 'urls.txt').write_text('\n'.join(ext) + '\n', encoding='utf-8')

# Words to check for voice
text = re.sub(r'<[^>]+>', ' ', re.sub(r'<style>.*?</style>', '', html, flags=re.S))
for w in ['LLM', 'PII', 'color', 'behavior', 'organization', 'recognize', 'license ', 'center', '!']:
    hits = [m.start() for m in re.finditer(re.escape(w), text)]
    if hits:
        print('voice', repr(w), len(hits), [text[max(0, h-40):h+40].replace('\n', ' ') for h in hits[:3]])
