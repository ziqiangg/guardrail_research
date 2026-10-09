import re, sys, collections
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
lines = s.splitlines()
print("first 4 lines:", [l[:60] for l in lines[:4]])
for bad in ["<!doctype", "<html", "<head", "<body", "<script", "<img", "lang=", "viewport"]:
    print("contains", bad, bad.lower() in s.lower())
print("title:", re.search(r"<title>(.*?)</title>", s).group(1))
print("h1:", re.search(r"<h1>(.*?)</h1>", s).group(1))
print("eyebrows:", re.findall(r'class="eyebrow">(.*?)<', s))
# svg checks
svgs = re.findall(r"<svg\b.*?</svg>", s, re.S)
print("svg count", len(svgs))
allids = []
for i, sv in enumerate(svgs):
    head = re.match(r"<svg[^>]*>", sv).group(0)
    vb = re.search(r'viewBox="([^"]+)"', head)
    role = 'role="img"' in head
    al = re.search(r'aria-label="([^"]+)"', head)
    bad_attrs = re.findall(r'\s(fill|stroke|style|width|height)="', re.sub(r"<marker[^>]*>", "", re.sub(r"<rect[^>]*>", lambda m: re.sub(r'\s(width|height)="[^"]*"', "", m.group(0)), sv)))
    # width/height on rect are geometry (allowed); check svg element and other non-rect elements
    svg_wh = re.findall(r'\s(width|height)="', head)
    ids = re.findall(r'<marker id="([^"]+)"', sv)
    refs = re.findall(r"url\(#([^)]+)\)", sv)
    allids += ids
    title = "<title" in sv
    print(i, vb.group(1) if vb else None, "role", role, "label_len", len(al.group(1)) if al else 0, "bad_attrs", bad_attrs, "svg_wh", svg_wh, "markers", ids, "refs", sorted(set(refs)), "unused", sorted(set(ids)-set(refs)), "unresolved", sorted(set(refs)-set(ids)), "title", title)
dup = [k for k, v in collections.Counter(allids).items() if v > 1]
print("duplicate marker ids:", dup)
print("h3:", re.findall(r"<h3>(.*?)</h3>", s))
print("diagram refs:", re.findall(r"diagrams? \d+(?: and \d+)?", s))
print("limits items:", len(re.findall(r"<li><b>", s)))
# classes used in svg
cls = collections.Counter(re.findall(r'<(?:rect|path|line)[^>]*class="([^"]+)"', s))
print("svg shape classes:", dict(cls))
print("legend:", re.findall(r'<i class="sw ([^"]+)"></i>([^<]+)', s))
print("pills:", collections.Counter(re.findall(r'pill (yes|partly|no)', s)))
# words
for w in ["LLM", "PII", "color", "behavior", "organization", "recognize", "analyze", "!", "anonymiz"]:
    hits = [m.start() for m in re.finditer(re.escape(w), re.sub(r"<style>.*?</style>", "", s, flags=re.S))]
    print("word", w, len(hits))
