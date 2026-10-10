import re, sys
sys.path.insert(0, "benchtest")
import build_eval_sheet as B
P = "benchtest/drafts/litmus_eval_tooling_final.md"
I = "benchtest/drafts/litmus_inventory_final.md"
secs = B.parse_md(P)
LAB = re.compile(r"\*\*\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*")
ALLOWED = re.compile(r"\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]")
txt = open(P, encoding="utf-8").read()
itxt = open(I, encoding="utf-8").read()
print("sections:", [s["name"] for s in secs])
for s in secs:
    nb = nt = nrows = 0
    for it in s["items"]:
        if it[0] == "summary":
            body = LAB.sub("", it[1]).strip()
            w = len(body.replace("**", "").split())
            wl = len(it[1].replace("**", "").split())
            print("  SUMMARY", s["name"], "words excl label", w, "incl label", wl, "** count", it[1].count("**"), "backtick/_/$:", bool(re.search(r"[`_$]", it[1])))
        elif it[0] == "detail":
            for b in it[1]:
                if b.startswith("• "):
                    nb += 1
                    if not LAB.search(b): print("  NOLABEL detail", s["name"], b[:80])
        elif it[0] == "bullet":
            nb += 1
            first = it[1].split("\n")[0]
            if not LAB.search(first): print("  NOLABEL bullet", s["name"], first[:80])
            if s["name"] == "Open questions":
                labs = LAB.findall(first)
                if not labs or any(l[0] not in ("To be verified", "Not disclosed") for l in labs): print("  BAD OQ LABEL", first[:80])
        elif it[0] == "table":
            nrows += len(it[2]); nt += 1
    print("  ", s["name"], "bullets", nb, "tables", nt, "rows", nrows)
# bracket forms
for name, t in (("EV", txt), ("INV", itxt)):
    br = re.findall(r"\[[^\]\n]{1,80}\]", t)
    bad = [b for b in br if not ALLOWED.fullmatch(b)]
    print(name, "bracket forms not allowed:", sorted(set(bad))[:20])
    for pat in (r"R0\d\d", r"Reviewer", r"this draft", r"I checked", r"see above", r"\bT\d{1,2}\b", r"\bP[0-9]\b", r"\(draft", r"R003|R011|R019|R032"):
        m = re.findall(pat, t)
        if m: print(name, "pattern", pat, len(m), m[:5])
print("INV ** / backtick / pipe check:", "**" in itxt, "`" in itxt)
cov = re.findall(r"— \(inventory only, not in Table 3\)", itxt)
print("INV covered markers", len(cov))
print("Illustrative:", re.findall(r".{20}[Ii]llustrative.{20}", txt + itxt))
print("EV lines", txt.count("\n"), "chars", len(txt))
