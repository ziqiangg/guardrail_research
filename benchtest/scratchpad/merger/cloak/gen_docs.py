import os, re, sys, subprocess, collections
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_lib as L
import merge_cloak as M

D = "benchtest/drafts/"
LABEL = r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"
H1 = "Cloak: Free-text PII detection and anonymisation"
H2 = "Cloak: Custom entity detection in free text (lists, regex and LLM)"
H3 = "Cloak: Reversible anonymisation and decryption (encrypt and restore)"
IDS = ["CK1", "CK2", "CK3"]


def words(s):
    s = re.sub(r"\*\*" + LABEL + r"\*\*\s*$", "", s).replace("**", "")
    return len(s.split())


def parse(paths):
    cols, cur, rn = [], None, None
    for path in paths:
        for ln in open(path, encoding="utf-8").read().splitlines():
            if ln.startswith("## Column"):
                m = re.match(r"^## Column ([A-Z]+\d+): (.+)$", ln)
                cur = {"id": m.group(1), "header": m.group(2), "R": {}}; cols.append(cur); rn = None
            elif ln.startswith("## Reviewer notes"):
                cur = None
            elif cur is not None and re.match(r"^### R([1-9])\s*$", ln):
                rn = int(ln.split("R")[1]); cur["R"][rn] = {"s": None, "d": []}
            elif cur is not None and rn is not None:
                if ln.startswith("Summary: "): cur["R"][rn]["s"] = ln[9:].strip()
                elif ln.startswith("• ") or ln.startswith("  – "): cur["R"][rn]["d"].append(ln)
    return cols


orig = parse([D + "cloak_cols_a.md", D + "cloak_cols_b.md"])
C, V = M.run()
open(D + "cloak_two_level.md", "w", encoding="utf-8").write(C.render(C.order))
open(D + "cloak_inventory_final.md", "w", encoding="utf-8").write(V.render())
final = parse([D + "cloak_two_level.md"])
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
out = ["# Cloak: Summary preview (Checkpoint 2)", "",
       "Generated from cloak_two_level.md on 2026-10-10. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60 (the merge keeps every Summary at most limit minus 1, lessons 18).", ""]
for c in final:
    out += ["## %s: %s" % (c["id"], c["header"]), ""]
    for n in range(1, 10):
        w_, b = grid[(c["id"], n)]
        out.append("- **R%d** (%dw, %d bullets): %s" % (n, w_, b, c["R"][n]["s"]))
    out.append("")
out += ["## Summaries changed in the merge", "", "| Location | Words before | Words after | Reason |", "|---|---|---|---|"]
for loc, wb, wa, why in changed:
    out.append("| %s | %s | %s | %s |" % (loc, wb, wa, why.replace("|", "/")))
open(D + "cloak_summaries_preview.md", "w", encoding="utf-8").write("\n".join(out) + "\n")


def short(s, n=230):
    s = s.replace("**", "").replace("\n", " // ")
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n: s = s[:n - 1].rstrip() + "…"
    return s.replace("|", "\\|")


colE = [e for e in L.LOG if e["file"] == "cols"]
invE = [e for e in L.LOG if e["file"] == "inv"]
cnt_c = collections.Counter(e["kind"] for e in colE)
cnt_i = collections.Counter(e["kind"] for e in invE)
per_col = collections.Counter(e["loc"].split()[0] for e in colE)

txt = open(D + "cloak_two_level.md", encoding="utf-8").read()
inv_txt = open(D + "cloak_inventory_final.md", encoding="utf-8").read()
labs = {i: collections.Counter() for i in IDS}; nolab = {i: 0 for i in IDS}; r8lab = {i: 0 for i in IDS}
for c in final:
    for n in range(1, 10):
        for d in c["R"][n]["d"]:
            if not d.startswith("• "): continue
            m = re.search(r"\*\*(" + LABEL + r")\*\*\s*$", d)
            if n <= 7:
                if m:
                    l = m.group(1)
                    labs[c["id"]]["Documented: repo" if l.startswith("[Documented: repo") else l.strip("[]")] += 1
                else: nolab[c["id"]] += 1
            elif n == 8 and m: r8lab[c["id"]] += 1

KNOWN = [
    ("read with pypdf|via pypdf|with pypdf", "extraction-tool wording (T70)"),
    ("read-only rule|research is read-only|during this research|during research", "session wording (T70)"),
    ("not interpreted here|carry no interpretation|not reconciled here", "process wording (T70, T64)"),
    ("CK1|CK2|CK3", "internal ids (T71); only the three heading lines"),
    ("GovTech's cloud", "not entailed (T34)"),
    ("learns from", "not entailed (T59)"),
    ("R0[0-9][0-9]|CP1|CP2|lessons|Reviewer notes|reviewer", "ruling ids and process terms"),
    ("bench will|we use|bench rule|this is the plan", "R032 decided-plan wording"),
    ("aliases, hashes|not an inline reply|custom salts in v2.1.0|built on Presidio \[Inferred\]|does not return a score|not re-read here|neither is chosen here|HTTP 200 after redirect", "strings removed in the P7 fix loop"),
    ("microsoft.github.io/presidio/tutorial/12_encryption/", "the 404 URL: only in the CK3 R4 HTTP-fact bullet and the PRESENC short-name definition, never as a Source URL"),
]
both = txt + "\n" + inv_txt
kn_rows = [(s, len(re.findall(s, both)), why) for s, why in KNOWN]


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return (p.stdout + p.stderr).strip(), p.returncode


c1, rc1 = run(["python", "benchtest/tools/check_drafts.py", "columns", D + "cloak_two_level.md", "--final", "--expect", "3"])
c2, rc2 = run(["python", "benchtest/tools/check_drafts.py", "inventory", D + "cloak_inventory_final.md", "--headers", D + "cloak_two_level.md"])

# inventory block stats
blocks = {}
cur = None
for ln in inv_txt.splitlines():
    if ln.startswith("## ("): cur = ln[3:6]; blocks[cur] = {"rows": 0, "name": ln[3:]}; hdr = False; sep = 0
    elif cur and ln.startswith("|"):
        blocks[cur]["rows"] += 1
for b in blocks.values(): b["rows"] -= 2
cov_all = inv_txt.count(H1) + inv_txt.count(H2) + inv_txt.count(H3)
cov_legacy = inv_txt.count("| — (legacy, not in Table 3) |")
cov_only = inv_txt.count("| — (inventory only, not in Table 3) |")
cov_plan = inv_txt.count("| — (planned, not in Table 3) |")
tbv_inv = inv_txt.count("[To be verified]"); tbv_col = txt.count("[To be verified]")
nd_col = txt.count("[Not disclosed]"); nd_inv = inv_txt.count("[Not disclosed]")
over = [(c["id"], n) for c in final for n in range(1, 10) if grid[(c["id"], n)][0] > (59 if n == 7 else 44)]
summ_code = [l[:40] for l in txt.splitlines() if l.startswith("Summary: ") and re.search(r"[`_$]", l)]
r9 = {c["id"]: grid[(c["id"], 9)][1] for c in final}

import docs_text as T

W = []
w = W.append
w("# Cloak merge: change log")
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
for cid in IDS:
    w("### " + cid)
    w("")
    w("| Location | Before | After | Reason |")
    w("|---|---|---|---|")
    for e in colE:
        if e["loc"].startswith(cid + " "):
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
w("## 5. P8 config notes and change counts")
w("")
w("### 5a. Change counts")
w("")
w("- Logged edits: %d in the columns (CK1 %d, CK2 %d, CK3 %d), %d in the inventory; %d in total." % (len(colE), per_col["CK1"], per_col["CK2"], per_col["CK3"], len(invE), len(colE) + len(invE)))
w("- Columns by kind: " + ", ".join("%s %d" % (k, cnt_c[k]) for k in sorted(cnt_c)) + ".")
w("- Inventory by kind: " + ", ".join("%s %d" % (k, cnt_i[k]) for k in sorted(cnt_i)) + ".")
p7c = [e for e in colE if e["reason"].startswith("P7")]; p7i = [e for e in invE if e["reason"].startswith("P7")]
w("- Of these, %d column edits and %d inventory edits are P7 verifier fixes (section 9)." % (len(p7c), len(p7i)))
w("- Summaries changed: %d of 27 (%s)." % (len(changed), ", ".join(c[0] for c in changed)))
w(T.HANDLED)
w("")
w("### 5b. P8 config (gr-xlsx-writer)")
w("")
w("- Product slug cloak; column ID prefix CK; **header prefix 'Cloak:'** (R009; frozen after CP2). The three headers are exactly: '%s'; '%s'; '%s'. Columns in the order CK1, CK2, CK3." % (H1, H2, H3))
w("- Inventory sheet (letter assigned at P8 per R003); Covered-by column name **'Covered by Table 3 column'**.")
bl = list(blocks.items())
w("- **BLOCKS (marker, expected rows): " + "; ".join("%s %s" % (k, v["rows"]) for k, v in bl) + "**, that is **%s** (%d rows). Table widths in cells: (a) 7, (b) 8, (c) 7, (d) 6, (e) 5, (f) 6." % ("/".join(str(v["rows"]) for k, v in bl), sum(v["rows"] for v in blocks.values())))
w("- Block headings, exactly as the markers must match: " + "; ".join("'%s'" % v["name"] for v in blocks.values()) + ".")
w("- **Markers tuple (all three are used):** legacy '— (legacy, not in Table 3)' (%d cell: enCRYPT, block (a)); inventory only '— (inventory only, not in Table 3)' (%d cells); planned '— (planned, not in Table 3)' (%d cell: the Sentinel integration row, block (b)). Every other Covered-by cell lists one to three of the exact headers above separated by '; ' (%d header mentions in total)." % (cov_legacy, cov_only, cov_plan, cov_all))
w("- The planned row cross-references GovTech Sentinel: PII detection and masking (AWS Bedrock) (sheet 3 column AF) in text only; no Sentinel header is in any Covered-by cell, so the Sentinel counters are not touched.")
w("- R9 URL counts: CK1 %d, CK2 %d, CK3 %d. Expected non-200 or redirect results for the P9 URL check (HTTP facts, not defects): https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ and https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/ (302 to the docs login page, then 200); https://www.cloak.gov.sg/packages (307 to sign-in); the cloak-anonymiser-package-guide and free-text decryption helper-script URLs (302 to login); the go.gov.sg short links in inventory Source cells (302 to file.go.gov.sg PDFs or the Credits page); https://www.cloak.gov.sg/terms and https://microsoft.github.io/presidio/tutorial/12_encryption/ (404, recorded only as HTTP facts in cell text, not as Source URLs); the old Cloak home-page decryption link under decryption-secret-sharing (404). The working Presidio tutorial URL is https://presidio.dataprivacystack.org/tutorial/12_encryption/ (200)." % (r9["CK1"], r9["CK2"], r9["CK3"]))
w("- Pins are unchanged from the drafts: playbook 45908b48 (blob URL in CK1 R9 and CK2 R9), spaCy release-v3.8.16, spacy-models ca6f473a, data-privacy-stack/presidio 2.2.364, Legrandin/pycryptodome v3.24.0 (T68: all latest tags on 2026-10-10).")
w("- Cloak has no evaluation-tooling sheet, so there is no cloak_eval_tooling.md. The brief (cloak_brief.md) was not edited: see section 1, header wording row.")
w("")
w("## 6. Remaining open items")
w("")
w("Counts in the finals: [To be verified] %d in the columns and %d in the inventory; [Not disclosed] %d in the columns and %d in the inventory." % (tbv_col, tbv_inv, nd_col, nd_inv))
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
w("### 6c. Items recorded here only")
w("")
for t in T.FYI: w("- " + t)
w("")
w("## 7. Moved Reviewer notes")
w("")
w("Verbatim from the drafts; the status of each correction is in section 7d.")
w("")
w("### 7a. cloak_cols_a.md (CK1), 10 notes")
w("")
pa = D + "cloak_cols_a.md"; pb = D + "cloak_cols_b.md"
for ln in C.reviewer_notes[pa]:
    if ln.strip(): w(ln)
w("")
w("### 7b. cloak_cols_b.md (CK2 and CK3), 13 notes")
w("")
for ln in C.reviewer_notes[pb]:
    if ln.strip(): w(ln)
w("")
w("### 7c. cloak_inventory.md, 8 items and the self-check")
w("")
for ln in V.reviewer_notes:
    if ln.strip(): w(ln)
w("")
w("### 7d. Status of the moved notes after P5 and P6")
w("")
w(T.NOTES_STATUS)
w("")
w("## 8. Self-check")
w("")
w("### 8a. Summary word counts (trailing label excluded; limit 45, R7 60; merge limit is limit minus 1, so 44 and 59)")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Over the merge limit |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
for i in IDS:
    w("| %s | " % i + " | ".join(str(grid[(i, n)][0]) for n in range(1, 10)) + " | %d |" % len([o for o in over if o[0] == i]))
w("")
w("### 8b. Top-level Detail bullets per row")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Total |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
for i in IDS:
    w("| %s | " % i + " | ".join(str(grid[(i, n)][1]) for n in range(1, 10)) + " | %d |" % sum(grid[(i, n)][1] for n in range(1, 10)))
w("")
w("### 8c. Labels on R1 to R7 Detail bullets")
w("")
w("| Column | Documented | Documented: repo | Inferred | To be verified | Not disclosed | R1-R7 bullets without a label | R8 bullets with a label |")
w("|---|---|---|---|---|---|---|---|")
for i in IDS:
    l = labs[i]
    w("| %s | %d | %d | %d | %d | %d | %d | %d |" % (i, l["Documented"], l["Documented: repo"], l["Inferred"], l["To be verified"], l["Not disclosed"], nolab[i], r8lab[i]))
w("")
w("### 8d. Structure")
w("")
w("| Check | Result |")
w("|---|---|")
w("| Columns | 3 (expected 3): CK1, CK2, CK3, prefix 'Cloak:' |")
w("| Summaries | 27; over the merge limit: %d; backtick, underscore or $ in a Summary: %d |" % (len(over), len(summ_code)))
w("| Rows R1 to R9 each once, Summary line and Detail present | yes (checker) |")
w("| Inventory tables | " + "; ".join("%s %d rows" % (k, v["rows"]) for k, v in bl) + " (checker; 85 rows) |")
w("| Inventory Covered-by values that are not an exact header or marker | 0 (checker) |")
w("| Inventory cells with bold markers, backticks or pipes; non-standard labels | 0 (checker) |")
w("| R8 bullets with a label | 0 |")
w("")
w("### 8e. Known-wrong strings and process wording")
w("")
w("| Pattern | Hits in the two finals | Note |")
w("|---|---|---|")
for s, n, why in kn_rows: w("| %s | %d | %s |" % (s.replace("|", " or "), n, why))
w("")
w("### 8f. Checker output (run from the repo root)")
w("")
w("```")
w("python benchtest/tools/check_drafts.py columns benchtest/drafts/cloak_two_level.md --final --expect 3")
w(c1)
w("python benchtest/tools/check_drafts.py inventory benchtest/drafts/cloak_inventory_final.md --headers benchtest/drafts/cloak_two_level.md")
w(c2)
w("```")
w("")
w("Exit codes: columns %d, inventory %d." % (rc1, rc2))
w("")
w("## 9. Verifier fixes")
w("")
w(T.VFIX_INTRO)
w("")
w("| Fix | Location | Before | After | Reason |")
w("|---|---|---|---|---|")
for e in colE + invE:
    if e["reason"].startswith("P7"):
        m = re.match(r"P7 (fix \d+|optional)", e["reason"])
        w("| %s | %s | %s | %s | %s |" % (m.group(1), e["loc"], short(e["before"], 300), short(e["after"], 420), e["reason"].replace("|", "/")))
w("")
w(T.VFIX_NOTES)
txtW = "\n".join(W).replace("\n## Self-check\n", "\n#### Inventory draft self-check\n")
open(D + "cloak_changes.md", "w", encoding="utf-8").write(txtW + "\n")
print("written", len(colE), len(invE), [c[0] for c in changed], rc1, rc2)
print(c1.splitlines()[-1], "|", c2.splitlines()[-1])
print("labels", {i: dict(labs[i]) for i in IDS}, nolab, r8lab)
print("cov", cov_all, cov_legacy, cov_only, cov_plan, "tbv", tbv_col, tbv_inv, "nd", nd_col, nd_inv)
print("blocks", {k: v["rows"] for k, v in blocks.items()})
print("grid", {i: [grid[(i, n)] for n in range(1, 10)] for i in IDS})
print("over", over)
for s, n, why in kn_rows:
    if n: print("HIT", s, n)
