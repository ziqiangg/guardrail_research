# groups_v3.md (sheet 4 regroup): fresh verifier review

Date of checks: 2026-10-11. Reviewer: gr-verifier (did not draft any part of groups_v3.md). File reviewed: benchtest/drafts/groups_v3.md as at commit 9054615 (unchanged in the working tree).

Inputs read:
- CLAUDE.md, drafts/README.md, groups_v2.md (format precedent), the docx section 4 (python-docx extraction: four criteria, the two example groups and the 8-column template).
- Rulings R002, R006, R025, R032, R037 in full; main's groups_v3 row in scratchpad/main/queue.md (marker reword to "Single-product: no comparator among the ten products yet"; C7 one group; multi-product = members from 2 or more different products; SDP AUP already recorded in SD6).
- Workbook sheet 3, columns E to BN, rows 3 to 21, dumped read-only to scratchpad/verifier/groups/sheet3.json; inventory and evaluation sheets 3c, 3g, 3k, 3n read where cited; *_inventory_final.md headings for every "3x (letter) title" reference.
- Finals: purplellama_two_level.md (PL4, PL6 for C14), cloak_two_level.md (Presidio links), sdp_inventory_final.md (limits).

Scripts:
- benchtest/scratchpad/grouper/check_v3.py (grouper's): 0 errors, 2 informational warnings. Output: scratchpad/verifier/groups/check_v3_out.txt.
- benchtest/scratchpad/verifier/groups/verify_groups_v3.py (independent, written for this review; does not reuse check_v3.py): 18 problems, all the same finding (marker text, Required fix 1); everything else clean. Output: scratchpad/verifier/groups/verify_out.txt.

## Verdict: PASS WITH FIXES

The structure, coverage and format are sound: 62 of 62 columns placed, accounting table and totals match the group table, 8 template columns, 802 bullets with none over 12 words, Refs lines on every text cell, C-IDs in order, multi-product band before single-product band, every multi-product group spans at least two products. Eleven required fixes remain. One is structural: C14 does not meet the docx "same ground truth" test on the sheet-3 evidence and should be split (Required fix 2). One applies main's marker ruling, which the draft predates (Required fix 1). The rest correct facts or ticks that the cited cells do not support.

## Keep / split / move verdicts on the judgement calls

| Call | Verdict | Basis (sheet 3) |
|---|---|---|
| BI and BK in C3/C4 | KEEP (borderline for BK) | Both are deterministic rules: BI R1, R2 (five fixed patterns; BI R8: "the code takes no pattern argument"), BK R1 (U+E0000 to U+E007F, score 0.0 or 1.0, BK R4). The docx tests are met only if the authored rule set given to N, AM, AO, BM and E includes BI's and BK's patterns; C3 says so ("BI, BK rules could be re-expressed as regex"). BK is a single-threat detector (hidden text, attached to tool messages in Meta's test, BK R3); grouping it is by mechanism, not threat. Acceptable under the four criteria. Optional 5 asks for one more caveat. |
| AN and AP in C15 | KEEP | AN R1, R3: content item can be "a string (value), a table"; up to 50,000 table values. AP R1: "text stored in container structures such as tables"; AP R3: record transformations act on tables. Same inputs, cell-level truth, comparable metrics with AL (AL R4, R5). |
| AS with X in C13 | KEEP, with a ground-truth caveat (Required fix 9) | Inputs and architecture fit (X R6, AS R3, AS R6). Ground truth is weaker than the ✓ says: X labels the hazard of an image-plus-text request under S1 to S13 (X R2; V R2 lists S1 Violent Crimes, S12 Sexual Content), and X's own test plan expects "Harmful-looking image + benign question" to "show ambiguity" (X R7). AS labels what the image depicts (AS R1, AS R2: "violent or gory content either real or fictionalized"). The overlap is approximate, not shared. |
| O with BH/BJ in C14 | SPLIT (Required fix 2) | O R2: "Exploit strings in generated output"; O R4: rules code (import_shells, import_networking), sqli, template, xss. BJ R2 Summary: "Insecure coding practices, not exploitable vulnerabilities". The draft's own ✓ rests on an "overlap subset still to confirm". Checked in purplellama_two_level.md: command injection is documented (BJ R2: potential-command-injection, CWE-78, C rules); SQL injection appears only as a docs example in BH R3 Detail ("if SQL injection risk is detected, the patch is rejected"); no XSS rule or CWE-79 appears in sheet 3 or the purplellama finals. Same-ground-truth is not met. |
| AW, BE, BF in C11 | KEEP, with a caveat (Required fix 10) | AW R3: response, tool output, MCP tools/call responses and grounding data. BE R3: "user inputs and untrusted content such as web data"; BF R3: defaults scan USER and TOOL. But BE R3 Detail: "Scanning model responses with Prompt Guard 2: no page describes it [Not disclosed]". The "model output" part of the group is AW alone. |
| C5/C6 reversible split | KEEP | AJ, AQ, BN are one column each (R002 library rule; R037 CK3), but each product exposes separate encrypt and restore operations (AJ R3 Deanonymize; AQ separate re-identify method, AQ R8; BN R3 "Encrypt on the way out, decrypt on the way back"). Inputs (raw text versus tokenised replies) and ground truth (no residual value versus exact restore) differ, so the docx criteria support two groups. This is not the same case as C7 (main's ruling: images have no direction and no input difference). Optional 2 suggests citing the docx criteria rather than "R002 reading". |

## Required fixes

1. **Marker text (main ruling, queue.md groups_v3 Q1).** Location: column H, first bullet, rows C16 to C33 (18 rows); section D2 "Marker bullet"; grouper's check_v3.py MARKER constant (grouper scratch, not the draft).
   Problem: every single-product row still reads "• Single-product: no comparator among NeMo / Llama Guard / Sentinel yet", followed by "• Also checked against the later columns (AH to BN): no comparator". Main has ruled the new wording; the second bullet then becomes redundant (and reads oddly in C30 to C33, whose own columns are in AH to BN).
   Replace in all 18 rows: "• Single-product: no comparator among NeMo / Llama Guard / Sentinel yet<br>• Also checked against the later columns (AH to BN): no comparator<br>" with "• Single-product: no comparator among the ten products yet<br>".
   Replace the D2 bullet beginning "Marker bullet: the single-product marker is kept exactly as in v2." with: "Marker bullet: reworded to Single-product: no comparator among the ten products yet (main ruling, queue.md groups_v3); the build matches only the prefix Single-product:, so the coverage panel is unaffected."
   Then set MARKER in benchtest/scratchpad/grouper/check_v3.py to "• Single-product: no comparator among the ten products yet" and re-run it.

2. **Split C14 (docx criterion 2 not met).** Location: table row C14, rationale C14, sections C, D1, E2 and every cross-reference.
   Problem: see the verdict table. The ✓ on ground truth is unsupported: O targets exploit payloads (O R2), Code Shield targets insecure coding practice and says it is "not exploitable vulnerabilities" (BJ R2). Of the three "overlap classes to confirm", only command execution is documented on both sides; SQL injection is a docs example only (BH R3 Detail); XSS has no Code Shield evidence. Under main's ruling BH and BJ on their own are one product (Purple Llama), so the split gives two single-product rows.
   Do:
   (a) Single-product row "Output-level injection detection" with O only: restore groups_v2.md row C12 cells verbatim, with the Required fix 1 marker and Refs lines added where v2 had none. Rationale line: "Why it has no partner ✗: BH and BJ: ground truth is insecure coding practice with CWE ids, not exploit payloads in output (O R2, BJ R2); Code Shield shows SQL injection only as a docs example (BH R3) and no XSS rule."
   (b) Single-product row "Output-level insecure-code detection in model responses" with "BH: LlamaFirewall: Output-level insecure-code detection (CodeShield scanner); BJ: Code Shield: Output-level insecure-code detection (LLM-generated code)", cells:
   - Test inputs: "• Suggested: scripted model outputs with insecure and benign code answers<br>• Possible seeds: CyberSecEval code prompts<br>• Benign code answers would be needed to test false positives<br>Refs: BH R7, BJ R7, 3k Reuse"
   - Ground truth: "• Suggested: per output, insecure or benign, with CWE class<br>• Independent labels would be needed; CyberSecEval ground truth is Code Shield itself<br>Refs: BH R2, BJ R2, 3k Reuse"
   - Outputs: "• BH: block or allow, score 1.0 or 0.0, issue list in reason<br>• BJ: insecure flag, issue list, block, warn or ignore<br>• Matched rule, CWE and line where given<br>• Latency; error<br>Refs: BH R5, BJ R5"
   - Metrics: "• Detection rate per CWE class; false-positive rate on benign code<br>• Agreement between the scanner and the library on the same text<br>• Latency by language<br>Refs: BH R5, BJ R5"
   - Architecture: "• Suggested harness: scripted outputs, adapters, recorder, evaluator<br>• BH: llamafirewall with codeshield and Semgrep; BJ: pip codeshield and Semgrep<br>• No key, model or gated access for BH or BJ<br>Refs: BH R7, BJ R7, 3j (d) Code Shield language and analyzer matrix"
   - Material differences: "• Single-product: no comparator among the ten products yet<br>• BH runs the BJ engine: one engine through two surfaces<br>• BH scans whole messages; BJ takes a code string<br>• BH and BJ language lists conflict: seven or eight<br>• Code Shield is not a taint-flow analyser; Semgrep licence recorded<br>• NeMo O checked: it flags payloads, not coding practice<br>Refs: BH R4, BH R3, BJ R3, BJ R2, BJ R8, O R2, 3j (f) licences, gating and terms"
   - Rationale: "Why it has no partner ✗: O: ground truth is exploit payloads, not insecure coding practice (O R2, BJ R2); BH and BJ are one engine through two Purple Llama surfaces (BH R4)."
   (c) Renumber: C15 becomes C14; the single-product band grows to 20 rows (C15 to C34). Update every C-number cross-reference (C4 and C10 rationale "C14", C25 rationale "BH and BJ (C14)", C1 and E1 "C15", all C16 to C33 references), section C (O, BH, BJ rows), D1 (v2 C12 row: "Single; renumbered"; add a "new" row for the BH, BJ single row), E2 Semgrep row, and the totals: "Totals: 62 functions (E to BN); 0 in no group; 23 in more than one group; 34 groups (14 multi-product, 20 single-product)." Also D intro ("v3 has 34 groups (14 multi-product, 20 single-product)"), section A band sentence ("C1 to C14 ... C15 to C34") and E3 ("34 rows, 14 comparison groups"). Regenerating with the grouper's gen_v3.py is the safe route; re-run both check scripts afterwards.
   If main or the user prefers to keep C14, the minimum alternative is to change the rationale to "Ground truth ✗ (to confirm): ..." and flag the row as provisional; a group with a ✗ on a docx criterion should not stand in the comparison band, so the split is the recommended fix.

3. **C3 hotword bullet is wrong for BM.** Location: C3, column H, bullet 4.
   Problem: "AM and AO add context or hotword rules; the others do not". BM R4 Detail: the API offers "custom recognisers (regex patterns, context words)"; BM R6 Summary: "Context words and per-pattern scores are API only."
   Replace with: "• AM, AO and BM (API only) add context or hotword rules", and add "BM R6" to that cell's Refs line.

4. **C3 rationale: AM does need a model.** Location: section B, C3, "Minimum architecture ✓" line.
   Problem: "no model is needed for N, AM, BI or BK". AM R7: "pip install presidio-analyzer and the English spaCy model"; C3's own architecture cell says "AM: local Analyzer with spaCy model".
   Replace "no model is needed for N, AM, BI or BK (N R7, AM R7, BI R7, BK R7, AO R7)" with "no detection model is needed for N, BI or BK, and AM loads a spaCy model with its Analyzer (N R7, AM R7, BI R7, BK R7, AO R7)".

5. **Cloak independence from Presidio is undisclosed.** Locations: E1 "Reasons for C1" and "Cautions"; C1 column H; C5 column H.
   Problem: E1 counts "at least four independent engines: AWS, Presidio, SDP, Cloak". Sheet 3 BL R4 Detail: Cloak "shares tag names ... with Presidio's catalogue, which could mean reuse of Presidio recognisers [Inferred]" and "No GovTech page says Cloak is built on Presidio [Not disclosed]". BN R4 Detail: "Whether Cloak's Encrypt is Presidio's encrypt operator is not stated ... the Encrypt page's wording and AES-CBC point that way [Inferred]".
   Replace in E1 "(9 functions on at least four independent engines: AWS, Presidio, SDP, Cloak)" with "(9 functions, joint widest with C2, on three documented independent engines, AWS, Presidio and SDP; whether Cloak reuses Presidio is undisclosed, BL R4)".
   Append to the E1 Cautions sentence after "K/AH backends": "; BL may reuse Presidio recognisers (BL R4, inferred)".
   C1 column H: after "• Shared backends, not independent: K-AH, AF-E, AX-AN" insert "• BL may reuse Presidio recognisers; GovTech does not say" and add "BL R4" to the Refs line.
   C5 column H: after "• Keys differ: ..." insert "• BN Encrypt may be Presidio's encrypt operator; GovTech does not say" and add "BN R4" to the Refs line.

6. **E1 "no taxonomy judgement" and "feeds C3".** Location: E1 "Reasons for C1".
   Problem: "the ground truth is objective (entity type and span) with no taxonomy judgement" contradicts C1's own ground-truth cell ("Entity lists differ: a harmonised common subset could be scored"). "the same labelled data feeds C2, C3, C5, C6, C7 and C15": C3's ground truth is the authored rule set, not PII types (C1 rationale, Checked and left out). "feeds" also reads as a decided plan (R032).
   Replace "the ground truth is objective (entity type and span) with no taxonomy judgement" with "the ground truth (entity type and span) needs a harmonised entity subset but less taxonomy judgement than the harmful-content groups".
   Replace "the same labelled data feeds C2, C3, C5, C6, C7 and C15" with "the same labelled data could seed C2, C5, C6, C7 and C15".

7. **Line 3 overstates the R032 wording; two new bullets use "must".** Locations: intro paragraph (line 3); C10 column C bullet 4; C14 column C bullet 4 and column D bullet 2 (these move to the BH, BJ row under fix 2).
   Problem: line 3 says bench content in columns C to G "is worded as proposals (R032)", but the carried rows keep v2 wording such as "Around a reference Colang configuration we author" (C16), "Thresholds we set" (C18), "Triggered through flows we author" (C21). D2 says carried rows keep v2 wording, so line 3 is inaccurate. New rows say "Benign look-alikes must be added" and "Benign code answers must be added", "Independent labels are needed": decided-plan tone; 3k's own wording is "would need".
   Replace on line 3 "Bench content in columns C to G is worded as proposals (R032); nothing here decides the bench design." with "Bench content in new and changed rows (columns C to G) is worded as proposals (R032); rows carried from v2 keep their v2 wording (see D2). Nothing here decides the bench design."
   C10: "• Benign look-alikes must be added; Meta publishes none" becomes "• Benign look-alikes would be needed; Meta publishes none".
   C14 or its successor row: "• Benign code answers must be added to test false positives" becomes "• Benign code answers would be needed to test false positives"; "• Independent labels are needed; CyberSecEval ground truth is Code Shield itself" becomes "• Independent labels would be needed; CyberSecEval ground truth is Code Shield itself".

8. **AS acceptable-use item missing.** Locations: C13 column H; C13 rationale "Recorded open items"; E2 table.
   Problem: AS R7 and AS R8 record a Google Cloud AUP limit that bears on C13 test images ("bars illegal content including child sexual exploitation and non-consensual explicit imagery ... which test images are acceptable is decided in the bench design"). Main's ruling notes "SDP AUP already recorded (SD6)". C13 and E2 omit it.
   C13 column H: add "• Google AUP limits on explicit test images apply to AS" before "• AS accuracy and thresholds are open questions", and add "AS R7" to the Refs line.
   C13 rationale: replace "Recorded open items (listed, not decided): EU licence clause for X (X R8)." with "Recorded open items (listed, not decided): EU licence clause for X (X R8). Google Cloud AUP limits on explicit or violent test images for AS: which images are acceptable is open (AS R7, AS R8)."
   E2: add the row "| Google Cloud AUP limits on explicit or violent test images (not the testing clause) | AS R7, AS R8 | C13 |".

9. **C13 ground truth ✓ overstated.** Locations: C13 column H; C13 rationale "Ground truth ✓".
   Problem: see the verdict table (X R2, X R7, AS R1, AS R2).
   C13 column H: add after "• AS judges the whole image; X judges image and text together" the bullet "• X judges request hazard; AS judges what the image shows", and add "X R7" and "AS R1" to the Refs line.
   Rationale: replace "- Ground truth ✓: Safe or unsafe per image on a harmonised subset: sexual content and violence (X R2, AS R2)." with "- Ground truth ✓ (approximate): Safe or unsafe per image on a harmonised subset, sexual content and violence; X labels the hazard of the image-plus-text request and expects harmful-looking images with benign text to be ambiguous (X R2, X R7), while AS labels what the image depicts (AS R1, AS R2), so agreement on the subset is measured, not assumed."

10. **C11: BE and BF on model replies is undocumented.** Locations: C11 column H; C11 rationale "Test inputs ✓".
    Problem: the group and its ✓ cover "model replies" for all three members; BE R3 Detail says no page describes scanning model responses [Not disclosed], and BF R3 says the defaults scan USER and TOOL.
    C11 column H: add "• BE, BF on model replies: undocumented; Meta names user and tool text" after "• BE behaviour on tool and retrieved text is untested by Meta", and add "BE R3, BF R3" to the Refs line.
    Rationale: replace "(AW R3, BE R3, BF R3)." at the end of the Test inputs line with "; BE and BF on model replies is undocumented (BE R3), and BF defaults to user and tool roles (AW R3, BE R3, BF R3)."

11. **C31 ✗ reason is factually wrong.** Location: section B, C31, "Why it has no partner ✗".
    Problem: "No other column examines URLs (AZ R2)". BB R2 Summary: document screening "Targets safety violations, prompt injection, sensitive data and malicious URLs in a file's text"; BB R5: "Malicious URL positions exist only for plain text". BB is the same product, so the single-product verdict stands, but the reason is wrong.
    Replace with: "- Why it has no partner ✗: No other product's column checks link reputation (AZ R2); BB runs the same Model Armor URL filter on files (BB R2); C11 and C10 look at instruction text, not link reputation."

## Optional suggestions

1. C1 column E, bullet 3: "Score: AH 0 to 1; AN five levels; AF 0.0 or 1.0". AF R5 documents a 0 to 1 score; only the examples are 0.0 or 1.0 (AF R4 Detail, [Inferred] flag). Suggest "Score: AH 0 to 1; AN five levels; AF 0 to 1, seen 0.0 or 1.0" (12 words).
2. C6 rationale "Checked and left out": cite the docx criteria rather than "R002 reading: prompt side versus response side", e.g. "The encrypt side is C5: inputs and ground truth differ (docx section 4), and each product exposes separate encrypt and restore operations (AJ R3, AQ R8, BN R3)." The same sentence in D2 ("Input and output stay separate (R002) for ... tokenisation versus restore") could say "(docx criteria)".
3. AS output side: AS R3 says the same call scores "an image a model generated", and D2 says a function is listed "in each side it applies to, as R002 requires". The draft lists AS only in C13 and notes "AS on generated images has no comparator". Either add a sentence in D2 that main's C7 ruling (no direction flag, one group) is applied to AS too, or add a single-product row; see QUESTIONS Q2.
4. BC and C13: BC R2 Detail says visual scanning takes its detectors from the customer's SDP inspect template [Inferred], so a template naming the three IMAGE_TYPE/CONTEXT detectors could make BC an image-safety scanner. C13 "Checked and left out" says BC is "not safety". Suggest "BC: sensitive-data screening of images; image safety through an SDP template is inferred only (BC R2)".
5. C3 column H: add "• BK compares only if the others get the tag-block regex" (11 words) so the BK borderline is visible.
6. E1 last bullet: "A harmful-content group (C8) has the most members with probability outputs" is not supported as a superlative (C8: AA, BD, V if extracted; C10: AB, BE, BF). Suggest "C8 has several members with probability outputs (AA, BD, V if extracted)".
7. E2 row "Preview features: synthetic data only (R025 ruling 2)" sits under "open items (listed, not decided)" but is a user decision; mark it "(decided by the user, R025)". R025 names Model Armor Preview features; applying it to AR faces is a reading, worth saying.
8. C7 column H refs: "AK is beta" is in AK R1, not AK R4; add AK R1 to that Refs line.
9. C15 column H: "AL JSON support has no documented SDP counterpart" is not traceable to a cell (AN R1 lists string, table, bytes, conversation, batch). Suggest "No SDP column documents JSON input; AL does".
10. C15 rationale "Checked and left out": "BL, BB: file uploads are a different object (C30)". BL is in C1 and C2, not C30; suggest "BB: file uploads are a different object (C30); BL file input is not studied in its columns".
11. C28 "Why it has no partner": AG covers AWS prompt leakage (Standard tier, input side; AG R2). Adding "AG: input-side leakage attempts, not leaked output (AG R2)" would show it was checked.
12. C12 "Checked and left out": Z (custom-policy) could carry an off-topic category; one line saying why it was left out would close the question.
13. Carried NeMo rows: if main prefers rewording to the line-3 qualifier (fix 7), the "we author" and "our own" bullets in C16, C18 and C21 could become "a reference Colang configuration would be authored" and similar.

## 1. Criteria check per multi-product group (docx section 4)

| Group | Inputs | Ground truth | Metrics | Architecture | Note |
|---|---|---|---|---|---|
| C1 | ✓ supported | ✓ supported (harmonised subset) | ✓ | ✓ | fix 5 (BL backend) |
| C2 | ✓ | ✓ | ✓ | ✓ | |
| C3 | ✓ (if BI, BK patterns are in the authored set) | ✓ | ✓ | ✓ wording wrong for AM (fix 4) | fix 3 |
| C4 | ✓ | ✓ | ✓ | ✓ | |
| C5 | ✓ | ✓ | ✓ | ✓ | fix 5 (BN operator) |
| C6 | ✓ | ✓ (failure cases open, stated) | ✓ | ✓ | |
| C7 | ✓ | ✓ | ✓ | ✓ | main ruling: one group |
| C8 | ✓ | ✓ (binary; category mapping partial) | ✓ | ✓ | |
| C9 | ✓ | ✓ | ✓ | ✓ | |
| C10 | ✓ | ✓ (definitions differ, stated) | ✓ | ✓ | fix 7 |
| C11 | ✓ partly: BE, BF on model replies undocumented | ✓ | ✓ | ✓ | fix 10 |
| C12 | ✓ | ✓ | ✓ | ✓ | |
| C13 | ✓ | approximate only | ✓ | ✓ | fixes 8, 9 |
| C14 | ✓ | not supported | ✓ | ✓ | fix 2 (split) |
| C15 | ✓ | ✓ | ✓ | ✓ | |

Every ✓/✗ line in section B cites cells that exist (independent script: every "L Rn" resolves to a sheet-3 column; every "3x (letter) title" resolves to a heading in the matching *_inventory_final.md; every 3c, 3k, 3n reference names a real section). The content of the cited cells supports the ticks except where the table above says otherwise. Single-product ✗ reasons were read for all 18 rows; C31 is wrong (fix 11); C28 and C12 could name one more checked candidate (Optional 11, 12).

## 2. Coverage and accounting

- 62 function columns E to BN in sheet 3 row 3; all 62 appear in at least one group; none missing.
- 23 columns appear in more than one group (E, N, X, Z, AA, AF, AG, AH, AI, AJ, AM, AN, AO, AP, AQ, BD, BE, BF, BI, BK, BL, BM, BN).
- Section C header text equals sheet 3 row 3 for every column; group lists equal the group table; totals line equals the computed values (62, 0, 23, 33, 15, 18).
- Function entries in column B equal the sheet 3 headers (E carries the "(template example column)" suffix, as in v2).
- No header is a substring of another and none holds COUNTIF wildcards (both scripts), so the coverage panel logic described in E3 holds.
- Multi-product rule (main): every C1 to C15 row spans at least two products; C11 and C14 qualify through Model Armor and NeMo respectively. After fix 2 the BH, BJ row is single-product (one product, Purple Llama).

## 3. Format

- 8 columns, header identical to the docx template.
- 802 bullets, longest 12 words; every text cell ends with one Refs line; no ** or backticks; no pipe inside a cell.
- C-IDs C1 to C33 in order; multi-product rows before single-product rows; rationale titles equal table titles; rationale Functions lines equal table members.
- Carried rows: compared with groups_v2.md by difflib. Changes are exactly those logged in D2: 22 Refs lines added, renumbered cross-references (C24, C26, C27), two new input bullets (C25, C29), and the added second marker bullet. No unlogged change.
- Non-ASCII characters limited to • ✓ ✗ and dashes; no emoji; British spelling (product terms "recognizer", "Analyzer" follow Presidio's own names).

## 4. Wording (R032) and licence or terms items

- New rows use "Suggested", "Possible", "could". Exceptions: the two "must be added" bullets and one "are needed" (fix 7), and line 3's claim about carried rows (fix 7).
- Licence and terms items are listed as open, never decided: Cloak Terms 3.4.7 (C1 to C6), Google AUP testing clause (recorded in AT, AU, AV, AW, AZ, BA, BC; not in AN, AP, AX, AY, BB: confirmed by a search of all 62 columns for the clause text), Llama 4 policy and 700M MAU clause (BE R8, BF R8), Together terms (BG R8, BI R7), embedder terms (BD R8), EU clause (X R8), Semgrep and Code Shield terms. Missing: the AS acceptable-use item (fix 8). One decided item (R025 ruling 2) sits in the open list (Optional 7).
- Test-first suggestion (E1): worded as a suggestion. Reasons checked against the workbook: 9 members (true, joint with C2); "four independent engines" not supported (fix 5); "no taxonomy judgement" contradicted by C1 (fix 6); "three members need no account" supported (AH R7 "no account or key is needed"; AI R7 "no account or key"; K R4 "Presidio runs locally"); "feeds C3" not supported (fix 6). Alternative C10 figures (251 English, 1,004 translated, no harmless look-alikes) match 3k exactly.

## 5. Spot-checks of facts in bullets (25)

| # | Location | Claim | Sheet 3 or final, quote | Result |
|---|---|---|---|---|
| 1 | C1 E | AH 0 to 1; AN five levels; AF 0.0 or 1.0 | AH R5 "a 0 to 1 score"; AN R5 "one of five likelihood levels"; AF R5 "a 0 to 1 score", examples 1.0 and 0.0 | MATCH (AF loose, Optional 1) |
| 2 | C1 H | AX basic mode short, US-leaning fixed list | AX R2 "Basic mode: a short US-leaning list" | MATCH |
| 3 | C3 H | AO caps regex at 1000 | AO R6 "a regex length of 1000" | MATCH |
| 4 | C3 H | AM and AO add context or hotword rules; others do not | BM R6 "Context words and per-pattern scores are API only." | MISMATCH (fix 3) |
| 5 | C3 rationale | no model needed for AM | AM R7 "pip install presidio-analyzer and the English spaCy model" | MISMATCH (fix 4) |
| 6 | C5 H | AJ random vector per entity | AJ R4 "AES-CBC with a random initialisation vector per entity" | MATCH |
| 7 | C5 H | AQ docs disagree on AES-SIV length | AQ R4 "the docs disagree on whether the length is kept" | MATCH |
| 8 | C7 H | AK beta; BC Preview, us and eu only | AK R1 "The package is marked beta."; BC R1 "Preview, us and eu multi-regions only." | MATCH (ref is AK R1, Optional 8) |
| 9 | C7 H | AK thresholds differ, Python and REST | AK R5 "The score threshold is 0 in Python and 0.4 on the REST upload form." | MATCH |
| 10 | C8 D | AG five categories; AT four plus CSAM | AG R2 "hate, insults, sexual, violence and misconduct"; AT R2 "Four harm categories plus CSAM" | MATCH |
| 11 | C8 H | AG has no self-harm category | AG R2 Detail "The AWS docs list no self-harm category" | MATCH |
| 12 | C8 C | AT nine languages | AT R2 "The filters are tested in nine languages" | MATCH |
| 13 | C10 C | CyberSecEval 251 English injection cases | 3k "prompt_injection.json (251 English cases: 196 direct, 55 indirect ...)" | MATCH |
| 14 | C10 H | BE 512-token limit, eight evaluated languages | BE R6 "One string of up to 512 tokens."; BE R2 "the card lists eight evaluated languages" | MATCH |
| 15 | C10 H | F fails open; English-only heuristics | F R4 Detail "If the detector is unreachable the rail allows the request (fails open)"; F R2 Detail "Both heuristics are intended for English only" | MATCH |
| 16 | C11 H | AW three-word rule for responses unknown | AW R8 "whether the three-word rule applies to responses" | MATCH |
| 17 | C11 C | CyberSecEval 55 indirect cases | 3k "196 direct, 55 indirect" | MATCH |
| 18 | C13 G | AS request names the three detectors | AS R6 "Image context detectors have to be requested in the configuration" | MATCH |
| 19 | C14 H | O docs and code disagree on default action | O R8 Detail "the docs say it is required; the code defaults to reject" | MATCH |
| 20 | C14 C | overlap classes: SQL injection, command injection, XSS | O R4 sqli, xss, code rules; BJ R2 Detail CWE-78; BH R3 Detail SQL injection docs example only; no XSS in sheet 3 or purplellama_two_level.md | UNVERIFIABLE for Code Shield XSS (fix 2) |
| 21 | C15 G | SDP caps 0.5 MB and 50,000 table values | AN R6 "Requests are capped at 0.5 MB"; AN R6 Detail "Maximum number of table values, 50,000" | MATCH |
| 22 | C15 H | AL alpha (0.0.8) | AL R4 "Package version 0.0.8, marked alpha" | MATCH |
| 23 | C28 H | 0.95 guidance misses a 0.909 clear leak | AD R5 Detail "Sentinel docs example 0.909 is below 0.95 yet is a clear leak" | MATCH |
| 24 | C31 rationale | No other column examines URLs | BB R2 "malicious URLs in a file's text" | MISMATCH (fix 11) |
| 25 | E1 | four independent engines incl. Cloak | BL R4 Detail "could mean reuse of Presidio recognisers [Inferred]"; "No GovTech page says Cloak is built on Presidio [Not disclosed]" | MISMATCH (fix 5) |

Tally: 19 MATCH, 5 MISMATCH, 1 UNVERIFIABLE. Also checked and matching, not tabled: C30 "69 bytes to 4 MB" (BB R6), C31 "first 256 URLs; encoded URLs not decoded" (AZ R2), C12 "AC is English only" (AC R6), C25 "500 prompts in five attack types" (3k), C33 "default model listed as removed from Together serverless" (BG R8), C8 "BD ships no cut-off; AA no server threshold" (BD R5, AA R5), C2 "AY basic list may not apply to responses" (AY R2), C10 "AG is the aws/prompt_attack id" (AG R2 Detail), C4 "N output check has no exception path" (N R5).

## 6. URLs

groups_v3.md contains no URLs (grep for "http": 0). Nothing to curl.
