"""P7 verifier: diff sdp_two_level.md against sdp_cols_a.md + sdp_cols_b.md (difflib).
Writes a per-row report of removed/added bullets and Summaries and whether each change
is findable in sdp_changes.md (by a normalised prefix).  Read-only on the drafts."""
import re, sys, difflib, json
D = "benchtest/drafts/"
HDR = re.compile(r"^## Column (SD\d):")
ROW = re.compile(r"^### R([1-9])\s*$")

def parse(path):
    cols, cur, row = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## Reviewer notes"):
            cur = None; continue
        m = HDR.match(line)
        if m:
            cur = m.group(1); cols[cur] = {}; row = None; continue
        if cur is None:
            continue
        m = ROW.match(line)
        if m:
            row = int(m.group(1)); cols[cur][row] = {"summary": "", "lines": []}; continue
        if row is None:
            continue
        if line.startswith("Summary: "):
            cols[cur][row]["summary"] = line[9:]
        elif line.startswith("• ") or line.startswith("  – "):
            cols[cur][row]["lines"].append(line)
    return cols

orig = {}
orig.update(parse(D + "sdp_cols_a.md")); orig.update(parse(D + "sdp_cols_b.md"))
fin = parse(D + "sdp_two_level.md")
log = open(D + "sdp_changes.md", encoding="utf-8").read()

def norm(s):
    s = s.replace("**", "").replace("`", "").replace("\\|", "|")
    s = re.sub(r"^\s*(•|–)\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()

lognorm = norm(log)

def inlog(s, n=40):
    t = norm(s)
    # try a few windows
    for start in (0, 20, 60):
        frag = t[start:start + n]
        if len(frag) >= 25 and frag in lognorm:
            return True
    return False

out = []
summ_changed = []
unlogged = []
for c in sorted(fin):
    for r in range(1, 10):
        o = orig.get(c, {}).get(r, {"summary": "", "lines": []})
        f = fin[c][r]
        if o["summary"] != f["summary"]:
            summ_changed.append(f"{c} R{r}")
            out.append(f"\n=== {c} R{r} SUMMARY\n- {o['summary']}\n+ {f['summary']}")
        sm = difflib.SequenceMatcher(None, o["lines"], f["lines"], autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            out.append(f"\n--- {c} R{r} {tag}")
            for x in o["lines"][i1:i2]:
                out.append("  - " + x)
            for x in f["lines"][j1:j2]:
                ok = inlog(x)
                out.append(("  + " if ok else "  +!") + x)
                if not ok:
                    unlogged.append((c, r, x))

open("benchtest/scratchpad/verifier/sdp/diff_cols.txt", "w", encoding="utf-8").write("\n".join(out))
print("Summaries changed:", len(summ_changed), summ_changed)
print("added/changed lines not found in log by prefix:", len(unlogged))
with open("benchtest/scratchpad/verifier/sdp/unlogged_candidates.txt", "w", encoding="utf-8") as fh:
    for c, r, x in unlogged:
        fh.write(f"{c} R{r}: {x}\n")
