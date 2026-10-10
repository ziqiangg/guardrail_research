# -*- coding: utf-8 -*-
import re, sys, json
sys.path.insert(0, 'benchtest/scratchpad/triager/litmus')
from items import ITEMS

OUT = 'benchtest/drafts/litmus_triage.md'
ids = {it['key']: 'T%d' % (i + 1) for i, it in enumerate(ITEMS)}
for i, it in enumerate(ITEMS):
    it['id'] = 'T%d' % (i + 1)

def res(s):
    return re.sub(r'\{(\w+)\}', lambda m: ids[m.group(1)] if m.group(1) in ids else m.group(0), s)

CLS = {'a': 'a', 'b': 'b (needs testing)', 'bg': 'b (honest gap)', 'bc': 'b (CP1 decision)', 'c': 'c'}
def cls_base(c):
    return {'a': 'a', 'b': 'b', 'bg': 'b', 'bc': 'b', 'c': 'c'}[c]

# ---------- counts
from collections import Counter, defaultdict
cp = Counter(); cnt = Counter(); gaps = []; cp1 = []; cl_c = []
for it in ITEMS:
    cnt[(cls_base(it['cls']), it['prio'])] += 1
    if it['cls'] == 'bg': gaps.append(it['id'])
    if it['cls'] == 'bc': cp1.append(it['id'])
    if it['cls'] == 'c': cl_c.append(it['id'])
def tot(c): return sum(v for (k, p), v in cnt.items() if k == c)
def totp(p): return sum(v for (k, pp), v in cnt.items() if pp == p)
N = len(ITEMS)
Hs = [it for it in ITEMS if it['prio'] == 'H']
fcount = Counter()
for it in ITEMS:
    for f in it['files']:
        fcount[f] += 1
groups = []
cur = None
for it in ITEMS:
    if cur is None or cur[0] != it['group']:
        cur = [it['group'], it['id'], it['id']]
        groups.append(cur)
    else:
        cur[2] = it['id']
grp_txt = '; '.join('%s %s to %s' % (g, a, b) for g, a, b in groups)

def line(c, label):
    h = cnt[(c, 'H')]; m = cnt[(c, 'M')]; l = cnt[(c, 'L')]
    return '| %s | %d | %d |' % (label, tot(c), h), (c, h, m, l)

o = []
w = o.append
w('# Litmus triage of open evidence items (DRAFT)')
w('')
w('Sources triaged: `litmus_eval_tooling.md` (evaluation-tooling draft, 8 sections: Overview 19 bullets, Tools 6 rows, Datasets 16 rows, Published results 7 rows, Red-teaming 7 bullets, Engine coverage 19 bullets, Reuse 10 bullets, Open questions 19 bullets; Reviewer notes 9), `litmus_inventory.md` (sheet 3x draft, option (a): (a) access paths 4 rows, (b) test suites 5, (c) integration parameters 6; 15 rows; Reviewer notes 6), the brief `litmus_brief.md` (scope, pins, facts to re-verify F1 to F23, conflicts C1 to C11, open items, Q-A and Q-B), rulings R003, R007, R011, R013, R015, R019, R020, R021, R032 (R002 and R009 as format precedents), and the litmus lines of `scratchpad/main/queue.md` and `log.md`. Litmus has no Table 3 columns (R003), so there is no columns draft. No research done; source suggestions only. Nothing here is verified. Written 2026-10-10 by gr-triager. Mechanical checks re-run at the start: `check_drafts.py inventory litmus_inventory.md` gives 0 errors and 0 warnings (tables 4, 5 and 6 rows; 8, 7 and 7 cells); `build_eval_sheet.parse_md` accepts the eval file (8 sections in order); every Summary has balanced `**` and no backtick, underscore or `$`; all 15 Covered-by cells equal `— (inventory only, not in Table 3)`.')
w('')
w('## Legend')
w('')
w('- File short names: EV = litmus_eval_tooling.md, INV = litmus_inventory.md, BR = litmus_brief.md, queue = `scratchpad/main/queue.md`. Line numbers are file lines as at 2026-10-10 and move when the merger edits (`EV:94` = line 94 of the eval draft; `INV:15` = the CI/CD row; `INV(b)` = block (b), lines 24-28). EV sections by line: Overview 6-30, Tools 38-43, Datasets 47-66, Published results 70-80, Red-teaming 83-91, Engine coverage 94-114, Reuse 117-126, Open questions 129-147, Reviewer notes 150-158. `EV RN-n` = Reviewer note n (9 notes, EV:150-158); `INV RN-n` (INV:45-50, 6 notes); `INV(a) row 4` = the onboarding row.')
w('- Other short names: DOCS = www.aiguardian.gov.sg wiki pages (Litmus-Overview, Litmus-Getting-Started, Litmus-Troubleshooting, Test-Information-Documentation; also AIG in INV); PORTAL = developer.tech.gov.sg Litmus pages (DEV in INV); PB = playbook files at `govtech-responsibleai/playbook@45908b48`; ACT = sample Action `dsaidgovsg/aiguardian-test-action@v0.0.1`; MS = `aiverify-foundation/moonshot` (AI Verify Foundation, not GovTech); F1 to F23 = the brief\'s facts to re-verify; C1 to C11 = the brief\'s conflicts, C12 and later are new in this triage.')
w('- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; SUM = a Summary line (Litmus has three: Overview EV:6, Red-teaming EV:83, Engine coverage EV:94; the other sections have none).')
w('- Class: a = answerable from an official page, a pinned repo file, a public GovTech or AI Verify page, or a drafting fix that needs no research; b = needs testing, access or the vendor (stays open); `honest gap` (class b) = closed or undisclosed vendor internals, or a vendor plan, where no public document is expected to answer; `CP1 decision` (class b) = closes when the user chooses (NeMo b22 and Presidio precedent); c = licensing, terms or access conditions.')
w('- Priority: H = changes an R1 to R7-style Summary line (here the three Summaries) or a Summary label or claim, a headline number (here the 2 suites, 6 and 14 tests, 4 categories), or fixes the sheet set (CP1 decisions, as the column-set decisions did in the Purple Llama and LionGuard triages); M = Detail, cell or Open-question level, or only an Open-question line; L = cosmetic or low impact. Open-question lines are not Summaries and are not counted as H.')
w('')
w('## Counts')
w('')
w('Total %d deduplicated items (T1 to T%d), drawn from the 19 Open questions, the explicit open labels (bracket occurrences in the eval draft: ND 55, TBV 11, INF 19; in the inventory draft: ND 24, TBV 7, INF 7), the two Reviewer-notes sections (EV 9, INV 6), the brief conflicts C1 to C11 plus ten new conflicts found in triage (C12 to C21), the queue items routed to triage (Q-A, Q-B), and a cross-draft comparison of the eval draft, the inventory draft and the brief.' % (N, N))
w('')
w('| Class | Count | of which H |')
w('|---|---|---|')
for c, lab in (('a', 'a doc-answerable (incl. drafting fixes)'), ('b', 'b needs testing, honest gap or CP1 decision'), ('c', 'c licensing / terms / access')):
    w('| %s | %d | %d |' % (lab, tot(c), cnt[(c, 'H')]))
w('| Total | %d | %d |' % (N, totp('H')))
w('')
w('Priority totals: H %d, M %d, L %d.' % (totp('H'), totp('M'), totp('L')))
w('')
w('Class by priority: ' + '; '.join('%s: H %d, M %d, L %d' % (c, cnt[(c, 'H')], cnt[(c, 'M')], cnt[(c, 'L')]) for c in 'abc') + '.')
w('')
w('Class b split: honest gap %d (%s); CP1 decision %d (%s); needs testing proper 0 (no run is possible: access is by onboarding and R019 bars API calls, sign-in and form submission, so every needs-testing item is an honest gap or waits for a user-approved run).' % (len(gaps), ', '.join(gaps), len(cp1), ', '.join(cp1)))
w('')
w('Class c items: %s. Items touching each source file (an item can touch several): litmus_eval_tooling.md %d; litmus_inventory.md %d; brief / queue / rulings %d.' % (', '.join(cl_c), fcount['E'], fcount['I'], fcount['B']))
w('')
w('Dedup note: the same absence appears in several places and is merged into one id with every location: the judge and backing model (Overview, six Tools rows, Engine, Open questions) is %s; dataset size, provenance, licence and languages (Datasets 16 rows, Reuse, Open questions) is %s; the host conflict C6 (portal, playbook, Getting Started link, sample Action; EV four bullets, INV two rows) is split into %s (which host is current) and %s (wording: three hosts in four sources); the Onboarding Guide and the three 403 pages are split into %s (HTTP facts and labels, answerable) and %s (guide identity, honest gap); eligibility (EV Open question, INV Needs cell, Overview Summary) is %s with the label mismatch in %s.' % (ids['judge'], ids['size'], ids['host_cur'], ids['host_count'], ids['p403'], ids['onboard_guide'], ids['elig'], ids['label_mismatch']))
w('')
w('Provenance note: EV and INV state that every number and quote came from raw page text (`fetch_text.py`, plain curl, raw GitHub files at pinned SHAs, urllib for link anchors, pdftotext for the one-pager), and that no fact comes from a summarising fetch; no item is classed as depending on one. Facts that depend on something not read or not re-readable here: the three unreachable 403 pages ({p403}, {onboard_guide}), the interest form and the web app and API hosts (not visited, R019), the link anchors ({anchors}), the one-pager through a downloaded copy ({onepager}), the Kaleidoscope repository ({q_b}), the Moonshot data repository ({cookbooks}), and the Wayback CDX index for the Sentinel path ({wayback}).'.replace('{p403}', ids['p403']).replace('{onboard_guide}', ids['onboard_guide']).replace('{anchors}', ids['anchors']).replace('{onepager}', ids['onepager']).replace('{q_b}', ids['q_b']).replace('{cookbooks}', ids['cookbooks']).replace('{wayback}', ids['wayback']))
w('')
w('Raw label census (whole-file bracket occurrences, including Reviewer notes): EV: [Documented] 55, repo-labelled [Documented: repo ...] 29, [Inferred] 19, [To be verified] 11, [Not disclosed] 55. INV: [Documented] 69, repo-labelled 23, [Inferred] 7, [To be verified] 7, [Not disclosed] 24. Every label bracket is one of the allowed forms; every EV Detail bullet carries exactly one label (0 multi-label bullets by regex).')
w('')
w('Groups (id ranges): ' + grp_txt + '.')
w('')
w('## Already ruled (not reopened here)')
w('')
w('| Matter | Ruling | Effect on triage |')
w('|---|---|---|')
w('| Litmus has an evaluation-tooling sheet only and no Table 3 columns; eval sheet pre-approved | R003 | No columns, no column ids, no `check_drafts.py columns` run; the eval Tools "Evaluates" cell may only name a Table 3 header as a possible reuse |')
w('| Inventory rows are not Table 3 functions | R011, queue (purplellama P1 Q1: "same for Litmus") | Checked: all 15 Covered-by cells use `— (inventory only, not in Table 3)`; no item |')
w('| Moonshot link is [Inferred] with its premise; the engine stays [Not disclosed] | queue q02 | Not reopened; {moonshot} only asks for a residual check and a label fix |'.replace('{moonshot}', ids['moonshot']))
w('| Three aiguardian pages return 403: retry, else "checked, not reachable" | queue q03 | Done at P1; {p403} and {wayback} only tidy labels and scope'.replace('{p403}', ids['p403']).replace('{wayback}', ids['wayback']) + ' |')
w('| Inventory panel and Covered-by logic must accept all-inventory-only rows | queue (litmus P1 Q-C) | P8 writer note only; no item |')
w('| Sheet letters assigned at P8; name at most 31 characters | R003, lessons 15 | Names `3x. Litmus Inventory` (20) and `3x. Litmus Eval Tooling` (23) are within the limit; Cloak is drafted in parallel, so the letters may shift; no item |')
w('| Research is read-only; needs-testing items stay open | R019 | No local-run consent item; all class b items wait for a user-approved run or a vendor reply |')
w('| Bench content is proposed, not decided; main does not put bench-design choices to the user | R032 | No bench-design question in the CP1 list; {r032} only audits the wording |'.replace('{r032}', ids['r032']))
w('| Absences are [Not disclosed] with what was checked; scope statements from module lists are [Inferred]; archived copies count as [Documented] with the date | R020, R015, R007 items 2 and 5 | Basis for the label items (T-ids in the hygiene table) |')
w('| Playbook pin is staging at 45908b48 (deployed site built from staging) | R007 item 7 (Sentinel precedent) | Pin accepted; {locators} only standardises line locators'.replace('{locators}', ids['locators']) + ' |')
w('| Raw GitHub fallback for pinned vendor files | R020, R013 | The playbook and Moonshot reads via raw.githubusercontent.com are within R020 |')
w('')
w('## Items for CP1 (decision-bearing for the user)')
w('')
w('Defaults are the triager\'s recommendations and match the brief where the brief drafted one. Nothing is decided here. Per R032 no bench-design choice is put to the user: how a bench might use the 14-test list, the playbook taxonomy, the endpoint-plus-key contract or sensitive test content stays a suggestion in the Reuse section.')
w('')
w('### Q-A Separate inventory sheet for Litmus (%s)' % ids['q_a'])
w('')
w('- Options: (a) drafted, default: a small `3x. Litmus Inventory` with 15 rows in three blocks, every Covered-by cell `— (inventory only, not in Table 3)`, the eval sheet right after it (R003 order); (b) no inventory sheet: the Tools and Datasets tables already hold the access paths and suites, and the six integration parameters become a second table in the Tools section or notes (the README section 6 parser accepts several tables per section; the P8 writer confirms how the builder renders two).')
w('- Evidence the choice turns on:')
w('  - R003 says "each new product gets one" and lists inventory sheets as pre-approved, so (a) needs no new-sheet ruling; the user chooses only whether to use it.')
w('  - Overlap, counted row by row: 9 of the 15 rows restate eval content in other columns: INV(a) web app, API and CI/CD (EV Tools rows 1 to 3), INV(a) onboarding (EV Overview bullets 17 and 18), INV(b) Baseline and Baseline+ (EV Datasets suite rows 51 and 52), wog-baseline-v1 (Tools row 5), custom scenarios (Tools row 4), Kaleidoscope (Tools row 6). The 6 rows of block (c) have no eval-sheet row.')
w('  - What only the inventory holds: the parameter-by-parameter table (Required "Yes" and Default "-" for all six, the example workflow differences, the sample Action input names `litmus_key` and `cookbpooks`), the identifier column (`aiguardian-baseline-tests`, `wog-baseline-v1`, `type cookbook`), and the per-path host cells. Conflicts C2, C3 and C6 are written in both files, so the merger and verifier must keep them in step (%s, %s, %s).' % (ids['action'], ids['params'], ids['host_cur']))
w('  - Cost of (a): a config module `build_litmus_inventory.py` (BLOCKS 4/5/6, `markers` with the inventory-only marker, a panel with no Table 3 count; queue Q-C), one more sheet of 15 thin rows, and duplicated facts. Cost of (b): the parameter table and the host and Action conflicts lose a tabular home, and Litmus becomes the only product without an inventory sheet.')
w('  - Sheet letters: Cloak is drafted in parallel and is listed before Litmus, so it probably takes the next letter first; (a) then needs two letters (inventory, then eval) and (b) one; main assigns them at P8.')
w('- Recommended default: (a), as drafted. It is consistent with the other products, needs no extra ruling, and block (c) has no other home. Choose (b) only if the user prefers fewer sheets; then {params}, {action} and {host_cur} are re-homed in the Tools and Engine sections, no Summary changes.'.replace('{params}', ids['params']).replace('{action}', ids['action']).replace('{host_cur}', ids['host_cur']))
w('')
w('### Q-B Kaleidoscope scope (%s)' % ids['q_b'])
w('')
w('- Options: (a) drafted, default: one Tools row, mentions in Overview, the Datasets note and INV(b), no repository research; (b) treat Kaleidoscope as its own evaluation-tool subject (its own evaluation-tooling rows or sheet; research of `govtech-responsibleai/kaleidoscope` at a pin, the arXiv 2607.14673 paper and the docs site); (c) middle path, not drafted: keep it inside the Litmus eval sheet but add a few Tools rows read from the pinned playbook file only, with no new sheet.')
w('- Evidence the choice turns on:')
w('  - The playbook says "Kaleidoscope is a contextual, functional evaluation module within Litmus" and, on its own page, "Try the open-sourced Kaleidoscope module today, or stay tuned for more updates to access it via Litmus"; the Kaleidoscope docs say Litmus is being extended "in the upcoming months" ({kal_status}: present tense on one page, future on two).'.replace('{kal_status}', ids['kal_status']))
w('  - It measures whether an application "performs well for its intended users, tasks, and context" (rubrics, persona-driven test sets, LLM judges calibrated to human labels): functional quality, not safety or guardrail behaviour, which is what the test bench is scoped around.')
w('  - R003 and CLAUDE.md pre-approve evaluation sheets only for Litmus and CyberSecEval; a Kaleidoscope sheet needs a user ruling. Its licence, code and paper are unread ({kal_lic}); the drafts read the playbook page, the docs home and the arXiv abstract only.'.replace('{kal_lic}', ids['kal_lic']))
w('  - No Summary line mentions Kaleidoscope, so the choice changes no Summary.')
w('- Recommended default: (a). If the user wants Kaleidoscope covered in depth, a separate product slug (own P0 to P10 pass and its own sheet ruling) keeps the Litmus sheet about Litmus; option (c) is the fallback that needs no new sheet.')
w('')
w('### Also for CP1 or CP2: class c and access judgements (record, decide later)')
w('')
w('- %s eligibility and %s terms: default record the playbook, portal and one-pager statements as written, keep "no explicit eligibility rule" and "no terms, pricing or data-handling statement" as [Not disclosed] with the pages named, and do not infer. Whether to request onboarding is the user\'s own decision outside research (R019); no run is proposed here.' % (ids['elig'], ids['terms']))
w('- %s and %s: default record only (GovTech material quoted under 40 words; the Moonshot and Kaleidoscope repository licences are listed with their owners\' pages if kept). No bench blocker is evident.' % (ids['reuse_terms'], ids['ms_lic']))
w('')
w('### Not put to the user (R032 and routing rules)')
w('')
w('- Whether and how a bench reuses the 14-test list, the WOG taxonomy, the endpoint-plus-key record shape, the benign-versus-malicious pairing idea or the sensitive-content handling: suggestions in EV Reuse (EV:117-126), not decisions.')
w('- Everything doc-answerable (class a) goes to a P5 resolver; every honest gap stays open in R8-style Open questions with what was checked.')
w('')
w('## Triage table')
w('')
w('| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |')
w('|---|---|---|---|---|---|')
for it in ITEMS:
    w('| %s | %s | %s | %s | %s | %s |' % (it['id'], res(it['text']), res(it['loc']), CLS[it['cls']], res(it['src']), it['prio']))
w('')

# ---------- label hygiene
w('## Label hygiene')
w('')
w('Scope: the two drafts against `drafts/README.md` section 3 (labels), section 4 rule 5 (one fact per label), section 5 (inventory cells) and section 6 (eval Open questions). Mechanical scan: every bracket in EV and INV is an allowed form; no `[Not found]`-style invented forms; every EV Detail bullet has exactly one label; the only look-alike brackets are the four category prefixes in the Datasets table (below). A scan of double-quoted spans finds no quote of 30 words or more.')
w('')
w('| Issue | Where | Proposed fix | T-id |')
w('|---|---|---|---|')
H = [
 ('Open questions carry [Inferred] (README section 6 allows [To be verified] or [Not disclosed] there); the HTTP 403 facts are [Documented] by README section 3 rule 7', 'EV:146, EV:147', 'Move the HTTP facts to Detail as [Documented]; keep one [Inferred] conclusion with its premise', 'p403, onboard_guide'),
 ('Same fact, different labels across files: `aiguardian-baseline-tests` selects the 6-test suite (EV documented, INV [Inferred]); six Baseline tests are all in Baseline+ (EV Used by column documented, INV [Inferred]); eligibility (INV [Documented: repo ...], EV [Not disclosed])', 'EV:51, EV:53-66; INV:24, INV:25, INV:16; EV:139', 'One label and one basis per fact; [Inferred] with the Getting Started sentence as premise', 'label_mismatch, elig'),
 ('Kaleidoscope availability asked as TBV in INV and as ND in EV (different questions, one topic)', 'INV:28; EV:144', 'One question, one label; keep the three quotes as separate bullets', 'kal_status'),
 ('Open question asks about vendor internals under [To be verified] (Moonshot compatibility; Domestic Affairs pass rule)', 'EV:130, EV:143', '[Not disclosed] if no public source can verify; keep TBV only for a future run', 'moonshot, domestic'),
 ('Inference worded as a documented fact: "typo" and "copy error" for the Baseline+ introduction (C5)', 'EV:47; INV:25', 'State the page text plainly or label the reading [Inferred]', 'wording_defects'),
 ('Absence inside a documented bullet: "how they work is not described" under [Documented]', 'EV:89; INV:27', 'Split: quote [Documented], absence [Not disclosed] with what was checked', 'rt_label'),
 ('One bullet, several facts or sources, one label', 'EV:20, EV:26, EV:28, EV:29', 'One fact per bullet', 'ov_bullets, ov_naig'),
 ('Whole-row label does not match the part it qualifies (refusal-score example: code is documented, real output is unverified)', 'EV:77, EV:42', 'Split the Label cell', 'refusal_label'),
 ('Paraphrase labelled [Documented: repo ...] ("kept only when reliable")', 'EV:43', 'Short verbatim quote or [Inferred]', 'kal_wording'),
 ('Summary entailment: "over HTTP" has no supporting bullet; "not a guardrail" lead rests on a quote plus an [Inferred] direction note', 'EV:94, EV:6, EV:16', 'Add the [Inferred] bullet or reword to the quote', 'over_http, sum_lead'),
 ('Absence claim without a named method (org search); one fact stated by two methods (HTTP 404 versus ls-remote)', 'EV:29, EV:110; INV:15', 'Name the method and date; one method per fact', 'repo_search, gh404'),
 ('Link-target facts labelled [Documented] although the text was not visible on the page (read from anchors)', 'EV:39, EV:111-113; INV:13-16, INV:36', 'Re-read and record the method, or relabel [To be verified]', 'anchors'),
 ('Label-lookalike category prefixes "[Security]", "[Specialised Advice]", "[Undesirable Content]", "[Political Content]"', 'EV:53-66', 'Use "Security:" or "(Security)"', 'brackets'),
 ('Same source cited with a repo label in one cell and plain [Documented] in the next (playbook Kaleidoscope page versus Litmus page)', 'INV:28', 'Pin the Kaleidoscope page to the same commit after matching passages', 'urls_unpinned'),
 ('Wayback scope over-stated ("no snapshot found" for three pages; one was not fully checked)', 'EV:146', 'Narrow to the availability API or retry the CDX query', 'wayback'),
 ('Process language and ruling ids in parsed text ("R002", "this draft", "R019", "R003", "R032")', 'EV:16, EV:18, EV:34; INV:9', 'Product-neutral wording', 'process_lang, r032'),
 ('Short names without a legend inside the parsed cells (DOCS or AIG, PORTAL or DEV, PB, ACT, MS); two name sets for the same sources', 'EV:3 and cells; INV:5 and cells', 'Spell out or move the legend into a parsed note; one name set', 'shortnames'),
 ('Reviewer notes sections must leave the finals', 'EV:149-158; INV:43-50', 'Move to `litmus_changes.md`', 'rn_move'),
]
for iss, wh, fx, ks in H:
    w('| %s | %s | %s | %s |' % (iss, wh, fx, ', '.join(ids[k] for k in ks.split(', '))))
w('')
w('Covered-by check: every "Covered by Table 3 column" cell in INV(a), (b) and (c) (15 cells) equals the marker `— (inventory only, not in Table 3)`; the checker confirms it (0 errors, 0 warnings); no Table 3 header appears in any Covered-by cell. The EV Tools "Evaluates" cells name the two Sentinel headers exactly as in `sentinel_two_level.md` (SN1 and SN2); both exist in the workbook. The INV config for P8 needs the inventory-only marker in `markers` (R011).')
w('')

# ---------- style
w('## Style issues in columns')
w('')
w('Litmus has no Table 3 columns; this section covers the eval and inventory drafts.')
w('')
st = [
 'Summaries (checker rules, README section 4 by analogy): Overview 44 words before the label and 45 with it; Red-teaming 36 and 38; Engine coverage 44 and 46 (the label "Not disclosed" is two words). The README limit is 45 before the label, so all three pass; lesson 18 (the workbook build counts the label) and the brief\'s "aim for 44" make the Engine Summary the one to trim by two words (%s). `**` is balanced (4 per Summary); no backticks, underscores or `$`; every Summary begins with a bold lead.' % ids['over_http'],
 'Tools "Evaluates (Table 3 columns)" cells: row 1 holds a paragraph (518 characters) with the two Sentinel headers inside prose; README section 6 wants exact sheet 3 headers or plain function names. All six rows say "No Table 3 column", which is correct under R003 but repeats (%s).' % ids['map_sent'],
 'Repeated cell text: "Judge needed" and Engine cells read "Not disclosed [Not disclosed]" or "[Not disclosed]" in six rows; one note under the table would do (%s).' % ids['judge'],
 'Cell and bullet length: the longest cells are 560 characters in EV (Tools row 3, Inputs cell) and 719 in INV (the endpoint row); INV(a) and (b) cells run 600 to 660 characters with three to six labelled facts each. Within the README rules (a cell may hold several facts, each with its label), but dense on screen. No wrapped bullets.',
 'Section sizes against the brief: Engine coverage 19 bullets (target about 8), Open questions 19 (about 12), Red-teaming 7 (about 5), Reuse 10 (about 8) (%s).' % ids['overlong'],
 'Process language in parsed text: "(R002)" and "in this draft" (EV:16), "(R019)" (EV:18), "(R003)" (EV:34), "(a proposal, R032)" (INV:9) (%s, %s). First-person or session wording ("Written at P1", "P1 check") appears only in the brief, not in the drafts.' % (ids['process_lang'], ids['r032']),
 'Short names and legends: see %s. The INV legend paragraph is long (about 1,300 characters) and sits outside the parsed intro.' % ids['shortnames'],
 'Locator formats differ: EV "(PB tools/litmus.md line 46)", "(ACT line 28 and lines 31 to 45)", "(action.yml line 28)"; INV "(lines 427 to 440)", "(AIG Getting Started)"; no `file@ref:line` form (%s).' % ids['locators'],
 'Spelling: British throughout (no US forms found by scan: licence, organisation, analyse, behaviour, customise); vendor spellings kept in quotes ("cookbpooks (sic)", "Gitlab", "analyse"); product names as the vendor writes them (DoAnythingNow, TechPass, AI Guardian).',
 'Quotes: all under 40 words; curly apostrophes in verbatim page text ("tenant\'s") are kept as the page prints them; ASCII elsewhere.',
 'URL cells: INV source cells separate several URLs with " ; " as the grammar requires; EV Source cells mix short names (DOCS, PORTAL) with full URLs, so some rows show an abbreviation only (%s).' % ids['shortnames'],
 'Direction wording (R002): no Litmus function is headed Input-level or Output-level; the direction note is a single Overview bullet (EV:16). Compliant.',
 'Bench wording (R032): compliant (%s).' % ids['r032'],
]
for i, s in enumerate(st, 1):
    w('%d. %s' % (i, s))
w('')

# ---------- contradictions
w('## Contradictions')
w('')
w('Source conflicts and cross-file inconsistencies, each with the ids that resolve them. "Both written" means the drafts already carry two labelled statements (README section 3 rule 4). C1 to C11 are the brief\'s list; C12 onward were found in triage.')
w('')
C = [
 ('C1 taxonomy', 'docs test page (Security, Specialised Advice, Undesirable Content, Political Content; 14 tests) versus portal How it works (four categories: Security, Undesirability, Specialised Advice, Political) versus one-pager ("toxicity, bias, misinformation, robustness")', 'INV(b) row 1 (all three); EV body has the docs taxonomy only, the other two sit in Open question 145 (not both written in EV)', 'taxonomy1'),
 ('C2 Action reference', 'docs step `dsaidgovsg/aiguardian-litmus-test@<version>` (repo not found) with `base_url`, `run_name`, `endpoint`, `num_of_prompts`, `api_key` versus the archived sample with `run_name`, `litmus_key`, `endpoint`, `cookbpooks` and a development host', 'Both written in EV Tools row 3 and INV(a) row 3', 'action, gh404'),
 ('C3 parameters', 'table: `test_suites` and `num_of_prompts` required, default "-" versus example: no `test_suites`, `num_of_prompts` default `1`; sample Action: `run_name` required with a default', 'Both written in INV(c); EV Tools row 3 carries one side and Open question 136', 'params'),
 ('C4 maturity', 'portal "PROOF OF CONCEPT" (page 19 May 2025) versus docs, one-pager and playbook describing an onboarding service with no label', 'Both written (EV:19, EV:20; INV(a) row 1); not in the Overview Summary', 'sum_status'),
 ('C5 typo', 'Baseline+ introduction says "Baseline Tests consists of all 14 tests"; heading and table say Baseline+ with 14', 'Both written (EV:47, INV(b) row 2); "typo" is an inference', 'wording_defects, counts'),
 ('C6 hosts', 'portal login -> staging host; playbook and `base_url` link -> production host; sample Action -> development host (three hosts, four sources)', 'Both or all written (EV:111-114; INV(a) rows 1 and 2)', 'host_cur, host_count, anchors'),
 ('C7 suite identifier', '`aiguardian-baseline-tests` (Getting Started) versus `wog-baseline-v1` (playbook example) versus `type` `cookbook` with the `cookbpooks` input (sample Action); Baseline+ has no identifier', 'Written (EV Datasets suite rows, Tools row 5; INV(b) rows 1 to 3)', 'client, label_mismatch'),
 ('C8 result shape', 'pass/fail per test case and pass/fail dashboards (Getting Started, one-pager) versus "category-level refusal scores" and `refusal_rate` (playbook example)', 'Written (EV Tools row 5, Published results rows 1 and 4; INV(b) row 3)', 'passrule, refusal_label'),
 ('C9 NAIG wording', 'docs Overview names NAIG, docs home does not', 'Both quotes in one bullet (EV:26)', 'ov_naig'),
 ('C10 generic testing wording', 'portal "UI glitches, and bugs", "user simulation", Troubleshooting "devices, browsers" versus docs describing prompt testing only', 'Open question 142 and INV(b) row 4; no body bullet gives the portal quote on its own', 'custom'),
 ('C11 test subject', 'test page says "model" for some tests, "application" for others; Overview says the application forwards prompts to the LLM', 'Both written (EV:99; INV(c) endpoint row)', 'model_vs_app'),
 ('C12 Kaleidoscope status (new)', 'playbook Litmus page "the contextual evaluation module within Litmus" versus Kaleidoscope page "stay tuned ... to access it via Litmus" and docs home "extending Litmus ... in the upcoming months"', 'All three quotes written (EV:24, EV:25; INV(b) row 5); the conflict is not named and the two files ask different questions', 'kal_status'),
 ('C13 Domestic Affairs pass rule (new)', 'description "refuses to answer" versus Outcome "maintains a neutral stance"', 'Both in one cell (EV:64) and in Open question 143; INV does not list the 14 tests', 'domestic'),
 ('C14 "refusal-based" versus pass conditions (new)', 'playbook: safety tests are "refusal-based" and a system that refuses everything may score well; docs test page: Medical, Financial, Legal, Geopolitics and Social Policies pass only with substantive, limited or balanced answers', 'Each side is quoted in a different section; never set side by side', 'refusal_based'),
 ('C15 eligibility wording (new)', 'playbook "available to public sector teams"; portal "WOG application developers"; one-pager invites collaboration ("Pilot with your AI applications"); INV(a) Needs cell states a public-sector requirement, EV Open question says no rule is stated', 'Both sides partly written; the two files disagree on the label', 'elig, label_mismatch'),
 ('C16 Wayback scope (new)', 'EV:146 "no Wayback snapshot found" for three pages versus brief "CDX query for the Sentinel path could not be completed"; INV:16 says only the availability API returned none', 'EV over-states; INV matches the evidence', 'wayback'),
 ('C17 method for one fact (new)', 'documented Action repository "HTTP 404 on github.com" (INV:15) versus "Repository not found" on `git ls-remote` (EV:29, EV:40, brief)', 'Same fact, two methods, two files', 'gh404'),
 ('C18 CI/CD platform (new)', 'step headed "Push Changes to GitHub/Gitlab" versus only a GitHub Actions workflow shown', 'INV(a) row 3 notes both; EV Tools row 3 does not', 'action'),
 ('C19 locator conflict (new)', '`LitmusClient` example at safety.mdx lines 432-437 and 440 (EV), 432-440 (brief), 427-440 (INV); litmus.md "line 46" cited for three different quotes', 'Cross-file inconsistency', 'locators'),
 ('C20 two API keys under one name (new)', 'Getting Started `api_key` row: key "provided by the AIGuardian team during onboarding" versus step 2: "API key for authentication" for the tenant application and an `x-api-key` header in its example body', 'INV(c) endpoint and api_key rows note the application key; EV Engine bullet gives the header without saying whose key', 'models'),
 ('C21 Summary versus Detail (new)', 'Engine Summary "over HTTP" and Overview lead "not a guardrail" are not backed by a Detail bullet or rest on an [Inferred] note', 'EV:94, EV:6', 'over_http, sum_lead'),
]
for i, (nm, sides, where, ks) in enumerate(C, 1):
    w('%d. **%s.** %s. Where written: %s. Resolves: %s.' % (i, nm, sides, where, ', '.join(ids[k] for k in ks.split(', '))))
w('')
w('## Questions routed to main (not the user)')
w('')
w('1. Browser User-Agent reads and the Hub listing GET (%s, %s): is a spoofed browser User-Agent for GET reads of public pages and the one-pager PDF acceptable under hard rule 5, R019 and R021, and is the `huggingface.co/api/datasets` listing covered by the P4 Hub-metadata ruling? Default: accept as GET-only public reads, record in the change log, do not repeat.' % (ids['procslip'], ids['onepager']))
w('2. Residual public-page checks for the P5 resolver (%s, %s, %s, %s): a read-only look at a PyPI project page for a GovTech `litmus` package, the Moonshot and AI Verify Foundation pages for "Litmus", and the Sentinel getting-started and playbook Sentinel pages for a guarded-endpoint statement. Default: allowed (no install, no run; R019 bars installs and API calls only).' % (ids['client'], ids['moonshot'], ids['cookbooks'], ids['guardrailed']))
w('3. Summary text (%s, %s, %s, %s): the resolver proposes exact new Summary text with word counts; main decides whether the Overview Summary carries a maturity or eligibility qualifier. Default: keep the three Summaries within 44 words excluding the label and add a qualifier only if a word-neutral rewrite exists.' % (ids['sum_lead'], ids['sum_status'], ids['elig'], ids['over_http']))
open(OUT, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
json.dump({'N': N, 'cnt': {'%s%s' % k: v for k, v in cnt.items()}, 'H': [(it['id'], it['key']) for it in Hs]}, open('benchtest/scratchpad/triager/litmus/counts.json', 'w'))
print(N, dict(cnt), len(Hs))
