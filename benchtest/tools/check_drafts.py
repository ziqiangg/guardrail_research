"""Mechanical checks for product drafts (P2/P3/P6/P7). Stdlib only; accepts ANY product prefix, so it works
before the product is registered in benchtest/products.py.

Usage:
  python benchtest/tools/check_drafts.py columns  benchtest/drafts/<slug>_two_level.md [--expect N] [--final]
  python benchtest/tools/check_drafts.py inventory benchtest/drafts/<slug>_inventory_final.md [--headers <two_level.md>]
Exit 0 = no errors. Warnings do not fail. --final also rejects a "## Reviewer notes" section in a columns file.

Checks (columns): heading grammar "## Column <ID>: <Prefix>: <Header>", R1..R9 each once, one "Summary: " line and
>=1 Detail bullet per row, Summary word limits (45; R7 60) excluding the trailing bold label, bold lead (R1-R8),
trailing bold label (R1-R7), R8 starts "**Key open questions.**" with no label, R9 plain (no **), no ` _ $ in
Summaries, balanced ** on every line, every Detail bullet in R1-R7 ends with a bold allowed label, R8/R9 bullets
unlabelled, R9 bullets contain exactly one URL, header prefixes consistent, IDs unique.
Checks (inventory): every table row has the header's cell count, no ** or backticks in cells, labels are allowed
forms, Covered-by cells contain only exact Table-3 headers (from --headers) or the legacy/planned markers.
"""
import argparse
import re
import sys

LABEL = r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"
BOLD_LABEL_END = re.compile(r"\*\*" + LABEL + r"\*\*\s*$")
ANY_BRACKET_LABEL = re.compile(r"\[(Documented[^\]]*|Inferred|To be verified|Not disclosed|Not found|TBV)[^\]]*\]")
ALLOWED = re.compile(LABEL)
HDR = re.compile(r"^## Column ([A-Za-z]{1,4}\d{1,2}): ([^:]+): (.+?)\s*$")
URL = re.compile(r"https?://\S+")
MARKERS = {"— (legacy, not in Table 3)", "— (planned, not in Table 3)", "— (inventory only, not in Table 3)"}  # 3rd marker: R011


def words(s):
    s = re.sub(r"\*\*" + LABEL + r"\*\*\s*$", "", s).replace("**", "")
    return len(s.split())


def check_columns(path, expect=None, final=False):
    err, warn = [], []
    cols, cur, rn, mode = [], None, None, None
    lines = open(path, encoding="utf-8").read().splitlines()
    for i, ln in enumerate(lines, 1):
        if ln.count("**") % 2:
            err.append(f"L{i}: unbalanced **")
        if ln.startswith("## Column"):
            m = HDR.match(ln)
            if not m:
                err.append(f"L{i}: bad column heading: {ln[:80]}")
                cur = None
                continue
            cur = {"id": m.group(1), "prefix": m.group(2), "header": f"{m.group(2)}: {m.group(3)}", "R": {}, "line": i}
            cols.append(cur)
            rn = None
            continue
        if ln.startswith("## "):
            if final and "reviewer notes" in ln.lower():
                err.append(f"L{i}: final file must not contain '{ln}'")
            cur = None
            continue
        m = re.match(r"^### R([1-9])\s*$", ln)
        if m and cur is not None:
            rn = int(m.group(1))
            if rn in cur["R"]:
                err.append(f"L{i}: {cur['id']} R{rn} duplicated")
            cur["R"][rn] = {"s": None, "d": []}
            mode = None
            continue
        if cur is None or rn is None:
            continue
        if ln.startswith("Summary: "):
            if cur["R"][rn]["s"] is not None:
                err.append(f"L{i}: {cur['id']} R{rn} second Summary line")
            cur["R"][rn]["s"] = (i, ln[9:].strip())
        elif ln.strip() == "Detail:":
            mode = "d"
        elif mode == "d" and (ln.startswith("• ") or ln.startswith("  – ")):
            cur["R"][rn]["d"].append((i, ln))
        elif mode == "d" and ln.strip() and not ln.startswith("#"):
            warn.append(f"L{i}: {cur['id']} R{rn} detail line ignored by parser (must start '• ' or '  – '): {ln[:60]}")
    if expect is not None and len(cols) != expect:
        err.append(f"expected {expect} columns, found {len(cols)}")
    if len({c['id'] for c in cols}) != len(cols):
        err.append("duplicate column IDs")
    if len({c['prefix'] for c in cols}) > 1:
        warn.append(f"several prefixes used: {sorted({c['prefix'] for c in cols})}")
    for c in cols:
        if sorted(c["R"]) != list(range(1, 10)):
            err.append(f"{c['id']}: rows present {sorted(c['R'])}, need R1..R9")
        for n, r in c["R"].items():
            tag = f"{c['id']} R{n}"
            if r["s"] is None:
                err.append(f"{tag}: no Summary")
                continue
            li, s = r["s"]
            if not r["d"]:
                err.append(f"{tag}: no Detail bullets")
            lim = 60 if n == 7 else 45
            if words(s) > lim:
                err.append(f"L{li} {tag}: Summary {words(s)} words > {lim}")
            if re.search(r"[`_$]", s):
                err.append(f"L{li} {tag}: Summary contains backtick, underscore or $")
            if n <= 8 and not s.startswith("**"):
                err.append(f"L{li} {tag}: Summary must start with a bold lead")
            if n <= 7 and not BOLD_LABEL_END.search(s):
                err.append(f"L{li} {tag}: Summary must end with a bold allowed label")
            if n == 8 and (not s.startswith("**Key open questions.**") or ANY_BRACKET_LABEL.search(s)):
                err.append(f"L{li} {tag}: R8 Summary must start '**Key open questions.**' and carry no label")
            if n == 9 and "**" in s:
                err.append(f"L{li} {tag}: R9 Summary must be plain (no **)")
            for di, d in r["d"]:
                top = d.startswith("• ")
                if n <= 7 and top and not BOLD_LABEL_END.search(d):
                    err.append(f"L{di} {tag}: Detail bullet must end with a bold allowed label")
                if n >= 8 and ANY_BRACKET_LABEL.search(d):
                    err.append(f"L{di} {tag}: R8/R9 bullets carry no labels")
                if n == 9 and top and len(URL.findall(d)) != 1:
                    err.append(f"L{di} {tag}: R9 bullet needs exactly one URL")
                for bad in ANY_BRACKET_LABEL.finditer(d):
                    if not ALLOWED.fullmatch(bad.group(0)):
                        err.append(f"L{di} {tag}: non-standard label {bad.group(0)}")
    print(f"columns: {len(cols)}  " + "  ".join(f"{c['id']}={c['header']}" for c in cols))
    return err, warn


def table_rows(lines):
    """Yield (section, header_cells, [(lineno, cells)])."""
    sec, hdr, rows, out = None, None, [], []
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            if hdr:
                out.append((sec, hdr, rows))
            sec, hdr, rows = ln[3:].strip(), None, []
            continue
        if ln.startswith("|"):
            cells = [x.strip() for x in ln.strip().strip("|").split("|")]
            if hdr is None:
                hdr = cells
            elif all(re.fullmatch(r":?-{3,}:?", x) for x in cells):
                continue
            else:
                rows.append((i, cells))
    if hdr:
        out.append((sec, hdr, rows))
    return out


def check_inventory(path, headers_md=None):
    err, warn = [], []
    headers = None
    if headers_md:
        headers = {f"{m.group(2)}: {m.group(3)}" for m in
                   (HDR.match(l) for l in open(headers_md, encoding="utf-8").read().splitlines()) if m}
    lines = open(path, encoding="utf-8").read().splitlines()
    for sec, hdr, rows in table_rows(lines):
        print(f"table '{sec}': {len(rows)} rows x {len(hdr)} cols")
        cov = next((k for k, h in enumerate(hdr) if h.lower().startswith("covered by")), None)
        for i, cells in rows:
            if len(cells) != len(hdr):
                err.append(f"L{i}: {len(cells)} cells, header has {len(hdr)} (stray '|'?)")
                continue
            for c in cells:
                if "**" in c or "`" in c:
                    err.append(f"L{i}: ** or backtick in cell")
                for lab in ANY_BRACKET_LABEL.finditer(c):
                    if not ALLOWED.fullmatch(lab.group(0)):
                        err.append(f"L{i}: non-standard label {lab.group(0)}")
            if cov is not None and headers is not None:
                for v in (x.strip() for x in cells[cov].split(";")):
                    if v and v not in headers and v not in MARKERS:
                        err.append(f"L{i}: Covered-by value not an exact Table-3 header or marker: {v[:70]}")
    return err, warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["columns", "inventory"])
    ap.add_argument("path")
    ap.add_argument("--expect", type=int)
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--headers", help="two_level md whose column headers are the valid Covered-by values")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.kind == "columns":
        err, warn = check_columns(a.path, a.expect, a.final)
    else:
        err, warn = check_inventory(a.path, a.headers)
    for w in warn:
        print("WARN ", w)
    for e in err:
        print("ERROR", e)
    print(f"RESULT: {len(err)} errors, {len(warn)} warnings")
    sys.exit(1 if err else 0)


if __name__ == "__main__":
    main()
