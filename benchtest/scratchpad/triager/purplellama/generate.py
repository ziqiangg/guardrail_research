import re, sys, io, collections
sys.path.insert(0, 'benchtest/scratchpad/triager/purplellama')
from items import ITEMS, GROUPS

OUT = 'benchtest/drafts/purplellama_triage.md'

# assign ids
for n, it in enumerate(ITEMS, 1):
    it['id'] = 'T%d' % n
ID = {it['key']: it['id'] for it in ITEMS}
assert len(ID) == len(ITEMS), 'duplicate keys'

# group ranges
for gi, g in enumerate(GROUPS):
    ids = [it['n'] if 'n' in it else None for it in ITEMS]
rng = {}
for it in ITEMS:
    rng.setdefault(it['group'], []).append(int(it['id'][1:]))


def R(text):
    def sub(m):
        k = m.group(1)
        assert k in ID, k
        return ID[k]
    return re.sub(r'<<(\w+)>>', sub, text)


def cls_letter(c):
    return c[0]


cnt = collections.Counter()
cnt_h = collections.Counter()
pri = collections.Counter()
cp1 = [it for it in ITEMS if it['cls'] == 'b-CP1']
hg = [it for it in ITEMS if it['cls'] == 'b-HG']
cls_pri = collections.Counter()
for it in ITEMS:
    c = cls_letter(it['cls'])
    cnt[c] += 1
    pri[it['pri']] += 1
    cls_pri[(c, it['pri'])] += 1
    if it['pri'] == 'H':
        cnt_h[c] += 1
N = len(ITEMS)

# per-file touches
def touches(it, pat):
    return re.search(pat, it['locs']) is not None
tA = sum(1 for it in ITEMS if touches(it, r'\bA[:\s]|A RN'))
tB = sum(1 for it in ITEMS if touches(it, r'\bB[:\s]|B RN'))
tI = sum(1 for it in ITEMS if touches(it, r'INV'))
tE = sum(1 for it in ITEMS if touches(it, r'\bEV'))
tO = sum(1 for it in ITEMS if touches(it, r'\bBR\b|queue|explorer|CLAUDE'))

L = []
w = L.append

w('# Purple Llama triage of open evidence items (DRAFT)')
w('')
w('Sources triaged: `purplellama_cols_a.md` (PL1, PL2, PL6, PL4), `purplellama_cols_b.md` (PL3, PL5, PL7), `purplellama_inventory.md` (sheet block (a) components 16 rows, (b) scanner catalogue 8, (c) roles 11, (d) Code Shield language matrix 16, (e) integration paths 12, (f) licences 8, (g) metrics 12, (h) adjacent 5; 88 rows in all), `purplellama_eval_tooling.md` (CyberSecEval, 8 sections), the brief `purplellama_brief.md`, the Reviewer notes sections (A 13, B 10, INV 7), rulings R002, R003, R004, R007, R009, R011, R013, R015, R019, R020, R021 (R025 as the AUP precedent) and the purplellama lines of `scratchpad/main/queue.md`. No research done; source suggestions only. Nothing here is verified. Written 2026-10-09 by gr-triager. Mechanical checks re-run at the start: `check_drafts.py columns` gives 0 errors on cols_a (1 warning: several prefixes, expected under option B) and 0 errors, 0 warnings on cols_b; `check_drafts.py inventory --headers` against the seven headers gives 0 errors, 0 warnings (16, 8, 11, 16, 12, 8, 12, 5 rows); `build_eval_sheet.parse_md` accepts the eval file (8 sections).')
w('')
w('## Legend')
w('')
w('- File short names: A = purplellama_cols_a.md, B = purplellama_cols_b.md, INV = purplellama_inventory.md, EV = purplellama_eval_tooling.md, BR = purplellama_brief.md. Line numbers are as at 2026-10-09 and move when the merger edits (`A:119` = line 119 of cols_a). `INV(f) row 101` and `INV:101` both mean file line 101 (a table row or a paragraph line); `INV(d) rows 64, 69` are the C++ and Kotlin lines.')
w('- Notes: `A RN-7(b)` = Reviewer note 7 item (b) in cols_a (A RN-1 to 13 at A:562-575); `B RN-n` (B:385-394); `INV RN-n` (INV:141-147). PL1 to PL7 are the draft column ids from the brief (PL1 Prompt Guard 2, PL2 PromptGuard scanner, PL3 AlignmentCheck, PL4 CodeShield scanner, PL5 Regex and custom, PL6 Code Shield engine, PL7 Hidden ASCII).')
w('- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; SUM = a Summary line. Other short names: PG2 = Prompt Guard 2, PG1 = Prompt Guard 1, ICD = Insecure Code Detector, CSE1 to CSE3 = the earlier CyberSecEval papers, LF = LlamaFirewall, AUP = Acceptable Use Policy, ZDR = zero data retention, pin = commit 172c1074.')
w('- Class: a = answerable from an official page, repo file at the pin, a Meta paper, or a third-party owner page that R019 allows citing as "not Meta docs"; b = needs testing (stays open for the bench) or is a CP1 decision item (closes when chosen, NeMo b22 precedent); `honest gap` (class b) = the vendor does not publish it and no public document is expected to answer; c = licensing, gating or terms.')
w('- Priority: H = changes an R1 to R7 Summary line (or an eval Summary), a Summary label, a headline number (version pin, the AUC, latency or language counts, column set) or a decision that fixes the column set; M = Detail level, or only an R8 Summary line (R8 Summaries list questions and are not counted as H, as in the Sentinel and Presidio triages); L = cosmetic or low impact.')
w('')
w('## Counts')
w('')
w('Total %d deduplicated items (T1 to T%d), drawn from the 71 R8 bullets (PL1 11, PL2 10, PL6 11, PL4 9, PL3 12, PL5 12, PL7 6), the explicit open labels (columns: ND 37 bullets, TBV 6 bullets; inventory: ND 25 cells, TBV 11 cells; eval: ND 10, TBV 8), the [Inferred] items that rest on an unchecked premise (columns 120 label occurrences, inventory 37, eval 23), the three Reviewer notes sections, the queue items routed to triage, and a cross-draft comparison of the four files.' % (N, N))
w('')
w('| Class | Count | of which H |')
w('|---|---|---|')
w('| a doc-answerable | %d | %d |' % (cnt['a'], cnt_h['a']))
w('| b needs testing or CP1 decision | %d | %d |' % (cnt['b'], cnt_h['b']))
w('| c licensing / terms | %d | %d |' % (cnt['c'], cnt_h['c']))
w('| Total | %d | %d |' % (N, pri['H']))
w('')
w('Priority totals: H %d, M %d, L %d.' % (pri['H'], pri['M'], pri['L']))
w('')
w('Class by priority: a: H %d, M %d, L %d; b: H %d, M %d, L %d; c: H %d, M %d, L %d.' % (
    cls_pri[('a', 'H')], cls_pri[('a', 'M')], cls_pri[('a', 'L')],
    cls_pri[('b', 'H')], cls_pri[('b', 'M')], cls_pri[('b', 'L')],
    cls_pri[('c', 'H')], cls_pri[('c', 'M')], cls_pri[('c', 'L')]))
w('')
w('Items touching each source file (an item can touch several): purplellama_cols_a.md %d; purplellama_cols_b.md %d; purplellama_inventory.md %d; purplellama_eval_tooling.md %d; brief / queue / explorer notes / CLAUDE.md %d.' % (tA, tB, tI, tE, tO))
w('')
w('CP1 decision items counted in class b: %s. Class b honest-gap items: %s.' % (
    ', '.join(it['id'] for it in cp1), ', '.join(it['id'] for it in hg)))
w('')
w('Dedup note: the same open question appears in several columns (threshold, latency and limits, release notes, PyPI parity, tool-call arguments, Together availability and terms, language count, per-call scanner creation) and is merged into one id with every location listed. Where a question has a documentation half and a run-it half it is split into two ids (a + b): <<thr_doc>> / <<thr_test>> (thresholds), <<tog_avail>> / <<tog_live>> (Together model availability), <<lf_reload>> / <<lf_reload_time>> (per-call scanner creation), <<cs_cov>> / <<cs_run>> (Code Shield rule paths). Licensing questions about the same Llama 4 text are split by what the user must decide: <<c_aup>> (test use), <<c_mau>> (user count), <<c_lictext>> (which text governs).')
w('')
w('Provenance note: cols_a, cols_b and the inventory state that docs pages were read raw with `fetch_text.py`, code from a shallow clone at the pin, and that WebFetch was not used for any quote or number, so no item is classed as depending on a summarising fetch. Facts that depend on something not read: the three gated HF card bodies (<<pin_hfcard>>), the PyPI sdists (<<pin_cs>>, <<pin_lf>>), the llama-cookbook files (<<pin_cookbook>>), the alignment-check evals dataset files (<<pin_aleval>>), the Together catalogue beyond one table read (<<tog_avail>>), the paper figure with per-language precision and recall (<<cs_pr>>), and the git history of the docs and the benchmark folder (<<samples>>, <<ev_maint>>).')
w('')
w('Raw label census (whole-file bracket occurrences, including Reviewer notes): A: [Documented] 68, [Documented: repo meta-llama/PurpleLlama@172c1074] 199, repo labels on the two PG2 HF repos 6, [Inferred] 71, [To be verified] 4, [Not disclosed] 19. B: [Documented] 41, PurpleLlama repo label 116, repo labels on the Maverick FP8 and alignment-check evals repos 2, [Inferred] 49, [To be verified] 4, [Not disclosed] 18. INV: [Documented] 43, PurpleLlama repo label 296, other repo labels 12, [Inferred] 37, [To be verified] 11, [Not disclosed] 25. EV: [Documented] 16, PurpleLlama repo label 55, other repo labels 4, [Inferred] 23, [To be verified] 8, [Not disclosed] 10.')
w('')
w('Groups (id ranges): ' + '; '.join('%s T%d to T%d' % (GROUPS[g][0], min(v), max(v)) for g, v in sorted(rng.items())) + '.')
w('')
w('## Already ruled (not reopened here)')
w('')
w('| Matter | Ruling | Effect on triage |')
w('|---|---|---|')
w('| Engine and wrapper stay separate columns (PL1 and PL2, PL6 and PL4) | queue.md q02 and q15, R004 | No item; the cross-references are checked in the contradictions |')
w('| AlignmentCheck is a column with the Trace-level label; R7 states the Together dependency | queue.md q04 | Terms questions go to class c (<<c_tog_pii>>, <<c_tog_ret>>) |')
w('| Pin = commit 172c1074 plus PyPI versions plus HF revisions, stated separately; release notes [Not disclosed] | queue.md q14, R020 | <<pin_notes>> is an honest gap; PyPI parity is <<pin_cs>>, <<pin_lf>> |')
w('| CyberSecEval 4 row Covered-by marker | queue.md P1 Q1, R011, R003 | Checked: INV(a) row 23 uses `— (inventory only, not in Table 3)` |')
w('| Sheet letters | queue.md P1 Q2, R003 | <<inv_letters>> only records wording to clean |')
w('| Research is read-only; needs-testing items stay open | R019 | No local-run consent item (unlike presidio); all b items wait for the bench |')
w('| "Not built for X" statements are [Inferred] with the premise named; absences are [Not disclosed] with what was checked | R015, R020, R007 item 5 | Used to label the Summary fixes in group "Summary labels and entailment" |')
w('| Llama Guard 3 and 4 are cross-referenced only | R004 | One plain sentence each in PL1 R2 and R3 and INV(f) and (h); checked, no Summary mentions Llama Guard |')
w('| P1 Q5 and Q6 (Llama AUP for red-teaming; Together API terms for traces) | queue.md Resolved: to P4 triage as class c | <<c_aup>>, <<c_mau>>, <<c_tog_pii>>, <<c_tog_ret>> |')
w('')
w('## Items for CP1 (decision-bearing for the user)')
w('')
w('Defaults are the triager\'s recommendations and match the brief where the brief drafted one. Nothing is decided here.')
w('')
w('### Q-A Header prefix (<<cp1_prefix>>)')
w('')
w('- Option B (drafted, default): per-tool prefixes `Prompt Guard 2:`, `LlamaFirewall:`, `Code Shield:`. Evidence: R009 says the prefix is the product\'s own name as its owner writes it; Meta names the three tools (and writes the first one three ways: Llama Prompt Guard 2, Prompt Guard 2, PromptGuard 2); `Llama Guard:` (also a Purple Llama tool) already has its own prefix on sheet 3; headers are shorter and the tool is visible at a glance. Cost: three registry prefixes at P8; the checker warns on several prefixes (expected).')
w('- Option A: one `Purple Llama:` prefix with the tool in a parenthesis. Evidence: R004 names it first; one registry entry; the inventory sheet and the diagram are titled Purple Llama either way. Cost: longer headers; Purple Llama is the umbrella project, not a tool a user installs.')
w('- Option C (mixed, raised in P0 q11, not drafted): `Purple Llama:` for the model and Code Shield, `LlamaFirewall:` for the scanners.')
w('- Switching later is mechanical: 7 `## Column` lines, the Covered-by cells in INV(a), (b), (c), (e) and the Evaluates cells in EV; no Summary or Detail changes. R004\'s example `Prompt Guard:` differs from the drafted `Prompt Guard 2:`; the header is fixed at CP1 and frozen after CP2 (R009).')
w('- Recommended default: option B.')
w('')
w('### Q-B Column set (<<cp1_pl7>>, <<cp1_pl8>>)')
w('')
w('- Default: seven columns PL1 to PL7, with PL7 Hidden ASCII provisional and PL5 one column.')
w('- PL7 Hidden ASCII. Keep (default): a distinct deterministic function, no dependency, named in the ScannerType enum, easy to test with a code-point oracle; P0 q13 recommended a column for it. Drop to inventory only: no Meta page describes it beyond one tutorial enum sentence, so purpose and support are inferred and its R2 Summary is [Inferred] only; Meta may not treat it as a supported feature (<<hid_supported>>).')
w('- PL5. One column (default, as drafted and as R004 lists it): Meta documents "Regex + Custom" as one layer; the LLM-prompt scanners are isolated in their own bullets. Split into PL8 (custom LLM-prompt scanning and PII check): different function and setup (Together key, experimental, PIICheck fails open, no docs page), and a PII scanner is what sheet 4 would want to group with the Presidio and Sensitive Data Protection columns. P0 q13 suggested inventory only for PIICheck and CustomCheckScanner. A split costs new R1 to R9 Summaries for PL8 and rewritten PL5 Summaries (<<s_pl5r2>>, <<s_other>>).')
w('- Column count: 6 (PL7 dropped), 7 (default), 8 (PL8 added); the Q-C role split would add two more.')
w('- Recommended default: keep PL7 as a column; keep PL5 as one column and revisit a PL8 split at CP2 if the user wants a PII group on sheet 4.')
w('')
w('### Q-C LlamaFirewall direction (<<cp1_dir>>)')
w('')
w('- Option 1 (drafted, default): one column per scanner, roles listed in Detail (R3, R6 and INV(c)). Evidence: no per-direction rail, flag or endpoint; scanner logic is identical across roles; defaults mix roles (INV(c) rows 45-49); the Sentinel LionGuard 2 and Presidio precedents.')
w('- Option 2: split by role. PromptGuard scanner into an input column (USER, SYSTEM) and a tool/retrieval column (TOOL, MEMORY); CodeShield scanner into an assistant-output column (ASSISTANT) and a tool-output column (TOOL); Regex and Hidden ASCII stay one column each. Evidence: R002 names prompt roles as a direction surface and keeps the split for a wrapper with per-direction configuration; test inputs differ by role. Cost: five roles not two, the same code path for each, two more near-identical columns.')
w('- Sub-question (level words): PL1, PL2, PL4, PL6 are headed Input-level or Output-level but their R3 says the string or role is arbitrary, and Meta evaluated PromptGuard on user and tool messages only. R002 lets an undifferentiated check be one column when R3 and R6 explain both uses; the Sentinel LionGuard 2 precedent carries no level word. Keeping the words is defensible because Meta\'s own intended-use text is one-sided (PromptGuard: "user inputs and untrusted content"; CodeShield: "output scanning").')
w('- Recommended default: option 1, level words kept, with R3 and INV(c) carrying the role detail (already drafted).')
w('')
w('### Q-D Bench design: own injection-removed negatives (<<cp1_neg>>)')
w('')
w('- Option 1: yes, the bench builds its own negatives by removing the injected span from the 251 English cases (and the multilingual file), documents the method, and treats results as bench-internal, not comparable to Meta\'s CSE3 figure. Evidence: the data is Meta-written and MIT (EV:52); the CSE3 method used matching injection-removed negatives (EV:70); the repo ships none (EV:108, EV:121); cases embed a secret-key task so removed-text negatives may be unrepresentative.')
w('- Option 2: no; use only external benign corpora and the 750 MITRE false-refusal prompts (EV:111) as negatives. Cost: no matched pairs, so a classifier that keys on topic rather than override intent cannot be separated.')
w('- Option 3: both, reported separately.')
w('- Recommended default: option 3 (own matched negatives plus external benign sets, results labelled bench-internal). Related open point: <<ev_neg>> may find that CSE3 published its negatives.')
w('')
w('### Also for CP1 or CP2: class c judgements (record, decide later, as R025)')
w('')
w('- <<c_aup>> and <<c_mau>>: default as R025 ruling 1, quote the AUP clause as [Documented], keep "whether bench red-team testing is permitted" as an open R8 item, and let the user or their legal contact settle it before any Prompt Guard 2 or PromptGuard scanner test starts. Evidence: only item 2.8 is close; no clause names security testing; the 700 million user clause depends on the organisation.')
w('- <<c_tog_pii>> and <<c_tog_ret>>: default as R025 ruling 2, a bench rule that AlignmentCheck, PIICheck and CustomCheckScanner are tested with synthetic data only (Together terms section 4 bars sensitive personal data; ZDR is an account setting with an unstated default), recorded in PL3 R7 and PL5 R7 and in INV(f).')
w('- <<c_semgrep>>: default to record the LGPL 2.1 fact and the dependency in INV(f) and leave legal consequences to the user; no bench blocker is evident from the drafts.')
w('- <<c_csedata>>: default to reuse only Meta-written MIT CyberSecEval data (prompt injection, MITRE, interpreter, spear phishing) and keep CrowdStrike, ARVO and third-party-code-derived data out of any redistributed bench artefact until the owners\' licences are read.')
w('- Local-run consent: not needed; R019 keeps all needs-testing items for the bench.')
w('')
w('## Triage table')
w('')
w('| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |')
w('|---|---|---|---|---|---|')
CLSNAME = {'a': 'a', 'b': 'b', 'b-CP1': 'b (CP1 decision)', 'b-HG': 'b (honest gap)', 'c': 'c'}
cur = None
for it in ITEMS:
    row = '| %s | %s | %s | %s | %s | %s |' % (it['id'], R(it['item']), R(it['locs']), CLSNAME[it['cls']], R(it['src']), it['pri'])
    # table safety
    body = row[1:-1]
    assert body.count('|') == 5, (it['id'], body.count('|'))
    w(row)
w('')

# ------------------------------------------------------------------ label hygiene
w('## Label hygiene')
w('')
w('Scope: the four files against `drafts/README.md` section 3 and section 6. Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Mechanical scan result: every label bracket in A and B is one of the allowed forms (one apparent hit, A:570, is the plain text "Documented: repo" in a Reviewer note); the inventory has one non-label brace form (`{I}`, INV:135); EV uses only allowed forms but stacks two labels on three Summaries. Repo labels use `meta-llama/PurpleLlama@172c1074` in all four files; HF repos carry their own revision labels (`meta-llama/Llama-Prompt-Guard-2-86M@a8ded8e6`, `...22M@11614a15`, `Prompt-Guard-86M@1209add6`, `Llama-4-Maverick-17B-128E-Instruct-FP8@94125d2b`, `facebook/llamafirewall-alignmentcheck-evals@d50916c9`, `facebook/cyberseceval3-visual-prompt-injection@79336620`, `facebook/CyberSecEval@164ca0b7`). No verbatim quote reaches 40 words (largest scanned: 38 words in EV:54, which README allows). Column bullets: one label per bullet in all 7 columns (0 multi-label bullets by regex); the multi-fact bullets are listed below.')
w('')
w('| Issue | Where | Proposed fix | T-id |')
w('|---|---|---|---|')
HY = [
 ("Summary label stronger than the weakest fact it draws on (README section 4 rule 5): PL4 R4, PL4 R6, PL5 R2, PL1 R3, PL2 R6", "A:464, A:500, A:217, A:30; B:172", "Relabel or reword to the documented parts (several Summaries sit at 43 to 45 words, so no additions)", "<<s_pl4r4>>, <<s_pl4r6>>, <<s_pl5r2>>, <<s_pl1r3>>, <<s_pl2r6>>"),
 ("Summary sentences with no supporting bullet in the same row", "B:7, B:159, B:200; A:141, A:283, A:318", "Add the bullet or trim", "<<s_other>>"),
 ("Two bold labels on one Summary line", "EV:6, EV:80, EV:90", "One label equal to the weakest fact; move the note out", "<<s_ev>>"),
 ("Non-standard label form `{I}`", "INV:135", "Use [Inferred] with the premise", "<<h_brace>>"),
 ("Same fact, different labels across files: CyberSecEval 4 paper not located is [To be verified] in INV(a) row 23 and the brief, [Not disclosed] in EV:13 and EV:120", "INV:23; EV:13, EV:120", "One label; [Not disclosed] if the search is complete", "<<ev_paper>>"),
 ("Same fact, different labels inside the columns: tool-call arguments are not scanned is [Inferred] in five columns and a [Documented] Summary claim in PL4 R3", "A:161, A:175, A:450, A:461; B:43, B:245", "One convention after re-running the grep (R020: absence = [Not disclosed] with the search named)", "<<tool_calls>>"),
 ("Own counts labelled [Documented: repo] (INV(d) 16 rows, rule counts, dataset sizes) against the Presidio rule that the label needs a vendor-stated number", "INV:63-78; A:301, A:328, A:447; EV:22-61", "[Inferred] 'counted by parsing', or plain text '(count made from the file)'", "<<h_counts>>"),
 ("Counts that are the drafter's own CWE tally carry first-person wording and [Inferred]", "A:395, A:531, A:570", "Neutral wording: 'a count of cwe_id values in the rule files gives about 47'", "<<cs_cwe>>"),
 ("Bullets with two facts or two labels", "B:55, B:57, B:99; EV:16, EV:83", "Split; B:99 is a code absence (R020: [Not disclosed] with the search named is acceptable)", "<<h_multi>>"),
 ("Open-question bullets in EV carry [Documented: repo] (README section 6: [To be verified] or [Not disclosed])", "EV:126-128", "Move the three conflicts to Detail; keep real questions only", "<<ev_conf>>"),
 ("Inventory cells that state a fact without any label ('no unit test file found in tests/'; 'Not applicable'; 'Setup step, no scanning')", "INV:66, INV:71, INV:85, INV:87", "Label the fact or drop the remark", "<<inv_notnamed>>"),
 ("Third-party facts cited without a 'not Meta docs' note: Semgrep LICENSE is attributed; Together terms and model table are attributed in B and INV; the HF API JSON is not attributed as a vendor API read", "INV:106; B:109-110, B:102-103; A:49-50", "Compliant with R019 for the first two; the third needs the q_hfapi ruling", "<<c_semgrep>>, <<q_hfapi>>"),
 ("Provisional wording in finals: 'proposed 3j', 'sheet 3x', 'provisional' column, 'checkpoint'", "INV:1, INV:3, INV:23, INV:135; B:311", "Replace after CP1 and P8 letter assignment", "<<inv_letters>>, <<h_process>>"),
 ("Process and session language in Detail (R019 as a reason, 'research does not install', 'my count', 'Not requested during research')", "B:102, B:107, B:119, B:121, B:253, B:358; A:116, A:395, A:531; INV:85", "Product-neutral rewording", "<<h_process>>"),
 ("Unpinned or API URLs in R9 and inventory source cells", "A:134-135; B:148, B:153-155; INV:94, INV:135", "Pin or note read date; ruling on API JSON", "<<h_url>>, <<q_hfapi>>"),
 ("Draft ids (PL1..PL7) as cross-references in Detail and in EV", "A:66, A:147, A:197, A:236, A:281, A:427, A:519; B:63, B:198, B:234; EV:22-32", "Header text or sheet column letters", "<<h_ids>>"),
 ("Reviewer notes sections must leave the finals", "A:561-575; B:384-394; INV:139-147", "Move to purplellama_changes.md", "<<h_rn>>"),
 ("Locator inconsistencies for the same source (paper sections, card line ranges)", "A:77, A:81-82, A:213; B:10-11; INV:14, INV:116, INV:118, INV:120", "Standardise on the section where the quoted text sits", "<<h_loc>>"),
]
for a, b, c, d in HY:
    assert '|' not in (a + b + c + d)
    w('| %s | %s | %s | %s |' % (R(a), R(b), R(c), R(d)))
w('')
w('Covered-by check: every "Covered by Table 3 column" cell in INV(a), (b), (c), (e) is either a ;-separated list of exact headers from the seven column headings or the marker `— (legacy, not in Table 3)` (Prompt Guard 1) or `— (inventory only, not in Table 3)` (CyberSecEval 4, ClassifyIt, the CyberSecEval command-line row); no `planned` marker; the checker confirms the headers. Blocks (d), (f), (g), (h) carry no Covered-by column, as the brief specifies. The INV config for P8 needs the legacy and inventory-only markers (R011).')
w('')

# ------------------------------------------------------------------ style
w('## Style issues in columns')
w('')
STY = [
 "Summaries are within limits (checker: 0 errors). Closest to the cap: PL4 R3 45 words, PL3 R8 45, PL4 R5 44, PL3 R6 44, PL5 R8 44, PL2 R1 43, PL6 R2 43 (R7 inside 60). Every Summary fix in <<s_pl4r4>> to <<s_other>> must not add words. All R8 Summaries start `**Key open questions.**` with no label; all R9 Summaries are plain; no underscores, backticks or `$` in any Summary.",
 "Code-like identifiers in Summaries (README forbids them): role enum names in capitals in PL2 R3 (\"USER and TOOL\", \"SYSTEM\"), PL2 R7 (\"USER role\"), PL4 R3 (\"ASSISTANT and TOOL roles\"); class names \"Message\" (PL2 R6) and \"Scanner\" (PL5 R1). Write \"user and tool messages\", \"a message\", \"a scanner\".",
 "Process language and ruling ids in Detail: see <<h_process>> (R019 named in B:102, B:107, B:253, B:358; \"checkpoint\" in B:170, B:258, B:272, B:311; \"my count\" in A:395, A:531).",
 "Draft ids used as cross-references (\"column PL1\", \"column PL4\", \"the Regex column, PL5\"): <<h_ids>>. The workbook carries no ids; the merger replaces them after CP1 (Q-A) and P8 (letters).",
 "Internal source letters in language bullets: PL6 R2 uses \"source A (7)\", \"source B\", \"B2\", \"C\", \"D\", \"D2\", \"E\" while PL4 R2 uses \"A\", \"A2\", \"B\", \"C\", \"D\" for the same sources with different letters (A:292-298, A:435-440). The letters mean nothing in the sheet; write \"The Code Shield README says ...\" and \"The ICD README says ...\" as plain pairs. Same for \"Latency, statement 1 to 4\" (keep or name the source only).",
 "Locator formats differ between files: cols_a `file@172c1074:line` without backticks, cols_b `file@172c1074:line` in backticks or \"(docs page scanners/alignment-check, line 4)\", INV \"(lines 21-29)\" without the file ref, EV \"(CSB/README.md:8-9)\". Choose one form at merge.",
 "Spelling: ordinary words British (licence, organisation, analyser) except vendor class names; the inventory uses \"analyzer\" (10 occurrences, some inside identifiers such as LANGUAGE_ANALYZER_MAP, e.g. INV(a) row 22) where the columns write \"analyser\" 12 times (R009 keeps vendor spelling only for product and class names such as Analyzer).",
 "Long bullets: no wrapped bullets in A or B; the longest EV bullets reach 640 characters (EV:83, EV:95, EV:97) and carry several facts each.",
 "R9 lists: one URL per bullet in all seven columns (checker). PL1 R9 includes two huggingface.co/api JSON URLs (A:134-135; see <<q_hfapi>>); PL3 R9 and PL5 R9 include live docs-site URLs next to the pinned .md URLs (B:148, B:294-296); PL3 R9 includes two Together pages (B:153-155) which are third-party and are flagged as such only in the Summary. Every repo URL is a full-SHA blob URL; HF URLs are tree URLs at the revision.",
 "Repetition: the pin-kinds bullet (\"Pins, stated separately ...\") is repeated in PL3, PL5, PL7 R4 (B:57, B:217, B:335) and the \"no release\" ND appears in 8 R4 bullets; acceptable so each column stands alone after a merge.",
 "R7 first bullet and Summary start `**Minimum setup:**` and are [Inferred] in all seven columns: compliant. PL3 R7 carries two [Documented] Together-terms bullets (B:109-110) inside an [Inferred] row; allowed, they are quotes.",
 "EV: the Tools table \"Evaluates (Table 3 columns)\" cell mixes prose, reuse ideas and PL ids; README section 6 asks for sheet 3 headers or plain function names. Final cells should name exact headers (after Q-A) or plain functions. The table is wide (8 columns, rows up to about 1,500 characters).",
]
for n, s in enumerate(STY, 1):
    w('%d. %s' % (n, R(s)))
w('')

# ------------------------------------------------------------------ contradictions
w('## Contradictions')
w('')
w('Source conflicts and cross-file inconsistencies, each with the ids that resolve them. "Both written" means the drafts already carry two labelled bullets (README rule 4).')
w('')
CON = [
 "Code Shield language count: 7 (CodeShield README, llama.com, paper section 4.4, CSE3) versus 8 (ICD README, LlamaFirewall README and docs, paper summary, code returns 8); the enum has 16 members and the analyser map 14 entries. Both written in PL4 R2, PL6 R2 and INV(d). See <<cs_lang>>.",
 "Code Shield latency: README (99% within 70 ms, p90 450 ms), LlamaFirewall docs (under 100 ms and about 300 ms), paper (about 60 ms and about 300 ms), llama.com (average 200 ms); the eval sheet adds CSE3 (within 60 ms, about 300 ms) which the columns and INV(g) do not list, and INV(g) says there are four statements. Both written, five sources in total. See <<cs_lat>>, <<cs_cse3>>.",
 "Code Shield CWE coverage: README \"more than 50+ CWEs\", CSE3 \"50 different CWEs\" and \"around 190 patterns\", own counts 47 / 63 / 65 (enabled rules, CyberSecEval rules, all languages), config.yaml 38 regex ids and 77 Semgrep ids. See <<cs_cwe>>.",
 "Rule coverage by language: analyser map regex-only for PHP and Rust, but PHP Semgrep rules exist; Rust in the default scan list with no CODESHIELD rules; C++ generated Semgrep JSON has 16 rules while config.yaml lists none for cpp (93 versus 77 rule ids). Inferred in PL6 R2, INV(d). See <<cs_cov>>.",
 "codeshield versions: repo pyproject 0.0.1, PyPI 1.0.0 and 1.0.1, llamafirewall requires >=1.0.1. See <<pin_cs>>, <<pin_lf>>.",
 "Prompt Guard 2 86M English AUC: card .998, paper table .98. Both written. See <<auc>>.",
 "Prompt Guard 2 parameter counts: card 86M and 22M backbone, HF safetensors 278.8M and 70.8M. See <<pg2_params>>.",
 "Prompt Guard 2 scope wording (brief C9): card says injection and jailbreak, README \"direct prompt injection\", docs page \"direct jailbreak\", paper \"explicit jailbreaking\"; all four written in PL1 R2 and PL2 R2. No item.",
 "Prompt Guard 2 licence text: folder LICENSE files are Llama 4; the README links ../LICENSE, the Llama 3.2 root file; the root README licence table has no Prompt Guard 2 row. Prompt Guard 1 has three versions. Only INV(f) records the link conflict; PL1 R4 does not. See <<c_lictext>>, <<c_pg1>>.",
 "Scanner enum name: docs use-case page PROMPT_INJECTION versus enum PROMPT_GUARD (PL2 R3, INV(b), INV(c)). Both written. See <<name_pi>>.",
 "Which scanners exist (brief C4): README and docs name four components, the code has seven; Hidden ASCII and PII_DETECTION are named in one tutorial sentence only. Recorded in PL7 R1, PL5 R2 and INV(b). See <<hid_supported>>, <<pii>>.",
 "Regex layer \"configurable\" (architecture page) versus a fixed pattern constant; custom-scanner how-to (BaseScanner, edit create_scanner) versus Scanner plus register_llamafirewall_scanner. Both written. See <<rx_conf>>, <<rx_docs>>.",
 "Docs sample outputs versus code (how-to page, regex tutorial): reason text and score on allow. See <<samples>>.",
 "AlignmentCheck scope: docs \"reasons over the entire execution trace\" versus the system prompt \"Only consider the selected action\". Both written (PL3 R2). See <<al_scope>>.",
 "AlignmentCheck tool outputs: paper mitigation excludes direct tool outputs, code filters nothing by role. Both written (PL3 R3). See <<al_tool>>.",
 "AlignmentCheck context: paper says the trace is truncated to a fixed window, code does not truncate (the code side is a [Not disclosed] absence). See <<al_ctx>>, <<h_multi>>.",
 "AlignmentCheck prompt tailoring: paper says custom few-shot examples are possible, code keeps the prompt in a module constant; both sides sit in one bullet under one label (B:55; B RN-1c). See <<h_multi>>.",
 "AlignmentCheck ASR drop: 83% (section 4.2 rounding) versus 84% (section 4.3.2); consistent within rounding, both written. No item.",
 "Default judge availability: Meta code defaults to Maverick on api.together.xyz; Together docs show api.together.ai and a model table without a Maverick row. See <<tog_avail>>, <<tog_live>>.",
 "Together terms: PL3 R7 and PL5 R6 quote section 4 (sensitive personal data) but INV(e) row 91 and INV(f) row 107 omit it and say only that models carry their own terms and ZDR is a setting. See <<c_tog_pii>>.",
 "Judge-model licences: PL3 R4 read the Maverick HF metadata (license_name llama4, gated manual); INV(f) row 107 says the Maverick and Llama 3.3 licences were not read. See <<c_tog_model>>.",
 "CyberSecEval 4 paper: [To be verified] in INV(a) row 23 and the brief, [Not disclosed] in EV. See <<ev_paper>>.",
 "CyberSecEval README versus files: secure-code benchmarks \"temporarily removed\" versus run.py registration; AutoPatch counts (README 142/120/20, files 136/113/20, blog 136/113); provider lists (README five, docs-site OpenAI/Anyscale/Together, code five); docs-site command names and a 404 link. See <<ev_instruct>>, <<ev_conf>>.",
 "CSE2 injection range 26 to 41% versus 13 to 47% in one paper. See <<ev_cse2>>.",
 "Semgrep pins: codeshield needs semgrep>1.68, CyberSecEval requirements pin 1.51.0. See <<cs_semgrep_pin>>.",
 "Header level words versus R3: PL1, PL2, PL4, PL6 are headed Input-level or Output-level while R3 says any string or any role (Meta evaluated PromptGuard on user and tool messages, CodeShield is documented for output). See <<cp1_dir>>.",
 "Reviewer note versus Summary: B RN-6 says the PL5 R2 Summary uses only [Documented] facts, but \"US-style\" is [Inferred]. See <<s_pl5r2>>.",
 "Per-call scanner creation (llamafirewall.py:117-118) appears in PL2 R4, R7, R8 and PL5 R4 but not in INV(b); the PL5 R4 Summary says patterns are \"compiled once\". See <<lf_reload>>, <<s_other>>.",
 "Paper locators differ between files: AgentDojo section 4.3 (columns) versus 4.3.2 (INV(g)); AlignmentCheck experimental section 1 and Figure 2 (PL3) versus section 4.2 (INV(a)). See <<h_loc>>.",
 "Brief versus findings (recorded as corrections in the Reviewer notes): Hidden ASCII and PII are not code-only (named once in a tutorial); PHP and Rust mapping; \"over 50 CWEs\" against about 47; gate page for the 22M repo (brief G-h said unread, INV(e) row 85 says read). No open item.",
 "Wrapper statements consistent across files: TOGETHER_API_TOKEN accepted by configure.py but only TOGETHER_API_KEY read (PL3 R6, INV(e) row 87); CyberSecEval --enable-lf stored and unused (INV(e) row 95, EV:100); no tool_calls reader (five columns, INV(c) intro). No conflict; see <<tool_calls>>, <<ev_enable>>.",
]
for n, s in enumerate(CON, 1):
    w('%d. %s' % (n, R(s)))
w('')
w('Cross-file values compared and found consistent (by reading): commit pin 172c1074 and author date 2026-09-29; PyPI latest files (llamafirewall 1.0.3, codeshield 1.0.1); HF revisions a8ded8e6, 11614a15, 1209add6; PG2 card values (.998, 97.5%, .995, 92.4 ms; .995, 88.7%, .942, 19.3 ms; 81.2% and 78.4%); default thresholds PromptGuard 0.9, Regex 1.0, Hidden ASCII 1.0, CodeShield 1.0, PIICheck 0.7, CustomCheckScanner 0.0; no-config role defaults (TOOL: CODE_SHIELD and PROMPT_GUARD, USER: PROMPT_GUARD, ASSISTANT: CODE_SHIELD, SYSTEM and MEMORY empty); AlignmentCheck decisions (ALLOW or HUMAN_IN_THE_LOOP_REQUIRED, never BLOCK; fail closed on LLM error, open on a missing trace); config.yaml regex rule ids 38 equal the sum of the INV(d) enabled counts (5+2+2+14+1+3+3+0+8) and the 77 Semgrep ids equal the INV(d) generated counts without C++ (16+20+11+13+7+10); the analyser map (7 regex plus Semgrep, 7 regex only) matches INV(d); the 16 enum members and 8 default languages match between PL4 R2, PL6 R2 and INV(d); the seven column headers are identical in the brief, the column files and every INV Covered-by cell; inventory row counts equal the brief targets (16, 8, 11, 16, 12, 8, 12, 5). Compared by reading, not by execution.')
w('')

open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('items', N, dict(cnt), 'H', pri['H'], dict(pri))
print('cp1', [i['id'] for i in cp1])
print('hg', [i['id'] for i in hg])
print('H items', [(i['id'], i['key']) for i in ITEMS if i['pri'] == 'H'])
print('touch', tA, tB, tI, tE, tO)
print('ranges', {GROUPS[g][0]: (min(v), max(v)) for g, v in rng.items()})
