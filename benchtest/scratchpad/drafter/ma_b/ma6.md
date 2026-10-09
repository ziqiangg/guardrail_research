
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
• Files: "Sensitive Data Protection de-identification is not supported for file-based prompts." The page says prompts; it shows no response-side file example (sanitize page, read 2026-10-09) **[Documented]**
• Agent Platform route covers the `generateContent` method only; Model Armor "intercepts responses before your application receives them" (Agent Platform integration page, read 2026-10-09) **[Documented]**
• Agent Gateway egress: Model Armor screens "the response payload" and also covers MCP, OpenAI-format and A2A payloads (Agent Gateway page, read 2026-10-09) **[Documented]**
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
• Agent Gateway route (GA 2026-06-24 per release notes) and Service Extensions route (GKE integration GA 2025-09-15): both can "block and redact" or "modify" traffic by their own wording, but neither page says how a de-identified response is returned (Agent Gateway and networking pages, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers route: floor settings only, no templates; release note 2026-04-22 says GA, while the floor settings page still labels it "(Preview)" (release notes and floor settings page, read 2026-10-09) **[Documented]**
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
• Enforcement: INSPECT_ONLY does not block; INSPECT_AND_BLOCK gives a block verdict that "the calling service or integration point or Policy Enforcement Point (PEP) is responsible for" acting on (overview, read 2026-10-09) **[Documented]**
• Apigee exposes SanitizeModelResponse flow variables for the sdp inspect and de-identify results, execution state and match state only (Apigee policy reference, read 2026-10-09) **[Documented]**
• Source conflict on shape: the REST reference describes `filterResults` as a keyed map, while the Sensitive Data Protection examples on the sanitize page show an array (SanitizationResult reference and sanitize page, read 2026-10-09) **[Documented]**
• Published detection accuracy or false-positive figures are not given (checked the overview, product page, blog, release notes and best practices) **[Not disclosed]**
### R6
Summary: **Template, location and the response text.** The same template settings, roles and location rule as for prompts apply. The response goes in its own field, optionally with the prompt. Text over 130,000 tokens is skipped, and cross-project use needs two Sensitive Data Protection roles. **[Documented]**
Detail:
• Request: template name in the path, `modelResponseData.text`, optional `userPrompt` and `multiLanguageDetectionMetadata` (sanitizeModelResponse reference, read 2026-10-09) **[Documented]**
• Template settings: basic `--basic-config-filter-enforcement=enabled`, or advanced inspect and optional de-identify template resource names (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Cross-project: "the Model Armor service agent must be granted the DLP User role (roles/dlp.user) and DLP Reader role (roles/dlp.reader)" in the Sensitive Data Protection project (templates page, read 2026-10-09) **[Documented]**
• Cross-project templates for responses: a service account in another project needs `roles/modelarmor.user` in the template project; Sensitive Data Protection templates can sit in the same central project (sanitize page, read 2026-10-09) **[Documented]**
• Token limit: 130,000 for Sensitive Data Protection against 65,536 for the other filters; the limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, read 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project" (quotas page, read 2026-10-09) **[Documented]**
• Language: English plus others depending on the chosen infoTypes (overview, read 2026-10-09) **[Documented]**
• Multi-language detection is available for responses via `multiLanguageDetectionMetadata`; whether it affects this filter is not stated (checked the sanitize page and templates page) **[Not disclosed]**
• The documented IAM roles for callers are `roles/modelarmor.user` and, for template managers, `roles/modelarmor.admin` (sanitize page and templates page, read 2026-10-09) **[Documented]**
• Google and Google Cloud MCP servers: configured only through floor settings; cross-project setups can run Model Armor twice (MCP integration page, read 2026-10-09) **[Documented]**
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
• Whether Agent Gateway and Service Extensions return de-identified response text, given the "redact" and "modify" wording (checked both pages, not stated)
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
