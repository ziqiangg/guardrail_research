## Column MA5: Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)
### R1
Summary: **Input-level sensitive data detection and de-identification.** Model Armor calls Sensitive Data Protection on the user prompt to find sensitive items. In advanced mode with a de-identify template it also returns a de-identified copy of the prompt; basic mode only inspects. **[Documented]**
Detail:
• Model Armor offers Sensitive Data Protection as one of its filters: "You can use Sensitive Data Protection directly within Model Armor to transform, tokenize, and redact sensitive elements while retaining non-sensitive context." (overview, read 2026-10-09) **[Documented]**
• Product page: Model Armor "helps prevent the leakage of personal identifiable information (PII), financial information, credentials, and custom-defined sensitive data types in both prompts and model responses" (product page, read 2026-10-09) **[Documented]**
• The prompt-side use case is named "Mask or redact sensitive values: Automatically obscure identified personally identifiable information (PII) or secrets within prompts or responses." (sanitize page, read 2026-10-09) **[Documented]**
• Two modes: basic "only supports inspection operations and doesn't support the use of Sensitive Data Protection templates"; advanced "supports both inspection and de-identification operations" (overview, read 2026-10-09) **[Documented]**
• Overview scenario: a chatbot user types a credit card number and "Model Armor blocks the prompt containing the PII"; the block depends on the Inspect and block enforcement type and is carried out by the calling service (overview, read 2026-10-09) **[Documented]**
• The filter's result key is `sdp` with `sdpFilterResult` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Sensitive Data Protection is a separate Google Cloud service that Model Armor calls; the infoType catalogue, transformation types and likelihood meaning are defined there, so this column covers only how Model Armor invokes it (see the Sensitive Data Protection columns on sheet 3). The premise is that Model Armor docs link out to the Sensitive Data Protection documentation for these topics **[Inferred]**
### R2
Summary: **Basic mode: a short fixed list; advanced mode: whatever your template defines.** Basic mode lists mainly US-oriented items such as card numbers, financial accounts and Google Cloud credentials; Google's pages disagree on whether the list has six or seven items. Advanced mode uses your Sensitive Data Protection template. **[Documented]**
Detail:
• Overview lists six basic categories: credit card number, US social security number, financial account number, US individual taxpayer identification number, Google Cloud credentials, Google Cloud API key (overview, read 2026-10-09) **[Documented]**
• REST reference: basic configuration inspects "using a fixed set of six info-types" (templates reference, read 2026-10-09) **[Documented]**
• Sanitize page lists, for all regions, CREDIT_CARD_NUMBER, FINANCIAL_ACCOUNT_NUMBER, GCP_CREDENTIALS, GCP_API_KEY and PASSWORD (sanitize page, read 2026-10-09) **[Documented]**
• Sanitize page adds, for US-based regions, US_SOCIAL_SECURITY_NUMBER and US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER, which makes seven in total (sanitize page, read 2026-10-09) **[Documented]**
• Source conflict: the overview and the REST reference say six items, while the sanitize page lists seven (it adds PASSWORD); no page reconciles the two counts (overview, REST reference and sanitize page, read 2026-10-09) **[Documented]**
• Which locations count as "US-based regions" for the two US identifiers is not defined (checked the sanitize page, overview and feature availability page) **[Not disclosed]**
• Overview strategy text: "basic Sensitive Data Protection provides limited infotypes, mainly addressed to the US region" and advises an advanced template for "the required infotypes for your use case" (overview, read 2026-10-09) **[Documented]**
• Basic mode lists no national identifier outside the US (no Singapore, UK or EU identifier); checked the overview, sanitize page and REST template reference **[Not disclosed]**
• Advanced mode takes its detectors from a customer inspect template: such templates hold "what predefined or custom detectors to use" (templates page, read 2026-10-09) **[Documented]**
• Advanced results may report a BASIC_AUTH_HEADER infoType "even if it is not explicitly included in the configured inspection template" (sanitize page, read 2026-10-09) **[Documented]**
• Language: the filter "supports English and other languages depending on the infoTypes that you selected" (overview, read 2026-10-09) **[Documented]**
• Encoded content is not decoded: "Model Armor doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext." (overview, read 2026-10-09) **[Documented]**
• Confidence levels cannot be set for this filter: "You can set confidence levels only for prompt injection and jailbreak detection and responsible AI safety filters", and "Confidence levels for Sensitive Data Protection operate differently" (overview, read 2026-10-09) **[Documented]**
### R3
Summary: **The latest user message, sent in the prompt field.** The text goes to the regional prompt-sanitising method; send only the current message, never history or system prompts. Each call is judged alone. Documented examples exist for the prompt side only. **[Documented]**
Detail:
• Method and field: `POST https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeUserPrompt` with body `{"userPromptData":{"text":"..."}}` (sanitize page, read 2026-10-09) **[Documented]**
• The regional endpoint is required: "The global endpoint (modelarmor.googleapis.com) doesn't support" template management or sanitizing (templates page, read 2026-10-09) **[Documented]**
• "The userPromptData field must contain only the content of the latest message from the user in the current conversation." (sanitize page, read 2026-10-09) **[Documented]**
• The same page says "Don't include conversation history" and "Don't include system prompts" in that field (sanitize page, read 2026-10-09) **[Documented]**
• "Model Armor inspects each prompt and response independently as a single-turn request." (overview, read 2026-10-09) **[Documented]**
• The basic infoType lists are introduced as types "scanned in the prompt" (sanitize page, read 2026-10-09) **[Documented]**
• Both the basic example (an ITIN in a prompt) and the advanced example (an IP address in a prompt) on the sanitize page send `userPromptData`; the page shows no input-side file example with de-identification (sanitize page, read 2026-10-09) **[Documented]**
• Overview guidance: the input template is "Focused on preventing malicious inputs, prompt injections, jailbreak attempts, and uploading sensitive data" (overview, read 2026-10-09) **[Documented]**
• Streaming: `StreamSanitizeUserPrompt` takes text only, and "Model Armor streaming methods don't support Sensitive Data Protection de-identification" (sanitize page, read 2026-10-09) **[Documented]**
• Files: "Sensitive Data Protection de-identification is not supported for file-based prompts." (sanitize page, read 2026-10-09) **[Documented]**
• Only active filters send data onward: "Model Armor only transmits and processes data for active filters" (overview, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers: Model Armor sanitizes `tools/call` requests and `prompts/get` requests through floor settings, and says this mitigates "prompt injection and sensitive data disclosure" (MCP integration page, read 2026-10-09) **[Documented]**
### R4
Summary: **A managed call from Model Armor to Sensitive Data Protection.** Basic mode uses a fixed list; advanced mode points to your inspect template and optionally a de-identify template in the same location. Model Armor docs do not describe the detectors, and the REST route returns the result without forwarding it. **[Documented]**
Detail:
• Basic mode: `sdpSettings.basicConfig.filterEnforcement` is ENABLED or DISABLED, and the unspecified value is "Same as Disabled" (templates reference, read 2026-10-09) **[Documented]**
• Advanced mode: `sdpSettings.advancedConfig` takes `inspectTemplate` and optionally `deidentifyTemplate`, as resource names such as `projects/PROJECT/locations/LOCATION/inspectTemplates/NAME` (templates reference, read 2026-10-09) **[Documented]**
• Basic and advanced are mutually exclusive: "At most one of the fields will be set" (templates reference, read 2026-10-09) **[Documented]**
• With only an inspect template, the REST reference says an InspectContent action is performed; with a de-identify template too, a DeidentifyContent action is performed and the result is returned in the de-identify result (templates reference, read 2026-10-09) **[Documented]**
• Rule: "all info-types present in the deidentify template must be present in inspect template" (templates reference, read 2026-10-09) **[Documented]**
• Same-location rule: "the Sensitive Data Protection templates must be in the same location as the Model Armor template" (sanitize page, read 2026-10-09) **[Documented]**
• The generated Go library comments for `SdpAdvancedConfig` repeat the InspectContent and DeidentifyContent behaviour (service.pb.go@37f936ac:2226) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Backing detectors: Model Armor docs give no detector internals or model identity for this filter; they only call Sensitive Data Protection "a Google Cloud service" (checked the overview, templates page, product page and REST reference) **[Not disclosed]**
• The filter version setting does not apply: "The filter version setting doesn't affect the Sensitive Data Protection and malicious URL filters." (set-filter-version page, read 2026-10-09) **[Documented]**
• Direct REST use returns the result and nothing more: "When you use the REST API for integration, Model Armor functions only as a detector using templates." (integrations page, read 2026-10-09) **[Documented]**
• Overview data flow: "The prompt (or sanitized prompt) is sent to the LLM." so the caller decides whether to forward the original or the de-identified text (overview, read 2026-10-09) **[Documented]**
• Gemini Enterprise Agent Platform route (GA 2025-12-03 per release notes): Model Armor "doesn't pass the de-identified data" back; with INSPECT_AND_BLOCK it issues a block verdict instead (Agent Platform integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise route: it "blocks the request or response rather than de-identifying it" when an infoType detector fires (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Apigee route: "Apigee allows, blocks, or redacts the request or response", and redacted data is extracted from flow variables and passed to the LLM; the pages read do not state GA or Preview (Apigee integration page, read 2026-10-09) **[Documented]**
• Agent Gateway route (GA 2026-06-24 per release notes): a template can "block and redact content that violates policies"; the page does not say how redaction is returned (Agent Gateway page, read 2026-10-09) **[Documented]**
• Service Extensions route: Model Armor tells the networking service to "allow, block, or modify the traffic" (networking page, read 2026-10-09) **[Documented]**
• Which integration actually forwards de-identified input text, other than Apigee, is not stated on the Agent Gateway and Service Extensions pages (checked both) **[Not disclosed]**
• Pricing: "When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it." (pricing page, read 2026-10-09) **[Documented]**
• Logging caveat: "Enabling logging in a template writes raw prompts and responses to Logging", so original sensitive text can appear in logs even when the API returns de-identified text (logging page, read 2026-10-09) **[Documented]**
• Location support: Sensitive Data Protection is listed as a supported filter in every location row, including the limited-support regions; asia-northeast3 lists it as the only supported filter (feature availability page, read 2026-10-09) **[Documented]**
• A self-hosted or offline route is not described (checked the overview, product page, integrations page and client library page) **[Not disclosed]**
### R5
Summary: **Match state plus findings or a de-identified copy.** The result holds an inspect, de-identify or redact result, each with execution and match state. Findings carry infoType, a likelihood word and a position. There is no numeric score and no published accuracy figure. **[Documented]**
Detail:
• The sdp result holds one of `inspectResult`, `deidentifyResult` or `redactResult`; "At most one of the fields will be set in a response" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• `inspectResult` fields: `executionState`, `messageItems`, `matchState`, `findings[]`, `findingsTruncated`, `extractedImageText` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Each finding has `infoType`, `likelihood` and `location` with `byteRange` and `codepointRange` for text (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Basic-mode example: an ITIN prompt returns `filterMatchState` MATCH_FOUND, infoType US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER, likelihood LIKELY, range 26 to 37 (sanitize page, read 2026-10-09) **[Documented]**
• `deidentifyResult` fields: `executionState`, `messageItems`, `matchState`, `data`, `transformedBytes`, `infoTypes` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Advanced-mode example returns `data.text` "is there anything malicious running on [IP_ADDRESS]?", `transformedBytes` "7" and `infoTypes` ["IP_ADDRESS"], with no findings list (sanitize page, read 2026-10-09) **[Documented]**
• The page text says the de-identified output is in "the deidentifyResult.data.text field of the finding" (templates page and sanitize page, read 2026-10-09) **[Documented]**
• Whether a findings list with positions also comes back when a de-identify template is set is not shown (checked the sanitize page example and REST reference) **[Not disclosed]**
• Likelihood values: VERY_UNLIKELY, UNLIKELY, POSSIBLE, LIKELY, VERY_LIKELY; unspecified is "same as POSSIBLE" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• How a likelihood is turned into a match, and any minimum-likelihood setting, belong to the Sensitive Data Protection template; Model Armor's overview only points to "Sensitive Data Protection match likelihood" **[Inferred]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• Execution problems: if text exceeds the token limit the filter returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**
• Error text for transient or quota errors in this detector became "Error occurred while processing sensitive data detection. Please try again." (release note 2026-02-10) **[Documented]**
• Enforcement: INSPECT_ONLY does not block and INSPECT_AND_BLOCK returns a block verdict that the caller must act on (overview, read 2026-10-09) **[Documented]**
• Source conflict on shape: the REST reference says `filterResults` is a map keyed "csam", "malicious_uris", "rai", "pi_and_jailbreak", "sdp" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Source conflict on shape: the basic and advanced sections of the sanitize page show `filterResults` as a JSON array of objects without keys (sanitize page, read 2026-10-09) **[Documented]**
• Published detection accuracy, recall or false-positive figures for this filter are not given in Model Armor docs (checked the overview, product page, blog, release notes and best practices) **[Not disclosed]**
### R6
Summary: **Template, location and a per-mode setting.** Basic mode needs one switch; advanced mode needs a full inspect template name and optionally a de-identify template name. Templates must share the Model Armor template's location. Cross-project use needs two Sensitive Data Protection roles. Text over 130,000 tokens is skipped. **[Documented]**
Detail:
• Basic config via gcloud: `gcloud model-armor templates create TEMPLATE_ID --location=LOCATION --project=PROJECT_ID --basic-config-filter-enforcement=enabled` (sanitize page, read 2026-10-09) **[Documented]**
• Advanced config via gcloud shows `--advanced-config-inspect-template="path/to/template"`; the page shows the de-identify template only in REST and client library samples (sanitize page, read 2026-10-09) **[Documented]**
• Resource name forms: `projects/projectId/locations/locationId/inspectTemplates/templateName` and `projects/projectId/locations/locationId/deidentifyTemplates/templateName` (templates page, read 2026-10-09) **[Documented]**
• Cross-project: "the Model Armor service agent must be granted the DLP User role (roles/dlp.user) and DLP Reader role (roles/dlp.reader)" in the project that holds the Sensitive Data Protection templates (templates page, read 2026-10-09) **[Documented]**
• The sanitize page repeats this and names the agent `service-PROJECT_NUMBER@gcp-sa-modelarmor.iam.gserviceaccount.com` (sanitize page, read 2026-10-09) **[Documented]**
• Caller roles: `roles/modelarmor.user` to sanitize and `roles/modelarmor.admin` to manage templates (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Token limit: the table gives 130,000 for Sensitive Data Protection against 65,536 for the other three filters; the limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, read 2026-10-09) **[Documented]**
• The overview does not give the 130,000 figure; only the quotas page does (checked the overview and best practices pages) **[Not disclosed]**
• Real-time streaming mode "supports unlimited tokens", but streaming does not de-identify (quotas page and sanitize page, read 2026-10-09) **[Documented]**
• Earlier release note 2025-07-28 said the Sensitive Data Protection filter returns SKIP_DETECTION over the limit; the current quotas page says EXECUTION_SKIPPED (release notes and quotas page, read 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project" for the Model Armor API (quotas page, read 2026-10-09) **[Documented]**
• Whether Model Armor's calls to Sensitive Data Protection use up Sensitive Data Protection quota is not stated (checked the quotas page and integrations page) **[Not disclosed]**
• Floor settings can enable the filter (the Agent Platform page example sets `sdpSettings.basicConfig`), and "Floor settings don't check templates for Sensitive Data Protection conformance" (floor settings page, read 2026-10-09) **[Documented]**
• Language: English plus others depending on the chosen infoTypes (overview, read 2026-10-09) **[Documented]**
• Multi-language detection is a template or per-request setting for the other filters; whether it affects this filter is not stated (checked the overview and templates page) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the Model Armor API enabled, a template in a regional location with basic or advanced Sensitive Data Protection on, and the Model Armor User role. Advanced mode also needs inspect and de-identify templates in the same location. Test with synthetic card numbers, US identifiers and passwords. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled (`gcloud services enable modelarmor.googleapis.com`), `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call it, and one regional template. Basic mode is the quickest start; for de-identification create Sensitive Data Protection inspect and de-identify templates in the template's location. Then POST to the regional `sanitizeUserPrompt` endpoint **[Inferred]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Test data: labelled prompts with synthetic card numbers, US SSN and ITIN strings, Google Cloud keys, passwords, near misses, and for advanced mode the identifiers your own template defines; Google gives no labelled test set **[Inferred]**
• Singapore (asia-southeast1) lists Sensitive Data Protection as supported, but basic mode names only US national identifiers, so a Singapore NRIC test needs an advanced template with a custom detector (see the Sensitive Data Protection columns) **[Inferred]**
• When testing through an integration in Inspect only mode, the overview says to "check the SanitizeOperationLogEntry records in Cloud Logging rather than relying on the response body"; direct REST calls return the filter result in the response (overview, read 2026-10-09) **[Documented]**
• No self-hosted or offline option is documented (checked the overview, product page and integrations page) **[Not disclosed]**
### R8
Summary: **Key open questions.** Whether basic mode has six or seven infoTypes, which regions are US-based, what de-identified input looks like with positions, whether floor settings accept advanced templates, how quota and latency are affected, and what accuracy to expect.
Detail:
• Basic infoType list: six (overview, REST reference) or seven (sanitize page, adds PASSWORD); needs a live test per region
• Which regions are "US-based" for the SSN and ITIN detectors (checked the sanitize page, overview and feature availability page, not stated)
• Whether a findings list is returned together with a de-identified copy (needs testing)
• Whether the de-identified text is returned when enforcement is Inspect only (needs testing; checked the overview and templates page, not stated)
• Whether floor settings accept an advanced inspect template given the same-location rule and the global floor-setting location (checked the floor settings page and Agent Platform page, not stated)
• Whether Model Armor's calls use Sensitive Data Protection quota and add latency (checked the quotas page, best practices and integrations pages; only the generic note that unnecessary detectors can add latency)
• What the sanitize page examples mean by a bare array for `filterResults` against the keyed map in the REST reference (needs testing)
• Detection accuracy for the basic detectors, and whether a hidden likelihood threshold applies in basic mode (checked the overview, REST reference and Sensitive Data Protection link; not stated)
• Whether the 130,000-token Sensitive Data Protection limit applies to the text sent by integrations (Gemini Enterprise is exempt per the quotas page)
• Whether multi-language detection changes Sensitive Data Protection results (checked the overview and templates page, not stated)
### R9
Summary: Model Armor docs (overview, templates, sanitize, quotas, integrations, floor settings, filter versions, logging, release notes, REST references), the product and pricing pages, and the pinned Google Go client library.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
• https://docs.cloud.google.com/model-armor/model-armor-apigee-integration
• https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
• https://docs.cloud.google.com/model-armor/model-armor-networking-integration
• https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration
• https://docs.cloud.google.com/model-armor/configure-floor-settings
• https://docs.cloud.google.com/model-armor/set-filter-version
• https://docs.cloud.google.com/model-armor/configure-logging
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go
