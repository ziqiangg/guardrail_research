## Column MA7: Model Armor: Input-level malicious URL detection
### R1
Summary: **Input-level malicious URL detection.** Model Armor extracts the URLs in a user prompt and checks whether each is malicious, such as a phishing or malware link. It returns a match state and the matched URLs, and scans only the first 256 URLs. **[Documented]**
Detail:
• Overview: "When malicious URL detection is enabled, Model Armor scans URLs to identify whether they're malicious." (overview, 2026-10-09) **[Documented]**
• Templates page lists it among the detection checks "on prompts and responses": it "Identifies web addresses (URLs) that are designed to harm users or systems" (templates page, 2026-10-09) **[Documented]**
• Product page wording: "Detects malicious files, malware, and unsafe URLs within AI prompts and responses." (product page, marketing text, 2026-10-09) **[Documented]**
• The overview frames the filter mainly around output: it "lets you take action and prevent malicious URLs from being returned", and its input-template focus does not name URLs while its output-template focus does (overview, 2026-10-09) **[Documented]**
• Vendor blog (supporting only): the filter "scans for malicious and phishing links in both the input and output" (Google Cloud blog, 2025-10-22) **[Documented]**
• Configured in a template under `filterConfig.maliciousUriFilterSettings` with a single field, `filterEnforcement` (`ENABLED` or `DISABLED`; unspecified is "Same as Disabled") (REST templates ref, 2026-10-09) **[Documented]**
• The result key is `malicious_uris` with `maliciousUriFilterResult` (REST result ref, 2026-10-09) **[Documented]**
• The service returns a verdict and the caller acts on it: "The calling service or integration point or Policy Enforcement Point (PEP) is responsible for blocking the further processing." (overview, 2026-10-09) **[Documented]**
### R2
Summary: **Phishing, malware and other malicious links.** Google describes disguised URLs used for phishing, malware distribution and other online threats. Only the first 256 URLs in a prompt are scanned, and URL-encoded content is not decoded. **[Documented]**
Detail:
• Threat description: "Malicious URLs are often disguised to look legitimate, making them a potent tool for phishing attacks, malware distribution, and other online threats." (overview, 2026-10-09) **[Documented]**
• Templates page: the URLs "might lead to phishing sites, malware downloads, or other cyberattacks" (templates page, 2026-10-09) **[Documented]**
• Document angle: "if a PDF contains an embedded malicious URL, it can be used to compromise any downstream systems processing LLM outputs"; documents are screened for malicious URLs (overview, 2026-10-09) **[Documented]**
• URL cap: "Model Armor extracts URLs until it reaches 256 URLs or the end of the payload, and scans only the first 256 URLs found in prompts and responses." (overview, quotas page, 2026-10-09) **[Documented]**
• A prompt that places more than 256 harmless URLs before a malicious one would leave the malicious URL unscanned, if URLs are taken in order of appearance **[Inferred]**
• Token limits do not apply: "Token system limits don't apply to malicious URL detection. Instead, Model Armor enforces a limit on the number of URLs scanned." (quotas page, 2026-10-09) **[Documented]**
• Model Armor "doesn't decode or inspect encoded content, such as prompts encoded in Base64, hexadecimal, URL encoding, or ciphertext" (overview, Limitations, 2026-10-09) **[Documented]**
• Release note 2026-03-26: the malicious URL detection and responsible AI filters "are fixed to improve detection accuracy and reduce the rate of false positives" (release notes, 2026-10-09) **[Documented]**
• Filter versions do not apply: "The filter version setting doesn't affect the Sensitive Data Protection and malicious URL filters." (filter version page, 2026-10-09) **[Documented]**
• Availability: the filter is listed for the full-support locations; in the seven limited-support locations with data residency enforced it is not (Singapore, asia-southeast1, lists only responsible AI, Sensitive Data Protection and prompt injection and jailbreak) (feature availability page, 2026-10-09) **[Documented]**
• Disabling data residency enforcement in the template allows cross-jurisdictional routing "to enable Model Armor features that are otherwise unavailable in limited-support regions" (release note 2026-08-27, data residency page, 2026-10-09) **[Documented]**
• Categories of malicious URL (phishing, malware, social engineering), the reputation source or list, how often it updates, and whether shortened, redirecting, defanged or internationalised URLs are resolved (checked overview, templates page, product page, REST references, release notes, blog) **[Not disclosed]**
• Whether URLs inside images are extracted by OCR and checked (the image examples show only `csam` and `sdp` results) **[To be verified]**
• The product page and the region tables also mention malware and antivirus scanning, and the result schema has a `virusScanFilterResult` for PDF; that is a separate capability and not part of this column (product page, feature availability page, REST result ref, 2026-10-09) **[Documented]**
### R3
Summary: **URLs found in the latest user message.** The caller posts the message to the sanitize-user-prompt method of a regional endpoint with a template name, and the filter extracts URLs from the text, up to 256. No system prompt or history is needed. **[Documented]**
Detail:
• Method and field: `POST https://modelarmor.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID:sanitizeUserPrompt` with body `{"userPromptData":{"text":"..."}}` (sanitize page, 2026-10-09) **[Documented]**
• Streaming variant `StreamSanitizeUserPrompt` has buffered and real-time modes and takes text only (sanitize page, 2026-10-09) **[Documented]**
• Input rules: `userPromptData` "must contain only the content of the latest message from the user"; "Don't include conversation history"; "Don't include system prompts" (sanitize page, conversational AI best practices, 2026-10-09) **[Documented]**
• Each prompt is inspected "independently as a single-turn request" (overview, Limitations, 2026-10-09) **[Documented]**
• Retrieved and intermediate text: the Gemini Enterprise, Agent Runtime and Apigee integrations also sanitize "intermediate steps, such as grounding data and responses returned by web search tools" (integrations page, 2026-10-09) **[Documented]**
• Routes whose pages mention this filter on traffic into a model or tool (docs pages named in each item, 2026-10-09) **[Documented]**
  – Agent Platform `generateContent`: the documented template example sets `malicious_uri_filter_settings` enabled, with `promptTemplateName` or project floor settings (Agent Platform page)
  – Apigee: the `SanitizeUserPrompt` policy sets `maliciousURIs` and `maliciousURIsDetected` flow variables (Apigee policy ref, Apigee docs not Model Armor docs)
  – Service Extensions on load balancers, GKE Inference Gateway and Secure Web Proxy: the filters identify "malicious URLs" (networking page)
  – Google and Google Cloud MCP servers via floor settings: the docs example enables `--malicious-uri-filter-settings-enforcement=ENABLED` and tests a `tools/call` parameter containing a phishing test URL, which is blocked (MCP page)
• Verification entry in the MCP docs: a blocked call shows a Cloud Logging entry such as `MALICIOUS_URI_DETECTED` (MCP page, 2026-10-09) **[Documented]**
• Folder-level floor settings can require templates to enable the malicious URI filter; the docs illustrate this with a folder where "All content in this folder must enable a malicious URI filter." (floor settings page, 2026-10-09) **[Documented]**
• Text extracted from documents is also screened for malicious URLs; file handling is in column MA9 (overview, Document screening, 2026-10-09) **[Documented]**
### R4
Summary: **Managed service; URL-checking method not disclosed.** Google names no reputation source, model or detection method for malicious URLs. The filter is not covered by filter versions and is unavailable in limited-support regions when data residency is enforced. **[Not disclosed]**
Detail:
• Model Armor is "a Google Cloud service"; callers use a REST API on regional endpoints (`modelarmor.LOCATION.rep.googleapis.com`) and a template; "The global endpoint (modelarmor.googleapis.com) doesn't support" template management or sanitizing (templates page, overview, 2026-10-09) **[Documented]**
• Generic product-page description: "combines rules-based controls, ML models, and powerful AI reasoning models"; no per-filter mapping is given (product page, 2026-10-09) **[Documented]**
• Product-page feature heading "Malware detection and safe browsing" with the text "Detects malicious files, malware, and unsafe URLs within AI prompts and responses" (product page, marketing text, 2026-10-09) **[Documented]**
• Reputation data source, whether Safe Browsing or another list is used, matching method and refresh rate (checked overview, templates page, product page, REST references, release notes, blog, MCP page; the MCP page only uses a Safe Browsing test page, testsafebrowsing.appspot.com, as a sample phishing URL) **[Not disclosed]**
• Feature availability "varies by region due to dependencies on services that could process data outside the location", and "no data is sent to or processed by the underlying service associated with" a disabled filter (feature availability page, overview, 2026-10-09) **[Documented]**
• The malicious URL filter therefore appears to depend on a separate service that is not available inside limited-support jurisdictions; the service is not named **[Inferred]**
• Filter versions do not apply to this filter: "The filter version setting doesn't affect the Sensitive Data Protection and malicious URL filters." (filter version page, 2026-10-09) **[Documented]**
• Update history, dates only: 2026-03-26 "fixed to improve detection accuracy and reduce the rate of false positives" (release notes, 2026-10-09) **[Documented]**
• Any other update to this filter (no other entry names malicious URL detection in the release notes or the version history) **[Not disclosed]**
• Pricing: standalone use has "no cost for using Model Armor up to 2 million tokens per month" and then "$0.10 per million tokens"; separately, "Security Command Center includes Model Armor with a predefined number of tokens per month at no additional cost" (pricing page, 2026-10-09) **[Documented]**
• Data handling: Model Armor "operates as a stateless service, processing all prompts and model responses entirely in memory"; content is stored only if Cloud Logging is enabled, and `logSanitizeOperations` logs the full content of prompts and responses (overview, logging page, 2026-10-09) **[Documented]**
• Failure behaviour on the Agent Platform route: Model Armor sanitisation is skipped and the request continues when Model Armor is unavailable in the region, temporarily unreachable or returns an error (Agent Platform page, 2026-10-09) **[Documented]**
• Client libraries exist for C#, Go, Java, Node.js, PHP and Python; the C# install line is a pre-release package (`--version 1.0.0-beta05`) (client libraries page, 2026-10-09) **[Documented]**
• Release status of routes: Agent Platform GA (release note 2025-12-03), Agent Gateway GA (2026-06-24), Gemini Enterprise GA (2025-09-16), Google and Google Cloud MCP servers GA (2026-04-22), GKE integration GA (2025-09-15), streaming sanitization GA (2026-07-10), LangChain Preview (LangChain page) **[Documented]**
• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse` and load-balancer Service Extensions other than GKE: no GA or Preview label found on the pages read **[To be verified]**
• Self-hosted or offline option: none described (checked overview, product page, locations page, client libraries page, which all call the managed API) **[Not disclosed]**
### R5
Summary: **Match flag and the matched URLs, no confidence level.** The result gives an execution state, a match state and a list of matched URIs, with character ranges for plain text. Confidence levels cannot be set for this filter. **[Documented]**
Detail:
• Overall result `sanitizationResult.filterMatchState` is `NO_MATCH_FOUND` or `MATCH_FOUND`; `invocationResult` is `SUCCESS`, `PARTIAL` or `FAILURE` (REST result ref, 2026-10-09) **[Documented]**
• `filterResults.malicious_uris.maliciousUriFilterResult` holds `executionState`, `messageItems`, `matchState` and `maliciousUriMatchedItems[]` (REST result ref, 2026-10-09) **[Documented]**
• `matchState` is `MATCH_FOUND` "if at least one Malicious URI is found" (REST result ref, 2026-10-09) **[Documented]**
• Each matched item has the `uri` and `locations[]` (start and end `RangeInfo`); "The locations field is supported only for plaintext content i.e. ByteItemType.PLAINTEXT_UTF8" (REST result ref, 2026-10-09) **[Documented]**
• "You can set confidence levels only for prompt injection and jailbreak detection and responsible AI safety filters." so this filter has no threshold (overview, 2026-10-09) **[Documented]**
• Numeric score, URL category (phishing or malware), or reason for the match: no such field (checked the result reference page) **[Not disclosed]**
• Docs sample outputs on the sanitize page show `malicious_uris` as `NO_MATCH_FOUND` (sanitize page, 2026-10-09) **[Documented]**
• A sample output with `maliciousUriMatchedItems` filled in (checked the sanitize page and the MCP page, which describes only a log entry) **[Not disclosed]**
• Enforcement type in `templateMetadata.enforcementType`: `INSPECT_ONLY` ("No action will be taken on the request") or `INSPECT_AND_BLOCK`; unspecified is "Same as INSPECT_AND_BLOCK" (REST templates ref, 2026-10-09) **[Documented]**
• Overview sample for Inspect and block: an LLM summarising web content includes a link to a known phishing site and "Model Armor blocks the entire LLM response" (overview, 2026-10-09) **[Documented]**
• Apigee sets `maliciousUriFilterResult.executionState`, `maliciousUriFilterResult.matchState`, `maliciousURIs` ("Appended list of malicious URIs detected by the malicious URI filter") and `maliciousURIsDetected` (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**
• Published detection rate, false-positive rate or latency for malicious URL detection (checked overview, best practices, product page, blog, release notes) **[Not disclosed]**
• Template exclusion rules (Preview) list only the prompt injection and jailbreak and the responsible AI filters as supported (exclusion rules page, 2026-10-09) **[Documented]**
### R6
Summary: **A template with the filter on and text containing URLs.** The only setting is on or off. Token limits do not apply, but only the first 256 URLs are scanned, and the location must be full-support or have data residency enforcement turned off. **[Documented]**
Detail:
• The filter runs only if `maliciousUriFilterSettings.filterEnforcement` is `ENABLED` (REST templates ref, 2026-10-09) **[Documented]**
• "Note: To sanitize prompts and responses, you must use regional endpoints." and the template must be in the location of the endpoint (sanitize page, templates page, 2026-10-09) **[Documented]**
• Required before calling: enable `modelarmor.googleapis.com`, create a template, and hold Model Armor User (`roles/modelarmor.user`); creating templates needs Model Armor Admin (`roles/modelarmor.admin`) (sanitize page, templates page, 2026-10-09) **[Documented]**
• Request fields for text: `userPromptData.text`; optional `multiLanguageDetectionMetadata` (sanitize page, 2026-10-09) **[Documented]**
• Positions (`locations`) are returned only for `PLAINTEXT_UTF8` content, so plain text requests give character ranges and file requests do not (REST result ref, 2026-10-09) **[Documented]**
• Limit: scans "only the first 256 URLs found in prompts and responses"; token limits do not apply (overview, quotas page, 2026-10-09) **[Documented]**
• Quota: "1200 queries per minute (QPM) per project", adjustable between 0 and 1,200; over-quota calls show HTTP 429 `RESOURCE_EXHAUSTED` (quotas page, integrations page, 2026-10-09) **[Documented]**
• Location support with data residency enforced: malicious URL detection is listed for eu, europe-southwest1, europe-west1, europe-west3, europe-west4, europe-west9, us, us-central1, us-east1, us-east4, us-west1, plus rows for us-east7 and global, and not for the seven limited-support locations (feature availability page, 2026-10-09) **[Documented]**
• Setting `dataResidencyCompliant` to false enables the other features in limited-support regions, with cross-jurisdictional routing; the template page says "Caution: Cross-jurisdictional routing of your data can impact your data residency compliance." (templates page, release note 2026-08-27, 2026-10-09) **[Documented]**
• The feature table lists `us-east7` and `global` rows that the locations page does not list; the global endpoint "doesn't support managing Model Armor templates or sanitizing prompts and responses" (feature availability page, locations page, data residency page, 2026-10-09) **[Documented]**
• From a VPC network, a Private Service Connect endpoint to the Model Armor APIs is needed to reach regional endpoints (overview, 2026-10-09) **[Documented]**
• Language handling: URLs are not language-dependent; the docs state nothing language-specific for this filter (checked overview, templates page, REST references) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the Model Armor API on, a template with the malicious URL filter enabled in a full-support region, and a script posting prompts with known-bad and benign URLs to the regional sanitize-user-prompt endpoint. Standalone use is free to 2 million tokens a month. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing, the Model Armor API enabled, `roles/modelarmor.admin` to create a template and `roles/modelarmor.user` to call; one template in a regional location with `maliciousUriFilterSettings` set to `ENABLED`; a script that posts each prompt to `:sanitizeUserPrompt` and records `filterMatchState` and `maliciousUriMatchedItems`. **[Inferred]**
• Cost: the premise is the standalone allowance of 2 million tokens a month (R4), so a few thousand short prompts cost nothing **[Inferred]**
• Test data: Google supplies none; start with the phishing test URL used in the MCP docs, then add known-bad URLs from a reputation list you trust and benign URLs from popular and internal sites. Do not open the URLs from the test machine **[Inferred]**
• Variants to test: bare URLs, URLs in markdown links, shortened and redirecting URLs, defanged forms such as hxxp, URL-encoded and Base64 forms, internationalised domains, and IP-address hosts **[Inferred]**
• Test the cap: place a malicious URL after 255, 256 and 257 benign URLs to confirm the first-256 rule **[Inferred]**
• Record `locations` on plain text and compare with the same content sent as a file (R6) **[Inferred]**
• Region: choose a full-support location (for example us-central1). In asia-southeast1 this filter is unavailable with residency enforced; set `dataResidencyCompliant` to false to test it there, accepting cross-jurisdictional routing (feature availability page, release note 2026-08-27) **[Inferred]**
• No self-hosted or offline option is described (R4), so tests need network access to Google Cloud and a billing account **[Inferred]**
### R8
Summary: **Key open questions.** What reputation source and method the filter uses, how obfuscated, shortened and redirecting URLs are handled, accuracy, behaviour past 256 URLs, why it is unavailable in limited-support regions, and whether it checks URLs from images.
Detail:
• Reputation source, categories and refresh rate (checked overview, templates page, product page, REST references, release notes, blog, MCP page; not stated)
• Handling of shortened, redirecting, defanged, encoded and internationalised URLs, and whether the filter fetches pages (not stated; needs testing)
• Which URLs count when a prompt has more than 256: order of appearance is assumed (needs testing)
• Detection rate and false-positive rate on a labelled URL set (no figures published; needs testing)
• Which service the filter depends on, and why it cannot run inside limited-support jurisdictions
• Whether URLs found in images by OCR are checked (see MA10)
• Whether `us-east7` and `global` rows in the feature availability table are real locations for templates, given the locations page lists 16 regions and 2 multi-regions
• Whether input-side use is intended, given the overview frames the filter around returned URLs
• Latency per call: no figure published; the best practices page says "Enabling unnecessary detectors can increase latency" (needs testing)
### R9
Summary: Model Armor documentation pages on docs.cloud.google.com, the Model Armor product page, the Security Command Center pricing page, the Google Cloud blog and the Apigee policy reference.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/set-filter-version
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/locations
• https://docs.cloud.google.com/model-armor/data-residency
• https://docs.cloud.google.com/model-armor/configure-exclusion-rules
• https://docs.cloud.google.com/model-armor/configure-floor-settings
• https://docs.cloud.google.com/model-armor/configure-logging
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/model-armor-apigee-integration
• https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration
• https://docs.cloud.google.com/model-armor/model-armor-networking-integration
• https://docs.cloud.google.com/model-armor/model-armor-langchain-integration
• https://docs.cloud.google.com/model-armor/best-practices
• https://docs.cloud.google.com/model-armor/reference/libraries
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps
• https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy
