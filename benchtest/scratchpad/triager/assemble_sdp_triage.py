#!/usr/bin/env python
import json, re
T = '/home/user/guardrail_research/benchtest/scratchpad/triager/'
rows = open(T + 'sdp_rows.md', encoding='utf-8').read().rstrip('\n')
c = json.load(open(T + 'sdp_counts.json'))
K = c['keys']
cp = c['cp']
def g(k): return cp.get(k, 0)
def t(key): return K[key]

# per-file touch counts from location strings
A = B = I = 0
for r in rows.splitlines():
    loc = r.split(' | ')[2]
    A += ('A SD' in loc) or loc.startswith('A ') or ('A and B' in loc)
    B += ('B SD' in loc) or ('A and B' in loc)
    I += ('INV' in loc)

head = f"""# Sensitive Data Protection (SDP) triage of open evidence items (DRAFT)

Sources triaged: `sdp_cols_a.md` (SD1 to SD3), `sdp_cols_b.md` (SD4 to SD6), `sdp_inventory.md` (blocks (a) method catalogue, (b) infoType groups, (c) transformations, (d) access paths, (e) limits and pricing, (f) regions), the brief `sdp_brief.md` (scope, format rules, conflicts C1 to C5, gaps G1 to G14, open questions Q01 to Q03), the explorer notes `scratchpad/explorer/20261009_sdp_p0.md` with `_q01.md` to `_q03.md`, rulings R002, R007, R009, R011, R012, R013, R014, and the inventory `## Reviewer notes`. No research done; source suggestions only. Nothing here is verified. Date of triage: 2026-10-09 (P4).

Important input gap: `sdp_cols_a.md` and `sdp_cols_b.md` contain no `## Reviewer notes` section (the P2 drafters' QUESTIONS blocks and notes were lost with the previous session). Uncertainties for the columns were harvested from the R8 bullets, the explicit labels and the conflict statements written inside Detail bullets. The inventory's Reviewer notes are intact and fully used.

## Legend
- File short names: A = sdp_cols_a.md, B = sdp_cols_b.md, INV = sdp_inventory.md, BR = sdp_brief.md, P0 = the explorer P0 note.
- Location notation: `SDn Rk` = column SDn, row Rk (Summary or Detail bullet named in brackets); `R8 #m` = the m-th R8 bullet of that column; `R8 Summary` = the R8 Summary line. `INV(a)` to `INV(f)` = inventory block, with the row named; `INV-RN` = the inventory Reviewer notes (headings: Row counts, Covered-by decisions, Conflicts 1 to 8, Counts, Uncertain bullets 1 to 9).
- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; R8 = unlabelled R8 bullet; SUM = a Summary line.
- Class: a = doc-answerable (an official SDP, Google Cloud or pinned `googleapis/google-cloud-python@google-cloud-dlp-v3.40.0` source, or a drafting fix that needs no research); b = needs testing or a closed-vendor answer (stays open; "honest gap" = Google internals or quality figures that no public document is expected to give); c = licensing or terms; D = CP1 decision (user or main), not a doc question, so counted separately from a, b and c.
- Priority: H = affects a Summary line (including R8 Summaries) or a headline number; M = Detail level; L = cosmetic or low impact.
- Group tag in front of each item: CP1 = decision for CP1; CPOL = content policy; SUM = Summary versus facts; LIM = limits, pricing, SLA; GAP = honest gaps; SG = Singapore-specific; LIST = infoType list, defaults, versions; CUST = custom detectors (SD2); DEID = de-identification (SD3); TOK = tokenisation (SD4); IMG = images (SD5, SD6); INV = inventory hygiene and rows; TERMS = terms; PROC = format and process.
- Source short names: DOCS = docs.cloud.google.com/sensitive-data-protection/docs; LIM = DOCS limits page; PRC = pricing page; SLA = SLA page; REST = DOCS reference/rest/v2 pages; LIB = `googleapis/google-cloud-python@google-cloud-dlp-v3.40.0` (packages/google-cloud-dlp); "not SDP docs" = Model Armor, Gemini Enterprise, Cloud KMS, Apigee or Data Fusion pages.

## Counts

Total {c['total']} deduplicated items (T1 to T{c['total']}), drawn from 69 R8 bullets (A 32: SD1 13, SD2 9, SD3 10; B 37: SD4 11, SD5 13, SD6 13), the explicit labels in the three files (ND: A 11, B 21, INV 22 table cells; TBV: A 6, B 0, INV 12; INF: A 43 and B 48 Detail bullets and INV 69 cells, of which only those resting on an unchecked premise are items), the inventory Reviewer notes (8 conflicts, 9 uncertain bullets, counts), the brief (C1 to C5, G1 to G14, Q01 to Q03) and cross-draft comparison.

| Class | Count | of which H |
|---|---|---|
| a doc-answerable (incl. drafting fixes) | {c['cls']['a']} | {g('aH')} |
| b needs testing or access | {c['cls']['b']} (honest gaps among them: GAP and SG items, T-ids {t('acc_text')} to {t('emul')}, {t('fin')} to {t('doctype')}, {t('localnorms')}) | {g('bH')} |
| c licensing / terms | {c['cls']['c']} ({t('benchterms')} is "suggested", not in the drafts) | {g('cH')} |
| D CP1 decision (not a, b or c) | {c['cls']['D']} | {g('DH')} |
| Total | {c['total']} | {c['prio']['H']} |

Priority totals: H {c['prio']['H']}, M {c['prio']['M']}, L {c['prio']['L']}. Class by priority: a H {g('aH')} / M {g('aM')} / L {g('aL')}; b H {g('bH')} / M {g('bM')} / L {g('bL')}; c M {g('cM')} / L {g('cL')}; D H {g('DH')} / M {g('DM')} / L {g('DL')}.

Items touching each source file (an item can touch several; counted from the location strings): sdp_cols_a.md about {A}, sdp_cols_b.md about {B}, sdp_inventory.md about {I}, brief or explorer only 3 or fewer.

Why H is large ({c['prio']['H']} of {c['total']}): every item named in an R8 Summary line counts as H by definition, and each R8 Summary lists four to eight open questions. 27 of the 46 are class b honest gaps or tests that stay open by design (accuracy, latency, backing models, language, Singapore forms, behaviour at limits); the 16 class a H items are the ones that can close before CP2 without a test.

Dedup note: the same question appears in up to six columns and is merged into one id with all locations: accuracy and recall ({t('acc_text')}, {t('acc_deid')}, {t('acc_img')}, {t('acc_safe')} by function), latency ({t('latency')}), backing models ({t('models')}), customer-data terms ({t('custdata')}), content-policy evaluation ({t('applyop')}, {t('cptest')}), default infoTypes ({t('defa')}, {t('defb')}), no emulator ({t('emul')}), 3,000-finding cap ({t('cap3000')}), conversation items ({t('convctx')}). Where one question has both a "do documents say it" half and a "does it hold live" half they are split into a and b ids ({t('defa')} / {t('defb')}, {t('pnamea')} / {t('pnameb')}, {t('fmt_a')} / {t('fmt_b')}, {t('ruleorder_a')} / {t('ruleorder_b')}, {t('sd4sum')} / {t('sd4len')}, {t('sd3sum')} / {t('sd3test')}). Conflicts whose both sides are already quoted verbatim in the drafts go to b (test), with the drafting action in the a item.

Provenance note: BR says every page was read as raw text with `fetch_text.py` and INV-RN states "Facts from summarising fetches: none" (85 phrases re-matched, 0 misses). A and B have no Reviewer notes, so for them it is unrecorded; see {t('rnmissing')}. Items that depend on something not re-read: the 3.40.0 line numbers in B ({t('citefmt')}), the limits page (empty body from the cloud.google.com copy, {t('limsum')}), `python_requires` at setup.py line 95 (BR's P1 grep found none; the drafts found it, {t('pylibdoc')}).

Mechanical status at triage time (re-run, not trusted from the hand-over): `check_drafts.py columns` gives 0 errors and 0 warnings for both column files (6 columns, headers identical to BR); `check_drafts.py inventory sdp_inventory.md --headers` over A plus B gives 0 errors (tables 15/24/12/13/16/7 rows). The 42 Summaries are all within limits. SD5 R3 Summary is now 44 words (it was 46; fixed by the parallel drafter).

## CP1 decision items (for the user and main)

| Item | Decision needed | Default in drafts | Who |
|---|---|---|---|
| {t('prefix')} | Header prefix: `Sensitive Data Protection:` or `Google Cloud Sensitive Data Protection:` | first form | user |
| {t('sd7')} | Content policy (SD7): Table 3 column or inventory only; evidence in {t('applyop')} and {t('cptest')} | inventory only, R011 marker | user |
| {t('fold')} | Fold SD2 into SD1 and SD4 into SD3 (decide once with Presidio PD3/PD6 and Model Armor) | six columns, SD2 and SD4 kept | user |
| {t('imgsplit')} | Split SD5 into inspect and redact; keep SD6 separate | one SD5, SD6 separate | user |
| {t('custdata')}, {t('benchterms')} | Licensing and terms: may Google Cloud terms pages be read as sources; are explicit or violent test images and real PII acceptable test data | not read | user |
| {t('mamarker')}, {t('extsrc')}, {t('oop')} | Marker for wrapped-path rows; acceptance of Apigee, Data Fusion and demo pages; one label pattern for the out-of-purpose statement | as drafted | main (ruling) |

## Triage table

| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |
|---|---|---|---|---|---|
"""

hyg = f"""
## Label hygiene

Scope: sdp_cols_a.md and sdp_cols_b.md (42 Summaries, 848 Detail bullets of which 215 are unlabelled R8 (69) or R9 (146) bullets) and sdp_inventory.md (6 tables, 87 rows, 445 bracket pairs). Allowed forms (README section 3): [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed].

Standard forms in use (no change needed):
- Columns, R1 to R7 Detail bullets: [Documented] 447 plain plus 57 [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (A 25: SD1 15, SD2 3, SD3 7; B 32: SD4 17, SD5 10, SD6 5), [Inferred] 91 (A 43, B 48), [Not disclosed] 32 (A 11, B 21), [To be verified] 6 (all in A: SD1 R2 four, SD2 R6 one, SD3 R4 one). All repo labels are one repo with the same tag, and every column that uses one lists a blob URL with that tag in R9 (checked per column). No R8 bullet carries a label; every R9 bullet is a bare URL.
- Summaries (R1 to R7): [Documented] 28, [Inferred] 14 (R3 and R7 in every column, plus SD3 R2 and SD6 R6), none [Not disclosed] or [To be verified]; R8 Summaries unlabelled; R9 Summaries plain. See SUM items below for Summaries whose label is stronger than their facts.
- Inventory: [Documented] 331 plain plus 10 repo labels (one repo, same tag), [Inferred] 69, [Not disclosed] 22, [To be verified] 12. By block (Documented / Inferred / ND / TBV): (a) 85 / 20 / 5 / 0, (b) 99 / 27 / 6 / 2, (c) 64 / 0 / 0 / 2, (d) 53 / 20 / 8 / 7, (e) 24 / 0 / 2 / 0, (f) 16 / 2 / 1 / 1 (repo labels counted in Documented).
- Docs facts carry plain "(SDP docs, <page>, read 2026-10-09)" hints and no pin, as BR requires; no `[Documented: develop/unreleased]` anywhere; every code quote is a single line; no quote reaches 40 words (scanned).

Non-standard bracket forms: one non-label pair in the inventory.

| Issue | Count / where | Proposed fix | T |
|---|---|---|---|
| Non-label bracket pair `[grpc]` in "google-api-core[grpc]" | 1: INV(d) Python client row (Notes) | Rewrite without brackets | {t('brackets')} |
| Self-referential label "[Documented] (this sheet)" | 1: INV(d) Model Armor advanced row | Drop the label (an internal pointer, not a source fact) | {t('brackets')} |
| Absence claims labelled [Documented] | 2 in INV(a) content policies row (resource page and client have no evaluation method); 1 borderline in A SD1 R4 (client bullet with "no evaluate method") | [Not disclosed] naming the pages and the client version; keep the repo label only for what the file contains | {t('absdoc')} |
| "Not read" labelled [Not disclosed] | 1: INV(d) Other client libraries row ("not read at a pinned ref") | [To be verified] or delete (BR: names only) | {t('otherlibs')} |
| Empty table cell read as "No" labelled [Documented] | 18 cells: INV(c) Reversible and Referential integrity columns | [Inferred] (premise: empty cell) or neutral wording | {t('emptycell')} |
| Same kind of statement, different labels across columns | out-of-purpose: INF x3, ND x3 (BR said Documented); docs-silent-and-test-needed: TBV in A (FIN, +65) versus ND in B (SD5 R2 Singapore passport detectors); "test your settings" quote: [Documented] in A SD2 R7 and SD3 R7, but [Not disclosed] (with the quote inside) in A SD1 R7; no-SLA-row: INF in B, ND in INV(e) | One pattern per kind: ND for vendor silence naming pages checked; TBV only for a checkable fact; a quote is its own [Documented] bullet | {t('oop')}, {t('slalabel')} |
| Inference or second fact inside a [Documented] bullet (README rule 5: separate [Inferred] bullet) | A SD1 R4 ("so the default set has changed before"), A SD2 R1 (surrogate detectors "belong to the reversible-tokenisation column", a scope decision), B SD4 R1 (header spelling remark after a quote), B SD4 R4 ("so it cannot support later reversal"), B SD6 R5 ("so the caller maps findings to a decision"), B SD6 R2 ("text-side analogues ... they classify text, not pixels") | Split, or drop the clause | {t('doctype')}, {t('noverdict')} |
| One bullet, two facts under one label | A SD1 R7 (absence of an evaluation toolkit plus a quoted recommendation, labelled [Not disclosed]) | Two bullets: [Not disclosed] absence; [Documented] quote | {t('oop')} |
| [Inferred] without a stated premise | B: 48 of 48 Detail bullets (premise only implicit in "so"/"because"); A: 10 of 43 (6 in SD1, 4 in SD3) | Add "(premise: ...)" as A mostly does | {t('premise')} |
| Counts the drafters made | 6 in columns, 27 cells in INV | Correct: [Inferred] with the counting rule stated; keep, and re-count at P7 | {t('counts')} |
| Summary label stronger than its facts | SD3 R1 and R4, SD4 R4, SD6 R2, R4, R5, SD2 R5, SD4 R5, SD5 R1 and R2 | Relabel the Summary or move the weaker sentence to R8 | {t('sd3sum')}, {t('sd4sum')}, {t('sd6sum')}, {t('noverdict')}, {t('faceprev')} |
| Wording "No other Singapore-named infoType exists" under [Not disclosed] | 1: A SD1 R2 | Say "none named in the reference" (an absence claim, not an existence claim) | {t('fin')} |
| Conflict labelled but one side missing from the inventory | INV(a) image row carries 3 of the 6 format statements; INV(c) AES-SIV row omits the length conflict | Carry all statements in both places (README rule 4) | {t('fmt_a')}, {t('sd4len')} |
| TBV used for process status | INV(d) S3/JDBC row "Not read [To be verified]" x3; BigQuery roles "not read in detail" | Read the page (class a) or drop the row | {t('unreadguides')} |
| Covered-by cells | All Covered-by cells valid per `check_drafts.py` (blocks (a) 15, (b) 24, (c) 12, (d) 13 rows; (a): 8 rows with SD headers and 7 with the inventory-only marker; b: SD1, SD5, SD6 headers only; c: SD3, SD4 headers; d: 5 rows with headers, 8 with the marker). Markers used: `— (inventory only, not in Table 3)` only; no legacy or planned marker, as BR requires. No stray `**`, backticks or literal pipes found by the checker. | No change; depends on {t('prefix')} and {t('fold')} | {t('prefix')} |

Rule of thumb: markup is clean (the checker passes) and the pins are uniform; the remaining work is label granularity (Summary labels, absence claims, TBV versus ND) and process language ({t('procfmt')}).
"""

style = f"""
## Style issues in columns

1. SD5 R3 Summary (reported at 46 words): now 44 words, within 45. SD5 R1 and SD5 R6 Summaries are exactly 45, so any added word breaks the limit. Largest R7 Summaries: SD6 56, SD1 47, SD4 47 of 60. No Summary has backticks, underscores, `$`, `%` or non-ASCII characters (scanned); every `**` pair balances; R8 Summaries start "**Key open questions.**" with no label; R9 Summaries are plain.
2. SD1 R4 Summary ends "The service was formerly called Cloud DLP." BR says headers and Summaries use the new name and "formerly Cloud DLP" goes in R1 and R4 Detail (SD1 R1 and R4 Detail already do). Remove the sentence or accept it as a deliberate exception.
3. Summary label versus facts (README section 3 rule 5): SD3 R1 and R4 ({t('sd3sum')}), SD4 R4 ({t('sd4sum')}), SD6 R2, R4, R5 ({t('sd6sum')}), SD2 R5 and SD4 R5 ({t('noverdict')}), SD5 R1 and R2 ({t('faceprev')}).
4. Internal column pointers: A and B refer to other columns as "the detection column", "the SD5 column", "the SD1 and SD2 columns" (15 bullets: A SD2 R2, R3, R5, R6 x2, R7, SD3 R2, R7 x2; B SD4 R2, SD5 R1, SD6 R1, R3, R6, R8). Column ids are not visible on the sheet; use the header words ("the sensitive-data detection in text column") or "see the text detection column" consistently.
5. Code citations differ between files ({t('citefmt')}): A gives the full path from the package root and the quoted line; B uses a shorter path and mostly no quotation.
6. Doubled parentheses in B SD6 R3 ("((SDP docs, REST projects.image.redact page, read 2026-10-09))"). Square-bracket text inside quotes in A SD3 R4 and R5 (A SD3 R4 "[fake@example.com]", R5 "[email-address]") sits in Detail bullets ending with a label; harmless for the parser (labels are matched at line end) but confusable with labels; consider a plain description.
7. B SD6 R2 has a bullet starting "Languages:" that is about pixels (not language), and B SD4 R1 mixes a quote with a remark about the British spelling in the header. Move the spelling note out of Detail.
8. R7 first Detail bullet: B SD4, SD5, SD6 start `**Minimum setup:**` in bold; A SD1, SD2 and SD3 start "Minimum setup: ..." without the bold markers. README section 4 requires the first Detail bullet and the Summary to start `**Minimum setup:**` (check_drafts.py passes both forms). All six R7 Summaries do start with the bold phrase.
9. No Reviewer notes section in A or B ({t('rnmissing')}); process language (README section 4 "no instructions to the reader") scan found none in A or B (searched "this draft", "I checked", "see above", "this brief"). Inventory has the process wording listed in {t('procfmt')}.
10. Out-of-purpose bullet placement and label vary by column ({t('oop')}); emulator or offline bullet present in five R7 rows and absent in SD2 R7 ({t('emul')}).
11. British spelling: American spellings appear only inside quotations of Google text ("analyze", "license", "organization") and product names (Analyzer, Anonymizer). Ordinary prose uses British forms (tokenisation, licence plates, colours).
12. Scope in columns: A SD1 R4 and SD3 R4 name Presidio and Sentinel headers only in Detail (allowed, R007 item 8); none appears in a Summary (checked). Content-policy text appears in SD1 R1 to R4 Detail and R8 only, as BR requires (SD7 is not drafted as a column).
"""

contra = f"""
## Contradictions

Source conflicts and cross-file inconsistencies, each with the ids that resolve them. Both sides are named.

1. Content policy "synchronous verdict" versus API surface (BR C2). Side one: overview "Get immediate, synchronous verdicts on content", the policy is "a reusable resource ... to evaluate content", and IAM defines `dlp.contentPolicies.apply` (inside `roles/dlp.user`) and a role "Apply content policies". Side two: the REST resource and client v3.40.0 expose create, delete, get, list and patch only. Carried in A SD1 R4 (as two labelled sources), INV(a), INV-RN 2. See {t('applyop')}, {t('cptest')}, {t('sd7')}.
2. Image formats for redaction and inspection (BR C1). Six statements in B SD5 R6: REST redact "PNG, JPEG, SVG or BMP"; redaction guide "not supported for SVG, PDF, XLSX, PPTX, or DOCX" and "JPEG, BMP, and PNG"; supported-file-types image row "bmp, gif, jpe, jpeg, jpg, png"; inspect guide "JPEG, BMP, PNG, and SVG"; method-types "JPEG, PNG, or TIFF"; client enum without GIF. INV(a) carries three of them and says the client docstring "repeats the REST wording", while B reports the enum value list (different facts, both possible). See {t('fmt_a')}, {t('fmt_b')}.
3. Bounding-box origin. REST InspectResult and client: (0,0) is upper left; inspect-images guide: bottom left; concepts page: "bottom-left corner". Only in B SD5 R5. See {t('bbox')}.
4. AES-SIV output length. Transformation table row: token "of the same length"; deterministic section: "Does not preserve the character set ... or length"; pseudonymization page: "does not preserve the character set or the length". The SD4 R4 Summary says "of any length". See {t('sd4sum')}, {t('sd4len')}.
5. `CryptoHashConfig` output. Table: "32-byte hexadecimal string"; body text and pseudonymization page: base64. In A SD3 R4/R8 and INV(c), INV-RN 3. INV(c) adds "HMAC-SHA-256" as [Documented] with no counterpart in A SD3. See {t('hashfmt')}, {t('emptycell')}.
6. Bucketing input type. Table cells say "Any"; the bucketing text says numerical data; date shift and time part samples use records. SD3 Summaries state the transformations as applied to detected values. See {t('sd3sum')}, {t('sd3test')}.
7. Default infoTypes when none are listed: five wordings on five pages (concepts: testing-only list; InspectConfig: "may automatically choose"; de-identify page: "ALL_BASIC"; redact images guide: "most common infoTypes"; REST image.redact: "may be all types"; de-identification: "applies to all built-in infoTypes that don't have a transformation"). BR observation O1. See {t('defa')}, {t('defb')}.
8. Custom detectors: dictionary size ("several tens of thousands" versus "several hundred thousand" versus 128 KB and 512 KB) and rule order (guide: as written; REST: exclusion last; release note 2026-02-23: enhanced ordering). A SD2 R4, R8. See {t('dictcap')}, {t('ruleorder_a')}, {t('ruleorder_b')}.
9. `DOCUMENT_TYPE/CONTEXT/*` on text. B SD6 R2 states as [Documented] that they "classify text, not pixels"; A SD1 R2/R8 #8 says it is unknown whether they run on a plain text string or in `asia-southeast1` (reference Availability: europe, global, us; limited availability). See {t('doctype')}.
10. Limits and re-identification. INV(e) applies the 0.5 MB and 100-transformation limits to `content.reidentify` as [Documented]; B SD4 R6 says the table does not name it and infers "probably". See {t('reidlim')}.
11. SLA coverage labels. B SD4 R6 and SD5 R6 [Inferred]; INV(e) [Not disclosed]; same fact. See {t('slalabel')}.
12. Out-of-purpose label. BR: [Documented]; A: [Inferred]; B: [Not disclosed]; README rule 2 favours [Not disclosed] for absence. See {t('oop')}.
13. Hash row coverage. BR and INV(c): hash row covered by SD3 and SD4; B SD4 R1: "its row belongs to the SD3 column". See {t('hashcov')}, {t('fold')}.
14. Summary versus Detail: SD3 R1/R4 versus the TBV bullet ({t('sd3sum')}); SD4 R4 versus the length conflict ({t('sd4sum')}); SD6 R2, R4, R5 versus their ND bullets ({t('sd6sum')}); "no verdict" versus Inferred bullets ({t('noverdict')}); SD5 R1/R2 "faces" versus Preview ({t('faceprev')}).
15. Libraries page versus package: samples "Python 2.7.x and 3.4 and higher" versus `python_requires >=3.10`; Ruby line installs `google-api-client`. A SD1 R7, INV(d), INV-RN 6. See {t('pylibdoc')}.
16. Region lists: locations page 43 regions including asia-southeast3; REST reference 42. INV(f), INV-RN 5. See {t('regionlist')}.
17. Limits page: two rate-quota rows share the name "Number of requests to a regional endpoint per minute per region" (600 and 100) and differ only by description; "subject to change". INV(e), INV-RN 7. See {t('limsum')}.
18. Domain and seeds: seeds.md still lists the pre-301 host; `docs/pricing` and `docs/quotas` are 404. INV-RN 8, BR C3. See {t('domain')}.
19. Brief versus drafts, resolved in the drafts' favour but to spot-check at P7: BR P1 grep found no `python_requires` (drafts cite setup.py line 95); BR asked whether metadata-label detectors can run on `content.inspect` (A SD2 R3 cites a documented `content.inspect` request with client-provided metadata); BR said add the Dataflow/S3/JDBC row only if a content-method use is shown (the draft adds it unread, {t('unreadguides')}).
20. Agreements worth recording (no action): the 21 credentials and secrets infoTypes (A SD1 R2 and INV(b)); the 261 infoTypes (A SD1 R2, INV(b) group counts sum to 261, INV(f) 240 + 21); Singapore NRIC and passport facts (A SD1, B SD5, INV(b)); the 10,000 / 600 / 100 per-minute quotas (A SD1/SD2/SD3, B SD4 to SD6, INV(e)); request caps 0.5 MB and 4 MB (A, B, INV(a), INV(e)). BR C5 (Model Armor basic mode "mainly the US region") is intentionally not carried, as BR allows.
"""

doc = head + rows + '\n' + hyg + style + contra
open('/home/user/guardrail_research/benchtest/drafts/sdp_triage.md', 'w', encoding='utf-8').write(doc)
print(len(doc.splitlines()), 'lines')
