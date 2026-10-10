import re, os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
D = os.path.join(ROOT, "benchtest", "diagrams")
new = open(os.path.join(D, "cloak-explained.html"), encoding="utf-8").read()
sent = open(os.path.join(D, "sentinel-explained.html"), encoding="utf-8").read()
nl, sl = new.split("\n"), sent.split("\n")
print("css 6-110 identical:", nl[5:110] == sl[5:110])
print("line5:", nl[4][:90])
print("additions header lines:", [l for l in nl if l.startswith("/* Additions")])
print("doctype/html/head/body/script/img/lang/meta:", [t for t in ("<!doctype","<html","<head","<body","<script","<img","lang=","<meta") if t in new.lower()])
print("title:", re.search(r"<title>(.*?)</title>", new).group(1))
print("h1:", re.search(r"<h1>(.*?)</h1>", new).group(1))
print("eyebrow:", re.search(r'<header>\s*<div class="eyebrow">(.*?)</div>', new).group(1))
# svgs
svgs = re.findall(r"<svg.*?</svg>", new, re.S)
print("svg count:", len(svgs))
ids = re.findall(r'<marker id="([^"]+)"', new)
print("marker ids:", ids, "dupes:", [i for i in set(ids) if ids.count(i) > 1])
urls = set(re.findall(r"url\(#([^)]+)\)", new))
print("unresolved:", urls - set(ids), "unused:", set(ids) - urls)
for i, s in enumerate(svgs):
    root = re.match(r"<svg[^>]*>", s).group(0)
    bad = [a for a in (" width=", " height=", " fill=", " stroke=", " style=") if a in root]
    inner = re.sub(r"<rect[^>]*>", "", s)  # rect width/height ok
    bad2 = [a for a in (" fill=", " stroke=", " style=") if a in s]
    ok = "viewBox" in root and 'role="img"' in root and "aria-label" in root
    print(i, re.search(r'viewBox="([^"]+)"', root).group(1), "ok" if ok and not bad and not bad2 else ("BAD", bad, bad2, ok))
# legend vs used
leg = set(re.findall(r'<i class="sw ([a-z]+)"', new))
used = set()
body = new[new.index("<div class=\"wrap\">"):]
for cls in re.findall(r'class="([^"]+)"', body):
    for c in cls.split():
        used.add(c)
print("legend:", sorted(leg))
roles = {"gate":"gate","dev":"dev","ed":"edit","part":"part","na":"na","mk-nd":"nd","mk-plan":"plan","ok":"pass","no":"stop"}
for k, v in roles.items():
    print(" role", k, "used" if k in used else "unused", "| legend" if v in leg else "| no legend")
# stray words
txt = re.sub(r"<[^>]+>", " ", body)
for w in ["LLM", "PII", "!", "behavior", "color ", "organization", "recognize", "anonymize", "customize", "utilize"]:
    n = [m.start() for m in re.finditer(re.escape(w), txt)]
    if n: print("word", repr(w), len(n), [txt[max(0,i-30):i+30].replace("\n"," ") for i in n[:3]])
print("rails h3:", re.findall(r"<h3>(.*?)</h3>", new))
print("limits:", new.count("<li><b>"))
print("links:", len(re.findall(r'<footer>.*', new, re.S)[0].split("href=")) - 1)
