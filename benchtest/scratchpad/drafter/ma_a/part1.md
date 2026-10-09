## Column MA1: Model Armor: Input-level responsible AI safety filtering
### R1
Summary: **Input-level responsible AI safety filtering.** Model Armor screens a user prompt for hate speech, harassment, sexually explicit and dangerous content at a confidence level set per category. A CSAM check also runs and cannot be turned off. The calling service enforces any block. **[Documented]**
Detail:
• The overview lists a "Responsible AI safety filter" that can "screen prompts and responses at the specified confidence levels" for four categories: hate speech, harassment, sexually explicit and dangerous content (overview, 2026-10-09) **[Documented]**
• Input side of the documented flow: "Model Armor inspects the incoming prompt for potentially sensitive content." (overview, Architecture, 2026-10-09) **[Documented]**
• Stated use case: "Filter toxic or harmful content: Screen user inputs and model outputs against configurable confidence thresholds for hate speech, harassment, sexual content, dangerous content, and child sexual abuse material (CSAM)." (overview, 2026-10-09) **[Documented]**
• Product page wording: "Provides fine-grained control of harmful, unethical, or undesirable content, such as hate speech, harassment, sexually explicit material, and dangerous topics." (product page, marketing text, 2026-10-09) **[Documented]**
• Configured in a template under `filterConfig.raiSettings.raiFilters[]`, each entry with a `filterType` and an optional `confidenceLevel` (REST templates ref, 2026-10-09) **[Documented]**
• The service returns a verdict and the caller acts on it: "The calling service or integration point or Policy Enforcement Point (PEP) is responsible for blocking the further processing." (overview, Inspect and block row, 2026-10-09) **[Documented]**
• Through the REST API, "Model Armor functions only as a detector using templates"; the application decides whether to block or allow (integrations page, 2026-10-09) **[Documented]**
• CSAM: "This filter is applied by default and cannot be turned off." (overview, 2026-10-09) **[Documented]**
• CSAM is not one of the four `RaiFilterType` values and has its own result key `csam`; it has no confidence setting (REST templates ref and REST result ref, 2026-10-09) **[Documented]**
### R2
Summary: **Four harm categories plus CSAM.** Hate speech, harassment, sexually explicit and dangerous content each have a one-line definition. The filters are tested in nine languages and do not decode encoded content or handle audio or video. **[Documented]**
Detail:
• Four category definitions (overview, 2026-10-09) **[Documented]**
  – Hate speech: "Negative or harmful comments targeting identity and/or protected attributes."
  – Harassment: "Threatening, intimidating, bullying, or abusive comments targeting another individual."
  – Sexually explicit: "Contains references to sexual acts or other lewd content."
  – Dangerous content: "Promotes or enables access to harmful goods, services, and activities."
• CSAM definition: "Contains references to child sexual abuse material (CSAM)." (overview, 2026-10-09) **[Documented]**
• Languages tested: Chinese (Mandarin), English, French, German, Italian, Japanese, Korean, Portuguese and Spanish; "These filters can work in many other languages, but the quality of results might vary." (overview, 2026-10-09) **[Documented]**
• Multi-language detection can be switched on per request (`enableMultiLanguageDetection`, optional `sourceLanguage`) or once in the template (`templateMetadata.multiLanguageDetection`); with a source language given, Model Armor "uses that language to evaluate the request" (sanitize page, REST templates ref, release note 2026-02-27) **[Documented]**
• In asia-south1 and northamerica-northeast2, "if you send non-English content to detectors like prompt injection and jailbreak or RAI, Model Armor returns a verdict of Skipped Detection for those specific checks" (sanitize page, 2026-10-09) **[Documented]**
• Model Armor "doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext" and "doesn't support audio or video" (overview, Limitations, 2026-10-09) **[Documented]**
• Each prompt is inspected "independently as a single-turn request"; Model Armor "doesn't track conversation history or maintain context across multi-turn interactions" (overview, Limitations, 2026-10-09) **[Documented]**
• Docs state the CSAM filter "cannot be turned off" (overview) but the feature table for templates with data residency enforced shows CSAM support "No" in all seven limited-support locations and "Yes" in the full-support ones (feature availability page, 2026-10-09) **[Documented]**
• Prompts combining text and images in one request are not supported; image handling is in column MA10 and documents in MA9 (overview, Limitations, 2026-10-09) **[Documented]**
• Topic enforcement (C10): the overview scenario "Enforce custom topics" says "A company's support bot is configured using custom rules to not discuss competitors" and the prompt or answer is blocked (overview, usage scenarios, 2026-10-09) **[Documented]**
• Topic enforcement configuration: no topic filter, setting or page was found (checked REST `FilterConfig` with four settings, the templates page detection list, the overview filter section, the blog's five capabilities and the product page features) **[Not disclosed]**
• Severity grades or a harm taxonomy beyond the four categories and CSAM (checked overview, templates page, REST references, product page, blog) **[Not disclosed]**
• Refusal handling: the overview says "A model's refusal is separate from a Model Armor block"; no refusal detector is described (checked the same pages) **[Not disclosed]**
### R3
Summary: **The latest user message, sent on its own.** The caller posts it to the sanitize-user-prompt method of a regional endpoint with a template name. Conversation history and system prompts are not to be included. **[Documented]**
Detail:
• Method and field: `POST https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeUserPrompt` with body `{"userPromptData":{"text":"..."}}` (sanitize page, 2026-10-09) **[Documented]**
• Streaming variant `StreamSanitizeUserPrompt` has buffered and real-time modes and takes text only: "Model Armor streaming methods support only textual input, not attachments like images and files." (sanitize page, 2026-10-09) **[Documented]**
• Input rules: `userPromptData` "must contain only the content of the latest message from the user"; "Don't include conversation history"; "Don't include system prompts" (sanitize page, conversational AI best practices, 2026-10-09) **[Documented]**
• The overview suggests separate templates for prompts and responses; its input-template focus lists "malicious inputs, prompt injections, jailbreak attempts, and uploading sensitive data" and does not name harmful content, while the sample initial deployment sets hate speech and harassment filters (overview, 2026-10-09) **[Documented]**
• Retrieved and intermediate text: the Gemini Enterprise, Agent Runtime and Apigee integrations also sanitize "intermediate steps, such as grounding data and responses returned by web search tools"; a violating payload is blocked and logged as a `SANITIZE_USER_PROMPT` operation (integrations page, 2026-10-09) **[Documented]**
• Routes that run this filter on prompts (docs pages named in each item, 2026-10-09) **[Documented]**
  – Agent Platform `generateContent`: `promptTemplateName` in the request or project floor settings; no documents or images (Agent Platform page)
  – Agent Gateway: ingress client requests for agents built with the Agent Development Kit, and egress requests to MCP servers, A2A agents and OpenAI-format services (Agent Gateway page)
  – Apigee: `SanitizeUserPrompt` policy added to the request flow (Apigee page)
  – Gemini Enterprise: user prompts screened through templates (Gemini Enterprise page)
  – Service Extensions on load balancers, GKE Inference Gateway and Secure Web Proxy; the filters identify "harmful or inappropriate content, such as hate speech and harassment" (networking page)
  – Google and Google Cloud MCP servers via floor settings; the docs example sets the Dangerous category at `MEDIUM_AND_ABOVE` (MCP page)
  – LangChain `ModelArmorSanitizePromptRunnable` (Preview) (LangChain page)
• Text extracted from documents is screened for safety as well; file handling is in column MA9 (overview, Document screening, 2026-10-09) **[Documented]**
• Whether the responsible AI filter is applied to text read out of images by OCR: the image examples show only `csam` and `sdp` results, and the reference says text and visual content "will be sanitized depending on the filter configuration" (sanitize page, REST templates ref, 2026-10-09) **[To be verified]**
### R4
Summary: **Managed Google Cloud service; model not disclosed.** The filter runs inside a template-driven regional API. Google names no model, training data or architecture, and the filter changes through numbered filter versions v1 to v4. **[Not disclosed]**
Detail:
• Model Armor is "a Google Cloud service"; callers use a REST API on regional endpoints (`modelarmor.LOCATION.rep.googleapis.com`) and a template; "The global endpoint (modelarmor.googleapis.com) doesn't support" template management or sanitizing (templates page, overview, 2026-10-09) **[Documented]**
• Generic product-page description: "combines rules-based controls, ML models, and powerful AI reasoning models"; no per-filter mapping is given (product page, 2026-10-09) **[Documented]**
• Backing model, size, architecture, training data and labelling for the responsible AI filter (checked overview, product page, filter version pages, release notes, REST references, blog, best practices) **[Not disclosed]**
• Filter versions: one version per template, chosen by number or alias (Latest, Stable, Legacy, Retired); "You can't specify different versions for individual filters" (filter version page, 2026-10-09) **[Documented]**
• Version timeline: v1 2025-01-30 (Legacy), v2 2025-06-19 (Legacy), v3 2026-05-25 (Stable), v4 2026-09-18 (Latest) (filter version page, 2026-10-09) **[Documented]**
• Version notes that name the responsible AI filter: v3 on 2026-07-20, "upgraded to improve detection accuracy and reduce the rate of false positives"; v4 on 2026-09-18, "Minor updates have been made across prompt injection and jailbreak detection, and responsible AI filters to address reported false positives" (version history, 2026-10-09) **[Documented]**
• Release note 2026-03-26: the malicious URL detection and responsible AI safety filters "are fixed to improve detection accuracy and reduce the rate of false positives" (release notes, 2026-10-09) **[Documented]**
• Legacy versions v1 and v2 retire on 2026-12-17 (filter version page; release note 2026-09-18) **[Documented]**
• An earlier release note (2026-09-02) gave 2026-11-29 for the same retirement; the later note and the version page supersede it (release notes, 2026-10-09) **[Documented]**
• In asia-southeast1 the template-version table lists v1 (Legacy), v3 (Stable) and v4 (Latest) (filter version page, 2026-10-09) **[Documented]**
• Templates without a version use Stable; floor settings use Stable by default (filter version page, 2026-10-09) **[Documented]**
• Pricing: standalone use has "no cost for using Model Armor up to 2 million tokens per month" and then "$0.10 per million tokens"; separately, "Security Command Center includes Model Armor with a predefined number of tokens per month at no additional cost" (pricing page, 2026-10-09) **[Documented]**
• Data handling: Model Armor "operates as a stateless service, processing all prompts and model responses entirely in memory"; content is stored only if Cloud Logging is enabled, and `logSanitizeOperations` logs the full content of prompts and responses (overview, logging page, 2026-10-09) **[Documented]**
• Failure behaviour on the Agent Platform route: Model Armor sanitisation is skipped and the request continues when Model Armor is unavailable in the region, temporarily unreachable or returns an error (Agent Platform page, 2026-10-09) **[Documented]**
• Release status of routes: Agent Platform GA (release note 2025-12-03), Agent Gateway GA (2026-06-24), Gemini Enterprise GA (2025-09-16), Google and Google Cloud MCP servers GA (2026-04-22), GKE integration GA (2025-09-15), streaming sanitization GA (2026-07-10), LangChain Preview (LangChain page) **[Documented]**
• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse` and load-balancer Service Extensions other than GKE: no GA or Preview label found on the pages read **[To be verified]**
• Client libraries exist for C#, Go, Java, Node.js, PHP and Python; the C# install line is a pre-release package (`--version 1.0.0-beta05`) (client libraries page, 2026-10-09) **[Documented]**
• Self-hosted or offline option: none described (checked overview, product page, locations page, client libraries page, which all call the managed API) **[Not disclosed]**
### R5
Summary: **Match flags per category, no numeric score.** The result gives an overall match state and a match state for each of the four categories, sometimes with a confidence level. Google publishes no accuracy figures. **[Documented]**
Detail:
• Overall result `sanitizationResult.filterMatchState` is `NO_MATCH_FOUND` or `MATCH_FOUND`; `invocationResult` is `SUCCESS`, `PARTIAL` or `FAILURE` (REST result ref, 2026-10-09) **[Documented]**
• `filterResults.rai.raiFilterResult` holds `executionState` (`EXECUTION_SUCCESS` or `EXECUTION_SKIPPED`), `matchState`, `messageItems` and `raiFilterTypeResults` keyed `sexually_explicit`, `hate_speech`, `harassment` and `dangerous`, each with `filterType`, `confidenceLevel` and `matchState` (REST result ref, 2026-10-09) **[Documented]**
• The RAI `matchState` is `MATCH_FOUND` "if at least one RAI filter confidence level is equal to or higher than the confidence level defined in configuration" (REST result ref, 2026-10-09) **[Documented]**
• CSAM result `filterResults.csam.csamFilterFilterResult` has `executionState`, `messageItems` and `matchState`, with no confidence field (REST result ref, 2026-10-09) **[Documented]**
• Numeric score or probability per category: none (the result reference page has no score field) **[Not disclosed]**
• Confidence enum: `LOW_AND_ABOVE` "Highest chance of a false positive", `MEDIUM_AND_ABOVE` "Some chance of false positives", `HIGH` "Low chance of false positives"; unspecified is "Same as LOW_AND_ABOVE" (REST templates ref, 2026-10-09) **[Documented]**
• Default level, console (C3): "If you don't specify a confidence level, it is set to High by default." (templates page, console steps, 2026-10-09) **[Documented]**
• Default level, REST: "If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the filterType." (REST templates ref, 2026-10-09) **[Documented]**
• The two default statements differ and no page says which applies to an API call that omits the level **[To be verified]**
• Whether the per-category `confidenceLevel` in a result is the detected level or the configured one: the sanitize page examples show `HIGH` in a prompt result and `MEDIUM_AND_ABOVE` in a response result, and the reference says only "Confidence level identified for this RAI filter" **[To be verified]**
• Threshold guidance in the overview: High suits "Production environments that prioritize uninterrupted user interactions"; Medium and above is for "Standard enterprise applications"; Low and above is "Not recommended for general responsible AI content categories due to the high risk of blocking harmless content" (overview, 2026-10-09) **[Documented]**
• Sample initial deployment: "Set general responsible AI filters (hate speech and harassment) to High." (overview, 2026-10-09) **[Documented]**
• The false-positive risk ratings in the overview table (very low, moderate, high) are qualitative; no measured rates accompany them **[Inferred]**
• Published accuracy, recall, F1 or false-positive rates for the responsible AI filter (checked overview, best practices, product page, blog, release notes, version history) **[Not disclosed]**
• Enforcement type in `templateMetadata.enforcementType`: `INSPECT_ONLY` ("No action will be taken on the request") or `INSPECT_AND_BLOCK`; unspecified is "Same as INSPECT_AND_BLOCK" (REST templates ref, 2026-10-09) **[Documented]**
• Inspect only logs to Cloud Logging, so "Cloud Logging must be enabled" to gain value from it (overview, 2026-10-09) **[Documented]**
• Template-specific exclusion rules (Preview): a matching rule makes Model Armor override "a MATCH_FOUND or EXECUTION_SKIPPED filter result and sets matchState to NO_MATCH_FOUND for that entire supported filter type", including all responsible AI categories (exclusion rules page, 2026-10-09) **[Documented]**
• Apigee exposes `raiFilterResult.matchState` and `raiMatchesFound` as flow variables of the `SanitizeUserPrompt` policy (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**
### R6
Summary: **A template, a regional endpoint and the message text.** The caller needs the Model Armor User role, a template in the endpoint's location, and text up to 65,536 tokens. Default quota is 1,200 queries per minute per project. **[Documented]**
Detail:
• "Note: To sanitize prompts and responses, you must use regional endpoints." and the template must be in the location of the endpoint (sanitize page, templates page, 2026-10-09) **[Documented]**
• Required before calling: enable `modelarmor.googleapis.com`, create a template, and hold Model Armor User (`roles/modelarmor.user`); viewing templates needs Model Armor Viewer, creating them Model Armor Admin (`roles/modelarmor.admin`) (sanitize page, templates page, 2026-10-09) **[Documented]**
• Cross-project use: the calling account needs `roles/modelarmor.user` in the project that hosts the template (sanitize page, 2026-10-09) **[Documented]**
• Request fields for text: `userPromptData.text`; optional `multiLanguageDetectionMetadata` with `enableMultiLanguageDetection` and `sourceLanguage` (sanitize page, 2026-10-09) **[Documented]**
• Template ID: "can contain letters, digits, underscores, or hyphens. It cannot exceed 63 characters, contain spaces, or start with a hyphen." (templates page, 2026-10-09) **[Documented]**
• Token limit: "Model Armor screens text up to 65,536 tokens (approximately 262,144 characters)" for prompt injection, responsible AI and CSAM filters (quotas page, 2026-10-09) **[Documented]**
• Over the limit the filter returns `EXECUTION_SKIPPED` with the message "Detection skipped as token limit exceeded." (quotas page, 2026-10-09) **[Documented]**
• Unlimited tokens apply in real-time streaming mode, and the limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, 2026-10-09) **[Documented]**
• Earlier limits in the release notes: 2,000 tokens for all filters (2025-05-28), superseded by 65,536 (2026-08-25) (release notes, 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project", adjustable between 0 and 1,200; over-quota calls show HTTP 429 `RESOURCE_EXHAUSTED` (quotas page, integrations page, 2026-10-09) **[Documented]**
• From a VPC network, a Private Service Connect endpoint to the Model Armor APIs is needed to reach regional endpoints (overview, 2026-10-09) **[Documented]**
• Data residency: new templates enforce it by default (`dataResidencyCompliant` true); the responsible AI filter is listed for every location except asia-northeast3, which lists only Sensitive Data Protection (feature availability page, REST templates ref, 2026-10-09) **[Documented]**
• Exclusion rules need the filter enabled, apply to one template, and are not supported in streaming APIs or floor settings (exclusion rules page, 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the Model Armor API on, a template with the four categories at chosen levels in a full-support region, and a script calling the regional sanitize-user-prompt endpoint with labelled safe and harmful prompts. Standalone use is free to 2 million tokens a month. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled, `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call; one template in a regional location with `raiSettings` for all four categories; a script that posts each test prompt to `:sanitizeUserPrompt` and records `filterMatchState` and each `raiFilterTypeResults` entry. **[Inferred]**
• Cost: the premise is the standalone allowance of 2 million tokens a month (R4), so a few thousand short prompts cost nothing **[Inferred]**
• Test data: Google supplies none for this filter; the bench needs labelled prompts per category (hate speech, harassment, sexually explicit, dangerous) plus benign near-misses such as technical or medical wording **[Inferred]**
• Run each set at all three confidence levels using one template per level, because the result gives match states, not scores **[Inferred]**
• Cover the nine tested languages and add Singlish, Malay and Tamil, which are not in the tested list (R2) **[Inferred]**
• Do not build CSAM test material; check only that `csam` returns `EXECUTION_SUCCESS` and `NO_MATCH_FOUND` on benign text **[Inferred]**
• Region: choose a full-support location (for example us-central1); asia-southeast1 offers the responsible AI filter with residency enforced but not CSAM, multi-language, malicious URL, image or antivirus, unless `dataResidencyCompliant` is set to false (feature availability page, release note 2026-08-27) **[Inferred]**
• No self-hosted or offline option is described (R4), so tests need network access to Google Cloud and a billing account **[Inferred]**
### R8
Summary: **Key open questions.** Which model backs the filter, the default confidence level, what the per-category confidence field means, accuracy by category and language, CSAM behaviour in limited-support regions, and any topic enforcement.
Detail:
• Backing model and whether prompts and responses share it (checked overview, product page, version pages, release notes, REST references; not stated)
• Default confidence level when the field is omitted: High (templates page console note) or the same as Low and above (REST reference); needs testing
• Whether the `confidenceLevel` in each category result is the detected or the configured level (docs examples differ)
• Precision and recall per category and per level, and the effect of the v3 and v4 changes (no figures published; needs testing)
• Coverage in Singlish, Malay and Tamil and in the other languages the docs say "might vary"
• Whether CSAM screening runs in limited-support regions with residency enforced, given "cannot be turned off" against the feature table's "No"
• Whether any custom topic or competitor rule can be configured, despite the overview scenario (no configuration page found)
• Latency per call: no figure published; the best practices page says "Enabling unnecessary detectors can increase latency" (needs testing)
• Whether RAI runs on OCR text from images (see MA10)
### R9
Summary: Model Armor documentation pages on docs.cloud.google.com, the Model Armor product page, the Security Command Center pricing page and the Apigee policy reference.
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
• https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy
