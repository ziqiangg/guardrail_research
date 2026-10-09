# sdp P10 diagram review: benchtest/diagrams/sdp-explained.html (commit 3930aea)

- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-09.
- Sources of truth: benchtest/drafts/sdp_two_level.md, benchtest/drafts/sdp_inventory_final.md. Rulings read: R012, R018, R023, R025.
- Renders: benchtest/scratchpad/verifier/sdp_diagram/sdp_{light,dark}_{1280,375}.png (gitignored), script render.py in the same folder.
- URL results: benchtest/scratchpad/verifier/sdp_diagram/url_check.txt.

## Verdict: PASS WITH FIXES (3 required fixes)

The page is structurally clean, renders well in both themes, and almost every claim traces to the drafts. There are three factual or consistency errors, each fixable in one line:
1. A date-shifting claim that the drafts and the source contradict.
2. A detector grouping that the page attributes to Google but that is ours.
3. The overview says "personal data only" for documents, which contradicts diagram 10 and the scorecard.

## 1. Required fixes

**RF1. Rail 4 "Good to know" (line 460): the date-shifting claim contradicts the drafts and the source.**
- Problem: the page says "Bucketing and date shifting are offered, but Google's samples show them on table fields only".
- The drafts disagree:
  - SD3 R1 Summary: "one sample also date-shifts a plain string".
  - SD3 R4 Detail: "The Go date-shift sample applies `dateShiftConfig` inside an infoType transformation to a plain string item".
  - The R8 open item covers bucketing and time extraction on free text.
- Source check: on the transformations-reference page, the Go sample comments read `input := "2016-01-10"` and `Will print "2016-01-09"`, and the item is `ContentItem_Value{Value: input}`, a plain string. Result: MISMATCH for the page.
- Replace:
  `Bucketing and date shifting are offered, but Google's samples show them on table fields only, so use on free text is to be verified.`
- With:
  `Bucketing and time extraction are offered, but Google's samples show them on tables only, so use on free text is to be verified; one sample does shift a date in a plain string.`

**RF2. Detector table, "Other countries" row (line 370): the grouping is attributed to Google, but it is ours.**
- Problem: the cell says "grouped by region in Google's reference".
- The inventory (b) block note says the group boundaries are the drafter's: "the Location column for the country groups".
- The reference page lists country infoTypes by country through a Location filter. It has no regional grouping: a grep of the read page finds no region headings.
- Replace:
  `National IDs, tax and health numbers, grouped by region in Google's reference`
- With:
  `National IDs, tax and health numbers, listed by country in Google's reference`

**RF3. Overview map (lines 132, 174, 202): "personal data only" contradicts diagram 10 and the scorecard.**
- Problem: the overview says that documents are checked for "personal data only".
- Diagram 10 says "personal data and keys". The scorecard says "Personal data and secrets in any passage or file".
- SD1 R3 says that the same detectors, secrets included, apply to retrieved text.
- Replace these three strings:
  - aria-label: `Documents fetched for the AI model can be checked for personal data only, and actions` becomes `Documents fetched for the AI model can be checked for personal data and keys but not for hidden instructions, and actions`
  - `.ts` at x=435 y=82: `personal data only` becomes `personal data and keys`
  - figcaption: `and can check passages from your documents for personal data only.` becomes `and can check passages from your documents for personal data and keys, but not for hidden instructions.`

## 2. Optional suggestions

- **O1. Rail 7 "Good to know" (line 600): the wording is stronger than the drafts.**
  - The page says "No Google page describes a round trip through an AI model".
  - SD4 R1 is scoped: "no LLM round trip is described on the pages cited for this column".
  - Suggested wording: "None of the Google pages we read describes a round trip through an AI model". Rail 10 ("No Google page describes checking retrieved passages") and the scorecard Retrieval row could get the same scoping. These are within the README's stock-phrase style, so this is optional.
- **O2. Detector table, "Worldwide IDs" row: "vehicle number" is ambiguous in Singapore.**
  - In Singapore usage, "vehicle number" means a licence plate. The detector is VEHICLE_IDENTIFICATION_NUMBER.
  - Suggest "vehicle identification number (VIN)".
- **O3. Detector table, "Pictures" row: the list names 7 objects, but the count of 11 includes 8 objects.**
  - OBJECT_TYPE/PERSON (a human figure) is missing.
  - Suggest adding "person" to the parenthesis, so that the list matches the count.
- **O4. Rail 3 example: "Two findings…" is stated as a result.**
  - S1234567D passes the NRIC check-letter rule (we computed D), so the claim is plausible.
  - The drafts warn that sample data which fails checks is not reported. "Expected: two findings…" would be safer.
- **O5. Header eyebrow: "formerly Cloud DLP" is neither a version nor a status (README section 2).**
  - This is acceptable as a descriptor; the Llama Guard eyebrow lists models in the same way.
  - Leave as is, or add a status only if the drafts give one. They give no overall launch stage.
- **O6. Limits item 6: the bold lead ends in a colon ("Its docs disagree in places:"), not a sentence.**
  - Suggest "Its docs disagree in places." followed by "They differ on which detectors…".

## 3. Points main asked to judge

**1. Scorecard calls**
- **Output = Yes with an "our reading" hedge: CONFIRM.**
  - SD1/SD3/SD4 R3 make the direction-agnostic call [Inferred].
  - SD6 R3 documents AI-generated images as an expected input, which is the response-side case.
  - It follows the Presidio page precedent: "No Presidio page shows it, so that is our reading".
- **Retrieval = Partly: CONFIRM.**
  - The drafts document file inputs. SD1 R3 says a PDF byte item is inspected via content.inspect [Documented]. SD5 R2 gives the use case "uploaded PDF or image attachments before processing in downstream workflows".
  - The data-path reading is [Inferred] in SD1 R3.
  - Indirect injection is uncovered: no such detector is named.
  - Note for main (cross-page): Sentinel scored Retrieval "No" on a similar "accepts any text, nothing official describes this" basis. The difference here is the documented file and attachment use. See Q1.
- **Execution = No: CONFIRM (defensible).**
  - The drafts give tool inputs and outputs exactly the same [Inferred] basis as retrieved text (SD1 R3: "prompts, responses, retrieved text, tool inputs and tool outputs").
  - Unlike retrieval, nothing tool-specific is documented.
  - Sentinel's page also says No.
  - Presidio's "Partly" rested on documented JSON and table masking for tool data, which has no SDP equivalent in the drafts.
  - The Why text states the gap honestly.
- **Image safety rail (diagram 9) = Partly: CONFIRM.**
  - SD6 R2: only three categories are listed. The absence of hate symbols, self-harm, weapons and child safety is [Not disclosed].
  - Google: "Don't rely solely on these classifiers…".
  - The scorecard Images row = Yes, with the Partly explained in the text. This is consistent.

**2. Detector-group counts: the sums are right.**
- Recount from the sdp_inventory_final.md (b) Count cells:
  - Other countries 125 = US 15 + Canada 7 + UK/IE 11 + W/S Europe 28 + N Europe 6 + E Europe/C Asia/ME/Africa 16 + East Asia 16 + S/SE Asia/Oceania 14 + Latin America 12.
  - Documents and source code 37 = context 8 + document kinds 13 + source code 16.
  - Pictures 11 = objects 8 + image context 3.
  - The global rows (9, 5, 12, 2, 13, 10, 8, 21, 6, 2) match one for one.
- Grand total: 88 + 125 + 37 + 11 = 261, which equals the [Inferred] 261 in SD1 R2 and inventory (f).
- Labelling: "by our count", "the counts are ours" and "Google gives no total" are acceptable and keep the [Inferred] hedge.
- The one problem is the region-grouping attribution (RF2).

**3. Four-column zone diagram and comparison table: no untraceable non-SDP facts.**
- The NeMo, Llama Guard and Sentinel cells in the table match sentinel-explained.html lines 265-272 word for word.
- The zone-diagram labels are abridged from Sentinel's diagram 1:
  - LionGuard and prompt attack become "Harm and attack".
  - Off-topic and leakage become "Off-topic, leakage".
  - Refusal and AWS checks become "Refusal, AWS checks".
  - "gives: safe or unsafe" drops "+ category", which is acceptable.
- "Only NeMo acts on a result" is Sentinel's own figcaption claim.
- The NeMo cross-references are correct against nemo-rails-explained.html: diagram 4 is personal-data masking on output, diagram 5 is masking on retrieved passages, and diagram 8 is the check before an action runs.
- No integration between SDP and NeMo, Llama Guard or Sentinel is claimed.
- These facts trace to the sibling pages, not to the SDP drafts, which README section 9 (cross-references) allows.

**4. Phone width (known shared issue, not counted as a fix)**
- At 375 px, the scrollWidth is 628 in both themes.
- The overflowing elements are header, h1, legend, sections and eyebrows (from the base CSS). This is the same as the Sentinel page.
- At 1280 px there is no overflow.

**5. URLs: 31 of 31 return 200.**
- The github.com blob link (dlp.py at google-cloud-dlp-v3.40.0) returns 200 directly; the raw.githubusercontent.com equivalent also returns 200.
- fonts.googleapis.com was not requested.
- All 31 footer URLs appear in the drafts.

**6. Workbook tab:** the page does not name the workbook tab, so there is nothing to check.

**AUP (R025):** limits item 8 says only that the AUP "bars illegal content" and that published results need replication information. Both trace to SD6 R7 and R8. The page does not mention the reverse-engineering or testing clause, so it is consistent with main's ruling.

## 4. Checklist (README section 11)

| Item | Result |
|---|---|
| CSS lines 6-109 identical to Sentinel; line 5 rewritten; no extra CSS block (none needed) | PASS (diff empty) |
| Fragment format; no doctype, lang, viewport, JS or images | PASS |
| Title, h1 and eyebrow | PASS (eyebrow descriptor, see O5) |
| Legend lists exactly the roles used (gate, dev, pass, stop, edit, part, na) | PASS |
| dev only on app-owned boxes; .part and .na match their pills | PASS |
| SVG viewBox, role and aria-label; no fill, stroke or style attributes | PASS (12 SVGs) |
| Marker ids unique, all resolve, none unused | PASS (21 markers) |
| Section order and stage numbers (1, 2, extras, 2b, 3); h3 sequence 1-10; "diagram N" references | PASS |
| Scorecard: five checkpoints in NeMo order plus Images and Monitoring, each with a pill and a Why | PASS (RF3 aligns the overview with it) |
| Limits: 8 items, each with a bold lead | PASS (O6) |
| Every claim traces to the drafts | FAIL until RF1 and RF2 are fixed (RF3 is internal consistency) |
| Voice: British spelling, "AI model", "personal data" | PASS |
| Footer mirrors the drafts' URLs | PASS |
| Renders in light and dark at 1280 and 375; no clipped box text | PASS (automated check found 0 text-overflow issues) |
| No horizontal overflow | Known shared issue at 375 (628 px), not counted |
| Looks like a sibling of Sentinel | PASS |

## 5. Source spot-checks (cached official pages, read 2026-10-09)

| # | Claim on page | Page | Result |
|---|---|---|---|
| 1 | 'not a perfectly accurate detection method' | concepts-infotypes | MATCH |
| 2 | FPE 'can run very slowly' | transformations-reference | MATCH |
| 3 | 'primarily trained and evaluated on real-world images' | concepts-image-redaction | MATCH |
| 4 | 'Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications.' | concepts-image-redaction (line-wrapped) | MATCH |
| 5 | Very likely = 'many strong signals' | likelihood | MATCH |
| 6 | Image-safety redaction covers the entire image | concepts-image-redaction | MATCH |
| 7 | The PASSPORT country list includes Singapore | infotypes-reference ("Russia, Singapore, Spain") | MATCH |
| 8 | Date-shift samples on table fields only | transformations-reference (the Go sample uses a plain string) | MISMATCH, see RF1 |
| 9 | Country detectors "grouped by region" in Google's reference | infotypes-reference (no region headings) | MISMATCH, see RF2 |
| 10 | Detector total of about 261 by our count | inventory (b) recount | MATCH (sums) |

Tally: 8 MATCH, 2 MISMATCH, 0 UNVERIFIABLE.
