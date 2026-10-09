"""Column edits for sdp_two_level.md (SD1 to SD6). Source texts are the draft impacts in sdp_resolutions_1/2.md."""
REPO = "**[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**"
DOCS = "https://docs.cloud.google.com/sensitive-data-protection/docs"
TERMS = [
    "https://cloud.google.com/terms",
    "https://cloud.google.com/terms/data-processing-addendum",
    "https://cloud.google.com/terms/service-terms",
    "https://cloud.google.com/terms/services",
]


def apply_cols(d):
    # ======================= SD1 =======================
    # ---- R2
    d.rep("SD1 R2", "• Out of purpose: the docs describe the product as discovering", [
        '• Purpose: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (SDP docs, overview page, read 2026-10-09) **[Documented]**',
        "• Out of purpose: the docs name no prompt-injection, jailbreak, toxicity or topic-drift detector (checked the overview, infoTypes concepts and reference pages); a scope judgement (premise: the purpose sentence above) **[Inferred]**",
    ], "T19 (R015)", "one label pattern for the out-of-purpose statement: purpose sentence [Documented], conclusion [Inferred] with its premise")
    d.sub("SD1 R2", "has 522 name and description cells",
          "(counted from the fetched page text by pairing the two cells after the Name and Description header; Google gives no total)",
          "(premise: one name cell and one description cell per infoType, paired after the Name and Description header in the page text; Google gives no total)",
          "T98", "state the premise of a count bullet")
    d.sub("SD1 R2", "location filter with 51 entries", "(counted from the fetched page text)",
          "(premise: the filter list on the reference page, counted in the page text)", "T98", "state the premise of a count bullet")
    d.sub("SD1 R2", "The secrets group lists 21 names",
          "(counted from the fetched page text by listing the entries between the Secrets heading and the Image-based infoTypes heading)",
          "(premise: the entries listed between the Secrets heading and the Image-based infoTypes heading, counted in the page text)",
          "T98", "state the premise of a count bullet")
    d.rep("SD1 R2", "• No other Singapore-named infoType exists",
          "• No other Singapore-named infoType is named in the reference: a search of the reference text for the string singapor found only the NRIC row, the passport row and the `PASSPORT` country list, so no FIN, UEN or address infoType is named (checked the reference and concepts pages) **[Not disclosed]**",
          "hygiene (T38)", "absence claim worded as 'none named in the reference', not 'does not exist'")

    # ---- R3
    d.rep("SD1 R3", "• The metadata-label page shows a `content.inspect` request that sends a PDF", [
        "• The metadata-label page shows a `content.inspect` request that sends a PDF as a `byteItem` of type `PDF` (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**",
        "• PDF byte items are accepted by `content.inspect`; which other file types are accepted is not stated per method (premise: the documented example; the supported-file-types table has no per-method column) **[Inferred]**",
    ], "T78", "split the documented example from the inference; file bytes stay Detail-level in this column (main ruling)")

    # ---- R4
    d.sub("SD1 R4", "Summary: ", " The service was formerly called Cloud DLP. **[Documented]**", " **[Documented]**",
          "T1 (R018)", "'formerly Cloud DLP' stays in R1 and R4 Detail; the Summary uses the new name only", full=True)
    d.rep("SD1 R4", "• Versioning: release notes show `InfoType.version` values", [
        "• `InfoType.version` values: release notes show `stable`, `latest` and `legacy` (release notes dated 2026-07-13 and 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**",
        '• For the new `PERSON_NAME` version the note says "In 30 days, the new version will be promoted to stable." (release note dated 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**',
    ], "T44", "one fact per bullet (versions; promotion quote)")
    d.rep("SD1 R4", "• Content-policy conflict, source 2b:",
          "• Content-policy conflict, source 2b: the client at the tag has `create_content_policy`, `update_content_policy`, `get_content_policy`, `list_content_policies` and `delete_content_policy` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:7363` \"def create_content_policy(\") " + REPO,
          "T91, T9", "the code bullet states only what the file contains; the absence goes in the next bullet")
    d.rep("SD1 R4", "• No documented way to submit an arbitrary string to a content policy", [
        "• No documented way to submit an arbitrary string to a content policy was found (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages, release notes and the client methods) **[Not disclosed]**",
        '• The roles page defines the permission `dlp.contentPolicies.apply` and the role DLP Content Policies Consumer ("Apply content policies."), and the manage page tells the administrator to grant `roles/dlp.user` to the Gemini Enterprise service account to apply policies (SDP docs, roles and permissions page and manage content policies page, read 2026-10-09) **[Documented]**',
    ], "T9", "R018 upgrade condition checked: no public apply or evaluate method; permission and role facts added")
    d.rep("SD1 R4", "• For how Model Armor calls SDP, see the Model Armor columns",
          '• For how Model Armor calls SDP, see the Model Armor columns "Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)" and "Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)"; those internals are not repeated here (premise: a pointer to the owning columns, not a source fact) **[Inferred]**',
          "T6", "headers written out in full and frozen by R017; 'provisional' dropped")
    d.rep("SD1 R4", "• Open-source and managed-cloud analogues for comparison only:",
          "• Open-source and managed-cloud analogues for comparison only: `Presidio: PII detection in text (Analyzer)` and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either (premise: a pointer to the sibling columns only) **[Inferred]**",
          "T6", "'provisional header' dropped (Presidio prefix frozen by R016)")

    # ---- R6
    d.rep("SD1 R6", "Summary: ",
          "Summary: **A project, a location and a list of infoTypes.** Send the text, the infoTypes and an optional minimum likelihood. The caller needs billing, the API enabled and the DLP User role. Requests are capped at 0.5 MB; REST calls the 3,000-finding limit not hard. **[Documented]**",
          "T20 (CORRECTION)", "the REST InspectConfig page says the 3,000 value 'isn't a hard limit'; 'capped at 3,000 findings' removed", full=True)
    d.ins_after("SD1 R6", "  – Maximum number of built-in and custom infoTypes per request | 150",
                '• Findings limit, second source: "If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower. This value isn\'t a hard limit." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**',
                "T20", "second documented statement kept as its own bullet")
    d.ins_after("SD1 R6", "• Default list, source 3:", [
        '• Default list, source 4: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**',
        "• The members of ALL_BASIC are not defined on any page checked (concepts, REST InspectConfig, content.inspect, content.deidentify and image.redact method pages, image guides, infoType reference, infoTypes.list page, release notes) **[Not disclosed]**",
    ], "T42", "fourth wording quoted; ALL_BASIC membership recorded as not disclosed (R020)")
    d.rep("SD1 R6", "• A 2019 release note says",
          '• A 2019 release note says "Updated the default list of infotypes included in ALL_BASIC." (release note dated 2019-02-11; SDP docs, release notes, read 2026-10-09) **[Documented]**',
          "hygiene", "inference ('so the default set has changed before') removed from a [Documented] bullet (README section 3 rule 5)")

    # ---- R7
    d.sub("SD1 R7", "• Minimum setup: one Google Cloud project", "• Minimum setup:", "• **Minimum setup:**", "style 8",
          "README section 4: first R7 Detail bullet starts with the bold phrase")
    d.sub("SD1 R7", "• No offline or emulator mode exists", "No offline or emulator mode exists in the docs or the client package",
          "No offline or emulator mode was found in the docs or the client package", "hygiene", "absence worded as 'was found', not 'exists'")
    d.rep("SD1 R7", "• There is no first-party evaluation toolkit for detection quality", [
        "• There is no first-party evaluation toolkit for detection quality (checked the docs navigation, the quickstarts and the client repo) **[Not disclosed]**",
        '• The docs say: "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**',
    ], "hygiene (T37)", "one bullet, two facts under one label split: absence [Not disclosed], quote [Documented]")
    d.ins_after("SD1 R7", "• A web demo exists:",
                "• What the web demo does with text entered into it is not described (checked the demo page, the SDP docs navigation and the infoTypes concepts page) **[Not disclosed]**",
                "T94", "caveat placed next to the test aid")
    d.ins_after("SD1 R7", "• Record the read date and the `InfoType.version` used",
                "• No promotion note for the new `PERSON_NAME` version had appeared (checked the release notes, whose newest entry is dated 2026-10-03, read 2026-10-09) **[Not disclosed]**",
                "T44", "state of the release notes on the read date; re-read due at P7 and P9")

    # ---- R8
    d.rep("SD1 R8", "• Content-policy evaluation: the REST resource and client have no evaluate method",
          '• Content-policy evaluation: the discovery document, RPC reference, REST resource and client list no apply or evaluate method, although the roles page defines the permission `dlp.contentPolicies.apply` and a role "Apply content policies."; how a caller outside Gemini Enterprise submits a string is not documented (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages and the client; needs a Gemini Enterprise check)',
          "T9", "R8 bullet updated with the pages checked")
    d.rep("SD1 R8", "• Customer-data terms: whether content sent to the API can be used by Google",
          "• Customer-data terms: the Google Cloud terms limit Google's processing of Customer Data to what the Data Processing Addendum allows, and the Service Specific Terms have no Sensitive Data Protection section; whether any SDP-specific use of content applies is not stated (checked the terms of service, Data Processing Addendum, Service Specific Terms and services list; the docs say request data \"is not stored\")",
          "T92 (R019)", "terms pages read; question narrowed")
    d.add_r9("SD1", [DOCS + "/reference/rpc/google.privacy.dlp.v2"] + TERMS, "T9, T92",
             "R9 completeness: RPC reference named in the R4 'checked' list; terms pages named in R8")

    d.rep("SD1 R8", "• Which infoTypes run when none are listed",
          "• Which infoTypes run when none are listed: the docs give several wordings (a testing-only default list, a list that may change, ALL_BASIC, the most common infoTypes for images, all built-in infoTypes in de-identification) and no page defines ALL_BASIC; the exact membership needs an `infoTypes.list` call or a test",
          "T42", "five wordings were confirmed (the bullet said three); process wording 'read-only rule' removed")
    d.sub("SD4 R1", "• Tokenising a prompt before the model", "the docs read for this column describe no LLM round trip",
          "no LLM round trip is described on the pages cited for this column", "style 7", "process wording")

    # ======================= SD2 =======================
    d.rep("SD2 R1", "• Surrogate detectors exist only to reverse format-preserving encryption", [
        '• The InspectConfig reference has the description "Message for detecting output from deidentification transformations that support reversing." for surrogate detection (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**',
        "• Surrogate detectors go with the reversible transformations and are described in the reversible tokenisation and re-identification column, not here (premise: the surrogate-type description above) **[Inferred]**",
    ], "hygiene", "the original 'exist only to reverse FPE in content.reidentify' was a scope remark inside a [Documented] bullet and conflicts with the AES-SIV surrogate use in the tokenisation column; split into a quoted fact and a pointer")
    d.rep("SD2 R4", "• Regex syntax: a code sample on the docs says", [
        '• Regex syntax: the REST Regex reference says "Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub." (SDP docs, REST Regex page, read 2026-10-09) **[Documented]**',
        '• A docs code sample comment also says "Refer https://github.com/google/re2/wiki/Syntax for creating regular expression." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**',
    ], "T47", "REST reference points to RE2 syntax; supported constructs stay a test item")
    d.ins_before("SD2 R4", "• Rule order, context:",
                 '• Rule order, worked example: "If you specify the exclusion rule first, then the DOCUMENT_TYPE/CONTEXT/HEALTH findings are excluded from the result set before they can be used to provide context to the adjustment rule." (SDP docs, creating custom infoTypes rules page, read 2026-10-09) **[Documented]**',
                 "T49", "guide's worked example supports order-as-written")
    d.rep("SD2 R4", "• Rule order, context:",
          '• Rule order, release note 2026-02-23 puts "Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset" at general availability; the REST page that says exclusion rules run last has a later footer date (2026-09-05), so it may be unchanged text rather than older text (premise: footer dates; they do not prove edits) **[Inferred]**',
          "T49", "'REST text may be older' weakened: REST footer is later than the release note; the two documented statements stay as two bullets (main ruling)")
    d.rep("SD2 R5", "Summary: ",
          "Summary: **Same findings as inspection, under your detector name.** A custom match returns the name you chose and a likelihood you set, Very likely unless changed, after any rules have run. The response holds only the findings. **[Documented]**",
          "T17", "'There is no verdict' rested on an [Inferred] bullet; replaced by the documented response field", full=True)
    d.ins_before("SD2 R5", "• No verdict is produced; the caller acts on findings",
                 '• The inspect response has the single field `result`, "The findings." (SDP docs, REST InspectContentResponse page, read 2026-10-09) **[Documented]**',
                 "T17", "documented response field added")
    d.rep("SD2 R6", "Summary: ",
          "Summary: **A CustomInfoType object inside the inspect request.** Give a name, a dictionary, regex or stored reference, an optional base likelihood and rules. Limits per request include 30 custom detectors, 10 regular dictionaries, 10 rule sets and a regex length of 1000. **[Documented]**",
          "T20 (CORRECTION)", "the limits page gives 'Maximum length of regular expressions | 1000' with no unit; '1000-character' removed", full=True)
    d.ins_after("SD2 R6", "  – Maximum size of a single input file stored in Cloud Storage | 200 MB", [
        "  – Maximum combined size of all input files stored in Cloud Storage | 1 GB",
        "  – Maximum number of input files stored in Cloud Storage | 100",
        "  – Maximum size of an input column in BigQuery | 1 GB",
    ], "T24", "three stored-infoType limits from the limits page added (optional item)")
    d.rep("SD2 R6", "• The caller's role `roles/dlp.user` lists only", [
        "• `roles/dlp.user` is \"Inspect, Redact, and De-identify Content\" and lists `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*` and `serviceusage.services.use`, with no `dlp.storedInfoTypes.*` permission (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**",
        "• `dlp.storedInfoTypes.get` and `dlp.storedInfoTypes.list` are listed under DLP Reader (`roles/dlp.reader`) and DLP Viewer (`roles/dlp.viewer`), and the REST `content.inspect` page names only `serviceusage.services.use` on the parent (SDP docs, roles and permissions and REST projects.content.inspect pages, read 2026-10-09) **[Documented]**",
        "• Whether a request that names a stored infoType needs `dlp.storedInfoTypes.get` on top of `roles/dlp.user` (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; not stated) **[Not disclosed]**",
    ], "T51", "role contents documented; the requirement is not disclosed; permission test stays in R8")
    d.sub("SD2 R7", "• Minimum setup: the project, billing, API", "• Minimum setup:", "• **Minimum setup:**", "style 8",
          "README section 4: first R7 Detail bullet starts with the bold phrase")
    d.ins_after("SD2 R7", "• Cost and data handling match built-in inspection",
                "• No offline or emulator mode applies to custom detectors; they run inside the same hosted inspect call as built-in detectors, for which none was found (checked the overview, method types, libraries, endpoints and locations pages and the package README) **[Not disclosed]**",
                "T37", "harmonised with the other five R7 rows, which carry an emulator bullet")
    d.rep("SD2 R8", "• Regex engine and unsupported constructs",
          "• Which RE2 constructs are accepted by the service and what happens with unsupported ones (the reference names RE2 syntax only; needs testing)",
          "T47", "R8 bullet reworded now that the reference names RE2")
    d.rep("SD2 R8", "• Whether `roles/dlp.user` is enough to use a stored infoType",
          "• Whether `roles/dlp.user` alone is enough to use a stored infoType in `content.inspect`: the role holds no stored-infoType permission and no page states what the request needs (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; needs a permission test)",
          "T51", "pages checked listed")
    d.rep("SD2 R8", "Summary: ",
          "Summary: **Key open questions.** Unsupported regex constructs, conflicting dictionary and rule-order statements, permissions for stored infoTypes, behaviour on unspaced scripts, and no published accuracy for custom detectors.",
          "T47", "R8 Summary no longer asks which regex engine applies", full=True)
    d.add_r9("SD2", [DOCS + "/reference/rest/v2/Regex", DOCS + "/reference/rest/v2/InspectContentResponse",
                     DOCS + "/reference/rest/v2/DeidentifyContentResponse", DOCS + "/reference/rest/v2/ReidentifyContentResponse"],
             "T47, T17", "R9: pages cited in the new bullets (the three response pages as listed by the resolver)")

    # ======================= SD3 =======================
    d.rep("SD3 R1", "Summary: ",
          "Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method finds sensitive values, then redacts, replaces, masks or hashes them. Bucketing and date shifting are offered but shown only on table fields. It returns the item and a summary of changes. **[Documented]**",
          "T12", "Summary claimed bucketing and date shifting on detected values while the column marks free-text use [To be verified]", full=True)
    d.ins_after("SD3 R1", "• The docs table lists 12 transformation objects",
                "• The date-shift, time-extraction and bucketing code samples on the transformation reference page use record (table) transformations (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**",
                "T12", "supports the narrowed R1 Summary ('shown only on table fields'): every Summary claim must be entailed by its own row")
    d.sub("SD3 R2", "• Out of purpose: transformations replace or hide values", "this is a scope judgement)",
          "a scope judgement; premise: the overview's purpose sentence \"discover, classify, and de-identify sensitive data\")",
          "T19, T98", "premise named for the out-of-purpose [Inferred] bullet")
    d.rep("SD3 R4", "Summary: ",
          "Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Each detected value is then redacted, replaced, masked or hashed; bucketing and date shifting are shown only on table fields. **[Documented]**",
          "T12", "same narrowing as the R1 Summary", full=True)
    d.rep("SD3 R4", "• The date-shift, time-extraction and bucketing code samples use record (table) transformations", [
        '• The API accepts `fixedSizeBucketingConfig`, `bucketingConfig`, `dateShiftConfig` and `timePartConfig` inside an infoType transformation, and describes them for numeric, timestamp and date values; `dateShiftConfig.cryptoKey` "Can only be applied to table items." (API discovery document revision 20261006, schemas PrimitiveTransformation, DateShiftConfig and TimePartConfig) **[Documented]**',
        "• The date-shift, time-extraction and bucketing code samples use record (table) transformations and a context field (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**",
        "• Whether the bucketing, date-shift and time-extraction transformations work on infoType findings in free text is not stated (checked the transformation reference; the docs table says Any or Dates/Times) **[To be verified]**",
    ], "T12", "documented API fact added; the sample fact and the open free-text question split so the TBV bullet carries one fact")
    d.ins_after("SD3 R4", "• Transformation errors: the client `DeidentifyConfig` has",
                '• The REST reference documents the same field on `DeidentifyConfig`: "Mode for handling transformation errors. If left unspecified, the default mode is TransformationErrorHandling.ThrowError."; `LeaveUntransformed` "Skips the data without modifying it if the requested transformation would cause an error." (SDP docs, REST deidentifyTemplates page, read 2026-10-09) **[Documented]**',
                "T57 (CORRECTION)", "the draft said only the client describes transformationErrorHandling; the REST reference documents it")
    d.ins_after("SD3 R4", "• No infoType listed:", [
        '• Inspection default quoted on the de-identifying page: "Otherwise, Sensitive Data Protection scans for a default set of infoTypes (ALL_BASIC), some of which you might not need." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**',
        '• When a string matches both a general and a specific infoType and both are requested, inspection reports two findings for it: "you get two findings for the same string" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**',
        "• How de-identification applies two transformations to overlapping findings of different infoTypes is not described (checked the de-identifying, transformation reference, text redaction and infoTypes concepts pages and the REST deidentify and InfoTypeTransformations references) **[Not disclosed]**",
    ], "T42, T54", "ALL_BASIC quote added; overlap: related inspection fact plus the undocumented de-identification behaviour")
    d.sub("SD3 R4", "• Replace with a value:", 'and the sample gives "My name is Alicia Abernathy, and my email address is [fake@example.com]."',
          'and in the sample the email address is replaced by the fixed text "fake@example.com"',
          "style 6", "square brackets inside a Detail bullet could be mistaken for labels")
    d.rep("SD3 R4", "• For how Model Armor invokes SDP de-identification, see the Model Armor columns",
          '• For how Model Armor invokes SDP de-identification, see the Model Armor columns "Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)" and "Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)"; those internals are not repeated here (premise: a pointer to the owning columns, not a source fact) **[Inferred]**',
          "T6", "headers written out in full and frozen by R017; 'provisional' dropped")
    d.rep("SD3 R4", "• Open-source and managed-cloud analogues for comparison only:",
          "• Open-source and managed-cloud analogues for comparison only: `Presidio: PII anonymisation and masking in text (Anonymizer)` and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either (premise: a pointer to the sibling columns only) **[Inferred]**",
          "T6", "'provisional header' dropped (Presidio prefix frozen by R016)")
    d.sub("SD3 R5", "• Only the requested infoTypes are changed:",
          'returns "My name is Alicia Abernathy, and my email address is [email-address]." with the name untouched',
          "returns the sentence with the email address replaced by its infoType name in brackets and the name untouched",
          "style 6", "square brackets inside a Detail bullet could be mistaken for labels")
    d.sub("SD3 R7", "• Minimum setup: a Google Cloud project", "• Minimum setup:", "• **Minimum setup:**", "style 8",
          "README section 4: first R7 Detail bullet starts with the bold phrase")
    d.sub("SD3 R7", "• Record the read date and detector versions", "(see the detection column) **[Inferred]**",
          "(premise: the dated release notes cited in the detection column) **[Inferred]**", "T98", "state the premise")
    d.rep("SD3 R8", "• Whether `LeaveUntransformed` error handling is reachable from REST",
          "• Whether `LeaveUntransformed` behaves as documented on a plain `content.deidentify` request, for example for a date shift applied to an IP address (the REST reference documents the field; needs testing)",
          "T57", "REST documentation now exists; the open part is behaviour")
    d.rep("SD3 R8", "• Customer-data terms: whether content sent to the API can be used by Google",
          "• Customer-data terms: the Google Cloud terms limit Google's processing of Customer Data to what the Data Processing Addendum allows, and the Service Specific Terms have no Sensitive Data Protection section; whether any SDP-specific use of content applies is not stated (checked the terms of service, Data Processing Addendum, Service Specific Terms and services list; the docs say request data \"is not stored\")",
          "T92 (R019)", "terms pages read; question narrowed")
    d.add_r9("SD3", [DOCS + "/reference/rest/v2/projects.deidentifyTemplates"] + TERMS, "T57, T92",
             "R9: REST deidentifyTemplates page cited in the new T57 bullet; terms pages named in R8")

    # ======================= SD4 =======================
    d.sub("SD4 R1", "• \"Pseudonymization is sometimes referred to as tokenization", "; the column header uses the British spelling tokenisation", "",
          "style 7", "spelling remark about the header does not belong in Detail")
    d.sub("SD4 R1", "• Tokenising a prompt before the model", "it needs the model to return the tokens unchanged **[Inferred]**",
          "it needs the model to return the tokens unchanged (premise: content methods accept any string, per the item types in R3) **[Inferred]**",
          "T98", "state the premise")
    d.sub("SD4 R1", "• Cryptographic hashing is the one-way contrast", "its row belongs to the SD3 column",
          "its row belongs to the masking and de-identification in text column", "style 4 (T65)",
          "hash row lives with the masking column (main ruling: SD4 dropped from the hash row); header words replace the column id")
    d.sub("SD4 R2", "• Detection coverage (PII, government IDs", "which follows from transformations being applied to findings **[Inferred]**",
          "(premise: transformations are applied to findings) **[Inferred]**", "T98", "state the premise")
    d.sub("SD4 R2", "• An infoType transformation names the infoTypes it applies to",
          "not a Singapore type (SDP docs, transformations-reference page, read 2026-10-09) **[Inferred]**",
          "not a Singapore type (premise: an infoType transformation lists the infoTypes it applies to; SDP docs, transformations-reference page, read 2026-10-09) **[Inferred]**",
          "T98", "state the premise")
    d.rep("SD4 R2", "• Prompt injection, jailbreaks, toxicity and topic control are not described",
          '• Out of purpose: prompt injection, jailbreaks, toxicity and topic control are not named on any page checked (overview, method-types, pseudonymization, transformation-reference and quickstart); this is a scope judgement (premise: the purpose sentence in the overview, "discover, classify, and de-identify sensitive data") **[Inferred]**',
          "T19 (R015)", "one label pattern for the out-of-purpose statement")
    d.rep("SD4 R3", "• Neither request has a field for direction, message role or prompt type",
          "• Neither request has a field for direction, message role or prompt type, so the caller decides what string to send; the column therefore applies to prompts, responses, retrieved text, tool inputs and tool outputs alike (premise: the REST request bodies for deidentify and reidentify list no such field) **[Inferred]**",
          "T98", "state the premise")
    d.ins_after("SD4 R3", "• For `content.reidentify`: \"The item to re-identify. Will be treated as text.\"",
                '• Whether `content.reidentify` accepts conversation and batch items is not stated: its item is "treated as text", and the release notes announce conversation and batch support for inspecting and de-identifying only (checked the REST reidentify and ContentItem pages, the release notes and the client request type) **[Not disclosed]**',
                "T60", "absence recorded in Detail (optional item)")
    d.sub("SD4 R3", "• Nothing in the request carries a system prompt", "so no prompt context is needed to tokenise or restore a string **[Inferred]**",
          "so no prompt context is needed to tokenise or restore a string (premise: the request fields listed above) **[Inferred]**", "T98", "state the premise")
    d.rep("SD4 R4", "Summary: ",
          "Summary: **Standard keyed encryption, not a model.** AES-SIV gives base64 tokens, and the docs disagree on whether the length is kept; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. **[Documented]**",
          "T14", "the Summary said 'of any length' against a three-way documented conflict on AES-SIV token length", full=True)
    d.rep("SD4 R4", "• A transient key \"is generated by Sensitive Data Protection", [
        '• A transient key "is generated by Sensitive Data Protection at the time of de-identification, and then discarded" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**',
        "• A transient key therefore cannot support later reversal (premise: the key is discarded after de-identification) **[Inferred]**",
    ], "hygiene", "inference ('so it cannot support later reversal') split from the quoted fact (README section 3 rule 5)")
    d.ins_after("SD4 R4", "• The client docstring names the permission needed for a KMS-wrapped key",
                '• The REST KmsWrappedCryptoKey schema says: "Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt" (SDP docs, REST deidentifyTemplates page, read 2026-10-09) **[Documented]**',
                "T63", "REST sentence added as a sibling of the client docstring bullet")
    d.sub("SD4 R4", "• Tokenisation itself uses a cryptographic algorithm", "whose backing models are covered in SD1 **[Inferred]**",
          "whose backing models are covered in the sensitive-data detection in text column (premise: the pseudonymization page names AES-SIV and FPE-FFX as the techniques) **[Inferred]**",
          "T98, style 4", "state the premise; header words replace the column id")
    d.rep("SD4 R5", "Summary: ",
          "Summary: **Transformed text plus a summary of changes.** The response returns the item with tokens or restored values and an overview listing each transformation with success or error counts. A token is a surrogate name, a length and the encrypted value. **[Documented]**",
          "T17", "'no verdict' rested on an [Inferred] bullet; Summary now states the documented response fields", full=True)
    d.ins_before("SD4 R5", "• The call returns no score, likelihood or allow or block verdict",
                 '• The REST response for `content.reidentify` has the fields `item` ("The re-identified item.") and `overview` ("An overview of the changes that were made to the item.") (SDP docs, REST ReidentifyContentResponse page, read 2026-10-09) **[Documented]**',
                 "T17", "documented response fields added")
    d.sub("SD4 R5", "• The call returns no score, likelihood or allow or block verdict",
          "which follows from the two response fields above **[Inferred]**",
          "(premise: the response fields `item` and `overview` above) **[Inferred]**", "T98", "state the premise")
    d.rep("SD4 R6", "• The limits table is headed as covering",
          "• The limits table is headed as covering \"inspecting and de-identifying content sent directly to the DLP API\" and does not name re-identification; the same limits probably also apply to `content.reidentify` (premise: re-identification is a content method with the same request shape) **[Inferred]**",
          "T98", "state the premise")
    d.ins_after("SD4 R6", "• Key location: the Cloud KMS key must be in global", [
        '• Cloud KMS: "Rotating keys creates new active key versions, but doesn\'t re-encrypt your data and doesn\'t disable or delete previous key versions." (Cloud KMS docs, not SDP docs, key rotation page, read 2026-10-09) **[Documented]**',
        '• Cloud KMS: "After a key is destroyed, data that was encrypted with the key version can\'t be decrypted." (Cloud KMS docs, not SDP docs, destroy and restore page, read 2026-10-09) **[Documented]**',
        "• Destroying the key version that wrapped the data key would stop re-identification, while rotation alone would not (premise: the wrapped key is a data encryption key encrypted by a Cloud KMS key, per the wrapped-key page and the REST CryptoKey schema, and the quickstart warns that destroying a key version stops decryption) **[Inferred]**",
        "• A Singapore key and the Singapore endpoint satisfy the placement rule (premise: the rule asks for the key in global or in the request region, and Cloud KMS and SDP both list asia-southeast1) **[Inferred]**",
    ], "T62, T63", "KMS key-version facts (Cloud KMS docs, not SDP docs) and the Singapore key placement")
    d.rep("SD4 R6", "• Because the SLA names only inspect and deidentify requests",
          [
              "• No uptime objective for `content.reidentify` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**",
              "• The SDP audit-logging page lists InspectContent, DeidentifyContent, ReidentifyContent and RedactImage with audit log type \"Data access\" (SDP docs, audit-logging page, read 2026-10-09) **[Documented]**",
              '• The Cloud Logging audit log reference says the request field "should never include user-generated data, such as file contents" (Cloud Logging docs, not SDP docs, read 2026-10-09) **[Documented]**',
              "• Content strings, tokens and wrapped keys are therefore not expected in audit entries (premise: that rule applies to SDP audit logs; the SDP page does not restate it) **[Inferred]**",
          ],
          "T22, T64", "SLA absence is [Not disclosed] naming the page (R020); audit-logging facts added")
    d.rep("SD4 R8", "• Effect of rotating or destroying a Cloud KMS key version",
          "• Effect of rotating or destroying a Cloud KMS key version on tokens already issued: the Cloud KMS pages say rotation does not disable earlier versions and destruction makes data encrypted with that version undecryptable, but no SDP page says how re-identification behaves (checked the quickstart, create-wrapped-key, pseudonymization and REST pages; needs testing)",
          "T62", "Cloud KMS facts folded into the open question")
    d.rep("SD4 R8", "• Which identity needs which Cloud KMS permission",
          "• Which identity needs a Cloud KMS decrypt or use permission at request time: the REST schema names `dlp.kms.encrypt` for the sender of the request, the quickstart grants the caller KMS Admin, CryptoKey Encrypter and DLP User, and no page says whether the DLP service agent or the caller unwraps the key (checked the quickstart, create-wrapped-key, roles, auth pages and the REST schemas)",
          "T63", "pages checked listed")
    d.rep("SD4 R8", "• Whether request bodies, tokens or wrapped keys appear in Cloud Audit Logs",
          "• Whether request bodies, tokens or wrapped keys appear in Cloud Audit Logs: the SDP page lists the content methods as Data Access audit methods and does not say what the entries contain (checked the audit-logging page; the general audit log reference says request fields should never include user-generated data; needs a look at a real log entry)",
          "T64", "audit-logging page now read")
    d.rep("SD4 R8", "• Whether tokenised output and the key reach any Google training",
          "• Whether tokenised output and the key reach any Google training or product-improvement use: the general Google Cloud terms limit processing to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)",
          "T92 (R019)", "terms pages read")
    d.rep("SD4 R8", "• Whether a Singapore-region KMS key can be used",
          "• Whether a key in `asia-southeast1` works end to end with the `asia-southeast1` regional endpoint (the wrapped-key page requires the key in global or the request region; test the Singapore pair)",
          "T63", "placement rule documented; the end-to-end test stays open")
    d.add_r9("SD4", [
        "https://docs.cloud.google.com/kms/docs/key-rotation",
        "https://docs.cloud.google.com/kms/docs/destroy-restore",
        "https://docs.cloud.google.com/kms/docs/locations",
        DOCS + "/audit-logging",
        "https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog",
        DOCS + "/reference/rest/v2/projects.deidentifyTemplates",
        DOCS + "/reference/rest/v2/ReidentifyContentResponse",
        DOCS + "/reference/rest/v2/DeidentifyContentResponse",
        DOCS + "/reference/rest/v2/InspectContentResponse",
    ] + TERMS, "T62, T63, T64, T17, T92", "R9: pages cited in the new bullets; terms pages named in R8")

    # ======================= SD5 =======================
    d.rep("SD5 R1", "Summary: ",
          "Summary: **Finds and blanks sensitive text and objects in images.** The service reads text in an image with OCR and also detects objects such as passports, photo ID cards, licence plates and faces (Preview). It returns boxes, or the image with opaque rectangles over matches. **[Documented]**",
          "T18", "face detector is in Preview", full=True)
    d.rep("SD5 R1", "• Image safety classification uses the same two methods",
          "• Image safety classification uses the same two methods and is covered by the image safety classification column (premise: the image context infoTypes are requested through the same inspect and redact calls) **[Inferred]**",
          "T98, style 4", "state the premise; header words replace the column id")
    d.rep("SD5 R2", "Summary: ",
          "Summary: **Sensitive text and ID-type objects in pictures.** Text infoTypes run on text read from the image, and object detectors cover faces (Preview), passports, photo ID cards, signatures, licence plates, barcodes and whiteboards. **[Documented]**",
          "T18", "face detector is in Preview", full=True)
    d.sub("SD5 R2", "• A Singapore NRIC printed in an image is therefore reachable by OCR",
          "this needs a test because no Singapore image example is given **[Inferred]**",
          "this needs a test because no Singapore image example is given (premise: text infoTypes run on text extracted from images and the NRIC infoType is a text infoType) **[Inferred]**",
          "T98", "state the premise")
    d.ins_after("SD5 R2", "• The face detector is not generally available:", [
        '• Preview features fall under the Pre-GA Offerings Terms, which exclude them from any SLA: "Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity." (Google Cloud Service Specific Terms, General Service Terms section 5, read 2026-10-09) **[Documented]**',
        "• The face detector's use therefore carries no SLA (premise: the detector is a Pre-GA Offering because the docs call it Preview) **[Inferred]**",
    ], "T73", "Pre-GA terms for the Preview detector (R019 allows terms pages; optional item)")
    d.rep("SD5 R2", "• Prompt injection or jailbreak text inside an image is not described",
          "• Out of purpose: prompt injection or jailbreak text inside an image is not named as something the service looks for (premise: the overview's purpose sentence and the image pages checked, which name only infoType detection and redaction) **[Inferred]**",
          "T19 (R015)", "one label pattern; the clause 'OCR text is matched only against the infoTypes requested' dropped (no quote)")
    d.sub("SD5 R3", "• None of these fields marks direction, role or prompt type", "with the caller supplying the bytes **[Inferred]**",
          "with the caller supplying the bytes (premise: the request body fields listed above) **[Inferred]**", "T98", "state the premise")
    d.sub("SD5 R3", "• No system prompt or conversation context is read", "the service sees the image and the configuration only **[Inferred]**",
          "the service sees the image and the configuration only (premise: the request fields above) **[Inferred]**", "T98", "state the premise")
    d.sub("SD5 R5", "• Setting `includeQuote` returns all recognised text", "so the response itself holds the sensitive text that redaction was meant to hide **[Inferred]**",
          "so the response itself holds the sensitive text that redaction was meant to hide (premise: the extractedText description above) **[Inferred]**", "T98", "state the premise")
    d.ins_after("SD5 R6", "• Format conflict, statement 6 (client enum, surface only)",
                '• The client docstring for the redact request repeats the REST wording: "The content must be PNG, JPEG, SVG or BMP." (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2705`) ' + REPO,
                "T66", "optional item: docstring repeats the REST wording (a labelled fact, not a seventh statement)")
    d.sub("SD5 R6", "• PNG, JPEG and BMP are the formats named by", "so tests should use PNG, JPEG and BMP first **[Inferred]**",
          "so tests should use PNG, JPEG and BMP first (premise: the REST reference, the redaction guide, the inspect guide and the client enum agree on these three) **[Inferred]**",
          "T98", "state the premise")
    d.rep("SD5 R6", "• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`",
          "• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`, so larger images need `image.redact` or a storage inspection job (premise: the 0.5 MB limit is listed for content sent directly to the API and image.redact has its own 4 MB entry) **[Inferred]**",
          "T98", "state the premise")
    d.ins_after("SD5 R6", "• Default detectors, statement 2:",
                '• For images, the redaction guide says "Default infoTypes don\'t include objects in images." (SDP docs, redacting sensitive data in images page, read 2026-10-09) **[Documented]**',
                "T42", "image-specific default statement added")
    d.rep("SD5 R6", "• The SLA covers only content.inspect and content.deidentify requests",
          [
              '• "Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests (Sensitive Data Protection SLA page, read 2026-10-09) **[Documented]**',
              "• No uptime objective for `image.redact` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**",
          ],
          "T22", "definition [Documented]; absence [Not disclosed] naming the page (R020)")
    d.rep("SD5 R8", "• Launch stage of image redaction by object infoType",
          '• Launch stage of the other object detectors and of the three image-context detectors: the reference marks only the face detector as Preview and the release notes say "available" without a stage (checked the reference and release notes of 2025-11-03, 2025-12-15, 2026-01-16 and 2026-06-08)',
          "T18", "pages and dates checked")
    d.rep("SD5 R8", "• Customer data terms for images sent to the API",
          "• Customer data terms for images sent to the API: the general Google Cloud terms limit processing of Customer Data to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)",
          "T92 (R019)", "terms pages read")
    d.add_r9("SD5", TERMS, "T92, T73", "R9: terms pages named in R2 and R8")

    # ======================= SD6 =======================
    d.rep("SD6 R2", "Summary: ",
          "Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a one-sentence definition, and the docs describe the use as content moderation. **[Documented]**",
          "T16", "the absence sentence ('Other harm categories are not listed') rested on a [Not disclosed] bullet", full=True)
    d.rep("SD6 R2", "• The text-side analogues are document-category infoTypes of the SD1 column", [
        '• The document-category infoTypes of the sensitive-data detection in text column include `DOCUMENT_TYPE/CONTEXT/SEXUAL` ("Content contains sex-related topics."), `DOCUMENT_TYPE/CONTEXT/OFFENSIVE` ("Content contains offensive topics.") and `DOCUMENT_TYPE/CONTEXT/OBSCENE` ("Content contains obscene topics.") (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**',
        "• These are the text-side analogues of the image categories (premise: the descriptions refer to topics in documents; whether they run on a plain string is open, see the detection column) **[Inferred]**",
    ], "hygiene (contradiction 9, style 4)", "'they classify text, not pixels' was stated as [Documented] while the detection column leaves open whether they run on a plain string; judgement split off as [Inferred]")
    d.rep("SD6 R2", "• Prompt injection, jailbreaks, toxicity in text and topic control are not part of this feature",
          "• Out of purpose: prompt injection, jailbreaks, toxicity in text and topic control are not named on the image concepts, inspect, redact and infoType reference pages (premise: the overview's purpose sentence) **[Inferred]**",
          "T19 (R015)", "one label pattern for the out-of-purpose statement")
    d.sub("SD6 R2", "• Languages: the classifier works on pixels", "• Languages: the classifier works on pixels, not on extracted text:",
          "• Input basis: the classifier works on pixels, not on extracted text:", "style 7", "the bullet is about pixels, not languages")
    d.rep("SD6 R3", "• The image methods have no direction, role or prompt-type field",
          "• The image methods have no direction, role or prompt-type field (SDP docs, REST projects.image.redact page, read 2026-10-09), so uploads, model-generated images, retrieved images and tool outputs go through the same call (premise: the request body fields in the REST page) **[Inferred]**",
          "style 6, T98", "doubled parentheses removed; premise stated")
    d.rep("SD6 R3", "• No system prompt or conversation context is read; the image and the configuration",
          "• No system prompt or conversation context is read; the image and the configuration are the only inputs (premise: the request fields listed above) **[Inferred]**",
          "T98", "state the premise")
    d.rep("SD6 R4", "Summary: ",
          "Summary: **A classifier over the whole image.** Image context detectors run an image content classification mode that assigns one theme or category. The models are described as trained mainly on real-world images. Rules can use the findings from June 2026. **[Documented]**",
          "T16", "'with unnamed models' rested on a [Not disclosed] bullet", full=True)
    d.rep("SD6 R5", "Summary: ",
          "Summary: **A rated finding for the image, or a fully blanked image.** The docs say classification produces a label, and give a likelihood bucket per finding rather than a number. **[Documented]**",
          "T16", "'They show no worked example' rested on a [Not disclosed] bullet", full=True)
    d.sub("SD6 R5", "• Each category is its own infoType, so one image can in principle produce one finding per category",
          "one finding per category **[Inferred]**", "one finding per category (premise: each category is a separate infoType and a finding carries one infoType) **[Inferred]**",
          "T98", "state the premise")
    d.rep("SD6 R5", "• No allow or block field exists in the redact response", [
        "• In the client, `RedactImageResponse` has the fields `redacted_image`, `extracted_text` and `inspect_result` and no allow or block field (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2845` class RedactImageResponse) " + REPO,
        "• The caller therefore maps findings to a decision (premise: the response holds only the image, the text and the findings) **[Inferred]**",
    ], "hygiene", "inference ('so the caller maps findings to a decision') split from the repo-labelled fact")
    d.sub("SD6 R6", "• Input handling uses the same methods and body as", "so those rules and that conflict carry over **[Inferred]**",
          "so those rules and that conflict carry over (premise: both columns call the same image methods with the same request body) **[Inferred]**", "T98", "state the premise")
    d.rep("SD6 R6", "• Whether a request with no infoTypes also runs image context detectors", [
        '• For images, the redaction guide says "Default infoTypes don\'t include objects in images." (SDP docs, redacting sensitive data in images page, read 2026-10-09) **[Documented]**',
        "• Whether a request with no infoTypes also runs image context detectors is not stated; the quoted sentence is about objects and is silent on image context infoTypes (checked the redact, inspect and REST pages) **[Not disclosed]**",
    ], "T42", "the quote is its own [Documented] bullet; the open point stays [Not disclosed]")
    d.sub("SD6 R6", "• Launch stage of the three detectors (general availability or Preview)", "(checked the infoType reference and release notes)",
          "(checked the infoType reference, which marks only the face detector, and the release notes of 2026-01-16)", "T73", "pages checked named")
    d.ins_after("SD6 R7", "• **Minimum setup:**", [
        "• Terms for the bench: the Service Specific Terms let the customer run benchmark tests itself and publish results only with all information needed to replicate them and a reciprocal right for Google (Google Cloud Service Specific Terms, General Service Terms section 7, read 2026-10-09) **[Documented]**",
        "• Test images must not be illegal content or non-consensual explicit imagery under the Acceptable Use Policy (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**",
    ], "T93 (R019)", "terms for the bench (main accepted the resolver's text for SD6 R7 and R8)")
    d.rep("SD6 R8", "• Customer data terms for images sent to the API",
          "• Customer data terms for images sent to the API: the general Google Cloud terms limit processing of Customer Data to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms). Acceptable-use limits for explicit or violent test images: the Google Cloud Acceptable Use Policy bars illegal content including child sexual exploitation and non-consensual explicit imagery and does not mention other explicit or violent test images; which test images are acceptable is decided in the bench design",
          "T92, T93 (R019)", "terms pages read; acceptable test data deferred to bench design")
    d.sub("SD6 R8", "• How the image format conflict recorded in the SD5 column", "the SD5 column", "the image detection and redaction column", "style 4",
          "header words replace the column id")
    d.add_r9("SD6", [DOCS + "/reference/rest/v2/InspectResult", "https://cloud.google.com/terms/aup"] + TERMS, "T86, T92, T93",
             "R9: InspectResult page cited in R5 but missing; terms and AUP pages cited in R7 and R8")

    # ======================= global phrase fixes (style 4) =======================
    d.gsub(r"the detection column", "the sensitive-data detection in text column", "style 4",
           "column ids are not visible on the sheet; header words replace 'the detection column'")
    d.gsub(r"the reversible-tokenisation column", "the reversible tokenisation and re-identification column", "style 4",
           "header words replace the column pointer")
    d.gsub(r"they are covered in the image columns", "they are covered in the image detection and redaction and the image safety classification columns", "style 4",
           "header words replace the column pointer")
    d.gsub(r"the SD1 and SD2 columns", "the sensitive-data detection in text and custom detector columns", "style 4", "header words replace the column ids")
    d.gsub(r"the SD5 column", "the image detection and redaction column", "style 4", "header words replace the column id")
    d.gsub(r"the SD6 column", "the image safety classification column", "style 4", "header words replace the column id")
    d.gsub(r"the SD3 column", "the masking and de-identification in text column", "style 4", "header words replace the column id")

    # ======================= code citation form (T97) =======================
    d.gsub(r"packages/google-cloud-dlp/(google/cloud/dlp/gapic_version\.py@|README\.rst@|setup\.py@)", r"\1", "T97",
           "A: package-root-relative citation form (drop the packages/google-cloud-dlp/ prefix)")
    d.gsub(r"(?<![/\w])dlp_v2/", "google/cloud/dlp_v2/", "T97", "B: package-root-relative citation form (add google/cloud/)")
    d.gsub(r"(?<![/\w])dlp/gapic_version\.py@", "google/cloud/dlp/gapic_version.py@", "T97", "B: package-root-relative citation form (add google/cloud/)")
