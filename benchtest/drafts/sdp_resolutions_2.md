# SDP resolutions 2 (P5, gr-resolver): items T50 to T98, classes a and c (plus T68 on request)

Date: 2026-10-09. Product: sdp. Triage: `benchtest/drafts/sdp_triage.md`. Another resolver handles T1 to T49 (`sdp_resolutions_1.md`); nothing in that range is touched here. Line numbers below are the line numbers of `sdp_cols_a.md` (A), `sdp_cols_b.md` (B) and `sdp_inventory.md` (INV) as read on 2026-10-09; locate by the quoted start of the bullet if lines have moved.

## Items handled (32)

Priority H first, then M, then L, in this order: T51, T54, T60, T62, T66, T68 (class b, re-read as asked), T52, T57, T63, T64, T65, T73, T78, T79, T88, T89, T91, T92, T93, T97, T80, T81, T83, T84, T85, T86, T87, T90, T94, T95, T96, T98.

Items settled by a ruling: none in this range (R018 covers T1 to T4 only; R019 is cited under T92 to T95).

## Items not handled (class b, they stay open for the bench)

T50, T53, T55, T56, T58, T59, T61, T67, T69, T70, T71, T72, T74, T75, T76, T77, T82. None of them is a doc-answerable item; the triage names no re-read that could settle them. Two notes that help the merger: (1) T56: the phrase "HMAC-SHA-256" is on the transformation reference and the pseudonymization page (see T88), so the inventory hash row is supported; the 32-byte hexadecimal versus base64 conflict still needs one request. (2) T72: the client `BytesType` docstring says "Only the first frame of each multiframe image is inspected. Metadata and other frames aren't inspected." (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1577`); that concerns inspection, not whether EXIF survives redaction, so T72 stays open.

## Method and access notes

- Docs pages were read as raw text with `python benchtest/tools/fetch_text.py` (status 200 unless stated) and saved under `benchtest/scratchpad/resolver/` (shared with the other resolver) and `benchtest/scratchpad/resolver/r2/` (mine). Quotes below are copied from that raw text with whitespace normalised.
- Code: shallow or sparse clones under /tmp per R013: `googleapis/google-cloud-python` at tag `google-cloud-dlp-v3.40.0` (commit 69401247a72c0f0786741ac937c3c5aa2afc8ead; `git ls-remote --tags` shows 3.40.0 is still the latest `google-cloud-dlp-v*` tag on 2026-10-09), `googleapis/python-dlp` (commit 21b91b9d51d4b21784ddede99d16ff15279c8f52), `GoogleCloudPlatform/dlp-dataflow-deidentification` (4213e271f5889c7b889d98ab5b0623f1406687b0) and `GoogleCloudPlatform/community` (sparse, 6f68203dec458268f177e97e2b57f3e085ca3668). The last two are Google sample or tutorial repositories: supporting only (R013), never a source for product behaviour.
- Terms pages (R019 allows them): `cloud.google.com/terms`, `/terms/service-terms`, `/terms/aup`, `/terms/data-processing-addendum`, `/terms/services`, read 2026-10-09.
- Cloud KMS and Cloud Logging pages are Google docs but not SDP docs; they are flagged that way in the labels.
- **Rule exception to disclose.** While URL-checking the drafts I ran a read-only script over every URL string in A, B and INV, including four code-pattern strings that are not source URLs. It sent four unauthenticated GET requests to `dlp.googleapis.com/v2/{parent=projects/*}/content:inspect`, `/content:deidentify`, `/image:redact` (all with a literal brace-and-asterisk path) and to `www.googleapis.com/auth/cloud-platform`. All four returned HTTP 400 with no data sent and nothing read back. This was an oversight under the "no vendor API calls" rule; no credentials, content or request bodies were involved. The URL check results below exclude those four strings. The url-checker should exclude code-pattern strings too (they appear inside Detail bullets, not in R9 or Source URL cells).
- Mechanical checks re-run: `check_drafts.py columns` on A and B gives 0 errors, 0 warnings; `check_drafts.py inventory sdp_inventory.md --headers <A+B concatenated>` gives 0 errors, 0 warnings, tables 15/24/12/13/16/7 rows (the tool accepts one headers file, so A and B were concatenated in the scratchpad).
- Whole-draft quote sweep (supports T96): every double-quoted fragment of 15 characters or more in A, B and INV (477 fragments) was matched, after case, whitespace and punctuation normalisation, against all saved page texts and the five tag files (dlp.py, client.py, setup.py, CHANGELOG.md, README.rst). 467 match verbatim. The 10 that do not match are not mis-quotations of Google text: 5 are the draft's own words between two quoted prices (A 148 twice, A 490 three times; the quoted prices and the 1 KB minimum are on the pricing page, "$0.00 (Free) / 1 gibibyte, per 1 month / account"), 2 are Python class paths that sit in `types/storage.py`, which was not in the sweep corpus (A 300 is at `storage.py:334` and A 351 at `storage.py:338`, both confirmed by grep at the tag) and 3 are descriptive phrases the draft put inside quote marks (A 426 once, A 451 twice). The merger may drop those quote marks.

---

## Priority H

### T51 — Is `roles/dlp.user` enough to use a stored infoType in `content.inspect`?
- Verdict: STILL OPEN (checked the roles page, REST `content.inspect`, REST ContentItem, creating-stored-infotypes and audit-logging pages; no page states a requirement). New documented facts to add; the question stays a permission test.
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions : "DLP User (roles/dlp.user) Inspect, Redact, and De-identify Content | dlp.contentPolicies.apply dlp.kms.encrypt dlp.locations.* dlp.locations.get dlp.locations.list serviceusage.services.use". The list holds no `dlp.storedInfoTypes.*` entry.
  - Same page: "DLP Reader (roles/dlp.reader) Read DLP entities, such as jobs and templates." with `dlp.storedInfoTypes.get`, `dlp.storedInfoTypes.list`, `dlp.inspectTemplates.get` and `dlp.deidentifyTemplates.get` in its list; DLP Viewer (`roles/dlp.viewer`) also holds `dlp.storedInfoTypes.get` and `.list`.
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect : "Authorization requires the following IAM permission on the specified resource parent: serviceusage.services.use" (the same sentence is on the deidentify, reidentify and image.redact REST pages).
  - https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-bq-tutorial : the Cloud Run service account is given both `roles/dlp.reader` and `roles/dlp.user` for a service that calls de-identification templates.
  - Supporting only (Google sample, R013): `GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271`, `dlp_tokenizing_runner_permissions.yaml:22-27` lists `serviceusage.services.use`, `dlp.kms.encrypt`, `dlp.inspectTemplates.get`, `dlp.inspectTemplates.list`, `dlp.deidentifyTemplates.get`, `dlp.deidentifyTemplates.list` for a runner that uses templates; no stored-infoType permission.
- Label: [Documented] for the role contents; [Not disclosed] for the requirement (named pages checked); [Inferred] only if a sentence says Reader is needed for stored infoTypes (premise: Reader holds `dlp.storedInfoTypes.get`; the BigQuery tutorial pairs Reader with User).
- Draft impact:
  - A SD2 R6, bullet starting "The caller's role `roles/dlp.user` lists only" (line 344, now `[To be verified]`). Replace with these three bullets:
    - `• `roles/dlp.user` is "Inspect, Redact, and De-identify Content" and lists `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*` and `serviceusage.services.use`, with no `dlp.storedInfoTypes.*` permission (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**`
    - `• `dlp.storedInfoTypes.get` and `dlp.storedInfoTypes.list` are listed under DLP Reader (`roles/dlp.reader`) and DLP Viewer (`roles/dlp.viewer`), and the REST `content.inspect` page names only `serviceusage.services.use` on the parent (SDP docs, roles and permissions and REST projects.content.inspect pages, read 2026-10-09) **[Documented]**`
    - `• Whether a request that names a stored infoType needs `dlp.storedInfoTypes.get` on top of `roles/dlp.user` (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; not stated) **[Not disclosed]**`
  - A SD2 R8 #4 (line 364): replace with `• Whether `roles/dlp.user` alone is enough to use a stored infoType in `content.inspect`: the role holds no stored-infoType permission and no page states what the request needs (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; needs a permission test)`.
  - A SD2 R8 Summary: no change (it already lists "permissions for stored infoTypes").
  - A SD2 R9: the roles URL is already listed. No new URL needed.
  - Optional, INV(d) BigQuery row, "Auth" cell: replace "Roles and service accounts are set in the tutorial steps [To be verified] (not read in detail)" with "The tutorial gives the Cloud Run service account roles/dlp.reader and roles/dlp.user [Documented] (DOCS deidentify-bq-tutorial)" (see T79).

### T54 — Overlapping findings of different infoTypes in de-identification
- Verdict: STILL OPEN (checked the de-identifying page, transformation reference, text-redaction concept page, infoTypes concepts, the inspect-and-de-identify quickstart, REST `content.deidentify` and the `DeidentifyConfig` and `InfoTypeTransformations` schema on the deidentifyTemplates REST page; no sentence says how two overlapping findings that each have a transformation are applied). One related inspection fact found.
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes : "if a string that you inspect matches the GERMANY_DRIVERS_LICENSE_NUMBER infoType and you scanned for both DRIVERS_LICENSE_NUMBER and GERMANY_DRIVERS_LICENSE_NUMBER in your request, then you get two findings for the same string".
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates (schema `InfoTypeTransformations`): "Required. Transformation for each infoType. Cannot specify more than one for a given infoType." This limits transformations per infoType, not overlap.
- Label: [Documented] for the two quotes; [Not disclosed] for the de-identification behaviour (pages checked).
- Draft impact:
  - A SD3 R4: add two bullets after the bullet on the no-infoType default:
    - `• When a string matches both a general and a specific infoType and both are requested, inspection reports two findings for it: "you get two findings for the same string" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**`
    - `• How de-identification applies two transformations to overlapping findings of different infoTypes is not described (checked the de-identifying, transformation reference, text redaction and infoTypes concepts pages and the REST deidentify and InfoTypeTransformations references) **[Not disclosed]**`
  - A SD3 R8 #4 (line 513): keep unchanged (still a test). R8 Summary unchanged. SD3 R9 already lists `concepts-infotypes`.

### T60 — Does `content.reidentify` accept conversation and batch items?
- Verdict: STILL OPEN (checked REST `content.reidentify`, ContentItem, release notes and the client; none says so). Absence now confirmed in the client too.
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify : "The item to re-identify. Will be treated as text." (field `item`, type ContentItem).
  - https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes : "Added support for inspecting and de-identifying conversational content. You can now include a Conversation in your ContentItem requests." (June 03, 2026) and "Added support for inspecting and de-identifying batched content." (June 12, 2026). Neither says "re-identifying".
  - `google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:3028` `ReidentifyContentRequest.item`: "The item to re-identify. Will be treated as text."
- Label: [Not disclosed] (pages and client checked).
- Draft impact: none to Detail text (B SD4 R8 #3 at line 154 is accurate). Optional addition to B SD4 R3 or R6, one bullet: `• The `item` of a re-identification request is a ContentItem "treated as text"; the release notes announce conversation and batch support for inspecting and de-identifying only (SDP docs, REST reidentify and release-notes pages, read 2026-10-09) **[Not disclosed]**` (reads as an absence claim about re-identification support). A SD1 R3 and SD3 R3 conversation bullets are unaffected. No Summary change.

### T62 — What happens to issued tokens when the Cloud KMS key is rotated or destroyed?
- Verdict: PARTLY RESOLVED. Cloud KMS docs (not SDP docs) answer the key-version mechanics; the SDP-specific effect on tokens is an inference that still needs a test.
- Evidence:
  - https://docs.cloud.google.com/kms/docs/key-rotation (Cloud KMS docs, not SDP docs): "Rotating keys creates new active key versions, but doesn't re-encrypt your data and doesn't disable or delete previous key versions."
  - https://docs.cloud.google.com/kms/docs/destroy-restore (Cloud KMS docs, not SDP docs): "After a key is destroyed, data that was encrypted with the key version can't be decrypted."
  - https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify (SDP quickstart): "Warning: When you destroy a key version, you can no longer decrypt content that was encrypted using that version of the key."
  - https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key : the wrapped key is made by calling Cloud KMS `cryptoKeys:encrypt` on an AES key ("That is your wrapped key.").
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates (schema `CryptoKey`): "This is a data encryption key (DEK) (as opposed to a key encryption key (KEK) stored by Cloud Key Management Service (Cloud KMS)."
- Label: [Documented] for each quote (KMS ones flagged "Cloud KMS docs, not SDP docs"); the application to SDP tokens is [Inferred] (premise: the wrapped key is a DEK encrypted by a KMS key, so a destroyed key version makes the wrapped key, and so the tokens, unrecoverable; rotation leaves old versions usable).
- Draft impact:
  - B SD4 R8 #6 (line 157): replace with `• Effect of rotating or destroying a Cloud KMS key version on tokens already issued: the Cloud KMS pages say rotation does not disable earlier versions and destruction makes data encrypted with that version undecryptable, but no SDP page says how re-identification behaves (checked the quickstart, create-wrapped-key, pseudonymization and REST pages; needs testing)`.
  - B SD4 R6 (or R4), add three bullets:
    - `• Cloud KMS: "Rotating keys creates new active key versions, but doesn't re-encrypt your data and doesn't disable or delete previous key versions." (Cloud KMS docs, not SDP docs, key rotation page, read 2026-10-09) **[Documented]**`
    - `• Cloud KMS: "After a key is destroyed, data that was encrypted with the key version can't be decrypted." (Cloud KMS docs, not SDP docs, destroy and restore page, read 2026-10-09) **[Documented]**`
    - `• Destroying the key version that wrapped the data key would stop re-identification, while rotation alone would not (premise: the wrapped key is a data encryption key encrypted by a Cloud KMS key, per the wrapped-key page and the REST CryptoKey schema, and the quickstart warns that destroying a key version stops decryption) **[Inferred]**`
  - B SD4 R9: add `https://docs.cloud.google.com/kms/docs/key-rotation` and `https://docs.cloud.google.com/kms/docs/destroy-restore` (one URL per bullet, no commentary). Also add `https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates` if the CryptoKey schema bullet is added.
  - Summary: B SD4 R8 Summary stays ("what happens to old tokens when keys change" is still a test).

### T66 — Image formats, documentation side (conflict C1)
- Verdict: RESOLVED (documentation side). All six statements in B SD5 R6 re-read verbatim; table headers confirmed; the conflict itself stays open and goes to the bench (T67). The inventory row carries three of the six statements and must carry all of them.
- Evidence (raw text, 2026-10-09):
  - REST: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact : "The content must be PNG, JPEG, SVG or BMP." (field `byteItem`). The client docstring repeats it: `google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2705` "The content must be PNG, JPEG, SVG or BMP."
  - Redaction guide https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images : "Sensitive Data Protection can redact sensitive data from many image types, including JPEG, BMP, and PNG." and "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files."
  - Inspect guide https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images : "Sensitive Data Protection can inspect many image types for sensitive data, including JPEG, BMP, PNG, and SVG."
  - Method types https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types : "Obfuscate sensitive text in image formats (such as JPEG, PNG, or TIFF) by overlaying opaque rectangles".
  - Supported file types https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types : the first table, "Supported file types in inspection and de-identification operations", has the columns "File type | File extensions | Limits | Scanning mode | Transformation support". Its Image row reads "bmp, gif, jpe, jpeg, jpg, png" | (Limits empty) | "OCR, Image content detection, Image content classification" | "Redaction". The second table, "Supported file clusters in discovery operations", lists Images as "bmp, gif, heic, ico, jpe, jpeg, jpg, pm, png, svg, tiff, webp" and says "Supported images (bmp, gif, jpe, jpeg, jpg, and png) smaller than 4 MiB are scanned using OCR in regions that support image scanning."
  - Client enum: `dlp.py@google-cloud-dlp-v3.40.0:1625` `IMAGE_SVG = 4`; the enum has `IMAGE` ("Any image type."), `IMAGE_JPEG`, `IMAGE_BMP`, `IMAGE_PNG`, `IMAGE_SVG`, no GIF.
  - The first table does not say which methods apply to its rows (it covers jobs and content methods under one heading); its Limits cell is empty for images.
- Label: [Documented] for each statement (pages) and [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] for the enum and docstring; the conflict statement stays [Inferred].
- Draft impact:
  - B SD5 R6: no change; the six bullets plus the discovery-table bullet are accurate. Optional extra bullet after statement 6: `• The client docstring for the redact request repeats the REST wording: "The content must be PNG, JPEG, SVG or BMP." (dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2705) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**`. B SD5 R6 Summary unchanged.
  - INV(a) "Image redaction" row, "Input types" cell: replace the text from "The REST reference says the content must be PNG, JPEG, SVG or BMP" up to "...GIF appears only in the third)" with:
    `The REST reference says the content must be PNG, JPEG, SVG or BMP [Documented] (REST redact). The Python docstring at the tag repeats it [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (types/dlp.py RedactImageRequest). The redaction guide says it can redact many image types including JPEG, BMP and PNG, and that content redaction is not supported for SVG, PDF, XLSX, PPTX or DOCX files [Documented] (DOCS redacting-sensitive-data-images). The inspect guide says it can inspect many image types including JPEG, BMP, PNG and SVG [Documented] (DOCS inspecting-images). The method-types page names JPEG, PNG or TIFF as redaction formats [Documented] (DOCS concepts-method-types). The inspection and de-identification table on the supported-file-types page lists bmp, gif, jpe, jpeg, jpg and png for images, with Redaction under Transformation support [Documented] (DOCS supported-file-types). The client enum has IMAGE, IMAGE_JPEG, IMAGE_BMP, IMAGE_PNG and IMAGE_SVG and no GIF [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (types/dlp.py BytesType). The statements do not agree on SVG, GIF and TIFF [Inferred] (premise: SVG is accepted in the REST and inspect texts and excluded in the redaction guide; GIF appears only in the file-types table; TIFF only on the method-types page).`
    The existing sentence "Only the first frame of a multiframe image is redacted [Documented] (REST redact)" stays.
  - INV(a) "Image redaction" Source URL cell: `https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images` is not in the cell; add it (the inspect-guide statement now cites it) and add `https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py`.
  - INV Reviewer notes (moves to the change log): "Image formats" conflict bullet: change "three statements" to "six statements" and drop "The Python docstring at the tag repeats the REST wording" as a separate remark (now a labelled fact in the cell).
  - B SD6 R6 carry-over bullet and R8 #10: no change.
  - Summaries: none change.

### T68 — Bounding-box origin (class b, re-read as asked)
- Verdict: STILL OPEN (all four statements re-read verbatim; no further page decides it; needs a request on an image with a known box).
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult (BoundingBox): "Top coordinate of the bounding box. (0,0) is upper left." and "Left coordinate of the bounding box. (0,0) is upper left."
  - Client: `google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2641` (class `BoundingBox` at 2634): "Top coordinate of the bounding box. (0,0) is upper left."
  - https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images : "The coordinates at the bottom left corner of an image are (0,0)."
  - https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction : "Each set of pixel coordinate and dimension values indicates the bottom-left corner and the dimensions of bounding boxes, respectively."
  - The guide's sample output (`"top": 383, "left": 419, "width": 82, "height": 38`) is printed without the image size, so the sample cannot settle it either. The response field names are `top` and `left`, not `bottom`, which fits the REST text but is not a documented tiebreak [Inferred].
- Label: stays [Documented] for each of the four statements (two sides recorded as separate bullets, README rule 4); the test is the only way to pick a side.
- Draft impact: none. B SD5 R5 bullets (lines 279 to 282) are accurate and B SD5 R7 already tells the bench to check the origin. B SD5 R8 #3 stays. No Summary change.

---

## Priority M

### T52 — Limits and region availability for `contentMetadata`, labels, metadata-label detectors and image rules
- Verdict: STILL OPEN (checked REST ContentItem, the limits page, the locations page, the metadata-label page and the release notes of 2026-06-29 and 2026-06-23; none states a size limit, label count or region list).
- Evidence: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem : `contentMetadata` is "User provided metadata for the content."; `properties[]` "User provided key-value pairs of content metadata."; `fileLabels[]` "Optional. The file labels associated with the content." No numeric limit. Release note 2026-06-29: "You can configure Sensitive Data Protection to detect specific file labels, which can represent Google Drive labels or Microsoft sensitivity labels." Release note 2026-06-23: "Image safety classification infoTypes are now supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." Neither names regions.
- Label: [Not disclosed] if written as a bullet; R8 bullets are unlabelled.
- Draft impact: none. A SD2 R8 #6 and #8 (lines 363 and 365) are accurate as written ("checked the ContentItem and limits pages; not stated"). Optionally add "and the metadata-label page and release notes" to both parentheses.

### T57 — Is `transformationErrorHandling` documented in the REST `DeidentifyConfig` reference?
- Verdict: CORRECTION. The draft says "only the client describes it"; the REST reference documents it.
- Evidence: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates (schema `DeidentifyConfig`, repeated on the organisation-level page): `transformationErrorHandling` — "Mode for handling transformation errors. If left unspecified, the default mode is TransformationErrorHandling.ThrowError." Schema `TransformationErrorHandling`: "A transformation error occurs when the requested transformation is incompatible with the data." `ThrowError`: "Throw an error and fail the request when a transformation error occurs." `LeaveUntransformed`: "Skips the data without modifying it if the requested transformation would cause an error." The REST `content.deidentify` page takes the same type: field `deidentifyConfig` is "object (DeidentifyConfig)". Page fetched 2026-10-09; the `DeidentifyConfig` anchor is on this page, not on its own URL (`/reference/rest/v2/DeidentifyConfig` returns 404).
- Label: [Documented].
- Draft impact:
  - A SD3 R4, after the client bullet "Transformation errors:" (line 453), add:
    `• The REST reference documents the same field on `DeidentifyConfig`: "Mode for handling transformation errors. If left unspecified, the default mode is TransformationErrorHandling.ThrowError."; `LeaveUntransformed` "Skips the data without modifying it if the requested transformation would cause an error." (SDP docs, REST deidentifyTemplates page, read 2026-10-09) **[Documented]**`
  - A SD3 R8 #6 (line 515): replace with `• Whether `LeaveUntransformed` behaves as documented on a plain `content.deidentify` request, for example for a date shift applied to an IP address (the REST reference documents the field; needs testing)`.
  - A SD3 R9: add `https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates`.
  - Summaries: none change (no Summary mentions error handling).

### T63 — KMS permissions at request time; Singapore key with the `asia-southeast1` endpoint
- Verdict: PARTLY RESOLVED. The key-placement rule is documented and answers the Singapore question; the permission is documented for the caller; whether the service agent or the caller needs a KMS decrypt permission is still not stated.
- Evidence:
  - Placement: https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key : "When you create a Cloud KMS key, you must store it in either global or in the same region that you will use for your Sensitive Data Protection requests. Otherwise, the Sensitive Data Protection requests will fail." Cloud KMS lists `asia-southeast1` (Singapore): https://docs.cloud.google.com/kms/docs/locations (Cloud KMS docs, not SDP docs). SDP supports `asia-southeast1` with a regional endpoint (locations page, INV(f)).
  - Permission: REST schema `KmsWrappedCryptoKey` on https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates : "Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt". The client docstring says the same (`dlp.py@google-cloud-dlp-v3.40.0:6484`). The permission is in `roles/dlp.user`.
  - Required roles for the quickstart: https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify : "Cloud KMS Admin (roles/cloudkms.admin)", "Cloud KMS CryptoKey Encrypter (roles/cloudkms.cryptoKeyEncrypter)", "DLP User (roles/dlp.user)" (for the setup steps).
  - Same REST schema `CryptoKey`: "be sure to set an appropriate IAM policy on the KEK to ensure an attacker cannot unwrap the DEK."
  - No page names a Cloud KMS decrypt role or the DLP service agent for this call (checked create-wrapped-key, the quickstart, auth, roles and the REST schemas).
- Label: [Documented] for the quotes. "A Singapore key works with the `asia-southeast1` endpoint" follows from the rule and the two location pages: [Inferred] (premise: both are the same region name).
- Draft impact:
  - B SD4 R8 #11 (line 162): replace with `• Whether a key in `asia-southeast1` works end to end with the `asia-southeast1` regional endpoint (the wrapped-key page requires the key in global or the request region; test the Singapore pair)`.
  - B SD4 R8 #7 (line 158): replace with `• Which identity needs a Cloud KMS decrypt or use permission at request time: the REST schema names `dlp.kms.encrypt` for the sender of the request, the quickstart grants the caller KMS Admin, CryptoKey Encrypter and DLP User, and no page says whether the DLP service agent or the caller unwraps the key (checked the quickstart, create-wrapped-key, roles, auth pages and the REST schemas)`.
  - B SD4 R6, add one bullet: `• A Singapore key and the Singapore endpoint satisfy the placement rule (premise: the rule asks for the key in global or in the request region, and Cloud KMS and SDP both list asia-southeast1) **[Inferred]**` and add `https://docs.cloud.google.com/kms/docs/locations` to B SD4 R9.
  - B SD4 R4 bullet 75 (`dlp.kms.encrypt` client docstring) stays; add the REST sentence as a sibling `[Documented]` bullet if wanted. No Summary change.

### T64 — Audit logs: do request bodies, tokens or wrapped keys appear?
- Verdict: PARTLY RESOLVED. The audit-logging page was read; it lists the content methods but says nothing about log contents. The general Cloud Logging reference (not SDP docs) says request and response fields should never include user-generated data.
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/audit-logging : the ADMIN_READ list includes `google.privacy.dlp.v2.DlpService.InspectContent`, `DeidentifyContent`, `ReidentifyContent` and `RedactImage`; each method block reads "Audit log type: Data access" (for example InspectContent: "Permissions: dlp.inspectTemplates.get - ADMIN_READ"). Nothing on request or response payloads.
  - https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog (Cloud Logging docs, not SDP docs): `request` "may not include all request parameters, such as those that are too large, privacy-sensitive, or duplicated elsewhere in the log record. It should never include user-generated data, such as file contents."
- Label: [Documented] for the list and the Cloud Logging sentence; "SDP audit logs do not hold the content" is [Inferred] (premise: the Cloud Logging statement applies to all Google Cloud audit logs; the SDP page does not restate it).
- Draft impact:
  - B SD4 R8 #8 (line 159): replace with `• Whether request bodies, tokens or wrapped keys appear in Cloud Audit Logs: the SDP page lists the content methods as Data Access audit methods and does not say what the entries contain (checked the audit-logging page; the general audit log reference says request fields should never include user-generated data; needs a look at a real log entry)`.
  - B SD4 R6, add: `• The SDP audit-logging page lists InspectContent, DeidentifyContent, ReidentifyContent and RedactImage with audit log type "Data access" (SDP docs, audit-logging page, read 2026-10-09) **[Documented]**` and `• The Cloud Logging audit log reference says the request field "should never include user-generated data, such as file contents" (Cloud Logging docs, not SDP docs, read 2026-10-09) **[Documented]**` and `• Content strings, tokens and wrapped keys are therefore not expected in audit entries (premise: that rule applies to SDP audit logs; the SDP page does not restate it) **[Inferred]**`. Add `https://docs.cloud.google.com/sensitive-data-protection/docs/audit-logging` and `https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog` to B SD4 R9.
  - Optional: A/B image and text columns' R6 could carry the audit-logging bullet; not required. No Summary change.

### T65 — Covered-by for the `CryptoHashConfig` row
- Verdict: RESOLVED (decision follows R018: SD4 kept as a column, so the question is only whether the hash row also names SD4).
- Evidence: B SD4 R1 (line 15) says the hash is "the one-way contrast" and "its row belongs to the SD3 column"; https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify : "The reversible transformations are: CryptoDeterministicConfig CryptoReplaceFfxFpeConfig" (the two names are on separate lines in the page; the hash is not on the list); SD4's header is "Reversible tokenisation and re-identification (AES-SIV and FPE)". The brief's column notes agree ("its row lives in SD3"); only the brief's Covered-by line adds SD4 for the hash.
- Label: n/a (a scope decision, not a fact).
- Draft impact: INV(c) "Pseudonymisation by cryptographic hash" row, "Covered by Table 3 column": replace "Sensitive Data Protection: Sensitive-data masking and de-identification in text; Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE)" with `Sensitive Data Protection: Sensitive-data masking and de-identification in text`. INV Reviewer notes "Covered-by decisions" bullet 1: change "SD4 added for the hash, FPE and AES-SIV objects" to "SD4 added for the FPE and AES-SIV objects". No row-count change, no Summary change. Block (c) then has SD4 on 2 rows.

### T73 — Launch stage of the object and image-context infoTypes
- Verdict: PARTLY RESOLVED. Only the face detector carries a stage mark. For the other seven object detectors and the three image-context detectors neither the reference nor the release notes give a stage.
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference : "OBJECT_TYPE/PERSON/FACE | Image of a person's face. This infoType detector is in Preview." No other infoType row for `OBJECT_TYPE/*` or `IMAGE_TYPE/CONTEXT/*` carries a stage sentence (the word "Preview" occurs once on the page).
  - https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes : "The OBJECT_TYPE/PERSON/FACE infoType detector is available in Preview in global and the asia, europe, and us multi-regions." (December 15, 2025). For the others the notes say "available" or "can detect and redact": 2025-07-04 (BARCODE, LICENSE_PLATE, PERSON, WHITEBOARD), 2025-11-03 (PASSPORT, PHOTO_ID_CARD), 2026-06-08 (SIGNATURE), 2026-01-16 (the three IMAGE_TYPE/CONTEXT detectors: "available in global and the asia, europe, and us multi-regions").
  - Pre-GA terms, for the Preview face detector: https://cloud.google.com/terms/service-terms (General Service Terms, section 5 "Pre-GA Offerings Terms", b): "Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity."
- Label: [Documented] for the face detector's Preview status and the release-note wording; [Not disclosed] for the stage of the other detectors (reference and release notes checked, 2025-07-04 to 2026-06-08).
- Draft impact:
  - B SD6 R6 bullet at line 464 ("Launch stage of the three detectors ... is not stated beyond the release note that says they are 'available'") already carries [Not disclosed]; add "(checked the infoType reference, which marks only the face detector, and the release notes of 2026-01-16)" if wanted.
  - B SD5 R8 #10 (line 346) stays; optional wording: "only the face detector is marked Preview in the reference and the release notes (2025-12-15); the other object detectors carry no stage mark".
  - Optional new bullet in B SD5 R2 after the Preview bullet (line 220): `• Preview features fall under the Pre-GA Offerings Terms, which exclude them from any SLA (Google Cloud Service Specific Terms, General Service Terms section 5, read 2026-10-09) **[Documented]**` plus `• The face detector's use therefore carries no SLA (premise: the detector is a Pre-GA Offering because the docs call it Preview) **[Inferred]**`.
  - No Summary change by this item (T18 covers the SD5 R1 and R2 Summaries).

### T78 — Do PDF, Word, Excel and PowerPoint byte items work on `content.inspect`?
- Verdict: PARTLY RESOLVED. The docs show a `content.inspect` request that sends a PDF as `byteItem`; the supported-file-types page has no per-method column that says "inspect content", so which file types `content.inspect` handles is still untested. (The triage described a column "Inspect content" per file type; it does not exist.)
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels : "The following example shows a content.inspect request that includes both a PDF file and client-provided metadata." with `"byteItem": { "type": "PDF", "data": "BASE64_ENCODED_PDF" }`.
  - https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types : columns "File type | File extensions | Limits | Scanning mode | Transformation support"; PDF row "Intelligent document parsing" with no Transformation support entry; "De-identify content" appears only for csv/tsv and the text row; the Image row says "Redaction".
  - Client enum `dlp.py@google-cloud-dlp-v3.40.0:1593` lists `TEXT_UTF8`, `WORD_DOCUMENT`, `PDF`, `POWERPOINT_DOCUMENT` (and Excel, Avro, CSV, TSV).
- Label: [Documented] for the example and the enum; "PDF byte items are accepted by `content.inspect`" is [Inferred] (premise: the documented example request).
- Draft impact: A SD1 R3 bullet "The metadata-label page shows a `content.inspect` request that sends a PDF as `byteItem`, so file bytes are accepted on this method" (line 67): split into
  - `• The metadata-label page shows a `content.inspect` request that sends a PDF as a `byteItem` of type `PDF` (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**`
  - `• PDF byte items are accepted by `content.inspect`; which other file types are accepted is not stated per method (premise: the documented example; the supported-file-types table has no per-method column) **[Inferred]**`.
  A SD3 R3 bullet at line 426 is accurate as written (the cells were verified). A SD1 R8 needs no change. Scope (main): files on the AI data path stay Detail-level in SD1 R3; job-based file scans stay inventory only. No Summary change.

### T79 — Dataflow, AWS S3 and JDBC guides row, plus Apigee, Data Fusion and BigQuery rows
- Verdict: RESOLVED. Recommend keeping the row (13 rows in block (d) unchanged) and rewriting its cells with what the linked material shows. The pages are read (S3 and JDBC by shallow clone, under R013, as supporting material); the Apigee, Data Fusion and BigQuery claims were re-checked and match.
- Evidence:
  - Navigation (https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview): "Use Sensitive Data Protection with AWS S3" links to `https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification`; "Use Sensitive Data Protection with JDBC Databases" links to `https://cloud.google.com/community/tutorials/dlp-hybrid-inspect`; "Build a secure anomaly detection solution using Dataflow, BigQuery ML, and Sensitive Data Protection" links to `https://cloud.google.com/architecture/building-anomaly-detection-dataflow-bigqueryml-dlp`.
  - S3 guide target (Google sample repo, supporting only): `GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271` README.md: "Passes data through Dataflow pipelines that perform inspection, de-identification, and re-identification through the Cloud Data Loss Prevention API (DLP API)." and "You can use this pipeline for Avro, CSV, JSONL, ORC, Parquet and TSV files stored or ingested in Cloud Storage or an Amazon S3 bucket." The Java source builds `InspectContentRequest`, `DeidentifyContentRequest` and `ReidentifyContentRequest` (`DLPInspectText.java`, `DLPDeidentifyText.java`, `DLPReidentifyText.java`). So content methods are used, on batch file data, not on a prompt path. Apache License 2.0. Last commit 2024-04-01.
  - JDBC guide target: `cloud.google.com/community/tutorials/dlp-hybrid-inspect` answered HTTP 403 to the page fetch and HTTP 301 to `https://github.com/GoogleCloudPlatform/community/blob/master/archived/dlp-hybrid-inspect/index.md` (curl -I, 2026-10-09). The archived file (`GoogleCloudPlatform/community@6f68203d`) says: "This document shows how to use Cloud DLP hybrid inspection jobs with a JDBC driver to inspect samples of tables in a SQL database like MySQL, SQL Server, or PostgreSQL." A hybrid job is the asynchronous path, not a content method.
  - Anomaly-detection solution: `https://cloud.google.com/architecture/building-anomaly-detection-dataflow-bigqueryml-dlp` answers HTTP 301 to `https://docs.cloud.google.com/architecture/building-anomaly-detection-dataflow-bigqueryml-dlp`, which answers HTTP 301 to `https://docs.cloud.google.com/sensitive-data-protection/docs` (curl -I, 2026-10-09): the page is gone, the navigation link is dead.
  - BigQuery tutorial (https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-bq-tutorial): "Grant the DLP Reader role:" `--role='roles/dlp.reader'` and "Grant the DLP User role:" `--role='roles/dlp.user'` for the Cloud Run service account.
  - Data Fusion (https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp, redirected from the cloud.google.com URL): "Cloud Data Fusion provides a Sensitive Data Protection plugin that provides three transforms that can filter, redact, or decrypt your sensitive data" and "Click Add Another Role. Use the search bar to search and then select DLP Administrator."; "Cloud Data Fusion version 6.1.1 or higher." Apigee (https://docs.apigee.com/api-platform/reference/extensions/google-cloud-data-loss-prevention/google-cloud-data-loss-prevention-extension-120): "Caution: This version of the extension is no longer supported and has been deprecated." with actions `deidentifyWithMask`, `deidentifyWithType`, `redactImage`.
- Label: [Documented] for the navigation, the HTTP facts and the quotes; [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] and [Documented: repo GoogleCloudPlatform/community@6f68203d] for the sample content.
- Draft impact: INV(d) row "Dataflow, AWS S3 and JDBC guides" (line 91). Replace the "Access method", "Auth", "Regional options", "Applies to", "Notes" cells with:
  - Access method: `The SDP navigation lists three guides: AWS S3 (links to the GoogleCloudPlatform/dlp-dataflow-deidentification repository), JDBC databases (links to a Google community tutorial) and a Dataflow, BigQuery ML anomaly detection solution [Documented] (DOCS sensitive-data-protection-overview, navigation). The S3 sample is a Dataflow pipeline that inspects, de-identifies and re-identifies Avro, CSV, JSONL, ORC, Parquet and TSV files from Cloud Storage or Amazon S3 and writes to BigQuery, and its Java code builds InspectContentRequest, DeidentifyContentRequest and ReidentifyContentRequest [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (README.md, src/main/java/com/google/swarm/tokenization/beam). The JDBC tutorial inspects SQL tables with a hybrid inspection job and is archived in GoogleCloudPlatform/community [Documented: repo GoogleCloudPlatform/community@6f68203d] (archived/dlp-hybrid-inspect/index.md). The anomaly detection page answers HTTP 301 to the SDP docs home [Documented] (observed 2026-10-09)`
  - Auth: `The sample's Dataflow runner role lists serviceusage.services.use, dlp.kms.encrypt and get and list on inspect and de-identify templates [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (dlp_tokenizing_runner_permissions.yaml). The JDBC tutorial lists creating a secret in Secret Manager among its objectives [Documented: repo GoogleCloudPlatform/community@6f68203d] (archived/dlp-hybrid-inspect/index.md)`
  - Regional options: `The S3 sample creates a bucket in us-central1 and a BigQuery dataset in the US multi-region for its demo [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (README.md); no regional endpoint guidance for SDP in the guides [Not disclosed] (checked README and tutorial)`
  - Applies to: `Not AI: batch file and database scanning and tokenisation [Inferred] (premise: the S3 sample reads files and the JDBC tutorial reads database tables)`
  - Notes: `Content methods are used for batch files in the S3 sample, so the row stays inventory only; the guides do not target prompts or responses [Inferred] (premise: the README describes file pipelines). Apache License 2.0 for the sample repository [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (LICENSE)`
  - Source URL cell: add `https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification/blob/4213e271f5889c7b889d98ab5b0623f1406687b0/README.md ; https://github.com/GoogleCloudPlatform/community/blob/6f68203dec458268f177e97e2b57f3e085ca3668/archived/dlp-hybrid-inspect/index.md` (pinned blob URLs, R013).
  - INV(d) "BigQuery at query time" row, Auth cell: replace "Roles and service accounts are set in the tutorial steps [To be verified] (not read in detail)" with `The tutorial gives the Cloud Run service account roles/dlp.reader and roles/dlp.user [Documented] (DOCS deidentify-bq-tutorial)`.
  - INV(d) Apigee and Data Fusion rows: all cell claims re-checked and accurate; change the Data Fusion Source URL to the redirect target `https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp` (the current URL answers HTTP 301).
  - INV(d) row count stays 13. INV Reviewer notes "Uncertain or not read" bullet 4 (Apigee, Data Fusion, BigQuery, S3, JDBC): delete from the final.

### T88 — Empty table cell read as "No" in INV(c)
- Verdict: RESOLVED. The Reversible column is supported by an explicit list; the Referential integrity column rests on empty cells and needs an [Inferred] label for the "No".
- Evidence:
  - https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference : the table columns are "Transformation | Object | Description | Can Reverse1 | Referential Integrity2 | Input Type", with a tick "✔" under Can Reverse for FPE and AES-SIV and under Referential Integrity for the hash, FPE, AES-SIV and date shift; other cells are empty. Footnote 2: "Referential integrity allows for records to maintain their relationship to one another while still de-identifying the data."
  - https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify : "This requires that only reversible transformations be provided here. The reversible transformations are: CryptoDeterministicConfig CryptoReplaceFfxFpeConfig".
  - Hash: transformations-reference "Unlike other types of crypto-based transformations, this type of transformation isn't reversible." The phrase "HMAC-SHA-256" (T56 re-match): "Sensitive Data Protection uses a SHA-256-based message authentication code (HMAC-SHA-256) on the input value, and then replaces the input value with the hashed value encoded in base64." (same page, "Cryptographic hashing") and https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization "an input value is hashed using HMAC-SHA-256 with a cryptographic key, and then encoded using base64."
- Label: Reversible column "No" for the 10 objects not on the reidentify list: [Documented] (REST reidentify list plus the empty cell). Referential integrity "No": the cell is empty [Documented]; reading it as "no referential integrity" is [Inferred] (premise: the table ticks the property where it holds, footnote 2 defines it, and nothing else in the docs says otherwise).
- Draft impact: INV(c).
  - "Reversible" column, the 10 cells that read "No: the Can Reverse cell is empty [Documented] (DOCS transformations-reference, transformation table)" (rows Redaction, value replacement, dictionary replacement, infoType replacement, character masking, hash, fixed-size bucketing, custom bucketing, date shifting, time extraction): replace with `No: not on the list of reversible transformations, and the Can Reverse cell is empty [Documented] (REST reidentify, DOCS transformations-reference, transformation table)`. For the hash row keep the following sentence about the pseudonymisation page.
  - "Referential integrity" column, the 8 cells "No: the Referential Integrity cell is empty [Documented] (DOCS transformations-reference, transformation table)" (rows Redaction, value replacement, dictionary replacement, infoType replacement, character masking, fixed-size bucketing, custom bucketing, time extraction): replace with `Not marked: the Referential Integrity cell is empty [Documented] (DOCS transformations-reference, transformation table). Read as No [Inferred] (premise: the table ticks the property where it holds)`.
  - Add `https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify` to the Source URL cell of rows that now cite it, or to one row of block (c).
  - The "HMAC-SHA-256" clause in the hash row is confirmed [Documented]; no change.
  - Summaries: none.

### T89 — Process language and first-person wording in INV cells
- Verdict: RESOLVED (mechanical rewrite; text below).
- Evidence: README sections 5 and 7: finals carry no process language. Instances found by grep in `sdp_inventory.md` on 2026-10-09: line 3 ("Counts that are mine are labelled Inferred with the counting rule."), line 27 ("Group boundaries are my own"), lines 31 to 54 (24 cells with "(my count of rows in the infoType categories table, grouped by my own rule)"), line 33 ("(my count of the Industry column)"), lines 121 and 124 ("(my count of ...)"), line 83 ("not exercised, read-only rule" and "Not signed in to or run for this sheet"), lines 84 and 85 ("Not covered in this sheet" twice; "(this sheet)"), line 91 ("not read, so no column is proposed"). That is 27 count cells. Lines 143 onward (Reviewer notes) are moved to the change log and need no rewrite.
- Label: n/a.
- Draft impact (apply to the final `sdp_inventory_final.md`):
  - Line 3: `Counts made by tallying rows on a page are labelled Inferred and state the counting rule.`
  - Line 27: replace "Group boundaries are my own; counts come from the infoType categories table on the same page." with `Group boundaries follow the rule in each Count cell (explicit name sets for global groups, the Location column for country groups, name prefixes for document and image groups); counts come from the infoType categories table on the same page.`
  - Lines 31 to 54 (24 cells) and line 33's second cell: replace "(my count of rows in the infoType categories table, grouped by my own rule)" with `(count of rows in the infoType categories table, grouped by the rule in the block note)`; replace "(my count of the Industry column)" with `(count of the Industry column)`.
  - Line 121: "(my count of region rows on the locations page; asia-southeast1 row read directly [Documented] (DOCS locations))" becomes `(count of region rows on the locations page; the asia-southeast1 row is stated directly [Documented] (DOCS locations))`. Line 124: "(my count of the Availability column)" becomes `(count of the Availability column)`.
  - Line 83 (console and demo row): "(not exercised, read-only rule)" becomes `(not exercised)`; "Not signed in to or run for this sheet. The demo page may help a quick manual test but its data handling is unknown [To be verified]" becomes `Not signed in to or run. The demo page may help a quick manual test but its data handling is not described [Not disclosed] (see T94)`.
  - Lines 84 and 85 (Model Armor rows): "Not covered in this sheet [Inferred] (premise: the Model Armor columns own the Model Armor access model)" becomes `Covered by the Model Armor columns, not repeated here [Inferred] (premise: the Model Armor columns own the Model Armor access model)`. Line 85 also: "The SDP inspection and de-identify templates themselves are rows in block (a) [Documented] (this sheet)" becomes `The SDP inspection and de-identify templates themselves are rows in block (a)` (drop the label, T90).
  - Line 91: replaced wholesale by the T79 text.
  - The INV scope paragraph also says "the sheet's allowed forms" and "this sheet": acceptable; "Labels use the sheet's allowed forms" can become "Labels use the allowed forms".

### T91 — Absence claims labelled [Documented]
- Verdict: RESOLVED (re-verified the absence, text below).
- Evidence: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies : methods table lists `create`, `delete`, `get`, `list`, `patch` only ("Create a ContentPolicy.", "Delete a ContentPolicy.", "Get a ContentPolicy.", "Lists ContentPolicies in a parent.", "Update a ContentPolicy."). Client `google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0`: the content-policy methods are `create_content_policy:7363`, `update_content_policy:7488`, `get_content_policy:7620`, `list_content_policies:7727` and `delete_content_policy:7850` (plus the path helpers `content_policy_path:229` and `parse_content_policy_path:242`); the file has no method with "apply" or "evaluate" in its name (111 `def` entries searched).
- Label: methods listed [Documented] / [Documented: repo]; "no evaluation method" [Not disclosed] naming the pages and the client version.
- Draft impact:
  - INV(a) "Content policies" row, "Method or resource" cell: replace "projects.locations.contentPolicies with create, delete, get, list and patch; no evaluation method is listed on the resource page or in the REST root [Documented] (REST contentPolicies, REST root). The Python client has create_content_policy, update_content_policy, get_content_policy, list_content_policies and delete_content_policy and no evaluation method [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (client.py). An evaluation method outside the public REST and client surface [Not disclosed] (checked REST root, contentPolicies page, content-policy and manage pages, client.py at the tag)" with `projects.locations.contentPolicies with the methods create, delete, get, list and patch [Documented] (REST contentPolicies, REST root). The Python client has create_content_policy, update_content_policy, get_content_policy, list_content_policies and delete_content_policy [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (client.py). An evaluation method on the resource, the REST root or the client [Not disclosed] (checked the REST root, the contentPolicies page, the content-policy and manage pages, and client.py at the tag)`.
  - A SD1 R4, bullet "Content-policy conflict, source 2b" (line 94 of A, the `create_content_policy` bullet): replace with `• Content-policy conflict, source 2b: the client at the tag has `create_content_policy`, `update_content_policy`, `get_content_policy`, `list_content_policies` and `delete_content_policy` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:7363` "def create_content_policy(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**`. The absence ("no evaluate method") is already carried by the next bullet, which is [Not disclosed] and names the pages and the client.
  - T9 (other resolver) may add the IAM permission facts; do not duplicate them here.

### T92 — Customer-data terms (use of content beyond serving the request)
- Verdict: PARTLY RESOLVED. R019 allows the terms pages; the general terms answer the question for Google Cloud services, and SDP is listed as one; no SDP-specific clause exists. Applying them to SDP request content is an inference.
- Evidence:
  - https://cloud.google.com/terms/services : under "Google Cloud Platform Services Summary": "Sensitive Data Protection (including Cloud Data Loss Prevention or DLP): Sensitive Data Protection is a fully-managed service enabling customers to discover, classify, de-identify, and protect sensitive data, such as personally identifiable information."
  - https://cloud.google.com/terms (Google Cloud Platform Terms of Service), section 5.2: "Google will only access, use, and otherwise process Customer Data in accordance with the Cloud Data Processing Addendum and will not access, use, or process Customer Data for any other purpose." Definition: "'Customer Data' means (a) for GCP Services ... data provided to Google by Customer or End Users through the Services under the Account, and data that Customer or End Users derive from that data through their use of the Services".
  - https://cloud.google.com/terms/data-processing-addendum, section 5.2: "Customer instructs Google to process Customer Data in accordance with the applicable Agreement (including this Addendum) only as follows: a. to provide, secure, and monitor the Services and TSS (if applicable)".
  - https://cloud.google.com/terms/service-terms (Service Specific Terms): the text has no section for Sensitive Data Protection or Cloud DLP (the product name occurs only in the navigation list; searched "Sensitive Data Protection", "Data Loss Prevention" and "DLP").
  - SDP docs on storage: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types "Request data is encrypted in transit and is not stored." (already in the drafts).
- Label: [Documented] for each quote (terms pages: "Google Cloud terms, not SDP docs"); "content sent to the SDP API is Customer Data that Google uses only to provide, secure and monitor the service" is [Inferred] (premise: SDP is listed as a GCP Service, the Customer Data definition covers data provided through the Services, and the Service Specific Terms have no SDP carve-out). Whether Pre-GA features (the Preview face detector) are covered the same way: the Pre-GA terms say "Pre-GA Offerings are not covered by TSS, and ... the Data Location Section above will not apply to Pre-GA Offerings" (Service Specific Terms, section 5.b) [Documented]; the effect on Customer Data use is not stated.
- Draft impact:
  - A SD1 R8 #12 (line 185) and A SD3 R8 #10 (line 519): replace with `• Customer-data terms: the Google Cloud terms limit Google's processing of Customer Data to what the Data Processing Addendum allows, and the Service Specific Terms have no Sensitive Data Protection section; whether any SDP-specific use of content applies is not stated (checked the terms of service, Data Processing Addendum, Service Specific Terms and services list; the docs say request data "is not stored")`.
  - B SD4 R8 #9 (line 160): replace with `• Whether tokenised output and the key reach any Google training or product-improvement use: the general Google Cloud terms limit processing to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)`.
  - B SD5 R8 #13 (line 349) and B SD6 R8 #13 (line 492): replace "Customer data terms for images sent to the API (not read)" with `• Customer data terms for images sent to the API: the general Google Cloud terms limit processing of Customer Data to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)`.
  - INV(f) "Data handling" row, last sentence (the [To be verified] one): replace "Use of customer content for product improvement and the data processing terms [To be verified] (not covered by the product docs read; terms pages were not read)" with `The Google Cloud terms say Google will "only access, use, and otherwise process Customer Data in accordance with the Cloud Data Processing Addendum and will not access, use, or process Customer Data for any other purpose" [Documented] (Google Cloud terms, not SDP docs). Sensitive Data Protection is listed among the Google Cloud Platform Services and the Service Specific Terms have no section for it [Documented] (Google Cloud terms services list and Service Specific Terms, not SDP docs). Content sent to the SDP API is therefore processed only to provide, secure and monitor the service [Inferred] (premise: the Customer Data definition covers data provided through the Services and no SDP carve-out exists)`; add the sources `https://cloud.google.com/terms ; https://cloud.google.com/terms/data-processing-addendum ; https://cloud.google.com/terms/service-terms ; https://cloud.google.com/terms/services` to that row's Source URL cell.
  - R8 bullets stay unlabelled; none of the R8 Summaries lists the terms question, so no Summary changes. Sending real PII or explicit test images remains a bench-design decision (R019), not decided here.

### T93 — Benchmarking and acceptable-use limits
- Verdict: PARTLY RESOLVED. Terms pages read. They allow the customer to benchmark itself and constrain publication; they do not name test images. What counts as acceptable test data is deferred to bench design (R019).
- Evidence:
  - https://cloud.google.com/terms/service-terms (General Service Terms, section 7 "Benchmarking"): "Customer may itself (but may not permit a third party to): (a) conduct benchmark tests of the Services" and "publicly disclose the results of such Tests only if (i) the public disclosure includes all necessary information to replicate the Tests, and (ii) Customer allows Google to conduct benchmark tests of Customer's publicly available products".
  - https://cloud.google.com/terms/aup (Google Cloud Acceptable Use Policy): "to engage in, promote, or encourage illegal activity, including child sexual exploitation, child abuse, or terrorism or violence that can cause death, serious harm, or injury to individuals or groups of individuals;" and "for any unlawful, invasive, infringing, defamatory, or fraudulent purpose including Non-consensual Explicit Imagery (NCEI)". Also: "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement".
  - The AUP and the Service Specific Terms do not mention sexually explicit or violent images as test inputs, and have no Sensitive Data Protection section.
- Label: [Documented] for each quote (Google Cloud terms, not SDP docs). Reading them as covering the bench is [Inferred] (premise: the bench is a customer using the service under the terms; whether adversarial robustness testing counts as "evade filtering" is a legal reading, not a fact).
- Draft impact: this item was suggested by the triager and is not in the drafts. Two places could carry it:
  - B SD6 R8 #13 (line 492), appended to the T92 replacement: `Acceptable-use limits for explicit or violent test images: the Google Cloud Acceptable Use Policy bars illegal content including child sexual exploitation and non-consensual explicit imagery and does not mention other explicit or violent test images; which test images are acceptable is decided in the bench design`.
  - A short INV(f) "Data handling" companion row is NOT proposed (row count). Alternative: a bullet in B SD6 R7 (first Detail bullet after "Minimum setup"): `• Terms for the bench: the Service Specific Terms let the customer run benchmark tests itself and publish results only with all information needed to replicate them and a reciprocal right for Google (Google Cloud Service Specific Terms, General Service Terms section 7, read 2026-10-09) **[Documented]**` and `• Test images must not be illegal content or non-consensual explicit imagery under the Acceptable Use Policy (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**`. R9 would need `https://cloud.google.com/terms/service-terms` and `https://cloud.google.com/terms/aup`.
  - Summaries: none change. QUESTION for main: does the bench team want the benchmarking clause recorded in the SDP columns at all, or only in the bench design? (QUESTIONS block.)

### T97 — Inconsistent code citations (A versus B)
- Verdict: RESOLVED (line numbers verified; only the path form needs normalising).
- Evidence (checked in the clone at `google-cloud-dlp-v3.40.0`): 61 `file@tag:line` citations in A, B and INV were checked. For the 23 that carry a quoted line, the quoted text is on or within two lines of the cited line in every case. For the 38 without a quote (most in B) the cited line holds the construct the bullet names: for example `client.py:1151` is `def reidentify_content(`, `client.py:1060` is `def deidentify_content(`, `dlp.py:2989` is `class ReidentifyContentRequest`, `dlp.py:6484` is `dlp.kms.encrypt`, `dlp.py:2641` is "Top coordinate of the bounding box. (0,0) is upper left.", `dlp.py:2845` is `class RedactImageResponse`, `dlp.py:1625` is `IMAGE_SVG = 4`, `setup.py:95` is `python_requires=">=3.10",`, `setup.py:45` is `"google-api-core[grpc] >= 2.28.0, <3.0.0"`, README.rst:88 is `pip install google-cloud-dlp`. All 10 repo files named in R9 exist at the tag (`CHANGELOG.md`, `LICENSE`, `README.rst`, `gapic_version.py`, `client.py`, `transports/rest.py`, `types/dlp.py`, `types/storage.py`, `setup.py`).
- Label: [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] unchanged.
- Draft impact: normalise at P6 to one path form, package-relative with the `google/cloud/` prefix for code and bare names for top-level files, followed by `@google-cloud-dlp-v3.40.0:<line>`:
  - The canonical form is A's majority form: the path relative to the package root (`packages/google-cloud-dlp/`), that is `google/cloud/dlp_v2/types/dlp.py`, `google/cloud/dlp_v2/services/dlp_service/client.py`, `google/cloud/dlp/gapic_version.py`, `setup.py` and `README.rst`.
  - B (31 cites in SD4 to SD6): prefix `google/cloud/` to every `dlp_v2/types/dlp.py@...` and `dlp_v2/services/dlp_service/client.py@...` (for example `dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6484` becomes `google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6484`); the 3 `dlp/gapic_version.py` cites (B lines 85, 269, 434) become `google/cloud/dlp/gapic_version.py`. The bare `README.rst` and `setup.py` cites in B line 134 are already in the target form.
  - A (5 cites at lines 89, 158, 159, 161, 505 written `packages/google-cloud-dlp/...`): drop the `packages/google-cloud-dlp/` prefix so they read `google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16`, `README.rst@google-cloud-dlp-v3.40.0:88`, `setup.py@google-cloud-dlp-v3.40.0:95` (twice) and `setup.py@google-cloud-dlp-v3.40.0:45`.
  - B's citations without a quoted line are acceptable as pure pointers (README rule 7 asks for quotes only where text is quoted); add a short quoted line where the bullet quotes a docstring and none is given (B lines 51, 58, 59, 67, 79, 80, 90 already quote in prose).
  - No Summary change.

---

## Priority L

### T80 — "Other libraries were not read at a pinned ref" labelled [Not disclosed]
- Verdict: RESOLVED (drafting fix).
- Evidence: README section 3: [Not disclosed] is for vendor silence. The sentence reports a research choice (R013: other libraries are names only). The libraries page names them: https://docs.cloud.google.com/sensitive-data-protection/docs/libraries ("This page shows how to get started with the Cloud Client Libraries for the ...", Ruby line `gem install google-api-client`).
- Label: none needed once the sentence is deleted.
- Draft impact: INV(d) "Other client libraries" row, Notes cell: delete "The other libraries were not read at a pinned ref [Not disclosed] (only the libraries page was read)." and keep the Ruby sentence. INV Reviewer notes "Uncertain or not read" bullet 5: delete.

### T81 — Archive notice of `googleapis/python-dlp`
- Verdict: RESOLVED.
- Evidence: shallow clone of https://github.com/googleapis/python-dlp (commit 21b91b9d51d4b21784ddede99d16ff15279c8f52, 2023-09-29), `README.rst` line 1: ":**NOTE**: **This github repository is archived. The repository contents and history have moved to** `google-cloud-python`_." with link target `https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-dlp`.
- Label: [Documented: repo googleapis/python-dlp@21b91b9d].
- Draft impact: INV(d) "Python client library" row, Notes cell: replace "The older googleapis/python-dlp repository is reported archived with its contents moved to google-cloud-python [To be verified] (exploration note only; the GitHub page returned HTTP 403 on 2026-10-09 and the archive notice was not re-read)" with `The older googleapis/python-dlp repository is archived and its README says the contents and history moved to google-cloud-python [Documented: repo googleapis/python-dlp@21b91b9d] (README.rst)`; add `https://github.com/googleapis/python-dlp/blob/21b91b9d51d4b21784ddede99d16ff15279c8f52/README.rst` to that row's Source URL cell. INV Reviewer notes "Uncertain or not read" bullet 3: delete. (R013's clone form worked; github.com page fetches still return 403.)

### T83 — Region counts: locations page 43 versus REST reference 42
- Verdict: RESOLVED (both counts reproduced).
- Evidence: https://docs.cloud.google.com/sensitive-data-protection/docs/locations lists 43 region rows (from `africa-south1` to `me-west1`, including `asia-southeast3` Bangkok); count made on the raw table cells. https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest ("Regional service endpoint") lists `global` plus 42 regions (46 tokens including the multi-regions `us`, `eu`, `in`), without `asia-southeast3`. Release note 2026-01-20: "Sensitive Data Protection is available in the asia-southeast3 (Bangkok) region."
- Label: [Documented] for the release note and each page's list; the counts stay [Inferred] (counting rule: region-name cells; REST list minus `global` and the three multi-region entries).
- Draft impact: INV(f) "Regional endpoints" row: keep as is; optionally add "The release notes of 2026-01-20 record asia-southeast3 as added [Documented] (DOCS release-notes)", and replace "(my count of region rows..." per T89. Add `https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes` to that row's Source URL cell. No row-count change.

### T84 — Python version: libraries page versus `python_requires`
- Verdict: RESOLVED (both sides re-read; no change).
- Evidence: `packages/google-cloud-dlp/setup.py@google-cloud-dlp-v3.40.0:95` `python_requires=">=3.10",`; `setup.py:45` `"google-api-core[grpc] >= 2.28.0, <3.0.0"`. https://docs.cloud.google.com/sensitive-data-protection/docs/libraries : "Samples are compatible with Python 2.7.x and 3.4 and higher." and "gem install google-api-client"; the page also says it covers "the Cloud Client Libraries" and "the older Google API Client Libraries". The brief's P1 grep missed `python_requires`; the drafts are right.
- Label: unchanged ([Documented: repo ...] and [Documented]).
- Draft impact: none to A SD1 R7 (lines 159 to 160) or INV(d). Apply only the T90 `[grpc]` fix. INV Reviewer notes conflict 6 stays in the change log.

### T85 — `seeds.md` host
- Verdict: RESOLVED.
- Evidence: `benchtest/scratchpad/main/seeds.md` line 30 now reads "Docs: https://docs.cloud.google.com/sensitive-data-protection/docs (cloud.google.com/sensitive-data-protection/docs and cloud.google.com/dlp/docs 301 there)". HTTP facts re-observed 2026-10-09 (curl -I): `https://cloud.google.com/sensitive-data-protection/docs` 301 to `https://docs.cloud.google.com/sensitive-data-protection/docs`; `https://cloud.google.com/dlp/docs` 301 to `https://cloud.google.com/sensitive-data-protection/docs`; `https://cloud.google.com/sensitive-data-protection/docs/pricing` 301 to `https://docs.cloud.google.com/sensitive-data-protection/docs/pricing`, which answers 404; `.../docs/quotas` 301 to the docs host. The pricing page `https://cloud.google.com/sensitive-data-protection/pricing` and `/sla` answer 200.
- Label: [Documented] (HTTP facts, observed 2026-10-09).
- Draft impact: INV Reviewer notes "Domain" conflict bullet (moves to the change log): replace "seeds.md still carries the old host" with "seeds.md was updated to the docs.cloud.google.com host". Brief C3: same. No change to the finals.

### T86 — URL hygiene
- Verdict: RESOLVED (one fix; rest checked).
- Evidence: all 83 distinct URLs in A, B and INV were requested read-only with redirects followed (2026-10-09); of the 73 non-GitHub URLs, 68 returned 200 (all REST, docs, pricing, SLA, limits, Apigee, Data Fusion, Model Armor, Gemini Enterprise and terms-related pages) and 5 are non-source strings (listed below); the 10 GitHub URLs cannot be fetched (R013): the 9 repo blob paths were checked in the clone and all exist at the tag, and the tenth (`github.com/google/re2/wiki/Syntax`) is a quoted code comment in a docs sample, not a source. Non-source strings that the url-checker should skip: `https://docs.cloud.google.com/sensitive-data-protection/docs/slug` (the short-name legend in the INV scope paragraph), `https://dlp.googleapis.com/v2/{parent=projects/*}/...` (three code patterns) and `https://www.googleapis.com/auth/cloud-platform` (an OAuth scope). Redirects: `https://cloud.google.com/data-fusion/docs/how-to/using-dlp` answers 301 to `https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp`; `https://cloud.google.com/dlp/demo` answers 302 to `https://cloud.google.com/dlp/demo/`. B SD6 R5 cites the REST InspectResult page (line 441) and B SD6 R9 does not list it; B SD5 R9 does (line 369).
- Label: n/a.
- Draft impact:
  - B SD6 R9: add `• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult`.
  - B SD4 R9: the "quickstart De-identify and re-identify sensitive data" pages cited in R1 to R7 is `.../inspect-sensitive-text-de-identify`, already in R9 (line 168 of B). No change.
  - T62, T63, T64, T57 above add further R9 URLs (KMS pages, audit-logging, Cloud Logging reference, deidentifyTemplates REST page).
  - INV(d) Data Fusion Source URL: use the redirect target (T79). INV(d) Python client row: add the python-dlp README URL (T81).
  - The url-checker's `sdp_urls.txt` is built from R9 bullets and Source URL cells only, so the code-pattern strings are not included.

### T87 — Inventory row counts for the config module
- Verdict: RESOLVED.
- Evidence: `python benchtest/tools/check_drafts.py inventory benchtest/drafts/sdp_inventory.md --headers <A and B concatenated>` on 2026-10-09: 0 errors, 0 warnings; tables (a) 15 rows x 8 cols, (b) 24, (c) 12, (d) 13 x 8, (e) 16 x 4, (f) 7 x 4 = 87. A direct count of table rows per block gives the same.
- Label: n/a.
- Draft impact: none. For `build_sdp_inventory.py`: BLOCKS counts 15/24/12/13/16/7. My proposals above change no counts (T79 keeps row (d) at 13; no rows are added or dropped; T24, in the other resolver's range, may change block (e)). The inventory tables are only valid with both column files supplying the headers, so the verifier should pass the merged `sdp_two_level.md`.

### T90 — Non-label bracket pair and self-referential label
- Verdict: RESOLVED.
- Evidence: `setup.py@google-cloud-dlp-v3.40.0:45` is `"google-api-core[grpc] >= 2.28.0, <3.0.0"` (an extras specifier). The Model Armor advanced row sentence is an internal pointer to block (a).
- Label: n/a.
- Draft impact: INV(d) "Python client library" row, Notes cell: replace "google-api-core[grpc] >=2.28.0 and <3.0.0" with `google-api-core with the grpc extra, version 2.28.0 or higher and below 3.0.0`. INV(d) "Model Armor advanced mode" row, Notes cell: replace "The SDP inspection and de-identify templates themselves are rows in block (a) [Documented] (this sheet)" with `The SDP inspection and de-identify templates themselves are rows in block (a)`.

### T94 — Data handling of the web demo app
- Verdict: STILL OPEN (checked the demo page, the SDP docs navigation and the infoTypes concepts page; no terms or privacy text for the app).
- Evidence: https://cloud.google.com/dlp/demo/ answers HTTP 200 with the page title "Sensitive Data Protection Demo" and no other text in the static HTML (the app is script-driven; not exercised). The SDP docs navigation links it as "Web-based inspection demonstration app" with no SDP docs page behind it. The infoTypes concepts page: "Sensitive Data Protection Demo is a web-based application that you can use to test built-in infoType detectors." The Service Specific Terms have no demo section.
- Label: [Not disclosed] (pages named).
- Draft impact: INV(d) "Cloud console, gcloud CLI and web demo" row, "Applies to" cell: `What the demo app does with entered text [To be verified] (not exercised, read-only rule)` becomes `What the demo app does with entered text [Not disclosed] (checked the demo page, which shows only its title, the SDP docs navigation and the infoTypes concepts page)`; Notes cell: see T89 for the second clause. A SD1 R7 web-demo bullet (line 164) is accurate; add a sibling bullet `• What the web demo does with text entered into it is not described (checked the demo page, the SDP docs navigation and the infoTypes concepts page) **[Not disclosed]**` so the caveat sits next to the test aid.

### T95 — Gemini Enterprise content-policy availability
- Verdict: RESOLVED.
- Evidence: https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data (Gemini Enterprise docs, not SDP docs): "You can use Sensitive Data Protection with all Gemini Enterprise editions except the Gemini Enterprise Business edition." and "There's no additional cost to use Sensitive Data Protection." and "Sensitive Data Protection supports the global, EU, and US multi-regions." The page also says "Note: Although you can upload video and audio files to the assistant, Sensitive Data Protection doesn't scan these file types."
- Label: [Documented] (Gemini Enterprise docs, not SDP docs).
- Draft impact: none; INV(d) Gemini Enterprise row and INV(e)/(f) content-policy cells already say this and are accurate. Whoever tests SD7 needs a Gemini Enterprise tenant on a non-Business edition (T10, other resolver).

### T96 — No Reviewer notes in A and B
- Verdict: RESOLVED (no action; the finals carry no Reviewer notes anyway).
- Evidence: `grep -c "Reviewer notes"` gives 0 for A and for B; the scan for "reviewer notes|this draft|I checked|see above|this brief" finds nothing in A or B. Provenance gap addressed by the quote sweep in the Method notes: 467 of 477 quoted fragments in A, B and INV match the raw page text or code verbatim, and the other 10 are not quotations of a source, so no fact there depends on a summarising fetch.
- Label: n/a.
- Draft impact: none. The P6 change log can cite this triage for the conflicts list and this file for the quote sweep.

### T98 — [Inferred] bullets in B without a "(premise: ...)" clause
- Verdict: RESOLVED (style; exact text for the four named bullets; the rest by rule).
- Evidence: counts on 2026-10-09: A has 43 [Inferred] Detail bullets, 33 with "premise"; B has 48, none. B bullets without a premise (line numbers in B): 14, 28, 29, 41, 52, 86, 106, 127, 133, 138 to 147, 207, 230, 242, 249, 288, 304, 306, 320, 324 to 332, 416, 421, 442, 459, 468 to 475. The R7 test-plan bullets (B 138 to 147, 324 to 332, 468 to 475, and the "Minimum setup" bullets) are [Inferred] by the R7 rule and are test designs; no premise is needed for them. A without a premise: 23, 25, 35, 47, 97, 98, 420, 459, 460, 506 (of which 459 and 460 are R7).
- Label: [Inferred] unchanged.
- Draft impact (exact text, B):
  - B SD4 R3 (line 41): `• Neither request has a field for direction, message role or prompt type, so the caller decides what string to send; the column therefore applies to prompts, responses, retrieved text, tool inputs and tool outputs alike (premise: the REST request bodies for deidentify and reidentify list no such field) **[Inferred]**`
  - B SD4 R6 (line 127): `• The limits table is headed as covering "inspecting and de-identifying content sent directly to the DLP API" and does not name re-identification; the same limits probably also apply to `content.reidentify` (premise: re-identification is a content method with the same request shape) **[Inferred]**`
  - B SD5 R6 (line 306): `• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`, so larger images need `image.redact` or a storage inspection job (premise: the 0.5 MB limit is listed for content sent directly to the API and image.redact has its own 4 MB entry) **[Inferred]**`
  - B SD6 R3 (line 421): `• No system prompt or conversation context is read; the image and the configuration are the only inputs (premise: the request fields listed above) **[Inferred]**`
  - Remaining non-R7 bullets (B 14, 28, 29, 52, 86, 106, 133, 207, 230, 242, 249, 288, 304, 416, 442; A 23, 25, 35, 47, 97, 98, 420, 506): append "(premise: <the fact bullet it rests on>)" at merge, one clause each; no research needed. Combined with T97 this keeps the final consistent. No Summary change.

---

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T51 | STILL OPEN | [Documented] role contents; [Not disclosed] requirement | no |
| T52 | STILL OPEN | [Not disclosed] | no |
| T54 | STILL OPEN | [Documented] inspect fact; [Not disclosed] de-identification behaviour | no |
| T57 | CORRECTION | [Documented] | no |
| T60 | STILL OPEN | [Not disclosed] | no |
| T62 | PARTLY RESOLVED | [Documented] (KMS docs); [Inferred] effect on tokens | no |
| T63 | PARTLY RESOLVED | [Documented]; [Inferred] Singapore pair | no |
| T64 | PARTLY RESOLVED | [Documented]; [Inferred] content not in logs | no |
| T65 | RESOLVED | n/a (scope decision) | no |
| T66 | RESOLVED (doc side; conflict stays) | [Documented] x6 | no |
| T68 | STILL OPEN | [Documented] x4 (two sides) | no |
| T73 | PARTLY RESOLVED | [Documented] face Preview; [Not disclosed] others | no |
| T78 | PARTLY RESOLVED | [Documented] example; [Inferred] acceptance | no |
| T79 | RESOLVED | [Documented]; [Documented: repo GoogleCloudPlatform/...] | no |
| T80 | RESOLVED | none (sentence deleted) | no |
| T81 | RESOLVED | [Documented: repo googleapis/python-dlp@21b91b9d] | no |
| T83 | RESOLVED | [Documented]; counts [Inferred] | no |
| T84 | RESOLVED | unchanged | no |
| T85 | RESOLVED | [Documented] (HTTP facts) | no |
| T86 | RESOLVED | n/a | no |
| T87 | RESOLVED | n/a | no |
| T88 | RESOLVED | [Documented] (Reversible); [Inferred] (Referential "No") | no |
| T89 | RESOLVED | n/a | no |
| T90 | RESOLVED | n/a | no |
| T91 | RESOLVED | [Documented]; [Not disclosed] absence | no |
| T92 | PARTLY RESOLVED | [Documented] (terms); [Inferred] applicability | no |
| T93 | PARTLY RESOLVED | [Documented] (terms); [Inferred] applicability | no |
| T94 | STILL OPEN | [Not disclosed] | no |
| T95 | RESOLVED | [Documented] (Gemini Enterprise docs) | no |
| T96 | RESOLVED | n/a | no |
| T97 | RESOLVED | unchanged | no |
| T98 | RESOLVED | [Inferred] unchanged | no |

## Report

1. Counts per verdict (32 items handled): RESOLVED 18 (T65, T66, T79, T80, T81, T83, T84, T85, T86, T87, T88, T89, T90, T91, T95, T96, T97, T98), PARTLY RESOLVED 7 (T62, T63, T64, T73, T78, T92, T93), STILL OPEN 6 (T51, T52, T54, T60, T68, T94), CORRECTION 1 (T57); 18 + 7 + 6 + 1 = 32. Not handled: 17 class b items (T50, T53, T55, T56, T58, T59, T61, T67, T69, T70, T71, T72, T74, T75, T76, T77, T82).
2. CORRECTION items: T57 only. A SD3 R4/R8 #6 say `transformationErrorHandling` is described only by the client; the REST `DeidentifyConfig` schema (on the deidentifyTemplates pages) documents it, with `ThrowError` as the default and `LeaveUntransformed`. Other stale statements found (not factual errors in the drafts): B SD4 R8 #8 says the audit-logging page was not read (T64); B SD4 R8 #11 says the KMS region point is "named only generally" although B SD4 R6 already quotes the placement rule (T63); INV(c) "No ... [Documented]" cells need an [Inferred] split for Referential integrity (T88); triage T78 describes an "Inspect content" column that does not exist on the supported-file-types page.
3. Summaries that must change: none. Every edit proposed in this file is at Detail, R8 bullet or inventory-cell level. Checked: the six R8 Summaries and the SD5 R6 Summary still match their Detail after the proposed edits.
4. Items still open after this pass: T51 (permission test), T52, T54, T60, T68 (needs a request), T94, and the class b items listed above; T62, T63, T64, T73, T78 keep a test or a documented gap; T92 and T93 keep the legal-reading and bench-design parts.
