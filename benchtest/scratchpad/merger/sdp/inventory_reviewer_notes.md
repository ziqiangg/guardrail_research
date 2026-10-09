## Reviewer notes

Row counts: (a) 15, (b) 24, (c) 12, (d) 13, (e) 16, (f) 7 = 87 rows, matching the brief targets, so the config module `build_sdp_inventory.py` can assert 15/24/12/13/16/7.

Covered-by decisions:
- Rows with SDP headers: content.inspect (SD1, SD2, SD5, SD6), content.deidentify (SD3, SD4), content.reidentify (SD4), image.redact (SD5, SD6), inspection template (SD1), de-identification template (SD3), stored infoType (SD2), infoTypes.list (SD1); in block (b) SD1 for text groups, SD5 for image object, SD6 for image context; in block (c) SD3 for all 12 and SD4 added for the hash, FPE and AES-SIV objects; in block (d) all six headers for the REST, regional and client-library rows, SD3 and SD5 for Apigee.
- Rows with the R011 marker: content policies (default per the brief, pending the column decision), storage inspection, hybrid inspection, de-identification in storage, discovery, risk analysis, job triggers, and in block (d) the console and demo row, both Model Armor rows (R012: the README allows only this product's own headers or a marker, so Model Armor is named in the text and the Model Armor columns are not cited), Gemini Enterprise, Data Fusion, BigQuery at query time, storage-side actions, and the Dataflow, S3 and JDBC guides.
- If the decision on the content policy column goes the other way, only the content-policy row in block (a) changes its Covered-by cell.
- The headers are the six default SDP headers from the brief with the provisional prefix Sensitive Data Protection. If the prefix or the column split changes, the Covered-by strings change with it (SD2 and SD4 may fold).

Conflicts between official sources (each carried as separate labelled facts, none resolved):
- Image formats for image.redact: the REST reference says PNG, JPEG, SVG or BMP; the redaction guide says redaction is not supported for SVG, PDF, XLSX, PPTX or DOCX; the supported-file-types table lists bmp, gif, jpe, jpeg, jpg and png for images. The Python docstring at the tag repeats the REST wording. Block (a) row 4.
- Content policy: the overview promises immediate synchronous verdicts and the resource is described as one used to evaluate content, but the REST resource and the client expose only create, delete, get, list and patch. New in this pass: IAM defines the permission dlp.contentPolicies.apply and a role DLP Content Policies Consumer. Block (a) row 5.
- CryptoHashConfig output: the transformation table says a 32-byte hexadecimal string; the body text and the pseudonymisation page say base64. Block (c) row 6.
- Bucketing input type: the table says Any; the bucketing text says numerical data. Block (c) rows 9 and 10.
- Region list: the locations page lists 43 regions including asia-southeast3 (Bangkok); the REST reference regional endpoint list has 42 of them and omits asia-southeast3. Block (f) row 2.
- Libraries page: the Python text says samples work with Python 2.7.x and 3.4 and higher while the package at the tag requires Python 3.10 or newer; the Ruby line installs google-api-client. Block (d) rows 3 and 4.
- Limits page: two rate-quota rows carry the identical name Number of requests to a regional endpoint per minute per region (600 and 100); only the descriptions tell the global-with-location and regional endpoint rows apart. Block (e) rows 12 and 13.
- Domain: cloud.google.com/sensitive-data-protection/docs answers HTTP 301 to docs.cloud.google.com/sensitive-data-protection/docs, and cloud.google.com/dlp/docs answers HTTP 301 to cloud.google.com/sensitive-data-protection/docs (curl -I, observed 2026-10-09); seeds.md still carries the old host. Not a content conflict.

Counts I made myself (all labelled Inferred in the cells):
- 261 infoTypes in the infoType categories table (261 distinct names, 240 ANY_LOCATION and 21 REGIONAL). The same 261 names appear in the description table. The sensitivity-score table has 157 high, 95 moderate and 9 low = 261.
- 24 groups in block (b); the grouping is my own rule: explicit name sets for global groups, the Location column for country groups, name prefixes for document and image groups. The group counts sum to 261.
- 43 regions on the locations page, counted from the Region name cells.

Uncertain or not read:
- gcloud dlp command group: not found in the pages read; not claimed.
- Web demo app at cloud.google.com/dlp/demo: HTTP 200, page title only; not exercised (read-only rule). What it does with entered text is unknown.
- googleapis/python-dlp archive notice: the P0 note recorded it, the GitHub page returned HTTP 403 today and a fresh clone was not permitted, so the cell labels it To be verified.
- Apigee, Data Fusion and the BigQuery tutorial were read only far enough to name the path, actions and requirements. The AWS S3 sample (GitHub, HTTP 403 observed 2026-10-09) and the JDBC community tutorial were not read.
- Other client libraries (Java, Go, Node.js, C#, PHP, Ruby) were not read at a pinned ref.
- Model Armor rows are kept to the integration-path facts; Model Armor internals (categories, limits, result fields) belong to the Model Armor columns.
- Customer-data-use terms were not read (To be verified in block (f)).
- Whether bucketing, date shift and time part can be used on free text through infoType transformations needs testing.
- Region support for DOCUMENT_TYPE/CONTEXT infoTypes: the reference lists europe, global and us only, so asia-southeast1 and the asia multi-region are not listed for them; this matters for Singapore tests.

Facts from summarising fetches: none. Every page was read as raw text with fetch_text.py on 2026-10-09; verbatim phrases used in cells were re-matched against the saved page text (85 phrases, 0 misses). Pages that were guesses and returned 404 (risk-analysis, deidentify-storage-data, hybrid-jobs, data-residency, sensitive-data-discovery under the docs path) are not cited.
