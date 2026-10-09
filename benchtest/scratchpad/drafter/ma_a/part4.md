## Column MA4: Model Armor: Output-level prompt injection and jailbreak detection
### R1
Summary: **Output-level prompt injection and jailbreak detection.** The overview, a sample response output and the Apigee response policy all show the filter running on model responses. The templates page describes it for prompts only. The calling service enforces any block. **[Documented]**
Detail:
• Overview: "When prompt injection and jailbreak detection is enabled, Model Armor scans prompts and responses for malicious content. If detected, Model Armor blocks the prompt or response." (overview, 2026-10-09) **[Documented]**
• Templates page describes the check for prompts only: "Detects malicious content and jailbreak attempts in a prompt." (templates page, 2026-10-09) **[Documented]**
• The `sanitizeModelResponse` sample output on the sanitize page includes a `pi_and_jailbreak` result with `piAndJailbreakFilterResult`, `EXECUTION_SUCCESS` and `NO_MATCH_FOUND` (sanitize page, 2026-10-09) **[Documented]**
• The Apigee `SanitizeModelResponse` policy sets `piAndJailbreakFilterResult.matchState`, `promptInjectionDetected` and `promptInjectionConfidence` (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**
• Taken together, the overview, the sample output and the Apigee variables show the filter runs on responses; the templates page wording is narrower, and the docs do not say which reading is intended **[Inferred]**
• A positive detection on a model response: no example in the docs (checked the sanitize page response examples, which show `NO_MATCH_FOUND` for this filter) **[Not disclosed]**
• Configured in a template under `filterConfig.piAndJailbreakFilterSettings` with `filterEnforcement` (`ENABLED` or `DISABLED`; unspecified is "Same as Disabled") and `confidenceLevel`; the template does not mark filters as input or output (REST templates ref, 2026-10-09) **[Documented]**
• The service returns a verdict and the caller acts on it: "The calling service or integration point or Policy Enforcement Point (PEP) is responsible for blocking the further processing." (overview, 2026-10-09) **[Documented]**
### R2
Summary: **Injection payloads and jailbreak output arriving from the model side.** The docs name MCP tool results as a target for injection by malicious tool authors and describe indirect injection through files and URLs. **[Documented]**
Detail:
• Overview definitions apply to both sides: prompt injection is "a security vulnerability where attackers craft special commands within the text input (the prompt) to trick an AI model" and jailbreaking is "the act of bypassing the safety protocols and ethical guidelines that are built into the model" (overview, 2026-10-09) **[Documented]**
• MCP: Model Armor sanitizes `tools/call` responses, `prompts/get` responses and "MCP tool execution errors (target for prompt injection by malicious MCP tools authors)" (MCP page, Agent Gateway page, 2026-10-09) **[Documented]**
• Product page: the service helps "Stop embedded threats like indirect prompt injection where safe and legitimate prompts may be contaminated with malicious files and URLs" (product page, marketing text, 2026-10-09) **[Documented]**
• Release note 2026-10-10 (entry dated 2026-10-10 present on 2026-10-09): enhanced prompt injection and jailbreak protection "when screening Workspace content, such as emails, documents, and files", on the us and eu multi-regions with filter version v3 or later (release notes, 2026-10-09) **[Documented]**
• Release note 2025-09-23 lists vectors with improved detection in the upgraded model: "Do Anything Now prompts", "System instruction manipulation", "Unauthorized action execution" and "Sensitive information retrieval"; the note does not say whether this applies to responses (release notes, 2026-10-09) **[Documented]**
• What response-side detection means (a response that carries an injection aimed at a downstream agent, or a response that shows the model was jailbroken): not defined (checked overview, templates page, product page, MCP page, REST references, blog) **[Not disclosed]**
• System-prompt leakage detection on responses: none described; the docs' sample attack "reveal your system prompt" is treated as an input attack (checked the overview filter list, templates page detection list, REST `FilterConfig`, product page features and blog capabilities) **[Not disclosed]**
• The overview's output-template focus on "leaking sensitive data" maps to Sensitive Data Protection, not to a system-prompt leakage check (columns MA5 and MA6) **[Inferred]**
• Languages tested: Chinese (Mandarin), English, French, German, Italian, Japanese, Korean, Portuguese and Spanish; "These filters can work in many other languages, but the quality of results might vary." (overview, 2026-10-09) **[Documented]**
• In asia-south1 and northamerica-northeast2, "if you send non-English content to detectors like prompt injection and jailbreak or RAI, Model Armor returns a verdict of Skipped Detection for those specific checks" (sanitize page, 2026-10-09) **[Documented]**
• Model Armor "doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext" and "doesn't support audio or video" (overview, Limitations, 2026-10-09) **[Documented]**
• Each response is inspected "independently as a single-turn request"; Model Armor "doesn't track conversation history or maintain context across multi-turn interactions" (overview, Limitations, 2026-10-09) **[Documented]**
• Template-specific exclusion rules (Preview) also apply to model responses (exclusion rules page, sanitize page, 2026-10-09) **[Documented]**
### R3
Summary: **The model response or tool output, sent on its own.** The caller posts it to the sanitize-model-response method of a regional endpoint, or a gateway or floor setting does so inline. For MCP, Google advises enabling the filter only where traffic carries natural language. **[Documented]**
Detail:
• Method and field: `POST https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeModelResponse` with body `{"modelResponseData":{"text":"..."}}` (sanitize page, 2026-10-09) **[Documented]**
• Streaming variant `StreamSanitizeModelResponse`: "Streams and sanitizes LLM-generated text"; buffered or real-time mode; text only (sanitize page, 2026-10-09) **[Documented]**
• The docs examples for the response method send the response text alone (sanitize page, 2026-10-09) **[Documented]**
• The Go client request struct for the response method has an optional `UserPrompt` field, commented "User Prompt associated with Model response." (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:2380-2381) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Whether any filter uses that prompt as context (checked the sanitize page, the REST template reference, the overview and the Go client comments; none says) **[Not disclosed]**
• MCP tip: "Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data." (MCP page, 2026-10-09) **[Documented]**
• MCP payloads sanitized: `tools/call` request and response, `prompts/get` request and response, and MCP tool execution errors; `tools/list`, `resources/*`, `notifications/*`, Streamable HTTP/SSE and MCP protocol errors are allowed without sanitization (MCP page, 2026-10-09) **[Documented]**
• Agent Gateway egress: "Model Armor screens the response payload, and Agent Gateway either allows it to reach the agent or blocks it"; A2A `SendMessage` payloads are sanitized while `SendStreamingMessage` is allowed without sanitization; for OpenAI-protocol traffic the page lists chat completions and responses (non-streaming variants only) and says payloads not listed are allowed without sanitization (Agent Gateway page, 2026-10-09) **[Documented]**
• Agent Gateway ingress: replies from agents built with the Agent Development Kit are screened; LangChain payloads are not sent to Model Armor (Agent Gateway page, 2026-10-09) **[Documented]**
• Retrieved and intermediate text: the Gemini Enterprise, Agent Runtime and Apigee integrations also sanitize "intermediate steps, such as grounding data and responses returned by web search tools" (integrations page, 2026-10-09) **[Documented]**
• Routes that run this filter on responses (docs pages named in each item, 2026-10-09) **[Documented]**
  – Agent Platform `generateContent`: `responseTemplateName` in the request or project floor settings; no documents or images (Agent Platform page)
  – Apigee: `SanitizeModelResponse` policy added to the response flow (Apigee page)
  – Gemini Enterprise: assistant outputs screened through templates; custom agents (ADK, A2A, Dialogflow) are not screened (Gemini Enterprise page)
  – Service Extensions on load balancers, GKE Inference Gateway and Secure Web Proxy (networking page)
  – LangChain `ModelArmorSanitizeResponseRunnable` (Preview) (LangChain page)
• Text extracted from documents is screened for prompt injection; file handling is in column MA9 (overview, Document screening, 2026-10-09) **[Documented]**
### R4
Summary: **Managed Google Cloud service; model not disclosed.** The filter is a numbered, versioned component of a template-driven regional API. Release notes record model updates in 2025 and 2026, but Google names no model, training data or architecture. **[Not disclosed]**
Detail:
• Model Armor is "a Google Cloud service"; callers use a REST API on regional endpoints (`modelarmor.LOCATION.rep.googleapis.com`) and a template; "The global endpoint (modelarmor.googleapis.com) doesn't support" template management or sanitizing (templates page, overview, 2026-10-09) **[Documented]**
• Generic product-page description: "combines rules-based controls, ML models, and powerful AI reasoning models"; no per-filter mapping is given (product page, 2026-10-09) **[Documented]**
• Backing model, architecture, training data and whether the response-side filter is the same model as the prompt-side filter (checked overview, product page, filter version pages, release notes, REST references, blog, best practices) **[Not disclosed]**
• Filter versions: one version per template, chosen by number or alias (Latest, Stable, Legacy, Retired); "You can't specify different versions for individual filters" (filter version page, 2026-10-09) **[Documented]**
• Version timeline: v1 2025-01-30 (Legacy), v2 2025-06-19 (Legacy), v3 2026-05-25 (Stable), v4 2026-09-18 (Latest) (filter version page, 2026-10-09) **[Documented]**
• Update history for this filter, dates only (release notes and version history, 2026-10-09) **[Documented]**
  – 2025-03-21: filter "upgraded with increased efficacy and higher model quality scores"
  – 2025-06-19: flags more threats across attack vectors, available in us-east1
  – 2025-09-23: upgraded model in the EU multi-region
  – 2026-01-30: upgraded in asia-south1 and asia-southeast1
  – 2026-03-31: improved to reduce false positives and false negatives
  – 2026-05-25: v3 "uses a new model" with fewer false positives
  – 2026-06-16 and 2026-06-22: v3 filter available in asia-south1, northamerica-northeast2 and asia-southeast1
  – 2026-09-18: v4 minor updates to address reported false positives
• The release notes do not say whether these updates apply to responses as well as prompts (checked the entries above) **[Not disclosed]**
• Legacy versions v1 and v2 retire on 2026-12-17 (filter version page; release note 2026-09-18) **[Documented]**
• An earlier release note (2026-09-02) gave 2026-11-29 for the same retirement; the later note and the version page supersede it (release notes, 2026-10-09) **[Documented]**
• In asia-southeast1 the template-version table lists v1 (Legacy), v3 (Stable) and v4 (Latest) (filter version page, 2026-10-09) **[Documented]**
• The Go client at v1.3.0 has no field for filter versions or exclusion-rule settings (grep of modelarmor/apiv1 and apiv1beta at googleapis/google-cloud-go@37f936ac found no match for FilterVersion, FilterRule or exclusion); the docs describe both **[Not disclosed]**
• Pricing: standalone use has "no cost for using Model Armor up to 2 million tokens per month" and then "$0.10 per million tokens"; separately, "Security Command Center includes Model Armor with a predefined number of tokens per month at no additional cost" (pricing page, 2026-10-09) **[Documented]**
• Data handling: Model Armor "operates as a stateless service, processing all prompts and model responses entirely in memory"; content is stored only if Cloud Logging is enabled, and `logSanitizeOperations` logs the full content of prompts and responses (overview, logging page, 2026-10-09) **[Documented]**
• Failure behaviour on the Agent Platform route: Model Armor sanitisation is skipped and the request continues when Model Armor is unavailable in the region, temporarily unreachable or returns an error (Agent Platform page, 2026-10-09) **[Documented]**
• LangChain runnables take a `fail_open` flag: `True` "logs a warning but lets content pass even if risks are detected" and `False` raises a `ValueError` (LangChain page, 2026-10-09) **[Documented]**
• Client libraries exist for C#, Go, Java, Node.js, PHP and Python; the C# install line is a pre-release package (`--version 1.0.0-beta05`) (client libraries page, 2026-10-09) **[Documented]**
• Release status of routes: Agent Platform GA (release note 2025-12-03), Agent Gateway GA (2026-06-24), Gemini Enterprise GA (2025-09-16), Google and Google Cloud MCP servers GA (2026-04-22), GKE integration GA (2025-09-15), streaming sanitization GA (2026-07-10), LangChain Preview (LangChain page) **[Documented]**
• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse` and load-balancer Service Extensions other than GKE: no GA or Preview label found on the pages read **[To be verified]**
• Self-hosted or offline option: none described (checked overview, product page, locations page, client libraries page, which all call the managed API) **[Not disclosed]**
### R5
Summary: **Match flag plus a confidence level.** The result gives an execution state, a match state and a confidence level. Google advises Medium in one place and High in another as the setting. **[Documented]**
Detail:
• Overall result `sanitizationResult.filterMatchState` is `NO_MATCH_FOUND` or `MATCH_FOUND`; `invocationResult` is `SUCCESS`, `PARTIAL` or `FAILURE` (REST result ref, 2026-10-09) **[Documented]**
• `filterResults.pi_and_jailbreak.piAndJailbreakFilterResult` holds `executionState`, `messageItems`, `matchState` and `confidenceLevel` (REST result ref, 2026-10-09) **[Documented]**
• Response example: for the text "IP address of the current network is ##.##.##.##" the sample result has `pi_and_jailbreak` with `EXECUTION_SUCCESS` and `NO_MATCH_FOUND`, and no confidence field (sanitize page, 2026-10-09) **[Documented]**
• Numeric score or probability: none (the result reference page has no score field) **[Not disclosed]**
• Confidence enum: `LOW_AND_ABOVE` "Highest chance of a false positive", `MEDIUM_AND_ABOVE` "Some chance of false positives", `HIGH` "Low chance of false positives"; the filter reports a match when "detection confidence is equal to or greater than the specified level" (REST templates ref, 2026-10-09) **[Documented]**
• Threshold advice A (C1), overview example strategy: "Set prompt injection and jailbreak detection filters to Medium. For applications like Gemini Enterprise, set the threshold to High to avoid false positives." (overview, 2026-10-09) **[Documented]**
• Threshold advice B (C1), templates page: "We recommend that you set the confidence level to High to minimize false positives and ensure consistent detection behavior." (templates page, 2026-10-09) **[Documented]**
• Threshold advice C, overview table: Low and above is "Potentially suitable for high-stakes categories like prompt injection and jailbreak detection, where preventing false negatives is critical, even at the risk of accepting false positives" (overview, 2026-10-09) **[Documented]**
• Default when the level is omitted: the enum says unspecified is "Same as LOW_AND_ABOVE", and the filter field has no separate default statement, so an omitted level would behave as Low and above **[Inferred]**
• Whether the three-word minimum applies to responses: the overview and quotas notes both say "such inputs lack enough information to constitute an attack" **[To be verified]**
• Google's advice is "Always test your filter configurations against a representative dataset of prompts and responses, including known good and bad examples." (overview, 2026-10-09) **[Documented]**
• Published accuracy, recall, F1 or false-positive rates for the filter on responses (checked overview, best practices, product page, blog, release notes, version history) **[Not disclosed]**
• Enforcement type in `templateMetadata.enforcementType`: `INSPECT_ONLY` ("No action will be taken on the request") or `INSPECT_AND_BLOCK`; unspecified is "Same as INSPECT_AND_BLOCK" (REST templates ref, 2026-10-09) **[Documented]**
• Template metadata can carry a custom error code and message for a response that trips a filter (`customLlmResponseSafetyErrorCode`, `customLlmResponseSafetyErrorMessage`) (REST templates ref, 2026-10-09) **[Documented]**
• Template-specific exclusion rules (Preview): a matching rule makes Model Armor override "a MATCH_FOUND or EXECUTION_SKIPPED filter result and sets matchState to NO_MATCH_FOUND for that entire supported filter type" (exclusion rules page, 2026-10-09) **[Documented]**
• The exclusion rules page shows `filterConfig.filterRuleSettings` in v1 requests, but the REST `FilterConfig` lists only `raiSettings`, `sdpSettings`, `piAndJailbreakFilterSettings` and `maliciousUriFilterSettings`; the field is absent from the Go v1 client at googleapis/google-cloud-go@37f936ac (C11) **[To be verified]**
• Apigee exposes `piAndJailbreakFilterResult.matchState`, `promptInjectionDetected` and `promptInjectionConfidence` as flow variables of the `SanitizeModelResponse` policy (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**
### R6
Summary: **A template with the filter enabled, a regional endpoint and the response text.** The caller needs the Model Armor User role and text up to 65,536 tokens. Default quota is 1,200 queries per minute per project. **[Documented]**
Detail:
• The filter runs only if `piAndJailbreakFilterSettings.filterEnforcement` is `ENABLED`; "Confidence level will only be used if the filter is enabled." (REST templates ref, 2026-10-09) **[Documented]**
• "Note: To sanitize prompts and responses, you must use regional endpoints." and the template must be in the location of the endpoint (sanitize page, templates page, 2026-10-09) **[Documented]**
• Required before calling: enable `modelarmor.googleapis.com`, create a template, and hold Model Armor User (`roles/modelarmor.user`); creating templates needs Model Armor Admin (`roles/modelarmor.admin`) (sanitize page, templates page, 2026-10-09) **[Documented]**
• For MCP traffic the filter is configured in project floor settings, which need Model Armor Floor Setting Admin (`roles/modelarmor.floorSettingsAdmin`) (MCP page, floor settings page, 2026-10-09) **[Documented]**
• Request fields for text: `modelResponseData.text`; optional `multiLanguageDetectionMetadata` with `enableMultiLanguageDetection` and `sourceLanguage` (sanitize page, 2026-10-09) **[Documented]**
• Optional `UserPrompt` string in the Go client request for this method, "User Prompt associated with Model response." (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:2380-2381) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• Token limit: "Model Armor screens text up to 65,536 tokens (approximately 262,144 characters)" for prompt injection, responsible AI and CSAM filters (quotas page, 2026-10-09) **[Documented]**
• Over the limit the filter returns `EXECUTION_SKIPPED` with the message "Detection skipped as token limit exceeded." (quotas page, 2026-10-09) **[Documented]**
• Unlimited tokens apply in real-time streaming mode, which suits long model outputs; buffered mode keeps the limits, and the limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, sanitize page, 2026-10-09) **[Documented]**
• Earlier limits in the release notes: 2,000 tokens for all filters (2025-05-28), 10,000 for this filter (2025-07-28), superseded by 65,536 (2026-08-25) (release notes, 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project", adjustable between 0 and 1,200; a call per prompt and another per response both count (quotas page, integrations page, 2026-10-09) **[Documented]**
• Exclusion rules limits: 10 rule sets per filter configuration, 10 rules per set, 10 dictionaries, 128 KB per word list, 1,000-character regular expressions, and only the first 130,000 tokens (0.5 MB) of input are evaluated; they are not supported in streaming APIs or floor settings (quotas page, exclusion rules page, 2026-10-09) **[Documented]**
• Data residency: new templates enforce it by default (`dataResidencyCompliant` true); the prompt injection and jailbreak filter is listed for every location except asia-northeast3, which lists only Sensitive Data Protection (feature availability page, REST templates ref, 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the Model Armor API on, a template with prompt injection and jailbreak detection enabled in a full-support region, and a script posting labelled model outputs or tool results to the regional sanitize-model-response endpoint. Standalone use is free to 2 million tokens a month. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled, `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call; one template in a regional location with `piAndJailbreakFilterSettings` set to `ENABLED`; a script that posts each output to `:sanitizeModelResponse` and records `filterMatchState` and the `pi_and_jailbreak` result. **[Inferred]**
• Cost: the premise is the standalone allowance of 2 million tokens a month (R4); responses are longer than prompts, so count tokens before a large run **[Inferred]**
• Test data: Google supplies none; the bench needs response-side items such as a retrieved web page or tool result carrying hidden instructions, a model reply that obeys an injected instruction, and a persona jailbreak reply, plus benign outputs that quote or explain prompts and instructions **[Inferred]**
• Include natural-language and structured tool results (JSON, code) separately, because Google advises against enabling the filter for MCP traffic that carries no natural language **[Inferred]**
• Run each set at all three confidence levels using one template per level, and compare a template that omits the level **[Inferred]**
• Send some items with the optional `userPrompt` field to see whether results change (R3) **[Inferred]**
• Test short outputs of fewer than three words to see whether the documented three-word rule also applies to responses (R5) **[Inferred]**
• Cover the nine tested languages and add Singlish, Malay and Tamil, which are not in the tested list (R2) **[Inferred]**
• Region: choose a full-support location (for example us-central1); asia-southeast1 offers prompt injection and jailbreak detection with residency enforced, but not CSAM, multi-language, malicious URL, image or antivirus; setting `dataResidencyCompliant` to false enables all of these except image, which stays limited to the us and eu multi-regions (feature availability page, templates page, release note 2026-08-27) **[Inferred]**
• No self-hosted or offline option is described (R4), so tests need network access to Google Cloud and a billing account **[Inferred]**
### R8
Summary: **Key open questions.** Which model backs the filter, what response-side detection covers, which threshold to use, whether the three-word rule applies to responses, accuracy by attack type, and the exclusion rules schema gap.
Detail:
• Backing model and whether prompts and responses share it (checked overview, product page, version pages, release notes, REST references; not stated)
• What a response-side detection is meant to catch, and a documented positive example (templates page says "in a prompt"; the overview and sample output include responses)
• Which confidence level to use: Medium (overview example strategy) or High (templates page recommendation); needs testing on a labelled set
• Default level when the field is omitted (inferred as Low and above from the enum; needs testing)
• Whether the three-word minimum applies to responses (the docs say "inputs")
• Detection rate and false-positive rate per attack style, version (v3 against v4) and language on responses (no figures published; needs testing)
• Whether the optional `userPrompt` field of the response request changes any result (the Go client documents it; the docs pages do not mention it)
• Whether `filterRuleSettings` is a supported field of the v1 template (shown in the exclusion rules page, absent from the REST reference and the Go client)
• Whether structured tool output (JSON, code) triggers false positives, given the MCP natural-language tip
• Latency per call: no figure published; the best practices page says "Enabling unnecessary detectors can increase latency" (needs testing)
### R9
Summary: Model Armor documentation pages on docs.cloud.google.com, the Model Armor product page, the Security Command Center pricing page, the Apigee policy reference and the Google Cloud Go client source.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/set-filter-version
• https://docs.cloud.google.com/model-armor/version-history
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/locations
• https://docs.cloud.google.com/model-armor/configure-exclusion-rules
• https://docs.cloud.google.com/model-armor/configure-floor-settings
• https://docs.cloud.google.com/model-armor/configure-logging
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
• https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
• https://docs.cloud.google.com/model-armor/model-armor-apigee-integration
• https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration
• https://docs.cloud.google.com/model-armor/model-armor-networking-integration
• https://docs.cloud.google.com/model-armor/model-armor-langchain-integration
• https://docs.cloud.google.com/model-armor/best-practices
• https://docs.cloud.google.com/model-armor/reference/libraries
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go
