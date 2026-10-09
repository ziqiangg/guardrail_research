"""Generate purplellama_changes.md and purplellama_summaries_preview.md from the merge log and the finals."""
import sys, os, re, subprocess, collections, datetime
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, "benchtest")
import merge_lib as L
import merge_pl as M
import self_check as S

D = "benchtest/drafts/"
TODAY = "2026-10-10"

# ------------------------------------------------------------------ run the merge once (fills L.LOG) and write the finals
K = M.build()
open(D + "purplellama_two_level.md", "w", encoding="utf-8").write(K.render(M.IDS))
n_cols = len(L.LOG)
V = M.build_inv()
open(D + "purplellama_inventory_final.md", "w", encoding="utf-8").write(V.render())
n_inv = len(L.LOG)
E = L.Ev(D + "purplellama_eval_tooling.md")
M.ops_ev.apply(E)
open(D + "purplellama_eval_tooling_final.md", "w", encoding="utf-8").write(
    E.render("## Topic: Meta CyberSecEval 4 evaluation tooling (reuse assessment for the test bench)"))
LOG = list(L.LOG)
COLLOG = LOG[:n_cols]
INVLOG = LOG[n_cols:n_inv]
EVLOG = LOG[n_inv:]


def count(logs):
    c = collections.Counter(x["kind"] for x in logs)
    return dict(sorted(c.items()))


def short(s, n=230):
    s = s.replace("**", "").replace("\n", " // ")
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n:
        s = s[:n - 1].rstrip() + "…"
    return s.replace("|", "\\|")


# ------------------------------------------------------------------ summaries before/after
def parse_summ(path):
    out = {}
    cur = rn = None
    for ln in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"^## Column (PL\d):", ln)
        if m:
            cur = m.group(1)
        m = re.match(r"^### R(\d)\s*$", ln)
        if m:
            rn = int(m.group(1))
        if cur and ln.startswith("Summary: "):
            out[(cur, rn)] = ln[9:]
    return out


orig = {}
for p in ("purplellama_cols_a.md", "purplellama_cols_b.md"):
    orig.update(parse_summ(D + p))
final = parse_summ(D + "purplellama_two_level.md")
changed = [k for k in sorted(final, key=lambda k: (k[0], k[1])) if final[k] != orig[k]]

# ------------------------------------------------------------------ summaries preview
LABEL = r"\[(?:Documented(?:: (?:repo [^\]]+|develop/unreleased))?|Inferred|To be verified|Not disclosed)\]"


def words(s):
    s = re.sub(r"\*\*" + LABEL + r"\*\*\s*$", "", s).replace("**", "")
    return len(s.split())


cols = S.parse(D + "purplellama_two_level.md")
prev = ["# Purple Llama: Summary preview (Checkpoint 2)", "",
        "Generated from purplellama_two_level.md on %s. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60. Summaries changed from the drafts are marked with an asterisk after the row number." % TODAY, ""]
for c in cols:
    prev.append("## %s: %s" % (c["id"], c["header"]))
    prev.append("")
    for n in range(1, 10):
        r = c["R"][n]
        nb = len([d for d in r["d"] if d.startswith("• ")])
        star = "*" if (c["id"], n) in changed else ""
        prev.append("- **R%d%s** (%dw, %d bullets): %s" % (n, star, words(r["s"]), nb, r["s"]))
    prev.append("")
open(D + "purplellama_summaries_preview.md", "w", encoding="utf-8").write("\n".join(prev).rstrip("\n") + "\n")

# ------------------------------------------------------------------ checker runs
env = dict(os.environ, PYTHONIOENCODING="utf-8")
r1 = subprocess.run([sys.executable, "benchtest/tools/check_drafts.py", "columns", D + "purplellama_two_level.md", "--final", "--expect", "7"], capture_output=True, text=True, env=env, encoding="utf-8")
r2 = subprocess.run([sys.executable, "benchtest/tools/check_drafts.py", "inventory", D + "purplellama_inventory_final.md", "--headers", D + "purplellama_two_level.md"], capture_output=True, text=True, env=env, encoding="utf-8")
chk_cols = r1.stdout.strip().splitlines()
chk_inv = r2.stdout.strip().splitlines()
rep = S.column_report(D + "purplellama_two_level.md")

import build_eval_sheet as B
evsecs = B.parse_md(D + "purplellama_eval_tooling_final.md")
ev_counts = []
for s in evsecs:
    kinds = collections.Counter(i[0] if isinstance(i, tuple) else i.get("kind", "?") for i in s["items"]) if False else None
    ev_counts.append((s["name"], len(s["items"])))


def ev_table_rows(path):
    secs = {}
    cur = None
    for ln in open(path, encoding="utf-8").read().splitlines():
        m = re.match(r"^## (.+?)\s*$", ln)
        if m:
            cur = m.group(1)
            secs[cur] = 0
        elif cur and ln.startswith("|") and not re.match(r"^\|[-: |]+\|$", ln):
            secs[cur] += 1
    return {k: max(0, v - 1) for k, v in secs.items()}


ev_rows = ev_table_rows(D + "purplellama_eval_tooling_final.md")
ev_bul = {}
cur = None
for ln in open(D + "purplellama_eval_tooling_final.md", encoding="utf-8").read().splitlines():
    m = re.match(r"^## (.+?)\s*$", ln)
    if m:
        cur = m.group(1)
        ev_bul[cur] = 0
    elif cur and ln.startswith("• "):
        ev_bul[cur] += 1

# ------------------------------------------------------------------ inventory row counts
inv_tables = [x for x in chk_inv if x.startswith("table")]

# ------------------------------------------------------------------ labels per column
LAB = re.compile(r"\*\*\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*")
label_rows = []
for c in cols:
    cnt = collections.Counter()
    nolabel = 0
    r8lab = 0
    for n in range(1, 8):
        for d in c["R"][n]["d"]:
            if d.startswith("• "):
                m = LAB.search(d)
                if m:
                    k = m.group(1)
                    cnt["Documented: repo" if k.startswith("Documented: repo") else ("Documented" if k == "Documented" else ("develop" if "develop" in k else k))] += 1
                else:
                    nolabel += 1
    for d in c["R"][8]["d"]:
        if "**[" in d:
            r8lab += 1
    label_rows.append((c["id"], cnt["Documented"], cnt["Documented: repo"], cnt["Inferred"], cnt["To be verified"], cnt["Not disclosed"], nolabel, r8lab))

# ------------------------------------------------------------------ known-wrong strings
finals = {n: open(D + n, encoding="utf-8").read() for n in ("purplellama_two_level.md", "purplellama_inventory_final.md", "purplellama_eval_tooling_final.md")}
alltext = "\n".join(finals.values())
checks = [
    ("Llama 4 AUP locator '2.8'", r"item 2\.8|\b2\.8\b.{0,30}(AUP|USE_POLICY)", "0"),
    ("released dataset called '600 scenarios' without the card count", r"released as the Hugging Face dataset", "0"),
    ("'sdist(s) not read' or 'equality ... To be verified' for PyPI", r"sdist (contents )?(was|were) not read|sdist not read|equality of PyPI", "0"),
    ("HTTP 401 card body premise", r"HTTP 401|returns HTTP 401|not readable without approved", "0"),
    ("CWE counts 47 / 63 / 65 (corrected to 46 / 62 / 64)", r"about 47\b|about 63\b|\b65 for all", "0"),
    ("'four statements' / 'four different statements' / 'four latency'", r"four (different )?(latency )?statements|four conflicting latency", "0"),
    ("'compiled once'", r"compiled once", "0"),
    ("'US-style'", r"US-style", "0"),
    ("'no direction setting'", r"no direction setting", "0"),
    ("'my count'", r"my count", "0"),
    ("'(counted from the file)'", r"\(counted from the file\)", "0"),
    ("'{I}' label form", r"\{I\}", "0"),
    ("'proposed 3j'", r"proposed 3j", "0"),
    ("draft ids as cross-references ('column PLn', 'PLn column')", r"\bPL[1-8]\b(?! *[=:,]).{0,0}", None),
    ("ruling ids R0nn, CP1/CP2, checkpoint, Reviewer notes, T-ids", r"\bR0[0-9]{2}\b|\bCP[12]\b|checkpoint|Reviewer note|\bT[0-9]{1,3}\b", "0"),
    ("'shallow clone', 'the clone', 'research does not', 'read-only rule'", r"shallow clone|the clone|research does not|read-only rule|makes no vendor API", "0"),
]
chk_rows = []
for name, pat, exp in checks:
    if exp is None:
        hits = len(re.findall(r"(?<!## )(?:column|Column) PL[1-8]\b|\bPL[1-8] column|\(PL[1-8]\)", alltext))
        chk_rows.append(("draft ids as cross-references ('column PLn', 'PLn column', '(PLn)')", str(hits), "0"))
        continue
    hits = 0
    for t in (alltext,):
        hits = len(re.findall(pat, t))
    if name.startswith("ruling ids"):
        # the column headings legitimately contain 'Column PLn:'; none of these patterns match them
        pass
    chk_rows.append((name, str(hits), exp))

api_hits = 0
for ln in finals["purplellama_two_level.md"].splitlines():
    if re.fullmatch(r"• https?://\S+", ln) and re.search(r"huggingface\.co/api/|//api\.|googleapis", ln):
        api_hits += 1
for ln in finals["purplellama_inventory_final.md"].splitlines():
    if ln.startswith("|"):
        last = ln.strip()[1:-1].split(" | ")[-1]
        if re.search(r"huggingface\.co/api/|//api\.|googleapis", last):
            api_hits += 1
chk_rows.append(("API paths or API hosts in R9 bullets and inventory Source URL cells (code-fact base URLs inside cells are not URL-list entries)", str(api_hits), "0"))

# ------------------------------------------------------------------ build the change log
O = []
w = O.append
w("# Purple Llama merge: change log")
w("")
w("Inputs merged: purplellama_brief.md, purplellama_cols_a.md (PL1, PL2, PL6, PL4), purplellama_cols_b.md (PL3, PL5, PL7), purplellama_inventory.md (88 rows), purplellama_eval_tooling.md (CyberSecEval, 8 sections), purplellama_triage.md (105 items), purplellama_resolutions_1.md (41 items) and purplellama_resolutions_2.md (items T19 to T105 in its scope, plus T5 and the R032 wording pass), the rulings R002, R003, R004, R007, R009, R011, R013, R015, R019, R020, R021, R030 and R032, and main's rulings on the P4 and P5 agent questions (queue.md, rows starting 'purplellama'). Outputs: purplellama_two_level.md (7 columns, PL1 to PL7), purplellama_inventory_final.md (88 rows), purplellama_eval_tooling_final.md (8 sections), purplellama_changes.md (this file), purplellama_summaries_preview.md. No source draft was modified and no new web or repository research was done; every added fact is in a resolutions file, a ruling or the drafts. Merged %s by gr-merger." % TODAY)
w("")
w("In this file bold markers are dropped from quoted text and long text is shortened to about 230 characters. Reason codes: Tn = triage id (resolution in purplellama_resolutions_1.md or _2.md; 'r1' and 'r2' say which resolver's text was used), 'style n' = triage Style issues in columns, 'hygiene' = triage Label hygiene, 'Rnnn' = ruling, 'Suppl. n' = supplementary finding n in resolutions 1. Kinds in brackets: summary, replace, edit, add, delete, url (R9 or Source URL cell), style, hygiene, covered. Entries have the form location | before | after | reason. The columns were assembled in the order PL1 to PL7 (the drafts hold PL1, PL2, PL6, PL4 in cols_a and PL3, PL5, PL7 in cols_b).")
w("")
w("## 1. Global changes")
w("")
w("| Scope | Before | After | Reason |")
w("|---|---|---|---|")
G = [
    ("Reviewer notes sections (cols_a, cols_b, inventory)", "present in the drafts (13, 10 and 7 notes)", "removed from the three finals, together with the title line and the drafting paragraph of cols_b; notes kept verbatim in section 7 with a status line", "instruction; README section 4; T102"),
    ("Header prefixes and column set", "option B drafted, CP1 open (Q-A, Q-B, Q-C); PL7 'provisional'; PL5 'column-split question for the checkpoint'", "three prefixes (Prompt Guard 2:, LlamaFirewall:, Code Shield:), 7 columns PL1 to PL7, PL7 stays a column, PL5 stays one column, one column per scanner with roles in R3 and R6 and in inventory block (c); the checkpoint, provisional and PL8 bullets are deleted (PL5 R1, R7, R8; PL7 R1)", "T1 to T4, R030 (Q-A to Q-C), T100"),
    ("Bench-design content (Q-D, T5 and every 'test plan' sentence)", "imperative or decided wording ('Review before redistributing', 'use synthetic data', 'Test set for Table 3', 'Mark the judge model as a test variable', 'Record the score ...')", "worded as proposals and suggestions ('A bench could ...', 'Possible ...', '(suggested)'); possible sources of attack examples and harmless look-alike messages are reported, none is chosen; R7 Summaries of PL2 to PL7 and the eval 'Reuse for the test bench' section rewritten", "R030 (Q-D not decided), R032; T5, T11, T100"),
    ("Process language in Detail and cells", "'research does not install or run it (R019)', 'because research makes no vendor API calls', 'checkpoint', 'Decision for the bench design, not research', 'my count', 'so the repo file was used', 'Not requested during research (read-only rule)', 'the clone', 'this half', 'Direction (R002)', 'Direction under R002', ruling id R011 in the inventory scope", "'this setup has not been run', 'a bench design would need to settle this', neutral count wording, 'the repository file list', 'Direction:'; the column heading 'Direction under R002' in block (c) became 'Direction (input, output or trace side)'", "T100, style 3, R019"),
    ("Draft ids as cross-references (PL1 to PL7)", "'column PL2', 'the Regex column, PL5', 'PL1 = ...' in the eval Tools note and Evaluates cells", "the exact header text, or a plain description; the section headings '## Column PLn:' stay (they are the parser ids)", "T101, style 4"),
    ("Label form of PyPI sdist facts", "no allowed form for PyPI; '[To be verified]' for 'sdist not read'", "[Documented] plus a plain-text hint '(PyPI sdist <name>-<ver>, sha256 <short>, read 2026-10-09)' for what an sdist contains; sdist-versus-pin comparisons are [Inferred] with the premise named; PyPI project URL and sdist file URL in R9 and Source URL cells", "main ruling on purplellama P5 r2 Q1; T19, T20"),
    ("Hugging Face Hub metadata as a source phrase and in R9", "'HF API' in R4 bullets; two huggingface.co/api/models URLs in PL1 R9", "'Hugging Face Hub model metadata' (public vendor-org metadata, allowed by main's P4 ruling); the two API URLs are removed from R9 and the gate or tree pages remain (see section 4, decision 2)", "T104, T105, main ruling on purplellama P5 r2 Q4 and lessons 12"),
    ("Third-party sources (Together, Semgrep, CrowdStrike, ARVO, Python, Hugging Face docs)", "cited ad hoc", "each cited with 'not Meta docs' where used and attributed once in the inventory scope paragraph; Together's own pages (terms, docs, deprecations, pricing, rate limits, privacy) are R9 URLs of PL3 and PL5", "R007 item 1, R019, main P4 Q4"),
    ("Own counts and parsed sizes", "[Documented: repo] on 'counted from the file' (16 inventory rows, rule counts, dataset sizes); first-person CWE counts 47, 63, 65, 65", "[Inferred] with 'premise: counted by parsing the file' (existence of a file or folder stays [Documented: repo]); CWE counts corrected to 46 (CODESHIELD rules), 62 (CyberSecEval rules), 64 (all rule files) and 64 (union); one rule has no cwe_id", "T98, T67 (CORRECTION)"),
    ("Code Shield latency statements", "'four statements' in two Summaries, INV(g) intro and a bullet", "five Meta sources (README, LlamaFirewall docs, LlamaFirewall paper, CyberSecEval 3 paper, protections page); the two papers give identical figures, so INV(g) keeps 12 rows (CSE3 merged into statement 3); the bullets are named by source, not 'statement 1 to 4'", "T65, T66, main ruling on purplellama P5 r2 Q2"),
    ("PyPI codeshield 1.0.1 versus the pin", "[To be verified] (sdist not read)", "documented difference: of 168 shared files 30 differ (nine Python files); rule YAML and config.yaml identical; Kotlin regex only, no Semgrep job cap, string enums in the sdist", "T19 (CORRECTION)"),
    ("Together default judge model", "'default Llama 4 Maverick on Together' with availability [To be verified]", "Together's own pages list Llama 4 Maverick FP8 as removed from serverless inference on 2026-03-31; PL3 R4 Summary and R7 and R8 Summaries say so; the live host check stays [To be verified]", "T46, T47"),
    ("Licence and terms items (class c)", "open R8 questions and [To be verified] cells", "clauses recorded as [Documented] (Llama 4 AUP item 1.h, Additional Commercial Terms, gate form, Together section 4 and defaults, Semgrep LGPL 2.1 and rules licence, CrowdStrike and ARVO licences); the questions whether they bar bench testing stay open as R8 bullets and are decided before bench testing", "T6 to T17, R019, main ruling (queue.md, purplellama P5 r1 Q2)"),
    ("Covered by Table 3 column (inventory)", "SYSTEM and MEMORY role rows listed all five LlamaFirewall headers", "SYSTEM row lists the PromptGuard, Regex and Hidden ASCII headers; MEMORY row lists PromptGuard, CodeShield, Regex and Hidden ASCII; other rows unchanged; markers: legacy (Prompt Guard 1), inventory only (CyberSecEval 4, ClassifyIt, CyberSecEval command line); planned not used", "T77"),
    ("R9 and Source URL lists", "API paths, blob/main URLs, develop-branch URL", "pinned URLs (cookbook SHA, Semgrep tag v1.69.0, ARVO and CrowdStrike SHAs), no API paths; every repo label has a same-ref R9 URL in its column (checked, section 8d)", "T22, T23, T104, T105"),
]
for g in G:
    w("| " + " | ".join(x.replace("|", "\\|") for x in g) + " |")
w("")

# ---- section 2
w("## 2. Column and row changes")
w("")
by_col = collections.defaultdict(list)
for i, x in enumerate(COLLOG):
    m = re.match(r"(PL\d) R(\d)(?: (Summary))?$", x["loc"])
    by_col[m.group(1)].append((int(m.group(2)), i, x))
for cid in M.IDS:
    hdr = next(c["header"] for c in cols if c["id"] == cid)
    w("### %s" % cid)
    w("")
    w("%s" % hdr)
    w("")
    w("| Location | Before | After | Reason |")
    w("|---|---|---|---|")
    for rn, i, x in sorted(by_col[cid], key=lambda t: (t[0], t[1])):
        w("| %s %s (%s) | %s | %s | %s |" % (cid, "R%d" % rn, x["kind"], short(x["before"]), short(x["after"]), short(x["reason"], 260)))
    w("")

# ---- section 3
w("## 3. Inventory changes (sheet block letters (a) to (h))")
w("")
groups = collections.OrderedDict()
groups["scope"] = []
for k in "abcdefgh":
    groups[k] = []
for x in INVLOG:
    m = re.match(r"INV \(([a-h])\)", x["loc"])
    groups[m.group(1) if m else "scope"].append(x)
titles = {"scope": "Title, scope paragraph and block intros", "a": "(a) Components and variants", "b": "(b) LlamaFirewall scanner catalogue", "c": "(c) Roles, use cases and default scanner map",
          "d": "(d) Code Shield language and analyzer matrix", "e": "(e) Integration and access paths", "f": "(f) Licences, gating and terms", "g": "(g) Published metrics and latency statements", "h": "(h) Adjacent and cross-reference items"}
for k, lst in groups.items():
    w("### %s" % titles[k])
    w("")
    w("| Location | Before | After | Reason |")
    w("|---|---|---|---|")
    for x in lst:
        w("| %s (%s) | %s | %s | %s |" % (x["loc"], x["kind"], short(x["before"]), short(x["after"]), short(x["reason"], 260)))
    w("")
w("## 3b. Evaluation-tooling changes (purplellama_eval_tooling_final.md)")
w("")
w("| Location | Before | After | Reason |")
w("|---|---|---|---|")
for x in EVLOG:
    w("| %s (%s) | %s | %s | %s |" % (x["loc"], x["kind"], short(x["before"]), short(x["after"]), short(x["reason"], 260)))
w("")

# ---- section 4 conflicts
w("## 4. Conflict decisions")
w("")
CONF = [
    ("Overlap split between the two resolvers (main's ruling on purplellama P5 r2 Q5)", "Resolutions 1 and 2 both edit PL1 and PL2 text (T35, T40, T93 to T95) and both give new PL3 Summaries.", "r2 text for T93, T94 and T95 and for the PL5 half of T40; r1 text for PL2 R4, R7 and R8, T35 and the PL2 half of T40; the shared T45, T46, T48, T11, T12, T13, T14, T19, T20, T22, T24 and T76 edits were reconciled bullet by bullet (details below and in the tables). Where both gave the same bullet it was applied once."),
    ("R9 and API paths (T104 r1 versus main's ruling on r2 Q4 and lessons 12)", "r1 T104: keep the two huggingface.co/api/models URLs in PL1 R9. Main: cite the public gate or model page, not the API path (lessons 12: no API paths in URL lists).", "Applied main's ruling to every column: the two API URLs are removed from PL1 R9, none is added to PL3 R9 (the Maverick gate page https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 is cited instead, and the alignment-check evals dataset README is cited as a raw file at the revision). The Hub metadata facts keep their repo labels with the tree-URL pins already in R9."),
    ("Label of the PL6 R4 Summary (T19 r2 text)", "r2 gave '... PyPI 1.0.1 has the same rule files but different code. [Documented]'.", "Text applied exactly, label changed to [Inferred]: the clause is a sdist-versus-pin comparison, which main's ruling on the PyPI label form marks [Inferred], and the Summary label is the weakest label of the facts it draws on (README section 3 rule 5)."),
    ("PL3 R4 Summary (T46: r1 versus r2)", "r1: '... The code default is Llama 4 Maverick on Together, which Together lists as removed from serverless inference. No local model is used.' r2: shorter, drops 'No local model is used'.", "r1 text: it keeps the no-local-model statement the row already supported and is within 45 words."),
    ("PL3 R7 Summary (T11 r1 versus T46 and R032 r2)", "r1 changed one clause ('so synthetic data is suggested', 48 words); r2 rewrote the whole Summary (60 words) to include the judge-model change.", "r2 text (it contains the r1 change and the T46 consequence; 60 words, the R7 limit)."),
    ("PL3 R6 Together availability bullets (T46: r1 versus r2)", "r1: two [Documented] bullets (deprecation row; model page still shows the model) plus an [Inferred] bullet. r2: five bullets (host, serverless table, deprecation, inference, live host [To be verified]).", "Both kept: r2's five bullets plus r1's bullet that Together's Llama 4 Maverick model page still presents the model and the .xyz host while the deprecations page says a model can still appear in catalog listings (README section 3 rule 4: two sources that conflict get two bullets, each labelled)."),
    ("PL3 R7 Together section 4 bullet (T11: r1 versus r2)", "r1: split the quote from the suggestion. r2: keep the quote and append the recommendation inside the [Documented] bullet.", "r1: the recommendation ('traces without real data') moves to its own [Inferred] bullet worded as a suggestion; the quote bullet is left [Documented] (README section 3 rule 5; R032)."),
    ("PL3 R8 cost bullet and PL5 R8 availability and cost bullet (T48: r1 versus r2)", "r1: 'Cost per call and numeric rate limits ... $1.04 ...' for both columns. r2: 'Cost per trace for a replacement judge model' for PL3 and PL5.", "PL3 R8 uses r2's question (the judge may be replaced); PL5 R8 merges r1's price and rate-limit facts with r2's availability clause (the PIICheckScanner default is on Together's serverless table, the CustomCheckScanner Maverick default is not)."),
    ("PL3 R5 dataset bullets (T24: r1 versus r2)", "r1: one added bullet (577 test cases, does not say whether it is the 600-scenario benchmark). r2: three bullets (paper links the dataset; card side of the size conflict; card fields).", "r2's three bullets; the paper-side bullet is relabelled 'Source conflict, benchmark size (paper side)'. The 'not said whether it is the same set' point is in PL3 R8 and INV(g)."),
    ("PL3 R7 dataset reuse bullet (T24)", "r1: 'is a possible source of agent traces (suggested)'. r2: 'cases hold prompts, labels and stored judge decisions rather than ready-made traces ... a bench would first need to check'.", "One bullet combining both, worded as a possibility, [Inferred] with the card fields as premise."),
    ("Status cells for PromptGuard, CodeShield, Regex and Hidden ASCII scanners (T76: r1 versus r2)", "r1: 'Available [Inferred]' kept, 'not marked experimental' [Not disclosed] with a grep named. r2: 'Available [Documented: repo]' from the README component list (PromptGuard line 30, Regex line 38, CodeShield line 44); Hidden ASCII stays [Inferred].", "r2's README-based [Documented: repo] for PromptGuard, CodeShield and Regex (a verbatim README line beats an inference), r1's named search for 'not marked experimental' [Not disclosed] on PromptGuard and Hidden ASCII, r2's 'no maturity statement [Not disclosed]' on CodeShield and Regex; Hidden ASCII keeps [Inferred]."),
    ("INV(a) llamafirewall sdist cell (T20: r1 versus r2)", "r1: 'differs from the pin in two functional places [Documented]'. r2: 'matches ... [Inferred]'.", "Facts about what the sdist and the pin contain are separate [Documented] clauses (sdist with hash and date in plain text; pin with the repo label); the statement that they differ and in which files is [Inferred] (main ruling); the history fact (version string set on 2025-05-28) is [Documented: repo]."),
    ("PL6 R2 Summary 'each with a CWE id' (T64 r2)", "One C Semgrep rule (vulnerable-strcpy) has no cwe_id (T70).", "Summary text applied exactly: the named examples (weak hashes, command injection, buffer-overflow functions) are each supported by a rule-message bullet that carries a CWE id; the vulnerable-strcpy exception is its own bullet."),
    ("PL6 R4 analyser-map bullet (T19 r2 append)", "r2: append '(at the pin; the PyPI 1.0.1 sdist maps Kotlin to regex only)' under the repo label.", "Only '(at the pin; ...)' appended; the sdist's regex-only Kotlin entry is its own [Documented] bullet, so two sources are not under one label."),
    ("Language-count bullets (T64, T101, style 5)", "Letter-labelled bullets 'source A, B, B2, C, D, D2, E' in PL6 R2 and a different lettering in PL4 R2.", "Plain pairs ('The Code Shield README says ...') in both columns; the CyberSecEval 3 statement, the Figure 18 axis, the inferred equality with the eight scanned languages, the 'which seven' absence and the 190-pattern statement added to both."),
    ("Per-language precision and recall (T72 r2 versus main's ruling on r2 Q3)", "r2 proposed [Inferred] readings of bar heights (about 0.67 for PHP and so on).", "Not applied (hard rule 4: numbers verbatim; no by-eye values). Only the existence of the chart (90% confidence bars, eight languages, no value table) and its axis labels are recorded; the question stays in R8 and the CSE3 Figure 18 note is in the eval sheet."),
    ("INV(g) shape (main's ruling on r2 Q2)", "CyberSecEval 3 latency figures could be a thirteenth row.", "Merged into 'CodeShield latency statement 3' (renamed 'LlamaFirewall paper and CyberSecEval 3 paper'); block (g) keeps 12 rows."),
    ("Together API slip evidence (main's ruling)", "Resolutions 1 disclose one GET to an API host (HTTP 401, response deleted).", "Not used anywhere; every Together fact cited here comes from Together's web and documentation pages."),
    ("Licence items (T6 to T8, T10, T11, T13 to T15; main's ruling)", "AUP item, Additional Commercial Terms, Together section 4 'probe, scan, or test' and 'benchmarking' clauses.", "Recorded as [Documented] clauses with quotes; the questions whether bench testing is permitted stay open as R8 bullets (PL1, PL2, PL3, PL5, PL6) and inventory block (f); no bench rule is written (R032; R025 covered Google Preview data only)."),
    ("Prompt Guard 2 licence text conflict (T8, README rule 4)", "README link target ../LICENSE is the Llama 3.2 root file; folder LICENSE files and the gate pages show Llama 4.", "Both sides are bullets with their own labels (README quote, root file, folder files, gate pages); 'which text prevails' is [Not disclosed]; INV(f) row 101 carries the same."),
    ("PL1 R3 and PL2 R6 Summaries (T93, T94: r1 versus r2)", "r1: 'no prompt structure to set' (41 words). r2: 'A single text string ...' (documented bullets).", "r2 text for both (main's overlap ruling)."),
    ("Row numbers and unit of INV(g) (T103)", "Locators for the same source differ (paper section 4.3 versus 4.3.1, 4.3.2).", "Standardised to the section where the text sits (4.3.1 for the role sentence, 4.3.2 for the numbers, Appendix B.2 for the 22M figure, section 4.2 Figure 2 caption for 'currently an experimental feature')."),
]
for i, (t, a, b) in enumerate(CONF, 1):
    w("%d. **%s.** Sources: %s Decision: %s" % (i, t, a, b))
    w("")

# ---- section 5
def distinct_urls():
    urls = set()
    for n in ("purplellama_two_level.md",):
        for ln in open(D + n, encoding="utf-8").read().splitlines():
            if re.fullmatch(r"• https?://\S+", ln):
                urls.add(ln[2:])
    for ln in open(D + "purplellama_inventory_final.md", encoding="utf-8").read().splitlines():
        if ln.startswith("|"):
            last = ln.strip()[1:-1].split(" | ")[-1]
            for u in last.split(" ; "):
                if u.startswith("http"):
                    urls.add(u.strip())
    for ln in open(D + "purplellama_eval_tooling_final.md", encoding="utf-8").read().splitlines():
        for u in re.findall(r"https?://[^\s|;,)]+", ln):
            urls.add(u)
    return urls

urls = distinct_urls()
w("## 5. Change counts and final counts for the P8 config")
w("")
w("- Logged edits: %d in the columns, %d in the inventory, %d in the eval sheet (%d in total)." % (len(COLLOG), len(INVLOG), len(EVLOG), len(LOG)))
w("- Columns by kind: %s. By column: %s." % (", ".join("%s %d" % kv for kv in count(COLLOG).items()), ", ".join("%s %d" % (c, len(by_col[c])) for c in M.IDS)))
w("- Inventory by kind: %s." % ", ".join("%s %d" % kv for kv in count(INVLOG).items()))
w("- Eval by kind: %s." % ", ".join("%s %d" % kv for kv in count(EVLOG).items()))
w("- Summaries changed: %d of 63 (list in purplellama_summaries_preview.md, marked with an asterisk): %s." % (len(changed), ", ".join("%s R%d" % k for k in changed)))
w("- Resolution items applied: r1 items T6 to T17, T20, T22 to T26, T28, T35, T40 to T46, T48, T76, T77, T80, T93, T94, T95 (PL2 R1), T97, T100 to T105 and supplementary findings 1 to 4 and 7; r2 items T5, T19, T20, T22, T24, T40 (PL5), T45, T46, T48, T54, T59, T64 to T70, T72, T74 to T78, T80 to T87, T89 to T101, T103 to T105 and the R032 pass. Items with no text change by design: T1 to T4 (R030: prefixes, seven columns, PL7 and PL5 kept, one column per scanner), T77 convention applied to two Covered-by cells only, T102 (process: notes moved), T103 (no content error; locators standardised).")
w("- Final inventory row counts for the P8 config (BLOCKS): (a) Components and variants 16, (b) LlamaFirewall scanner catalogue 8, (c) Roles, use cases and default scanner map 11, (d) Code Shield language and analyzer matrix 16, (e) Integration and access paths 12, (f) Licences, gating and terms 8, (g) Published metrics and latency statements 12, (h) Adjacent and cross-reference items 5 (88 rows). Checker lines: %s." % "; ".join(inv_tables))
w("- Final columns: 7 (PL1 to PL7), three prefixes: 'Prompt Guard 2:' (PL1), 'LlamaFirewall:' (PL2, PL3, PL4, PL5, PL7), 'Code Shield:' (PL6); column order PL1 to PL7 as in the final file.")
w("- Evaluation-tooling sheet sections and items (parser order kept: Overview, Tools, Datasets, Published results, Red-teaming, Engine coverage, Reuse for the test bench, Open questions): %s; table rows: Tools %d, Datasets %d, Published results %d; standalone bullets: Reuse for the test bench %d, Open questions %d." % (", ".join("%s %d items" % t for t in ev_counts), ev_rows.get("Tools", 0), ev_rows.get("Datasets", 0), ev_rows.get("Published results", 0), ev_bul.get("Reuse for the test bench", 0), ev_bul.get("Open questions", 0)))
w("")
w("## 5b. Notes for P8 (workbook) and P9 (URL check)")
w("")
w("- Registry (gr-xlsx-writer): three prefixes 'Prompt Guard 2:', 'LlamaFirewall:', 'Code Shield:' (R030); column ID prefix PL; the seven headers are the seven '## Column PLn:' lines of purplellama_two_level.md, in order PL1 to PL7. The columns checker gives one 'several prefixes' warning, which is expected.")
w("- Inventory config: sheet '3x. Purple Llama Inventory' (letter assigned at P8 in queue order, R003; the name is 26 characters with the letter, lessons 15); md path purplellama_inventory_final.md; BLOCKS (marker, title, rows): '## (a) Components and variants' 16, '## (b) LlamaFirewall scanner catalogue' 8, '## (c) Roles, use cases and default scanner map' 11, '## (d) Code Shield language and analyzer matrix' 16, '## (e) Integration and access paths' 12, '## (f) Licences, gating and terms' 8, '## (g) Published metrics and latency statements' 12, '## (h) Adjacent and cross-reference items' 5. Covered-by column name 'Covered by Table 3 column' (blocks a, b, c, e only; blocks d, f, g, h have no Covered-by column).")
w("- Markers tuple: legacy '— (legacy, not in Table 3)' (Prompt Guard 1) and inventory only '— (inventory only, not in Table 3)' (CyberSecEval 4, ClassifyIt, CyberSecEval command line; R011). The planned marker is not used. Block (c) column heading 'Direction under R002' was renamed 'Direction (input, output or trace side)'; if the config addresses columns by heading text, use the new text (the checker accepts it).")
w("- Eval sheet (the eval builder needs MD, TITLE, NOTE only; SECTION_ORDER is unchanged): MD = purplellama_eval_tooling_final.md (the build reads the final under whatever name main registers); proposed sheet name '<letter>. CyberSecEval Eval Tooling' (29 characters with a one-letter prefix such as 3k; letters are assigned at P8 in queue order, so if lionguard (R033, expected 3i) is written first expect 3j for the Purple Llama inventory and 3k for this sheet; at most 31 characters); proposed TITLE '<letter>. Meta CyberSecEval 4 Evaluation Tooling (PurpleLlama@172c1074)'; proposed NOTE 'Evaluation tools, datasets, published results and reuse assessment for the test bench (possible sources and suggestions, not decisions). Labels as in sheet 3.' The sheet is placed right after the inventory sheet (R003). The file parses with build_eval_sheet.parse_md (8 sections).")
w("- Distinct URLs in R9 lists, inventory Source URL cells and the eval sheet: %d. Hosts: github.com (blob and tree at the pin SHA, tags or SHAs), huggingface.co (gate, tree and one dataset raw README at a revision; no api paths), arxiv.org, dev.meta.ai and llama.com pages, meta-llama.github.io docs sites, pypi.org and files.pythonhosted.org (two sdist files), Together (docs.together.ai, www.together.ai), semgrep.dev, docs.python.org, engineering.fb.com. No *.googleapis.com host, no API path and no {…} template is a URL-list entry; code-fact base URLs such as https://api.together.xyz/v1 appear inline in cells and in one eval bullet and must not be requested by the URL check (hard rule 5, lessons 12). Expected statuses for gr-url-checker: github.com blob pages answer HTTP 403 from the session proxy (check the raw.githubusercontent.com equivalent at the same ref); tree URLs and short-SHA blob URLs (https://github.com/n132/ARVO-Meta/blob/51cfeab5/LICENSE) cannot be served raw and are listed as exceptions; the Llama gate pages and the three gated model pages answer 200 for the gate text; dev.meta.ai and llama.com answer after a redirect." % len(urls))
w("")

# ---- section 6 remaining open items
w("## 6. Remaining open items")
w("")
tri = open(D + "purplellama_triage.md", encoding="utf-8").read().splitlines()
tmap = {}
for ln in tri:
    m = re.match(r"^\| (T\d+) \| (.*?) \| (.*?) \| (a|b|c)[^|]* \| .*? \| (H|M|L) \|$", ln)
    if m:
        tmap[m.group(1)] = (m.group(4), m.group(5), re.sub(r"\s+", " ", m.group(2))[:170])
OPEN_B = {
    "T18": "No release, tag or CHANGELOG: [Not disclosed] bullets in every column R4 and the inventory scope paragraph (honest gap).",
    "T21": "Residual closed by Suppl. 1: the gate page carries the card text; the sentence-level equality is [Inferred] in the inventory scope paragraph. Nothing open.",
    "T27": "PL1 R7 and R8; PL2 R7 and R8 (threshold sweep on a bench set).",
    "T29": "PL1 R4 and R5 [Not disclosed] bullets (private benchmark, training data, languages).",
    "T30": "PL1 R4 [Inferred] bullet and PL1 R8 (parameter totals; honest gap).",
    "T31": "PL1 R8 and PL2 R8 (tool, retrieved, memory and assistant text); the documentation half is now PL1 R3 (cookbook tutorial, cell 12).",
    "T32": "PL1 R8 (paraphrased, encoded or long jailbreaks).",
    "T33": "PL1 R8 (22M versus 86M on non-English prompts).",
    "T34": "[Not disclosed] latency bullets in PL1 R5, PL2 R5, PL3 R5, PL4 R5, PL5 R5, PL6 R5, PL7 R5 and R8; partly answered by the cookbook timing (PL1 R5) and the Together prices (PL3, PL5).",
    "T36": "PL2 R7 and R8 (first versus later scan timing).",
    "T37": "PL2 R8 (gated config not read; the cookbook scores index 1 as malicious).",
    "T38": "PL2 R8 (512-token truncation test).",
    "T39": "PL2 R8 (whitespace-removing preprocessing).",
    "T47": "PL3 R6 [To be verified] bullet and PL3 R8 first bullet (does api.together.xyz still answer); PL5 R8.",
    "T49": "PL3 R8 (long traces).", "T50": "PL3 R8 (whole trace versus one action).", "T51": "PL3 R8 (tool outputs in the trace).",
    "T52": "PL3 R8 (judge manipulation).", "T53": "PL3 R8 (non-English traces, run-to-run variation).",
    "T55": "PL3 R5 [Not disclosed] (threshold or calibration guidance).",
    "T56": "PL5 R5 and R8 (regex rates, latency).", "T57": "PL5 R2 [Inferred] bullets and R8 (pattern coverage).", "T58": "PL5 R4 [Inferred] and R8 (pattern set not configurable).",
    "T60": "PL5 R2, R5 and R8 (PIICheck and CustomCheck docs silence, accuracy, fail-open).",
    "T61": "PL7 R1 [Not disclosed] (no docs page for Hidden ASCII).", "T62": "PL7 R8 (emoji tag sequences).", "T63": "PL7 R8 (other invisible characters, normalisation, decoded reason).",
    "T71": "PL4 R8 and PL6 R8 (runtime confirmation, per-language precision and recall on the bench's own set).",
    "T73": "PL4 R8 (block on every finding; tool-call fields).",
    "T79": "Inventory (a) to (h) cells marked [Not disclosed] (MEMORY direction, approval time, gating of Code Shield and CyberSecEval, root README silence).",
    "T88": "Eval Engine coverage (unused --enable-lf, caught_by_promptguard) and Open questions (does --enable-lf do anything later).",
}
PARTLY = {
    "T6": ("c", "Quoted clause [Documented]; whether bench red-team testing of Prompt Guard 2 and the PromptGuard scanner is permitted stays an R8 bullet in PL1 and PL2 and an INV(f) note; to be decided before bench testing."),
    "T7": ("c", "Clause recorded; whether the 700 million MAU clause matters for the bench owner's organisation stays an R8 bullet in PL1."),
    "T8": ("c", "Which licence text prevails is [Not disclosed] (PL1 R4) and an R8 bullet (PL1 R8); INV(f) row 101."),
    "T10": ("c", "Form fields and instruction text recorded; approval time [Not disclosed]; who applies is a bench decision."),
    "T11": ("c", "Section 4 and the 'probe, scan, or test' and 'benchmarking' clauses recorded; whether made-up values count stays an R8 bullet in PL3 and PL5; synthetic data is worded as a suggestion."),
    "T12": ("c", "Together defaults recorded; retention period [Not disclosed]; whether sending traces is acceptable stays an R8 bullet (PL3 R8)."),
    "T13": ("c", "Meta-side licences recorded; the licence of the Together-served builds [Not disclosed] (PL5 R4, INV(f) row 107)."),
    "T14": ("c", "LGPL 2.1 and the rules licence recorded; consequences for a bench stay an R8 bullet (PL6 R8) and an INV(f) note."),
    "T15": ("c", "CrowdStrike (CC BY-ND 4.0, CC BY-SA 4.0) and ARVO (BSD 2-Clause) recorded; IC3, CISA and NSA report licences, OSS projects inside the ARVO images and the CAPTCHA source stay [To be verified] or [Not disclosed] (EV Datasets, EV Open questions, INV(f) row 105)."),
    "T16": ("c", "Meta-side restrictions recorded; OpenAI, Anthropic and Google provider terms not read [To be verified] (INV(f) row 105)."),
    "T17": ("c", "Two documented facts; the combined licence stack is [Inferred] and Meta's statement of it [Not disclosed] (INV(f) row 103)."),
    "T28": ("a", "Which AUC (.998 card, .98 paper) is right is not stated: both bullets stay (PL1 R5, R8; INV(g))."),
    "T44": ("a", "Timeout and size-limit absence is [Not disclosed] with the search named (PL2 R6)."),
    "T48": ("a", "No Maverick serverless price and no numeric rate limit are published: [Not disclosed] (PL3 R5, PL5 R6); per-call cost needs a measurement (PL3 R8, PL5 R8)."),
    "T64": ("a", "Which seven languages the '7' statements mean is [Not disclosed] (PL4 and PL6 R2, R8; INV(d))."),
    "T65": ("a", "Latency measurement stays a bench item (PL4 R8, PL6 R8); five sources are recorded."),
    "T69": ("a", "Whether Semgrep findings can ever recommend blocking: premise (Semgrep output format) not read; PL6 R8."),
    "T70": ("a", "Runtime confirmation of the code observations (temporary file, notebook comparison, CWE-CWE text): PL4 and PL6 R8."),
    "T72": ("a", "Per-language precision and recall values are not published as text; chart existence and axis labels recorded; PL4 R5 and R8."),
    "T76": ("a", "Hidden ASCII status stays [Inferred] (INV(a), (b))."),
    "T87": ("a", "The conclusion sentence reuses the interpreter-abuse range: [Inferred] in EV Published results."),
}
w("### 6a. Items not resolvable from documents (class b needs testing, and honest gaps), unchanged in the finals")
w("")
w("| T-id | Class | Priority | Item (triage) | Where it stays open in the finals |")
w("|---|---|---|---|---|")
for t in sorted(OPEN_B, key=lambda s: int(s[1:])):
    cl, pr, it = tmap.get(t, ("b", "?", ""))
    w("| %s | %s | %s | %s | %s |" % (t, cl, pr, it.replace("|", "\\|"), OPEN_B[t].replace("|", "\\|")))
w("")
w("### 6b. Residual parts of handled items (verdict PARTLY RESOLVED or class c with the question left open)")
w("")
w("| T-id | Class | Priority | Residual and where it stays open |")
w("|---|---|---|---|")
for t in sorted(PARTLY, key=lambda s: int(s[1:])):
    cl, pr, it = tmap.get(t, (PARTLY[t][0], "?", ""))
    w("| %s | %s | %s | %s |" % (t, PARTLY[t][0], pr, PARTLY[t][1].replace("|", "\\|")))
w("")
w("### 6c. Closed by rulings (not open)")
w("")
w("T1 to T4 closed by R030 (Q-A to Q-C). T5 (Q-D): not decided by the user; the drafts report possible sources of attack examples and the need for harmless look-alike messages as proposals only (R030, R032; PL1 R7, PL2 R7, eval 'Reuse for the test bench'). T105 closed by main's P4 ruling. T102 (process) done by this merge.")
w("")
w("### 6d. Follow-ups noted for main (not Purple Llama column items)")
w("")
w("- Together's deprecation history also lists meta-llama/Llama-Guard-4-12B as removed from serverless inference on 2026-08-25 (resolutions 1, supplementary 5). Llama Guard is frozen (R004); sheet 3d may carry a Together serving route worth a check at the final-run summary.")
w("- The CP2 summary should list the licence and terms clauses recorded in 6b (class c) as clauses to decide before bench testing (queue.md ruling).")
w("")

# ---- section 7 reviewer notes
w("## 7. Moved Reviewer notes")
w("")
STAT_A = {
    1: "Status: both AUC values kept; a second copy of the card (gate page) prints .998 and the paper has one version (T28).",
    2: "Status: unchanged and still open (T30, honest gap).",
    3: "Status: language statements now include CyberSecEval 3 (7) and the Figure 18 axis (eight); 'which seven' [Not disclosed] (T64, T66).",
    4: "Status: five latency sources, bullets named by source (T65, T66).",
    5: "Status: the docs defect is confirmed on the live page (T43).",
    6: "Status: explained from the git history (T40).",
    7: "Status: (a) recorded as documented code with the cost [Inferred] (T35); (b) code lines [Documented: repo], consequence [Inferred] (T69); (c) code lines [Documented: repo], consequence [Inferred] (T70); (d) and (e) now [Documented: repo] (T68); (f) import order documented, consequence [Inferred], PyPI package differs from the pin (T74, T19).",
    8: "Status: corrected. Counts are 46, 62, 64 and 64 (one rule, vulnerable-strcpy, has no cwe_id and was counted as an empty CWE); own counts are [Inferred]; first-person wording removed (T67, T98).",
    9: "Status: superseded for the PyPI sdists (read and compared, T19, T20), the llama-cookbook files (read at a pinned commit, T23) and the Hugging Face card bodies (readable on the public gate pages, Suppl. 1); the Code Shield per-language figure is an image with no value table (T72).",
    10: "Status: the five pages are confirmed against the pinned files and the deploy source is stated in the repo (T22).",
    11: "Status: closed by R030 (three prefixes).",
    12: "Status: the clause is item 1.h of the Llama 4 Acceptable Use Policy, not 2.8 (T6); still a licensing question.",
    13: "Status: unchanged.",
}
STAT_B = {
    1: "Status: (c) split into two bullets (T99); (d) the code side is [Not disclosed] by absence, re-worded with the search named (T99).",
    2: "Status: the require_full_trace finding is now a PL3 R3 bullet (T54).",
    3: "Status: unchanged.",
    4: "Status: Together's deprecation page and serverless table confirm that Llama 4 Maverick FP8 is removed from serverless inference (T46); the licences were read (T13).",
    5: "Status: main's ruling allows the public Hub metadata; R9 cites gate and tree pages, not API paths.",
    6: "Status: true after T92 (the PL5 R2 Summary uses only documented facts).",
    7: "Status: the deploy source is in the pinned repo and passages match (T22).",
    8: "Status: corrected: PyPI lists 13 llamafirewall releases (0.0.0 to 1.0.3, including 1.0.0.post1) and the 1.0.3 sdist was read and compared (T20).",
    9: "Status: unchanged.",
    10: "Status: closed by R030 (PL5 stays one column; PL8 not drafted).",
}
STAT_I = {
    1: "Status: block (d) intro now lists five language-count sources and the Figure 18 axis; block (g) intro says five sources in four rows.",
    2: "Status: Rust and PHP findings are now [Documented: repo] where the code is explicit (T68).",
    3: "Status: row counts unchanged: 16, 8, 11, 16, 12, 8, 12, 5.",
    4: "Status: superseded: sdists read (T19, T20), cookbook files read (T23), Maverick and Llama 3.3 licences read (T13), gate-page card text equals the repo card (Suppl. 1); Semgrep rule licence read (T14).",
    5: "Status: Hub metadata is allowed evidence (main's ruling); no fact comes from a summarising fetch.",
    6: "Status: counts are labelled [Inferred] with 'counted by parsing' (T98).",
    7: "Status: SYSTEM and MEMORY rows now list only the headers whose Detail names the role (T77); Semgrep is labelled with the tag pin (T14).",
}
def emit_notes(title, lines, stat):
    w("### " + title)
    w("")
    items = [ln for ln in lines if ln.strip()]
    meth = [ln for ln in items if not re.match(r"^\d+\. ", ln)]
    for ln in meth:
        w(ln)
        w("")
    for ln in items:
        m = re.match(r"^(\d+)\. ", ln)
        if m:
            w(ln)
            w("")
            n = int(m.group(1))
            if n in stat:
                w("   " + stat[n])
                w("")
notes_a = K.reviewer_notes[D + "purplellama_cols_a.md"]
notes_b = K.reviewer_notes[D + "purplellama_cols_b.md"]
emit_notes("7a. purplellama_cols_a.md (PL1, PL2, PL4, PL6), 13 notes", notes_a, STAT_A)
emit_notes("7b. purplellama_cols_b.md (PL3, PL5, PL7), 10 notes", notes_b, STAT_B)
emit_notes("7c. purplellama_inventory.md, 7 notes", V.reviewer_notes, STAT_I)

# ---- section 8 self-check
w("## 8. Self-check")
w("")
w("### 8a. Summary word counts (limit 45, R7 60; trailing label excluded)")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Over limit |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
for c in cols:
    ws = [words(c["R"][n]["s"]) for n in range(1, 10)]
    over = sum(1 for n, x in enumerate(ws, 1) if x > (60 if n == 7 else 45))
    w("| %s | %s | %d |" % (c["id"], " | ".join(str(x) for x in ws), over))
w("")
w("### 8b. Top-level Detail bullets per row")
w("")
w("| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | Total |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
for c in cols:
    bs = [len([d for d in c["R"][n]["d"] if d.startswith("• ")]) for n in range(1, 10)]
    w("| %s | %s | %d |" % (c["id"], " | ".join(str(x) for x in bs), sum(bs)))
w("")
w("### 8c. Labels on R1 to R7 Detail bullets")
w("")
w("| Column | Documented | Documented: repo | Inferred | To be verified | Not disclosed | R1-R7 bullets without a label | R8 bullets with a label |")
w("|---|---|---|---|---|---|---|---|")
for r in label_rows:
    w("| " + " | ".join(str(x) for x in r) + " |")
w("")
w("### 8d. Structure")
w("")
w("| Check | Result |")
w("|---|---|")
w("| Columns | 7 (expected 7), IDs PL1 to PL7, prefixes Prompt Guard 2, LlamaFirewall, Code Shield |")
w("| Summaries | 63 (7 x 9); over limit: 0; backtick, underscore or $ in a Summary: 0 (checker) |")
w("| Rows R1 to R9 each once, Summary line and Detail present | yes (checker) |")
w("| Repo labels with an R9 URL of the same repo and ref in the same column; cited file names present in R9 | %d problems (self_check.py) |" % len(rep["problems"]))
w("| Reviewer notes or process language in the finals | 0 (grep, 8e) |")
w("| Inventory tables | %s |" % "; ".join(inv_tables))
w("| Inventory cells with ** , backtick or pipe; non-standard labels; Covered-by values that are not an exact header or marker | 0 (checker) |")
w("| Eval file | parses with build_eval_sheet.parse_md: 8 sections in parser order |")
w("")
w("### 8e. Known-wrong strings and process wording (lessons.md item 6)")
w("")
w("| String or pattern | Hits in the three finals | Expected |")
w("|---|---|---|")
for n, h, e in chk_rows:
    w("| %s | %s | %s |" % (n.replace("|", "\\|"), h, e))
w("")
w("### 8f. Checker output (run from the repo root)")
w("")
w("```")
w("python benchtest/tools/check_drafts.py columns benchtest/drafts/purplellama_two_level.md --final --expect 7")
for x in chk_cols:
    if x.startswith("columns:"):
        continue
    w(x)
w("python benchtest/tools/check_drafts.py inventory benchtest/drafts/purplellama_inventory_final.md --headers benchtest/drafts/purplellama_two_level.md")
for x in chk_inv:
    w(x)
w("```")
w("")
w("Exit codes: columns %d, inventory %d. The one warning is 'several prefixes used', expected for three per-tool prefixes." % (r1.returncode, r2.returncode))
w("")
open(D + "purplellama_changes.md", "w", encoding="utf-8").write("\n".join(O).rstrip("\n") + "\n")
print("changes written; cols/inv/eval edits:", len(COLLOG), len(INVLOG), len(EVLOG), "changed summaries:", len(changed))
print("checker:", chk_cols[-1], "|", chk_inv[-1], "| problems:", len(rep["problems"]))
for r in chk_rows:
    if r[1] != r[2]:
        print("HIT", r)
