#!/usr/bin/env python
# Builds benchtest/drafts/sdp_triage.md from the item data below (keys -> T-ids, counts computed).
import re, collections, sys

# (key, tag, item, locations, cls, source_or_why, prio)
I = []
def add(key, tag, item, loc, cls, src, prio):
    I.append(dict(key=key, tag=tag, item=item, loc=loc, cls=cls, src=src, prio=prio))

# ---------------------------------------------------------------- CP1 decisions
add('prefix', 'CP1',
    'Header prefix (Q01): `Sensitive Data Protection:` (BR default; the name docs, pricing page and console use) versus `Google Cloud Sensitive Data Protection:` (the CLAUDE.md product row). "Cloud DLP" is rejected as the legacy name. R009 freezes the prefix after CP2.',
    'BR scope and Q01; `## Column` lines SD1 to SD6 (A, B); INV Covered-by cells in (a) 8 rows, (b) all 24, (c) all 12, (d) 5 rows; INV scope paragraph',
    'D',
    'Decision for the user at CP1 (R009: the product\'s own name, vendor only if part of the brand). Evidence in BR: Google docs call it "Sensitive Data Protection"; only the API, host, IAM role and package keep "DLP". Cost of a change is mechanical (6 column headings plus 78 header strings in INV Covered-by cells, counted), so decide early. Drafts already mention the old name in SD1 R1 and R4 Detail as the brief asks.',
    'H')
add('sd7', 'CP1',
    'SD7 content policy (Q02, conflict C2): Table 3 column, or inventory only with the R011 marker. Default in BR and in the drafts is inventory only; the alternative is a seventh column `Sensitive Data Protection: Allow or block verdict by data sensitivity (content policy)` drafted as a third file.',
    'BR scope, C2, Q02; A SD1 R1 (contrast bullet), SD1 R4 (5 content-policy bullets), SD1 R8 #11 and R8 Summary; B SD5 R4 (last bullet), SD5 R8 #12, SD6 R4 (last bullet), SD6 R8 #12; INV(a) content policies row, INV(d) Gemini Enterprise row, INV(e) content policy file-limits row, INV(f) content policy location; INV-RN conflict 2',
    'D',
    'Decision for the user at CP1 (scope, new column). It is the only ALLOW or BLOCK output in the product and GA since 2026-08-31, but no documented way to submit a string was found, so a column would fail R7. New evidence in the drafts that BR does not have: IAM permission `dlp.contentPolicies.apply` is listed under `roles/dlp.user`, and a role described "Apply content policies" exists (see {applyop}); a user check of Gemini Enterprise access would settle testability ({cptest}).',
    'H')
add('fold', 'CP1',
    'Column split (Q03): fold SD2 (custom detectors and rules) into SD1 and SD4 (reversible tokenisation) into SD3, or keep six columns. Presidio PD3 and PD6 and the Model Armor split are to be decided the same way ("decide once", Q03 note).',
    'BR scope, Q03, "If CP1 folds"; A SD2 (all rows), B SD4 (all rows); INV(a) rows content.inspect, content.deidentify, content.reidentify, stored infoType; INV(b) all rows; INV(c) hash, FPE and AES-SIV rows; INV(d) five SD-header rows',
    'D',
    'Decision for the user at CP1. For folding SD2: A SD2 R3 says custom detectors are fields of the same InspectConfig on the same method and inputs, only large dictionaries need stored resources; surrogate detectors belong to SD4 (A SD2 R1). For keeping SD4: it has its own method (`content.reidentify`), its own request class, KMS key material, a round-trip test design (B SD4 R7) and its own open items (T-ids {altered}, {reidcv}, {keyrot}). If folded, the merger moves Detail bullets into SD1 R4 and R6 and SD3 R4 and R6, drops the SD2 and SD4 Summaries and removes two headers from every Covered-by list (INV-RN Covered-by decisions bullet 4). Hash row Covered-by also depends on this ({hashcov}).',
    'H')
add('imgsplit', 'CP1',
    'Q03 options (c) and SD6 placement: split SD5 into image inspection and image redaction, and keep SD6 (image safety) a separate column.',
    'BR Q03; B SD5 R1 (inspection and redaction "two distinct operations"), SD5 R5 (both outputs); B SD6 R1 (same two methods); INV(a) image redaction row, INV(b) image object and image context rows',
    'D',
    'Decision for the user at CP1; default (one image detection-and-redaction column, SD6 separate) is what the drafts follow. For separate SD6: different threat (whole-image safety, AI-generated image caveat) and different Summary label profile (B SD6). For keeping SD5 whole: `image.redact` bundles detection and redaction, inspection of images is also `content.inspect` (B SD5 R1).',
    'M')
add('mamarker', 'CP1',
    'Covered-by for rows that are integration paths into SDP (Model Armor basic and advanced modes, Gemini Enterprise attachment, Apigee, Data Fusion, BigQuery remote functions): drafts use the marker `— (inventory only, not in Table 3)` for the Model Armor rows because Covered-by may hold only this product\'s headers or a marker; R012 keeps the Model Armor columns as the owner.',
    'INV(d) Model Armor basic and advanced rows, Gemini Enterprise row, Data Fusion row, BigQuery row; INV-RN Covered-by decisions bullet 2',
    'D',
    'Decision for main (precedent R011/R012), no user input expected. Question: is "inventory only" the right marker for a path that is in scope for prompts and responses but whose columns live under Model Armor, or should the cell name the Model Armor headers? The checker accepts only known Table 3 headers or markers; check_drafts.py passes with the marker.',
    'M')
add('xrefhdr', 'CP1',
    'Cross-product headers written out in Detail bullets are provisional: Model Armor sensitive-data header (Input-level, and the "matching Output-level column" unwritten), `Model Armor: Image screening with OCR and visual scanning`, `Presidio: PII detection in text (Analyzer)`, `Presidio: PII anonymisation and masking in text (Anonymizer)`, `GovTech Sentinel: PII detection and masking (AWS Bedrock)`.',
    'A SD1 R4 (2 bullets), A SD3 R4 (2 bullets), B SD5 R4 (1 bullet)',
    'a',
    'At triage time every string matches presidio_brief.md, modelarmor_brief.md and the Sentinel brief exactly (compared by grep). Re-compare at P6 against presidio_two_level.md and modelarmor_two_level.md after their CP1; if their splits or prefixes change, edit these 5 bullets. The Output-level Model Armor header is named only by description; write it out at merge.',
    'M')
add('extsrc', 'CP1',
    'Google-owned pages outside the BR source list are cited in the inventory: Apigee extension page (docs.apigee.com), Cloud Data Fusion page, the SDP BigQuery tutorial and the `cloud.google.com/dlp/demo` page. BR lists only the Model Armor and Gemini Enterprise docs as cross-reference pages.',
    'INV(d) Apigee, Cloud Data Fusion, BigQuery at query time and console/demo rows',
    'D',
    'Decision for main (R007 item 1 and CLAUDE.md rule 1: the vendor\'s own docs are official; the cells already flag them "not SDP docs"). Log a ruling or have the rows cite them as cross-reference only. Related: {unreadguides}, {demodata}.',
    'M')
add('blog', 'CP1',
    'Google Cloud blog and Context7 not used (G13). BR: "If CP1 wants a blog source for LLM-guardrail positioning, add one fetch pass."',
    'BR "Not used"; P0 G13',
    'D',
    'Decision for the user only if LLM-guardrail positioning is wanted; no draft depends on it. Blog posts would be vendor-authored (allowed by rule 1) but marketing in kind.',
    'L')

# ---------------------------------------------------------------- content policy
add('applyop', 'CPOL',
    'Is there a public apply or evaluate operation for content policies? The REST resource lists create, delete, get, list and patch only and the client at v3.40.0 has no evaluate method (conflict C2), yet the IAM page lists the permission `dlp.contentPolicies.apply` (also inside `roles/dlp.user`) and a role described "Apply content policies".',
    'A SD1 R4 (definition bullet, 3 conflict bullets and 1 [ND] bullet), SD1 R6 (role bullet), R8 #11 and R8 Summary ("no verified way to apply a content policy to a string"); INV(a) content policies row (4 cells), INV-RN conflict 2; BR C2, G6',
    'a',
    'Answerable only if a public page names the operation: DOCS access-control/roles-permissions (full permission list and role description), manage-content-policies, content-policy, REST contentPolicies page and REST root, release notes 2026-08-31, and the Google API discovery document for the DLP v2 API (official Google page). If none names a callable method, reclassify as b (honest gap, Gemini Enterprise only). Settles {sd7}.',
    'H')
add('cptest', 'CPOL',
    'Direct test path for content-policy verdicts outside Gemini Enterprise (connectors, uploads, notebooks): no way to submit an arbitrary prompt or response is documented.',
    'A SD1 R8 #11; B SD5 R8 #12; B SD6 R8 #12; INV(a) content policies row (Table 3 scope "Partly"); BR Q02 option (c)',
    'b',
    'Needs a Gemini Enterprise tenant (or a confirmed API, see {applyop}). Ask the user whether such access exists (Q02 option c). Until then the SD1 R8 Summary item stands and the bench cannot call it, so R7 fails for a column.',
    'H')
add('cpmeta', 'CPOL',
    'Content-policy price, SLO, processing region of evaluation and whether evaluated content is stored: all [Not disclosed]; the Gemini Enterprise page says there is no extra cost there.',
    'INV(a) content policies row (storage cell), INV(e) content-policy file-limits row (price [ND]), INV(f) content policy location ([ND]); BR G6',
    'a',
    'PRC (no content-policy row seen), SLA page, manage-content-policies, content-policy, REST contentPolicies; Gemini Enterprise docs for the "no additional cost" sentence (not SDP docs). Re-read at P5; if still absent keep [Not disclosed] naming the pages.',
    'M')

# ---------------------------------------------------------------- Summary versus facts
add('sd3sum', 'SUM',
    'SD3 R1 and R4 Summaries say the method "redacts, replaces, masks, buckets, date-shifts or hashes" detected values (R1) and that each value is "redacted, replaced, masked, bucketed or date-shifted" (R4) under label [Documented], but the same column marks as [To be verified] whether bucketing, date shift and time part work on free-text infoType findings (docs samples use record transformations).',
    'A SD3 R1 Summary, R4 Summary, R4 [TBV] bullet (date-shift, time-extraction, bucketing samples), R8 #3; INV(c) bucketing (2 rows, [TBV]), date shifting and time extraction rows; INV-RN conflict 4 and uncertain bullet 8',
    'a',
    'Drafting fix at P5: narrow the Summaries (say bucketing, date shifting and time extraction apply to record fields) or relabel. DOCS transformations-reference (Input type cells: Any for bucketing, Dates/Times for date shift) and the REST InfoTypeTransformation/PrimitiveTransformation reference may state which primitives are allowed on infoType findings. Behaviour test is {sd3test}.',
    'H')
add('sd3test', 'DEID',
    'Do `FixedSizeBucketingConfig`, `BucketingConfig`, `DateShiftConfig` and `TimePartConfig` work on infoType findings in free text, or only on table fields? Docs table says "Any"/"Dates/Times", the bucketing text says numerical data.',
    'A SD3 R4 [TBV] bullet, R8 #3 and R8 Summary; INV(c) rows 9 to 12 (fixed-size and custom bucketing [TBV] x2, date shift, time extraction); INV-RN conflict 4, uncertain bullet 8',
    'b',
    'Needs one request per transformation on a free-text string with a matching infoType (for example a date inside a sentence). Docs checked: transformations-reference, de-identifying page; both silent for free text.',
    'H')
add('sd4sum', 'SUM',
    'SD4 R4 Summary says "AES-SIV gives base64 tokens of any length" while R4 Detail records a three-way conflict on AES-SIV output length (transformation table row: "of the same length"; deterministic section: does not preserve length; pseudonymization page: hashed value, does not preserve length) and R8 #2 leaves it open.',
    'B SD4 R4 Summary and 4 conflict bullets, R7 (token-length bullet), R8 #2; INV(c) AES-SIV row (does not mention the length conflict)',
    'a',
    'Drafting fix: drop "of any length" or state the conflict; re-read the three sentences on transformations-reference (table row versus deterministic-encryption section) and pseudonymization. Test is {sd4len}.',
    'H')
add('sd4len', 'TOK',
    'Does an AES-SIV token keep the input length (table row) or not (deterministic section, pseudonymization page)?',
    'B SD4 R4 (conflict bullets 1 to 3 plus client docstring bullet), R7 (token length versus input length), R8 #2',
    'b',
    'Tokenise several inputs of different length with `CryptoDeterministicConfig` and compare lengths; client docstring at the tag (types/dlp.py around line 5840) says base64 output and is silent on length.',
    'H')
add('sd6sum', 'SUM',
    'Three SD6 Summaries are labelled [Documented] but each contains a sentence whose only support is a [Not disclosed] bullet: R2 "Other harm categories are not listed", R4 "with unnamed models", R5 "They show no worked example of an image safety response". README section 3 rule 5: the Summary label is the weakest label among the facts it draws on.',
    'B SD6 R2 Summary vs bullet "reference lists only these three ... [ND]"; B SD6 R4 Summary vs bullet "Model names, architecture ... [ND]"; B SD6 R5 Summary vs bullet "Worked request or response samples ... [ND]"',
    'a',
    'Drafting fix at P5: either label those Summaries [Not disclosed] or move the absence sentence to R8. No new research.',
    'H')
add('noverdict', 'SUM',
    '"No verdict" is stated in two Summaries under [Documented] but the only supporting bullet is [Inferred]: A SD2 R5 ("There is no verdict.", bullet premise: same response shape as built-in inspection) and B SD4 R5 (title "no verdict", bullet "follows from the two response fields"). The same claim is [Documented] in SD1 R5 (content-policy contrast; client `InspectContentResponse`) and SD5 R5 (client redact response).',
    'A SD2 R5 Summary and its [Inferred] bullet; B SD4 R5 Summary and its [Inferred] bullet; A SD3 R5 (bullet [Inferred], Summary silent)',
    'a',
    'Cite the client response types at the tag as SD1 R5 and SD5 R5 do (B SD4 R5 already cites `item` and `overview` fields as [Documented: repo]) or relabel the Summaries [Inferred].',
    'H')
add('faceprev', 'SUM',
    'SD5 R1 and R2 Summaries list "faces" among detectable objects without saying the face detector is in Preview (the same column and INV(b) say so); R8 #10 asks whether other object detectors have a launch stage.',
    'B SD5 R1 Summary, R2 Summary; B SD5 R2 (Preview bullet), R8 #10; INV(b) image object detectors row',
    'a',
    'Drafting fix. Confirm Preview status and any stage marks on DOCS infotypes-reference and release notes (2025-12-15) for all eight object infoTypes ({stage}).',
    'H')
add('oop', 'SUM',
    'The "out of purpose" statement (no prompt-injection, jailbreak, toxicity or topic-drift detection) is labelled three ways: [Inferred] in SD1, SD2, SD3 R2; [Not disclosed] in SD4, SD5, SD6 R2. BR told drafters to write it [Documented] "from the overview page".',
    'A SD1 R2 (out-of-purpose bullet), SD2 R2, SD3 R2; B SD4 R2, SD5 R2, SD6 R2; BR scope bullet "No other guardrail functions"',
    'a',
    'Pick one pattern at P5 (README section 3 rule 2: absence is [Not disclosed] naming the pages checked, so BR\'s [Documented] suggestion for the absence conflicts with the README). Suggested: purpose sentence [Documented] (overview page) plus one [Not disclosed] bullet. Ruling by main (QUESTIONS).',
    'M')

# ---------------------------------------------------------------- limits and numbers
add('limsum', 'LIM',
    'Limits-page numbers that appear in Summaries: 0.5 MB and 3,000 findings (SD1 R6), 30 custom detectors, 10 regular dictionaries, 10 rule sets, 1000-character regexes (SD2 R6), 0.5 MB, 100 transformations, 3,000 (SD3 R6), 4 MB and 0.5 MB (SD5 R6). The page says its values are "subject to change"; the cloud.google.com copy returns an empty body through fetch_text.py, so only the docs.cloud.google.com copy was read; two rate-quota rows carry the same quota name and differ only by description.',
    'A SD1 R6 Summary, SD2 R6 Summary, SD3 R6 Summary; B SD5 R6 Summary; INV(e) rows 1 to 8, 11 to 13 and conflicts note 7; BR G12',
    'a',
    'Re-match every number against DOCS limits (docs.cloud.google.com/sensitive-data-protection/limits) as raw text on the P7 read date; keep the "subject to change" caveat in Detail. Check also the REST InspectConfig page for the 3,000 wording ("isn\'t a hard limit").',
    'H')
add('reidlim', 'LIM',
    'INV(e) applies the 0.5 MB request limit and the 100-transformation limit to `content.reidentify` as [Documented], while B SD4 R6 says the limits table is headed "inspecting and de-identifying content" and does not name re-identification, and only infers ("probably") that the limits apply.',
    'INV(e) rows 1 and 6 (Applies-to cells); B SD4 R6 ([Inferred] bullet), R8 #4 and #10',
    'a',
    'Re-read the heading of the LIM table and the REST reidentify page; then fix the INV Applies-to cell or relabel it [Inferred] to match the column.',
    'M')
add('slalabel', 'LIM',
    'No SLA/uptime row for `content.reidentify` and `image.redact`: the columns label this [Inferred] ("Because the SLA names only inspect and deidentify requests ...") while INV(e) labels it [Not disclosed] (checked the SLA page).',
    'B SD4 R6 (SLA bullets), SD4 R8 #10; B SD5 R6 (last bullet); INV(e) Availability SLO row; BR G8',
    'a',
    'SLA page: the "Covered Service" definition lists inspect and deidentify only. An absence claim is [Not disclosed] naming the SLA page; align the three places.',
    'M')
add('price', 'LIM',
    'Pricing figures and free-tier wording ("first gibibyte per month per account", 1 KB minimum, simple-redaction exemption, per-method billing table, content inspection versus transformation prices).',
    'A SD1 R6, R7; SD3 R5, R6, R7; B SD4 R6, R7; SD5 R6; SD6 R6; INV(e) content method prices row',
    'a',
    'PRC raw text re-match (price tiers are table cells, one per line); confirm that "per month per account" is on the page and not only in the brief. Not in any Summary.',
    'L')
add('invlimcov', 'LIM',
    'INV(e) omits the stored-infoType file and row limits listed in A SD2 R6 (200 MB input file, 5,000,000 BigQuery rows, 500 MB output files); the other custom-detector limits appear in both. Coverage differs between the column and the inventory.',
    'A SD2 R6 (stored infoType limits bullet group); INV(e) "Custom dictionary size" and "Resources per project" rows',
    'a',
    'LIM raw text; add rows or accept the gap. Row count of block (e) (16) is asserted by the config module, so tell main if rows change.',
    'L')
add('quotagap', 'GAP',
    'Per-method quotas (for example `image.redact`) and quota maxima are not on the public limits page; the console "Quotas & System Limits" page is not public.',
    'A SD1 R8 #13; BR G11',
    'b',
    'Honest gap: checked LIM, pricing, SLA; only the console quota page could answer.',
    'L')

# ---------------------------------------------------------------- honest gaps
add('acc_text', 'GAP',
    'No published accuracy, precision or recall for any built-in infoType, including Singapore NRIC and passport, by language or by likelihood level; same for custom detectors (depends on the user\'s list or pattern).',
    'A SD1 R5 [ND], R8 #1 and R8 Summary; A SD2 R5 [ND], R8 #9; INV(b) Document context categories row (accuracy [ND]); BR G1',
    'b',
    'Honest gap: checked infoTypes reference, concepts, likelihood, overview, release notes and the client repo. Stays open by design; this is what the bench measures. Docs only say to test your settings.',
    'H')
add('acc_deid', 'GAP',
    'No published residual-leak rate, accuracy or utility measure for de-identification, and no effect-on-LLM-answer-quality guidance for each replacement style.',
    'A SD3 R5 [ND], R8 #1, #8 and R8 Summary; R7 (residual-leak and utility tests)',
    'b',
    'Honest gap; test design is already in A SD3 R7. Docs checked: de-identifying, transformation reference, text redaction, likelihood, concepts.',
    'H')
add('acc_tok', 'GAP',
    'No published measure of tokenisation round-trip correctness, token collision rate or throughput.',
    'B SD4 R5 [ND], R7 (round trip, determinism, FPE edge cases), R8 #1',
    'b',
    'Honest gap; test in B SD4 R7. Docs checked: pseudonymization, transformation reference, quickstart, pricing, limits, SLA, release notes.',
    'M')
add('acc_img', 'GAP',
    'No published precision, recall, false-positive rate, OCR error rate or per-object detection accuracy for image text and object detectors.',
    'B SD5 R5 [ND], R8 #4 and R8 Summary',
    'b',
    'Honest gap: checked image concepts, inspect, redact, likelihood, infoType reference, release notes.',
    'H')
add('acc_safe', 'GAP',
    'No accuracy, thresholds per category or calibrated minimum likelihood for image safety classification; AI-generated images are a stated weak point and several categories may fire on one image.',
    'B SD6 R2 (AI-generated bullets), R5 [ND] x3, R8 #1, #4, R8 Summary; R7 (threshold sweep)',
    'b',
    'Honest gap: checked image concepts, likelihood, infoType reference. Docs themselves say "Don\'t rely solely on these classifiers" and to test your own use case.',
    'H')
add('latency', 'GAP',
    'Latency and throughput: no figures for any method (only "run much more slowly" for name and location infoTypes, FPE "can run very slowly", 99.5% availability SLO for two methods); includes Conversation items and image calls.',
    'A SD1 R8 #2, R8 Summary; A SD2 R8 #9; A SD3 R8 #7; B SD4 R8 #1 and R8 Summary; B SD5 R8 #9; B SD6 R8 #9; BR G2, G9',
    'b',
    'Honest gap: checked inspecting-text, limits, pricing, SLA. Needs measuring from Singapore against global and `asia-southeast1` endpoints.',
    'H')
add('models', 'GAP',
    'Backing models for the ML-based detectors: `PERSON_NAME` ("natural language understanding"), document-category classifiers, OCR, object detection and image safety classification: names, versions and training data not disclosed.',
    'A SD1 R4 [ND], R8 #3 and R8 Summary; B SD5 R4 [ND]; B SD6 R4 [ND] and R4 Summary; INV(b) image context row [ND]; BR G3',
    'b',
    'Honest gap (closed Google internals): checked concepts-infotypes, reference, supported-file-types, image concepts, release notes. Not expected in a public document.',
    'H')
add('lang_text', 'GAP',
    'Per-infoType language coverage: one general sentence ("English and the respective country\'s languages; most global infoTypes work with multiple languages"); Singlish, Chinese, Malay and Tamil text support untested, and which languages count as Singapore\'s is not stated.',
    'A SD1 R2 ([ND] bullet and [TBV] bullet), R8 #4 and R8 Summary; B SD4 R2 (language bullet); INV(b) Singapore row ([ND]), all country rows (language sentence)',
    'b',
    'Docs checked: concepts-infotypes, reference, infoTypes.list page; no table. Needs a multilingual labelled set.',
    'H')
add('lang_cust', 'GAP',
    'Dictionary and regex word boundaries on unspaced scripts (Chinese, Malay, Tamil): behaviour of the "different type" boundary rule is untested.',
    'A SD2 R2 ([Inferred] bullet on Unicode), R8 #5 and R8 Summary',
    'b',
    'Docs checked: regular custom dictionary page (BMP letters and digits matched; other characters act as whitespace). Needs testing with CJK and Tamil dictionary entries.',
    'H')
add('lang_ocr', 'GAP',
    'OCR languages and scripts, handwriting accuracy, rotated or low-resolution text and minimum text size: not stated.',
    'B SD5 R2 [ND], R8 #5, R8 Summary ("non-English text")',
    'b',
    'Honest gap: checked image concepts, inspect, redact, supported-file-types, infoType reference.',
    'H')
add('ctxlen', 'GAP',
    'Context-length or token limits: only a 0.5 MB byte cap is documented.',
    'BR G7 (not carried into any R8 bullet)',
    'b',
    'Honest gap; low impact because the limit is bytes. Mention in SD1 R6 only if the merger wants it.',
    'M')
add('emul', 'GAP',
    'No offline or emulator mode and no first-party evaluation toolkit for any function (every test sends data to Google).',
    'A SD1 R7 [ND] x2, SD3 R7 [ND]; B SD4 R7 [ND], SD5 R7 [ND], SD6 R7 [ND]; A SD2 R7 (no emulator bullet)',
    'b',
    'Honest gap: checked overview, method types, libraries, endpoints, locations, package README. Note SD2 R7 has no emulator bullet while the other five R7 rows do; harmonise at merge.',
    'L')

# ---------------------------------------------------------------- Singapore
add('fin', 'SG',
    'Does `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` also cover FIN numbers, and how is the check letter treated? Description names only the NRIC card ("nine alpha-numeric characters"). No other Singapore infoType (FIN, UEN, address) exists in the reference.',
    'A SD1 R2 ([TBV] bullet and [ND] bullet), R8 #5 and R8 Summary; INV(b) Singapore row ([TBV], [ND]); B SD5 R2 (NRIC in images)',
    'b',
    'Docs checked: reference and concepts. Needs synthetic S/T/F/G/M-series numbers with valid and invalid check letters. Re-check the reference for new Singapore infoTypes on the P7 date ({counts}).',
    'H')
add('plus65', 'SG',
    'Does `PHONE_NUMBER` detect Singapore +65 numbers? Described only as "A telephone number." with no country scope.',
    'A SD1 R2 ([TBV] bullet), R8 #5 and R8 Summary; INV(b) global person identifiers row ([TBV])',
    'b',
    'Needs a test with +65 and 8-digit local formats at several minimum likelihood levels; docs checked: reference, concepts.',
    'H')
add('sgimg', 'SG',
    'Do the passport and photo-ID-card object detectors recognise Singapore passports and NRIC cards (including FIN cards)? And is an NRIC printed in an image found through OCR plus the text detector ([Inferred])?',
    'B SD5 R2 ([ND] bullet and [Inferred] bullet), R8 #6 and R8 Summary',
    'b',
    'Docs checked: reference, release notes, image pages; no Singapore example. Needs synthetic images.',
    'H')
add('doctype', 'SG',
    'Do the `DOCUMENT_TYPE/CONTEXT/*` classifiers run on a short plain-text string, and are they usable in `asia-southeast1` (reference Availability: europe, global, us only; "limited availability")?',
    'A SD1 R2 ([TBV] bullet and limited-availability bullet), R8 #8; INV(b) Document context categories row; INV-RN uncertain bullet 9; B SD6 R2 (bullet calling them "text-side analogues ... they classify text, not pixels")',
    'b',
    'Docs checked: reference (Availability column, "can cause scanning issues in unsupported regions"). Needs a test in `asia-southeast1` and in `global`. B SD6 R2 states as [Documented] that they classify text, which A SD1 says is unknown for plain strings (contradiction 9).',
    'M')

# ---------------------------------------------------------------- infoType list, defaults, versions
add('defa', 'LIST',
    'Which infoTypes run when none are given: five wordings on five pages (testing-only default list; "may automatically choose ... may change over time"; "default set (ALL_BASIC)"; "searches for the most common infoTypes" / "By default this may be all types" for images; de-identification "applies to all built-in infoTypes that don\'t have a transformation provided"), plus a 2019 note that ALL_BASIC changed.',
    'A SD1 R6 (4 default-list bullets), R8 #6; A SD3 R4 (no-infoType bullet); B SD5 R6 (2 default bullets and the "always specify" advice); B SD6 R6 ([ND] bullet), R8 #6; BR observation O1',
    'a',
    'Re-read concepts-infotypes, InspectConfig, REST image.redact, redacting-sensitive-data-images, de-identifying page and release notes; check whether ALL_BASIC is defined anywhere (infoTypes.list `supportedBy`, a listing page). Quote all wordings, no label upgrade. Membership test is {defb}.',
    'H')
add('defb', 'LIST',
    'Exact membership of the default infoType set (and whether image context detectors run when none are listed) on the read date.',
    'A SD1 R8 #6 and R8 Summary; B SD6 R8 #6 and R8 Summary',
    'b',
    'Needs one empty-infoTypes request on a probe string and one on an image, or an `infoTypes.list` call (read-only rule: not run in research). Docs say "Always specify infoTypes explicitly".',
    'H')
add('pnamea', 'LIST',
    'Time-sensitive: a new `PERSON_NAME` version (updated name dictionary) was released 2026-10-03 and "in 30 days" is promoted to stable (about 2026-11-02); `InfoType.version` values stable, latest and legacy. Findings depend on the read date and version.',
    'A SD1 R4 (3 bullets), R7 (version bullet), R8 #7 and R8 Summary; INV(b) Health row (MEDICAL_ID version note), global person identifiers row',
    'a',
    'Re-read the release notes on the P7 and P9 dates; record whether the promotion happened, and cite the note with its date. Record the version used in tests.',
    'H')
add('pnameb', 'LIST',
    'Effect of the `PERSON_NAME` version change on a fixed test set before and after promotion to stable.',
    'A SD1 R8 #7',
    'b',
    'Two test runs with `version` pinned to latest and to stable; honest gap in docs.',
    'H')
add('counts', 'LIST',
    'Dated counts made by the drafters: 261 infoTypes (522 description cells paired), 240 ANY_LOCATION and 21 REGIONAL, 21 secrets, location filter of 51 entries, 43 regions on the locations page, 24 group counts that sum to 261. The reference "changes periodically".',
    'A SD1 R2 (3 [Inferred] count bullets); INV(b) all 24 rows, intro paragraph; INV(f) infoType availability and regional endpoints rows; INV-RN counts; BR "Exploration findings"',
    'a',
    'Recount from raw reference text at the P7 date (the group counts sum to 261 at triage: checked by addition). Counts stay [Inferred] with the counting rule; never quote as Google figures.',
    'M')

# ---------------------------------------------------------------- SD2 custom detectors
add('regex', 'CUST',
    'Which regex engine and syntax limits apply to custom regex detectors: only a docs code-sample comment points to RE2; the guide text names no engine; unsupported constructs unknown.',
    'A SD2 R4 (regex syntax bullet), R8 #1 and R8 Summary',
    'a',
    'Re-read creating-custom-infotypes-regex, InspectConfig.Regex reference and the likelihood/rules pages for an RE2 statement; if only the sample comment exists keep [Documented] for the comment and add a b test for constructs.',
    'H')
add('dictcap', 'CUST',
    'Dictionary capacity conflict: "up to several tens of thousands" (concepts) versus "at most several hundred thousand" (custom-infoType overview) versus LIM 128 KB inline and 512 KB from Cloud Storage per regular dictionary.',
    'A SD2 R4 (2 size bullets), R6 (limits groups), R8 #2 and R8 Summary',
    'b',
    'Both statements and the LIM values are already quoted; reconcile units by testing a real word list (words versus KB). Keep as two labelled bullets until then.',
    'H')
add('ruleorder_a', 'CUST',
    'Rule order: guide says rules apply in the order written; REST InspectConfig says exclusion rules run last; release note 2026-02-23 announces "Enhanced rule ordering" at GA, so the REST text may be older.',
    'A SD2 R4 (3 order bullets, one [Inferred]), R5 ("Rules are applied in the order that they are specified"), R8 #3 and R8 Summary',
    'a',
    'Read the creating-custom-infotypes-rules page, REST InspectConfig rule set text and the 2026-02-23 release note together; the dated note may settle which text is current. Then {ruleorder_b}.',
    'H')
add('ruleorder_b', 'CUST',
    'Behaviour of mixed rule sets (exclusion, hotword, adjustment) against the documented order.',
    'A SD2 R8 #3, R7 (rule on/off comparison)',
    'b',
    'Test with a mixed rule set on one string; needed only if {ruleorder_a} leaves the order ambiguous.',
    'M')
add('storedperm', 'CUST',
    'Is `roles/dlp.user` (four listed permissions: `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*`, `serviceusage.services.use`) enough to use a stored infoType in `content.inspect`? The listed permissions name no stored-infoType permission.',
    'A SD2 R6 ([TBV] bullet), R8 #4 and R8 Summary; INV(a) stored infoType row',
    'a',
    'DOCS access-control/roles-permissions (full permission lists for DLP User and DLP Reader, any stored-infoType permission) and creating-stored-infotypes (required roles). If silent, add a permission test (b).',
    'H')
add('cmeta', 'CUST',
    'Size limits for `contentMetadata`, number of labels per request, and region availability of metadata-label detectors and image rules.',
    'A SD2 R8 #6 and #8; INV(a) content.inspect row (Input types)',
    'a',
    'ContentItem and limits pages, locations page and release notes (2026-03-07, 03-28, 06-29 notes); checked in draft: not stated.',
    'M')
add('convctx', 'CUST',
    'Conversation items: do CONTEXT messages improve detection in neighbouring messages or only get ignored; can custom detectors match across messages; do the request cap and finding cap apply to the whole conversation or batch?',
    'A SD1 R8 #9, #10; A SD2 R8 #7; A SD3 R8 #9, #5; BR G9',
    'b',
    'REST ContentItem and release notes (2026-06-03, 06-12) checked: not stated. Needs tests with split and joined messages.',
    'M')

# ---------------------------------------------------------------- SD3
add('overlap', 'DEID',
    'How overlapping findings of different infoTypes are transformed when both have a transformation.',
    'A SD3 R8 #4 and R8 Summary',
    'a',
    'Check the de-identify page, REST InfoTypeTransformations reference and any overlap statement in infoTypes concepts; draft says "not stated". If silent, test (b).',
    'H')
add('cap3000', 'DEID',
    'Behaviour near the 3,000-finding cap in de-identification: error message only or partial result; whether the cap counts across conversation messages or batch strings.',
    'A SD3 R5 (Too many findings, partial subset bullets), R8 #5 and R8 Summary; A SD1 R8 #10; B SD4 R5 (same message), R8 #4',
    'b',
    'Docs give the message and "arbitrary subset" wording; needs a request with more than 3,000 matches (single string, conversation, batch).',
    'H')
add('hashfmt', 'DEID',
    '`CryptoHashConfig` output: table says 32-byte hexadecimal string, body text and pseudonymization page say base64; inventory adds "HMAC-SHA-256" as [Documented].',
    'A SD3 R4 (hash source 1 and source 2 bullets), R8 #2 and R8 Summary; INV(c) hash row; INV-RN conflict 3',
    'b',
    'Both statements are quoted; needs one request. Also re-match the "HMAC-SHA-256" phrase on transformations-reference (it is in the inventory only, not in A SD3).',
    'H')
add('lvuntr', 'DEID',
    'Is `transformationErrorHandling` (ThrowError/LeaveUntransformed) documented in the REST DeidentifyConfig reference? Draft says "only the client describes it".',
    'A SD3 R4 (client transformation-errors bullet), R8 #6',
    'a',
    'REST DeidentifyConfig / DeidentifyContentRequest reference pages (not read as REST pages by A).',
    'M')
add('llmq', 'DEID',
    'Effect of each replacement style (mask, fixed value, infoType name) on LLM answer quality.',
    'A SD3 R7 (utility test), R8 #8',
    'b',
    'Test design item, not a product fact; no Google guidance found.',
    'L')

# ---------------------------------------------------------------- SD4
add('altered', 'TOK',
    'How the service treats a token altered by a model (truncated, case-changed, split), a token made with another key, or a surrogate name that occurs naturally: error, unchanged text or wrong text.',
    'B SD4 R4 (failure-mode docstring bullet), R7 (hostile cases), R8 #5 and R8 Summary',
    'b',
    'Client docstring (types/dlp.py around line 5876) names two failure modes; needs tests with altered tokens.',
    'H')
add('reidcv', 'TOK',
    'Does `content.reidentify` accept conversation and batch items (release notes 2026-06-03/06-12 say "inspecting and de-identifying" only)?',
    'B SD4 R8 #3 and R8 Summary; A SD1 R3 / SD3 R3 (conversation support bullets)',
    'a',
    'REST reidentify page, ContentItem, release notes; draft says the REST text says only "treated as text". Then test if silent.',
    'H')
add('reidcap', 'TOK',
    'Do the 3,000-finding limit and error message also apply to `content.reidentify`?',
    'B SD4 R5 (too-many-findings bullet), R8 #4',
    'b',
    'Message is documented only on the de-identification page; needs a request.',
    'M')
add('keyrot', 'TOK',
    'What happens to tokens already issued when the Cloud KMS key version is rotated or destroyed? Quickstart cleanup warns that destroying a key version stops decryption; no rotation guidance found.',
    'B SD4 R8 #6 and R8 Summary ("what happens to old tokens when keys change")',
    'a',
    'Cloud KMS docs on key versions and wrapped-key decryption (Google docs, flag "not SDP docs"), SDP create-wrapped-key and quickstart cleanup. Then test (b) if still unclear.',
    'H')
add('kmsid', 'TOK',
    'Which identity needs which Cloud KMS permission at request time (caller or DLP service agent), and does a Singapore-region KMS key work with the `asia-southeast1` regional endpoint?',
    'B SD4 R8 #7, #11; R6 (KMS placement bullets); R7 (minimum setup)',
    'a',
    'Quickstart, create-wrapped-key, roles and auth pages plus Cloud KMS locations (not SDP docs). Draft: "both named only generally".',
    'M')
add('audit', 'TOK',
    'Do request bodies, tokens or wrapped keys appear in Cloud Audit Logs? The audit-logging page was not read.',
    'B SD4 R8 #8',
    'a',
    'SDP audit-logging page (exists in the docs navigation per draft).',
    'M')
add('hashcov', 'TOK',
    'Covered-by for the `CryptoHashConfig` row: BR adds the SD4 header; B SD4 R1 says the hash is "the one-way contrast" whose row belongs to SD3.',
    'INV(c) hash row (Covered-by lists SD3 and SD4); B SD4 R1 (contrast bullet); BR column notes (SD4)',
    'a',
    'Internal consistency, decide with {fold}: if SD4 stays, either drop the SD4 header from the hash row or keep it because SD4 R1 uses hash as contrast.',
    'M')

# ---------------------------------------------------------------- images
add('fmt_a', 'IMG',
    'Image formats, documentation side (conflict C1): REST `image.redact` "PNG, JPEG, SVG or BMP"; redaction guide "not supported for SVG, PDF, XLSX, PPTX, or DOCX" and "JPEG, BMP, and PNG"; supported-file-types image row "bmp, gif, jpe, jpeg, jpg, png" (a second, discovery row lists more); inspect guide "JPEG, BMP, PNG, and SVG"; method-types page "JPEG, PNG, or TIFF"; client enum has IMAGE, JPEG, BMP, PNG, SVG and no GIF. SD5 carries six statements; INV(a) carries three.',
    'B SD5 R6 (6 conflict bullets, discovery-table bullet, [Inferred] test-first bullet), R7, R8 #1 and R8 Summary; B SD6 R6 (carry-over bullet), R8 #10; INV(a) image redaction row, INV-RN conflict 1; BR C1',
    'a',
    'Re-read supported-file-types raw text and confirm which table and column header each row belongs to (content methods versus discovery), then align the INV row with the six statements (INV omits the inspect-guide SVG statement, the method-types TIFF statement and the client enum). No label upgrade.',
    'H')
add('fmt_b', 'IMG',
    'Which image formats `content.inspect` and `image.redact` actually accept (PNG, JPEG, BMP, SVG, GIF, TIFF).',
    'B SD5 R7 (formats bullet), R8 #1 and R8 Summary; B SD6 R8 #10',
    'b',
    'Needs one request per format at sizes below 0.5 MB and 4 MB; docs conflict ({fmt_a}).',
    'H')
add('bbox', 'IMG',
    'Bounding-box origin: REST InspectResult and client say (0,0) is upper left; the inspect-images guide says (0,0) is the bottom left; concepts page says "bottom-left corner" and dimensions.',
    'B SD5 R5 (3 statement bullets plus client bullet), R7 (origin check), R8 #3 and R8 Summary',
    'b',
    'All sides quoted; needs a request on an image with a known box. Impacts any box-overlap scoring in the bench.',
    'H')
add('nosupreg', 'IMG',
    'What `content.inspect` / `image.redact` return in a region without image scanning: an error, a binary scan or silently empty results (locations page describes files, not content calls).',
    'B SD5 R8 #7 and R8 Summary; B SD6 R8 #8; INV(f) image-scanning locations row',
    'b',
    'Docs checked: locations page, release notes. Needs a call in an unsupported region.',
    'H')
add('sizebase64', 'IMG',
    'Do the 4 MB and 0.5 MB limits apply to the base64 text or the decoded bytes; does the 0.5 MB limit apply to images sent to `content.inspect` (draft: [Inferred])?',
    'B SD5 R6 ([Inferred] bullet), R8 #2; B SD6 R6 (carry-over)',
    'b',
    'LIM and REST pages checked: not stated; needs images just under and over each limit.',
    'M')
add('overlapred', 'IMG',
    'Whether redaction of overlapping or adjacent findings leaves partial text visible, and how box padding is chosen.',
    'B SD5 R8 #8',
    'b',
    'Needs testing on dense images.',
    'M')
add('exif', 'IMG',
    'Is metadata (EXIF) stripped from the redacted image? REST text says metadata is omitted for multiframe images only.',
    'B SD5 R8 #11',
    'b',
    'Needs a test with an EXIF-bearing image.',
    'M')
add('stage', 'IMG',
    'Launch stage (GA or Preview) of each object infoType and of the three image-context detectors: only the face detector is marked Preview; for the image-context detectors the release note says only "available".',
    'B SD5 R8 #10; B SD6 R6 ([ND] bullet), R8 #7; INV(b) image object and image context rows',
    'a',
    'DOCS infotypes-reference (stage marks), release notes 2025-07-04, 2025-11-03, 2025-12-15, 2026-01-16, 2026-06-08.',
    'M')
add('imgfind', 'IMG',
    'What a whole-image safety finding returns for location (a box covering the image, no box, or another value), and whether several categories can fire on one image.',
    'B SD6 R5 (ImageLocation bullet, [Inferred] one-finding-per-category bullet), R8 #3, #4 and R8 Summary',
    'b',
    'supported-file-types table lists ImageLocation for image content classification; no worked sample ([ND]). Needs a test.',
    'H')
add('textinimg', 'IMG',
    'Does text printed in an image (offensive words, captions) affect the safety classifier? Docs say it uses pixels and features, not extracted text.',
    'B SD6 R2 (pixels bullet), R7 (text-only images), R8 #5 and R8 Summary',
    'b',
    'Needs a test; docs checked: supported-file-types, image concepts.',
    'H')
add('localnorms', 'IMG',
    'How strictly "racy" and "sexually suggestive" are defined and whether the labels reflect Singapore community norms; a one-sentence definition is all the reference gives.',
    'B SD6 R8 #2 and R8 Summary ("local norms"); R2 (definition bullets)',
    'b',
    'Honest gap (closed model behaviour). Needs a human-labelled local set.',
    'H')
add('imgsize', 'IMG',
    'Reliability on very small, very large and multi-subject images, including minimum image size for safety classification.',
    'B SD6 R8 #11',
    'b',
    'Not stated; needs testing.',
    'M')
add('fileon', 'IMG',
    'Do PDF, Word, Excel and PowerPoint byte items work on `content.inspect` (client enum lists them; metadata-label page shows a PDF `byteItem` request), given that BR puts file inspection through jobs out of scope and SD3 R3 shows de-identify supports only CSV, TSV and text?',
    'A SD1 R3 (byte items bullets), SD3 R3 (supported-file-types bullet); A SD2 R3 (metadata formats bullet); BR scope bullet 5',
    'a',
    'DOCS supported-file-types ("Inspect content" per file type) and the metadata-label page; then a test (b). Decide whether files on the AI data path are in scope for SD1 (BR: "files or images sent to or from the model" are in scope).',
    'M')

# ---------------------------------------------------------------- inventory
add('unreadguides', 'INV',
    'Dataflow, AWS S3 and JDBC guides row (and Apigee, Data Fusion, BigQuery rows) were "read only far enough": four cells say "Not read [To be verified]" or "To be verified". BR said to add the row only if a guide shows a content-method use.',
    'INV(d) Dataflow/AWS S3/JDBC row (4 cells), Apigee row, Data Fusion row, BigQuery row (roles [TBV]); INV-RN uncertain bullet 4',
    'a',
    'The SDP-docs guides for S3 and JDBC are readable (GitHub sample page returned 403 and is out of scope under R013). Read them, then keep the row only if a content method is used, else drop it (block (d) count 13 changes; tell main).',
    'M')
add('otherlibs', 'INV',
    '"The other libraries were not read at a pinned ref [Not disclosed] (only the libraries page was read)": [Not disclosed] is for vendor silence, this is "not read".',
    'INV(d) Other client libraries row (Notes); INV-RN uncertain bullet 5',
    'a',
    'Relabel [To be verified] or drop the sentence (BR says name them only; do not read them).',
    'L')
add('pydlp', 'INV',
    'Archive notice of `googleapis/python-dlp` is [To be verified] (exploration note; github.com returned 403 and a fresh clone was not made).',
    'INV(d) Python client row (Notes); INV-RN uncertain bullet 3; BR "Code (supporting only)"',
    'a',
    'R013: shallow clone of googleapis/python-dlp and read the README archive notice; if denied record "checked, not reachable".',
    'L')
add('gcloud', 'INV',
    'No dedicated `gcloud` command group for content inspection found; demo app at `cloud.google.com/dlp/demo` returned HTTP 200 with a title only.',
    'INV(d) console, gcloud and web demo row ([ND], [TBV]); INV-RN uncertain bullets 1 and 2',
    'b',
    'Honest gap/absence: checked method-types and inspect-sensitive-text-api. Demo data handling is {demodata}.',
    'L')
add('regionlist', 'INV',
    'Locations page lists 43 regions including asia-southeast3 (Bangkok); the REST reference regional-endpoint list has 42 and omits it. Counts made by the drafter ([Inferred]).',
    'INV(f) regional endpoints row; INV-RN conflict 5',
    'a',
    'Re-read both pages; keep two labelled facts. Not Singapore-relevant.',
    'L')
add('pylibdoc', 'INV',
    'Libraries page says samples work with "Python 2.7.x and 3.4 and higher" (and the Ruby line installs `google-api-client`), while the package at the tag requires Python 3.10 or later (`python_requires` found at setup.py line 95; BR P1 grep found none).',
    'A SD1 R7 (2 Python-version bullets); INV(d) Python client row, Other client libraries row; INV-RN conflict 6',
    'a',
    'Re-read setup.py around line 95 at the tag and the libraries page; keep two bullets; the samples text is a docs-staleness note, not a package conflict.',
    'L')
add('domain', 'INV',
    'seeds.md still carries the old docs host (301 chain cloud.google.com to docs.cloud.google.com); `docs/pricing` and `docs/quotas` are 404.',
    'INV-RN conflict 8; BR C3',
    'a',
    'HTTP facts already recorded (curl -I, 2026-10-09). Housekeeping for main (seeds.md); not a content conflict.',
    'L')
add('urls', 'INV',
    'URL hygiene: many R9 and inventory URLs were not in the BR list of P0-read pages (for example inspecting-structured-text, quote, concepts-templates, create-custom-infotypes-metadata-labels, inspect-sensitive-text-api, inspect-sensitive-text-de-identify, create-wrapped-key, auth, access-control/roles-permissions, inspecting-storage, concepts-hybrid-jobs, concepts-deidentify-storage, deidentify-storage, data-profiles, concepts-job-triggers, concepts-risk-analysis, listing-infotypes, specifying-location, deidentify-bq-tutorial, Apigee, Data Fusion, dlp/demo, rest.py, CHANGELOG.md, LICENSE); B SD6 R5 cites the REST InspectResult page but SD6 R9 does not list it.',
    'A and B R9 lists; INV Source URL cells; B SD6 R5 vs R9',
    'a',
    'P9 URL check (gr-url-checker). Fix at P6: add the InspectResult URL to B SD6 R9. INV-RN says guessed pages that returned 404 are not cited.',
    'L')
add('rowcounts', 'INV',
    'Inventory row counts for the config module `build_sdp_inventory.py`: (a) 15, (b) 24, (c) 12, (d) 13, (e) 16, (f) 7 = 87 (matches BR targets); check_drafts reports 0 errors with `--headers` over both column files.',
    'INV-RN row counts',
    'a',
    'Report to main/xlsx-writer for the config; any row added or dropped by {unreadguides}, {invlimcov} changes the asserted counts.',
    'L')
add('emptycell', 'INV',
    'Block (c) records "No: the Can Reverse cell is empty [Documented]" and "No: the Referential Integrity cell is empty [Documented]" for 10 and 8 transformations: reading an empty table cell as "No" is an inference.',
    'INV(c) Reversible column 10 cells, Referential integrity column 8 cells',
    'a',
    'Relabel [Inferred] (premise: empty cell in the docs table) or state the cell and the table header without "No". Also re-match "HMAC-SHA-256" ({hashfmt}).',
    'M')
add('procfmt', 'INV',
    'Process language and first-person wording inside deliverable cells and the (b) intro note: "(my count of ...)" in 27 places, "Group boundaries are my own", "this sheet", "read-only rule", "exploration note only", "(not read, so no column is proposed)".',
    'INV(a) intro and rows, INV(b) intro and 27 count cells, INV(d) console, python-dlp, S3/JDBC and Model Armor advanced rows; INV scope paragraph ("Counts that are mine")',
    'a',
    'README section 5/7: finals contain no process language; the (b) intro becomes a merged note on the sheet. Rewrite as "count by rule X" at P6.',
    'M')
add('brackets', 'INV',
    'Non-label bracket pair `[grpc]` in "google-api-core[grpc]" and a self-referential label "[Documented] (this sheet)" (templates are rows in block (a)).',
    'INV(d) Python client row (Notes), Model Armor advanced mode row (Notes)',
    'a',
    'Rewrite without brackets (as the Sentinel precedent did for its bracket phrase) and drop the self-reference label.',
    'L')
add('absdoc', 'INV',
    'Absence claims labelled [Documented]: "no evaluation method is listed on the resource page or in the REST root [Documented]" and "the Python client ... no evaluation method [Documented: repo ...]".',
    'INV(a) content policies row (Method or resource cell); A SD1 R4 (client create_content_policy bullet)',
    'a',
    'README section 3 rule 2. The positive facts (methods listed) are [Documented]; the absence is [Not disclosed] naming the pages checked and the client version. For code surface questions BR allows the repo label (R007 item 4), so the repo bullet may stay if it says only what the file contains.',
    'M')

# ---------------------------------------------------------------- terms (c)
add('custdata', 'TERMS',
    'Customer-data terms: whether content sent to the API can be used by Google beyond serving the request (training, product improvement); docs say only "Request data is encrypted in transit and is not stored". Terms pages were not read.',
    'A SD1 R8 #12; A SD3 R8 #10; B SD4 R8 #9; B SD5 R8 #13; B SD6 R8 #13; INV(f) data handling row ([TBV]); BR G10',
    'c',
    'Google Cloud terms for SDP: the Service Specific Terms and Data Processing terms are not product docs; read at P5 if the user allows them as sources, else keep [To be verified]. Bears on sending real PII or explicit images to the service.',
    'M')
add('benchterms', 'TERMS',
    '(Suggested, not in drafts.) Whether Google Cloud terms or acceptable-use policy restrict benchmarking and publishing results of the service, or sending sexually explicit and violent test images to image safety classification.',
    'not in drafts; relevant to B SD6 R7 ("lawful, approved image set") and R8 #13, and to any report of Table 3 results',
    'c',
    'Google Cloud Service Specific Terms, Acceptable Use Policy and Generative AI/Vertex terms where relevant; user to confirm acceptable test data.',
    'M')
add('demodata', 'TERMS',
    'Data handling of the web-based demo app (`cloud.google.com/dlp/demo`): what it does with entered text is unknown.',
    'INV(d) console, gcloud and web demo row ([TBV]); INV-RN uncertain bullet 2; A SD1 R7 (web demo bullet)',
    'c',
    'Demo page terms or privacy notice; do not exercise (read-only rule). A SD1 R7 mentions the demo as a test aid, so the caveat matters.',
    'L')
add('geedition', 'TERMS',
    'Gemini Enterprise content-policy availability: "all editions except Business", no extra cost stated, global/EU/US regions only; relevant to who can test SD7.',
    'INV(d) Gemini Enterprise row; INV(e) content-policy row; B SD5 R4 / SD6 R4 (cross-reference bullets)',
    'c',
    'Gemini Enterprise docs (not SDP docs) and its pricing/edition page; needed only if {sd7} goes to a column or {cptest} is pursued.',
    'L')

# ---------------------------------------------------------------- format and process
add('rnmissing', 'PROC',
    'No `## Reviewer notes` section exists in sdp_cols_a.md or sdp_cols_b.md (README section 7 item 2 requires one; the drafters\' QUESTIONS blocks were lost with the previous session). Uncertainties were harvested from R8 bullets, labels and in-bullet conflict statements instead; INV-RN is intact.',
    'A, B (end of file); INV-RN',
    'a',
    'No action beyond this triage: the finals carry no Reviewer notes anyway. P6 change log should cite this triage for the conflicts list; if a drafter re-adds notes, diff them against section "Contradictions" below. Because the notes are missing, it is unrecorded whether any fact in A or B came from a summarising fetch (INV-RN states none for the inventory); ask the drafters or re-match quotes at P7.',
    'L')
add('citefmt', 'PROC',
    'Inconsistent code citations: A writes `google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:3175 "quoted text"`; B writes `dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2989` (shorter path, usually no quoted line). README section 3 rule 7: code quotes are single lines cited file@ref:line.',
    'A SD1 to SD3 (repo-label bullets, 25); B SD4 to SD6 (repo-label bullets, 32)',
    'a',
    'Normalise at P6 to one form (suggest A\'s: full path from the package root plus the quoted line); line numbers should be re-matched at the tag (clone at /tmp per R013).',
    'M')
add('premise', 'PROC',
    '[Inferred] bullets in B never use the "(premise: ...)" wording that A uses (A: 33 of 43 Inferred bullets name a premise; B: 0 of 48, premise sits inline in "so"/"because"). README section 3: state the premise in the bullet.',
    'B SD4 to SD6 (all [Inferred] bullets); A SD1 R7 and SD3 R4 R7 (10 without)',
    'a',
    'Style only; add "(premise: ...)" where the reasoning step is not obvious (B SD4 R3 #41, R6 #127, B SD5 R6 #306, B SD6 R3).',
    'L')

# ====================================================================== build
keys = {}
for n, it in enumerate(I, 1):
    keys[it['key']] = 'T%d' % n
def sub(s):
    return re.sub(r'\{(\w+)\}', lambda m: keys[m.group(1)], s)

rows = []
for n, it in enumerate(I, 1):
    rows.append('| T%d | (%s) %s | %s | %s | %s | %s |' % (n, it['tag'], sub(it['item']), sub(it['loc']), it['cls'], sub(it['src']), it['prio']))

cnt = collections.Counter((it['cls'], it['prio']) for it in I)
cls_tot = collections.Counter(it['cls'] for it in I)
pr_tot = collections.Counter(it['prio'] for it in I)
Hs = [(n, it) for n, it in enumerate(I, 1) if it['prio'] == 'H']
open('/home/user/guardrail_research/benchtest/scratchpad/triager/sdp_rows.md', 'w', encoding='utf-8').write('\n'.join(rows) + '\n')
import json
json.dump(dict(keys=keys, cls=dict(cls_tot), prio=dict(pr_tot), cp={f'{k[0]}{k[1]}': v for k, v in cnt.items()}, total=len(I), H=[(f'T{n}', it['key'], it['cls']) for n, it in Hs]),
          open('/home/user/guardrail_research/benchtest/scratchpad/triager/sdp_counts.json', 'w'), indent=1)
print(len(I), dict(cls_tot), dict(pr_tot))
print({k: v for k, v in sorted(cnt.items())})
