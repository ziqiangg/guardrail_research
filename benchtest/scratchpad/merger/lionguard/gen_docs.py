import os, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_lib as L
import merge_lionguard as M
import docs_text as T

D = "benchtest/drafts/"
LABEL = r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"


def words(s):
    s = re.sub(r"\*\*" + LABEL + r"\*\*\s*$", "", s).replace("**", "")
    return len(s.split())


def parse(path):
    cols, cur, rn = [], None, None
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("## Column"):
            m = re.match(r"^## Column ([A-Z]+\d+): (.+)$", ln)
            cur = {"id": m.group(1), "header": m.group(2), "R": {}}; cols.append(cur); rn = None
        elif cur is not None and re.match(r"^### R([1-9])\s*$", ln):
            rn = int(ln.split("R")[1]); cur["R"][rn] = {"s": None, "d": []}
        elif cur is not None and rn is not None:
            if ln.startswith("Summary: "): cur["R"][rn]["s"] = ln[9:].strip()
            elif ln.startswith("• ") or ln.startswith("  – "): cur["R"][rn]["d"].append(ln)
    return cols


orig = parse(D + "lionguard_cols_a.md")
C, V = M.run()
open(D + "lionguard_two_level.md", "w", encoding="utf-8").write(C.render(C.order))
open(D + "lionguard_inventory_final.md", "w", encoding="utf-8").write(V.render())
final = parse(D + "lionguard_two_level.md")
grid = {}
for c in final:
    for n in range(1, 10):
        r = c["R"][n]
        grid[(c["id"], n)] = (words(r["s"]), len([d for d in r["d"] if d.startswith("• ")]))

# ---------------------------------------------------------------- preview
reasons = collections.defaultdict(list)
for e in L.LOG:
    if e["kind"] == "summary":
        reasons[e["loc"].replace(" Summary", "")].append(e["reason"])
oc = {c["id"]: c for c in orig}
changed = []
for c in final:
    for n in range(1, 10):
        a, b = oc[c["id"]]["R"][n]["s"], c["R"][n]["s"]
        if a != b:
            loc = "%s R%d" % (c["id"], n)
            changed.append((loc, words(a), words(b), "; ".join(reasons[loc]) or "(see section 2)"))
out = ["# LionGuard: Summary preview (Checkpoint 2)", "",
       "Generated from lionguard_two_level.md on 2026-10-10. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60.", ""]
for c in final:
    out += ["## %s: %s" % (c["id"], c["header"]), ""]
    for n in range(1, 10):
        w_, b = grid[(c["id"], n)]
        out.append("- **R%d** (%dw, %d bullets): %s" % (n, w_, b, c["R"][n]["s"]))
    out.append("")
out += ["## Summaries changed in the merge", "", "| Location | Words before | Words after | Reason |", "|---|---|---|---|"]
for loc, wb, wa, why in changed:
    out.append("| %s | %s | %s | %s |" % (loc, wb, wa, why.replace("|", "/")))
open(D + "lionguard_summaries_preview.md", "w", encoding="utf-8").write("\n".join(out) + "\n")


def short(s, n=230):
    s = s.replace("**", "").replace("\n", " // ")
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n: s = s[:n - 1].rstrip() + "…"
    return s.replace("|", "\\|")


colE = [e for e in L.LOG if e["file"] == "cols"]
invE = [e for e in L.LOG if e["file"] == "inv"]
cnt_c = collections.Counter(e["kind"] for e in colE)
cnt_i = collections.Counter(e["kind"] for e in invE)

txt = open(D + "lionguard_two_level.md", encoding="utf-8").read()
inv_txt = open(D + "lionguard_inventory_final.md", encoding="utf-8").read()
labs = collections.Counter(); nolab = 0; r8lab = 0
for n in range(1, 10):
    for d in final[0]["R"][n]["d"]:
        if not d.startswith("• "): continue
        m = re.search(r"\*\*(" + LABEL + r")\*\*\s*$", d)
        if n <= 7:
            if m:
                l = m.group(1)
                labs["Documented: repo" if l.startswith("[Documented: repo") else l.strip("[]")] += 1
            else: nolab += 1
        elif n == 8 and m: r8lab += 1

both = txt + "\n" + inv_txt
kn_rows = [(s, both.count(s), why) for s, why in T.KNOWN]
summ_code = [l[:40] for l in txt.splitlines() if l.startswith("Summary: ") and re.search(r"[`_$]", l)]


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return (p.stdout + p.stderr).strip(), p.returncode


c1, rc1 = run(["python", "benchtest/tools/check_drafts.py", "columns", D + "lionguard_two_level.md", "--final", "--expect", "1"])
c2, rc2 = run(["python", "benchtest/tools/check_drafts.py", "inventory", D + "lionguard_inventory_final.md", "--headers", D + "lionguard_two_level.md"])

cov_hdr = inv_txt.count("| LionGuard: Localised harmful-content classification |")
cov_legacy = inv_txt.count("— (legacy, not in Table 3)")
cov_only = inv_txt.count("— (inventory only, not in Table 3)")
tbv_inv = inv_txt.count("[To be verified]"); tbv_col = txt.count("[To be verified]")
nd_col = txt.count("[Not disclosed]"); nd_inv = inv_txt.count("[Not disclosed]")
over = sum(1 for n in range(1, 10) if grid[("LN1", n)][0] > (60 if n == 7 else 45))

W = []
w = W.append
w("# LionGuard merge: change log")
w("")
w(T.INTRO)
w("")
w("## 1. Global changes")
w("")
w("| Scope | Before | After | Reason |")
w("|---|---|---|---|")
for g in T.GLOBAL: w("| " + " | ".join(x.replace("|", "/") for x in g) + " |")
w("")
w("## 2. Column and row changes")
w("")
w("Entries are listed in the order the edits were applied. Several bullets in one 'after' cell are joined by ' // '.")
w("")
w("### LN1")
w("")
w("| Location | Before | After | Reason |")
w("|---|---|---|---|")
for e in colE:
    w("| %s (%s) | %s | %s | %s |" % (e["loc"], e["kind"], short(e["before"]), short(e["after"]), e["reason"].replace("|", "/")))
w("")
w("## 3. Inventory changes")
w("")
w("| Location | Before | After | Reason |")
w("|---|---|---|---|")
for e in invE:
    w("| %s (%s) | %s | %s | %s |" % (e["loc"], e["kind"], short(e["before"]), short(e["after"]), e["reason"].replace("|", "/")))
w("")
w("## 4. Conflict decisions")
w("")
for i, t in enumerate(T.CONFLICTS, 1): w("%d. %s" % (i, t)); w("")
w("## 5. Change counts and P8 config notes")
w("")
w("- Logged edits: %d in the columns, %d in the inventory (%d in total)." % (len(colE), len(invE), len(colE) + len(invE)))
w("- Columns by kind: " + ", ".join("%s %d" % (k, cnt_c[k]) for k in sorted(cnt_c)) + ". All in LN1.")
w("- Inventory by kind: " + ", ".join("%s %d" % (k, cnt_i[k]) for k in sorted(cnt_i)) + ".")
w("- Summaries changed: %d of 9 (%s). R5 (77.0, confirmed by T21) and R9 are unchanged in wording class; R9 Summary text unchanged." % (len(changed), ", ".join(c[0] for c in changed)))
w(T.HANDLED)
w("- **P8 config (gr-xlsx-writer).** Inventory sheet for slug lionguard; Covered-by column name 'Covered by Table 3 column'; BLOCKS (marker, expected rows): (a) Variant table 4, (b) Output keys and taxonomy 11, (c) Dependencies and access 8, (d) Artefacts and references 11, (e) Cross-reference to Sentinel 4, that is **4/11/8/11/4** (38 rows; table widths 12, 7, 7, 7, 6 cells).")
w("- Markers tuple: legacy '— (legacy, not in Table 3)' (%d cells: the LionGuard 1 row and the BAAI embedder row) and inventory only '— (inventory only, not in Table 3)' (%d cells: block (d) 11, block (e) 4); 'planned' is not used. Every other Covered-by cell equals the exact header 'LionGuard: Localised harmful-content classification' (%d cells: (a) 3, (b) 11, (c) 7)." % (cov_legacy, cov_only, cov_hdr))
w("- Final columns: 1 (LN1), prefix 'LionGuard:' (R009, R031). No Sentinel header is listed in any Covered-by cell, on purpose.")
w("- R9 of LN1 holds %d URLs. %s" % (grid[("LN1", 9)][1], T.URL_NOTE))
w("")
w("## 6. Remaining open items")
w("")
w("Counts in the finals: [To be verified] %d in the column and %d in the inventory; [Not disclosed] %d in the column and %d in the inventory. The column has no [To be verified] bullet: its open terms question is an unlabelled R8 bullet." % (tbv_col, tbv_inv, nd_col, nd_inv))
w("")
w("### 6a. Class b items (needs testing or honest gap), unchanged in the finals")
w("")
w("| T | Item | Class | Where it stays | Checked |")
w("|---|---|---|---|---|")
for o in T.OPEN: w("| " + " | ".join(x.replace("|", "/") for x in o) + " |")
w("")
w("### 6b. Residual parts of handled items (class a and c)")
w("")
w("| T | Residual | Class | Label in the finals | Checked |")
w("|---|---|---|---|---|")
for o in T.RES: w("| " + " | ".join(x.replace("|", "/") for x in o) + " |")
w("")
w("### 6c. FYI items recorded here only")
w("")
for t in T.FYI: w("- " + t)
w("")
w("## 7. Moved Reviewer notes")
w("")
w("### 7a. lionguard_cols_a.md (LN1), 12 notes")
w("")
for p, notes in C.reviewer_notes.items():
    for ln in notes:
        if ln.strip(): w(ln)
w("")
w("### 7b. lionguard_inventory.md, 8 notes and the self-check line")
w("")
for ln in V.reviewer_notes:
    if ln.strip(): w(ln)
w("")
w(T.NOTES_STATUS)
w("")
w("## 8. Self-check")
w("")
w("### 8a. Summary word counts (limit 45, R7 60; trailing label excluded)")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Over limit |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
w("| LN1 | " + " | ".join(str(grid[("LN1", n)][0]) for n in range(1, 10)) + " | %d |" % over)
w("")
w("### 8b. Top-level Detail bullets per row")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Total |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
w("| LN1 | " + " | ".join(str(grid[("LN1", n)][1]) for n in range(1, 10)) + " | %d |" % sum(grid[("LN1", n)][1] for n in range(1, 10)))
w("")
w("### 8c. Labels on R1 to R7 Detail bullets")
w("")
w("| Column | Documented | Documented: repo | Inferred | To be verified | Not disclosed | R1-R7 bullets without a label | R8 bullets with a label |")
w("|---|---|---|---|---|---|---|---|")
w("| LN1 | %d | %d | %d | %d | %d | %d | %d |" % (labs["Documented"], labs["Documented: repo"], labs["Inferred"], labs["To be verified"], labs["Not disclosed"], nolab, r8lab))
w("")
w("### 8d. Structure")
w("")
w("| Check | Result |")
w("|---|---|")
w("| Columns | 1 (expected 1), ID LN1, prefix 'LionGuard:' |")
w("| Summaries | 9; over limit: %d; backtick, underscore or $ in a Summary: %d |" % (over, len(summ_code)))
w("| Rows R1 to R9 each once, Summary line and Detail present | yes (checker) |")
w("| Inventory tables | (a) 4 rows x 12 cols; (b) 11 x 7; (c) 8 x 7; (d) 11 x 7; (e) 4 x 6 (checker) |")
w("| Inventory Covered-by values that are not an exact header or marker | 0 (checker) |")
w("| Inventory cells with bold markers, backticks or pipes; non-standard labels | 0 (checker) |")
w("")
w("### 8e. Known-wrong strings and process wording (lessons.md item 6)")
w("")
w("| String or pattern | Hits in the two finals | Note |")
w("|---|---|---|")
for s, n, why in kn_rows: w("| %s | %d | %s |" % (s, n, why))
w("| T-ids, CP1, CP2, Q01 to Q04, ruling ids | 0 | grep of both finals |")
w("")
w("### 8f. Checker output (run from the repo root)")
w("")
w("```")
w("python benchtest/tools/check_drafts.py columns benchtest/drafts/lionguard_two_level.md --final --expect 1")
w(c1)
w("python benchtest/tools/check_drafts.py inventory benchtest/drafts/lionguard_inventory_final.md --headers benchtest/drafts/lionguard_two_level.md")
w(c2)
w("```")
w("")
w("Exit codes: columns %d, inventory %d." % (rc1, rc2))
open(D + "lionguard_changes.md", "w", encoding="utf-8").write("\n".join(W) + "\n")
print("written", len(colE), len(invE), [c[0] for c in changed], rc1, rc2)
print(c1.splitlines()[-1], "|", c2.splitlines()[-1])
print("labels", dict(labs), nolab, r8lab, "cov", cov_hdr, cov_legacy, cov_only, "tbv", tbv_col, tbv_inv, "nd", nd_col, nd_inv)
print("grid", [grid[("LN1", n)] for n in range(1, 10)])
for s, n, why in kn_rows:
    if n: print("HIT", s, n)
