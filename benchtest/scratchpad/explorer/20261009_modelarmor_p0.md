# Model Armor P0 exploration (docs only; no vendor repo)

## 1. Header
- Product: Google Cloud Model Armor. Slug `modelarmor`. ID prefix `MA` (R009). Date read: 2026-10-09. Role: gr-explorer. Phase P0.
- Pin: none possible (no repo, no versioned docs). Docs pinned by date read; each page footer says "Last updated 2026-10-06 UTC" (release notes page: 2026-10-07 UTC). Labels: `[Documented]` = page read on 2026-10-09 via `fetch_text.py` (verbatim tag-stripped text). Short names: DOCS = https://docs.cloud.google.com/model-armor/ ; PROD = https://cloud.google.com/security/products/model-armor ; SCCP = https://cloud.google.com/security-command-center/pricing .
- Official domains used: docs.cloud.google.com/model-armor/*, cloud.google.com/security/products/model-armor, cloud.google.com/security-command-center/pricing, cloud.google.com/blog/products/identity-security/... (Google Cloud blog). Google GitHub repos: not readable (HTTP 403 via proxy), see Gaps.
- Ownership/redirect findings (seed correction): the seed URL `https://cloud.google.com/security-command-center/docs/model-armor-overview` returns 200 but its final URL is `https://docs.cloud.google.com/model-armor/overview` (redirect observed 2026-10-09; first hop is HTTP 301). Model Armor now has its own docs section (`/model-armor/...`), not under Security Command Center. Owner is Google Cloud throughout; no ownership change. `cloud.google.com/model-armor/docs` is 404. Docs host moved from cloud.google.com to docs.cloud.google.com; many old `cloud.google.com/...` paths redirect.
- Naming drift to record: Vertex AI is now called "Gemini Enterprise Agent Platform" in the Model Armor docs (the docs still say "Gemini API in Vertex AI" once).

## 2. Function list (PROPOSED Table 3 columns)
Direction (R002): Model Armor has separate per-direction API methods (`sanitizeUserPrompt` vs `sanitizeModelResponse`, plus streaming variants) and the docs advise separate input and output templates (S4, S8). It is a wrapper with per-direction flows, so each filter is split into Input-level and Output-level columns (R002 definition). The same filter set, thresholds and result schema serve both (S9), so the two columns will share most facts; difference is the request field (`userPromptData` vs `modelResponseData`) and the use case. Prefix proposed: `Model Armor:` (product's own name; "Google Cloud" is the vendor, per R009 not needed).

| Id | Exact header (proposed) | Function | Direction | Evidence |
|---|---|---|---|---|
| MA1 | `Model Armor: Input-level responsible AI safety filtering` | RAI filter on prompts: hate speech, harassment, sexually explicit, dangerous content (confidence LOW_AND_ABOVE / MEDIUM_AND_ABOVE / HIGH) plus always-on CSAM filter | Input | S1, S4, S6, S9, S15 |
| MA2 | `Model Armor: Output-level responsible AI safety filtering` | Same filters on model responses | Output | S1, S6, S9, S15 |
| MA3 | `Model Armor: Input-level prompt injection and jailbreak detection` | Detects attempts to override instructions or bypass safety in prompts; confidence level; min 3 words | Input | S1, S4, S5, S7, S12 |
| MA4 | `Model Armor: Output-level prompt injection and jailbreak detection` | Same filter on responses (and, via MCP integration, tool responses) | Output | S1, S7, S12, S19 |
| MA5 | `Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)` | SDP basic (fixed infoTypes) or advanced (inspect + optional de-identify templates) on prompts; image redaction | Input | S1, S3, S10, S11 |
| MA6 | `Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)` | Same on responses | Output | S1, S10, S11 |
| MA7 | `Model Armor: Input-level malicious URL detection` | Scans first 256 URLs in a prompt for malicious ones | Input | S1, S2, S3 |
| MA8 | `Model Armor: Output-level malicious URL detection` | Same on responses | Output | S1, S2 |
| MA9 | `Model Armor: Document and file screening` | Extracts text from PDF, CSV, TXT, Office files and runs the template filters; 4 MB limit | Both (a modality of MA1 to MA8) | S1, S2, S13 |
| MA10 | `Model Armor: Image screening (Preview)` | OCR text screening and (advanced SDP only) visual scanning of JPEG/PNG/BMP images; us and eu multi-regions only | Both | S1, S14 |

Candidates NOT proposed as firm columns (CP1 call, default = inventory):
- Antivirus scanning (`virusScanFilterResult`, PDF only): appears in the result schema, region tables and release notes (S16, S17) but no configuration page found; `[To be verified]`. Put in inventory block (a) until a config path is documented.
- Tool-call and tool-response screening for Google and Google Cloud MCP servers (GA; floor settings only; `tools/call`, `prompts/get`, tool execution errors) (S18). Data-path function per scope guide, but it re-uses MA3/MA4/MA5/MA6 filters and has no template. Default: inventory integration row plus Detail in MA4 and MA6; alternative: one extra column MA11 `Model Armor: Tool-call and tool-response screening (MCP)`.
- Streaming sanitisation (text; buffered or real-time), template-specific exclusion rules (Preview), multi-language detection, filter versions, floor settings, enforcement type, data residency, logging: configuration/variant facts -> Detail bullets and inventory, not columns.
- Prompt-leakage, off-topic, hallucination, refusal: checked overview, filters list, product page and REST FilterConfig; the schema has only raiSettings, sdpSettings, piAndJailbreakFilterSettings, maliciousUriFilterSettings: not offered `[Not disclosed]` (absence).
Merge options for CP1: (a) 10 columns as above; (b) 6 columns if main wants the R002 exception (not recommended: separate methods exist); (c) drop MA9/MA10 into Detail of MA1-MA8.

## 3. Proposed inventory blocks (sheet 3f; new config module `build_modelarmor_inventory.py`; row counts are proposals)
Short names: DOCS, PROD, SCCP as above.
- (a) Filters and detectors (about 9 rows): Responsible AI (4 categories), CSAM, Prompt injection and jailbreak, Malicious URL, Sensitive Data Protection basic, Sensitive Data Protection advanced, Antivirus (To be verified), Visual scanning. Columns: Filter | Config key (e.g. `raiSettings`) | Levels/options | Default | Applies to input/output | Result field | Limit | Covered by Table 3 column | Source URL.
- (b) Integration paths (about 10 rows): REST API (`modelarmor.LOCATION.rep.googleapis.com`), client libraries (C#, Go, Java, Node.js, PHP, Python), gcloud and Terraform, Gemini Enterprise Agent Platform (Vertex AI generateContent; floor settings or templates; GA), Agent Gateway (GA), Apigee policies, Gemini Enterprise (GA), Google and Google Cloud MCP servers (GA), Service Extensions on Cloud Load Balancing / GKE Inference Gateway / Secure Web Proxy, LangChain (Preview), Security Command Center findings. Columns: Path | Status (GA/Preview) | Modalities | Mode (inline/API) | Direction | Limitations | Covered by | Source URL.
- (c) Template and floor-setting parameters (about 14 rows): enforcementType, filterVersionSelector, multiLanguageDetection, modalities, dataResidencyCompliant, ignorePartialInvocationFailures, custom error codes/messages, logging flags, exclusion rules, floor-setting levels (org/folder/project), etc.
- (d) Locations and feature availability (about 20 rows, one per region): jurisdiction, data-residency states, supported filters, multi-language, CSAM, image, antivirus. Singapore (asia-southeast1) is limited-support (S20).
- (e) Quotas, limits and pricing (about 12 rows): 1200 QPM; ExternalProcessor 600 QPM; 65,536 tokens (SDP 130,000); 4 MB; 69 bytes minimum; 256 URLs; exclusion-rule limits; pricing tiers; filter version lifecycle (v1 to v4).
- (f) Optional: filter version history (v3, v4 with dates) - could fold into (c).

## 4. Sources (verbatim quotes; all read 2026-10-09)
S1 Overview. https://docs.cloud.google.com/model-armor/overview (seed URL redirects here; footer "Last updated 2026-10-06 UTC")
- "Model Armor is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses" `[Documented]` R1.
- "Model Armor filters both input (prompts) and output (responses) to prevent the LLM from exposure to or generation of malicious or sensitive content." `[Documented]` R3.
- "Whether you are deploying AI in Google Cloud or other cloud providers" `[Documented]` R3/R7.
- "Model Armor inspects each prompt and response independently as a single-turn request. It doesn't track conversation history or maintain context across multi-turn interactions." `[Documented]` R6.
- "Model Armor doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext." `[Documented]` R2.
- "Model Armor doesn't support audio or video." `[Documented]` R2.
- "Model Armor doesn't support prompts that combine text and images in a single request." `[Documented]` R6.

S2 Overview, filters (same URL).
- RAI: "Hate speech | Negative or harmful comments targeting identity and/or protected attributes." "Harassment | Threatening, intimidating, bullying, or abusive comments targeting another individual." "Sexually explicit | Contains references to sexual acts or other lewd content." "Dangerous content | Promotes or enables access to harmful goods, services, and activities." `[Documented]` R2.
- "CSAM | Contains references to child sexual abuse material (CSAM). This filter is applied by default and cannot be turned off." `[Documented]` R2.
- PI: "When prompt injection and jailbreak detection is enabled, Model Armor scans prompts and responses for malicious content. If detected, Model Armor blocks the prompt or response." `[Documented]` R3 (note "blocks" is the INSPECT_AND_BLOCK default; see S4).
- "if the word count is fewer than three words, Model Armor returns NO_MATCH_FOUND because such inputs lack enough information to constitute an attack." `[Documented]` R6.
- URL: "Model Armor extracts URLs until it reaches 256 URLs or the end of the payload, and scans only the first 256 URLs found in prompts and responses." `[Documented]` R6.
- Languages: "The responsible AI and prompt injection and jailbreak detection filters are tested on the following languages: Chinese (Mandarin) English French German Italian Japanese Korean Portuguese Spanish" ; "These filters can work in many other languages, but the quality of results might vary." ; "The Sensitive Data Protection filter supports English and other languages depending on the infoTypes that you selected." `[Documented]` R2.
- Confidence: "Note: You can set confidence levels only for prompt injection and jailbreak detection and responsible AI safety filters." `[Documented]` R5.
- Documents: "Supported files are limited to 4 MB in size. If a file exceeds this limit, Model Armor skips scanning the file." and "Model Armor rejects requests to scan files that are smaller than 69 bytes and returns an InvalidDocumentInputException error" ; formats "PDFs, CSV, Text files: TXT, Microsoft Word documents: DOCX, DOCM, DOTX, DOTM, ... PowerPoint ... Excel ..." `[Documented]` R6.
- Images: "Image screening Preview"; "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." "Optical character recognition (OCR): Screens the text within images." "Model Armor screens images only in the JPEG, PNG, and BMP formats." "Each image must be 4 MB or smaller." "Model Armor screens only a single image per request." "Image screening is supported only in the us and eu multi-regions." "Model Armor doesn't screen images embedded within files." `[Documented]` R2/R6.
- Data handling: "Model Armor operates as a stateless service, processing all prompts and model responses entirely in memory." ; "data in transit using TLS 1.2 and later" ; "FedRAMP High" appears in release notes (S21). `[Documented]` R7.
- Network: "To access Model Armor regional endpoints from within a VPC network, you must create a Private Service Connect endpoint" `[Documented]` R7.
- Best practice: "Decouple templates: Configure separate Model Armor templates for user prompts and model responses." `[Documented]` R3.
- Pricing pointer: "Model Armor can be purchased as a standalone service or as an integrated part of Security Command Center." `[Documented]` R7.

S3 Overview, SDP. same URL.
- "Basic configuration only supports inspection operations and doesn't support the use of Sensitive Data Protection templates." ; "Advanced configuration supports both inspection and de-identification operations." ; basic categories on overview: "Credit card number, US social security number (SSN), Financial account number, US individual taxpayer identification number (ITIN), Google Cloud credentials, Google Cloud API key". `[Documented]` R2/R4.
- "Model Armor can accept existing inspection templates, which function as blueprints" `[Documented]` R4. Cross-ref: SDP internals belong to the sdp explorer; do not duplicate.

S4 Templates. https://docs.cloud.google.com/model-armor/manage-templates (footer 2026-10-06)
- "The global endpoint (modelarmor.googleapis.com) doesn't support managing Model Armor templates or sanitizing prompts and responses." `[Documented]` R6/R7.
- Template metadata table: "enforcement_type | Enum | INSPECT_AND_BLOCK" (default) ; "INSPECT_ONLY: Model Armor inspects requests that violate the configured settings, but it doesn't block them." `[Documented]` R5.
- "log_sanitize_operations | Boolean | False" ; "multiLanguageDetection | Boolean | False" ; "data_residency_compliant | Boolean | True" ; "modalities (Preview) ... Leaving this field empty scans only text." `[Documented]` R6.
- "Prompt injection and jailbreak detection: ... We recommend that you set the confidence level to High to minimize false positives and ensure consistent detection behavior." `[Documented]` R5.
- "Advanced: A more configurable option that uses an inspection template defined in the Sensitive Data Protection service as a single source for sensitive data infoTypes." ; "If you specify Inspect template and De-identify template, Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding." `[Documented]` R4/R5.
- Template ID: "It cannot exceed 63 characters" ; "You cannot change the location later." `[Documented]` R7.
- Roles: "Model Armor Admin (roles/modelarmor.admin)". `[Documented]` R7.

S5 Overview confidence/best practice. same as S1: "Set prompt injection and jailbreak detection filters to Medium." (best-practice recommendation on overview) vs S4 "recommend ... High" -> conflict C1. `[Documented]` x2.

S6 Overview confidence levels: "High: Identifies content with a high likelihood of violation. Medium and above: ... Low and above: ..." `[Documented]` R5. REST ref: "LOW_AND_ABOVE | Highest chance of a false positive." "HIGH | Low chance of false positives." https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates `[Documented]`.

S7 Filter versions. https://docs.cloud.google.com/model-armor/set-filter-version and https://docs.cloud.google.com/model-armor/version-history
- "You configure a single filter version at the template level. You can't specify different versions for individual filters." ; "The filter version setting doesn't affect the Sensitive Data Protection and malicious URL filters." ; "Legacy: ... remains available for 90 days after a new Stable version is released." `[Documented]` R4.
- History: "v4 | 2026-09-18 | Minor updates have been made across prompt injection and jailbreak detection, and responsible AI filters to address reported false positives." ; "2026-05-25 | The prompt injection and jailbreak detection filter is updated and uses a new model" `[Documented]` R4 (version and recency only; model identity not stated, see Gaps).

S8 Sanitize methods. https://docs.cloud.google.com/model-armor/sanitize-prompts-responses (footer 2026-10-06)
- "Note: To sanitize prompts and responses, you must use regional endpoints." `[Documented]` R7.
- REST: `:sanitizeUserPrompt` with body `{"userPromptData":{"text":"TEST_PROMPT"}}`; `:sanitizeModelResponse` with `{"modelResponseData":{"text":"..."}}` at `https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:...` `[Documented]` R6.
- "The userPromptData field must contain only the content of the latest message from the user in the current conversation." ; "Don't include conversation history" ; "The system prompt shouldn't be included in the userPromptData field. Model Armor focuses on detecting threats only in user-provided inputs." `[Documented]` R3/R6.
- Streaming: "StreamSanitizeUserPrompt: Streams and sanitizes user-provided text." "StreamSanitizeModelResponse: Streams and sanitizes LLM-generated text." ; "Model Armor streaming methods don't support Sensitive Data Protection de-identification." ; release note 2026-07-10 "Streaming sanitization for text is generally available (GA)." `[Documented]` R4/R6.
- Files: "Model Armor doesn't automatically detect the file type. You must explicitly set the byteDataType field" ; values "PLAINTEXT_UTF8, PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT, and CSV" ; "Sensitive Data Protection de-identification is not supported for file-based prompts." `[Documented]` R6. Examples are shown for `userPromptData` only; file/image on `modelResponseData` not exemplified `[To be verified]` (overview says images in "prompts and responses").

S9 Result schema. https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
- "filterMatchState ... NO_MATCH_FOUND: No filters in configuration satisfy matching criteria... MATCH_FOUND: At least one filter in configuration satisfies matching." ; filter keys "csam", "malicious_uris", "rai", "pi_and_jailbreak", "sdp" ; "invocationResult ... SUCCESS: All filters were executed successfully. PARTIAL: Some filters were skipped or failed execution. FAILURE: All filters were skipped or failed execution." ; `executionState` values EXECUTION_SUCCESS/EXECUTION_SKIPPED ; PI result has `matchState` and `confidenceLevel`; RAI result has per-type `raiFilterTypeResults` with `filterType`, `confidenceLevel`, `matchState`; SDP has `inspectResult` (infoType, likelihood, location) and `deidentifyResult` ; malicious URI has `maliciousUriMatchedItems`. `[Documented]` R5. Output is a verdict per filter, no numeric score field found in schema (checked SanitizationResult page).

S10 Basic SDP. sanitize page: "The following Sensitive Data Protection infoTypes are scanned in the prompt for all regions: CREDIT_CARD_NUMBER ... FINANCIAL_ACCOUNT_NUMBER ... GCP_CREDENTIALS ... GCP_API_KEY ... PASSWORD" and "additional ... for US-based regions: US_SOCIAL_SECURITY_NUMBER ... US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER" `[Documented]` R2. Conflict C2 with S3 (6 categories, no PASSWORD).
- Advanced: "the Sensitive Data Protection templates must be in the same location as the Model Armor template." ; cross-project roles "DLP User (roles/dlp.user) and DLP Reader (roles/dlp.reader)". `[Documented]` R7.
- Image redaction: "Make sure that you configure image redaction in the de-identify template." (images section) `[Documented]` R4.
- Gemini Enterprise: "Model Armor doesn't pass de-identified or masked data back to Gemini Enterprise" ; Agent Platform: "Model Armor doesn't pass the de-identified data ... back" (S18 neighbours) `[Documented]` R4.

S11 Pricing/SDP. SCCP: "When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it." `[Documented]` R7.

S12 Release notes. https://docs.cloud.google.com/model-armor/release-notes (footer 2026-10-07)
- "The prompt injection and jailbreak detection filter is updated and uses a new model, which together have the following benefits" (2026-05-25); "A new filter version, v3, is available under the Latest alias. v3 features an updated prompt injection and jailbreak detection filter. This new model has been trained to: Significantly reduce false positives." ; 2025-09-23 upgraded model improves "Do Anything Now prompts, System instruction manipulation, Unauthorized action execution, Sensitive information retrieval" ; 2026-10-10 entry: "enhanced prompt injection and jailbreak protection for Workspace data" for filter version v3 or later in us and eu `[Documented]` R4.
- "Model Armor is FedRAMP High compliant." (2026-04-06) `[Documented]` R7.
- Superseded limits: 2025-05-28 "All Model Armor filters support up to 2,000 tokens." ; 2025-07-28 "prompt injection and jailbreak detection filter now supports 10,000 tokens" ; 2026-08-25 "up to 65,536 tokens". Current is S13.

S13 Quotas. https://docs.cloud.google.com/model-armor/quotas
- "API queries | 1200 queries per minute (QPM) per project" ; "Requests to ExternalProcessor | 600 QPM per project" ; "Model Armor screens text up to 65,536 tokens (approximately 262,144 characters) for prompt injection and jailbreak detection, responsible AI, and child sexual abuse material (CSAM) filters." ; "Sensitive Data Protection | 130,000" ; "If the prompt or response exceeds the filter's token limit, the filter returns EXECUTION_SKIPPED" ; "When you sanitize streaming text in real-time mode, Model Armor supports unlimited tokens." ; "All supported files and images | 4 MB". Exclusion rule limits: "Maximum rule sets per filter configuration | 10", "Maximum regular expression pattern length | 1,000 characters". `[Documented]` R6/R7.

S14 Image details: see S2. Console note: "Only us and eu multi-regions support image modality." (S4) `[Documented]`.

S15 Product page. https://cloud.google.com/security/products/model-armor
- "It uses a hybrid defense in-depth approach that combines rules-based controls, ML models, and powerful AI reasoning models to provide adaptive defenses." `[Documented]` R4 (generic; no per-filter mapping).
- "Model Armor protects all LLMs (including Gemini, OpenAI, Anthropic, Llama, and more) via a REST API" `[Documented]` R3/R7.
- "Detects malicious files, malware, and unsafe URLs within AI prompts and responses." `[Documented]` R2.

S16 Result schema, virus. SanitizationResult page: `VirusScanFilterResult` with "scannedContentType" enum PLAINTEXT/PDF and note "PDF Scanning for only PDF is supported."; release note 2026-04-10: "The level of detail provided in the virusDetails field of the Antivirus filter scan results has been updated." `[Documented]` that the output exists; configuration `[To be verified]` (FilterConfig in templates REST has only raiSettings, sdpSettings, piAndJailbreakFilterSettings, maliciousUriFilterSettings).

S17 Regions. https://docs.cloud.google.com/model-armor/feature-availability-by-region and https://docs.cloud.google.com/model-armor/data-residency
- "If you create a Model Armor template in a full-support region, you have access to all of the following filters." Table: eu, europe-southwest1, europe-west1/3/4/9, us, us-central1, us-east1, us-east4, us-west1 full support ; limited: asia-northeast1, asia-northeast3, asia-south1, asia-southeast1 (Singapore), australia-southeast2, europe-west2, northamerica-northeast2. Supported-filters row: "asia-southeast1 | Responsible AI Sensitive Data Protection Prompt injection and jailbreak | No | No | No | No" (no malicious URL, multi-language, CSAM, image, antivirus). `[Documented]` R7.
- "The global endpoint (modelarmor.googleapis.com)" for floor settings; templates need `modelarmor.LOCATION.rep.googleapis.com`.
- Release note 2026-06-22: "Model Armor supports data residency in-use compliance in Singapore (asia-southeast1). This region has limited feature support." ; fix route: "you can disable data residency enforcement in your Model Armor template" (`data_residency_compliant` false). `[Documented]` R7.

S18 Integrations. https://docs.cloud.google.com/model-armor/integrations and per-integration pages (…/model-armor-vertex-integration, -apigee-, -agent-gateway-, -gemini-enterprise-, -mcp-google-cloud-, -networking-, -langchain-integration)
- "Direct REST API: The Model Armor REST API supports all modalities, including text, documents, and images." ; "only the Gemini Enterprise integration supports documents. All other integrations scan and sanitize only text." `[Documented]` R3/R6.
- Floor settings: "Inline enforcement: Apply Model Armor protections to Gemini models and Google Cloud MCP servers. Inline enforcement is configured at the project level." ; "You cannot create or update a template that's less strict than the floor settings." ; org/folder via API only. https://docs.cloud.google.com/model-armor/configure-floor-settings `[Documented]` R6/R7.
- MCP: "Model Armor sanitizes only the following MCP payloads: tools/call request and response; prompts/get request and response; MCP tool execution errors" ; "Tip: Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data." `[Documented]` R3.
- Networking: "The mechanism for this integration is through Service Extensions." ; Cloud Load Balancing, GKE Inference Gateway, Secure Web Proxy. `[Documented]` R4.
- LangChain: runnables "ModelArmorSanitizePromptRunnable" and "ModelArmorSanitizeResponseRunnable"; Preview. `[Documented]` R4/R7.
- Vertex/Agent Platform: "Model Armor provides prompt and response protection within Gemini API in Vertex AI for the generateContent method." `[Documented]` R3.
- Gemini Enterprise: "Interactions with custom agents from your organization (such as ADK, A2A, and Dialogflow) are not screened." `[Documented]` R3.
- Status dates from release notes: Agent Platform GA 2025-12-03; MCP GA (2026-04-22); Agent Gateway GA (2026-06-24); GKE/Service Extensions GA (2025-09-15); Gemini Enterprise GA (2025-09-16); Apigee: GA status not found in notes (`[To be verified]`).

S19 Libraries. https://docs.cloud.google.com/model-armor/reference/libraries : "pip install --upgrade google-cloud-modelarmor" and "npm install @google-cloud/modelarmor" `[Documented]` R7. Client repos live under `googleapis` org (search result titles; not read, GitHub 403).

S20 Pricing. https://cloud.google.com/security-command-center/pricing and PROD pricing table: "Free for up to 2 million tokens/month" ; "$0.10 per additional 1 million tokens" ; SCC Premium/Enterprise subscription "3 billion tokens/month" ; "Model Armor uses the same token definition as Gemini Enterprise Agent Platform: four characters (using UTF-8 code points) per token excluding white space." `[Documented]` R7.

S21 Blog. https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps (2025-10-22): "Prompt injection and jailbreak detection: It identifies and blocks attempts to manipulate an LLM into ignoring its instructions and safety filters." ; "Model Armor is designed to be model-independent and cloud-agnostic" `[Documented]` R1/R3 (vendor blog; supporting only).

S22 Floor setting scope in Vertex: https://docs.cloud.google.com/model-armor/model-armor-vertex-integration : "Sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported in this integration." `[Documented]` R6.

S23 Template-specific exclusion rules (Preview). https://docs.cloud.google.com/model-armor/configure-exclusion-rules : "You can use exclusion rules for the following filters: Prompt injection and jailbreak detection ... Responsible AI safety filters" ; release note 2026-09-28 "Template-specific exclusion rules are available in Preview." `[Documented]` R5/R6.

S24 Logging. https://docs.cloud.google.com/model-armor/configure-logging : log label `modelarmor.googleapis.com/client_correlation_id`; floor-setting logging flag `enableCloudLogging`. `[Documented]` R5/R7 (SCC findings: Agent Gateway page says "These findings are also surfaced in Security Command Center.").

## 5. Gaps (checked X, Y: not stated)
- G1 Backing model/classifier identity and architecture of each filter (RAI, PI/jailbreak, URL): checked overview, product page, filter-version pages, release notes, blog; only "rules-based controls, ML models, and ... AI reasoning models" and "new model" are stated. `[Not disclosed]`.
- G2 Published accuracy/recall/F1 or benchmark numbers: checked overview, best practices, product page, blog, release notes; only qualitative "reduce false positives". `[Not disclosed]`. Docs advise own testing.
- G3 Latency/SLA for the Model Armor API itself: checked overview, quotas, integrations, retry-strategy page title (not read fully), Apigee page; no latency figure. SLA statement only for Gemini Enterprise integration. `[Not disclosed]`.
- G4 Taxonomy of prompt-injection/jailbreak categories: only the 2025-09-23 list of improved vectors. `[Not disclosed]`.
- G5 Numeric score output: schema has enum confidenceLevel/likelihood, no numeric score (checked SanitizationResult). Report as absence of a documented numeric score `[Not disclosed]`.
- G6 Antivirus filter configuration, thresholds and supported types beyond PDF: `[To be verified]` (S16).
- G7 Response-side file and image examples (`modelResponseData` with `byteItem`): not shown; `[To be verified]`.
- G8 Apigee integration GA/Preview status and policy names: page body read only at top; not confirmed `[To be verified]`.
- G9 Official GitHub samples: `github.com/GoogleCloudPlatform/*` and `googleapis/*` pages return HTTP 403 through the session proxy (apigee-samples, generative-ai, model-armor-samples); search snippet names `GoogleCloudPlatform/apigee-samples` (llm-security sample) and `googleapis/google-cloud-java` java-modelarmor; none read. `git clone` not attempted (P0 cap). `[To be verified]`.
- G10 Whitepapers (product page "Read white paper"): not read.
- G11 Singapore-specific infoTypes in the SDP filter: basic mode has none (US SSN/ITIN only); advanced mode depends on SDP templates (sdp explorer). `[To be verified]` here.
- G12 Terraform resource page and Cloud Logging log schema detail not read beyond labels.

## 6. Conflicts between official sources
- C1 PI/jailbreak confidence recommendation: overview best practices say "Set prompt injection and jailbreak detection filters to Medium." (S5), templates page says "We recommend that you set the confidence level to High" (S4). Two bullets needed.
- C2 Basic SDP infoTypes: overview lists 6 categories (credit card, US SSN, financial account, ITIN, Google Cloud credentials, API key) (S3); sanitize page lists 7 infoTypes incl. PASSWORD and says SSN/ITIN apply to US-based regions only (S10).
- C3 Default confidence level: console steps in manage-templates say "If you don't specify a confidence level, it is set to High by default." (S4) vs REST reference "DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED | Same as LOW_AND_ABOVE." (S6). Test needed.
- C4 Images embedded in documents: overview and integrations overview say they are not screened ("Model Armor doesn't screen images embedded within files."; "images embedded in documents aren't screened") but the Gemini Enterprise integration page says it screens "Images contained inside other files and documents that you upload directly."
- C5 Token limits over time: release notes 2025-05-28 (2,000), 2025-07-28 (10,000 PI) vs current 65,536 (S13); current page wins, notes are historical. Also overview vs quotas: SDP 130,000 only on quotas page. Gemini Enterprise "no token limits".
- C6 Filter version retirement date: release note 2026-09-02 says v1/v2 retire 2026-11-29; 2026-09-18 note says 2026-12-17 (later note supersedes).
- C7 Overview lists 4 filter families (RAI, PI/jailbreak, SDP, malicious URL) plus CSAM; product page and region tables also list antivirus/malware scanning; no configuration doc (G6).
- C8 Template filter version: REST says filterVersionSelector overrides "deprecated filterVersion fields" in RaiFilterSettings and PiAndJailbreakFilterSettings; docs say a single version per template. Not a contradiction, record in inventory.
- C9 Seed URL path (SCC docs) superseded by /model-armor/ section (redirect, see header). Also the release notes page shows an entry dated "October 10, 2026" while read on 2026-10-09 (system date); likely time-zone/pre-announced; labelled as read.

## 7. URLs visited (HTTP status, 2026-10-09)
200 https://cloud.google.com/security-command-center/docs/model-armor-overview (301 first hop, final https://docs.cloud.google.com/model-armor/overview)
200 https://cloud.google.com/model-armor/overview (empty body in fetch)
404 https://cloud.google.com/model-armor/docs
200 https://docs.cloud.google.com/model-armor/{overview, manage-templates, sanitize-prompts-responses, configure-floor-settings, quotas, feature-availability-by-region, data-residency, set-filter-version, version-history, configure-exclusion-rules, integrations, model-armor-vertex-integration, model-armor-apigee-integration, model-armor-agent-gateway-integration, model-armor-gemini-enterprise-integration, model-armor-langchain-integration, model-armor-mcp-google-cloud-integration, model-armor-networking-integration, best-practices, retry-strategy, reference/libraries, configure-logging, monitoring-dashboard, access-control/roles-permissions, troubleshooting, release-notes}
200 https://docs.cloud.google.com/model-armor/reference/rest/v1/{projects.locations.templates, SanitizationResult}
404 https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations/sanitizeModelResponse ; .../v1/FilterConfig (guessed paths)
200 https://cloud.google.com/security/products/model-armor ; https://cloud.google.com/security-command-center/pricing ; https://docs.cloud.google.com/release-notes (not used)
200 https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps
404 https://docs.cloud.google.com/sensitive-data-protection/docs/model-armor (guessed)
403 https://github.com/GoogleCloudPlatform/model-armor-samples ; /generative-ai ; /apigee-samples (proxy)
Tools: WebSearch (1 call, locator only). Not run: Context7, GitHub MCP, Hugging Face (no vendor repo/model). ~45 fetches (several bulk).
Pages fetched but only skimmed (not quoted): best-practices, retry-strategy, monitoring-dashboard, roles-permissions, troubleshooting, Apigee body.

## 8. QUESTIONS
Q01 - Column count and split: 10 columns (MA1-MA10) with input/output pairs for RAI, PI/jailbreak, SDP and malicious URL, plus two modality columns; antivirus and MCP screening as inventory by default. Rationale R002 (separate sanitize methods). Blocking: no; decide at CP1. See 20261009_modelarmor_q01.md.
Q02 - SDP overlap with the sdp product: MA5/MA6 cover only how Model Armor invokes SDP (basic/advanced, inspect and de-identify templates). SDP internals (infoTypes, transformations) stay in sdp columns; confirm main wants MA5/MA6 as Model Armor columns rather than only cross-references. Not blocking.
Q03 - Header prefix `Model Armor:` (without "Google Cloud"), to fix at CP1 under R009. Not blocking.
Q04 - Official-source scope: docs.cloud.google.com and cloud.google.com pages only; Google GitHub samples/client libraries are unreadable in this session (403). Is the 403 acceptable (record as gap) or should a different route be tried? Not blocking.
