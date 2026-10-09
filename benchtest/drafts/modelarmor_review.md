# Model Armor workbook: fresh verifier review (P7)

Date of checks: 2026-10-09. Verifier: gr-verifier (did not draft, triage, resolve or merge). Inputs read: CLAUDE.md, drafts/README.md, gr-verifier definition, rulings R002, R011, R012, R013, R015, R017, R019, R020, queue.md resolved rows for modelarmor, lessons.md; modelarmor_brief.md (scope, headers, sources), modelarmor_changes.md (in full), modelarmor_summaries_preview.md (in full), modelarmor_two_level.md (all 90 Summaries; Detail of every changed Summary row and of every row named below), modelarmor_inventory_final.md (diffed cell by cell, blocks (a), (b), (d), (e) read where checked); modelarmor_resolutions_1.md and _2.md (headers, reports, T21, T44); modelarmor_triage.md (label hygiene section). Originals diffed: modelarmor_cols_a.md, modelarmor_cols_b.md, modelarmor_inventory.md. Format models: sentinel_review.md, lg_review.md. Scripts and page copies: benchtest/scratchpad/verifier/modelarmor/ (diff_cols_g.py, diff_inv.py, res_match.py, harvest_urls.py, show.py, html2text.py, pages/, gosrc/, url_check.txt). No file other than this one and that folder was written.

## Verdict: PASS WITH FIXES

The merge is faithful and well logged. 30 source spot-checks were made (plus 14 Go line references at the tag): 29 MATCH, 1 MISMATCH (a "no latency figure published" absence claim, contradicted by a Google Service Extensions page read verbatim for the first time in this review), 0 UNVERIFIABLE. Every substantive change found by difflib is in modelarmor_changes.md. No known-wrong string from the resolutions survives. The mechanical checks pass: check_drafts.py gives 0 errors and 0 warnings for both finals; there are 10 columns and 90 Summaries, none over its limit; inventory blocks are 10/15/16/20/16; the preview matches the final file exactly. All 59 URLs resolve: 45 return 200 directly and 14 github.com URLs return 403 through the proxy but resolve through raw files or `git ls-remote`.

There are 7 required fixes:

- 3 Summaries not entailed by their own row's Detail (6 rows);
- 1 stale process-language bullet (T21), now resolvable with a verbatim read;
- 1 wrong absence claim (latency);
- 1 judgement labelled Documented;
- 1 set of absence claims labelled To be verified or Documented.

None changes a number in a Summary. No Summary text needs to change.

## Required fixes

1. **MA1 R1 and MA2 R1: the CSAM caveat in the Summary is not entailed by the R1 Detail.** The new Summary sentence (T9) reads "A CSAM check is on by default but unavailable in limited-support locations with residency enforced." The R1 Detail carries only "This filter is applied by default and cannot be turned off." The feature-table fact sits in R2. README section 4 requires every Summary claim to be entailed by the same row's Detail.
   - In MA1 R1 and in MA2 R1, insert after the bullet `• CSAM: "This filter is applied by default and cannot be turned off." (overview, 2026-10-09) **[Documented]**`:
     `• With data residency enforcement on, the feature availability table lists CSAM support as "No" in all seven limited-support locations (asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2, northamerica-northeast2) (feature availability page, 2026-10-09) **[Documented]**`
   - The Summaries stay as they are (45 words each).

2. **MA5 R6 and MA6 R6: the over-limit clause in the Summary is not entailed by the R6 Detail.** Both Summaries say "Past 130,000 tokens a match still counts; no match gives a skipped check." That fact (T52) was placed only in R5 Detail. The MA6 R6 Detail has no over-limit bullet at all. The MA5 R6 Detail has only the 2025-07-28 SKIP_DETECTION history bullet.
   - In MA5 R6 and MA6 R6, insert after the "Token limit:" bullet:
     `• Over the 130,000-token limit a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, 2026-10-09) **[Documented]**`
   - I re-read this at source: "If a filter detects a match, it returns MATCH_FOUND. If a filter doesn't detect a match … exceeds the filter's token limit, the filter returns EXECUTION_SKIPPED".

3. **MA9 R4 and MA10 R4: the Summary leads are not entailed by the R4 Detail.**
   - **MA9 R4.** The lead "Text extraction, then the ordinary filters." has no R4 bullet. The merge removed only the "Extraction runs inside the managed service" clause (style 3g); the lead has the same problem. Insert as the first two R4 Detail bullets (copied from MA9 R1):
     `• Overview: "Model Armor can screen the following types of documents for safety, prompt injection and jailbreak attempts, sensitive data, and malicious URLs" (overview, 2026-10-09) **[Documented]**`
     `• The REST modality reference says the text modality will "sanitize text fields, and text extracted from rich text files (like PDFs, DOCs) and plain text files (like TXT)" (templates reference, 2026-10-09) **[Documented]**`
   - **MA10 R4.** "OCR plus advanced Sensitive Data Protection, in Preview" and "The service reads image text" have no R4 bullet: no R4 bullet states the OCR method or the Preview stage of image screening. Insert as the first two R4 Detail bullets (copied from MA10 R1):
     `• Method 2: "Optical character recognition (OCR): Screens the text within images." (overview, 2026-10-09) **[Documented]**`
     `• The overview and templates pages label the feature Preview, subject to the Pre-GA terms (overview and templates page, 2026-10-09) **[Documented]**`
   - The Summaries stay as they are (MA9 R4 25 words, MA10 R4 43 words).

4. **T21 Service Extensions bullet: process language, and the page has now been read verbatim.** The bullet sits in R4 of MA1, MA2, MA3, MA4, MA7 and MA8 (lines 93, 298, 502, 716, 1256, 1436) and in the INV(b) Service Extensions Status cell. It says "the Service Extensions configuration page returned no text through the raw fetch, so it is unread". That is process language, which README section 4 does not allow in finals. It is also no longer true.
   - **How I read the page.** `fetch_text.py` still returns an empty body. A plain `curl` GET of https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services returned 200 (174,862 bytes). I parsed it with a stdlib HTML parser (pages/se_google_services_parsed.txt). The page is "Configure an extension to call a Google service" and its footer reads "Last updated 2026-10-07 UTC". It carries no launch-stage banner and states no GA date. Its Model Armor section says the extension works "to application load balancers, including GKE Inference Gateway".
   - **Why not To be verified.** The Model Armor networking page links the Secure Web Proxy row to `/service-extensions/docs/configure-traffic-extensions`. That page also has no banner and does not mention Model Armor. The absence is therefore now a checked absence (README section 3 rule 2; R020 ruling 1).
   - **Columns.** In each of the six R4 locations, replace the bullet with:
     `• A GA date for load balancers other than GKE and for Secure Web Proxy (checked the release notes, the networking and integrations pages, and the Service Extensions guides "Configure an extension to call a Google service" and "Configure a traffic extension", neither of which carries a launch-stage label) **[Not disclosed]**`
   - **Inventory, Status cell.** In INV(b) row "Service Extensions on Cloud Load Balancing …", replace `GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN, NET and INT; the Service Extensions configuration page returned no text through the raw fetch, so it is unread)` with `GA date for other load balancers and Secure Web Proxy [Not disclosed] (checked RN, NET, INT, SEGS and SETE; neither Service Extensions page carries a launch-stage label)`.
   - **Inventory, Source URL cell.** Append ` ; https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services ; https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions`.
   - **Inventory, scope paragraph.** Add the short names `SEGS = https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services (Service Extensions docs, not Model Armor docs); SETE = https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions (Service Extensions docs, not Model Armor docs)`.
   - **R9.** Add both URLs to R9 of the six columns (see fix 5).
   - **Ruling to record.** Main ruled [To be verified] because the page was unread (queue: "modelarmor P5 r1 Q4"). Main should record that the P7 retry read it.

5. **Latency: the R8 claim "no figure published" is contradicted by an official Google page.** R8 of MA1, MA2, MA3, MA4, MA7 and MA8 (lines 161, 371, 578, 790, 1313, 1495) says: "Latency per call: no figure published; the best practices page says …". The brief's honesty rule says the same. The Service Extensions guide (SEGS above, Google docs, linked from the Model Armor networking page) says, in its traffic-extension steps:
   - Quote: "For Timeout, specify a value between 10 and 1000 milliseconds after which a message on the stream times out. Consider that Model Armor has a latency of approximately 250 milliseconds."
   - **R4 insert.** In R4 of the six columns, insert after the Service Extensions release-status bullet:
     `• The Service Extensions guide for a Model Armor traffic extension says "Consider that Model Armor has a latency of approximately 250 milliseconds" when setting the callout timeout of 10 to 1000 milliseconds; no measurement conditions are given (Service Extensions docs, not Model Armor docs, 2026-10-09) **[Documented]**`
   - **R8 replacement.** In R8 of the six columns, replace the latency bullet with:
     `• Latency per call: the only figure found is "approximately 250 milliseconds" in the Service Extensions guide for load-balancer callouts, with no conditions or per-filter breakdown; the best practices page says "Enabling unnecessary detectors can increase latency" (needs testing)`
   - **R9.** Add to R9 of MA1, MA2, MA3, MA4, MA7 and MA8:
     `• https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services`
     `• https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions`
   - **R9 Summary lines.** Add "a Service Extensions guide" to the R9 Summary line of each of the six columns. Example for MA1: `Model Armor documentation pages on docs.cloud.google.com, the product page, the Security Command Center pricing page, the Google Cloud blog, the Apigee policy reference and release notes, Service Extensions guides, and Google's terms pages.` (32 words.)
   - **What stays.** The MA7 and MA8 R5 bullet "Published detection rate, false-positive rate or latency for malicious URL detection … [Not disclosed]" can stay: the 250 ms figure is not given per filter. The brief is not a final source and is not edited.

6. **MA1, MA2, MA3, MA4, MA7 and MA8 R4: a judgement is labelled Documented.** The bullet appears at lines 90, 295, 499, 713, 1253 and 1433. It reads: "The floor settings page still labels the Google Cloud MCP servers integration "(Preview)" (floor settings page, 2026-10-09); the dated release note 2026-04-22 says General Availability and is preferred, because the page label is undated **[Documented]**". The preference is an editorial judgement. INV(b) and INV(c) label the same preference [Inferred]. Change log section 4 says the preference is [Inferred] in the inventory and "stated in the six A R4 bullets", but there it carries a Documented label. README section 3 rule 5 requires one label and one fact per bullet. Replace the bullet in all six places with two bullets:
   `• The floor settings page still labels the Google Cloud MCP servers integration "(Preview)" (floor settings page, 2026-10-09) **[Documented]**`
   `• The dated release note 2026-04-22 (General Availability, sub-bullet above) is taken as current because the page label is undated **[Inferred]**`

7. **Absence claims labelled To be verified or Documented (README section 3 rule 2; R020 ruling 1).** These were not flagged in triage.
   - **MA9 R3 (line 1579).** The bullet "Whether a document in a model response is accepted, and how an LLM would produce one, is not stated; the overview example of a PDF "processing LLM outputs" is about downstream systems (overview, 2026-10-09) **[To be verified]**" combines an absence, a reading and a test item. Replace it with:
     `• Whether a document can be sent in a model response is not stated (checked the overview, sanitize page, templates reference and release notes) **[Not disclosed]**`
     `• The overview's PDF example ("it can be used to compromise any downstream systems processing LLM outputs") concerns systems after the model, not a document sent to the response method **[Inferred]**`
     The test half stays in R8 (T61).
   - **MA10 R3 (line 1726).** Replace `**[To be verified]**` with `**[Not disclosed]**` in "No page shows a request body that sends an image through `modelResponseData` (checked the sanitize page, overview, templates page and release notes)".
   - **MA4 R2 (line 638).** Split "…; the note does not say whether this applies to responses (release notes, 2026-10-09) **[Documented]**" into the existing quote bullet, ending at "…"Sensitive information retrieval" (release notes, 2026-10-09) **[Documented]**", and a new bullet:
     `• Whether the 2025-09-23 detection improvements apply to responses is not stated (checked the release note) **[Not disclosed]**`

**After applying the fixes.** The merger should log each fix in modelarmor_changes.md as P7 fixes. It should then re-run check_drafts.py for both finals and regenerate the preview. Expected R1 to R7 bullet counts change; no Summary word count changes, except the six R9 lines in fix 5.

## Optional suggestions

- **MA3 R5 Summary.** "Google's pages advise … Low and above for high-stakes categories" is stronger than the source: Low and above is "Use with caution. Potentially suitable for high-stakes categories like prompt injection and jailbreak detection". Suggested replacement (38 words): `**Match flag plus a confidence level.** The result gives an execution state, a match state and a confidence level. Google's pages advise Medium or High as the setting, and call Low and above potentially suitable for high-stakes categories. **[Documented]**`
- **GKE naming.** The six A R4 Service Extensions bullets say "the GKE Inference Gateway integration is Generally Available from release note 2025-09-15". The note reads "Model Armor integration with Google Kubernetes Engine is available in General Availability"; it does not name Inference Gateway. Suggest "the Google Kubernetes Engine integration is Generally Available from release note 2025-09-15". INV(b) already says "GKE integration GA 2025-09-15".
- **Consequences inside Documented bullets.** Several [Documented] bullets end in a derived consequence after "so …" or "which shows …". Consider moving the consequence into a separate [Inferred] bullet. None is wrong, but README section 3 rule 5 prefers the split. Lines:
  - 435 (MA3 R2, "so attacks split across turns are not linked");
  - 890 (MA5 R4, "so the caller decides …");
  - 902 and 1082 (logging, "so original sensitive text can appear in logs");
  - 1034 (MA6 R2, "so response-side coverage is whatever that template defines");
  - 1049 (MA6 R3, "which shows the response path can carry a de-identify result");
  - 1642 (MA9 R7, "so URL tests there need … enforcement turned off").
- **INV(b) Client libraries, Status cell.** "Release notes and changelogs of these four repositories [Not disclosed] (not read; versions come from tag names only)": a page not read is not an absence. Use [To be verified] (R020 ruling 2 analogue).
- **INV(b) Service Extensions, Limitations.** SEGS (read in this review) states several test-relevant limits. If the merger wants them, add each as a [Documented] (SEGS) fact:
  - "Streaming API responses aren't supported for any API. Model Armor sanitizes the non-streaming responses and ignores the streaming responses."
  - "any other operation is ignored and allowed to proceed without sanitization";
  - "only the first item in the list of choices is sanitized";
  - the Fail open option is not selected by default.
- **Secure Web Proxy.** The Service Extensions navigation marks "Configure an extension for Secure Web Proxy" Preview, and that page carries a Pre-GA banner. It does not mention Model Armor, and the Model Armor networking page links the Secure Web Proxy row to SETE instead. Do not cite it as Model Armor's status. An R8 note "whether Model Armor on Secure Web Proxy is Preview (the Service Extensions page for Secure Web Proxy extensions is Preview but does not name Model Armor)" would record the lead.
- **MA6 R3.** "A response-side result with `deidentifyResult` is not shown in the docs prose" sits next to "response-side de-identified text is documented in prose but not by example". Suggest "is not shown in any docs example".
- **MA6 R2.** "US-leaning" in the Summary relies on the SSN and ITIN detail. For symmetry, add the MA5 R2 overview bullet ("basic Sensitive Data Protection provides limited infotypes, mainly addressed to the US region") to MA6 R2.
- **Change log 2c.** The log lists the identical input/output Summary pairs but misses two pairs made identical at merge: MA1 R5 = MA2 R5, and MA2 R9 = MA8 R9. Add them when logging the P7 fixes.
- **Change log section 1, pin row.** It says the merger "could not re-read the files at the tag". This review read every cited file at tag modelarmor/v1.3.0 through raw.githubusercontent.com (R020 ruling 2); see check 4. The caveat can be closed.

## Style question from main: identical input/output Summary pairs (change log 2c)

Identical Summary pairs in the final:

- R3: MA1 = MA3;
- R4: MA1 = MA2, MA3 = MA4, MA7 = MA8;
- R5: MA1 = MA2, MA7 = MA8;
- R9: MA2 = MA8, MA3 = MA4.

**Judgement: acceptable; no change required.** Reasons:

1. In every pair both Summaries are entailed by their own Detail. I checked MA2 R5 in particular, which became identical to MA1 R5 at merge: its Detail carries the three default statements.
2. The facts are the same for both directions: the same template, filter, result type and mechanism. R002 asks for separate columns, not for different wording, and the brief asks for "both columns in full", which they are.
3. Each sheet 3 column is read on its own, so repetition does not mislead.
4. Where a direction-specific difference exists, the Summary already shows it: MA2 R3 (optional userPrompt), MA4 R1 and R5 (templates page wording; response example without a level), MA6 R2 and R3 (response-side gaps), and MA8 R3.

The one weakness is that the column header alone carries the direction in the identical R4 and R5 pairs. That is acceptable because R4 is about mechanism and R5 about result shape, and neither differs by direction. Logging gap: see optional suggestion on 2c.

## 1. Unlogged differences (check 1)

**Method.** Python difflib (SequenceMatcher on the bullet lists of each row) over all 90 rows of modelarmor_two_level.md against cols_a (MA1 to MA4, MA7, MA8) and cols_b (MA5, MA6, MA9, MA10). The three global changes in change log section 1 were first normalised on the originals:

- hint style "read 2026-10-09" to "2026-10-09";
- re-pin of 37f936ac to modelarmor/v1.3.0;
- R7 full stop before the label.

Each added or changed line was then matched to modelarmor_changes.md by a normalised 40-character window. The remaining lines were matched to the resolution texts, and the rest were inspected by hand. Inventory: cell-by-cell comparison keyed on the first cell, with every changed cell matched to change log section 3.

**Results.**

- **Summaries.** 36 changed (26 in R1 to R8, 10 in R9), all listed in change log section 2b. Section 2b also marks which are substantive. The changed Summaries are:
  - MA1 R1, R5, R9;
  - MA2 R1, R3, R5, R9;
  - MA3 R5, R9;
  - MA4 R1, R2, R5, R9;
  - MA5 R3, R4, R5, R6, R9;
  - MA6 R2, R3, R5, R6, R9;
  - MA7 R1, R9;
  - MA8 R9;
  - MA9 R3, R4, R5, R6, R9;
  - MA10 R3, R4, R5, R6, R9.
- **Detail lines.** After normalisation, 164 added or changed lines were not found in the log by prefix. Every one of them lies in a row that has a log entry; 0 lines sit in rows with no entry. 117 of the 164 are word-for-word in a resolution's "Draft impact" text. The other 47 are:
  - the 42 route sub-bullets made by splitting the "Release status of routes" bullet (7 routes × 6 columns; dates unchanged against the original bullet; hygiene "one bullet, several facts");
  - 3 R8 checked-list extensions in MA5, MA6 and MA10 (T49);
  - MA4 R2 "best practices" added to the checked list (T36);
  - MA9 R8 antivirus checked list (T57).
  None is a new fact without a reason code.
- **Inventory.**
  - Rows: two new rows in (d), us-east7 and global (T77). The (b) Terraform row's first cell was renamed (T24). No row was removed.
  - Changed cells: 48. All are covered by change log section 3. The five my script could not match by prefix (CSAM Default, Antivirus Config key, OCR Levels, Apigee Status, Service Extensions Status) are logged under T9, T57, T11, T20 and T21 with shortened text.
  - The (a) and (d) intros changed (logged as T35, T36 and T77).
- **Result.** No substantive unlogged change.

## 2. Sourcing and label strength (check 2)

- **Traceability of changed Documented facts.** Every changed [Documented] fact I traced has a quote in resolutions_1 or resolutions_2 (T2, T9, T16, T20, T44, T45, T52, T55, T78, T85, T86, among others), or is carried from the draft. I re-read 30 of them at source (section 4).
- **Leftover scan (lessons.md item 6).** No hits in either final for: "only the Go client", "Go client documents", "docs pages do not mention", "130,000 tokens is skipped", "October 10", "2026-10-10", "two different defaults", "Always on", "mainly around", "client library has an optional", "Medium in one place", "Text over", "every docs page footer". The other strings checked:
  - "custom detector" occurs only as "no custom detector is needed" (NRIC), in the T35 Inferred topicality bullet and in a templates-page quote.
  - "is skipped" occurs only for the Agent Platform fail-open behaviour and for the modality skip. Every token-limit bullet now carries the MATCH_FOUND or EXECUTION_SKIPPED split (MA1 to MA4 R6, MA5 and MA6 R5, MA9 R5, INV(a), INV(e)).
  - 37f936ac occurs once, in the INV scope paragraph, naming the clone HEAD next to the tag.
- **Apigee GA or Preview.** No Apigee "not stated" or To be verified leftover remains; all eight Apigee status bullets carry the release-note dates.
- **Inferences labelled Documented.**
  - Fix 6: the MCP preference, in six places.
  - Optional: the "so …" consequences.
  - The rest of the [Inferred] bullets I read state their premise: T3, T35, T43, T44, T47, T55, T67, T68, T70, T76 and the CSAM-with-enforcement-off reading.
- **Absence claims under the wrong label.** Fix 7 (three locations). The T21 To be verified label is now an absence after the verbatim read (fix 4).
- **Wrong absence claim.** Latency (fix 5).
- **Code pins.** Every `[Documented: repo …@ref]` label in R1 to R7 has an R9 URL naming the same repo and ref in the same column. Every non-API URL cited in R1 to R8 text appears in that column's R9 (script check, 0 misses).

## 3. Summary entailment and style (check 3)

- **Mechanical checks.** `python benchtest/tools/check_drafts.py columns benchtest/drafts/modelarmor_two_level.md --final --expect 10` gives 0 errors and 0 warnings; the headers match the brief exactly. The script also gives:
  - word counts: maximum 45 for R1 to R6 and R8 (MA1 R1, MA2 R1, MA6 R6), maximum 56 for R7 (MA3 R7), none over the limit;
  - bold leads, R8 "**Key open questions.**" with no label, R9 plain lines;
  - no backtick, underscore or dollar sign in any Summary.
  - No "Reviewer notes", "this draft", "I checked" or "see above" in either final.
- **Label counts.** These match change log 7b: [Documented] 821, [Not disclosed] 144, [Inferred] 124, google-cloud-go@modelarmor/v1.3.0 21, [To be verified] 14, google-cloud-java@v1.93.0 2, apigee-samples@2b1a9f00 1. There are 1,458 top-level bullets and 101 sub-bullets.
- **Preview.** modelarmor_summaries_preview.md matches the final: 90 lines, with the same text, word counts and bullet counts (script, 0 mismatches).
- **Entailment.** All changed Summaries were read against their own Detail, along with every R4 [Not disclosed] Summary.
  - Not entailed: MA1 R1, MA2 R1 (fix 1); MA5 R6, MA6 R6 (fix 2); MA9 R4, MA10 R4 (fix 3).
  - Entailed: MA1 R5, MA2 R5 (three defaults); MA2 R3 (REST optional field); MA3 R5 and MA4 R5 (four advice bullets A to D, plus the response example with no level); MA4 R1 (overview sentence plus sample); MA4 R2 (MCP execution errors); MA6 R2, MA6 R3, MA6 R4; MA7 R1.
- **Weakest-label rule.** It is applied correctly: the R4 Summaries of all ten columns, MA6 R2 and R3, and MA9 and MA10 R3 carry [Not disclosed].
- **Style.** British spelling holds in the text I read ("sanitisation", "organisation"); vendor terms keep the vendor spelling ("sanitize page", "de-identify").

## 4. Spot-checks at source (check 4)

Read on 2026-10-09:

- with `python benchtest/tools/fetch_text.py` (all docs.cloud.google.com and cloud.google.com pages);
- with curl plus a stdlib HTML parser for the two Service Extensions pages, where fetch_text returns an empty body;
- through raw.githubusercontent.com at the tag for code (R020 ruling 2).

No sign-in, no API host, no form. Page copies are in benchtest/scratchpad/verifier/modelarmor/pages/ and gosrc/.

| # | Claim | Location | Source URL | Verbatim quote | Match |
|---|---|---|---|---|---|
| 1 | CSAM on by default, cannot be turned off | MA1, MA2 R1 and R2; INV(a) | https://docs.cloud.google.com/model-armor/overview | "Contains references to child sexual abuse material (CSAM). This filter is applied by default and cannot be turned off." | MATCH |
| 2 | CSAM unavailable in the 7 limited-support locations with enforcement on (new Summary caveat) | MA1, MA2 R1 Summary, R2; INV(d) | https://docs.cloud.google.com/model-armor/feature-availability-by-region | Table "Supported features by region … template that has data residency enforcement enabled": CSAM support "No" for asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2, northamerica-northeast2; "Yes" for eu, us and the full-support regions | MATCH (but the fact sits in R2, not R1: fix 1) |
| 3 | Three different defaults for an omitted RAI level | MA1, MA2 R5 Summary and Detail; INV(a) | https://docs.cloud.google.com/model-armor/manage-templates ; https://docs.cloud.google.com/model-armor/configure-floor-settings ; https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates | "If you don't specify a confidence level, it is set to High by default." / "If you don't specify a confidence level, it defaults to Medium and above." / "DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED \| Same as LOW_AND_ABOVE" and "the system will use a reasonable default level based on the filterType" | MATCH |
| 4 | PI floor default LOW_AND_ABOVE | MA3, MA4 R5; INV(c) | https://docs.cloud.google.com/model-armor/configure-floor-settings | "If you don't specify the prompt injection and jailbreak detection confidence level, the confidence level defaults to LOW_AND_ABOVE for all levels: project, organization, or folder." | MATCH |
| 5 | userPrompt optional field in the REST method reference (T16 correction) | MA2 R3 Summary; MA2, MA4, MA6, MA8 R3 and R6 | https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse | "\| userPrompt \| string Optional. User Prompt associated with Model response." (footer "Last updated 2026-08-19 UTC") | MATCH |
| 6 | Over 130,000 tokens: a match still counts, no match returns EXECUTION_SKIPPED | MA5, MA6 R5 and R6 Summaries; MA1 to MA4 R6; INV(a), (e) | https://docs.cloud.google.com/model-armor/quotas | "Sensitive Data Protection \| 130,000 If a filter detects a match, it returns MATCH_FOUND. … If the prompt or response exceeds the filter's token limit, the filter returns EXECUTION_SKIPPED and includes Detection skipped as token limit exceeded." | MATCH |
| 7 | NRIC is a built-in infoType, available in any location | MA5, MA6 R7 | https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference | "SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER \| A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card."; categories table "SINGAPORE … GOVERNMENT_ID PII SPII … ANY_LOCATION"; "The value ANY_LOCATION means that the infoType is available in all regions." | MATCH |
| 8 | PI three-word minimum | MA3 R6, R7 Summaries; INV(e) | https://docs.cloud.google.com/model-armor/overview | "if the word count is fewer than three words, Model Armor returns NO_MATCH_FOUND because such inputs lack enough information to constitute an attack" (also on the quotas page) | MATCH |
| 9 | 65,536 tokens; 1,200 QPM default | MA1 to MA4 R6 Summaries; INV(e) | https://docs.cloud.google.com/model-armor/quotas | "Model Armor screens text up to 65,536 tokens"; "API queries \| 1200 queries per minute (QPM) per project"; ExternalProcessor "600 QPM per project" | MATCH |
| 10 | First 256 URLs only | MA7, MA8 R2, R3, R6 Summaries | https://docs.cloud.google.com/model-armor/overview | "Model Armor extracts URLs until it reaches 256 URLs or the end of the payload, and scans only the first 256 URLs found in prompts and responses." | MATCH |
| 11 | Release note dated 2026-10-09 (T78 correction) | MA3, MA4 R2; INV scope | https://docs.cloud.google.com/model-armor/release-notes | "October 09, 2026 Feature Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data. … multi-region endpoints in the US (us) and EU (eu) … filter version v3 or la[ter]" | MATCH |
| 12 | Route GA dates | A R4 route sub-bullets | https://docs.cloud.google.com/model-armor/release-notes | 2025-12-03 "integration with Gemini Enterprise Agent Platform is available in General Availability"; 2026-06-24 Agent Gateway "generally available (GA)"; 2025-09-16 Gemini Enterprise "General Availability"; 2025-09-15 "integration with Google Kubernetes Engine is available in General Availability"; 2026-07-10 "Streaming sanitization for text is generally available (GA)"; 2025-04-09 traffic extension "This feature is in Preview." | MATCH (GKE naming nuance: optional suggestion) |
| 13 | Filter v4 and v1/v2 retirement | MA1 to MA4 R4 | https://docs.cloud.google.com/model-armor/release-notes ; https://docs.cloud.google.com/model-armor/set-filter-version | "Filter version v4 is available and set as the default for the Latest alias." (2026-09-18); "v2 transition to Legacy status and retire on December 17, 2026"; version table "v4 \| Latest \| 2026-09-18" | MATCH |
| 14 | Pricing: free to 2 million tokens, then $0.10 per million | all R7 Summaries; R4; INV(e) | https://cloud.google.com/security-command-center/pricing | "there is no cost for using Model Armor up to 2 million tokens per month. Use of Model Armor beyond this no-cost monthly allocation is billed at a rate of $0.10 per million tokens." | MATCH |
| 15 | Apigee policies Preview 2025-05-22, GA 2025-09-04 (T20) | A R4; MA5, MA6 R4; INV(b) | https://docs.cloud.google.com/apigee/docs/release-notes | "May 22, 2025 Apigee X … Public Preview of Apigee policies for LLM/GenAI workloads … SanitizeUserPrompt SanitizeModelResponse"; "September 04, 2025 Apigee X … Apigee policies for LLM/GenAI workloads are Generally Available (GA)" | MATCH |
| 16 | Apigee SanitizeModelResponse has a required UserPromptSource | MA2 R3 | https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy | "<UserPromptSource> The location of the payload for the user prompt text to be extracted. … Required? \| Required" | MATCH |
| 17 | AUP testing clause and CSAM clause (T86) | R7 of MA1 to MA4, MA7, MA8, MA10 | https://cloud.google.com/terms/aup | "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement"; "illegal activity, including child sexual exploitation, child abuse" | MATCH |
| 18 | Pre-GA Offerings terms (T85) | MA3, MA4 R5; MA10 R4 | https://cloud.google.com/terms/service-terms | "PRE-GA OFFERINGS ARE PROVIDED “AS IS” WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND."; "Customer should not use Pre-GA Offerings to process personal data or other data subject to legal or regulatory compliance requirements" | MATCH |
| 19 | Nine tested languages | MA1 to MA4 R2 Summaries | https://docs.cloud.google.com/model-armor/overview | "are tested on the following languages: Chinese (Mandarin) English French German Italian Japanese Korean Portuguese Spanish These filters can work in many other languages, but the quality of results might vary." | MATCH |
| 20 | 4 MB, 69 bytes, JPEG/PNG/BMP, one image, us and eu only | MA9, MA10 R1, R2, R5, R6 Summaries; INV(e) | https://docs.cloud.google.com/model-armor/overview | "Supported files are limited to 4 MB in size."; "rejects requests to scan files that are smaller than 69 bytes"; "screens images only in the JPEG, PNG, and BMP formats"; "screens only a single image per request"; "Image screening is supported only in the us and eu multi-regions." | MATCH |
| 21 | Basic SDP: six (overview, REST) vs seven (sanitize page adds PASSWORD) | MA5, MA6 R2; INV(a) | https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates ; https://docs.cloud.google.com/model-armor/sanitize-prompts-responses ; https://docs.cloud.google.com/model-armor/overview | "using a fixed set of six info-types"; sanitize list "CREDIT_CARD_NUMBER … FINANCIAL_ACCOUNT_NUMBER … GCP_CREDENTIALS … GCP_API_KEY … PASSWORD … additional … for US-based regions: US_SOCIAL_SECURITY_NUMBER …"; overview six categories | MATCH |
| 22 | PI threshold advice A to D | MA3, MA4 R5 Summaries and Detail; INV(a), (c) | https://docs.cloud.google.com/model-armor/overview ; https://docs.cloud.google.com/model-armor/manage-templates | "Set prompt injection and jailbreak detection filters to Medium. For applications like Gemini Enterprise, set the threshold to High"; "We recommend that you set the confidence level to High"; Low and above "Use with caution. Potentially suitable for high-stakes categories like prompt injection and jailbreak detection"; "start with High or Medium and above to minimize false positives" | MATCH ("advise" for C is strong: optional) |
| 23 | MCP execution errors and the natural-language tip | MA4 R2 Summary, R3 | https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration | "MCP tool execution errors (target for prompt injection by malicious MCP tools authors)"; "Tip: Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data." | MATCH |
| 24 | Send only the latest message, no history or system prompt | MA1, MA3, MA5, MA7 R3 Summaries | https://docs.cloud.google.com/model-armor/sanitize-prompts-responses | "The userPromptData field must contain only the content of the latest message from the user in the current conversation. Don't include conversation history … Don't include system prompts" | MATCH |
| 25 | PI response example shows no confidence level; Python sample shows HIGH | MA4 R5 Summary; MA3 R5 | https://docs.cloud.google.com/model-armor/sanitize-prompts-responses | JSON: "piAndJailbreakFilterResult": { "executionState": "EXECUTION_SUCCESS", "matchState": "NO_MATCH_FOUND" }; Python: "pi_and_jailbreak_filter_result { … match_state: MATCH_FOUND confidence_level: HIGH }" | MATCH |
| 26 | Agent Platform and Gemini Enterprise do not return de-identified data | MA6 R4 Summary | https://docs.cloud.google.com/model-armor/model-armor-vertex-integration ; https://docs.cloud.google.com/model-armor/integrations | "Model Armor doesn't pass the de-identified data—such as masked, redacted, or hashed content—back to Gemini Enterprise Agent Platform"; "Gemini Enterprise blocks the response rather than de-identifying it." | MATCH |
| 27 | FAR-only rows us-east7 and global; template ID limit | INV(d) new rows; INV(e) | https://docs.cloud.google.com/model-armor/feature-availability-by-region ; https://docs.cloud.google.com/model-armor/manage-templates | us-east7 "Responsible AI Sensitive Data Protection Prompt injection and jailbreak Malicious URL \| Yes \| Yes \| No \| Yes"; global "… \| Yes \| Yes \| Yes \| Yes"; "It cannot exceed 63 characters, contain spaces, or start with a hyphen." | MATCH |
| 28 | Go service.pb.go line references at tag modelarmor/v1.3.0 (main's ask; R020) | MA2, MA4 R3 (2380-2381); MA3, MA4 R4 (1861); MA5, MA6 R2 (2160); MA5 R4 (2226); MA5, MA6 R5 (2559); MA5 R6 (1129); MA9 R2 (783), R4 (776), R3 (2379), R5 (3222), R2 (3433); MA10 R6 (454), R5 (3586, 3376), R3 (2379, 792) | https://raw.githubusercontent.com/googleapis/google-cloud-go/modelarmor/v1.3.0/modelarmor/apiv1/modelarmorpb/service.pb.go | 2379 "ModelResponseData *DataItem"; 2380 "// Optional. User Prompt associated with Model response."; 2381 "UserPrompt string"; 1861 "type FilterConfig struct {" (fields RaiSettings, SdpSettings, PiAndJailbreakFilterSettings, MaliciousUriFilterSettings); 2160 "content for sensitive data using a fixed set of six info-types"; 2226 "type SdpAdvancedConfig struct {"; 2559 "Results for all filters where the key is the filter name" (2561 map[string]*FilterResult); 1129 "FilterConfig *FilterConfig"; 776 "ByteDataItem_BYTE_ITEM_TYPE_UNSPECIFIED"; 783 "XLSX, XLSM, XLTX, XLYM"; 792 "ByteDataItem_IMAGE … = 8"; 3222 "type ByteDataItem struct {"; 3376 "BoundingBoxes []*SdpImageFindingLocation_SdpBoundingBox"; 3433 "Nested names could be absent if the embedded object has no string"; 454 "Modality_MODALITY_UNSPECIFIED"; 3586 "when include_findings in the SDP template is set to true." | MATCH (14 of 14) |
| 29 | Go absence grep; module version; Java v1 FilterConfig and pom | MA3, MA4 R4; INV(b), (c) | raw …/google-cloud-go/modelarmor/v1.3.0/modelarmor/apiv1beta/modelarmorpb/service.pb.go ; …/modelarmor/internal/version.go ; https://raw.githubusercontent.com/googleapis/google-cloud-java/v1.93.0/java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto ; …/java-modelarmor/pom.xml | FilterVersion, FilterRule, ExclusionRule, DataResidency: 0 hits in apiv1 and apiv1beta; version.go "const Version = "1.3.0""; Java `message FilterConfig` has rai_settings, sdp_settings, pi_and_jailbreak_filter_settings, malicious_uri_filter_settings, and filter_version, filter_rule, data_residency, exclusion each 0 hits; pom "<version>0.40.0</version>" | MATCH |
| 30 | "Latency per call: no figure published" | MA1, MA2, MA3, MA4, MA7, MA8 R8 | https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services | "For Timeout, specify a value between 10 and 1000 milliseconds after which a message on the stream times out. Consider that Model Armor has a latency of approximately 250 milliseconds." | MISMATCH (fix 5) |

**Tally.** 30 checked: 29 MATCH, 1 MISMATCH, 0 UNVERIFIABLE. Row 28 alone covers 14 line references, all MATCH. This confirms the merger's carried-over line numbers at the tag, which the merger could not re-read itself.

**T21 retry (main's ask 3).** fetch_text.py still returns an empty body for the Service Extensions page (158 bytes, status 200). curl returned the full HTML (200, 174,862 bytes), parsed with a stdlib HTMLParser (`python -I`). Findings:

- No launch-stage banner and no GA date on SEGS (footer "Last updated 2026-10-07 UTC").
- The Model Armor section reads: "You can configure a traffic extension to call Model Armor to uniformly enforce security policies on generative AI inference traffic to application load balancers, including GKE Inference Gateway."
- SETE (the Secure Web Proxy reference from the networking page) also has no banner and does not mention Model Armor.

**Outcome.** The GA date stays unknown and the bullet becomes a checked absence (fix 4). The latency sentence is new (fix 5).

## 5. Inventory consistency (check 5)

- **Checker.** `python benchtest/tools/check_drafts.py inventory benchtest/drafts/modelarmor_inventory_final.md --headers benchtest/drafts/modelarmor_two_level.md` gives 0 errors and 0 warnings.
- **Row counts.** (a) 10 rows × 10 columns, (b) 15 × 9, (c) 16 × 7, (d) 20 × 12, (e) 16 × 6. These match change log section 0 and 7c (BLOCKS 10/15/16/20/16 for P8).
- **Covered-by** (my own script, split on ";" and compared with the 10 headers in modelarmor_two_level.md). Every value is an exact header or the marker `— (inventory only, not in Table 3)`.
  - Eight marker rows: Antivirus in (a); gcloud, Terraform, Agent Gateway egress, MCP servers, Security Command Center findings, console and monitoring in (b). This is consistent with R017 items 1 and 2.
  - Mapping: RAI and CSAM → MA1, MA2; PI → MA3, MA4; URL → MA7, MA8; both SDP rows → MA5, MA6; OCR → MA10; visual scanning → MA5, MA6, MA10; documents → MA9.
  - REST API, client libraries and Gemini Enterprise → MA1 to MA10. Agent Platform, Agent Gateway ingress, Apigee, Service Extensions and LangChain → MA1 to MA8.
- **Cell rules.** No `**`, no backticks, no stray "|" (0 and 0 by grep; the checker passes). Labels found are only [Documented], [Documented: repo …@…], [Inferred], [To be verified] and [Not disclosed]; no non-standard form.
- **Spot-checks.** INV(d) rows for asia-northeast3 (SDP only; all four flags No), europe-southwest1 (Image No), us-east7 and global match the FAR table (rows 2 and 27 above). The INV(e) template ID limit matches. The Apigee Status cell matches the Apigee release notes.
- **Label nit.** Client libraries "[Not disclosed] (not read; …)": optional suggestion.

## 6. URLs (check 6)

**Harvest.** 59 distinct URLs: every R9 bullet in the 10 columns plus every URL in the Source URL cells of INV blocks (a) to (e). No `*.googleapis.com` API host or `{…}` template path was in either set, so none was requested (lessons.md item 12; hard rule 5).

**Request.** `curl -s -L --max-time 30 -A "Mozilla/5.0"`, one GET each.

**github.com 403s.** These were checked through raw equivalents:

- the 10 blob URLs as raw.githubusercontent.com at the same ref, all 200;
- the 4 tree URLs as `git ls-remote --tags`, all tags present:
  - google-cloud-dotnet Google.Cloud.ModelArmor.V1-1.0.0-beta07 → c7114485;
  - google-cloud-node modelarmor-v0.10.0 → 703154ba;
  - google-cloud-php-modelarmor v0.8.3 → 00a3ea17;
  - google-cloud-python google-cloud-modelarmor-v0.7.2 → 69401247.

| Class | Count | Verdict |
|---|---|---|
| 200 | 45 | all docs.cloud.google.com and cloud.google.com pages; no redirect (final URL equals request) |
| 403 | 14 | all github.com (proxy refuses github.com HTML); every one verified through raw (10) or ls-remote (4); expected, not a failure |
| 404 or other | 0 | none |

**Proposed additions (fixes 4 and 5).** Both return 200 by curl:

- https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services
- https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions

fetch_text.py returns an empty body for both; record this in the url_check file.

### Appendix: URL table

| URL | Status | Used in |
|---|---|---|
| https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps | 200 | MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://cloud.google.com/products | 200 | MA10 R9 |
| https://cloud.google.com/security-command-center/pricing | 200 | INV(b), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://cloud.google.com/security/products/model-armor | 200 | INV(a), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://cloud.google.com/terms/aup | 200 | MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA7 R9, MA8 R9 |
| https://cloud.google.com/terms/service-terms | 200 | MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy | 200 | INV(b), MA2 R9, MA4 R9, MA6 R9, MA8 R9 |
| https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy | 200 | INV(b), MA1 R9, MA3 R9, MA7 R9 |
| https://docs.cloud.google.com/apigee/docs/release-notes | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/mcp/model-armor-supported-products | 200 | INV(b) |
| https://docs.cloud.google.com/model-armor/best-practices | 200 | MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/configure-exclusion-rules | 200 | INV(a), INV(c), INV(e), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/configure-floor-settings | 200 | INV(a), INV(b), INV(c), MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9 |
| https://docs.cloud.google.com/model-armor/configure-logging | 200 | INV(b), INV(c), INV(e), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/data-residency | 200 | INV(b), INV(c), INV(d), MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/feature-availability-by-region | 200 | INV(a), INV(c), INV(d), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/integrations | 200 | INV(b), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/locations | 200 | INV(d), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/manage-templates | 200 | INV(a), INV(b), INV(c), INV(d), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-apigee-integration | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration | 200 | INV(a), INV(b), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-langchain-integration | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration | 200 | INV(b), INV(c), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-networking-integration | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/model-armor-vertex-integration | 200 | INV(a), INV(b), INV(c), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/monitoring-dashboard | 200 | INV(b) |
| https://docs.cloud.google.com/model-armor/overview | 200 | INV(a), INV(b), INV(c), INV(d), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/quotas | 200 | INV(a), INV(b), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/reference/libraries | 200 | INV(b), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem | 200 | MA10 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting | 200 | MA5 R9 |
| https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult | 200 | INV(a), INV(c), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates | 200 | INV(a), INV(b), INV(c), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse | 200 | MA10 R9, MA2 R9, MA4 R9, MA6 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/release-notes | 200 | INV(a), INV(b), INV(c), INV(d), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/retry-strategy | 200 | INV(e) |
| https://docs.cloud.google.com/model-armor/sanitize-prompts-responses | 200 | INV(a), INV(b), INV(c), INV(d), INV(e), MA1 R9, MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9, MA9 R9 |
| https://docs.cloud.google.com/model-armor/set-filter-version | 200 | INV(a), INV(c), INV(d), MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/model-armor/version-history | 200 | MA1 R9, MA2 R9, MA3 R9, MA4 R9, MA7 R9, MA8 R9 |
| https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings | 200 | INV(a), INV(b) |
| https://docs.cloud.google.com/security-command-center/docs/terraform | 200 | INV(b) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels | 200 | INV(a), MA9 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference | 200 | MA5 R9, MA6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images | 200 | MA10 R9 |
| https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/LICENSE.txt | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/llm-security-v2/README.md | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml | 403 (github.com via proxy); raw or ls-remote 200/tag present | MA6 R9 |
| https://github.com/googleapis/google-cloud-dotnet/tree/Google.Cloud.ModelArmor.V1-1.0.0-beta07 | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/LICENSE | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/CHANGES.md | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/apiv1/modelarmorpb/service.pb.go | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(a), INV(b), INV(c), MA10 R9, MA2 R9, MA3 R9, MA4 R9, MA5 R9, MA6 R9, MA8 R9, MA9 R9 |
| https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/apiv1beta/modelarmorpb/service.pb.go | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b), MA3 R9, MA4 R9 |
| https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/internal/version.go | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/pom.xml | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b), INV(c), MA3 R9, MA4 R9 |
| https://github.com/googleapis/google-cloud-node/tree/modelarmor-v0.10.0 | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-php-modelarmor/tree/v0.8.3 | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |
| https://github.com/googleapis/google-cloud-python/tree/google-cloud-modelarmor-v0.7.2 | 403 (github.com via proxy); raw or ls-remote 200/tag present | INV(b) |

Source files: benchtest/scratchpad/verifier/modelarmor/url_table.md and url_check.txt.
