"""Column edits for MA5, MA6, MA9, MA10 (cols_b)."""
from lib import rep, edit, ins_after, ins_before, dele, setsum, editsum, r9add, r9sum, OPS

D = " **[Documented]**"
I = " **[Inferred]**"
ND = " **[Not disclosed]**"
TBV = " **[To be verified]**"
GO = " **[Documented: repo googleapis/google-cloud-go@modelarmor/v1.3.0]**"
AS = " **[Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00]**"

URL_APG_RN = "https://docs.cloud.google.com/apigee/docs/release-notes"
URL_SDPI = "https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference"
URL_SDPM = "https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels"
URL_SDPR = "https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images"
URL_FS = "https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting"
URL_AS = "https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml"
URL_GST = "https://cloud.google.com/terms/service-terms"
URL_AUP = "https://cloud.google.com/terms/aup"
URL_PRODUCTS = "https://cloud.google.com/products"

NAMING = ('• Naming: the docs call the Vertex AI route "Gemini Enterprise Agent Platform" (short form Agent Platform below); '
          'they still say "Gemini API in Vertex AI" for the generateContent method and use VERTEX_AI in gcloud flags, and list '
          '"Gemini Enterprise" as a separate integration (integrations page, Agent Platform integration page, 2026-10-09)' + D)
APIGEE_GA = ('• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse`: Public Preview on 2025-05-22 and Generally Available on 2025-09-04 on Apigee X '
             '(Apigee release notes, Apigee docs not Model Armor docs, 2026-10-09)' + D)
LOG_OV = '• The overview says that with Cloud Logging enabled, event details "might include metadata or snippets of the analyzed content as configured" (overview, 2026-10-09)' + D
OVERLIMIT_SDP = ('• Over the 130,000-token limit a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with '
                 '"Detection skipped as token limit exceeded." (quotas page, 2026-10-09)' + D)
APIGEE_LIMIT = ('• Apigee route: "Model Armor has token limits for processing prompts and responses, which vary by filter. Content exceeding these limits might not be fully scanned." '
                '(Apigee integration page, 2026-10-09)' + D)
OTHER_ROUTES = ('• Whether the token limits apply on the Agent Platform, Agent Gateway (non-streaming), Service Extensions and MCP routes is not stated '
                '(checked the quotas page and the five integration pages)' + ND)
FILTERRESULTS = lambda: [
    '• The sanitize page shows `filterResults` as a keyed object in six of its eight example responses and as an array of single-key objects in the two Sensitive Data Protection prompt examples (basic and advanced) (sanitize page, 2026-10-09)' + D,
    '• The pinned Go library types the field as `map[string]*FilterResult` and describes it as "Results for all filters where the key is the filter name" (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:2559)' + GO,
    '• The REST reference and the pinned Go type agree on a keyed map, so the two array examples are probably an older or abbreviated sample format; the live shape is untested. Premise: code at the pinned tag outranks page examples' + I,
]
NRIC = lambda mid: [
    '• Singapore (asia-southeast1) lists Sensitive Data Protection as supported, but basic mode names only US national identifiers (feature availability page, overview and sanitize page, 2026-10-09)' + D,
    '• Singapore NRIC is a built-in Sensitive Data Protection infoType: SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER, "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card.", available in any location (Sensitive Data Protection infoTypes reference, 2026-10-09)' + D,
    f'• A Singapore NRIC test{mid} therefore needs an advanced template whose inspect template lists that built-in infoType; no custom detector is needed. Premise: an inspect template holds "what predefined or custom detectors to use" (templates page)' + I,
]
PRE_GA = lambda: [
    '• Preview features are Pre-GA Offerings: "PRE-GA OFFERINGS ARE PROVIDED “AS IS” WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND." (Google Cloud General Service Terms, Pre-GA Offerings Terms, 2026-10-09)' + D,
    '• Unless Google\'s documentation says otherwise, "no data processing terms (including the Cloud Data Processing Addendum) apply to Pre-GA Offerings and Customer should not use Pre-GA Offerings to process personal data or other data subject to legal or regulatory compliance requirements" (Google Cloud General Service Terms, 2026-10-09)' + D,
    '• Google\'s launch-stage description says "Unless stated otherwise by Google, Preview offerings are intended for use in test environments only." (Google Cloud products page, 2026-10-09)' + D,
]


def apply(C):
    # =================================================================== MA5
    rep(C, "MA5", 1, "Sensitive Data Protection is a separate Google Cloud service that Model Armor calls", [
        '• The overview links to the Sensitive Data Protection infoTypes reference, match likelihood and overview pages (overview page links, 2026-10-09)' + D,
        '• Sensitive Data Protection is a separate Google Cloud service that Model Armor calls; its infoType catalogue, transformation types and likelihood meaning are covered in the Sensitive Data Protection columns on sheet 3, so this column covers only how Model Armor invokes it. The premise is that the overview links out for these topics (previous bullet)' + I,
    ], "T56")
    rep(C, "MA5", 2, "Source conflict: the overview and the REST reference say six items", [
        '• Source conflict: the overview and the REST reference say six items, the sanitize page lists seven (it adds PASSWORD) (overview, REST reference, sanitize page, 2026-10-09)' + D,
        '• A Go client comment on the basic configuration also says "a fixed set of six info-types" (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:2160)' + GO,
        '• Which count is current: no page reconciles them and no release note mentions PASSWORD (checked the overview, REST reference, sanitize page and release notes)' + ND,
    ], "T41 + hygiene (absence clause inside a [Documented] bullet)")
    ins_after(C, "MA5", 2, "Which locations count as",
              '• "US-based regions" is probably the set of locations whose jurisdiction is the United States (the us multi-region, us-central1, us-east1, us-east4, us-west1); the premise is the jurisdiction column of the data residency page' + I, "T43")
    editsum(C, "MA5", 3, " Documented examples exist for the prompt side only.", "", "style 2 (absence in a [Documented] Summary; irrelevant to an input-level column)")
    editsum(C, "MA5", 4, "**[Documented]**", "**[Not disclosed]**", "style 1 + 2 (Summary states an absence: weakest label wins)")
    edit(C, "MA5", 4, "Apigee route:", "; the pages read do not state GA or Preview", "", "T20 (open question closed)")
    ins_after(C, "MA5", 4, "Apigee route:", APIGEE_GA, "T20")
    rep(C, "MA5", 4, "Whether Agent Gateway or Service Extensions forward de-identified input text", [
        '• Agent Gateway page: a template can "block and redact content that violates policies", yet its flow text says the gateway "either allows or blocks it based on the verdict"; the networking page says Model Armor instructs the service to "allow, block, or modify" traffic (Agent Gateway and networking pages, 2026-10-09)' + D,
        '• Whether Agent Gateway or Service Extensions forward the de-identified text rather than only blocking (checked the Agent Gateway, networking and integrations pages)' + ND,
    ], "T26")
    ins_after(C, "MA5", 4, "Logging caveat:", LOG_OV, "T79")
    ins_before(C, "MA5", 4, "Gemini Enterprise Agent Platform route", NAMING, "T84")
    rep(C, "MA5", 5, "Execution problems: if text exceeds the token limit", OVERLIMIT_SDP, "T52 (CORRECTION)")
    rep(C, "MA5", 5, "Source conflict on shape: the REST reference says", FILTERRESULTS(), "T47")
    dele(C, "MA5", 5, "Source conflict on shape: the basic and advanced sections", "T47 (replaced by the three bullets above)")
    editsum(C, "MA5", 5, " There is no numeric score and no published accuracy figure.", "", "style 2 (absence in a [Documented] Summary; both gaps stay in Detail and R8)")
    setsum(C, "MA5", 6,
           "**Template, location and a per-mode setting.** Basic mode needs one switch; advanced mode needs inspect and optional de-identify templates in the same location. Cross-project use needs two Sensitive Data Protection roles. Past 130,000 tokens a match still counts; no match gives a skipped check. **[Documented]**",
           "T52 (CORRECTION: 'Text over 130,000 tokens is skipped' was wrong)")
    ins_after(C, "MA5", 6, "Token limit: the table gives 130,000", [APIGEE_LIMIT, OTHER_ROUTES], "T53")
    rep(C, "MA5", 6, "Real-time streaming mode \"supports unlimited tokens\"", [
        '• In real-time streaming mode Model Armor "supports unlimited tokens"; buffered streaming mode keeps the token limits (quotas page, sanitize page, 2026-10-09)' + D,
        '• For streamed content, "make sure that individual chunks don\'t exceed the token limits" (sanitize page, 2026-10-09)' + D,
        '• Streaming methods do not support Sensitive Data Protection de-identification (sanitize page, 2026-10-09)' + D,
    ], "T54")
    ins_after(C, "MA5", 6, "\"Floor settings don't check templates for Sensitive Data Protection conformance.\"", [
        '• A floor setting\'s `filterConfig` is the same `FilterConfig` type as a template\'s, which includes `sdpSettings.advancedConfig` (FloorSetting and templates REST references, 2026-10-09)' + D,
        '• The pinned Go `FloorSetting` has `FilterConfig *FilterConfig` (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:1129)' + GO,
        '• A floor setting can therefore carry an advanced inspect template. Premise: the shared FilterConfig type; no page shows an example, and the only floor-setting example uses basic mode' + I,
        '• Which location the inspect template must be in for a floor setting stored at `locations/global` is not stated (checked the floor settings, sanitize and Agent Platform pages and both REST references)' + ND,
    ], "T50")
    rep(C, "MA5", 7, "Singapore (asia-southeast1) lists Sensitive Data Protection as supported, but basic mode", NRIC(""), "T55 (CORRECTION: built-in infoType exists; no custom detector needed)")
    edit(C, "MA5", 8, "Whether the de-identified text is returned when enforcement is Inspect only", "(needs testing; checked the overview and templates page, not stated)",
         "(needs testing; checked the overview, templates page, REST references, sanitize page and the Agent Platform and Gemini Enterprise pages, not stated)", "T49")
    rep(C, "MA5", 8, "Whether floor settings accept an advanced inspect template",
        "• Which location an advanced inspect template must have when it is used from a floor setting at locations/global (checked the floor settings page, Agent Platform page and REST references, not stated; needs testing)", "T50")
    rep(C, "MA5", 8, "What the sanitize page examples mean by a bare array",
        "• Whether a live call returns `filterResults` as the keyed map in the REST reference and the Go library or as the array in two sample responses (needs one test call)", "T47")
    rep(C, "MA5", 8, "Whether the 130,000-token Sensitive Data Protection limit applies",
        "• Whether the 130,000-token limit applies on the Agent Platform, Agent Gateway, Service Extensions and MCP routes (Gemini Enterprise is exempt and Apigee is limited per the integration pages; the others are not stated)", "T53")
    r9add(C, "MA5", [URL_FS, URL_SDPI, URL_APG_RN], "T50 / T55 / T20")
    r9sum(C, "MA5", "Model Armor docs (overview, templates, sanitize, quotas, integrations, floor settings, filter versions, logging, release notes, REST references), the product and pricing pages, the Apigee release notes, the Sensitive Data Protection infoTypes reference, and the pinned Google Go client library.")

    # =================================================================== MA6
    rep(C, "MA6", 1, "Sensitive Data Protection is a separate Google Cloud service; its infoType catalogue", [
        '• The overview links to the Sensitive Data Protection infoTypes reference, match likelihood and overview pages (overview page links, 2026-10-09)' + D,
        '• Sensitive Data Protection is a separate Google Cloud service; its infoType catalogue, transformations and likelihood meaning are covered in the Sensitive Data Protection columns on sheet 3, and this column covers only how Model Armor invokes it on responses. The premise is that the overview links out for these topics (previous bullet)' + I,
    ], "T56")
    setsum(C, "MA6", 2,
           "**Sensitive items a model might output.** The documented basic lists are written for prompts: a short, US-leaning fixed list. Advanced mode uses the customer's template. Google's pages do not say whether the basic list also applies to responses. **[Not disclosed]**",
           "T44 (Summary; label to Not disclosed: it states an absence)")
    rep(C, "MA6", 2, "Source conflict: six items (overview, REST reference) against seven", [
        '• Source conflict: the overview and the REST reference say six items, the sanitize page lists seven (it adds PASSWORD) (overview, REST reference, sanitize page, 2026-10-09)' + D,
        '• A Go client comment on the basic configuration also says "a fixed set of six info-types" (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:2160)' + GO,
        '• Which count is current: no page reconciles them and no release note mentions PASSWORD (checked the overview, REST reference, sanitize page and release notes)' + ND,
    ], "T41 + hygiene")
    ins_after(C, "MA6", 2, "The sanitize page introduces the basic infoType lists as", [
        '• Advanced mode on responses: "Model Armor screens the LLM prompts and responses using the advanced Sensitive Data Protection configuration setting." (sanitize page, 2026-10-09)' + D,
        '• Template note: "Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding." (templates page, 2026-10-09)' + D,
        '• Google\'s Apigee sample checks the response-side result: its shared flow tests SanitizeModelResponse.SMR-Sanitize-Model-Response.sdpFilterResult.inspectResult.matchState for MATCH_FOUND (llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml:44)' + AS,
        '• Basic mode probably scans responses with the same list as prompts. Premise: the basic or advanced setting sits once in the template filter config, which has no direction field and is used by both sanitize methods (templates reference, 2026-10-09)' + I,
    ], "T44")
    setsum(C, "MA6", 3,
           "**The model response, sent in its own field.** The text goes to the regional response-sanitising method, with an optional field for the matching user prompt. Google shows no worked response-side de-identification example. **[Not disclosed]**",
           "T45 (Summary; label to Not disclosed)")
    ins_after(C, "MA6", 3, "A response-side result with `deidentifyResult` is not shown",
              '• The templates page says the de-identified "prompts or responses" are returned in `deidentifyResult.data.text`, so response-side de-identified text is documented in prose but not by example (templates page, 2026-10-09)' + D, "T45")
    ins_after(C, "MA6", 3, "Streaming: `StreamSanitizeModelResponse` streams LLM text",
              '• For streamed content, "make sure that individual chunks don\'t exceed the token limits" (sanitize page, 2026-10-09)' + D, "T54")
    edit(C, "MA6", 4, "Apigee route:", "; GA or Preview is not stated", "", "T20 (open question closed)")
    ins_after(C, "MA6", 4, "Apigee route:", APIGEE_GA, "T20")
    ins_after(C, "MA6", 4, "Service Extensions route (GKE integration GA",
              '• Whether Agent Gateway or Service Extensions forward the de-identified response text rather than only blocking (checked the Agent Gateway, networking and integrations pages)' + ND, "T26")
    ins_after(C, "MA6", 4, "Logging caveat:", LOG_OV, "T79")
    ins_before(C, "MA6", 4, "Gemini Enterprise Agent Platform route", NAMING, "T84")
    rep(C, "MA6", 5, "Over-limit text returns EXECUTION_SKIPPED", OVERLIMIT_SDP, "T52 (CORRECTION)")
    rep(C, "MA6", 5, "Source conflict on shape: the REST reference describes", FILTERRESULTS(), "T47")
    editsum(C, "MA6", 5, " No numeric score or accuracy figure is published.", "", "style 2 (absence in a [Documented] Summary; stays in Detail and R8)")
    setsum(C, "MA6", 6,
           "**Template, location and the response text.** Template settings, roles and the location rule are as for prompts; the response goes in its own field. Past 130,000 tokens a match still counts; no match gives a skipped check. Cross-project use needs two Sensitive Data Protection roles. **[Documented]**",
           "T52 (CORRECTION)")
    ins_after(C, "MA6", 6, "Token limit: 130,000 for Sensitive Data Protection", [APIGEE_LIMIT, OTHER_ROUTES], "T53")
    rep(C, "MA6", 7, "Singapore (asia-southeast1) lists Sensitive Data Protection as supported; the basic list", NRIC(" on model output"), "T55 (CORRECTION)")
    # NRIC() puts the tail before the label already; tidy the last bullet's wording for the response column
    rep(C, "MA6", 8, "Whether the basic infoType list is the same for responses",
        "• Whether the basic infoType list is the same for responses as for prompts (checked the sanitize page, overview, templates page, REST references and the Apigee policy page; the lists say \"scanned in the prompt\"; needs testing)", "T44")
    rep(C, "MA6", 8, "A real response-side `deidentifyResult` and findings",
        "• A real response-side `deidentifyResult` and findings (needs testing; the templates page names the field but the sanitize page has no response example)", "T45")
    dele(C, "MA6", 8, "Whether the Apigee integration is GA or Preview", "T20 (answered: Apigee policies are GA)")
    edit(C, "MA6", 8, "Whether de-identification is applied when enforcement is Inspect only", "(needs testing)",
         "(needs testing; checked the overview, templates page, REST references, sanitize page and the Agent Platform and Gemini Enterprise pages, not stated)", "T49")
    r9add(C, "MA6", [URL_AS, URL_SDPI, URL_APG_RN], "T44 / T55 / T20")
    r9sum(C, "MA6", "Model Armor docs (overview, templates, sanitize, REST references, quotas, integrations, floor settings, logging, release notes), the product and pricing pages, Apigee docs and sample, the Sensitive Data Protection infoTypes reference, and the pinned Google Go client library.")

    # =================================================================== MA9
    rep(C, "MA9", 1, "Antivirus scanning is covered only in the inventory sheet",
        '• Antivirus scanning is covered only in the inventory sheet, not as a Table 3 column; no configuration for it (a template setting, enable flag or threshold) appears in the templates reference, the FilterConfig in the Go v1 library, the floor settings page, the templates page, the overview, the sanitize page or the Security Command Center findings page (checked all)' + ND,
        "T57 (label To be verified -> Not disclosed)")
    ins_after(C, "MA9", 2, "The REST enum description for Excel reads", [
        '• The pinned Go library repeats "XLSX, XLSM, XLTX, XLYM" in its comment for the Excel byte item type (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:783)' + GO,
        '• XLYM is probably a typo for XLTM. Premise: the overview and the release note both say XLTM and the REST text and the Go comment appear to share one source comment' + I,
    ], "T67")
    rep(C, "MA9", 2, "Rich documents with metadata labels: release note 2026-04-06", [
        '• Rich documents with metadata labels: release note 2026-04-06 says Model Armor "can sanitize data passed in as rich documents that have specific metadata labels" (release notes, 2026-10-09)' + D,
        '• It needs a custom metadata-label infoType in an advanced Sensitive Data Protection configuration of the Model Armor template; detected labels are Google Drive labels and Microsoft sensitivity labels on DOCX, PDF, PPTX and XLSX (Sensitive Data Protection custom metadata label page, 2026-10-09)' + D,
        '• Custom metadata label detectors are not supported in inspection rule sets or de-identification transformations (Sensitive Data Protection custom metadata label page, 2026-10-09)' + D,
        '• A Model Armor request field for client-provided metadata is not documented (checked the DataItem, sanitizeUserPrompt and sanitizeModelResponse references and the sanitize page)' + ND,
    ], "T66")
    ins_after(C, "MA9", 2, "Source conflict on embedded images (3)", [
        '• No page reconciles the three statements on embedded images (checked the overview, integrations page, Gemini Enterprise page, release notes 2025-09-16 and 2026-06-25, and the sanitize page)' + ND,
        '• The pinned Go comment for the finding container says nested names "could be absent if the embedded object has no string identifier (for example, an image contained within a document)", so the result schema allows an embedded-image container (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:3433)' + GO,
    ], "T58")
    setsum(C, "MA9", 3,
           "**A base64 file in the prompt field.** The file goes in a data item with its file type set by hand. The schema lets a response carry a file too, but the docs show no response-side example. The template modality must include text. **[Not disclosed]**",
           "style 2 + 5 (absence in a [Documented] Summary; code term 'byte item' removed)")
    ins_before(C, "MA9", 3, "Agent Platform and Agent Gateway pages both say", NAMING, "T84")
    setsum(C, "MA9", 4,
           "**Text extraction, then the ordinary filters.** Gemini Enterprise discards a violating file whole. The extractor and its handling of scans and layout are not described. **[Not disclosed]**",
           "style 1 + 2 + 3g (Summary stated 'Extraction runs inside the managed service' with no Detail bullet; absence in a [Documented] Summary)")
    editsum(C, "MA9", 5, " No score or accuracy figure is published.", "", "style 2 (absence in a [Documented] Summary)")
    rep(C, "MA9", 5, "Which response field returns the file label is not shown", [
        '• The file label is probably returned as that container name. Premise: both fields are described as identifying the file; no page names the response field' + I,
        '• The pinned Go v1 `ByteDataItem` has only `ByteDataType` and `ByteData`, no file label (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:3222)' + GO,
    ], "T68 (the container-name quote is already the 'Finding containers' bullet above, so it is not repeated)")
    rep(C, "MA9", 5, "Token overflow in extracted text", '• Token overflow in extracted text: a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, 2026-10-09)' + D, "T52 (CORRECTION)")
    editsum(C, "MA9", 6, "The byte data type must be set;", "The file type must be set;", "style 5 (code term in Summary)")
    ins_after(C, "MA9", 6, "The template's `modalities` field is optional", [
        '• The enum value MODALITY_UNSPECIFIED is described as "Unspecified modality. If specified, all modalities will be sanitized." (templates reference, 2026-10-09)' + D,
        '• Listing MODALITY_UNSPECIFIED explicitly would scan all modalities, while omitting the field scans text only. Premise: the two REST descriptions; no example shows it' + I,
    ], "T76")
    rep(C, "MA9", 8, "Whether the rich-document metadata-label feature needs special request fields",
        "• Whether the rich-document metadata-label feature works through the direct REST API as well as Gemini Enterprise (needs testing)", "T66")
    rep(C, "MA9", 8, "Whether filters report which page or sheet matched",
        "• Whether filters report which page or sheet matched (checked the SanitizationResult reference and the Go comments; only a container name and text ranges are described)", "T68")
    edit(C, "MA9", 8, "Antivirus: configuration, supported file types beyond PDF", "(checked the REST references, overview, manage-templates and release notes;",
         "(checked the REST references, overview, manage-templates, floor settings, sanitize, quotas and integrations pages, the Security Command Center findings page and release notes;", "T57 (checked list)")
    r9add(C, "MA9", [URL_SDPM], "T66")
    r9sum(C, "MA9", "Model Armor docs (overview, sanitize, templates, quotas, integrations, release notes, REST references, data residency, feature availability), the product and pricing pages, the blog, a Sensitive Data Protection page, and the pinned Google Go client library.")

    # =================================================================== MA10
    rep(C, "MA10", 1, "Sensitive Data Protection is a separate Google Cloud service; what its image detectors", [
        '• The overview links to the Sensitive Data Protection infoTypes reference, match likelihood and overview pages (overview page links, 2026-10-09)' + D,
        '• Sensitive Data Protection is a separate Google Cloud service; what its image detectors and redaction transformations can do is covered in the Sensitive Data Protection columns on sheet 3 for images, and this column covers how Model Armor invokes them. The premise is that the overview links out for these topics (previous bullet)' + I,
    ], "T56")
    ins_after(C, "MA10", 2, "Source conflict on embedded images (1)",
              '• Source conflict on embedded images (2): the integrations page says "images embedded in documents aren\'t screened" for the Gemini Enterprise integration (integrations page, 2026-10-09)' + D,
              "T58 (third source; the Gemini Enterprise bullet below is renumbered (3), as in MA9)")
    edit(C, "MA10", 2, "Source conflict on embedded images (2): the Gemini Enterprise page", "Source conflict on embedded images (2)", "Source conflict on embedded images (3)", "T58 (renumber)")
    ins_after(C, "MA10", 2, "Source conflict on embedded images (3)",
              '• No page reconciles the three statements on embedded images (checked the overview, integrations page, Gemini Enterprise page, release notes 2025-09-16 and 2026-06-25, and the sanitize page)' + ND, "T58")
    setsum(C, "MA10", 3,
           "**One base64 image in the prompt field.** The image goes in a data item of image type, in a template with image modality, at a us or eu endpoint. Docs say responses are screened too but show no response example. Text-plus-image requests are unsupported. **[Not disclosed]**",
           "style 2 + 5 (absence in a [Documented] Summary; enum value 'IMAGE' removed)")
    ins_after(C, "MA10", 3, "Integrations, source conflict (2)",
              '• No page reconciles the two lists (checked the integrations page, the Gemini Enterprise page and release notes 2025-09-16 and 2026-06-25)' + ND, "T60")
    ins_before(C, "MA10", 3, "The Agent Platform page says", NAMING, "T84 (first mention of the route in this column is R3)")
    editsum(C, "MA10", 4, "**[Documented]**", "**[Not disclosed]**", "style 1 + 2 (Summary states 'The OCR engine is not disclosed')")
    ins_after(C, "MA10", 4, "Self-hosted or offline image screening is not described", PRE_GA(), "T85")
    editsum(C, "MA10", 5, " No score or accuracy figure is published.", "", "style 2 (absence in a [Documented] Summary)")
    ins_after(C, "MA10", 5, "The generated Go library carries the same comment on the redact result findings", [
        '• In the Sensitive Data Protection API, `includeFindings` is a field of the image redact request ("Whether the response should include findings along with the redacted image."), not of an inspect or de-identify template (Sensitive Data Protection API discovery document, 2026-10-09)' + D,
        '• Where Model Armor sets `include_findings`, and whether a template setting controls it, is not stated (checked the templates reference, templates page, sanitize page and floor settings page)' + ND,
    ], "T71")
    rep(C, "MA10", 5, "Source conflict on box shape (2)", [
        '• The pinned Go library types `BoundingBoxes` as a list of boxes with `Top`, `Left`, `Width` and `Height` (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:3376)' + GO,
        '• Source conflict on box shape (2): the sanitize page redaction example shows a single `boundingBox` object (top 16, left 121, width 620, height 90) (sanitize page, 2026-10-09)' + D,
        '• The example is probably abbreviated or from an older format. Premise: the REST reference and the pinned Go type both give a list' + I,
    ], "T70")
    editsum(C, "MA10", 6, "The type must be IMAGE and the format", "The data type must be image and the format", "style 5 (code term in Summary)")
    ins_after(C, "MA10", 6, "Template field `modalities` (Preview)", [
        '• The enum value MODALITY_UNSPECIFIED is described as "Unspecified modality. If specified, all modalities will be sanitized." (templates reference, 2026-10-09)' + D,
        '• Listing MODALITY_UNSPECIFIED explicitly would scan all modalities, while omitting the field scans text only. Premise: the two REST descriptions; no example shows it' + I,
    ], "T76")
    ins_after(C, "MA10", 7, "Singapore (asia-southeast1) cannot be used for images",
              '• The General Service Terms commit to storing Customer Data at rest only in the selected region or multi-region and "do not limit the locations from which Customer or Customer End Users may access Customer Data" (Google Cloud General Service Terms, 2026-10-09)' + D, "T86")
    ins_after(C, "MA10", 7, "Response-side image tests are exploratory",
              '• Image tests should use synthetic images only, because the Pre-GA terms in R4 advise against processing personal data in Pre-GA Offerings' + I, "T85 (R7 only; the clauses themselves are in R4, not repeated)")
    aup = [
        '• Google\'s Acceptable Use Policy bars using the Services "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement" (Google Cloud Acceptable Use Policy, 2026-10-09)' + D,
        '• Whether sending jailbreak, injection or harmful-content prompts to measure detection rates is "expressly permitted" is not stated (checked the Acceptable Use Policy and the General Service Terms)' + ND,
    ]
    C["MA10"]["rows"][7]["detail"].extend(aup)
    OPS.append(dict(loc="MA10 R7", kind="insert", before="(none)", after=aup, reason="T86"))
    rep(C, "MA10", 8, "Whether `include_findings` in the Sensitive Data Protection template",
        "• Where include_findings is set when Model Armor calls Sensitive Data Protection (the Model Armor reference says \"in the SDP template\", but in the Sensitive Data Protection API it is an image redact request field; checked the Model Armor pages, not stated; needs testing)", "T71")
    rep(C, "MA10", 8, "Box field name:",
        "• Whether a live redaction response returns `boundingBoxes` as a list as the REST reference and Go library say (one sample shows a single `boundingBox`; needs testing)", "T70")
    edit(C, "MA10", 8, "Whether `redactedImage` is returned when enforcement is Inspect only", "(needs testing)",
         "(needs testing; checked the overview, templates page, REST references, sanitize page and the Agent Platform and Gemini Enterprise pages, not stated)", "T49")
    r8 = "• Whether the Acceptable Use Policy testing clause covers detection benchmarks (checked the Acceptable Use Policy and General Service Terms, not stated; needs the project owner's reading)"
    C["MA10"]["rows"][8]["detail"].append(r8)
    OPS.append(dict(loc="MA10 R8", kind="insert", before="(none)", after=[r8], reason="T86 (class c; user question open at CP2)"))
    r9add(C, "MA10", [URL_SDPR, URL_GST, URL_AUP, URL_PRODUCTS], "T71 / T85 / T86")
    r9sum(C, "MA10", "Model Armor docs (overview, sanitize, templates, quotas, integrations, release notes, REST references, feature availability), the pricing page, Google's Sensitive Data Protection, terms and products pages, and the pinned Google Go client library.")
