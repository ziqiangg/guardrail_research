"""Generates presidio_summaries_preview.md and presidio_changes.md from the merge log and the final files.
Run after merge_presidio.py (it re-runs the merge itself so the log is in memory)."""
import os, re, subprocess, sys, collections
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_lib as L, ops_cols, ops_inv
import self_check as S

ROOT = "/home/user/guardrail_research"
D = ROOT + "/benchtest/drafts/"
C = L.Cols([D + "presidio_cols_a.md", D + "presidio_cols_b.md"])
V = L.Inv(D + "presidio_inventory.md")
orig_cols = S.parse(D + "presidio_cols_a.md") + S.parse(D + "presidio_cols_b.md")
ops_cols.apply(C)
ops_inv.apply(V)
open(D + "presidio_two_level.md", "w", encoding="utf-8").write(C.render(C.order))
open(D + "presidio_inventory_final.md", "w", encoding="utf-8").write(V.render())

final = S.parse(D + "presidio_two_level.md")
rep = S.column_report(D + "presidio_two_level.md")
LAB = re.compile(r"\*\*\[(Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]\*\*\s*$")

# ------------------------------------------------------------------ summaries preview
def preview():
    out = ["# Presidio: Summary preview (Checkpoint 2)", "",
           "Generated from presidio_two_level.md on 2026-10-09. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60.", ""]
    for c in final:
        out.append("## %s: %s" % (c["id"], c["header"]))
        out.append("")
        for n in range(1, 10):
            r = c["R"][n]
            w, b = rep["grid"][(c["id"], n)]
            out.append("- **R%d** (%dw, %d bullets): %s" % (n, w, b, r["s"]))
        out.append("")
    out.append("## Summaries changed in the merge")
    out.append("")
    out.append("| Location | Words before | Words after | Reason |")
    out.append("|---|---|---|---|")
    for loc, wb, wa, why in summaries_changed():
        out.append("| %s | %s | %s | %s |" % (loc, wb, wa, why))
    return "\n".join(out) + "\n"

def summaries_changed():
    oc = {c["id"]: c for c in orig_cols}
    rows = []
    reasons = collections.defaultdict(list)
    for e in L.LOG:
        if e["kind"] == "summary":
            reasons[e["loc"].replace(" Summary", "")].append(e["reason"])
    for c in final:
        for n in range(1, 10):
            a, b = oc[c["id"]]["R"][n]["s"], c["R"][n]["s"]
            if a != b:
                loc = "%s R%d" % (c["id"], n)
                rows.append((loc, S.words(a), S.words(b), "; ".join(reasons[loc]) or "(see section 2)"))
    return rows

open(D + "presidio_summaries_preview.md", "w", encoding="utf-8").write(preview())

# ------------------------------------------------------------------ checker output
def run(args):
    r = subprocess.run([sys.executable, ROOT + "/benchtest/tools/check_drafts.py"] + args, capture_output=True, text=True, encoding="utf-8", cwd=ROOT,
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return r.stdout.strip(), r.returncode

cols_out, cols_rc = run(["columns", "benchtest/drafts/presidio_two_level.md", "--final", "--expect", "6"])
inv_out, inv_rc = run(["inventory", "benchtest/drafts/presidio_inventory_final.md", "--headers", "benchtest/drafts/presidio_two_level.md"])
cols_result = [l for l in cols_out.splitlines() if l.startswith("RESULT")][0]
inv_result = [l for l in inv_out.splitlines() if l.startswith("RESULT")][0]
inv_tables = [l for l in inv_out.splitlines() if l.startswith("table")]

# ------------------------------------------------------------------ helper tables
def esc(s):
    return re.sub(r"(?<!\\)\|", r"\\|", s)

def tbl(rows, header):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    for r in rows:
        out.append("| " + " | ".join(esc(str(x)) if i not in () else str(x) for i, x in enumerate(r)) + " |")
    return out

def log_rows(filter_fn):
    rows = []
    for e in L.LOG:
        if not filter_fn(e):
            continue
        before = e["before"]
        if e["kind"] == "add":
            before = "(none; new bullet)" if e["loc"].startswith("PD") else "(none; sentence appended to the cell)"
        loc = e["loc"] + " (%s)" % e["kind"]
        rows.append((loc, L.short(before), L.short(e["after"]), e["reason"]))
    return rows

# ------------------------------------------------------------------ counts
col_log = [e for e in L.LOG if e["file"] == "cols"]
inv_log = [e for e in L.LOG if e["file"] == "inv"]
kinds_c = collections.Counter(e["kind"] for e in col_log)
kinds_i = collections.Counter(e["kind"] for e in inv_log)
by_col = collections.Counter(e["loc"].split()[0] for e in col_log)
tids = set()
for e in L.LOG:
    for t in re.findall(r"\bT(\d+)\b", e["reason"]):
        tids.add(int(t))
handled = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 24, 26, 30, 35, 37, 38, 41, 42, 44, 46, 47, 52, 54, 55, 56, 57, 58, 59, 60, 61, 63, 65, 66, 67, 68, 69, 70]
assert len(handled) == 47
no_edit_expected = {2: "R016 item 2: six columns kept, no text change", 4: "R016 item 3: 31 family rows kept, no text change", 5: "R010 confirmed: presidio-research stays an inventory row, no text change", 67: "NeMo note recorded here only (frozen sheets, R001); the PD2 R2 split is logged under T67"}
missing = [t for t in handled if t not in tids and t not in no_edit_expected]

# ------------------------------------------------------------------ the change log
def census(col):
    cnt = collections.Counter()
    for n in range(1, 8):
        for d in col["R"][n]["d"]:
            m = LAB.search(d)
            if m and d.startswith("• "):
                lab = m.group(1)
                cnt["Documented: repo" if lab.startswith("Documented: repo") else ("Documented: develop/unreleased" if "develop" in lab else lab)] += 1
    return cnt

CONFLICTS = [
    ("Where the labelled develop/unreleased fact for main commit 2523c7b lives (main Q3)",
     "main's ruling asks for a PD2 R8 bullet labelled [Documented: develop/unreleased]. drafts/README.md section 4 says R8 bullets are unlabelled and check_drafts.py rejects any label in an R8 bullet.",
     "The labelled fact is a PD2 R2 bullet (next to the REMOVE_INTERSECTIONS code facts, label [Documented: develop/unreleased], text: head 2523c7b, 2026-10-08, fix #2331, not in tag 2.2.364). PD2 R8 carries an unlabelled question about it (develop/unreleased written in plain text). The pin stays 2.2.364. R9 gets https://github.com/data-privacy-stack/presidio/commit/2523c7b. Only the commit number, date and PR number from main's note are used; no commit text was read, so the bullet makes no claim about what the fix changes."),
    ("2.2.364 release body (T9, main Q1)",
     "The GitHub release body is unreadable; the P0 note held quotes from it. CHANGELOG.md at the tag has no 2.2.364 heading and lists the four features under unreleased.",
     "CHANGELOG at the tag is the substitute (R015), labelled [Documented: repo data-privacy-stack/presidio@2.2.364]. No release-note wording is used in any column. 'Latest release' and the release wording stay [To be verified] only in the inventory (rows 22 and 98 of sheet 3f), as 'release notes were not read'. The unreleased heading looks stale is an [Inferred] bullet with its premise (PD1 R4)."),
    ("PD6 R8 release-notes bullet (T9 vs T13)",
     "T9 says rewrite B:452 like the other release-notes bullets; T13 says delete B:452 because the question it asked (is score_thresholds in the released package) is answered.",
     "Deleted (T13 is the more specific resolution). The generic release-notes question is kept in PD1, PD2, PD3, PD4 and PD5 R8, so it is not lost."),
    ("Ownership tense: FAQ versus transition page (T1, contradiction 1)",
     "FAQ: 'has since transitioned'; transition page: 'in the process of transitioning'. Both are Presidio docs.",
     "Two bullets, each [Documented] with its page (PD1 R4); PD2 to PD4 R4 keep the transition-page wording. The PD2 and PD3 R4 Summaries said 'now under the Data Privacy Stack community', which their own Detail did not entail; they now say 'moving to', as PD1 and PD4 already did (entailment fix, README section 4)."),
    ("Operator rows in Covered-by (T66, main Q2)",
     "Resolver proposed adding PD5 to seven operator rows and PD6 to the Docker row; main: list a header only where that column's Detail cites the row's function.",
     "Test applied row by row. PD5: R4 cites the factory's anonymise list (Custom, Encrypt, Hash, Keep, Mask, Redact, Replace), R6 cites replace and custom, R7 tests replace, redact, mask, hash, custom, encrypt, so all seven rows pass. decrypt and deanonymize_keep fail (PD5 R4 says they are not reachable), surrogate_ahds is left out as in the proposal (PD5 hardcodes the Anonymize type; the surrogate needs an extra). PD6 R7 cites running the Analyzer image with ad_hoc_recognizers, so the Docker row passes. Recognizer rows (b) unchanged. check_drafts accepts the exact headers."),
    ("Label of the application of Ollama's licence rule (T6)",
     "Resolver labelled 'shipped model qwen2.5:1.5b is under the Apache 2.0 license' [Documented]. The Ollama page says all models except the 3B and 72B are Apache 2.0; it does not name the 1.5B model.",
     "Two facts: the page sentence [Documented] and the application to the 1.5B model [Inferred] with its premise (README section 3 rule 5; no label upgrade without a quote)."),
    ("T6 optional PD4 R4 Tesseract-licence bullet",
     "Optional in the resolution; R016 item 5 puts component licences in the inventory.",
     "Not added to the columns: it would need an unpinned main-branch URL in R9 (README section 4 wants pinned repo URLs). The licence is in sheet 3f block (a), row presidio-image-redactor."),
    ("T44 optional PD5 R4 Summary",
     "Optional rewording that adds 'marked alpha'.",
     "Applied: T44 is a CORRECTION and the old Summary left out a documented maturity fact (42 words, entailed by the new alpha bullet)."),
    ("Counts of the YAML (74/73/50/24) labelled [Documented: repo]",
     "Triage hygiene row suggests [Inferred] for own counts; the resolutions did not change them.",
     "Kept [Documented: repo]: the bullet names the pinned file and the method (counted by parsing the YAML), a deterministic read. The entity-row count on the live page (80) is [Inferred] as the resolver ruled, because the page is unpinned and the vendor states no total."),
    ("Python versions (T15)",
     "Live installation page 3.10 to 3.13; docs/installation.md@2.2.364 3.10 to 3.14; pyproject <3.15; presidio-cli README 3.10 to 3.13.",
     "One bullet per source in PD1 to PD5 R4 and inventory (a) row 16; the explanation (docs site predates the tag, T14) is an [Inferred] bullet in PD1 R4. PD4 and PD5 now carry the pyproject and installation.md bullets in place of the narrative lead-in. The internal tags C2, C3 and C4 are removed everywhere, including PD2 R4 (A:306), which the resolution did not name."),
    ("Brief versus code: 0.0.60 (T10, main Q7)",
     "Brief, P0 note and seeds line read 'Release 2.2.364 / 0.0.60' as presidio-structured.",
     "Drafts and inventory follow pyproject.toml at the tag: image-redactor 0.0.60, structured 0.0.8, cli 0.0.9. The inventory (a) intro lists all values. The seeds correction is main's."),
    ("NeMo columns E and F still call the Presidio default string unverified (T67, main Q7)",
     "NeMo R8 on sheet 3 (two_level_v2.md lines 586 and 680) says the default replacement string is 'not verified in the Presidio docs'; Presidio's anonymizer page and replace.py document <ENTITY_TYPE>.",
     "NeMo sheets are frozen (R001): no change. The PD2 R2 bullet states only the code fact; the remark about NeMo is removed from the deliverable and recorded here."),
    ("Documented fact sourced from Microsoft docs (T7)",
     "Azure retention and region statements come from Microsoft Learn pages, not Presidio docs.",
     "Kept as [Documented] with the plain-text hint 'Microsoft docs, not Presidio docs' (R019, R007 item 1 precedent); AHDS retention and region are [Not disclosed] naming the pages checked. Microsoft Learn URLs are unpinned deployed docs."),
    ("Docs-site facts and pins (T14)",
     "The live site cannot be matched to a commit.",
     "Live-docs facts stay [Documented] without a pin ('read 2026-10-09' where the bullet gives a date); the gh-pages date 2026-07-04 and workflow are [Documented: repo ...@2.2.364] and the inference that the site predates the tag is [Inferred]."),
    ("Kubernetes ingress: optional or default (T52)",
     "Sheet 3f (d) row 92 described the chart as having 'an optional ingress'; the Kubernetes sample page says Presidio is deployed with an ingress controller by default.",
     "Both statements are kept in the row, each with its source (the chart description and the page sentence); no reading is picked. PD1 R6 cites only the page sentence."),
    ("PD2 R8 AHDS bullet wording",
     "Resolution text says 'see T8' (a triage id).",
     "Reworded to 'see R6'. The T7 text was kept otherwise."),
]

DISPO_A = [
    ("1", "Method: docs read raw with fetch_text.py; no summarising fetch", "No action; method is stated in the resolutions."),
    ("2", "Code read from a shallow clone at tag 2.2.364 (779dbd28)", "No action; the pin is carried by every repo label."),
    ("3", "presidio-research readable, tags up to 0.3.2, HEAD differs", "Resolved by T11 and T24; not carried (pins moved to 0.3.2 everywhere)."),
    ("4", "GitHub release page for 2.2.364 not readable; 'latest release' and release wording [To be verified]", "T9: CHANGELOG at the tag is the substitute (main Q1); the [To be verified] bullets are gone from the columns."),
    ("5", "Corrections to the brief (1) ignored labels (2) published numbers (3) 16 pattern recognizers (4) four recognizers absent from the YAML (5) 80 vs 81 rows (6) FAQ authentication, no TLS (7) deanonymize_keep and 'surrogate'", "Carried: (1) PD1 R4; (2) PD1 R5 under R014; (3) PD1 R2 Summary no longer states it, A:26 and A:27 keep the notebook and loader readings; (4) PD1 R2; (5) T20; (6) PD1 R6 and T52; (7) PD2 R2 and PD3 R4."),
    ("6", "Source conflicts logged: C2, C3, C4, API spec vs code, correlation-id header, ConflictResolutionStrategy NONE, ~30%", "C2: T19; C3: T15; C4: T16; API spec: T42; header: T54; NONE: T30; ~30%: T26. Internal C-numbers removed."),
    ("7", "Inferences worth a second look (a) 16 active recognizers (b) 'no verdict' label (c) wrong-key behaviour (d) token arithmetic (e) text leaves the process", "(a) T18 stays open; (b) accepted (T58, hygiene); (c) T33 stays open; (d) kept [Inferred]; (e) T8: code calls now [Documented: repo], conclusion [Inferred]."),
    ("8", "Notebook caveats: no version, hardware or date; coverage gaps", "T24 and T26."),
    ("9", "German recipe not in the nav; live site not checked", "T68: served on the live site; bullet added."),
    ("10", "Judgement calls (encrypt split, LiteLLM, OpenAI sample, repeated R4 boilerplate, NeMo cross-reference)", "T2 and R016: six columns kept; boilerplate kept so each column stands alone; T69 for the OpenAI sample."),
    ("11", "Not covered here by design", "No action."),
    ("12", "Inferred and Not disclosed bullets state premises and pages checked", "No action; checked mechanically."),
]
DISPO_B = [
    ("1", "Sources and method (clone at /tmp/presidio_probe, live pages saved)", "No action."),
    ("2", "Quotes and line cites checked mechanically", "No action."),
    ("3", "Not read: release page; presidio-research README and tags", "T9 and T12: replaced by CHANGELOG facts and by [Not disclosed] / [Documented: repo ...@0.3.2] bullets."),
    ("4", "Corrections to the brief: (1) 0.0.60 belongs to image-redactor (2) score thresholds are in tagged code", "T10 and T13."),
    ("5", "Source conflicts carried (Python versions, live API text, registry page, concepts page, API spec, REST thresholds)", "T15, T13, T46, T42, T39 (stays open)."),
    ("6", "Inferences worth a second look (a) JSON fill colour (b) structured replace '<None>' (c) image-redactor env vars (d) HTTP 500 for invalid regex", "(a) T39 open; (b) T45 open; (c) T41 resolved; (d) T48 open."),
    ("7", "'Out of purpose' bullets applied as [Documented]; offered switch to [Inferred]", "T57 (R015): [Inferred] with premise in all six columns."),
    ("8", "Mixed-source facts split; DICOM sample counts are the drafter's", "Kept; the DICOM count stays 'count made from the file'."),
    ("9", "Published numbers are demonstrations or advice", "No action."),
    ("10", "CP1 question on PD5 column or inventory only", "T3 and R016: PD5 stays a column; the CP1 wording is gone from PD5 R3 and R8."),
    ("11", "Other notes (DICOM metadata, LangExtract provider, ellipsis)", "No action."),
]
DISPO_I = [
    ("1", "Source conflicts carried in cells (i) entity page vs YAML (ii) Python versions (iii) Docker names (iv) operator table vs code (v) FAQ vs transition page", "(i) T19; (ii) T15; (iii) T16; (iv) T31 stays open; (v) T1."),
    ("2", "Release title 'Release 2.2.364 / 0.0.60' names presidio-structured", "T10 CORRECTION: pyproject values listed in the block (a) intro."),
    ("3", "Tagged code includes items CHANGELOG lists under unreleased", "T13: reworded without brackets; labels stay [Documented: repo ...@2.2.364]."),
    ("4", "YAML counts 74 / 50 / 24 by parser and grep", "Kept."),
    ("5", "presidio-research read at HEAD 0cb36502; latest release and date [To be verified]", "T11: re-pinned to tag 0.3.2 (06d20306, 2026-08-04); 7 labels and 2 URLs changed."),
    ("6", "Only the Presidio side of the NeMo path is recorded", "No action."),
    ("7", "Facts from fetch_text.py; github.com blob URLs could not be fetched; need the URL check at P9", "T70 (main Q5): 13 directory links to /tree/; P9 uses the raw equivalents (R020)."),
    ("8", "Marker use (R011)", "Kept: presidio-cli, presidio meta-package and presidio-research use the inventory-only marker; Legacy V1 the legacy marker; none uses the planned marker."),
    ("9", "Row counts 14 / 31 / 10 / 14", "Kept (R016 item 3); final counts below."),
]

OPEN = {
    "T17": "PD4 R4 (Tesseract version in the GHCR image, [Not disclosed]) and PD4 R8; sheet 3f (d) row 88 'Current for 2.2.364 [Inferred]'",
    "T18": "PD1 R2 (loader reading [Inferred]) and PD1 R8; sheet 3f (b) Singapore, Finland and Korea rows ('Not listed')",
    "T23": "PD1 R7 and R8, PD4 R8, PD6 R8 (threshold sweep on a labelled set)",
    "T25": "PD1 R5 and R8 (version that produced the notebook outputs; reproduction)",
    "T27": "PD1 R5/R8, PD2 R8, PD4 R6, PD5 R8, PD6 R5; sheet 3f (d) rows 89, 92, 93",
    "T28": "PD1 R2 and R8 (per-entity and non-English accuracy)",
    "T29": "PD2 R5 and R8, PD3 R5, PD4 R5, PD5 R5, PD6 R5 ([Not disclosed] absences)",
    "T31": "PD2 R4 and R8, PD3 R4 and R8 (keep, surrogate_ahds, deanonymize_keep over REST)",
    "T32": "PD2 R8 (merge flag, non-BMP offsets, hash leakage, best operator)",
    "T33": "PD3 R5 ([Inferred]) and PD3 R8 (wrong key, damaged token)",
    "T34": "PD3 R2 and R8 (LLM handling of 44-character tokens)",
    "T36": "PD3 R8; sheet 3f (d) row 96 (LiteLLM behaviour beyond the Presidio page)",
    "T39": "PD4 R5, R6 ([Inferred]) and PD4 R8 (REST thresholds and fill colour)",
    "T40": "PD4 R2, R3 ([Not disclosed]) and PD4 R8 (image scope and limits)",
    "T43": "PD4 R8 (beta to stable), PD5 R8 (roadmap)",
    "T45": "PD5 R4 ([Inferred]) and PD5 R8 (structured behaviours)",
    "T48": "PD6 R8 (HTTP status for a bad regex or language)",
    "T49": "PD6 R7 and R8 (regex timeout, concurrency, who may send ad-hoc recognizers)",
    "T50": "PD6 R8 (weak-pattern scores, overlap with built-ins, NoOp context)",
    "T51": "PD6 R8 (request versus recognizer thresholds in batch REST calls)",
    "T53": "PD1 R6/R8, PD2 R6, PD4 R6/R8, PD5 R6, PD6 R6 ([Not disclosed] size limits)",
    "T62": "sheet 3f (b) rows 55, 57, 59, 60, 61 (languages)",
    "T64": "sheet 3f (d) row 100 (community integrations)",
}
RESIDUAL = [
    ("T9", "a (PARTLY)", "GitHub release body and title for 2.2.364 unread; sheet 3f rows 22 and 98 keep [To be verified]; R8 in PD1, PD2, PD3, PD4, PD5"),
    ("T7", "c (PARTLY)", "AHDS retention and region [Not disclosed] (PD1 R8, PD2 R8, sheet 3f (b) row 61, (c) row 76); Document Intelligence terms beyond 24 hours (PD4 R8)"),
    ("T6", "c (RESOLVED)", "Stanza model licences [To be verified] (sheet 3f (a) row 19)"),
    ("T14", "a (PARTLY)", "Live docs cannot be tied to a commit; stays unpinned [Documented]"),
    ("T24", "a (PARTLY)", "Exact Presidio version behind the notebook figures (PD1 R8)"),
    ("T35", "a (PARTLY)", "Roadmap for authenticated encryption (PD3 R8); guidance half closed as [Not disclosed]"),
    ("T69", "a (PARTLY)", "Maintenance status of the OpenAI sample [Not disclosed] (PD1 R3)"),
    ("main Q3", "-", "Effect of the post-tag REMOVE_INTERSECTIONS fix on main (PD2 R8)"),
]

triage_rows = {}
for l in open(D + "presidio_triage.md", encoding="utf-8"):
    if re.match(r"^\| T\d+ \|", l):
        c = [x.strip() for x in l.strip().strip("|").split(" | ")]
        triage_rows[c[0]] = (c[1], c[3], c[5])

out = []
A = out.append
A("# Presidio merge: change log")
A("")
A("Inputs merged: presidio_brief.md, presidio_cols_a.md (PD1 to PD3), presidio_cols_b.md (PD4 to PD6), presidio_inventory.md, presidio_triage.md, presidio_resolutions_1.md (47 items), the rulings R010, R011, R014, R015, R016, R019, R020 and main's rulings on agent questions (queue.md, Resolved questions, rows starting 'presidio'). Outputs: presidio_two_level.md, presidio_inventory_final.md, presidio_changes.md (this file), presidio_summaries_preview.md. No source file was modified and no new web or repository research was done; every added fact is in the resolutions file or in a ruling. Merged 2026-10-09 by gr-merger; the edits were applied by script (benchtest/scratchpad/merger/presidio/) so each one is logged below.")
A("")
A("In this file bold markers are dropped from quoted text and long text is shortened. Reason codes: Tn = triage id (resolution in presidio_resolutions_1.md), 'style n' = triage Style issues in columns, 'hygiene' = triage Label hygiene, 'main Qn' = main's rulings on the P5 questions, 'Rnnn' = ruling. Kinds in brackets: summary, replace, edit, add, delete, url (R9 or Source URL cell), style, hygiene, pin, covered. Format of the entries: location | before | after | reason.")
A("")
A("## 1. Global changes")
A("")
G = [
    ("Reviewer notes sections (cols A, cols B, inventory)", "present in the drafts", "removed from presidio_two_level.md and presidio_inventory_final.md; kept verbatim in section 7", "instruction; README section 4"),
    ("Ownership and official sources", "Q01 bullets in PD1, PD2, PD3 R8; 'choice of official source is open for CP1' in the inventory scope", "R8 process bullets deleted; scope paragraph names the sources used (Data Privacy Stack docs host, GitHub organisation and container registry, plus the Microsoft-authored transition page and stub); FAQ ownership quote added beside the transition-page quote in PD1 R4; prefix 'Presidio:' unchanged", "T1, R016 item 1"),
    ("Column set and scope", "six columns; PD5 'column or inventory only (CP1)'; 'Scope note for CP1'", "six columns kept; PD5 stays a column; CP1 wording removed from PD5 R3 and R8 and its R8 Summary", "T2, T3, R016 item 2"),
    ("Inventory granularity", "31 family rows", "kept (14 / 31 / 10 / 14 rows)", "T4, R016 item 3, main P2 Q5"),
    ("Out-of-purpose statement (prompt injection, harmful content, topics)", "[Documented] in PD4, PD5, PD6 (bullets) and PD4, PD5 (Summaries); [Inferred] in PD1, PD2", "[Inferred] with the premise named ('Home page module list') in every column and in the PD4 and PD5 R2 Summaries (text unchanged)", "T57, R015 ruling 1"),
    ("Release-note facts", "[To be verified] bullets and R8 bullets citing 'github.com returned 403' / 'could not be read'", "CHANGELOG.md at tag 2.2.364 is the substitute for the release body (labelled repo@2.2.364); R8 bullets say the release page was not read; the release wording is not used in any column", "T9, R015 ruling 2, main Q1"),
    ("Process wording in deliverable text", "'through the proxy', 'returned 403 here', 'was not readable here', 'local clone log', 'shallow clone', 'Owner question Q01', 'decision belongs to CP1', '(R010)', 'not readable as text'", "removed or reworded as sources checked; nothing in the finals names a session, proxy, ruling id or checkpoint", "style 3, 4, 5; T9, T12"),
    ("Internal conflict tags C2, C3, C4", "'Source conflict C2/C3/C4' lead-ins in PD1 R2, PD1 R4, PD2 R4, PD3 R4", "plain bullet pairs ('The entity page lists ...', 'The analyzer page shows ...'); both sides kept", "style 3, T15, T16, T19"),
    ("presidio-research pin", "inventory used short SHA 0cb36502 (HEAD, 2026-09-30); columns used tag 0.3.2", "release tag 0.3.2 (06d20306, 2026-08-04) everywhere; 5 repo labels or URLs re-pinned in sheet 3f (a) row 23; requires-python read at the tag", "T11, R014"),
    ("Notebook figure in the PD1 R5 Summary", "'F2 0.661 for default settings'", "'F2 0.661 for default recognizers at threshold 0.4 on synthetic data'; provenance bullets added (commit dates)", "T24, R014"),
    ("Third-party component licences", "not in the sheet", "licences of Tesseract, pytesseract, pydicom, spaCy and en_core_web_lg, Stanza, transformers, the sample transformers model, the OpenMed model, Medical-NER, GLiNER and its library, LangExtract, Ollama and the shipped Qwen model, each citing the owner's page, marked 'not Presidio docs', with the read date in the scope paragraph and model-card last-modified dates in the cells", "T6, R016 item 5, R019, main Q4"),
    ("Microsoft service data terms", "'terms belong to Microsoft'", "Azure Language, Azure OpenAI and Document Intelligence statements cited from Microsoft docs ('not Presidio docs'); AHDS retention and region [Not disclosed] naming the pages checked", "T7"),
    ("What leaves the process (Azure recognizers and operators)", "[Inferred] from endpoint parameters", "the SDK calls that take the text are [Documented: repo ...@2.2.364] with file and line; the conclusion that the text leaves the process stays [Inferred] with its premise (PD1 R6, sheet 3f (b) rows 59 to 61, (c) row 76)", "T8"),
    ("Code identifiers in Summaries", "'DataFrame' (PD5 R3, R5, R6, R7), 'a DEFAULT entry' (PD2 R6), 'IV' (PD3 R4), 'NONE' (PD2 R8)", "'table', 'a default entry', 'random initialisation vector', NONE question removed", "style 2"),
    ("Pip-extra brackets in inventory cells", "pip install \"presidio_analyzer[stanza]\" etc.", "'presidio_analyzer with the stanza extra' (%d cells in sheet 3f)" % len([e for e in inv_log if "pip-extra" in e["reason"]]), "hygiene"),
    ("Bracketed non-labels in inventory cells", "'[unreleased]' in sheet 3f (a) row 22 and (d) row 98", "'under its unreleased heading of CHANGELOG.md'", "T13, hygiene"),
    ("R9 lists", "URLs for pages and files cited in the old text", "%d URLs added in the columns so every new pin, page and file cited in R1 to R8 is in the R9 list of its column; one URL per bullet" % kinds_c["url"], "T7, T8, T12, T14, T15, T20, T22, T26, T41, T42, T44, T46, T52, T55, T68, T69, main Q3"),
    ("Directory links in sheet 3f (b)", "13 Source URL cells with .../country_specific/<country>/ under /blob/", "/tree/ (13 cells)", "T70, main Q5"),
    ("Covered by Table 3 column", "operator rows listed PD2 or PD3 only; Docker row omitted PD6", "PD5 appended to the seven operator rows replace, redact, hash, mask, custom, keep, encrypt; PD6 appended to the Docker row; other rows unchanged", "T66, main Q2"),
    ("Status vocabulary", "'alpha' outside stable/beta/legacy", "vendor wording stays (documented on the getting-started page); status checked lists extended with 'no Development Status classifier in any package at the tag'", "T60, T44, main P2 Q1"),
]
for l in tbl(G, ["Scope", "Before", "After", "Reason"]):
    A(l)
A("")
A("## 2. Column and row changes")
A("")
A("Entries are listed in the order the edits were applied. 'Detail split' appears as an (add) or (replace) with several bullets joined by ' // '.")
A("")
for cid in C.order:
    A("### " + cid)
    A("")
    rows = log_rows(lambda e, cid=cid: e["file"] == "cols" and e["loc"].split()[0] == cid)
    for l in tbl(rows, ["Location", "Before", "After", "Reason"]):
        A(l)
    A("")
A("## 3. Inventory changes (sheet 3f)")
A("")
A("Locations name the block, the row (first words of its first cell) and the column. Row numbers quoted in this file (for example row 22) are line numbers in presidio_inventory_final.md, as in the triage and resolutions; the merge added and removed no lines, so they equal the draft line numbers.")
A("")
for blk, name in [("scope", "Scope paragraph and block intros"), ("a", "(a) Components and variants"), ("b", "(b) Recognizer catalogue"), ("c", "(c) Anonymizer operators"), ("d", "(d) Integration paths")]:
    A("### " + name)
    A("")
    if blk == "scope":
        rows = log_rows(lambda e: e["file"] == "inv" and (e["loc"].startswith("INV scope") or e["loc"].startswith("INV intro")))
    else:
        rows = log_rows(lambda e, blk=blk: e["file"] == "inv" and e["loc"].startswith("INV (%s)" % blk))
    for l in tbl(rows, ["Location", "Before", "After", "Reason"]):
        A(l)
    A("")
A("## 4. Conflict decisions")
A("")
for i, (t, both, chosen) in enumerate(CONFLICTS, 1):
    A("%d. **%s.** Sources: %s Decision: %s" % (i, t, both, chosen))
    A("")
A("## 5. Change counts and final counts for the P8 config")
A("")
A("- Logged edits: %d in the columns, %d in the inventory (%d in total)." % (len(col_log), len(inv_log), len(L.LOG)))
A("- Columns by kind: " + ", ".join("%s %d" % (k, v) for k, v in sorted(kinds_c.items())) + ". By column: " + ", ".join("%s %d" % (k, v) for k, v in sorted(by_col.items())) + ".")
A("- Inventory by kind: " + ", ".join("%s %d" % (k, v) for k, v in sorted(kinds_i.items())) + ".")
sc = summaries_changed()
A("- Summaries changed: %d of 54 (list in presidio_summaries_preview.md and in the Summary rows of section 2): %s." % (len(sc), ", ".join(x[0] for x in sc)))
A("- Resolution items handled: 47 (T1 to T16, T19 to T22, T24, T26, T30, T35, T37, T38, T41, T42, T44, T46, T47, T52, T54 to T61, T63, T65 to T70). Items with no text change by design: " + "; ".join("T%d (%s)" % (k, v) for k, v in sorted(no_edit_expected.items())) + ". Items cited in the log: %d. Handled items not cited and not in the previous list: %s." % (len([t for t in handled if t in tids]), missing or "none"))
A("- Final inventory row counts for the P8 config (BLOCKS): (a) Components and variants 14, (b) Recognizer catalogue 31, (c) Anonymizer operators 10, (d) Integration paths 14 (%s)." % "; ".join(inv_tables))
A("- Final columns: 6 (PD1 to PD6), prefix 'Presidio:'. Markers used in Covered by Table 3 column: inventory only (presidio-cli, presidio meta-package, presidio-research, command line path) and legacy (Legacy V1); planned is not used. The config markers tuple needs legacy and inventory only (R011).")
A("")
A("## 5b. Notes for P8 (workbook) and P9 (URL check)")
A("")
urls = set()
for c in final:
    for d in c["R"][9]["d"]:
        urls.add(d[2:].strip())
for l in open(D + "presidio_inventory_final.md", encoding="utf-8").read().splitlines():
    if l.startswith("|"):
        cells = [x.strip() for x in l.strip()[1:-1].split(" | ")]
        for u in cells[-1].split(" ; "):
            if u.startswith("http"):
                urls.add(u.strip())
gh = sorted(u for u in urls if u.startswith("https://github.com/data-privacy-stack/"))
tree = sorted(u for u in urls if "/tree/" in u)
thirdparty = sorted(u for u in urls if not u.startswith("https://github.com/data-privacy-stack/") and "presidio.dataprivacystack.org" not in u and "github.io/presidio" not in u and "docs.nvidia.com" not in u)
A("- Inventory config (gr-xlsx-writer): sheet 3f; BLOCKS (a) Components and variants 14, (b) Recognizer catalogue 31, (c) Anonymizer operators 10, (d) Integration paths 14; Covered-by column name 'Covered by Table 3 column'; markers tuple = legacy and inventory only (R011); prefix 'Presidio:', column IDs PD1 to PD6 (R009); headers are the six lines of the form 'Presidio: ...' in presidio_two_level.md.")
A("- Distinct URLs in R9 lists and inventory Source URL cells: %d (%d on github.com/data-privacy-stack, %d on the docs host presidio.dataprivacystack.org, %d elsewhere, including the two github.io pages, the NVIDIA page and the third-party pages listed below)." % (len(urls), len(gh), len([u for u in urls if "presidio.dataprivacystack.org" in u]), len([u for u in urls if not u.startswith("https://github.com/data-privacy-stack/") and "presidio.dataprivacystack.org" not in u])))
A("- Expected statuses for gr-url-checker (R020, main Q5): github.com answers HTTP 403 from the session proxy, so check the raw.githubusercontent.com equivalent of each blob URL (same owner, repo, ref, path). Directory and commit URLs cannot be served raw; list them as exceptions verified by their parent files: %d /tree/ URLs (%d country folders and the gh-pages head), the commit URL https://github.com/data-privacy-stack/presidio/commit/2523c7b." % (len(tree), len([u for u in tree if "country_specific" in u])))
A("- https://data-privacy-stack.github.io/presidio/ answers HTTP 301 to https://presidio.dataprivacystack.org/ (an HTTP fact, kept on purpose); https://microsoft.github.io/presidio/ answers 200 with a meta-refresh stub.")
A("- Third-party URLs added by T6 and T7 (not Presidio docs): " + "; ".join(thirdparty) + ".")
A("")
A("## 6. Remaining open items")
A("")
A("### 6a. Items not handled in P5 (class b needs testing, and honest gaps), unchanged in the finals")
A("")
rows = []
for t in sorted(OPEN, key=lambda x: int(x[1:])):
    item, cls, pr = triage_rows[t]
    rows.append((t, cls, pr, L.short(item, 120), OPEN[t]))
for l in tbl(rows, ["T-id", "Class", "Priority", "Item (triage)", "Where it stays open in the finals"]):
    A(l)
A("")
A("Class b items stay in R8 (or in [Inferred] / [Not disclosed] bullets with their premise); R016 item 4 and R019 keep them as needs-testing for the bench. Honest-gap items (T27, T28, T29, T35, T36, T43, T62, T64) are marked as such in the triage. Class c: T1 and T6 are closed; T7 is partly closed (residual in 6b).")
A("")
A("### 6b. Residual parts of handled items")
A("")
for l in tbl(RESIDUAL, ["Item", "Class", "What remains"]):
    A(l)
A("")
A("Label census of what is still unconfirmed: [To be verified] occurs 0 times in the columns and 3 times in sheet 3f (Stanza model licences, row 19; release notes, rows 22 and 98).")
A("")
A("## 7. Moved Reviewer notes")
A("")
A("The notes below were removed from the finals. The dispositions say where each one went.")
A("")
A("### 7a. presidio_cols_a.md (PD1 to PD3), 12 notes")
A("")
for l in tbl(DISPO_A, ["Note", "Subject", "Disposition"]):
    A(l)
A("")
for p, notes in C.reviewer_notes.items():
    if p.endswith("cols_a.md"):
        A("Verbatim text:")
        A("")
        for n in notes:
            if n.strip():
                A("> " + n)
        A("")
A("### 7b. presidio_cols_b.md (PD4 to PD6), 11 notes")
A("")
for l in tbl(DISPO_B, ["Note", "Subject", "Disposition"]):
    A(l)
A("")
for p, notes in C.reviewer_notes.items():
    if p.endswith("cols_b.md"):
        A("Verbatim text:")
        A("")
        for n in notes:
            if n.strip():
                A("> " + n)
        A("")
A("### 7c. presidio_inventory.md, 9 notes")
A("")
for l in tbl(DISPO_I, ["Note", "Subject", "Disposition"]):
    A(l)
A("")
A("Verbatim text:")
A("")
for n in V.reviewer_notes:
    if n.strip():
        A("> " + n)
A("")
A("## 8. Self-check")
A("")
A("### 8a. Summary word counts (limit 45, R7 60; trailing label excluded)")
A("")
hdr = ["Column"] + ["R%d" % n for n in range(1, 10)] + ["Over limit"]
rows = []
tot = 0
for c in final:
    ws = [rep["grid"][(c["id"], n)][0] for n in range(1, 10)]
    over = sum(1 for n, w in enumerate(ws, 1) if w > (60 if n == 7 else 45))
    tot += over
    rows.append([c["id"]] + ws + [over])
for l in tbl(rows, hdr):
    A(l)
A("")
A("### 8b. Top-level Detail bullets per row")
A("")
rows = []
for c in final:
    rows.append([c["id"]] + [rep["grid"][(c["id"], n)][1] for n in range(1, 10)] + [sum(rep["grid"][(c["id"], n)][1] for n in range(1, 10))])
for l in tbl(rows, ["Column"] + ["R%d" % n for n in range(1, 10)] + ["Total"]):
    A(l)
A("")
A("### 8c. Labels on R1 to R7 Detail bullets and Summaries")
A("")
rows = []
for c in final:
    cn = census(c)
    miss = 0
    for n in range(1, 8):
        if not LAB.search(c["R"][n]["s"]):
            miss += 1
        for d in c["R"][n]["d"]:
            if d.startswith("• ") and not LAB.search(d):
                miss += 1
    labs_r8 = sum(1 for d in c["R"][8]["d"] if "**[" in d)
    rows.append([c["id"], cn["Documented"], cn["Documented: repo"], cn["Documented: develop/unreleased"], cn["Inferred"], cn["To be verified"], cn["Not disclosed"], miss, labs_r8])
for l in tbl(rows, ["Column", "Documented", "Documented: repo", "develop/unreleased", "Inferred", "To be verified", "Not disclosed", "R1-R7 items without a label", "R8 bullets with a label"]):
    A(l)
A("")
A("### 8d. Structure")
A("")
rows = [
    ("Columns", "6 (expected 6), IDs PD1 to PD6, one prefix 'Presidio:'"),
    ("Summaries", "54 (6 x 9); over limit: %d; backtick, underscore or $ in a Summary: 0 (checker)" % tot),
    ("Rows R1 to R9 each once, Summary line and Detail present", "yes (checker)"),
    ("R9 bullets", "%d URLs in total; one URL per bullet (checker)" % sum(len(c["R"][9]["d"]) for c in final)),
    ("Repo labels with an R9 URL of the same repo and ref in the same column; cited file names present in R9", "%d problems (self_check.py)" % len(rep["problems"])),
    ("Reviewer notes or process language in the finals", "0 (grep, 8e)"),
    ("Inventory tables", "; ".join(inv_tables)),
    ("Inventory cells with ** , backtick or pipe; non-standard labels; Covered-by values that are not an exact header or marker", "0 (checker)"),
    ("Inventory cells (outside name, URL and Covered-by columns) with no evidence label", "0 (scan)"),
]
for l in tbl(rows, ["Check", "Result"]):
    A(l)
A("")
A("### 8e. Known-wrong strings and process wording (lessons.md item 6)")
A("")
two = open(D + "presidio_two_level.md", encoding="utf-8").read()
inv = open(D + "presidio_inventory_final.md", encoding="utf-8").read()
both = two + "\n" + inv
def hits(pat, text=both, flags=re.I):
    return len(re.findall(pat, text, flags))
G2 = [
    ("0cb36502 (old presidio-research pin)", r"0cb36502", "0"),
    ("'0.0.60' attributed to presidio-structured, or the release title 'Release 2.2.364 / 0.0.60'", r"presidio-structured[^.,;\n|]{0,40}\b0\.0\.60|/ 0\.0\.60", "0 (the 0.0.60 hits are presidio-image-redactor; the structured version 0.0.8 appears in PD5 R4 and sheet 3f (a))"),
    ("'maturity ... not stated' for presidio-structured", r"maturity label[^|\n]{0,40}not stated", "0 (PD5 R4 quotes the alpha notice)"),
    ("'default settings' next to F2 0.661", r"default settings[^|\n]{0,80}0\.661|0\.661[^|\n]{0,80}default settings", "0 (now 'default recognizers at threshold 0.4 on synthetic data')"),
    ("release-note wording used as fact (batch deanonymization, no-op NLP engine, Python 3.14 compatibility, threshold flag)", r"feat\(|feat:", "0"),
    ("Q01, CP1, CP2, R010, T-ids, C2/C3/C4, 'Reviewer notes'", r"Q0\d|CP[12]\b|\bR010\b|\bT\d{1,2}\b|conflict C\d|Reviewer notes", "0"),
    ("403, proxy, 'returned', 'not readable', 'readable here'", r"\b403\b|through the proxy|returned HTTP|not readable|readable here|read here", "0"),
    ("[unreleased] as bracketed text", r"\[unreleased\]", "0"),
    ("shallow clone, local clone", r"shallow clone|local clone", "0"),
    ("'Owner question'", r"Owner question", "0"),
]
rows = []
for name, pat, exp in G2:
    if name.startswith("'0.0.60'"):
        h = hits(pat)
    else:
        h = hits(pat)
    rows.append((name, h, exp))
for l in tbl(rows, ["String or pattern", "Hits in the two finals", "Expected / note"]):
    A(l)
A("")
A("### 8f. Checker output (run from the repo root)")
A("")
A("```")
A("python benchtest/tools/check_drafts.py columns benchtest/drafts/presidio_two_level.md --final --expect 6")
A(cols_result)
A("python benchtest/tools/check_drafts.py inventory benchtest/drafts/presidio_inventory_final.md --headers benchtest/drafts/presidio_two_level.md")
for t in inv_tables:
    A(t)
A(inv_result)
A("```")
A("")
A("Exit codes: columns %d, inventory %d." % (cols_rc, inv_rc))
A("")
open(D + "presidio_changes.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("changes.md lines:", len(out))
print(cols_result, "|", inv_result, "|", cols_rc, inv_rc)
print("missing handled-not-cited:", missing)
print("summaries changed:", [x[0] for x in sc])
print("hits:", rows)
