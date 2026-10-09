"""Inventory edits for sdp_inventory_final.md (blocks (a) to (f)). Source texts are in sdp_resolutions_1/2.md."""
DOCS = "https://docs.cloud.google.com/sensitive-data-protection/docs"
GITHUB_REST = DOCS + "/reference/rest/v2/projects.content/reidentify"


def apply_inv(d):
    # ------------------------------------------------ head (scope paragraph)
    d.sub("head", "Scope: Google Cloud Sensitive Data Protection", "Covered-by cells use the six provisional SDP column headers.",
          "Covered-by cells use the six SDP column headers.", "T1 (R018)", "prefix frozen at CP1; 'provisional' dropped")
    d.sub("head", "Scope: Google Cloud Sensitive Data Protection", "Labels use the sheet's allowed forms;", "Labels use the allowed forms;",
          "T89", "process wording")
    d.sub("head", "Scope: Google Cloud Sensitive Data Protection", "Counts that are mine are labelled Inferred with the counting rule.",
          "Counts made by tallying rows on a page are labelled Inferred and state the counting rule.", "T89", "first-person wording")
    d.sub("head", "Scope: Google Cloud Sensitive Data Protection", "(REST root = DOCS/reference/rest);",
          "(REST root = DOCS/reference/rest); RPC reference = DOCS/reference/rpc/google.privacy.dlp.v2; API discovery document = the Google API discovery document for the DLP API v2, revision 20261006;", "T9",
          "short names for the RPC reference and the discovery document cited in the content-policy row")
    d.sub("head", "Scope: Google Cloud Sensitive Data Protection",
          "Model Armor docs and Gemini Enterprise docs are cross-reference pages and are marked not SDP docs.",
          "Model Armor docs, Gemini Enterprise docs, Apigee docs, Cloud Data Fusion docs and Google Cloud terms pages are cross-reference pages and are marked not SDP docs. Two Google sample repositories (GoogleCloudPlatform/dlp-dataflow-deidentification and GoogleCloudPlatform/community) are cited as supporting material only.",
          "T7, T79 (main ruling)", "Google-authored pages outside the SDP docs are official but flagged; sample repos are supporting only")

    # ------------------------------------------------ (a)
    d.sub("(a)", "Components of the DLP API grouped by what they do.",
          "its evaluation call is not exposed in the REST resource or the Python client",
          "no call that submits content to a policy is documented in the REST resource, the RPC reference or the Python client",
          "T9", "R018 upgrade condition checked; wording matches the evidence")
    d.cell("(a)", "Image redaction", 4,
           old="The REST reference says the content must be PNG, JPEG, SVG or BMP [Documented] (REST redact). The redaction guide says content redaction is not supported for SVG, PDF, XLSX, PPTX or DOCX files [Documented] (DOCS redacting-sensitive-data-images). The supported-file-types table lists bmp, gif, jpe, jpeg, jpg and png for images [Documented] (DOCS supported-file-types). These three statements list different image types and do not agree [Inferred] (premise: SVG appears in one list and is excluded in another, GIF appears only in the third).",
           repl="The REST reference says the content must be PNG, JPEG, SVG or BMP [Documented] (REST redact). The Python docstring at the tag repeats it [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (types/dlp.py RedactImageRequest). The redaction guide says it can redact many image types including JPEG, BMP and PNG, and that content redaction is not supported for SVG, PDF, XLSX, PPTX or DOCX files [Documented] (DOCS redacting-sensitive-data-images). The inspect guide says it can inspect many image types including JPEG, BMP, PNG and SVG [Documented] (DOCS inspecting-images). The method-types page names JPEG, PNG or TIFF as redaction formats [Documented] (DOCS concepts-method-types). The inspection and de-identification table on the supported-file-types page lists bmp, gif, jpe, jpeg, jpg and png for images, with Redaction under Transformation support [Documented] (DOCS supported-file-types). The client enum has IMAGE, IMAGE_JPEG, IMAGE_BMP, IMAGE_PNG and IMAGE_SVG and no GIF [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (types/dlp.py BytesType). The statements do not agree on SVG, GIF and TIFF [Inferred] (premise: SVG is accepted in the REST and inspect texts and excluded in the redaction guide; GIF appears only in the file-types table; TIFF only on the method-types page).",
           tid="T66", reason="all six format statements carried (the row had three); docstring now a labelled fact")
    d.cell("(a)", "Image redaction", 7,
           old="https://docs.cloud.google.com/sensitive-data-protection/limits",
           repl="https://docs.cloud.google.com/sensitive-data-protection/limits ; " + DOCS + "/inspecting-images ; https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py",
           tid="T66", reason="sources of the new statements")
    d.cell("(a)", "Content policies", 1,
           new="projects.locations.contentPolicies with the methods create, delete, get, list and patch [Documented] (REST contentPolicies, REST root, API discovery document revision 20261006). The DlpService RPC reference lists CreateContentPolicy, DeleteContentPolicy, GetContentPolicy, ListContentPolicies and UpdateContentPolicy [Documented] (RPC reference). The Python client has create_content_policy, update_content_policy, get_content_policy, list_content_policies and delete_content_policy [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (client.py). A method that submits content to a policy for a verdict [Not disclosed] (checked the discovery document, RPC reference, REST root and resource pages, the content-policy and manage pages, release notes and client.py at the tag)",
           tid="T9, T91", reason="absence claims were labelled [Documented]; now [Not disclosed] naming what was checked; discovery document and RPC reference added")
    d.cell("(a)", "Content policies", 2,
           old="The call that submits content for a verdict is not exposed [Not disclosed] (checked the same pages). IAM has a permission dlp.contentPolicies.apply and a role DLP Content Policies Consumer, described as Apply content policies [Documented] (DOCS access-control/roles-permissions); an apply operation exists somewhere in the service [Inferred] (premise: a permission with that name is defined)",
           repl="IAM has a permission dlp.contentPolicies.apply, inside roles/dlp.user and the role DLP Content Policies Consumer (Apply content policies) [Documented] (DOCS access-control/roles-permissions). The Gemini Enterprise service account is told to hold roles/dlp.user to apply policies [Documented] (DOCS manage-content-policies). The apply permission is what that service account uses, with no public method for other callers [Inferred] (premise: the manage page names this as the only consumer and no method is listed)",
           tid="T9", reason="old inference 'an apply operation exists somewhere in the service' removed")
    d.cell("(a)", "Content policies", 5,
           old="(premise: the evaluation call is not in the REST resource or the client)",
           repl="(premise: no apply or evaluate method is documented in the REST resource, the RPC reference or the client)",
           tid="T9", reason="premise matches the evidence checked")
    d.cell("(a)", "Content policies", 7,
           old="https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies",
           repl="https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies ; " + DOCS + "/reference/rpc/google.privacy.dlp.v2",
           tid="T9", reason="RPC reference URL")

    # ------------------------------------------------ (b)
    d.sub("(b)", "Built-in infoTypes grouped, not one row per infoType",
          "Group boundaries are my own; counts come from the infoType categories table on the same page.",
          "Group boundaries follow one rule: explicit name sets for the global groups, the Location column for the country groups and name prefixes for the document and image groups; counts come from the infoType categories table on the same page.",
          "T89", "first-person wording in a note that becomes a merged note on the sheet")
    d.gsub(r"\(my count of rows in the infoType categories table, grouped by my own rule\)",
           "(count of rows in the infoType categories table, grouped by the rule in the block note)", "T89",
           "first-person wording in 24 count cells", secs_filter=lambda s: s == "(b)")
    d.gsub(r"\(my count of the Industry column\)", "(count of the Industry column)", "T89", "first-person wording", secs_filter=lambda s: s == "(b)")
    d.cell("(b)", "Health (global)", 2,
           old="A MEDICAL_ID behaviour change took effect for InfoType.version latest, with the old behaviour on stable [Documented] (DOCS release-notes)",
           repl="Since 2026-07-13, MEDICAL_ID with InfoType.version unset or stable also reports MEDICAL_RECORD_NUMBER findings as MEDICAL_ID; the old behaviour is available with version legacy for 90 days [Documented] (DOCS release-notes). The legacy window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)",
           tid="T44 (CORRECTION)", reason="the 2026-07-13 note applies to unset and stable, and legacy gives the old behaviour; the draft had latest and stable the wrong way round")
    d.cell("(b)", "Image object detectors", 2,
           old="(DOCS infotypes-reference, Image-based infoTypes)",
           repl="(DOCS infotypes-reference, Image-based infoTypes). The launch stage of the other object detectors is not stated [Not disclosed] (checked the reference and release notes, which say available without a stage)",
           tid="T18, T73", reason="Preview is stated for the face detector only")
    d.cell("(b)", "Image context (safety) detectors", 2,
           old="Accuracy and the model behind them [Not disclosed] (checked the reference, concepts-image-redaction and release-notes pages)",
           repl="Accuracy and the model behind them [Not disclosed] (checked the reference, concepts-image-redaction and release-notes pages). Launch stage [Not disclosed] (checked the reference and the release note of 2026-01-16, which says available)",
           tid="T73", reason="stage not stated for the image context detectors")

    # ------------------------------------------------ (c)
    rev_old = "No: the Can Reverse cell is empty [Documented] (DOCS transformations-reference, transformation table)"
    rev_new = "No: not on the list of reversible transformations, and the Can Reverse cell is empty [Documented] (REST reidentify, DOCS transformations-reference, transformation table)"
    ref_old = "No: the Referential Integrity cell is empty [Documented] (DOCS transformations-reference, transformation table)"
    ref_new = "Not marked: the Referential Integrity cell is empty [Documented] (DOCS transformations-reference, transformation table). Read as No [Inferred] (premise: the table ticks the property where it holds)"
    rev_rows = ["Redaction", "Replacement with a value", "Replacement from a dictionary", "Replacement with the infoType name", "Character masking",
                "Pseudonymisation by cryptographic hash", "Bucketing in fixed-size ranges", "Bucketing in custom ranges", "Date shifting", "Time extraction"]
    ref_rows = ["Redaction", "Replacement with a value", "Replacement from a dictionary", "Replacement with the infoType name", "Character masking",
                "Bucketing in fixed-size ranges", "Bucketing in custom ranges", "Time extraction"]
    for r in rev_rows:
        d.cell("(c)", r, 2, old=rev_old, repl=rev_new, tid="T88",
               reason="reading an empty cell as 'No' needs the REST reidentify list as support; the 10 non-reversible objects are not on that list")
        d.cell("(c)", r, 7, old=d.split_row(d.lines[d.find("(c)", "| " + r + " |")[0]])[7],
               repl=d.split_row(d.lines[d.find("(c)", "| " + r + " |")[0]])[7] + " ; " + GITHUB_REST,
               tid="T88", reason="source of the new reversible-list statement")
    for r in ref_rows:
        d.cell("(c)", r, 3, old=ref_old, repl=ref_new, tid="T88",
               reason="an empty table cell read as 'No' is an inference: label split [Documented] cell state, [Inferred] reading")
    d.cell("(c)", "Pseudonymisation by cryptographic hash", 6,
           new="Sensitive Data Protection: Sensitive-data masking and de-identification in text",
           tid="T65 (main ruling)", reason="hashing is one-way; the reversible tokenisation column (SD4) is kept per R018 and is not covered by the hash row")
    d.cell("(c)", "Pseudonymisation by deterministic token (AES-SIV)", 5,
           old="Surrogate annotation allows re-identification with the original key and the entire output value [Documented] (DOCS pseudonymization)",
           repl="Surrogate annotation allows re-identification with the original key and the entire output value [Documented] (DOCS pseudonymization). The transformations table row says the token has the same length as the input, while the same page's deterministic section and the pseudonymization page say length is not preserved [Documented] (DOCS transformations-reference, DOCS pseudonymization)",
           tid="T14", reason="the length conflict is carried in the inventory as in the column (README section 3 rule 4)")

    # ------------------------------------------------ (d)
    d.cell("(d)", "Python client library (google-cloud-dlp 3.40.0)", 5,
           old="google-api-core[grpc] >=2.28.0 and <3.0.0", repl="google-api-core with the grpc extra, version 2.28.0 or higher and below 3.0.0",
           tid="T90", reason="bracket pair that is not a label")
    d.cell("(d)", "Python client library (google-cloud-dlp 3.40.0)", 5,
           old="The older googleapis/python-dlp repository is reported archived with its contents moved to google-cloud-python [To be verified] (exploration note only; the GitHub page returned HTTP 403 on 2026-10-09 and the archive notice was not re-read)",
           repl="The older googleapis/python-dlp repository is archived and its README says the contents and history moved to google-cloud-python [Documented: repo googleapis/python-dlp@21b91b9d] (README.rst)",
           tid="T81", reason="archive notice read from a shallow clone (R013)")
    d.cell("(d)", "Python client library (google-cloud-dlp 3.40.0)", 7,
           old="https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/LICENSE",
           repl="https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/LICENSE ; https://github.com/googleapis/python-dlp/blob/21b91b9d51d4b21784ddede99d16ff15279c8f52/README.rst",
           tid="T81", reason="source of the archive notice")
    d.cell("(d)", "Other client libraries", 5,
           old="The other libraries were not read at a pinned ref [Not disclosed] (only the libraries page was read). ", repl="",
           tid="T80", reason="'not read' is a research choice, not vendor silence")
    d.cell("(d)", "Cloud console, gcloud CLI and web demo", 4,
           old="What the demo app does with entered text [To be verified] (not exercised, read-only rule)",
           repl="What the demo app does with entered text [Not disclosed] (checked the demo page, which shows only its title, the SDP docs navigation and the infoTypes concepts page)",
           tid="T94, T89", reason="absence labelled [Not disclosed] naming the pages; process wording removed")
    d.cell("(d)", "Cloud console, gcloud CLI and web demo", 5,
           old="Not signed in to or run for this sheet. The demo page may help a quick manual test but its data handling is unknown [To be verified]",
           repl="Not signed in to or run. The demo page may help a quick manual test but its data handling is not described [Not disclosed] (checked the demo page, the SDP docs navigation and the infoTypes concepts page)",
           tid="T89, T94", reason="process wording removed; label")
    d.cell("(d)", "Model Armor basic mode", 2,
           old="Not covered in this sheet [Inferred]", repl="Covered by the Model Armor columns, not repeated here [Inferred]", tid="T89", reason="process wording")
    d.cell("(d)", "Model Armor basic mode", 3,
           old="Not covered in this sheet [Inferred]", repl="Covered by the Model Armor columns, not repeated here [Inferred]", tid="T89", reason="process wording")
    d.cell("(d)", "Model Armor advanced mode", 2,
           old="Not covered in this sheet [Inferred]", repl="Covered by the Model Armor columns, not repeated here [Inferred]", tid="T89", reason="process wording")
    d.cell("(d)", "Model Armor advanced mode", 5,
           old="rows in block (a) [Documented] (this sheet)", repl="rows in block (a)", tid="T90, T89",
           reason="self-referential label removed (an internal pointer, not a source fact)")
    d.cell("(d)", "Gemini Enterprise content-policy attachment", 5,
           old="Not applied to older data stores such as Cloud Storage, BigQuery or websites [Documented] (Gemini Enterprise docs, not SDP docs)",
           repl="Not applied to older data stores such as Cloud Storage, BigQuery or websites [Documented] (Gemini Enterprise docs, not SDP docs). Gemini Enterprise attaches a policy through its own API field sensitiveDataProtectionPolicy.policy, the content policy resource name [Documented] (Gemini Enterprise docs, not SDP docs; REST DataProtectionPolicy)",
           tid="T9", reason="a policy is attached by name, not by submitting content")
    d.cell("(d)", "Cloud Data Fusion", 7, new="https://docs.cloud.google.com/data-fusion/docs/how-to/using-dlp", tid="T79",
           reason="the cloud.google.com URL answers HTTP 301; the redirect target is cited")
    d.cell("(d)", "BigQuery at query time", 2,
           old="Roles and service accounts are set in the tutorial steps [To be verified] (not read in detail)",
           repl="The tutorial gives the Cloud Run service account roles/dlp.reader and roles/dlp.user [Documented] (DOCS deidentify-bq-tutorial)",
           tid="T79", reason="tutorial read")
    row = "Dataflow, AWS S3 and JDBC guides"
    d.cell("(d)", row, 1,
           new="The SDP navigation lists three guides: AWS S3 (links to the GoogleCloudPlatform/dlp-dataflow-deidentification repository), JDBC databases (links to a Google community tutorial) and a Dataflow, BigQuery ML anomaly detection solution [Documented] (DOCS sensitive-data-protection-overview, navigation). The S3 sample is a Dataflow pipeline that inspects, de-identifies and re-identifies Avro, CSV, JSONL, ORC, Parquet and TSV files from Cloud Storage or Amazon S3 and writes to BigQuery, and its Java code builds InspectContentRequest, DeidentifyContentRequest and ReidentifyContentRequest [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (README.md, src/main/java/com/google/swarm/tokenization/beam; Google sample repository, supporting only). The JDBC tutorial inspects SQL tables with a hybrid inspection job and is archived in GoogleCloudPlatform/community [Documented: repo GoogleCloudPlatform/community@6f68203d] (archived/dlp-hybrid-inspect/index.md; Google sample repository, supporting only). The anomaly detection page answers HTTP 301 to the SDP docs home [Documented] (observed 2026-10-09)",
           tid="T79 (main ruling: sample repos supporting only)", reason="linked guides read; row kept at 13 rows")
    d.cell("(d)", row, 2,
           new="The sample's Dataflow runner role lists serviceusage.services.use, dlp.kms.encrypt and get and list on inspect and de-identify templates [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (dlp_tokenizing_runner_permissions.yaml; Google sample repository, supporting only). The JDBC tutorial lists creating a secret in Secret Manager among its objectives [Documented: repo GoogleCloudPlatform/community@6f68203d] (archived/dlp-hybrid-inspect/index.md; Google sample repository, supporting only)",
           tid="T79", reason="was 'Not read [To be verified]'")
    d.cell("(d)", row, 3,
           new="The S3 sample creates a bucket in us-central1 and a BigQuery dataset in the US multi-region for its demo [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (README.md; Google sample repository, supporting only). No regional endpoint guidance for SDP in the guides [Not disclosed] (checked the README and the tutorial)",
           tid="T79", reason="was 'Not read [To be verified]'")
    d.cell("(d)", row, 4,
           new="Not AI: batch file and database scanning and tokenisation [Inferred] (premise: the S3 sample reads files and the JDBC tutorial reads database tables)",
           tid="T79", reason="premise from the pages read")
    d.cell("(d)", row, 5,
           new="Content methods are used for batch files in the S3 sample, so the row stays inventory only; the guides do not target prompts or responses [Inferred] (premise: the README describes file pipelines). Apache License 2.0 for the sample repository [Documented: repo GoogleCloudPlatform/dlp-dataflow-deidentification@4213e271] (LICENSE)",
           tid="T79", reason="was 'whether any of these guides uses a content method [To be verified] (not read)'")
    d.cell("(d)", row, 7,
           old="https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview",
           repl="https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview ; https://github.com/GoogleCloudPlatform/dlp-dataflow-deidentification/blob/4213e271f5889c7b889d98ab5b0623f1406687b0/README.md ; https://github.com/GoogleCloudPlatform/community/blob/6f68203dec458268f177e97e2b57f3e085ca3668/archived/dlp-hybrid-inspect/index.md",
           tid="T79", reason="pinned blob URLs (R013)")

    # ------------------------------------------------ (e)
    lim_app = " The limits table is headed as covering inspecting and de-identifying content and does not name content.reidentify [Documented] (LIM). Whether it applies to content.reidentify [Inferred] (premise: the request carries the same item and configuration types)"
    d.cell("(e)", "Maximum size of each request, except image.redact", 1, old="Larger files should go to Cloud Storage and an inspection job [Documented] (LIM)",
           repl="Larger files should go to Cloud Storage and an inspection job [Documented] (LIM)." + lim_app, tid="T21",
           reason="the draft applied the limit to content.reidentify as [Documented]; the page does not name it")
    d.cell("(e)", "Maximum size of each request, except image.redact", 2, new="content.inspect, content.deidentify", tid="T21",
           reason="reidentify removed from the documented scope")
    d.cell("(e)", "Maximum transformations per request", 1, old="100 [Documented] (LIM)", repl="100 [Documented] (LIM)." + lim_app, tid="T21",
           reason="as above")
    d.cell("(e)", "Maximum transformations per request", 2, new="content.deidentify", tid="T21",
           reason="reidentify removed; only content.deidentify applies transformations to detected values")
    d.cell("(e)", "Maximum findings per request", 1,
           old="the findings returned are an arbitrary subset [Documented] (DOCS deidentify-sensitive-data)",
           repl="the findings returned are an arbitrary subset [Documented] (DOCS deidentify-sensitive-data). The REST page says this value is not a hard limit [Documented] (REST InspectConfig)",
           tid="T20", reason="second documented statement on the 3,000 figure")
    d.cell("(e)", "Custom dictionary size", 1,
           old="40 components per phrase [Documented] (LIM)",
           repl="40 components per phrase; stored infoType creation: input file in Cloud Storage 200 MB each, 1 GB combined, 100 files; BigQuery input column 1 GB and 5,000,000 rows; output files 500 MB [Documented] (LIM)",
           tid="T24", reason="stored-infoType limits were missing from the inventory")
    d.cell("(e)", "Content policy file limits", 1,
           old="Content policy price: no row on the pricing page [Not disclosed] (checked PRC)",
           repl="Content policy price and availability objective: no row on the pricing page or the SLA page [Not disclosed] (checked PRC, SLA)",
           tid="T11", reason="SLA page added to the pages checked")

    # ------------------------------------------------ (f)
    d.cell("(f)", "Regional endpoints", 1,
           old="[Inferred] (my count of region rows on the locations page; asia-southeast1 row read directly [Documented] (DOCS locations))",
           repl="[Inferred] (count of region rows on the locations page; the asia-southeast1 row is stated directly [Documented] (DOCS locations))",
           tid="T89", reason="first-person wording")
    d.cell("(f)", "Regional endpoints", 1,
           old="The two pages differ and are not reconciled",
           repl="The two pages differ and are not reconciled. The release notes of 2026-01-20 record asia-southeast3 as added [Documented] (DOCS release-notes)",
           tid="T83", reason="release note that explains the difference (optional item)")
    d.cell("(f)", "Regional endpoints", 3,
           old="https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest",
           repl="https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest ; " + DOCS + "/release-notes", tid="T83", reason="source of the release note")
    d.cell("(f)", "InfoType availability by location", 1,
           old="(my count of the Availability column)", repl="(count of the Availability column)", tid="T89", reason="first-person wording")
    d.cell("(f)", "Data handling", 1,
           old="Use of customer content for product improvement and the data processing terms [To be verified] (not covered by the product docs read; terms pages were not read)",
           repl='The Google Cloud terms say Google will "only access, use, and otherwise process Customer Data in accordance with the Cloud Data Processing Addendum and will not access, use, or process Customer Data for any other purpose" [Documented] (Google Cloud terms, not SDP docs). Sensitive Data Protection is listed among the Google Cloud Platform Services and the Service Specific Terms have no section for it [Documented] (Google Cloud terms services list and Service Specific Terms, not SDP docs). Content sent to the SDP API is therefore processed only to provide, secure and monitor the service [Inferred] (premise: the Customer Data definition covers data provided through the Services and no SDP carve-out exists)',
           tid="T92 (R019)", reason="terms pages read; applicability to SDP content is an inference")
    d.cell("(f)", "Data handling", 3,
           old="https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints",
           repl="https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints ; https://cloud.google.com/terms ; https://cloud.google.com/terms/data-processing-addendum ; https://cloud.google.com/terms/service-terms ; https://cloud.google.com/terms/services",
           tid="T92", reason="terms sources")
