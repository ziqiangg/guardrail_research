## Column MA5: Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)
### R1
Summary: **Input-level sensitive data detection and de-identification.** Model Armor calls Sensitive Data Protection on the user prompt to find sensitive items. In advanced mode with a de-identify template it also returns a de-identified copy of the prompt; basic mode only inspects. **[Documented]**
Detail:
• Model Armor offers Sensitive Data Protection as one of its filters: "You can use Sensitive Data Protection directly within Model Armor to transform, tokenize, and redact sensitive elements while retaining non-sensitive context." (overview, read 2026-10-09) **[Documented]**
• Product page: Model Armor "helps prevent the leakage of personal identifiable information (PII), financial information, credentials, and custom-defined sensitive data types in both prompts and model responses" (product page, read 2026-10-09) **[Documented]**
• The prompt-side use case is named "Mask or redact sensitive values: Automatically obscure identified personally identifiable information (PII) or secrets within prompts or responses." (sanitize page, read 2026-10-09) **[Documented]**
• Two modes: basic "only supports inspection operations and doesn't support the use of Sensitive Data Protection templates"; advanced "supports both inspection and de-identification operations" (overview, read 2026-10-09) **[Documented]**
• Overview scenario: a chatbot user types a credit card number and "Model Armor blocks the prompt containing the PII" (overview, read 2026-10-09) **[Documented]**
• The filter's result key is `sdp` with `sdpFilterResult` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Sensitive Data Protection is a separate Google Cloud service that Model Armor calls; the infoType catalogue, transformation types and likelihood meaning are defined there, so this column covers only how Model Armor invokes it (see the Sensitive Data Protection columns on sheet 3). The premise is that Model Armor docs link out to the Sensitive Data Protection documentation for these topics **[Inferred]**
### R2
Summary: **Basic mode: a short US-leaning list; advanced mode: your template.** Basic mode covers card numbers, financial accounts and Google Cloud credentials, and Google's pages disagree on six or seven items. Advanced mode uses a Sensitive Data Protection template you supply. **[Documented]**
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
Summary: **A managed call from Model Armor to Sensitive Data Protection.** Basic mode uses a fixed list; advanced mode names an inspect template and optionally a de-identify template in the same location. The detectors are not described; the REST route only returns the result. **[Documented]**
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
• Agent Gateway route (GA 2026-06-24 per release notes): the intro says a template can "block and redact content that violates policies" (Agent Gateway page, read 2026-10-09) **[Documented]**
• Agent Gateway traffic flow: "Model Armor screens the request. If blocked, the client receives an error." and responses are allowed or blocked on the verdict; the flow text mentions no redacted copy (Agent Gateway page, read 2026-10-09) **[Documented]**
• Service Extensions route: Model Armor tells the networking service to "allow, block, or modify the traffic" (networking page, read 2026-10-09) **[Documented]**
• Whether Agent Gateway or Service Extensions forward de-identified input text to the model is not stated (checked both pages; only Apigee documents extracting redacted data) **[Not disclosed]**
• Pricing: "When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it." (pricing page, read 2026-10-09) **[Documented]**
• Logging caveat: "Enabling logging in a template writes raw prompts and responses to Logging", so original sensitive text can appear in logs even when the API returns de-identified text (logging page, read 2026-10-09) **[Documented]**
• Location support: Sensitive Data Protection is listed as a supported filter in every location row of the supported-features table, including the limited-support regions (feature availability page, read 2026-10-09) **[Documented]**
• Seoul (asia-northeast3) lists Sensitive Data Protection as its only supported filter when data residency is enforced (feature availability page, read 2026-10-09) **[Documented]**
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
• How a likelihood is turned into a match, and any minimum-likelihood setting, belong to the Sensitive Data Protection template; Model Armor's overview only points to "Sensitive Data Protection match likelihood" (overview, read 2026-10-09) **[Inferred]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• Execution problems: if text exceeds the token limit the filter returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**
• Error text for transient or quota errors in this detector became "Error occurred while processing sensitive data detection. Please try again." (release note 2026-02-10) **[Documented]**
• Enforcement: INSPECT_ONLY does not block and INSPECT_AND_BLOCK returns a block verdict that the caller must act on (overview, read 2026-10-09) **[Documented]**
• Source conflict on shape: the REST reference says `filterResults` is a map keyed "csam", "malicious_uris", "rai", "pi_and_jailbreak", "sdp" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Source conflict on shape: the basic and advanced sections of the sanitize page show `filterResults` as a JSON array of objects without keys (sanitize page, read 2026-10-09) **[Documented]**
• Published detection accuracy, recall or false-positive figures for this filter are not given in Model Armor docs (checked the overview, product page, blog, release notes and best practices) **[Not disclosed]**
### R6
Summary: **Template, location and a per-mode setting.** Basic mode needs one switch; advanced mode needs an inspect template name and optionally a de-identify template name in the same location. Cross-project use needs two Sensitive Data Protection roles. Text over 130,000 tokens is skipped. **[Documented]**
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
• Floor settings can enable the filter: the Agent Platform page example sets `sdpSettings.basicConfig` with `filterEnforcement` ENABLED (Agent Platform integration page, read 2026-10-09) **[Documented]**
• "Floor settings don't check templates for Sensitive Data Protection conformance." (floor settings page, read 2026-10-09) **[Documented]**
• Language: English plus others depending on the chosen infoTypes (overview, read 2026-10-09) **[Documented]**
• Multi-language detection is a template or per-request setting for the other filters; whether it affects this filter is not stated (checked the overview and templates page) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the Model Armor API enabled, a template in a regional location with basic or advanced Sensitive Data Protection on, and the Model Armor User role. Advanced mode also needs inspect and de-identify templates in the same location. Test with synthetic card numbers, US identifiers and passwords. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled (`gcloud services enable modelarmor.googleapis.com`), `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call it, and one regional template. Basic mode is the quickest start; for de-identification create Sensitive Data Protection inspect and de-identify templates in the template's location. Then POST to the regional `sanitizeUserPrompt` endpoint **[Inferred]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Test data: labelled prompts with synthetic card numbers, US SSN and ITIN strings, Google Cloud keys, passwords, near misses, and for advanced mode the identifiers your own template defines; Google gives no labelled test set **[Inferred]**
• Singapore (asia-southeast1) lists Sensitive Data Protection as supported, but basic mode names only US national identifiers, so a Singapore NRIC test needs an advanced template with a custom detector (see the Sensitive Data Protection columns) **[Inferred]**
• When testing through an integration in Inspect only mode, the overview says to "check the SanitizeOperationLogEntry records in Cloud Logging rather than relying on the response body for proper validation" (overview, read 2026-10-09) **[Documented]**
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

## Column MA6: Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)
### R1
Summary: **Output-level sensitive data detection and de-identification.** Model Armor calls Sensitive Data Protection on a model response to find sensitive items that the model produced or repeated. Advanced mode with a de-identify template returns a de-identified copy; basic mode only inspects. **[Documented]**
Detail:
• Product page: the Sensitive Data Protection integration helps prevent leakage of PII, financial information, credentials and custom-defined sensitive data types "in both prompts and model responses" (product page, read 2026-10-09) **[Documented]**
• Overview: the output template is "Focused on preventing the model from leaking sensitive data, generating harmful or off-brand content, or returning malicious URLs" (overview, read 2026-10-09) **[Documented]**
• The response-side use case is the same text as the prompt side: "Automatically obscure identified personally identifiable information (PII) or secrets within prompts or responses" (sanitize page, read 2026-10-09) **[Documented]**
• Two modes: basic "only supports inspection operations", advanced "supports both inspection and de-identification operations" (overview, read 2026-10-09) **[Documented]**
• The filter result key is `sdp`, the same as for prompts (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Sensitive Data Protection is a separate Google Cloud service; its infoType catalogue, transformations and likelihood meaning are covered in the Sensitive Data Protection columns on sheet 3, and this column covers only how Model Armor invokes it on responses. The premise is the same as for the input-level column **[Inferred]**
### R2
Summary: **Sensitive items a model might output.** The documented lists are written for prompts: a short, US-leaning fixed list in basic mode and the customer template in advanced mode. Model Armor docs do not say whether the basic list is the same for responses. **[Documented]**
Detail:
• Basic mode: the overview lists six categories (credit card number, US social security number, financial account number, US individual taxpayer identification number, Google Cloud credentials, Google Cloud API key) (overview, read 2026-10-09) **[Documented]**
• Basic mode: the sanitize page lists CREDIT_CARD_NUMBER, FINANCIAL_ACCOUNT_NUMBER, GCP_CREDENTIALS, GCP_API_KEY and PASSWORD for all regions, plus the SSN and ITIN types for US-based regions (sanitize page, read 2026-10-09) **[Documented]**
• Source conflict: six items (overview, REST reference) against seven (sanitize page); no page reconciles them (overview, REST reference and sanitize page, read 2026-10-09) **[Documented]**
• The sanitize page introduces the basic infoType lists as "scanned in the prompt"; it does not repeat the lists for responses (checked the sanitize page, overview, templates page and REST reference) **[Not disclosed]**
• Advanced mode uses the customer's inspect template, so response-side coverage is whatever that template defines (templates page, read 2026-10-09) **[Documented]**
• Language: "supports English and other languages depending on the infoTypes that you selected" (overview, read 2026-10-09) **[Documented]**
• Encoded output is not decoded: "Model Armor doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext." (overview, read 2026-10-09) **[Documented]**
• Confidence levels cannot be set for this filter; "Confidence levels for Sensitive Data Protection operate differently" (overview, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers: tool responses are sanitised through floor settings, and the page says this mitigates "prompt injection and sensitive data disclosure" (MCP integration page, read 2026-10-09) **[Documented]**
• For MCP traffic the page sanitises `tools/call` response, `prompts/get` response and tool execution errors, and lets `tools/list`, `resources/*` and protocol errors through unsanitised (MCP integration page, read 2026-10-09) **[Documented]**
### R3
Summary: **The model response, sent in its own field.** The text goes to the regional response-sanitising method. An optional field can carry the matching user prompt. Documented examples for response-side de-identification are missing. **[Documented]**
Detail:
• Method and field: `POST https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeModelResponse` with `{"modelResponseData":{"text":"..."}}` (sanitize page, read 2026-10-09) **[Documented]**
• REST request fields: `modelResponseData` ("Required. Model response data to sanitize."), `userPrompt` ("Optional. User Prompt associated with Model response."), `multiLanguageDetectionMetadata`, `streamingMode` (sanitizeModelResponse reference, read 2026-10-09) **[Documented]**
• What Model Armor does with `userPrompt` (for example, whether any filter uses it as context) is not stated (checked the REST method reference and sanitize page) **[Not disclosed]**
• The documented response example (an IP address text) returns rai, pi_and_jailbreak, csam and malicious_uris results and no sdp result, so it does not show response-side Sensitive Data Protection output (sanitize page, read 2026-10-09) **[Documented]**
• A response-side result with `deidentifyResult` is not shown in the docs prose (checked the sanitize page, templates page and overview) **[Not disclosed]**
• Apigee's SanitizeModelResponse policy lists read-only flow variables `SanitizeModelResponse.POLICY_NAME.sdpFilterResult.deidentifyResult.executionState` and `.matchState`, which shows the response path can carry a de-identify result (Apigee policy reference, read 2026-10-09) **[Documented]**
• "Model Armor inspects each prompt and response independently as a single-turn request." (overview, read 2026-10-09) **[Documented]**
• Streaming: `StreamSanitizeModelResponse` streams LLM text, and "Model Armor streaming methods don't support Sensitive Data Protection de-identification" (sanitize page, read 2026-10-09) **[Documented]**
• Files: "Sensitive Data Protection de-identification is not supported for file-based prompts." (sanitize page, read 2026-10-09) **[Documented]**
• The sanitize page words this limit for prompts and shows no response-side file example (checked the sanitize page and templates page) **[Not disclosed]**
• Agent Platform route covers the `generateContent` method; Model Armor "intercepts responses before your application receives them" (Agent Platform integration page, read 2026-10-09) **[Documented]**
• Agent Gateway ingress: "Model Armor screens the response, and Agent Gateway either allows or blocks it based on the verdict." (Agent Gateway page, read 2026-10-09) **[Documented]**
• Agent Gateway egress: Model Armor screens incoming responses from external systems such as MCP servers and other agents before the agent receives them (Agent Gateway page, read 2026-10-09) **[Documented]**
• LangChain (Preview): the response runnable "screens the output generated by the LLM before it is returned to the user", and "Any modifications that the user makes to the response after the primary security check are not filtered" (LangChain page, read 2026-10-09) **[Documented]**
### R4
Summary: **The same managed call as for prompts, on the response path.** Basic and advanced settings, templates and roles are shared; only the method differs. Agent Platform and Gemini Enterprise block a flagged response instead of returning a de-identified one; Apigee exposes redacted data. **[Documented]**
Detail:
• The Sensitive Data Protection setting is part of the template and applies to whichever method is called; basic `basicConfig.filterEnforcement`, advanced `advancedConfig.inspectTemplate` and optional `deidentifyTemplate` (templates reference, read 2026-10-09) **[Documented]**
• Overview advice is to keep separate templates: "Configure separate Model Armor templates for user prompts and model responses" (overview, read 2026-10-09) **[Documented]**
• Same-location rule: "the Sensitive Data Protection templates must be in the same location as the Model Armor template" (sanitize page, read 2026-10-09) **[Documented]**
• The response-side generated request type takes a general data item for the response (`ModelResponseData *DataItem`), the same type as the prompt side (service.pb.go@37f936ac:2379) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Backing detectors: no detector internals or model identity are given for this filter in Model Armor docs (checked the overview, templates page, product page and REST reference) **[Not disclosed]**
• Filter versions do not apply: "The filter version setting doesn't affect the Sensitive Data Protection and malicious URL filters." (set-filter-version page, read 2026-10-09) **[Documented]**
• Direct REST use: "Model Armor functions only as a detector", so the application decides what to send to the user (integrations page, read 2026-10-09) **[Documented]**
• Overview data flow: "The response (or sanitized response) is sent to you." (overview, read 2026-10-09) **[Documented]**
• Gemini Enterprise Agent Platform route (GA 2025-12-03 per release notes): Model Armor "doesn't pass the de-identified data" back; with INSPECT_AND_BLOCK it blocks the response (Agent Platform integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise route (GA 2025-09-16 per release notes): it "blocks the request or response rather than de-identifying it" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Apigee route: the SanitizeModelResponse policy sits in the response flow, and "If the request or response is redacted, extract the redacted data using flow variables"; GA or Preview is not stated (Apigee integration page, read 2026-10-09) **[Documented]**
• Agent Gateway route (GA 2026-06-24 per release notes): its flow text says responses are allowed or blocked on the verdict, while its intro mentions "block and redact" (Agent Gateway page, read 2026-10-09) **[Documented]**
• Service Extensions route (GKE integration GA 2025-09-15 per release notes): Model Armor tells the networking service to "allow, block, or modify the traffic" (networking page, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers route: configured "Only using floor settings" (integrations page, read 2026-10-09) **[Documented]**
• Status of the MCP route, source conflict (1): release note 2026-04-22 says "Model Armor integration with Google and Google Cloud MCP servers is in General Availability." (release notes, read 2026-10-09) **[Documented]**
• Status of the MCP route, source conflict (2): the floor settings page links it as "Model Armor integration with Google Cloud MCP servers (Preview)" (floor settings page, read 2026-10-09) **[Documented]**
• Pricing: "When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it." (pricing page, read 2026-10-09) **[Documented]**
• Logging caveat: "Enabling logging in a template writes raw prompts and responses to Logging", so an unredacted model response can be stored in logs (logging page, read 2026-10-09) **[Documented]**
• Location support: Sensitive Data Protection is listed in every location row of the supported-features table, including limited-support regions (feature availability page, read 2026-10-09) **[Documented]**
• A self-hosted or offline route is not described (checked the overview, product page, integrations page and client library page) **[Not disclosed]**
### R5
Summary: **Same result shape as for prompts.** The sdp result holds an inspect, de-identify or redact result with execution and match state. Findings carry infoType, likelihood and position, and de-identified text sits in a data field. No numeric score or accuracy figure is published. **[Documented]**
Detail:
• The sdp result holds one of `inspectResult`, `deidentifyResult` or `redactResult` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• `inspectResult` fields include `matchState`, `findings[]` (each with `infoType`, `likelihood`, `location`) and `findingsTruncated` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• `deidentifyResult` fields include `matchState`, `data`, `transformedBytes` and `infoTypes`; the matched value is MATCH_FOUND "if content is de-identified" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• The only de-identify output example is on a prompt: `data.text` "is there anything malicious running on [IP_ADDRESS]?" (sanitize page, read 2026-10-09) **[Documented]**
• Whether the response-side result is identical to the prompt-side result is not shown in an example (checked the sanitize page and REST references) **[Not disclosed]**
• Likelihood values run VERY_UNLIKELY to VERY_LIKELY, with unspecified "same as POSSIBLE"; their meaning is defined by Sensitive Data Protection (SanitizationResult reference, read 2026-10-09) **[Documented]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• Over-limit text returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**
• Transient and quota errors from the detector return "Error occurred while processing sensitive data detection. Please try again." (release note 2026-02-10) **[Documented]**
• Enforcement: INSPECT_ONLY does not block; INSPECT_AND_BLOCK gives a block verdict, and "The calling service or integration point or Policy Enforcement Point (PEP) is responsible for blocking the further processing." (overview, read 2026-10-09) **[Documented]**
• Apigee exposes SanitizeModelResponse flow variables for the sdp inspect and de-identify results, execution state and match state only (Apigee policy reference, read 2026-10-09) **[Documented]**
• Source conflict on shape: the REST reference describes `filterResults` as a keyed map, while the Sensitive Data Protection examples on the sanitize page show an array (SanitizationResult reference and sanitize page, read 2026-10-09) **[Documented]**
• Published detection accuracy or false-positive figures are not given (checked the overview, product page, blog, release notes and best practices) **[Not disclosed]**
### R6
Summary: **Template, location and the response text.** The same template settings, roles and location rule as for prompts apply. The response goes in its own field, optionally with the prompt. Text over 130,000 tokens is skipped, and cross-project use needs two Sensitive Data Protection roles. **[Documented]**
Detail:
• Request: template name in the path, `modelResponseData.text`, optional `userPrompt` and `multiLanguageDetectionMetadata` (sanitizeModelResponse reference, read 2026-10-09) **[Documented]**
• Template settings: basic `--basic-config-filter-enforcement=enabled`, or advanced inspect and optional de-identify template resource names (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Cross-project: "the Model Armor service agent must be granted the DLP User role (roles/dlp.user) and DLP Reader role (roles/dlp.reader)" in the Sensitive Data Protection project (templates page, read 2026-10-09) **[Documented]**
• Cross-project templates: a calling service account in another project needs `roles/modelarmor.user` in the template-hosting project (sanitize page, read 2026-10-09) **[Documented]**
• Token limit: 130,000 for Sensitive Data Protection against 65,536 for the other filters; the limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, read 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project" (quotas page, read 2026-10-09) **[Documented]**
• Language: English plus others depending on the chosen infoTypes (overview, read 2026-10-09) **[Documented]**
• Multi-language detection is available for responses via `multiLanguageDetectionMetadata`; whether it affects this filter is not stated (checked the sanitize page and templates page) **[Not disclosed]**
• Callers use `roles/modelarmor.user`; template managers use `roles/modelarmor.admin` (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers: if the agent and the MCP server are in different projects, floor settings in both projects mean Model Armor is invoked twice (MCP integration page, read 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** the same project, Model Armor API, regional template and roles as the input-level column, with basic or advanced Sensitive Data Protection on. Call the regional response method with model outputs that contain synthetic card numbers, US identifiers or passwords. Advanced mode needs inspect and de-identify templates in the same location. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled, a regional template with the Sensitive Data Protection filter on (basic, or advanced with templates in the same location), `roles/modelarmor.user` for the caller, then POST model outputs to the regional `sanitizeModelResponse` endpoint **[Inferred]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Test data: labelled model responses, written or captured from a model, that contain synthetic sensitive strings, near misses and clean controls; Google gives no labelled test set **[Inferred]**
• Because the documented examples are prompt-side, the first test should confirm that a response containing a known item yields a MATCH_FOUND sdp result and, with a de-identify template, a de-identified copy **[Inferred]**
• Singapore (asia-southeast1) lists Sensitive Data Protection as supported; the basic list names only US national identifiers, so Singapore identifiers need an advanced template **[Inferred]**
• No self-hosted or offline option is documented (checked the overview, product page and integrations page) **[Not disclosed]**
### R8
Summary: **Key open questions.** Whether the basic infoType list applies to responses, what a response-side de-identify result looks like, which integrations can return de-identified output, whether the optional prompt field matters, and what accuracy and latency to expect.
Detail:
• Whether the basic infoType list is the same for responses as for prompts (checked the sanitize page, overview and REST reference; the lists say "scanned in the prompt")
• A real response-side `deidentifyResult` and findings (needs testing; the sanitize page has no such example)
• What the optional `userPrompt` field changes, if anything (checked the REST method reference and sanitize page, not stated)
• Whether Agent Gateway and Service Extensions return de-identified response text, given the "block and redact" and "modify" wording (checked both pages, not stated)
• Whether the Apigee integration is GA or Preview (checked the Apigee integration page and both policy reference pages, not stated)
• Whether the MCP integration is GA (release note 2026-04-22) or Preview (floor settings page label); needs the owner to confirm
• Whether Sensitive Data Protection quota use and latency change when Model Armor calls it (checked quotas, best practices and integrations pages, not stated)
• Whether de-identification is applied when enforcement is Inspect only (needs testing)
• Detection accuracy for the basic detectors on model output (checked the overview, product page, blog and release notes, not stated)
### R9
Summary: Model Armor docs (overview, templates, sanitize, REST references, quotas, integrations, floor settings, logging, release notes), the product and pricing pages, Apigee policy references, and the pinned Google Go client library.
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
• https://docs.cloud.google.com/model-armor/model-armor-langchain-integration
• https://docs.cloud.google.com/model-armor/configure-floor-settings
• https://docs.cloud.google.com/model-armor/set-filter-version
• https://docs.cloud.google.com/model-armor/configure-logging
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go

## Column MA9: Model Armor: Document screening (PDF, CSV, text and Office files)
### R1
Summary: **Screens the text inside uploaded documents.** Model Armor extracts text from supported PDF, CSV, text and Office files and runs the template's filters on it. Only the direct API and the Gemini Enterprise integration accept documents; other integrations take text only. **[Documented]**
Detail:
• Overview: "Model Armor can screen the following types of documents for safety, prompt injection and jailbreak attempts, sensitive data, and malicious URLs" (overview, read 2026-10-09) **[Documented]**
• Overview: "Text extracted from supported files is subject to the token system limits." (overview, read 2026-10-09) **[Documented]**
• The REST modality reference says the text modality will "sanitize text fields, and text extracted from rich text files (like PDFs, DOCs) and plain text files (like TXT)" (templates reference, read 2026-10-09) **[Documented]**
• Vendor blog (supporting only): "Document screening: It can also screen text in documents, including PDFs and Microsoft Office files, for malicious and sensitive content." (Google Cloud blog 2025-10-22, read 2026-10-09) **[Documented]**
• Release note 2025-06-08 lists the Office types: "Model Armor supports screening text in the following document types for malicious content" (release notes, read 2026-10-09) **[Documented]**
• The direct REST API "supports all modalities, including text, documents, and images" (integrations page, read 2026-10-09) **[Documented]**
• In integrations, "only the Gemini Enterprise integration supports documents. All other integrations scan and sanitize only text." (integrations page, read 2026-10-09) **[Documented]**
• Product page: "Detects malicious files, malware, and unsafe URLs within AI prompts and responses." (product page, read 2026-10-09) **[Documented]**
• The REST result schema has a `virusScanFilterResult` type whose scanned content type note reads "PDF Scanning for only PDF is supported." (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Antivirus scanning is covered only in the inventory sheet, not as a Table 3 column; its configuration (a template setting, enable flag or threshold) is not found in the template reference, manage-templates page or overview (checked all three) **[To be verified]**
### R2
Summary: **Threats hidden in documents.** Targets safety violations, prompt injection, sensitive data and malicious URLs in a file's text. Listed types are PDF, CSV, TXT and modern Word, PowerPoint and Excel files. Images embedded in files are not screened, though one Google page says otherwise. **[Documented]**
Detail:
• Overview example: "if a PDF contains an embedded malicious URL, it can be used to compromise any downstream systems processing LLM outputs" (overview, read 2026-10-09) **[Documented]**
• Product page: "Stop embedded threats like indirect prompt injection where safe and legitimate prompts may be contaminated with malicious files and URLs." (product page, read 2026-10-09) **[Documented]**
• Supported types: PDF; CSV; TXT; Word DOCX, DOCM, DOTX, DOTM; PowerPoint PPTX, PPTM, POTX, POTM, POT; Excel XLSX, XLSM, XLTX, XLTM (overview, read 2026-10-09) **[Documented]**
• The REST enum description for Excel reads "XLSX, XLSM, XLTX, XLYM", while the overview and release notes say XLTM (DataItem reference and overview, read 2026-10-09) **[Documented]**
• Older binary Office formats (DOC, XLS, PPT), RTF, HTML, JSON, Markdown and archives are not in the list; no statement that they are rejected or ignored (checked the overview, sanitize page and DataItem reference) **[Not disclosed]**
• Filters that run on the extracted text: safety, prompt injection and jailbreak, sensitive data and malicious URLs, as listed in the overview sentence (overview, read 2026-10-09) **[Documented]**
• Sensitive Data Protection de-identification does not work on files: "Sensitive Data Protection de-identification is not supported for file-based prompts." (sanitize page, read 2026-10-09) **[Documented]**
• Rich documents with metadata labels: release note 2026-04-06 says Model Armor "can sanitize data passed in as rich documents that have specific metadata labels", using a custom metadata-label infoType in an advanced Sensitive Data Protection configuration (release notes, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (1): "Model Armor doesn't screen images embedded within files." (overview, image screening section, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (2): the integrations page says "images embedded in documents aren't screened" for Gemini Enterprise (integrations page, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (3): the Gemini Enterprise page says it screens "Images contained inside other files and documents that you upload directly" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Encoded content is not decoded: Base64, hexadecimal, URL-encoded and ciphertext inputs are not inspected (overview limitations, read 2026-10-09) **[Documented]**
• Audio and video are not supported (overview limitations, read 2026-10-09) **[Documented]**
• Scanned PDFs that hold only page images have no extractable text; whether any OCR is applied is not stated (checked the overview, sanitize page and quotas page) **[Not disclosed]**
### R3
Summary: **A base64 file in the prompt field.** The file goes in a byte item with its type set by hand. The schema lets a response carry a file too, but the docs show no response-side example. The template modality must include text. **[Documented]**
Detail:
• Prompt side: `{"userPromptData":{"byteItem":{"byteDataType":"FILE_TYPE","byteData":"<base64>"}}}` posted to `:sanitizeUserPrompt` (sanitize page, file-based prompts section, read 2026-10-09) **[Documented]**
• "Model Armor doesn't automatically detect the file type. You must explicitly set the byteDataType field to indicate the file format." (sanitize page, read 2026-10-09) **[Documented]**
• Response side: the request field `modelResponseData` has the same data item type as `userPromptData`, which can be text or a byte item (sanitizeModelResponse and DataItem references, read 2026-10-09) **[Documented]**
• The generated Go request type has `ModelResponseData *DataItem`, the same type as the prompt field (service.pb.go@37f936ac:2379) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• No example in the sanitize page sends a document through `modelResponseData`; its response examples are text only (checked the sanitize page, overview and templates page) **[Not disclosed]**
• Whether a document in a model response is accepted, and how an LLM would produce one, is not stated; the overview example of a PDF "processing LLM outputs" is about downstream systems (overview, read 2026-10-09) **[To be verified]**
• Template modality must allow text: `TEXT` "Scans text strings and text embedded in the supported file formats" and an empty `modalities` field scans only text (templates page and templates reference, read 2026-10-09) **[Documented]**
• With a single modality set, the other is skipped: "If you specify a single modality (IMAGE or TEXT), Model Armor skips the other and returns EXECUTION_SKIPPED." So an image-only template should skip documents (sanitize page, read 2026-10-09) **[Inferred]**
• Streaming methods are text only: "Model Armor streaming methods support only textual input, not attachments like images and files." (sanitize page, read 2026-10-09) **[Documented]**
• Gemini Enterprise: the integration "screens the following files only when you upload them to the Gemini Enterprise assistant" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Agent Platform and Agent Gateway pages both say sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported (Agent Platform and Agent Gateway pages, read 2026-10-09) **[Documented]**
• LangChain (Preview): the runnables "are limited to text screening. If a prompt includes a document, the system scans only the extracted text." (LangChain page, read 2026-10-09) **[Documented]**
### R4
Summary: **Text extraction, then the ordinary filters.** Extraction runs inside the managed service on the direct API and Gemini Enterprise routes, and Gemini Enterprise discards a violating file whole. The extractor and its handling of scans and layout are not described. **[Documented]**
Detail:
• Extraction engine, parser identity and handling of tables, headers, comments, hidden text or embedded objects are not described (checked the overview, sanitize page, templates reference, product page and release notes) **[Not disclosed]**
• The generated Go library defines the byte item types as enum values PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT, CSV, PLAINTEXT_UTF8 and IMAGE (service.pb.go@37f936ac:776) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• GA or Preview status for document screening is not labelled on the overview or sanitize pages (checked both and the release notes; the image feature is labelled Preview, documents are not) **[Not disclosed]**
• Gemini Enterprise route (GA 2025-09-16 per release notes): screens PDFs and other documents the user uploads; "If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• "Interactions with custom agents from your organization (such as ADK, A2A, and Dialogflow) are not screened." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise page: "There are no token limits when you use Model Armor with Gemini Enterprise." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise does not de-identify: it blocks the request instead of masking content that triggers a Sensitive Data Protection infoType (integrations page and Gemini Enterprise page, read 2026-10-09) **[Documented]**
• Antivirus: the feature availability page lists "Antivirus scanning" among the filters available in full-support regions and as a column in the by-region table (feature availability page, read 2026-10-09) **[Documented]**
• Release note 2026-04-10 says the antivirus `virusDetails` field no longer includes security vendor names or threat signatures (release notes, read 2026-10-09) **[Documented]**
• Pricing: the pricing page counts "the total number of tokens in AI prompts and responses"; how files and extracted text are counted is not stated (pricing page, read 2026-10-09) **[Not disclosed]**
• Data handling: core data "includes prompts, responses, and input files", processed but not stored at rest (data residency page, read 2026-10-09) **[Documented]**
• Self-hosted or offline document screening is not described (checked the overview, product page and integrations page) **[Not disclosed]**
### R5
Summary: **The standard verdict, with limited location detail.** Output is the usual per-filter result. Malicious URL positions exist only for plain text, oversize files are skipped and files under 69 bytes are rejected. No score or accuracy figure is published. **[Documented]**
Detail:
• Output is the normal `sanitizationResult` with `filterMatchState`, `invocationResult` and per-filter results (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Malicious URL locations: "The locations field is supported only for plaintext content i.e. ByteItemType.PLAINTEXT_UTF8" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Sensitive data positions: "when the content is not textual, this references the UTF-8 encoded textual representation of the content" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Finding containers: "The top level name is the source file name or table name." (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Optional `fileLabel` on the byte item is "used to identify the file in the response" (DataItem reference, read 2026-10-09) **[Documented]**
• Which response field returns the file label is not shown (checked the SanitizationResult reference and sanitize page) **[Not disclosed]**
• Oversize file: "If a file exceeds this limit, Model Armor skips scanning the file." (overview, read 2026-10-09) **[Documented]**
• The result code or message returned for a skipped oversize file is not stated (checked the overview, quotas page and SanitizationResult reference) **[Not disclosed]**
• Tiny file: requests for files under 69 bytes are rejected with an `InvalidDocumentInputException` error (overview and quotas page, read 2026-10-09) **[Documented]**
• Token overflow in extracted text: the filter returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**
• Gemini Enterprise acts on the verdict by discarding the whole file (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Antivirus result fields: `matchState`, `scannedContentType` (UNKNOWN, PLAINTEXT, PDF), `virusDetails`, `scannedSize` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• Published extraction accuracy or detection rates for documents are not given (checked the overview, product page, blog and release notes) **[Not disclosed]**
### R6
Summary: **Base64 bytes, a stated type and a 4 MB cap.** The byte data type must be set; files under 69 bytes fail and files over 4 MB are skipped. Extracted text counts against the filter token limits. Callers need the user role. **[Documented]**
Detail:
• `byteDataType` is required; the sanitize page lists PLAINTEXT_UTF8, PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT and CSV, and "If the field is missing or not specified, the request fails." (sanitize page, read 2026-10-09) **[Documented]**
• The REST enum adds IMAGE and maps WORD_DOCUMENT to DOCX, DOCM, DOTX, DOTM; EXCEL_DOCUMENT to XLSX, XLSM, XLTX; POWERPOINT_DOCUMENT to PPTX, PPTM, POTX, POTM, POT (DataItem reference, read 2026-10-09) **[Documented]**
• Size: "Supported files are limited to 4 MB in size." and the system limit table gives 4 MB for "All supported files and images" (overview and quotas page, read 2026-10-09) **[Documented]**
• Release note 2025-09-27: "Model Armor limits the maximum input size for files and text to 4 MB, automatically skipping any content that exceeds this threshold." (release notes, read 2026-10-09) **[Documented]**
• Minimum size: files under 69 bytes are rejected "because such files are highly likely to be invalid" (overview, read 2026-10-09) **[Documented]**
• Token limits on extracted text: 65,536 for prompt injection, responsible AI and CSAM, 130,000 for Sensitive Data Protection, no limit in the Gemini Enterprise integration (quotas page, read 2026-10-09) **[Documented]**
• Malicious URL detection "scans only the first 256 URLs found in prompts and responses" (overview, read 2026-10-09) **[Documented]**
• Example command: `base64 -w 0 -i sample.pdf` piped into `jq` to build the JSON body (sanitize page, read 2026-10-09) **[Documented]**
• Roles: `roles/modelarmor.user` to sanitize; `roles/modelarmor.admin` to manage templates (sanitize page, read 2026-10-09) **[Documented]**
• Quota: 1,200 queries per minute per project; each file is one request (quotas page, read 2026-10-09) **[Documented]**
• The template's `modalities` field is optional; empty means text only (templates reference, read 2026-10-09) **[Documented]**
• Regional limits for documents are not stated separately; the by-region table lists filter, multi-language, CSAM, image and antivirus support, not documents (checked the feature availability page) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a project with the Model Armor API enabled, a template in a full-support region with the wanted filters, the user role, and base64 test files of each type. Use files of 69 bytes to 4 MB with planted injection text, fake sensitive data and test URLs, then call the prompt method. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing and the Model Armor API enabled, a regional template with the filters you want to test (use a full-support region such as `us-central1` or the `us` multi-region, because limited-support regions drop some filters), `roles/modelarmor.user`, and base64-encoded files posted with `byteDataType` set to the file format **[Inferred]**
• Test files: one clean and one planted file per type (PDF, DOCX, XLSX, PPTX, CSV, TXT), with prompt-injection text, fake card numbers or SSNs, and a safe test URL; plus boundary files just under 69 bytes, around 4 MB, and a file with an embedded image **[Inferred]**
• Singapore (asia-southeast1) lists no malicious URL filter with data residency enforced, so URL tests there need the template's data residency enforcement turned off (feature availability page and release notes 2026-08-27, read 2026-10-09) **[Documented]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Response-side document tests are exploratory because the docs show no example **[Inferred]**
• No self-hosted or offline option is documented (checked the overview, product page and integrations page) **[Not disclosed]**
### R8
Summary: **Key open questions.** Whether responses can carry documents, what the extractor does with scans and layout, what a skipped oversize file returns, whether embedded images are screened, how antivirus is configured, and what accuracy to expect.
Detail:
• Whether a model response can be sent as a file in `modelResponseData` (schema allows it; checked the sanitize page, overview, REST references and release notes, no example)
• The text extractor: scanned or image-only PDFs, tables, hidden text, comments, password-protected and corrupt files (checked the overview, quotas page and sanitize page, not stated)
• What the API returns for a file over 4 MB: an error, or a skipped filter result and which one (checked the overview and quotas page, not stated)
• Embedded images in files: not screened per the overview, screened per the Gemini Enterprise page (needs testing in both routes)
• Antivirus: configuration, supported file types beyond PDF, and whether it runs on documents sent through the REST API (checked the REST references, overview, manage-templates and release notes; only the result type, region table and 2026-04-10 note exist)
• Whether the Gemini Enterprise integration lists documents only (integrations table) or documents and images (Gemini Enterprise page)
• How files and extracted text are billed in tokens (checked the pricing page, not stated)
• Older Office formats and other file types: ignored, rejected or failed (needs testing)
• Whether the rich-document metadata-label feature needs special request fields beyond a custom infoType in an advanced Sensitive Data Protection template (checked the release note only)
• Whether LangChain's "scans only the extracted text" means document support or only text extracted client-side (checked the LangChain page, not stated)
• Whether filters report which page or sheet matched (checked the SanitizationResult reference; only character ranges and a container name)
### R9
Summary: Model Armor docs (overview, sanitize, templates, quotas, integrations, release notes, REST references, data residency, feature availability), the product and pricing pages, the Google Cloud blog, and the pinned Google Go client library.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
• https://docs.cloud.google.com/model-armor/model-armor-langchain-integration
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/data-residency
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse
• https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go

## Column MA10: Model Armor: Image screening with OCR and visual scanning
### R1
Summary: **Screens images by reading text and scanning visuals.** One JPEG, PNG or BMP image is checked by text extraction (OCR) and, with an advanced Sensitive Data Protection template, by visual scanning; a redacted image can come back. Preview, us and eu multi-regions only. **[Documented]**
Detail:
• Overview: "Model Armor screens images provided in the prompts and responses to help protect your generative AI applications from risks embedded within images." (overview, read 2026-10-09) **[Documented]**
• Method 1: "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." (overview, read 2026-10-09) **[Documented]**
• Method 2: "Optical character recognition (OCR): Screens the text within images." (overview, read 2026-10-09) **[Documented]**
• The REST modality reference says the image modality "will sanitize image files. The visual content and the text content in the image will be sanitized depending on the filter configuration." (templates reference, read 2026-10-09) **[Documented]**
• The overview and templates pages label the feature Preview, subject to the Pre-GA terms (overview and templates page, read 2026-10-09) **[Documented]**
• Release note 2026-06-25: "Model Armor supports screening images within prompts and responses." and the feature is in Preview (release notes, read 2026-10-09) **[Documented]**
• Release note 2026-07-01 added modality selection (text, images or both) in the console, also in Preview (release notes, read 2026-10-09) **[Documented]**
• Overview use case: "Inspect visual content and text within images to detect embedded threats, sensitive information types (infoTypes), or policy violations." (overview, read 2026-10-09) **[Documented]**
• Sensitive Data Protection is a separate Google Cloud service; what its image detectors and redaction transformations can do is covered in the Sensitive Data Protection columns on sheet 3, and this column covers how Model Armor invokes them. The premise is that Model Armor docs only describe the call **[Inferred]**
### R2
Summary: **Sensitive content and text inside images.** Documented targets are embedded threats, infoType matches and policy violations in an image's pixels or its text. Only three formats are listed. The overview excludes images inside files, text-plus-image prompts, audio and video. **[Documented]**
Detail:
• Overview use case lists "embedded threats, sensitive information types (infoTypes), or policy violations" in "visual content and text within images" (overview, read 2026-10-09) **[Documented]**
• What visual scanning can find is set by the customer's Sensitive Data Protection inspect template, since the visual route uses only the advanced filter and that filter takes its detectors from the template (see the Sensitive Data Protection columns) **[Inferred]**
• Because visual scanning is limited to that filter, safety, prompt injection and malicious URL checks probably run only on OCR text, not on pixels. The premise is the word "only" in the overview **[Inferred]**
• Which filters examine the OCR text is not listed (checked the overview, templates page, sanitize page and REST references; the REST note says "depending on the filter configuration") **[Not disclosed]**
• Formats: "Model Armor screens images only in the JPEG, PNG, and BMP formats." (overview, read 2026-10-09) **[Documented]**
• Other formats (GIF, WebP, TIFF, HEIC, SVG) are not listed as supported or rejected (checked the overview, sanitize page and DataItem reference) **[Not disclosed]**
• Source conflict on embedded images (1): "Model Armor doesn't screen images embedded within files." (overview, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (2): the Gemini Enterprise page says the integration screens "Images contained inside other files and documents that you upload directly" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• "Model Armor doesn't support prompts that combine text and images in a single request." (overview, read 2026-10-09) **[Documented]**
• "Model Armor doesn't support audio or video." (overview, read 2026-10-09) **[Documented]**
• Supported languages for OCR text are not stated; the text filters are tested on nine languages (checked the overview language section, not tied to images) **[Not disclosed]**
• Whether the CSAM filter analyses image pixels is not stated; the image example output includes a CSAM result but the page does not explain it (checked the overview and sanitize page) **[Not disclosed]**
### R3
Summary: **One base64 image in the prompt field.** The image goes in a byte item typed IMAGE, in a template with image modality, at a us or eu endpoint. Docs say responses are screened too but show no response example. Text-plus-image requests are unsupported. **[Documented]**
Detail:
• Prompt side: `{"userPromptData": {"byteItem": {"byteDataType": "IMAGE", "byteData": "<base64>"}}}` posted to `:sanitizeUserPrompt` (sanitize page, prompts containing images section, read 2026-10-09) **[Documented]**
• "You must explicitly set the byteDataType field to IMAGE and provide the base64-encoded image in the supported format in the byteData field." (sanitize page, read 2026-10-09) **[Documented]**
• Response side, docs wording: the overview says Model Armor screens images provided "in the prompts and responses" (overview, read 2026-10-09) **[Documented]**
• Response side, release note 2026-06-25: "Model Armor supports screening images within prompts and responses." (release notes, read 2026-10-09) **[Documented]**
• Response side, schema: `modelResponseData` is a data item that can hold a byte item, and `IMAGE` is a byte item type (sanitizeModelResponse and DataItem references, read 2026-10-09) **[Documented]**
• Response side, code: the generated Go types give `SanitizeModelResponseRequest.ModelResponseData` as `*DataItem` and define `ByteDataItem_IMAGE` (service.pb.go@37f936ac:2379 and :792) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• The overview limitations name both methods: "Model Armor doesn't screen images provided along with text in prompts and responses if you're using the SanitizeUserPrompt and SanitizeModelResponse methods." (overview, read 2026-10-09) **[Documented]**
• No page shows a request body that sends an image through `modelResponseData` (checked the sanitize page, overview, templates page and release notes) **[To be verified]**
• Template modality: "To enable image screening, set the modality in the template metadata." (sanitize page, read 2026-10-09) **[Documented]**
• An empty `modalities` field scans text only (templates reference, read 2026-10-09) **[Documented]**
• With one modality set, the other is skipped: "Model Armor skips the other and returns EXECUTION_SKIPPED." (sanitize page, read 2026-10-09) **[Documented]**
• Regions: "Image screening is supported only in the us and eu multi-regions." (overview, read 2026-10-09) **[Documented]**
• An image sent to a regional endpoint without image screening gives `invocation_result` FAILURE (overview, read 2026-10-09) **[Documented]**
• Streaming: "Model Armor streaming methods support only textual input, not attachments like images and files." (sanitize page, read 2026-10-09) **[Documented]**
• Integrations, source conflict (1): the Gemini Enterprise page says it screens "Images that you upload directly" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Integrations, source conflict (2): the integrations options table lists the Gemini Enterprise integration's supported modalities as "Text, documents" with no images (integrations page, read 2026-10-09) **[Documented]**
• The Agent Platform page says "Sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported", and the integrations page says every integration other than Gemini Enterprise scans only text (Agent Platform page and integrations page, read 2026-10-09) **[Documented]**
### R4
Summary: **OCR plus advanced Sensitive Data Protection, in Preview.** The service reads image text and uses your inspect template for visuals; redaction needs a de-identify template with image redaction. The OCR engine is not disclosed. Images run only in the us and eu multi-regions. **[Documented]**
Detail:
• OCR engine, image models, resolution handling and how OCR text is passed to other filters are not described (checked the overview, templates page, product page, sanitize page, release notes and blog) **[Not disclosed]**
• Visual scanning relies on the advanced Sensitive Data Protection setting, so an inspect template in the same location as the Model Armor template is needed (overview and sanitize page, read 2026-10-09) **[Documented]**
• Redaction: "Model Armor redacts images only if you configured Model Armor filters with a Sensitive Data Protection inspect template and a Sensitive Data Protection de-identify template." (sanitize page, read 2026-10-09) **[Documented]**
• "Make sure that you configure image redaction in the de-identify template." (sanitize page, read 2026-10-09) **[Documented]**
• Console note: "Only us and eu multi-regions support image modality." (templates page, read 2026-10-09) **[Documented]**
• Disabling data residency enforcement "enables all Model Armor features except for image modality, which remains restricted to the us and eu multi-regions" (templates page, read 2026-10-09) **[Documented]**
• The supported-features table shows image support as Yes only for `eu` and `us`; Singapore (asia-southeast1) and every other regional row show No (feature availability page, read 2026-10-09) **[Documented]**
• Serving route: the direct REST API supports "all modalities, including text, documents, and images" (integrations page, read 2026-10-09) **[Documented]**
• Gemini Enterprise integration (GA 2025-09-16 per release notes): its own page says it screens images uploaded to the assistant (Gemini Enterprise integration page and release notes, read 2026-10-09) **[Documented]**
• The Go library pins the `Modality` enum values MODALITY_UNSPECIFIED, MODALITY_TEXT and MODALITY_IMAGE (service.pb.go@37f936ac:454) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Pricing counts tokens, defined as "four characters (using UTF-8 code points) per token excluding white space"; how an image is counted is not stated (pricing page, read 2026-10-09) **[Not disclosed]**
• Sensitive Data Protection use inside Model Armor carries no extra charge (pricing page, read 2026-10-09) **[Documented]**
• Data handling: images are processed in memory with no durable storage unless Cloud Logging is enabled (overview, read 2026-10-09) **[Documented]**
• Self-hosted or offline image screening is not described (checked the overview, product page and integrations page) **[Not disclosed]**
### R5
Summary: **Match state, extracted text and an optional redacted image.** Results come as inspect or redact results with execution and match state. A redact result can carry the redacted image, findings with pixel boxes and the extracted text. No score or accuracy figure is published. **[Documented]**
Detail:
• The sdp result holds `inspectResult` or `redactResult` for images; the redact result is "primarily used for image redaction" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• `inspectResult` includes `extractedImageText` ("Contains text extracted from the image, if applicable") (SanitizationResult reference, read 2026-10-09) **[Documented]**
• `redactResult` fields: `executionState`, `messageItems`, `matchState`, `redactedImage`, `findings[]`, `extractedImageText`; match is MATCH_FOUND "if content is redacted" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• The redacted image is "Output only. The redacted image. The type will be the same as the original image." and is a base64-encoded string (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Findings carry `infoType`, `likelihood` and `location.contentLocations[].imageFindingLocation` with pixel boxes `top`, `left`, `width`, `height`; "(0,0) is upper left" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Redact-result findings are "populated in the response only when include_findings in the SDP template is set to true" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• The generated Go library carries the same comment on the redact result findings (service.pb.go@37f936ac:3586) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Source conflict on box shape (1): the REST reference gives `imageFindingLocation.boundingBoxes[]`, a list (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Source conflict on box shape (2): the sanitize page example shows a single `boundingBox` object with top 16, left 121, width 620, height 90 (sanitize page, read 2026-10-09) **[Documented]**
• The redaction example shows `redactedImage` as the placeholder "[REDACTED_IMAGE]", an infoType EMAIL_ADDRESS and likelihood LIKELY, so it shows no real image bytes (sanitize page, read 2026-10-09) **[Documented]**
• Image prompt example: a prompt image returns `filterMatchState` MATCH_FOUND with CSAM no match and sdp `inspectResult` MATCH_FOUND, and no other filters shown (sanitize page, read 2026-10-09) **[Documented]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• OCR accuracy, visual detection rates and false-positive figures are not given (checked the overview, product page, blog, release notes and best practices) **[Not disclosed]**
### R6
Summary: **Base64 image, 4 MB cap, one image per call.** The type must be IMAGE and the format JPEG, PNG or BMP. The template needs image modality, a us or eu location and, for visual scanning, an advanced template; redaction needs a de-identify template. **[Documented]**
Detail:
• Formats and size: JPEG, PNG and BMP; "Each image must be 4 MB or smaller." (overview, read 2026-10-09) **[Documented]**
• Oversize behaviour: "If a file or image exceeds this limit, Model Armor skips scanning it." (quotas page, read 2026-10-09) **[Documented]**
• "Model Armor screens only a single image per request." and multiple images at a time are unsupported with the two sanitize methods (overview, read 2026-10-09) **[Documented]**
• Template field `modalities` (Preview): `MODALITY_IMAGE`, `MODALITY_TEXT`, or both; "If empty, only text modality will be scanned." (templates reference, read 2026-10-09) **[Documented]**
• Console: "Select modality to specify whether you want to screen text, images, or both", and the field is disabled in regions other than us and eu (templates page, read 2026-10-09) **[Documented]**
• Image requests therefore go to a us or eu endpoint, for example `modelarmor.us.rep.googleapis.com` or `modelarmor.eu.rep.googleapis.com`, built from the documented `modelarmor.LOCATION.rep.googleapis.com` pattern (templates page, read 2026-10-09) **[Inferred]**
• Advanced Sensitive Data Protection settings: `inspectTemplate` and, for redaction, `deidentifyTemplate`, in the same location as the Model Armor template (sanitize page, read 2026-10-09) **[Documented]**
• Cross-project use needs `roles/dlp.user` and `roles/dlp.reader` for the Model Armor service agent in the project holding the Sensitive Data Protection templates (templates page, read 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project" (quotas page, read 2026-10-09) **[Documented]**
• How image content counts against token limits is not stated (checked the quotas page, overview and pricing page) **[Not disclosed]**
• Callers need `roles/modelarmor.user`; template managers need `roles/modelarmor.admin` (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Language handling for OCR text and for text-in-image is not stated (checked the overview and sanitize page) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a project with the Model Armor API enabled, a template in the us or eu multi-region with image modality and advanced Sensitive Data Protection, plus the user role. For redaction add a de-identify template with image redaction. Send base64 test images containing fake sensitive text. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing and the Model Armor API enabled, `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call it, a template in `us` or `eu` with `modalities` including `MODALITY_IMAGE`, an advanced Sensitive Data Protection inspect template in the same location (and a de-identify template with image redaction to test redaction), then POST a base64 JPEG, PNG or BMP of up to 4 MB with `byteDataType` IMAGE **[Inferred]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Test images: synthetic screenshots, scans and photos containing fake card numbers or identifiers, injected instruction text, and clean controls; also edge cases at 4 MB, in other formats and with several images **[Inferred]**
• Singapore (asia-southeast1) cannot be used for images because image support is "No" there; a Singapore-based tester must call a us or eu endpoint, which sends the image across jurisdictions **[Inferred]**
• Response-side image tests are exploratory because the docs show no response example **[Inferred]**
• No self-hosted or offline option is documented (checked the overview, product page and integrations page) **[Not disclosed]**
### R8
Summary: **Key open questions.** Whether responses can carry images, which filters examine OCR text, OCR language coverage, how images are billed, whether other formats work, what the redacted image looks like, and why box fields differ between pages.
Detail:
• Whether an image in `modelResponseData` works (schema, code and docs wording say it should; checked the sanitize page, overview, templates page and release notes, no example)
• Which filters run on OCR text: safety, prompt injection, malicious URL, sensitive data (needs testing; REST note says "depending on the filter configuration")
• Whether the CSAM filter looks at pixels (checked the overview and sanitize page, not stated)
• OCR languages and handwriting, rotated or low-resolution text (checked the overview and sanitize page, not stated)
• Whether GIF, WebP, TIFF or animated images are rejected or ignored (needs testing)
• How an image is counted for the token limits, quotas and billing (checked the pricing, quotas and overview pages, not stated)
• Whether `include_findings` in the Sensitive Data Protection template must be set for findings, and where it is set (checked the SanitizationResult reference and Go comments, not explained)
• Whether `redactedImage` is returned when enforcement is Inspect only (needs testing)
• Box field name: `boundingBox` in the sanitize page example against `boundingBoxes` list in the REST reference (needs testing)
• Embedded images in documents: not screened per the overview, screened per the Gemini Enterprise page (needs testing)
• Why the integrations table lists Gemini Enterprise as text and documents while its own page covers images (checked both pages, not reconciled)
• When image screening reaches GA and other regions (checked release notes, no date given)
### R9
Summary: Model Armor docs (overview, sanitize, templates, quotas, integrations, release notes, REST references, feature availability), the pricing page, and the pinned Google Go client library.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse
• https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://cloud.google.com/security-command-center/pricing
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go
