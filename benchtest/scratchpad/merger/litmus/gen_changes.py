import json, re, sys, subprocess, collections, os
sys.path.insert(0, "benchtest")
import build_eval_sheet as BES

D = "benchtest/drafts/"
log = json.load(open("benchtest/scratchpad/merger/litmus/log.json", encoding="utf-8"))
EV, INV, CONF = log["ev"], log["inv"], log["conf"]
evt = open(D + "litmus_eval_tooling_final.md", encoding="utf-8").read()
invt = open(D + "litmus_inventory_final.md", encoding="utf-8").read()
ev0 = open(D + "litmus_eval_tooling.md", encoding="utf-8").read().split("\n")
inv0 = open(D + "litmus_inventory.md", encoding="utf-8").read().split("\n")
res = open(D + "litmus_resolutions_1.md", encoding="utf-8").read().split("\n")
secs = BES.parse_md(D + "litmus_eval_tooling_final.md")

LAB = re.compile(r"\*\*\[(Documented(: [^\]]+)?|Inferred|To be verified|Not disclosed)\]\*\*")


def esc(s):
    return s.replace("|", "/").replace("\n", " ")


# ------------------------------------------------------------------ counting
def kinds(entries):
    c = collections.Counter(e["kind"] for e in entries)
    return ", ".join("%s %d" % (k, c[k]) for k in sorted(c))


def tids(entries):
    c = collections.Counter()
    for e in entries:
        for t in set(re.findall(r"\bT(\d+)\b", e["why"])):
            c[int(t)] += 1
    return c


# ------------------------------------------------------------------ section grouping for EV log
SECTION_KEYS = [
    ("Title", "Title and Version scope (unparsed lines)"), ("Version scope", "Title and Version scope (unparsed lines)"),
    ("Overview", "Overview"), ("Tools", "Tools"), ("Datasets", "Datasets"), ("Published results", "Published results"),
    ("Red-teaming", "Red-teaming"), ("Engine coverage", "Engine coverage"), ("Reuse", "Reuse for the test bench"),
    ("Open questions", "Open questions"), ("Reviewer notes", "Reviewer notes")]
ORDER = []
for _, n in SECTION_KEYS:
    if n not in ORDER:
        ORDER.append(n)


def section_of(loc):
    for k, n in SECTION_KEYS:
        if loc.startswith(k):
            return n
    raise SystemExit("no section for " + loc)


def table(entries, collapse_t43=False):
    out = ["| Location | Before (shortened) | After (shortened) | Reason |", "|---|---|---|---|"]
    i = 0
    n43 = [e for e in entries if e["why"].startswith("T43")]
    done43 = False
    for e in entries:
        if collapse_t43 and e["why"].startswith("T43"):
            if not done43:
                out.append("| Datasets rows EV:53-66 (14 test rows, Contents cell; %d edits) | [Security] / [Specialised Advice] / [Undesirable Content] / [Political Content] prefix | Category: Security. / Specialised Advice. / Undesirable Content. / Political Content. prefix | T43: look-alike bracket prefix replaced (kind hygiene) |" % len(n43))
                done43 = True
            continue
        out.append("| %s | %s | %s | %s (%s) |" % (esc(e["loc"]), esc(e["before"]), esc(e["after"]), esc(e["why"]), e["kind"]))
    return "\n".join(out)


# ------------------------------------------------------------------ checks run now
def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, shell=True, encoding="utf-8")
    return (p.stdout + p.stderr).strip()

chk_inv = run("python benchtest/tools/check_drafts.py inventory benchtest/drafts/litmus_inventory_final.md")
chk_inv_h = run("python benchtest/tools/check_drafts.py inventory benchtest/drafts/litmus_inventory_final.md")
parse8 = run("python -c \"import sys; sys.path.insert(0,'benchtest'); import build_eval_sheet as B; print(len(B.parse_md('benchtest/drafts/litmus_eval_tooling_final.md')))\"")

# ------------------------------------------------------------------ self-check numbers
summ = []
for s in secs:
    for it in s["items"]:
        if it[0] == "summary":
            body = LAB.sub("", it[1]).strip()
            summ.append((s["name"], len(body.replace("**", "").split()), len(it[1].replace("**", "").split()), it[1].count("**"),
                         bool(re.search(r"[`_$]", it[1])), body))
sec_counts = {}
for s in secs:
    det = sa = tb = rows = nolab = 0
    for it in s["items"]:
        if it[0] == "detail":
            for b in it[1]:
                if b.startswith("• "):
                    det += 1
                    nolab += 0 if LAB.search(b) else 1
        elif it[0] == "bullet":
            sa += 1
            nolab += 0 if LAB.search(it[1].split("\n")[0]) else 1
        elif it[0] == "table":
            tb += 1
            rows += len(it[2])
    sec_counts[s["name"]] = (det, sa, tb, rows, nolab)
oq = [it[1] for s in secs if s["name"] == "Open questions" for it in s["items"] if it[0] == "bullet"]
oq_labels = collections.Counter(LAB.search(b).group(1) for b in oq)
brackets = collections.Counter(re.findall(r"\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]", evt))
ibrackets = collections.Counter(re.findall(r"\[(Documented(?:: [^\]]+)?|Inferred|To be verified|Not disclosed)\]", invt))
badproc = {}
for name, t in (("EV", evt), ("INV", invt)):
    for pat in (r"R0\d\d", r"Reviewer notes", r"this draft", r"I checked", r"see above", r"\bT\d{1,2}\b", r"\(draft"):
        badproc[(name, pat)] = len(re.findall(pat, t))

# pinned refs check
pins = {"govtech-responsibleai/playbook@45908b48": "45908b48c0a8b6d3855a154c0e41a12958a99205",
        "dsaidgovsg/aiguardian-test-action@v0.0.1": "190600937062c100d0c10181e3edf71702230244",
        "aiverify-foundation/moonshot@0.4.11": "ab4dbbad9177ff8590838071de82079b6d47ad51",
        "aiverify-foundation/moonshot@0.5.0": "f1b816c0bdb26051bea8890d5ff73b460b3efe33",
        "aiverify-foundation/moonshot@0.7.6": "03e9344dc9fc949ae05b1f38580611fce36528ab",
        "aiverify-foundation/moonshot-data@0.7.6": "30fac12375476ac1eb9f47e5872ea5d379c1aa4c"}
pinrows = []
for k, sha in pins.items():
    lab = "[Documented: repo %s]" % k
    n = evt.count(lab) + invt.count(lab)
    url = ("/" + sha + "/") in evt or ("/" + sha + "/") in invt
    pinrows.append((k, n, sha[:8], "yes" if url else "NO"))

# inventory block row counts
blocks = []
cur = None
for line in invt.split("\n"):
    if line.startswith("## ("):
        cur = [line[3:], 0]; blocks.append(cur)
    elif cur and line.startswith("|") and not line.startswith("|---") and not re.match(r"\| (Path|Suite or identifier|Parameter) \|", line):
        cur[1] += 1
inv_rows = [(b[0], b[1]) for b in blocks]

# ------------------------------------------------------------------ resolver verdict table
verd = {}
for line in res:
    m = re.match(r"\| T(\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|", line)
    if m:
        verd[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip(), m.group(4).strip())
tc_ev, tc_inv = tids(EV), tids(INV)
NOTEXT = {
    1: "closed by R038 (CP1): small inventory sheet yes; Kaleidoscope one Tools row; no text change",
    2: "closed by R038 (CP1); no text change (the Kaleidoscope Source cell wording is T6)",
    11: "locators standardised (see T11 rows); the cited lines of PB litmus.md, kaleidoscope.md and sentinel.md needed no change; brief 432-440 and INV legend noted in section 7",
    16: "process note; moved to section 7 with the one-GET and User-Agent facts; nothing in the sheet text",
    19: "host playbooks.aip.gov.sg: no sheet text uses it; EV RN-8 and INV RN-5(vi) go to section 7; pin correction is A1",
    24: "stays open as drafted: [Not disclosed] bullet 'No version, release number or release notes' (Overview)",
    25: "stays open as drafted: Tools row 2 and the INV API row ([Not disclosed] and [To be verified] cells)",
    27: "stays open as drafted: INV block (c) carries both sides; EV Open question on the Action name and test_suites",
    29: "stays open as drafted: Open question on UI testing wording [To be verified]",
    33: "stays open as drafted (Engine Summary keeps 'no judge model'); repeated Tools cells merged by T61",
    34: "counts confirmed (2 suites, 6 and 14 tests, 4 categories, 8 Baseline+-only, 12 WOG categories); no change",
    36: "stays open as drafted: Datasets Size/Licence cells and the Open question on dataset sizes",
    37: "stays open as drafted: Open question on 'hundreds of curated prompts' versus num_of_prompts",
    38: "stays open as drafted: Published results rows and Open question on the pass or fail rule",
    45: "stays open as drafted: Published results rows 'No published scores' and 'Sample report'",
    47: "stays open as drafted: Red-teaming Summary unchanged (36 words) and the [Not disclosed] bullet",
    56: "stays open as drafted: Open question on retrieval, tool-call, multimodal and multi-turn tests",
    57: "no text change (EV Engine bullet and INV endpoint row already list both sides)",
}
tid_rows = []
for t in range(1, 64):
    v = verd.get(t, ("?", "?", "?"))
    ne, ni = tc_ev.get(t, 0), tc_inv.get(t, 0)
    note = ""
    if ne + ni == 0:
        note = NOTEXT.get(t, "no text change")
    tid_rows.append((t, v[0], ne, ni, note))

# ------------------------------------------------------------------ URL list for P9
urls = []
for p in ("litmus_eval_tooling_final.md", "litmus_inventory_final.md"):
    for u in re.findall(r"https?://[^\s;|)\]\"`,]+", open(D + p, encoding="utf-8").read()):
        u = u.rstrip(".,")
        if u not in urls:
            urls.append(u)
NOREQ = [u for u in urls if re.search(r"form\.gov\.sg|litmus\.(stg\.|dev\.)?aiguardian\.gov\.sg", u)]
EXPECT = [u for u in urls if re.search(r"aiguardian-litmus-test$|aiguardian\.gov\.sg/litmus$|Litmus-Onboarding-Guide$|one%20pager\.pdf", u)]

# ------------------------------------------------------------------ write
L = []
a = L.append
a("# Litmus merge: change log")
a("")
a("Inputs merged: litmus_eval_tooling.md (8 sections, 9 Reviewer notes), litmus_inventory.md (blocks 4/5/6, 6 Reviewer notes), litmus_triage.md (63 items, H 11), litmus_resolutions_1.md (63 items: 35 RESOLVED, 5 PARTLY RESOLVED, 2 CORRECTION, 21 STILL OPEN), litmus_brief.md, and the rulings R003, R007, R011, R015, R019, R020, R021, R032, R038 plus main's litmus rows in scratchpad/main/queue.md (P5 Q1 to Q5: Open-question bullets carry only [To be verified] or [Not disclosed]; staging pin with a production-versus-staging note; Overview Summary = the resolver's RECOMMENDED text; Engine Summary = the resolver's new text; Baseline subset of Baseline+ [Documented] in both files, id mapping [Inferred]).")
a("")
a("Outputs: litmus_eval_tooling_final.md (8 sections, parses with build_eval_sheet.parse_md), litmus_inventory_final.md (3 blocks, 15 rows), litmus_changes.md (this file), litmus_summaries_preview.md. Litmus has no Table 3 columns (R003), so there is no litmus_two_level.md and no columns check; the final text carries no column IDs. Merge method: every edit was applied by script to the draft lines named in the resolutions (line numbers as at 2026-10-10, EV = eval draft, INV = inventory draft), so each edit below is also the log entry. Bold markers are dropped from quoted text, long text is shortened, and pipes inside cells are shown as slashes. Reason codes: Tn = triage id (resolution in litmus_resolutions_1.md), A1 = the resolver's pin CORRECTION, 'main P5' = main's queue ruling, 'hygiene' = label or look-alike fix, 'style' = wording or process text.")
a("")
a("## 1. Global changes")
a("")
a("| Scope | Before | After | Reason |")
a("|---|---|---|---|")
G = [
    ("Reviewer notes sections", "EV 9 notes, INV 6 notes in the drafts", "removed from both finals; kept verbatim in section 7", "T62; README section 7 item 2"),
    ("Sheet set", "inventory option (a) (3 blocks) plus eval sheet, pending CP1", "unchanged: inventory blocks 4/5/6 (15 rows), eval sheet with 8 sections; no Table 3 columns; every Covered-by cell is the inventory-only marker", "T1, T2 (R038); R003; R011"),
    ("Overview Summary", "'Litmus is a hosted testing service for AI applications, not a guardrail ... before launch' (44 words excl. label)", "resolver's RECOMMENDED text with the eligibility and proof-of-concept qualifiers (44 words excl. label; fallback text not used)", "T20, T4, T21; main P5 ruling"),
    ("Engine coverage Summary", "44 words excl. label, 46 incl. (claims 'over HTTP' with no Detail bullet; 'no statement on guardrailed endpoints')", "resolver's new text, 43 words excl. label, 45 incl.; 'over HTTP' backed by a new Detail bullet; 'no support statement for guardrailed endpoints'", "T51, T50; lessons 18"),
    ("Playbook pin (EV Version scope, INV legend)", "'staging branch ... the deployed site is built from staging'", "same pin 45908b48 (staging) plus the production-versus-staging note: the README lists staging (built from staging) and production (built from main); pinned pages match staging; production carries the same statements except the refusal sentence in tools/litmus.md line 53", "A1 (CORRECTION); main P5 ruling; T40"),
    ("Open-question labels", "two Open questions under [Inferred] (EV:146, EV:147); two vendor-internal questions under [To be verified]", "every Open-question bullet carries [To be verified] or [Not disclosed] only (counts in section 8)", "main P5 ruling (README section 6); T14, T15, T39, T52, T53"),
    ("Short-name set", "two name sets: DOCS/PORTAL in EV, AIG/DEV in INV; legend only in unparsed lines", "one set DOCS, PORTAL, PB, ACT (MS in EV): legend also in the parsed Tools note (EV) and the block (a) intro (INV)", "T60"),
    ("Process wording in parsed text", "'(R002)', 'in this draft', '(R019)', '(R003)', '(a proposal, R032)', 'conflict C1 ... C20' (brief conflict ids)", "removed or reworded in plain words (24 distinct conflict-id phrasings, 28 occurrences); unparsed lines also lose R003, R011, R019 and 'R007 item 7'", "T59, T58; README section 4"),
    ("Line locators into pinned files", "'line 46', 'lines 31 to 45', 'lines 432 to 437', 'line 11'", "file@ref:line form; ACT lines 31-44 (headers 45); safety.mdx 429-440; benchmark_runner_dto.py@0.7.6:10", "T11"),
    ("Link-target facts", "'(link target read from the page)'", "method named: read from the page HTML with curl and the Python standard-library parser, 2026-10-10; not visited", "T9; R021"),
    ("Moonshot tags", "tags 0.4.0, 0.5.0, 0.7.6", "tags 0.4.11 (in force at the sample Action commit), 0.5.0, 0.7.6; Apache-2.0 licence bullet; moonshot-data name-resemblance bullet", "T12, T7, T53; R019"),
    ("Datasets Contents cells", "leading '[Security]' style brackets (look like labels)", "'Category: Security.' style prefix in all 14 test rows", "T43"),
]
for g in G:
    a("| %s | %s | %s | %s |" % g)
a("")
a("## 2. Eval sheet changes (litmus_eval_tooling_final.md)")
a("")
a("Entries are in document order. Several new bullets in one 'after' cell are joined by ' // '.")
a("")
for sname in ORDER:
    ents = [e for e in EV if section_of(e["loc"]) == sname]
    if not ents:
        continue
    a("### 2.%d %s (%d edits)" % (ORDER.index(sname) + 1, sname, len(ents)))
    a("")
    a(table(ents, collapse_t43=(sname == "Datasets")))
    a("")
a("### 2.%d Brief conflict ids removed from parsed text (%d patterns, %d occurrences)" % (len(ORDER) + 1, len(CONF), sum(c[2] for c in CONF)))
a("")
a("| Before | After | Occurrences | Reason |")
a("|---|---|---|---|")
for old, new, c in CONF:
    a("| %s | %s | %d | style: C1 to C21 are brief and triage ids that mean nothing on the sheet (T59) |" % (esc(old), esc(new), c))
a("")
a("## 3. Inventory changes (litmus_inventory_final.md)")
a("")
a("Blocks unchanged in count: (a) Access paths 4, (b) Test suites 5, (c) Integration parameters 6 (15 rows). Short-name renames (AIG to DOCS, DEV to PORTAL) are logged per line.")
a("")
a(table(INV))
a("")
a("## 4. Conflict decisions")
a("")
CD = [
    ("Overview Summary: recommended text versus fallback (T20, T4, T21)", "The resolver gave a recommended text with the eligibility and proof-of-concept qualifiers (44 words) and a fallback without them (39 words). Decision: the recommended text, per main P5 ruling. Every clause is backed by a Detail bullet: 'scores responses' (bullets 'Litmus tests a system' and 'How a run works'), 'web app or CI/CD' (new bullet quoting playbook line 25), 'available to public sector teams' (the TechPass and availability bullet), 'May 2025 portal page labels it proof of concept' (status source one). Label [Documented] (every clause rests on a quote)."),
    ("Playbook pin: staging versus production (A1, T40, T63)", "Sources: the pinned file at staging 45908b48 and the production site (Last updated on Jul 29, 2026). Decision: keep the staging pin (R007 item 7 precedent); state both deployments in EV Version scope and the INV legend; the one sentence that differs (tools/litmus.md line 53) is written as two bullets or statements, each labelled (staging [Documented: repo ...@45908b48], production [Documented]) in Published results row 3. Main decides separately whether the Sentinel 3e note needs the same wording (queue: final-summary follow-up)."),
    ("Open-question labels (resolver note versus main's earlier 'no labels')", "Resolver proposed [To be verified] or [Not disclosed] on every Open question and flagged the question; README section 6 and the NeMo and CyberSecEval finals use these labels. Decision: labels kept, per main P5 ruling; no [Inferred] or [Documented] remains in Open questions."),
    ("Baseline subset of Baseline+ and the id mapping (T35)", "EV Used-by column said [Documented], INV said [Inferred]. Decision: [Documented] in both (membership in each table is read directly), per main P5 ruling; the mapping 'aiguardian-baseline-tests selects the 6-test Baseline Tests suite' stays [Inferred] with its premise in both files."),
    ("Eligibility label mismatch (T4, C15)", "INV Needs cell said [Documented: repo ...] 'a public sector team'; EV Open question said no rule is stated. Decision: INV says the playbook states availability for public sector teams, not as a requirement, and that an explicit rule for others is [Not disclosed]; EV Open question restated to match."),
    ("Terms-of-Use clause bullet (T3, T22)", "The resolver's terms bullet mixed a quoted clause with an absence under [Not disclosed] and allowed a split. Decision: two bullets, the quoted clause [Documented] and the absence [Not disclosed] (one label per fact, README section 3 rule 5)."),
    ("Moonshot tag bullets (T12)", "Draft cited 0.4.0, 0.5.0 and 0.7.6; the resolver replaced them by 0.4.11, 0.5.0 and 0.7.6. Decision: applied; the DTO file is byte-identical at 0.4.0, 0.4.11 and 0.5.0 so no fact is lost. The T61 suggestion to merge EV:105 (sample Action) with the 0.4.11 bullet was not applied: the two bullets carry different repo labels."),
    ("T61 consolidation (advisory)", "T61 proposed about 14 Engine bullets, about 15 Open questions, and 'Not disclosed (see Engine coverage)' in repeated Tools cells. Applied: the repeated Judge and Engine cells now read '[Not disclosed] (see Engine coverage)' with one note under the table (the bracket label is kept so each cell fact still ends with a label); EV:145 and EV:146 dropped, EV:147 one question, EV:130 and EV:131 relabelled. Not applied: bullet merges, because each remaining bullet carries a different label or source and the resolver's own text for T7, T9, T12, T49, T50 and T53 adds bullets. Final counts: Engine coverage 26 bullets, Open questions 18, Overview 34, Red-teaming 8, Reuse 10."),
    ("EV:109 premise wording", "'the matches in the three bullets above' stopped being true once the T7 licence bullet was inserted between the Moonshot tag bullets and the possible-link bullet (T12 said it stays correct). Decision: reworded to 'the sample Action bullet and the Moonshot tag bullets above'."),
    ("Edits beyond the resolver's list (consistency, each logged)", "EV:39 link-target method (T9 triage location); EV:77 Conditions cell 'Illustrative code' to 'Code example' (T28 wording); EV:114 locator form (T11); INV:13 Status checked list and Host cell home-page login link, plus the home-page URL in the Source cell (T21, T9, T54); INV:28 'the repository was not researched here' aligned with the EV Source cell (T6); EV Tools Judge and Engine cells in rows 2 to 5 (T61). Each follows a resolver finding for the same fact in the other file."),
    ("Sentinel wiki path dropped (T14)", "The draft listed https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Getting-Started (HTTP 403) as a third Litmus address. Decision: dropped from the Litmus sheets; it is not a Litmus page and the real Sentinel page (HTTP 200) is already in the Overview bullet 'Litmus and Sentinel share one interest form'."),
]
for i, (t, body) in enumerate(CD, 1):
    a("%d. **%s.** %s" % (i, t, body))
a("")

a("## 5. Change counts and P8 config notes")
a("")
cev = collections.Counter(e["kind"] for e in EV)
cinv = collections.Counter(e["kind"] for e in INV)
a("- Logged edits: %d in the eval sheet (%d entries plus %d conflict-id rewrites covering %d occurrences; the 14 Datasets bracket edits are 14 entries shown as one row), %d in the inventory; %d in total." % (len(EV) + len(CONF), len(EV), len(CONF), sum(c[2] for c in CONF), len(INV), len(EV) + len(CONF) + len(INV)))
a("- Eval by kind (entries, excluding the conflict-id rewrites, which are style): %s; conflict-id rewrites: style %d." % (kinds(EV), len(CONF)))
a("- Inventory by kind: %s." % kinds(INV))
a("- Resolution items touching text: eval %d distinct T-ids, inventory %d (table in section 8d). Items with no text change by design are listed there with the reason." % (len(tc_ev), len(tc_inv)))
a("- Summaries changed: 2 of 3 (Overview, Engine coverage). Red-teaming is unchanged (36 words, 38 with label); see litmus_summaries_preview.md.")
fin = {s["name"]: sec_counts[s["name"]] for s in secs}
a("- Final eval sections and items (default parser order): " + "; ".join("%s: %d Detail bullets, %d standalone bullets, %d table rows" % (n, v[0], v[1], v[3]) for n, v in fin.items()) + ".")
a("- Final inventory rows: " + ", ".join("%s %d" % (n, r) for n, r in inv_rows) + " (total %d)." % sum(r for _, r in inv_rows))
a("")
a("### 5b. P8 config notes (gr-xlsx-writer) and P9 notes")
a("")
a("- **Inventory sheet:** name '3x. Litmus Inventory' (20 characters; the letter is assigned at P8 in queue order, R003; Cloak is merged in parallel, so the letters may shift). New config module for the inventory (md = benchtest/drafts/litmus_inventory_final.md). BLOCKS (marker, bold title or None, expected rows): ('## (a) Access paths', 'Access paths', 4), ('## (b) Test suites', 'Test suites', 5), ('## (c) Integration parameters', 'Integration parameters', 6); 15 rows. Covered-by column name 'Covered by Table 3 column' in all three tables (the last-but-one column of each). Short-name legend is in the unparsed paragraph before block (a) and in the block (a) intro (parsed).")
a("- **Markers tuple:** only '— (inventory only, not in Table 3)' (R011), on all 15 rows; legacy and planned are not used. **Panel:** there are no Table 3 columns, so the panel must not require a non-zero Table 3 count or a COUNTIF against Table 3 headers (queue: litmus P1 Q-C); suggested panel items are row counts per block and the number of inventory-only rows (15 of 15). No validators are needed (no crosswalk blocks). No registry prefix, no column IDs, nothing added to products.py MDS or HDR_RE for Table 3.")
a("- **Eval sheet:** sheet name '3x. Litmus Eval Tooling' (23 characters with a one-letter prefix, at most 31), inserted right after the Litmus inventory sheet (R003). The builder needs MD = benchtest/drafts/litmus_eval_tooling_final.md, TITLE and NOTE; proposed TITLE '3x. GovTech Litmus Evaluation Tooling (hosted service, no release; playbook@45908b48)', proposed NOTE 'Evaluation-tool facts, the test list, published results and reuse assessment for the test bench (possible sources and suggestions, not decisions). Labels as in sheet 3.' SECTION_ORDER is unchanged; the file parses to 8 sections; the widest table has 8 columns (Tools). Notes under the Tools and Datasets headings carry the short-name legend and the Table 3 headers named.")
a("- **Sheet 3e cross-reference:** the Overview bullet names 'sheet 3e, columns AA to AG' in plain text (sheet 3e is the Sentinel inventory; the Sentinel columns on sheet 3 are AA to AG). If the P8 writer renumbers sheets, only that plain-text mention changes.")
a("- **URL check (P9):** %d distinct URLs in the two finals (litmus_urls.txt is not written by the merger). Do NOT request (hard rule 5, R019, lessons 12): %s. Expected non-200 by design: %s (HTTP facts kept in the text; the one-pager PDF answers 403 to plain curl and 200 to a browser User-Agent; aiguardian-litmus-test is a missing repository). github.com blob pages answer 403 from the session proxy: check the raw.githubusercontent.com equivalent at the same ref. The unpinned live URLs https://govtech-responsibleai.github.io/playbook/tools/wog-safety-testing/ and https://govtech-responsibleai.github.io/kaleidoscope/ are plain-text references." % (len(urls), "; ".join(NOREQ), "; ".join(EXPECT)))
a("- **Checker lines (inventory):** table '(a) Access paths': 4 rows x 8 cols; '(b) Test suites': 5 rows x 7 cols; '(c) Integration parameters': 6 rows x 7 cols.")
a("")
a("## 6. Remaining open items")
a("")
a("Counts in the finals: eval sheet [To be verified] %d and [Not disclosed] %d bracket labels in the whole file (Open questions: [To be verified] %d, [Not disclosed] %d of %d); inventory [To be verified] %d and [Not disclosed] %d. Class (b) items stay open as [Not disclosed] or [To be verified] statements and Open questions; none is closed without a source." % (
    brackets["To be verified"], brackets["Not disclosed"], oq_labels["To be verified"], oq_labels["Not disclosed"], len(oq), ibrackets["To be verified"], ibrackets["Not disclosed"]))
a("")
a("### 6a. Class b items (needs testing, honest gap or vendor reply), unchanged in substance")
a("")
a("| T-id | Class | Priority | Item | Where it stays open in the finals |")
a("|---|---|---|---|---|")
OPEN_B = [
    ("T15", "b", "L", "Is the Getting Started page the Litmus Onboarding Guide the portal links to (no capture of the guide)", "Open question [To be verified]; INV (a) onboarding row Caveats [Inferred] sentence"),
    ("T21", "b (honest gap)", "H", "Maturity: portal 'PROOF OF CONCEPT' (19 May 2025) versus docs, one-pager and playbook with no label", "Overview Summary carries the qualifier; Overview status bullets (source one [Documented], source two [Not disclosed]); Open question on maturity [Not disclosed]; INV (a) web app Status"),
    ("T24", "b (honest gap)", "L", "No release, version or release notes for the hosted service", "Overview [Not disclosed] bullet; INV scope paragraph"),
    ("T25", "b (honest gap)", "M", "Litmus API: no reference page; result schema, auth beyond the API key, rate limits; base_url link versus sample Action route", "Tools row 2; Engine coverage bullets; INV (a) API row Caveats"),
    ("T26", "b (honest gap)", "M", "CI/CD Action identity: documented dsaidgovsg/aiguardian-litmus-test versus archived sample", "Tools row 3; Open question [To be verified]; INV (a) CI/CD row"),
    ("T27", "b (honest gap)", "M", "Parameter table versus example workflow (test_suites, num_of_prompts, run_name default)", "INV block (c) rows; Open question on the Action name and test_suites"),
    ("T29", "b (honest gap)", "M", "Custom scenarios, user simulation and generic-testing wording (UI glitches, devices, browsers)", "Tools row 4; Red-teaming bullets; Open question [To be verified]; INV (b) custom row"),
    ("T32", "b (honest gap)", "M", "Kaleidoscope status: module within Litmus versus 'stay tuned' versus 'upcoming months'", "Overview bullets (three quotes); Open question [Not disclosed]; INV (b) Kaleidoscope row"),
    ("T33", "b (honest gap)", "H", "Evaluator or judge mechanism and backing model", "Overview bullet; Engine coverage bullet and Summary; Open question [Not disclosed]; Tools note"),
    ("T36", "b (honest gap)", "M", "Per-test dataset size, provenance, licence, languages, cadence", "Datasets note and Size/Licence cells; Reuse bullet; Open question [Not disclosed]"),
    ("T37", "b (honest gap)", "M", "'hundreds of curated prompts' versus num_of_prompts and the two suites", "Open question [Not disclosed]; INV (c) num_of_prompts row"),
    ("T38", "b (honest gap)", "M", "Pass or fail rule per test, scoring formula, report schema; docs pass/fail versus playbook refusal rate", "Published results rows 1 to 4, 7; Open question [Not disclosed]; INV (b) wog-baseline-v1 row"),
    ("T39", "b (honest gap)", "M", "Domestic Affairs: refuses versus neutral stance", "Datasets row Domestic Affairs (both quoted); Open question [Not disclosed]"),
    ("T45", "b (honest gap)", "M", "No published Litmus scores, sample report or schema", "Published results rows 'Published Litmus scores' and 'Sample report' [Not disclosed]"),
    ("T47", "b (honest gap)", "H", "Automated attack generation, mutation, adaptive or multi-turn red-teaming not described", "Red-teaming Summary and bullet [Not disclosed]; Open question on multi-turn and other test types"),
    ("T49", "b (honest gap)", "M", "Supported models, request and response formats, limits; two API keys under one name", "Engine coverage bullets (key bullets added); Open question on guardrailed endpoints"),
    ("T50", "b", "H", "Can a guardrailed (for example Sentinel-protected) endpoint be tested; how blocks are scored", "Engine coverage [Not disclosed] bullet and Summary; Open question [Not disclosed]"),
    ("T54", "b", "M", "Which host is current (production, staging, development) across five sources", "Engine coverage host bullets (five); Open question [To be verified]; INV (a) rows 1 and 2"),
    ("T56", "b", "M", "Retrieval, tool-call, multimodal and multi-turn tests, languages tested", "Open question [Not disclosed]"),
]
for r in OPEN_B:
    a("| " + " | ".join(r) + " |")
a("")
a("### 6b. Residual parts of handled items (verdict PARTLY RESOLVED, STILL OPEN class c, or an open question left in the finals)")
a("")
a("| T-id | Class | Item | Where it stays open |")
a("|---|---|---|---|")
OPEN_R = [
    ("T3", "c", "Litmus's own terms, pricing, quota, service levels, data handling and retention (the portal Terms of Use only say featured products have separate terms)", "Overview [Not disclosed] bullets (terms and absence, data handling); Open question on maturity and pricing; INV (a) rows 1 and 4 Caveats"),
    ("T4", "c", "Eligibility rule for organisations other than public sector teams", "Open question [Not disclosed]; INV (a) onboarding row Needs"),
    ("T5", "c", "Licence or reuse terms of the quoted GovTech material (no LICENSE in the playbook at 45908b48 or the Action repository)", "Overview [Not disclosed] bullet"),
    ("T6", "c", "Licence of the Kaleidoscope repository and terms of the arXiv paper (not researched, R038)", "new Open question [Not disclosed]; Tools row 6 Engine cell; INV (b) Kaleidoscope row"),
    ("T10", "a (PARTLY)", "Which official page links the one-pager PDF (none found on the AI Guardian, portal and playbook pages read)", "change log only (no sheet text states it)"),
    ("T28", "a (PARTLY)", "Whether the LitmusClient example exists as a package or API (no GovTech package on PyPI; an unrelated project named litmus)", "Open question [To be verified]; Tools row 5; INV (b) wog-baseline-v1 row"),
    ("T53", "a (PARTLY)", "Whether any of the 14 tests reuse AI Verify cookbooks or datasets (name resemblances only)", "Open question [Not disclosed]; Engine coverage name-resemblance bullet"),
]
for r in OPEN_R:
    a("| " + " | ".join(r) + " |")
a("")
a("### 6c. Closed by rulings or resolutions (not open)")
a("")
a("- T1, T2: R038 (small inventory sheet; Kaleidoscope one Tools row, GovTech pages only).")
a("- T7 (Apache-2.0 licence of moonshot, [Documented: repo aiverify-foundation/moonshot@0.7.6]), T8 (docs unpinned, source repository not found), T9, T12, T13, T14, T16 to T19, T22, T23, T30, T31, T34, T35, T40 to T44, T46, T48, T51, T52, T55, T57 to T63: applied as logged in sections 2 and 3.")
a("")
a("### 6d. Follow-ups noted for main (not Litmus sheet items)")
a("")
a("- A1: the Sentinel 3e note on the playbook pin (R007 item 7 rationale 'the deployed site is built from staging') may need the production-versus-staging note; main ruled this a final-summary follow-up (queue, litmus P5 Q1 to Q5).")
a("- The T6 not-researched list: the Kaleidoscope repository (licence, code), the arXiv paper terms and the main branch contents were not read, per R038.")
a("")
a("## 7. Moved Reviewer notes and process notes")
a("")
a("### 7a. litmus_eval_tooling.md, 9 notes (verbatim)")
a("")
st = [i for i, l in enumerate(ev0) if l.startswith("## Reviewer notes")][0]
for l in ev0[st + 1:]:
    if l.strip():
        a(l)
a("")
a("### 7b. litmus_inventory.md, 6 notes (verbatim)")
a("")
st = [i for i, l in enumerate(inv0) if l.startswith("## Reviewer notes")][0]
for l in inv0[st + 1:]:
    if l.strip():
        a(l)
a("")
a("### 7c. Process, method and not-in-sheet notes from the resolutions (moved here per T16, T9, T19, T44, T42, T10, T8, T6)")
a("")
for s in [
    "T16: one unauthenticated GET to https://huggingface.co/api/datasets outside the brief (nothing used or cited; covered by main's P4 Hub-metadata ruling); a browser User-Agent was needed only to download the one-pager PDF (md5 6423235d77ce909ea5742e52d41d7c92); every docs, portal, playbook and AI Guardian page answered plain curl with HTTP 200 (main P4 Q1: acceptable, logged, not repeated).",
    "T9: link targets (https://litmus.aiguardian.gov.sg/api/v1/, https://litmus.stg.aiguardian.gov.sg/login, the Onboarding Guide link, the playbook login link, the AI Guardian home page 'Try Litmus Now' link) were read from raw page HTML fetched with plain curl and the Python standard-library HTML parser, 2026-10-10 (R021); none was visited or called.",
    "T8 method: GitHub MCP repository search 2026-10-10 (litmus org:dsaidgovsg returns only dsaidgovsg/aiguardian-test-action, archived; litmus org:govtech-responsibleai returns 0; the govtech-responsibleai organisation lists 11 repositories, none a docs site for AI Guardian). The docs pages carry no edit link and no editUrl; Last-Modified Thu, 08 Oct 2026 08:42:14 GMT on all five docs pages.",
    "T10: no GovTech page read links the one-pager PDF (searched anchors for 'isomer' and '.pdf' on the AI Guardian home and docs pages, the five portal pages and the playbook Litmus page). PDF metadata CreationDate 2025-09-16, classification label 'Official (Open)'.",
    "T11 corrections: the triage premise 'line 46 cited for three different quotes' is accurate and not a defect (all three quotes are on line 46 of PB tools/litmus.md); the real defects were the safety.mdx range (429-441, comment 429-431), the action.yml body range (31-44, headers 45), benchmark_runner_dto.py@0.7.6 line 10, and the brief's '432-440' and the INV legend's '427 to 440' (brief and INV legend not carried into the finals).",
    "T19 / A1: the playbooks.aip.gov.sg host named in the LitmusClient code comment is the playbook's production site (README.md@45908b48:13 and :73-74); EV RN-8 and INV RN-5(vi) are dropped; no sheet text uses the host as a source.",
    "T44: the brief's list F21 of WOG taxonomy names (11) was short; the playbook table has 12 risk categories (Hateful L1 L2, Insults and Toxic, Sexual L1 L2, Self-Harm L1 L2, Graphic Content, Misconduct L1 L2, Domestic Politics, Geopolitics, Race and Religion, Financial Advice, Legal Advice, Medical Advice).",
    "T42: the Self-Harm description ends 'as long as they are out of context' (verbatim, odd wording); not quoted anywhere in the finals.",
    "T55: 'three hosts in five sources' (AI Guardian home page, PORTAL, playbook, the Getting Started link, the sample Action) replaces the brief's 'Four hosts' (the brief file is not edited).",
    "T6: not researched, per R038: the Kaleidoscope repository (licence and code), its main branch e806bf39bb4ccd1c5e8ab831ed8ef027fa4b5890 and the arXiv paper 2607.14673 terms.",
    "T28 / T53 / T52 non-vendor reads (main ruled acceptable, logged): a 2,158-byte wheel of an unrelated PyPI project named litmus was downloaded to scratchpad/resolver/litmus1/ and read as a zip (METADATA only, not installed or run); the PyPI simple index, the Internet Archive availability and CDX endpoints, playbooks.aip.gov.sg and aiverifyfoundation.sg pages were read with GET.",
    "Staging pin note: one compound command that would have created a bare clone under C:/t was denied by the permission system and not retried (resolver note).",
]:
    a("- " + s)
a("")
a("## 8. Self-check")
a("")
a("### 8a. Summary word counts (limit 45 excluding the trailing label; lessons 18 asks for at most 44)")
a("")
a("| Section | Words excl. label | Words incl. label | `**` count | Code chars | Result |")
a("|---|---|---|---|---|---|")
for n, w, wl, st_, cc, body in summ:
    a("| %s | %d | %d | %d | %s | %s |" % (n, w, wl, st_, "none" if not cc else "FOUND", "pass" if (w <= 44 and st_ % 2 == 0 and not cc) else "FAIL"))
a("")
a("### 8b. Items per section")
a("")
a("| Section | Detail bullets | Standalone bullets | Tables | Table rows | Bullets without a label |")
a("|---|---|---|---|---|---|")
for n, v in sec_counts.items():
    a("| %s | %d | %d | %d | %d | %d |" % (n, v[0], v[1], v[2], v[3], v[4]))
a("")
a("### 8c. Labels, structure and process wording")
a("")
a("- Open-question labels: %s of %d bullets; none other." % (", ".join("%s %d" % (k, v) for k, v in oq_labels.items()), len(oq)))
a("- Bracket forms in the eval final: " + ", ".join("[%s] %d" % (k, v) for k, v in sorted(brackets.items())) + "; every bracket is an allowed form (scan: none outside the allowed set).")
a("- Bracket forms in the inventory final: " + ", ".join("[%s] %d" % (k, v) for k, v in sorted(ibrackets.items())) + "; none outside the allowed set.")
a("- Pinned refs (every repo label has the pinned URL with the same ref in the file): " + "; ".join("%s x%d, URL with %s: %s" % p for p in pinrows) + ".")
a("- Process wording in the finals (counts; 0 expected): " + "; ".join("%s /%s/ %d" % (k[0], k[1], v) for k, v in badproc.items()) + ".")
a("- Inventory: no '**', no backtick in the final (checked); every Covered-by cell is '— (inventory only, not in Table 3)' (15 of 15); row counts per block %s." % ", ".join("%s %d" % x for x in inv_rows))
a("")
a("### 8d. Resolution items: edits per T-id (logged entries mentioning the id; section 2 for the eval sheet, section 3 for the inventory)")
a("")
a("| T-id | Verdict (resolver) | Eval edits | Inventory edits | If none |")
a("|---|---|---|---|---|")
for t, v, ne, ni, note in tid_rows:
    a("| T%d | %s | %d | %d | %s |" % (t, esc(v), ne, ni, esc(note)))
a("")
a("### 8e. Checker output (run from the repo root)")
a("")
a("```")
a("python benchtest/tools/check_drafts.py inventory benchtest/drafts/litmus_inventory_final.md")
a(chk_inv)
a("")
a("python -c \"import sys; sys.path.insert(0,'benchtest'); import build_eval_sheet as B; print(len(B.parse_md('benchtest/drafts/litmus_eval_tooling_final.md')))\"")
a(parse8)
a("```")
a("")
a("The columns checker (check_drafts.py columns ... --final --expect N) is not run: Litmus has no Table 3 columns (R003) and no litmus_two_level.md exists. The inventory checker was run without --headers for the same reason (no Table 3 headers to compare; the Covered-by cells are markers only).")
a("")
open(D + "litmus_changes.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")

# ------------------------------------------------------------------ summaries preview
P = []
p = P.append
p("# GovTech Litmus: Summary preview (Checkpoint 2)")
p("")
p("Generated from litmus_eval_tooling_final.md on 2026-10-10. Format: section (words excluding the trailing label, top-level Detail bullets): Summary text. Limit 45 words (lessons 18: at most 44 excluding the label). Summaries changed from the draft are marked with an asterisk after the section name. Litmus has no Table 3 columns, so these three Summaries are the only Summary lines.")
p("")
CH = {"Overview": "*", "Engine coverage": "*"}
for s in secs:
    for it in s["items"]:
        if it[0] == "summary":
            body = LAB.sub("", it[1]).strip()
            w = len(body.replace("**", "").split())
            nb = sum(1 for x in s["items"] if x[0] == "detail" for b in x[1] if b.startswith("• "))
            p("- **%s**%s (%dw, %d bullets): %s" % (s["name"], CH.get(s["name"], ""), w, nb, it[1]))
p("")
p("Counts: 3 Summaries, 2 changed (Overview, Engine coverage), 0 over the limit.")
open(D + "litmus_summaries_preview.md", "w", encoding="utf-8", newline="\n").write("\n".join(P) + "\n")
print("written", len(L), "lines")
