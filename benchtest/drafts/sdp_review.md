# Sensitive Data Protection workbook: fresh verifier review

Date of checks: 2026-10-09. Inputs read: CLAUDE.md, drafts/README.md, sdp_brief.md, sdp_two_level.md (read in full), sdp_inventory_final.md (read in full), sdp_changes.md (read in full), sdp_summaries_preview.md (regenerated and compared), sdp_cols_a.md, sdp_cols_b.md and sdp_inventory.md (diffed), sdp_triage.md and sdp_resolutions_1.md / _2.md (targeted entries T9, T12, T14, T16 to T24, T42, T44, T60, T62, T66, T73, T78, T79, T83, T92, T93, T97), rulings R011, R012, R015, R018, R019, R020, main's queue rows for sdp, lessons.md, and the models lg_review.md and sentinel_review.md. Scripts, fetched page text and code are in `benchtest/scratchpad/verifier/sdp/`. No file other than this one and that folder was written.

## Verdict: PASS WITH FIXES

The merge is mechanically clean and, with one exception, faithful. Every changed line in the columns and every changed inventory cell is explained by an entry in the merger's edit log, and every log entry is in sdp_changes.md. Source spot-checks: 33 facts checked, 31 MATCH, 2 MISMATCH. A quote sweep of 523 quoted fragments found 514 verbatim on the official pages or the client code at the tag; the other 9 are header names or the draft's own words between quoted prices, not quotes. All 96 URLs return 200. The release notes, re-read today, still have 2026-10-03 as their newest entry, so the dated PERSON_NAME and MEDICAL_ID statements are correct as written.

The most important finding is fix 7. The T12 merge turned the draft's unchecked [To be verified] remark ("the date-shift, time-extraction and bucketing code samples use record (table) transformations") into a [Documented] fact in SD3 R1 and R4. Both changed Summaries rest on it ("shown only on table fields"). At source this is wrong. The transformation reference has no bucketing code sample at all, and its Go date-shift sample applies date shifting to infoType findings in a plain string.

There are 7 required fixes:
- 1 false [Documented] fact, driving two changed Summaries (fix 7);
- 1 absence claim labelled Documented (fix 1);
- 3 more Summaries not entailed by their own Detail, one of them also wrong at source (fixes 2 to 4);
- 1 group of 4 inferences inside Documented bullets (fix 5);
- 1 absence claim that does not name what was checked (fix 6).

None changes a number, a column header, an inventory row count or a Covered-by value.

## Required fixes

1. **INV(f) "Data handling" row, Detail cell: absence claim labelled [Documented].** The cell says "Sensitive Data Protection is listed among the Google Cloud Platform Services and the Service Specific Terms have no section for it [Documented] (Google Cloud terms services list and Service Specific Terms, not SDP docs)". The second half is an absence claim. Under README section 3 rule 2 and R020 ruling 1 it must be [Not disclosed] and name what was checked. The resolver's T92 text carried the same label and the merger copied it. I confirmed the facts: on cloud.google.com/terms/service-terms the product name appears only in the page navigation (fetched lines 556 and 998).
   - Replace that sentence with: `Sensitive Data Protection is listed among the Google Cloud Platform Services [Documented] (Google Cloud terms services list, not SDP docs). A Sensitive Data Protection section in the Service Specific Terms [Not disclosed] (checked the Service Specific Terms for Sensitive Data Protection, Data Loss Prevention and DLP; the name appears only in the page navigation).`
   - The column R8 bullets that say the same thing are unlabelled, so they need no change.

2. **SD6 R2 Summary: does not match the source and is not entailed by R2 Detail. Also SD6 R8.**
   - (a) "each with a one-sentence definition" is wrong. In the infoType reference each of the three image-context entries has two sentences. For example, VIOLENCE reads "A finding of this type indicates that an image contains violent or gory content either real or fictionalized. Violent content might include imagery related to death, serious injury, or harm to an individual or group of individuals or animals." SD6 R2 Detail itself quotes both sentences for each entry (the "Same entry" bullets).
   - (b) "the docs describe the use as content moderation" rests only on an SD6 **R1** bullet ("You can use this feature to support content moderation and enforce acceptable use policies."). No R2 bullet supports it.
   - The error came from the resolver's T16 replacement text, and the merger's self-check passed it.
   - Replace the Summary with: `Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a short two-sentence description, and the docs describe the use as content moderation. **[Documented]**` (29 words).
   - Insert as the first SD6 R2 Detail bullet: `• Stated use: "You can use this feature to support content moderation and enforce acceptable use policies." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**`
   - SD6 R8, in the bullet beginning "How strictly "racy" and "sexually suggestive" are defined", replace `(the reference gives a one-sentence definition only)` with `(the reference gives a two-sentence description only)`.

3. **SD4 R4 Summary: the bold lead rests on an [Inferred] bullet under a [Documented] label.** "Standard keyed encryption, not a model." The only Detail support for "not a model" is the [Inferred] bullet "Tokenisation itself uses a cryptographic algorithm and no machine-learning model ...". README section 4 says the Summary label must be the weakest label among the facts it draws on. The merger fixed the same pattern in SD2 R5 and SD4 R5 (T17) but kept this lead when it rewrote this Summary for T14.
   - Replace with: `Summary: **Standard keyed encryption.** AES-SIV gives base64 tokens, and the docs disagree on whether the length is kept; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. **[Documented]**` (39 words). The [Inferred] Detail bullet stays.

4. **SD4 R6 Summary: not entailed. It contradicts documented key types.** "Requests need a Cloud KMS wrapped key in a matching region". SD4 R4 Detail documents three key types: Cloud KMS wrapped, transient and unwrapped. SD4 R6 Detail describes the wrapped key as the quickstart's setup, not as a requirement. This Summary is from the draft, not the merge.
   - Replace with: `Summary: **Needs a key, a surrogate name and a supported input.** The documented setup uses a Cloud KMS wrapped key in a matching region, a surrogate annotation for free text, and values within AES-SIV or FPE limits. API keys cannot be used with wrapped keys. **[Documented]**` (44 words).

5. **Four inferences inside [Documented] bullets (README section 3 rule 5).** The merger split this pattern in several places (hygiene entries for SD1 R6, SD4 R4 and SD6 R5) but missed these four. Split each into a [Documented] bullet and an [Inferred] bullet:
   - (a) SD1 R7, bullet "The first gibibyte of content inspected each month per account is free, so a small labelled test set costs nothing; billing information is still required: ...". Replace it with two bullets:
     - `• The first gibibyte of content inspected each month per account is free, and billing information is still required: "Sensitive Data Protection requires billing information for all accounts before you can start using the service." (SDP pricing page, read 2026-10-09) **[Documented]**`
     - `• A small labelled test set therefore stays within the free tier (premise: the free first gibibyte per month on the pricing page) **[Inferred]**`
   - (b) SD4 R1, bullet "Cryptographic hashing is the one-way contrast: ... ; its row belongs to the masking and de-identification in text column **[Documented]**". Replace it with two bullets:
     - `• Cryptographic hashing is the one-way contrast: "Unlike other types of crypto-based transformations, this type of transformation isn't reversible." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**`
     - `• The hash row is covered by the masking and de-identification in text column, not here (premise: a pointer to the owning column, not a source fact) **[Inferred]**`
   - (c) SD5 R1, bullet ""Inspection and redaction are two distinct operations:" and the page defines both, so one image can be inspected without being changed ...". Replace it with two bullets:
     - `• "Inspection and redaction are two distinct operations:" and the page defines each (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**`
     - `• One image can therefore be inspected without being changed (premise: inspection is defined separately from redaction and returns only infoTypes and pixel coordinates) **[Inferred]**`
   - (d) SD5 R2, bullet ""Default infoTypes don't include objects in images." so object detectors must be requested by name ...". Replace it with two bullets:
     - `• "Default infoTypes don't include objects in images." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**`
     - `• Object detectors must therefore be requested by name (premise: the sentence above) **[Inferred]**`

6. **SD6 R5, absence claim without the pages checked (README section 3 rule 2).** The bullet "Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images **[Not disclosed]**" names no pages. I checked: the concepts-image-redaction and supported-file-types pages have no precision, recall or latency terms. On the infoType reference, "latency" appears only in the "latency sensitive operations" notes. The likelihood page defines the terms only. The one latency hit in the release notes concerns inspection jobs.
   - Replace with: `• Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images (checked the image concepts, supported-file-types, infoType reference and likelihood pages and the release notes) **[Not disclosed]**`

7. **SD3 R1 and SD3 R4: a false [Documented] fact, and the two changed Summaries (T12) that rest on it. Also SD3 R4 [To be verified] and SD3 R8.**
   - **What the finals say.** SD3 R1 Detail says "The date-shift, time-extraction and bucketing code samples on the transformation reference page use record (table) transformations ... **[Documented]**". SD3 R4 has the same claim. The Summaries say "Bucketing and date shifting are offered but shown only on table fields" (R1) and "bucketing and date shifting are shown only on table fields" (R4).
   - **Where it came from.** In the draft, this sample claim sat inside a [To be verified] bullet. The T12 resolution quoted only the discovery schema, the Input-type column and the bucketing text, not the samples. The merger split the claim out as [Documented] with no quote (README section 3 rule 1).
   - **What the source shows.** I read the raw transformations-reference page:
     - the "Bucketing" section (fetched lines 7572 to 7655) has no code sample, only a JSON fragment of a `bucketingConfig`;
     - the "Date shifting" section has six samples. Java, Node.js, Python, PHP and C# use record transformations on a table. The Go sample `deidentifyDateShift` builds `DeidentifyConfig_InfoTypeTransformations` with `PrimitiveTransformation_DateShiftConfig`, inspects for `DATE`, and sends `ContentItem_Value` with the comments `input := "2016-01-10"` and `Will print "2016-01-09"`. That is date shifting on infoType findings in a plain string;
     - all time-extraction samples use record transformations on a table.
   - SD3 R1 Summary, replace with: `Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method redacts, replaces, masks or hashes detected values; one sample also date-shifts a plain string. Bucketing and time extraction are not shown on free text. It returns the item and a change summary. **[Documented]**` (45 words)
   - SD3 R4 Summary, replace with: `Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Detected values are redacted, replaced, masked or hashed, and one sample date-shifts a plain string; bucketing and time extraction are not shown on free text. **[Documented]**` (45 words)
   - SD3 R1, replace the bullet "The date-shift, time-extraction and bucketing code samples on the transformation reference page use record (table) transformations ..." with two bullets:
     - `• On the transformation reference page, the time-extraction samples and five of the six date-shift samples use record (table) transformations, and the bucketing section gives only a JSON configuration fragment with no code sample (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**`
     - `• The Go date-shift sample applies `dateShiftConfig` inside an infoType transformation to a plain string item with `DATE` inspection; its comments read `input := "2016-01-10"` and `Will print "2016-01-09"` (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**`
   - SD3 R4: replace the bullet "The date-shift, time-extraction and bucketing code samples use record (table) transformations and a context field" with the same two bullets.
   - SD3 R4: replace the [To be verified] bullet with `• Whether the bucketing and time-extraction transformations work on infoType findings in free text is not stated (checked the transformation reference; the docs table says Any or Dates/Times) **[To be verified]**`
   - SD3 R8: replace the bucketing bullet with `• Whether `FixedSizeBucketingConfig`, `BucketingConfig` and `TimePartConfig` apply to infoType findings in free text, and whether date shifting on free text behaves as the Go sample shows (checked the transformation reference; needs testing)`. The R8 Summary can stay.
   - Also note: sdp_changes.md section 4 conflict 5 and section 7 ("SD3 R1 gained one bullet for 'shown only on table fields'") record the wrong reading. The merger should log this fix in the "Verifier fixes" section. INV(c) needs no change: its bucketing rows keep [To be verified] for free text, and the date-shift row makes no free-text claim.

## Optional suggestions

- **Dated statements will go stale soon (INV(b) Health row; SD1 R4 and R7).** The MEDICAL_ID legacy window ends about 2026-10-11, two days after this review, probably before P9. The present-tense "the old behaviour is available with version legacy for 90 days [Documented]" will then be outdated.
  - Suggested Health-row text: `Since 2026-07-13, MEDICAL_ID with InfoType.version unset or stable also reports MEDICAL_RECORD_NUMBER findings as MEDICAL_ID, and the note offered the old behaviour with version legacy for the next 90 days [Documented] (DOCS release-notes). That window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)`.
  - P9 must re-read the release notes in any case (PERSON_NAME promotion about 2026-11-02).
  - Background: the release notes also carry a 2026-05-11 MEDICAL_ID note ("If you set InfoType.version to latest ... You can still use the old functionality by setting InfoType.version to stable"). That was the draft's source, so the T44 "CORRECTION" was in fact an update to the later 2026-07-13 note. The final text is right.
- **SD1 R4, content-policy cross-reference bullet:** "(separate resource, not part of this column by default)". The words "by default" are left over from the provisional brief. R018 fixed the policy as inventory only. Suggest `(separate resource, inventory only, not part of this column)`.
- **SD3 R4, bullet citing "API discovery document revision 20261006":** this is not URL-traceable (no googleapis.com URLs, per lessons item 12). The same facts are on the REST projects.deidentifyTemplates page, which is already in SD3 R9: fetched line 1051/1055 "Can only be applied to table items.", and `fixedSizeBucketingConfig` inside PrimitiveTransformation. Suggest changing the hint to `(SDP docs, REST projects.deidentifyTemplates page, schemas PrimitiveTransformation and DateShiftConfig, read 2026-10-09; also the API discovery document revision 20261006)`.
- **SD5 R4 and SD5 R9:** `.../rest/v2/organizations.deidentifyTemplates` answers HTTP 301 to `.../rest/v2/projects.deidentifyTemplates`. Cite the final URL and change the hint to "REST projects.deidentifyTemplates page".
- **R9 lists pages the column does not cite.**
  - SD2 R9 lists DeidentifyContentResponse and ReidentifyContentResponse; SD2 cites only InspectContentResponse.
  - SD4 R9 lists InspectContentResponse and DeidentifyContentResponse; SD4 cites only ReidentifyContentResponse (REST) and the client for deidentify.
  - Optional cleanup.
- **SD6 R7, bullet "Test images must not be illegal content or non-consensual explicit imagery under the Acceptable Use Policy [Documented]".** This applies the AUP to test images. The resolver's own T93 label note says "Reading them as covering the bench is [Inferred]". Main accepted the text, so this is optional. A cleaner form keeps to the AUP's words: `• The Acceptable Use Policy bars using the services for illegal activity, including child sexual exploitation, and for unlawful purposes including Non-consensual Explicit Imagery (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**`.
- **SD5 R2, [Inferred] "The face detector's use therefore carries no SLA".** The same Pre-GA section (Service Specific Terms 5.a) also says that using a Pre-GA component inside a generally available Service "does not negate unrelated commitments that Google makes for its Services". Suggest: `• The face detector itself carries no SLA; whether a content.inspect request that names it keeps the method's SLA is not stated (premise: the Pre-GA terms exclude Pre-GA Offerings from any SLA but keep unrelated commitments for generally available Services) **[Inferred]**`.
- **INV(f) Data handling, [Inferred] "processed only to provide, secure and monitor the service".** DPA 5.2 also has clause b ("as further specified via ... Customer's use of the Services"). Suggest "processed only as the Data Processing Addendum instructs, that is to provide, secure and monitor the services and as the customer's use of them specifies".
- **SD1 R6 Summary** says "an optional minimum likelihood", and **SD3 R1 Summary** says "a summary of changes". Each is supported only by the R5 Detail of its column. Add a one-line pointer bullet to each R6 or R1 Detail, or accept this as cross-row support. Both phrases predate the merge.
- **SD2 R6** "Request-level caps ... (0.5 MB, 3,000 findings, 50,000 table values) still apply ... [Documented]". "Still apply" to custom-detector requests is a small inference, and "caps" sits awkwardly next to the T20 "not a hard limit" wording. Suggest "The content limits table (0.5 MB per request, 3,000 findings, 50,000 table values) covers these requests too (premise: custom detectors travel in the same inspect request) **[Inferred]**", keeping the numbers as [Documented] in SD1 R6.
- **SD4 R2 and SD4 R5:** stray comma before "(premise:" in "a value the detectors miss is not tokenised, (premise:" and "decides what to do with the output, (premise:". This came from the T98 insertions.
- **SD6 R1, client bullet:** cites only `client.py@...:965` (`redact_image`) for both `inspect_content` and `redact_image`. Add `:872` as in SD5 R1.
- **SD4 R4, last bullet** ends "...; behaviour needs a test **[Documented: repo ...]**". Move "behaviour needs a test" to R8. It already is there: "Whether token length follows ...".
- **INV(d) "Dataflow, AWS S3 and JDBC guides" row:**
  - "The anomaly detection page answers HTTP 301 to the SDP docs home [Documented] (observed 2026-10-09)" lacks the URL and final URL that README section 3 rule 7 asks for. The resolver gives the URL (cloud.google.com/architecture/building-anomaly-detection-dataflow-bigqueryml-dlp).
  - The pinned files cited in the cell (dlp_tokenizing_runner_permissions.yaml, LICENSE) are not in the Source URL cell. I read both at 4213e271 and they match.
- **INV(d) Apigee row:** the extension is "no longer supported and has been deprecated", yet the row is covered by the SD3 and SD5 headers. See QUESTIONS.
- **Change log granularity (same remark as the Sentinel review):**
  - Many "After" cells are truncated, and later parts of split bullets ("//") cannot be read in sdp_changes.md.
  - The global-pattern table says "see reason" instead of the replacement strings.
  - Every one of these traces to `scratchpad/merger/sdp/log.json` and `cols_edits.py`, so I treat them as logged.
  - Section 7's "each claim has a bullet" self-check did not catch fixes 2 and 3.

## 1. Unlogged differences (Check 1)

Method (scripts `diff_cols.py`, `diff_cols2.py`, `diff_inv.py` in `scratchpad/verifier/sdp/`):
- **Columns.** Python difflib compared each (column, row) Summary and Detail-line list in sdp_two_level.md with SD1 to SD3 in sdp_cols_a.md and SD4 to SD6 in sdp_cols_b.md. For every added or changed final line, the script then checked whether it equals an original line after the merger's 10 global substitutions (column-pointer wording, T97 citation paths) or is contained in an "after" text in `scratchpad/merger/sdp/log.json`. It also checked every removed original line against the log's "before" texts.
- **Inventory.** Cell-by-cell comparison of all 87 rows (row keys and headers identical), with the same log matching for changed cells and block notes.
- **Log against sdp_changes.md.** Each log.json entry was matched to sdp_changes.md by a normalised prefix.

Results:
- **Summaries changed:** 14, exactly the list in sdp_changes.md section 0 (SD1 R4, R6; SD2 R5, R6, R8; SD3 R1, R4; SD4 R4, R5; SD5 R1, R2; SD6 R2, R4, R5). Each is in section 2 with its before and after text and a word count.
- **Column lines:** 0 final lines are unexplained by the substitutions or the log, and 0 removed lines lack a log entry. The 68 lines that a plain 40-character prefix match did not find in sdp_changes.md are all later parts of "//" splits or T97 citation-path rewrites. All are in log.json and covered by a row or global entry in sdp_changes.md.
- **Inventory:** 0 unexplained changed cells; block row counts are unchanged at 15/24/12/13/16/7.
- **Log against sdp_changes.md:** 190 of 206 log.json entries match by prefix. The other 16 are the 14 Summary entries (the log stores them with the "Summary: " prefix and sdp_changes.md quotes them without it), the T97 regex entry (in the global pattern table) and one T89 "my count" cell (covered by the grouped "(f) Regional endpoints, InfoType availability by location" row).
- **Result:** no substantive unlogged change. The log is coarse in the places listed in the last optional suggestion.

## 2. Sourcing and label strength (Check 2)

**Changed [Documented] facts.** Every new or changed [Documented] fact traces either to a resolution entry with a verbatim quote or to the original draft, with one exception. The SD3 R1 and R4 bullet "The date-shift, time-extraction and bucketing code samples ... use record (table) transformations" was part of a [To be verified] bullet in sdp_cols_a.md (T12). The merger split it out as [Documented] without a quote; the T12 resolution quotes the discovery schema, not the samples. At source it is wrong (fix 7). I re-read the other main facts at source (section 4).

**Merger edits beyond the resolver's exact text** (main asked for these, queue row "sdp P6 Q2/Q3/Q6"):
- **T21, INV(e) row 6 "Maximum transformations per request".** The resolver asked for "Applies to" = "content.inspect, content.deidentify" on rows 1 and 6. The merger used "content.deidentify" for row 6, reason "only content.deidentify applies transformations". Accepted: content.inspect applies no transformations. The Value cell carries the [Documented] table-heading fact and the [Inferred] reidentify point exactly as the resolver wrote them.
- **T24, SD2 R6** (optional item applied). The three added sub-bullets (1 GB combined, 100 files, BigQuery column 1 GB) are verbatim limits-page rows and sit under the existing "Stored infoType limits" group. Verified at source.
- **T60, SD4 R3** (optional item applied, wording adapted). The new bullet is labelled [Not disclosed] and names the pages checked: REST reidentify, ContentItem, release notes and client request type. This matches the resolver's evidence; the 2026-06-03 and 2026-06-12 notes say only "inspecting and de-identifying", and `dlp.py:3028` says "The item to re-identify. Will be treated as". Accepted.
- **T66, SD5 R6 and INV(a) image row.** The docstring bullet and the six-statement cell are as the resolver wrote them. `dlp.py@google-cloud-dlp-v3.40.0:2705` reads "The content must be PNG, JPEG, SVG or BMP." Accepted.
- **T73, SD5 R2** (optional item applied). The merger added the verbatim Pre-GA sentence to the resolver's proposed bullet; it matches Service Specific Terms section 5.b. The [Inferred] SLA consequence is honest, but see the optional suggestion on section 5.a.
- **T83, INV(f) "Regional endpoints"** (optional item applied). The release note dated 2026-01-20 reads "Sensitive Data Protection is available in the asia-southeast3 (Bangkok) region." The REST root page has no asia-southeast3, and the locations page lists it. Accepted.
- **SD2 R1, surrogate split** (hygiene; not a resolver item).
  - The old bullet ("exist only to reverse format-preserving encryption in content.reidentify") was a scope remark under [Documented], and it conflicted with AES-SIV surrogate use in SD4.
  - The new [Documented] quote "Message for detecting output from deidentification transformations that support reversing." is verbatim on REST InspectConfig: it is the description of the `surrogateType` field, at fetched line 653.
  - The pointer bullet is [Inferred] with its premise.
  - Accepted. The same page's SurrogateType schema adds "such as CryptoReplaceFfxFpeConfig"; the overview quote in R1 keeps that wording.
- **Terms URLs in R9.** SD1, SD3, SD4, SD5 and SD6 R9 add terms, data-processing-addendum, service-terms and services; SD6 also adds aup.
  - Each is named in that column's R8 terms bullet, or in SD5 R2 or SD6 R7, which is R019-permitted.
  - All five return 200 and are Google-owned official pages.
  - SD2 has no terms bullet and correctly has no terms URLs.
  - Accepted.
- **Ruling ids removed from cells** (`ruling R012 ...` became "those internals are not repeated here"). Same meaning, accepted by main.

**Inferences or absences labelled [Documented]:**
- Required fixes 1 and 5, plus the label upgrade in fix 7.
- Optional: the SD6 R7 AUP bullet and the SD2 R6 "still apply" bullet.
- Grep of all [Documented] bullets for "therefore / so / probably / appears / belongs / needs a test" found nothing else of substance; the remaining hits are verbatim quotes containing those words.

**Absence claims without a checked list:** one, required fix 6. Every other [Not disclosed] bullet names pages; two name the likelihood page inline.

**Leftovers against resolutions.** I grepped the finals for the 39 known-wrong strings in sdp_changes.md section 7 and for "provisional", "CP1", "SD7", "not read", "Reviewer", "ruling", "this draft", "I checked" and "see above". None remains, except:
- "by default" in SD1 R4 (optional suggestion);
- the column-header line ids, which are correct.

Leftovers on specific topics:
- **3,000 findings:** every Summary uses "not hard" or "cap" correctly. SD3 R5 and R8 refer to the de-identification error threshold, which is documented as an error at more than 3,000.
- **Content policy:** stays inventory only in every column (SD1 R4, SD5 R4, SD6 R4 cross-references only).
- **INV(a) content-policy row:** the absence is [Not disclosed] with the pages listed.

**Release notes re-read (main's ask 2).** Release notes fetched raw on 2026-10-09; the page says "Last updated 2026-10-07 UTC".
- **Newest entry:** "October 03, 2026", the PERSON_NAME note: "A new version with an updated name dictionary is available for the PERSON_NAME infoType detector. ... In 30 days, the new version will be promoted to stable." There is no later entry and no promotion note.
  - So SD1 R7 "No promotion note for the new PERSON_NAME version had appeared (... newest entry is dated 2026-10-03, read 2026-10-09) [Not disclosed]" is correct.
  - "about 2026-11-02" is correct arithmetic: 2026-10-03 plus 30 days.
- **"July 13, 2026":** "If you leave InfoType.version unset or set it to stable when setting the MEDICAL_ID infoType in your InspectConfig, Sensitive Data Protection includes MEDICAL_RECORD_NUMBER findings as type MEDICAL_ID in the scan results. You can still use the old functionality by setting InfoType.version to legacy for the next 90 days."
  - 2026-07-13 plus 90 days is 2026-10-11, so INV(b) Health is correct.
  - The tense will go stale after 2026-10-11 (optional suggestion).
- **SD1 R4 "release notes dated 2026-07-13 and 2026-10-03" for stable, latest and legacy:** MATCH.
- **Re-read due at P9:** the PERSON_NAME promotion falls after any likely P9 date in October, but the MEDICAL_ID window closes on 2026-10-11.

**Cross-product headers** (main's P6 Q4). Since the merge, modelarmor_two_level.md and presidio_two_level.md exist. I compared them: MA5, MA6 and MA10 headers, PD1 and PD2 headers, and the SN6 header in sentinel_two_level.md all match the strings cited in SD1 R4, SD3 R4 and SD5 R4 exactly. Main can close P6 Q4.

## 3. Summary entailment and style (Check 3)

**Mechanical checks.**
- `python benchtest/tools/check_drafts.py columns benchtest/drafts/sdp_two_level.md --final --expect 6`: 6 columns, exact headers, RESULT 0 errors, 0 warnings.
- `python benchtest/tools/check_drafts.py inventory benchtest/drafts/sdp_inventory_final.md --headers benchtest/drafts/sdp_two_level.md`: tables 15x8, 24x7, 12x8, 13x8, 16x4, 7x4; RESULT 0 errors, 0 warnings.
- The checker confirms the 54 Summaries are within the word limits, bold leads are present, R1 to R7 end with one allowed label, R8 starts "**Key open questions.**" with no label, and R9 is plain.
- No backtick, underscore or $ appears in a Summary. Every R1 to R7 bullet is labelled, R9 bullets are bare URLs, and every repo pin has an R9 URL.

**Preview.** I regenerated each Summary's word and bullet counts from the final file and compared them with sdp_summaries_preview.md: all 54 lines match.

**Entailment of the 14 changed Summaries,** each read against its own row's Detail:

| Summary | Result |
|---|---|
| SD1 R4 | entailed |
| SD1 R6 | entailed, except "optional minimum likelihood", whose Detail is in R5 (optional suggestion) |
| SD2 R5 | entailed by the new InspectContentResponse bullet |
| SD2 R6 | entailed, verified at the limits page |
| SD2 R8 | unlabelled, consistent with the R8 bullets |
| SD3 R1 | formally entailed by the new samples bullet, but that bullet is false at source, so the Summary is wrong (fix 7); "summary of changes" only in R5 (optional) |
| SD3 R4 | same as SD3 R1 (fix 7) |
| SD4 R4 | not entailed by a [Documented] bullet for its lead (fix 3) |
| SD4 R5 | entailed |
| SD5 R1 | entailed: release notes 2025-07-04, 2025-11-03, 2025-12-15, 2026-06-08 |
| SD5 R2 | entailed |
| SD6 R2 | not entailed, and "one-sentence" is wrong at source (fix 2) |
| SD6 R4 | entailed |
| SD6 R5 | entailed |

**Unchanged Summaries.** I read all 40. One is not entailed: SD4 R6 (fix 4). The rest are entailed, and their labels match their weakest facts, including [Inferred] for SD1, SD2, SD3, SD4, SD5 and SD6 R3, SD3 R2, SD6 R6 and all R7. Honest-gap wording is neutral. No cross-referenced product (Model Armor, Presidio, Sentinel, Gemini Enterprise) appears in any Summary.

## 4. Spot-checks at source (Check 4)

**Access.**
- Pages were fetched read-only with `python benchtest/tools/fetch_text.py`; the saved text is in `scratchpad/verifier/sdp/pages/`.
- Client code was read at tag `google-cloud-dlp-v3.40.0`, and the Google sample repos at their pinned shas, through raw.githubusercontent.com (R020; github.com returns 403 here).
- No sign-in, no API call and no googleapis.com API host was requested (lessons item 12). The API discovery document was therefore not opened, and the same facts were checked on the REST reference page (row 12).

| # | Claim | Location | Source URL | Verbatim quote | Match |
|---|---|---|---|---|---|
| 1 | PERSON_NAME new version promoted in 30 days; newest release-note entry is 2026-10-03 | SD1 R4, SD1 R7, SD1 R8 | https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes | "October 03, 2026" … "In 30 days, the new version will be promoted to stable." (page "Last updated 2026-10-07 UTC"; no later entry) | MATCH |
| 2 | MEDICAL_ID unset or stable includes MEDICAL_RECORD_NUMBER; legacy for 90 days (T44 correction) | INV(b) Health | same | "If you leave InfoType.version unset or set it to stable when setting the MEDICAL_ID infoType … You can still use the old functionality by setting InfoType.version to legacy for the next 90 days." (July 13, 2026) | MATCH |
| 3 | 3,000 is not a hard limit (T20, changed Summary) | SD1 R6 Summary and Detail, INV(e) | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig | "If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower." / "This value isn't a hard limit." | MATCH |
| 4 | Content limits 0.5 MB, 3,000, 100 transformations, 150 infoTypes; table heading | SD1 R6, SD3 R6, SD4 R6, INV(e) | https://docs.cloud.google.com/sensitive-data-protection/limits | "inspecting and de-identifying content sent directly to the DLP API as text or images" / "Maximum size of each request, except projects.image.redact \| 0.5 MB" / "Maximum number of transformations per request \| 100" / "Maximum number of built-in and custom infoTypes per request \| 150" | MATCH |
| 5 | Custom limits: 30, 10, 10 rule sets, regex length 1000 with no unit (T20, changed Summary) | SD2 R6 Summary | same | "Maximum number of custom infoTypes per request \| 30" / "Maximum number of regular custom dictionaries per request \| 10" / "Maximum number of inspection rule sets per inspection configuration \| 10" / "Maximum length of regular expressions \| 1000" | MATCH |
| 6 | Stored infoType limits (T24) | SD2 R6, INV(e) | same | "Maximum combined size of all input files stored in Cloud Storage \| 1 GB" / "Maximum number of input files stored in Cloud Storage \| 100" / "Maximum size of an input column in BigQuery \| 1 GB" / "… input table rows in BigQuery \| 5,000,000" / "Maximum size of output files \| 500 MB" | MATCH |
| 7 | Inspect response holds only the findings (T17, changed Summary) | SD2 R5 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectContentResponse | "Results of inspecting an item." … field result "object (InspectResult) The findings." (single field) | MATCH |
| 8 | Surrogate detection description (merger split) | SD2 R1, SD4 R4 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig | surrogateType: "Message for detecting output from deidentification transformations that support reversing." | MATCH |
| 9 | Regex syntax points to RE2 (T47) | SD2 R4, SD2 R8 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex | "Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub." | MATCH |
| 10 | Rule order: GA note versus REST "executed in the end" (T49) | SD2 R4 | release notes; REST InspectConfig | "Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset." (February 23, 2026) / "Exclusion rules, contained in the set are executed in the end" (page "Last updated 2026-09-05 UTC") | MATCH |
| 11 | "The date-shift, time-extraction and bucketing code samples ... use record (table) transformations" (T12, changed Summaries "shown only on table fields") | SD3 R1, SD3 R4 | https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference | Bucketing section (fetched lines 7572 to 7655): no code sample, only a `"bucketingConfig":{` JSON fragment. Go date-shift sample: `Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{` … `PrimitiveTransformation_DateShiftConfig` … `Name: "DATE"` … `DataItem: &dlppb.ContentItem_Value{` with `// input := "2016-01-10"` and `// Will print "2016-01-09"`. The other five date-shift samples and all time-part samples use record transformations | MISMATCH (fix 7) |
| 12 | dateShiftConfig.cryptoKey table-only; bucketing allowed in PrimitiveTransformation (T12) | SD3 R4 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates | "Causes the shift to be computed based on this key and the context. … Can only be applied to table items."; `"fixedSizeBucketingConfig": { object (FixedSizeBucketingConfig)` in PrimitiveTransformation (the discovery document itself not opened, by rule) | MATCH |
| 13 | transformationErrorHandling documented in REST (T57) | SD3 R4, SD3 R8 | same | "Mode for handling transformation errors. If left unspecified, the default mode is TransformationErrorHandling.ThrowError." / LeaveUntransformed "Skips the data without modifying it if the requested transformation would cause an error." | MATCH |
| 14 | Two findings for one string (T54) | SD3 R4 | https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes | "then you get two findings for the same string—one for DRIVERS_LICENSE_NUMBER and one for GERMANY_DRIVERS_LICENSE_NUMBER" | MATCH |
| 15 | AES-SIV length conflict, three statements (T14, changed Summary) | SD4 R4, INV(c) | transformations-reference; https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization | "Replaces an input value with a token, or surrogate value, of the same length using AES in Synthetic Initialization Vector mode (AES-SIV)." / "Does not preserve the character set ("alphabet") or length of the input value post-encryption" / "This method produces a hashed value, so it does not preserve the character set or the length of the input value." | MATCH |
| 16 | Re-identify response fields (T17, changed Summary) | SD4 R5 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse | "The re-identified item." / "An overview of the changes that were made to the item." | MATCH |
| 17 | KMS-wrapped key needs dlp.kms.encrypt (T63) | SD4 R4 | https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates | "Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt" | MATCH |
| 18 | Face detector in Preview (T18, changed Summaries) | SD5 R1, SD5 R2, INV(b) | https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference ; release notes | "OBJECT_TYPE/PERSON/FACE \| Image of a person's face. This infoType detector is in Preview." / "available in Preview in global and the asia, europe, and us multi-regions" (December 15, 2025); the word "Preview" appears once in the reference | MATCH |
| 19 | Pre-GA terms (T73, merger addition) | SD5 R2 | https://cloud.google.com/terms/service-terms | "5. Pre-GA Offerings Terms." … "Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity." | MATCH |
| 20 | Image-context definitions are "one-sentence" (T16, changed Summary) | SD6 R2 Summary, SD6 R8 | https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference | "A finding of this type indicates that an image contains violent or gory content either real or fictionalized. Violent content might include imagery related to death, serious injury, or harm …" (two sentences; SEXUALLY_EXPLICIT and SEXUALLY_SUGGESTIVE also two) | MISMATCH (fix 2) |
| 21 | Classifier trained on real-world images; produces a label (T16, changed Summaries) | SD6 R4, SD6 R5 | https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction ; https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types | "are primarily trained and evaluated on real-world images." / "analyzes the entire image to assign a single theme or category and produces a label or classification." | MATCH |
| 22 | Content-policy surface: REST methods, client methods, permission, role, Gemini service account (T9) | SD1 R4, SD1 R8, INV(a) | REST projects.locations.contentPolicies; client.py at tag; https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions ; https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies | Methods "create … delete … get … list … patch" only; `client.py:7363` "def create_content_policy(", with update, get, list, delete and no evaluate or apply method; "DLP Content Policies Consumer … Apply content policies."; DLP User "Inspect, Redact, and De-identify Content" with dlp.contentPolicies.apply, dlp.kms.encrypt, dlp.locations.*, serviceusage.services.use; "grant the DLP User (roles/dlp.user) role to your Gemini Enterprise service account" | MATCH |
| 23 | Pricing method table | SD4 R6, SD5 R6, SD6 R6, INV(e) | https://cloud.google.com/sensitive-data-protection/pricing | "API method \| Content inspection \| Content transformation \| projects.image.redact \| Yes \| No \| projects.content.inspect \| Yes \| No \| projects.content.deidentify \| Yes \| Yes \| projects.content.reidentify \| Yes \| Yes" | MATCH |
| 24 | SLA covered services (T22) | SD4 R6, SD5 R6, INV(e) | https://cloud.google.com/sensitive-data-protection/sla | ""Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests." | MATCH |
| 25 | Customer Data terms; SDP listed; no SDP section in the Service Specific Terms (T92) | SD1, SD3 to SD6 R8, INV(f) | https://cloud.google.com/terms ; https://cloud.google.com/terms/services ; https://cloud.google.com/terms/service-terms ; https://cloud.google.com/terms/data-processing-addendum | "5.2 Protection of Customer Data. Google will only access, use, and otherwise process Customer Data in accordance with the Cloud Data Processing Addendum and will not access, use, or process Customer Data for any other purpose." / "Sensitive Data Protection (including Cloud Data Loss Prevention or DLP): …" / Service Specific Terms: the name appears only in the navigation / DPA "a. to provide, secure, and monitor the Services and TSS (if applicable); and b. as further specified via: …" | MATCH (label: fix 1) |
| 26 | Benchmarking clause and AUP (T93) | SD6 R7, SD6 R8 | https://cloud.google.com/terms/service-terms ; https://cloud.google.com/terms/aup | "7. Benchmarking. Customer may itself (but may not permit a third party to): (a) conduct benchmark tests of the Services" … "(i) the public disclosure includes all necessary information to replicate the Tests" / "illegal activity, including child sexual exploitation" / "Non-consensual Explicit Imagery (NCEI)" | MATCH |
| 27 | Region lists and the 2026-01-20 note (T83) | INV(f) | https://docs.cloud.google.com/sensitive-data-protection/docs/locations ; https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest ; release notes | locations lists "asia-southeast3"; REST root has no "asia-southeast3"; "Sensitive Data Protection is available in the asia-southeast3 (Bangkok) region." (January 20, 2026) | MATCH |
| 28 | Image formats docstring at tag (T66) | SD5 R6, INV(a) | https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py | `dlp.py:2705` "The content must be PNG, JPEG, SVG or BMP."; `:1625` `IMAGE_SVG = 4` | MATCH |
| 29 | Other cited code lines at tag | SD1 R3 to R7, SD3, SD4, SD5 | client.py, dlp.py, storage.py, setup.py, README.rst, gapic_version.py at tag | `client.py:1151` "def reidentify_content("; `dlp.py:3084` "class ReidentifyContentResponse"; `:2845` "class RedactImageResponse"; `:2641` "Top coordinate of the bounding box. (0,0) is"; `:5449` "Mode for handling transformation errors. If left"; `:6484` "dlp.kms.encrypt"; `storage.py:194` "Optional version name for this InfoType."; `setup.py:95` `python_requires=">=3.10",`; `:45` `"google-api-core[grpc] >= 2.28.0, <3.0.0",`; `README.rst:88` "pip install google-cloud-dlp"; `gapic_version.py:16` `__version__ = "3.40.0"` | MATCH |
| 30 | Sample repo and archive facts (T79, T81) | INV(d) | dlp-dataflow-deidentification@4213e271; python-dlp@21b91b9d; google-cloud-python CHANGELOG at tag | "Creates a bucket ({project-id}-demo-data) in the us-central1 region" / "Creates a BigQuery dataset (demo_dataset) in the US multi-region"; permissions yaml lists serviceusage.services.use, dlp.kms.encrypt, dlp.inspectTemplates.get/list, dlp.deidentifyTemplates.get/list; LICENSE "Apache License Version 2.0"; python-dlp README "This github repository is archived. The repository contents and history have moved to"; CHANGELOG "[3.40.0] … (2026-10-01)" | MATCH |
| 31 | Latency notes on nine infoTypes | INV(b) person and place rows | https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference | "Not recommended for use during latency sensitive operations." appears 9 times: PERSON_NAME, FIRST_NAME, LAST_NAME, FEMALE_NAME, MALE_NAME, DATE_OF_BIRTH, STREET_ADDRESS, LOCATION, ORGANIZATION_NAME | MATCH |
| 32 | Stored-infoType read permissions in Reader and Viewer, not in DLP User (T51) | SD2 R6 | https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions | DLP Viewer (roles/dlp.viewer) and DLP Reader (roles/dlp.reader) list "dlp.storedInfoTypes.get" and "dlp.storedInfoTypes.list"; DLP User lists no dlp.storedInfoTypes permission | MATCH |
| 33 | Conversation and batch notes say inspecting and de-identifying only (T60) | SD1 R1, SD3 R3, SD4 R3 | release notes | "Added support for inspecting and de-identifying conversational content." (June 03, 2026) / "Added support for inspecting and de-identifying batched content." (June 12, 2026) | MATCH |

**Tally: 33 checked, 31 MATCH, 2 MISMATCH (rows 11 and 20), 0 UNVERIFIABLE.**

Quote sweep (`quote_sweep.py`):
- 523 quoted fragments from both final files were checked against the union of the 84 fetched official pages and the client files at the tag, after whitespace and curly-quote normalisation.
- 514 were found verbatim.
- The other 9 are not quotes:
  - 4 are cross-product header strings in double quotes (SD1 R4, SD3 R4);
  - 4 are the draft's own words between quoted prices (SD1 R6, SD3 R6);
  - 1 is the word list in "the crypto hash reads ..." (SD3 R4).
- No misquote was found.

## 5. Inventory consistency (Check 5)

- **Row counts** (checker): (a) 15, (b) 24, (c) 12, (d) 13, (e) 16, (f) 7 = 87. These match sdp_changes.md section 0 and the config numbers it gives main for `build_sdp_inventory.py`. Cell counts per table: 8, 7, 8, 8, 4, 4.
- **Covered-by validity** (checker, plus my reading). Every cell is a ";" list of the exact six SD headers or the single marker `— (inventory only, not in Table 3)`; that marker is used on 15 rows. No legacy or planned marker is used.
  - (a) content.inspect maps to SD1, SD2, SD5 and SD6. content.deidentify maps to SD3 and SD4; content.reidentify to SD4; image.redact to SD5 and SD6; the inspection template to SD1; the de-identification template to SD3; the stored infoType to SD2; infoTypes.list to SD1. The content policy and the six storage or job rows carry the marker (R018, R011).
  - (b) Text groups map to SD1, image objects to SD5 and image context to SD6.
  - (c) All 12 rows map to SD3. FPE and AES-SIV also map to SD4. The hash row maps to SD3 only (T65 ruling).
  - (d) REST global, REST regional, Python and other libraries map to all six. Apigee maps to SD3 and SD5. The other 8 rows carry the marker; Model Armor is named in text only (R012).
  - All consistent with the columns.
- **Labels.** Only allowed forms appear: [Documented] 343, [Documented: repo …] 19 (googleapis/google-cloud-python@google-cloud-dlp-v3.40.0 12, GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271 4, GoogleCloudPlatform/community@6f68203d 2, googleapis/python-dlp@21b91b9d 1), [Inferred] 82, [Not disclosed] 25, [To be verified] 4. No invented forms.
- **Repo pins in the Source URL cells.** Each pinned label has a URL at the same ref in its row. The exception is the two files named only in the Dataflow row's text (optional suggestion).
- **Forbidden characters.** `**` occurs 0 times and backticks 0 times; there is no literal pipe in a cell (the parser asserts equal cell counts).
- **Scope paragraph.** "DOCS slug = https://docs.cloud.google.com/sensitive-data-protection/docs/slug" is a placeholder, not a URL, and is not in any Source URL cell.
- **Label issue in a cell:** INV(f) Data handling (fix 1).

## 6. URLs (Check 6, appendix)

**Method.**
- Harvested only R9 bullets and the inventory Source URL cells, as main asked: 96 distinct URLs, 0 googleapis.com hosts, 0 `{…}` templates.
- Command: `curl -s -o /dev/null -L --max-time 30 -A "Mozilla/5.0" -w "%{http_code} %{url_effective}"`, with one retry on a non-200.
- The 12 github.com URLs were requested as their raw.githubusercontent.com equivalents at the same tag or sha (R020).
- Raw output: `scratchpad/verifier/sdp/url_check.txt`.

**Result: 96 of 96 return 200. No 403, 404 or other failure.** Two redirects are worth noting:
- `organizations.deidentifyTemplates` answers 301 to `projects.deidentifyTemplates` (optional suggestion).
- `cloud.google.com/dlp/demo` answers 302 to the trailing-slash URL; this is already recorded in the resolutions.

| URL | Status | Used in |
|---|---|---|
| https://cloud.google.com/dlp/demo | 200 (HTTP 302 to trailing-slash URL) | INV(d) |
| https://cloud.google.com/sensitive-data-protection/pricing | 200 | INV(a), INV(c), INV(d), INV(e), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://cloud.google.com/sensitive-data-protection/sla | 200 | INV(e), SD1 R9, SD3 R9, SD4 R9, SD5 R9 |
| https://cloud.google.com/terms | 200 | INV(f), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://cloud.google.com/terms/aup | 200 | SD6 R9 |
| https://cloud.google.com/terms/data-processing-addendum | 200 | INV(f), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://cloud.google.com/terms/service-terms | 200 | INV(f), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://cloud.google.com/terms/services | 200 | INV(f), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://docs.apigee.com/api-platform/reference/extensions/google-cloud-data-loss-prevention/google-cloud-data-loss-prevention-extension-120 | 200 | INV(d) |
| https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp | 200 | INV(d) |
| https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data | 200 | INV(a), INV(d), INV(e), INV(f), SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/kms/docs/destroy-restore | 200 | SD4 R9 |
| https://docs.cloud.google.com/kms/docs/key-rotation | 200 | SD4 R9 |
| https://docs.cloud.google.com/kms/docs/locations | 200 | SD4 R9 |
| https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog | 200 | SD4 R9 |
| https://docs.cloud.google.com/model-armor/overview | 200 | INV(a), INV(d), SD1 R9, SD5 R9 |
| https://docs.cloud.google.com/model-armor/sanitize-prompts-responses | 200 | INV(d), SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions | 200 | INV(a), SD1 R9, SD2 R9, SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints | 200 | INV(d), INV(e), INV(f), SD1 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/audit-logging | 200 | SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/auth | 200 | INV(d), SD4 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting | 200 | SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage | 200 | INV(a) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-hybrid-jobs | 200 | INV(a) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction | 200 | INV(b), SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes | 200 | INV(b), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers | 200 | INV(a), INV(e) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types | 200 | INV(a), INV(d), INV(f), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis | 200 | INV(a) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates | 200 | INV(a), INV(d), SD1 R9, SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction | 200 | SD1 R9, SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy | 200 | INV(a), INV(d), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels | 200 | SD1 R9, SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key | 200 | SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes | 200 | INV(a), SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary | 200 | SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood | 200 | SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex | 200 | SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules | 200 | SD2 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes | 200 | INV(a), SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles | 200 | INV(a), INV(d) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-bq-tutorial | 200 | INV(d) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data | 200 | INV(a), INV(c), INV(e), SD1 R9, SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage | 200 | INV(a), INV(d) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference | 200 | INV(a), INV(b), INV(f), SD1 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api | 200 | INV(d), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify | 200 | SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images | 200 | INV(a), SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage | 200 | INV(a), INV(d) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text | 200 | SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text | 200 | SD1 R9, SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/libraries | 200 | INV(d), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood | 200 | INV(b), SD1 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/listing-infotypes | 200 | INV(a) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/locations | 200 | INV(d), INV(f), SD1 R9, SD3 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies | 200 | INV(a), INV(d), INV(f), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization | 200 | INV(c), SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/quote | 200 | SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images | 200 | INV(a), SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest | 200 | INV(a), INV(f) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem | 200 | INV(a), INV(e), SD1 R9, SD2 R9, SD3 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DeidentifyContentResponse | 200 | SD2 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig | 200 | INV(e), SD1 R9, SD2 R9, SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectContentResponse | 200 | SD2 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult | 200 | SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse | 200 | SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex | 200 | SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse | 200 | SD2 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates | 200 (HTTP 301 to https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates) | SD5 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify | 200 | INV(a), SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect | 200 | INV(a), SD1 R9, SD2 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify | 200 | INV(a), INV(c), SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates | 200 | SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact | 200 | INV(a), SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/reidentify | 200 | SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies | 200 | INV(a), INV(f), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact | 200 | SD5 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2 | 200 | INV(a), SD1 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes | 200 | INV(a), INV(b), INV(e), INV(f), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview | 200 | INV(a), INV(d), INV(f), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location | 200 | INV(d), INV(f) |
| https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types | 200 | INV(a), SD3 R9, SD5 R9, SD6 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference | 200 | INV(b), INV(c), SD3 R9, SD4 R9 |
| https://docs.cloud.google.com/sensitive-data-protection/limits | 200 | INV(a), INV(d), INV(e), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://github.com/GoogleCloudPlatform/community/blob/6f68203dec458268f177e97e2b57f3e085ca3668/archived/dlp-hybrid-inspect/index.md | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
| https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification/blob/4213e271f5889c7b889d98ab5b0623f1406687b0/README.md | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/CHANGELOG.md | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/LICENSE | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/README.rst | 200 (raw.githubusercontent.com at the same ref, R020) | SD1 R9, SD4 R9 |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py | 200 (raw.githubusercontent.com at the same ref, R020) | SD1 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py | 200 (raw.githubusercontent.com at the same ref, R020) | INV(a), INV(d), SD1 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/transports/rest.py | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py | 200 (raw.githubusercontent.com at the same ref, R020) | INV(a), INV(e), SD1 R9, SD2 R9, SD3 R9, SD4 R9, SD5 R9, SD6 R9 |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/storage.py | 200 (raw.githubusercontent.com at the same ref, R020) | SD1 R9, SD2 R9 |
| https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/setup.py | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d), SD1 R9, SD3 R9, SD4 R9 |
| https://github.com/googleapis/python-dlp/blob/21b91b9d51d4b21784ddede99d16ff15279c8f52/README.rst | 200 (raw.githubusercontent.com at the same ref, R020) | INV(d) |
