import re, io
s = io.open("benchtest/diagrams/sentinel-explained.html", encoding="utf-8").read()
h = io.open("benchtest/diagrams/presidio-explained.html", encoding="utf-8").read()
st = re.search(r'<table class="cats">.*?</table>', s, re.S).group(0)
rows = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', st)
ours = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>', h)
d = {o[0]: o[:4] for o in ours}
for r in rows:
    print(r[0], d.get(r[0]) == r if r[0] in d else "ROW-ABSENT (dropped: Sentinel row not in README list)")
ids = re.findall(r'<marker id="([^"]+)"', h); used = set(re.findall(r'url\(#([^)]+)\)', h))
print("dups", len(ids) - len(set(ids)), "unresolved", used - set(ids), "unused", set(ids) - used)
for sv in re.findall(r'<svg [^>]*>', h):
    assert 'viewBox' in sv and 'role="img"' in sv and 'aria-label="' in sv and not re.search(r'\s(width|height|fill|stroke|style)=', sv)
print("limits", h.count('<li><b>'), "svgs", len(re.findall('<svg ', h)), "PII/LLM", re.findall(r'\bPII\b|\bLLM\b', h))
for u in re.findall(r'href="([^"]+)"', h):
    pass
