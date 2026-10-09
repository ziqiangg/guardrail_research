# Triage items for modelarmor P4. Fields: key, item, locations, class (a/b/c), honest_gap, source/why, priority
# Cross references use {k:key} and are replaced by T-ids at build time.
# Files touched (A/B/INV) are derived from the location text (MAn tokens, "A RN", "B RN", "INV").
ITEMS = []
def add(key, item, loc, cls, src, pri, hg=False):
    ITEMS.append(dict(key=key, item=item, loc=loc, cls=cls, src=src, pri=pri, hg=hg))

# ---------------------------------------------------------------- defaults, thresholds, result semantics
add("rai_default",
    "Default confidence level when a RAI category omits it: templates page console note says High; REST reference says unspecified is the same as LOW_AND_ABOVE and RAI uses 'a reasonable default level based on the filterType'; floor-settings page console note says Medium and above. No page says which applies to an API-created template",
    "MA1 R5 (Summary 'two different defaults'; 3 bullets), MA1 R8; MA2 R5 (3 bullets), MA2 R8; INV(a) RAI Default cell [TBV]; INV(c) raiSettings Default; INV(c) Floor-setting levels Default; INV RN 1.3; A RN-8; BR C3",
    "b",
    "Needs testing: create templates with the level omitted by REST, gcloud and console, send graded prompts, compare with explicit LOW_AND_ABOVE, MEDIUM_AND_ABOVE and HIGH templates (queue: C3 needs-testing). Documentation half is {k:rai_default_doc}",
    "H")
add("rai_default_doc",
    "MA1 and MA2 R5 give two default statements (console High, REST unspecified) but not the third one that INV and B record (floor-settings page: Medium and above for RAI). The R5 Summary 'Google states two different defaults' therefore understates the conflict",
    "MA1 R5 (Summary and bullets), MA2 R5; INV(a) RAI Default; INV(c) Floor-setting levels Default; INV RN 1.3; B RN-2.8",
    "a",
    "configure-floor-settings (console note), manage-templates (console steps), REST templates ref. Merger adds the floor-settings bullet and adjusts the Summary count",
    "H")
add("pi_default",
    "Default PI and jailbreak level when omitted: A writes [Inferred] 'would behave as Low and above' and says no page has a separate default; INV records [Documented] that floor settings default PI to LOW_AND_ABOVE and that the REST enum treats unspecified as LOW_AND_ABOVE. Same fact, two labels; the template default (as opposed to the floor-setting default) is still untested",
    "MA3 R5 (Inferred bullet), MA3 R7, MA3 R8; MA4 R5 (Inferred bullet), MA4 R8; INV(a) PI Default; INV(c) piAndJailbreakFilterSettings Default; INV(c) Floor-setting levels Default; INV RN 1.3",
    "a",
    "configure-floor-settings (statement that the PI level defaults to LOW_AND_ABOVE), REST templates ref. Align A to INV: floor-setting default Documented, template default stays Inferred or To be verified; residual test falls under {k:rai_default}",
    "H")
add("pi_advice_doc",
    "PI and jailbreak threshold advice conflict (C1): overview example strategy says Medium (High for Gemini Enterprise); templates page says High; overview table calls Low and above 'potentially suitable' for high-stakes categories; floor-settings illustration uses Medium; docs examples use High and Low and above. R5 Summary states the conflict",
    "MA3 R5 (Summary; 4 bullets), MA3 R8; MA4 R5 (Summary; 4 bullets), MA4 R8; INV(a) PI Levels; INV(c) piAndJailbreakFilterSettings Effect; INV RN 1.1; A RN-7; BR C1",
    "a",
    "overview, manage-templates, best-practices, Gemini Enterprise page, release notes (does a later note change the advice?). Record page dates; no pin exists for docs",
    "H")
add("pi_level_test",
    "Which PI and jailbreak level to use: detection and false-positive trade-off at the three levels on a labelled prompt set, per filter version (v3 against v4)",
    "MA3 R7, MA3 R8; MA4 R7, MA4 R8",
    "b",
    "Needs testing with labelled attacks and benign near-misses (Google supplies none); one template per level and per version. Doc half is {k:pi_advice_doc}",
    "M")
add("conf_meaning",
    "Whether confidenceLevel in a result is the detected or the configured level, and whether PI results carry it at all: Python sample prints HIGH for a matched PI result, REST JSON sample shows no confidence field, RAI response sample shows MEDIUM_AND_ABOVE. MA3 and MA4 R5 Summary says the result gives 'a confidence level'",
    "MA1 R5, MA1 R8; MA2 R5, MA2 R8; MA3 R5 (Summary; 1 bullet), MA3 R8; MA4 R5 (Summary; response example bullet); A RN-17; INV(a) RAI Result field; INV(a) PI Result field",
    "b",
    "Needs testing: send one prompt through templates set at each level and compare the returned level. Doc half: the field description in SanitizationResult ('Confidence level identified for this RAI filter')",
    "H")
add("three_word",
    "Whether the three-word PI minimum applies to responses (overview and quotas wording says 'inputs')",
    "MA4 R5 [TBV], MA4 R7, MA4 R8; INV(e) PI minimum word count",
    "b",
    "Needs testing: short responses on a PI-enabled template. Doc half: overview and quotas wording",
    "M")
add("ip_sample",
    "MA2 R5 Summary leads with the docs sample 'IP address of the current network is ##.##.##.##' flagged Dangerous at MEDIUM_AND_ABOVE; Detail says the page does not say whether it is real output. Whether masked data triggers Dangerous is unknown",
    "MA2 R5 (Summary; 2 bullets), MA2 R8; A RN-17",
    "b",
    "Re-send the sample text to a RAI template and record the result; if it does not reproduce, drop the sentence from the Summary",
    "H")

# ---------------------------------------------------------------- CSAM
add("csam_doc",
    "CSAM filter 'applied by default and cannot be turned off' (overview) against the feature-availability table showing CSAM 'No' in all seven limited-support locations with data residency enforced. The R1 Summaries assert it always runs; INV(a) CSAM Default says 'Always on' while its Limit cell says not available in limited regions",
    "MA1 R1 (Summary), MA1 R2 (one bullet holding both sides), MA1 R8; MA2 R1 (Summary), MA2 R2, MA2 R8; INV(a) CSAM Default and Limit; INV(d) CSAM column (7 limited rows); A RN-4 (C14); queue C14",
    "a",
    "feature-availability-by-region, data-residency, locations, overview, release notes 2026-08-27 and 2026-09-04 (does turning residency enforcement off enable CSAM?)",
    "H")
add("csam_test",
    "Observed CSAM behaviour in a limited-support location (executionState and matchState of the csam result on benign text) with residency enforcement on and off",
    "MA1 R7, MA1 R8; MA2 R7, MA2 R8; INV(a) CSAM row",
    "b",
    "Needs testing in asia-southeast1 or another limited location. No CSAM material may be built (MA1 R7); read executionState only. Doc half is {k:csam_doc}",
    "H")

# ---------------------------------------------------------------- OCR text
add("ocr_doc",
    "Whether RAI, PI and malicious URL filters run on text read from images by OCR (and on visual-scan output). Labels differ: MA1, MA3, MA7 [TBV]; MA10 R2 [ND] ('which filters examine the OCR text is not listed') plus two [INF] bullets; INV(a) OCR row says the filters follow the template, [Documented] from the REST modality note",
    "MA1 R3 [TBV], MA1 R8; MA3 R3 [TBV], MA3 R8; MA7 R2 [TBV], MA7 R8; MA8 R2 [TBV] (generated images), MA8 R8; MA10 R1 (Summary), MA10 R2 (Summary; ND bullet; 2 INF bullets), MA10 R8; INV(a) Image OCR row; INV(a) Image visual row; queue (RAI, PI, URL on OCR)",
    "a",
    "REST templates ref modality text ('depending on the filter configuration'), overview image section, sanitize page image examples, manage-templates. Queue routes this to the P5 resolver; align the labels in all five columns after it",
    "H")
add("ocr_test",
    "The same question by test: image carrying harmful text, an injection and a phishing URL, sent to a us or eu template with RAI, PI and URL filters on; which filter results appear",
    "MA10 R2, MA10 R8; MA1 R8; MA3 R8; MA7 R8; MA8 R8",
    "b",
    "Needs testing (image modality is Preview, us and eu only). Doc half is {k:ocr_doc}",
    "H")

# ---------------------------------------------------------------- response-side PI
add("pi_resp_doc",
    "MA4 R1 Summary says the overview, a sample response output and the Apigee response policy 'all show' the filter running on responses, labelled [Documented], while Detail calls that reading [Inferred] and the templates page says 'in a prompt'. INV(a) records Applies to as Input and Output [Documented]",
    "MA4 R1 (Summary; 5 bullets), MA4 R8; INV(a) PI Applies to; A RN-14 (C12); queue C12",
    "a",
    "overview, manage-templates, REST method page for sanitizeModelResponse, Apigee SanitizeModelResponse policy. Decide Summary label (weakest is Inferred) or reword to state the three texts separately",
    "H")
add("pi_resp_test",
    "Does the PI filter fire on a response (injection in a retrieved page or tool result, a reply obeying an injection) and what does a response-side match return. No positive response-side example exists; release notes do not say whether model updates apply to responses",
    "MA4 R1 (ND bullet), MA4 R2 (ND), MA4 R4 (ND bullet), MA4 R7, MA4 R8",
    "b",
    "Needs testing with response-side payloads at the three levels. Doc half is {k:pi_resp_doc}",
    "H")
add("pi_taxonomy",
    "PI and jailbreak attack taxonomy, benchmark coverage, indirect injection, multi-turn and obfuscated coverage, and what response-side detection is meant to catch. The only list is the 2025-09-23 release note (improved vectors, upgraded model in the EU multi-region)",
    "MA3 R2 (Summary lists the 4 vectors; 2 ND bullets), MA3 R8; MA4 R2 (ND bullet), MA4 R8; BR G4",
    "b",
    "Honest gap: checked overview, product page, templates page, version history, release notes, blog, none gives a taxonomy. Only a labelled attack set can map coverage",
    "M", hg=True)

# ---------------------------------------------------------------- userPrompt
add("userprompt_doc",
    "Optional userPrompt field of sanitizeModelResponse: A says only the Go client documents it and 'the docs pages do not mention it'; B quotes the REST method reference ('Optional. User Prompt associated with Model response.'). The Apigee SanitizeModelResponse policy page also has a UserPromptSource element and a userPrompt flow variable. Cross-file contradiction; MA2 R3 Summary and MA6 R3 Summary say different things",
    "MA2 R3 (Summary; 3 bullets), MA2 R6, MA2 R8; MA4 R3, MA4 R6, MA4 R8; MA8 R3 (Summary; bullet), MA8 R8; MA6 R3 (Summary; 2 bullets), MA6 R6, MA6 R8; A RN-3; B RN-2.1; queue C16",
    "a",
    "REST method page .../projects.locations.templates/sanitizeModelResponse (200 per B), Apigee sanitize-llm-response policy page (already in MA2 R9), Go proto comment at 37f936ac. Unify the claim and add the method URL to R9 of MA2, MA4 and MA8",
    "H")
add("userprompt_effect",
    "What the optional userPrompt changes (whether any filter uses it as context)",
    "MA2 R3 (ND), MA2 R7, MA2 R8; MA4 R3 (ND), MA4 R7, MA4 R8; MA6 R3 (ND), MA6 R8; MA8 R8",
    "b",
    "Needs testing: same response with and without the field. Honest gap if no page explains the field. Doc half is {k:userprompt_doc}",
    "M", hg=True)

# ---------------------------------------------------------------- Go client lag, status
add("go_lag",
    "Docs describe filterVersionSelector, filterRuleSettings, dataResidencyCompliant and the GOOGLE_MCP_SERVER floor setting; the Go v1 client at google-cloud-go@37f936ac (module 1.3.0) has none of them (apiv1beta has the MCP service); the sanitize page Go streaming sample imports apiv1beta. A records ND bullets, INV records repo facts. No conclusion drawn",
    "MA3 R4 (ND bullet); MA4 R4 (ND bullet); INV(b) Client libraries Limitations; INV(c) filterVersionSelector; INV RN 1.11; A RN-3; A RN-6; queue C16",
    "a",
    "apiv1beta protos and CHANGES.md at the pinned sha, other-language clients in googleapis repos (shallow clone, R013), reference/libraries. Say 'client lags' only as [Inferred]",
    "M")
add("excl_schema",
    "Exclusion rules schema gap (C11): the exclusion-rules page shows filterConfig.filterRuleSettings (ruleSets, rules, exclusionRule) in v1 requests, but the REST FilterConfig lists four settings only and the Go v1 client has no such field. Feature is Preview (release note 2026-09-28)",
    "MA3 R5 ([TBV] bullet), MA3 R8; MA4 R5 ([TBV] bullet), MA4 R8; INV(c) filterRuleSettings Where set; INV RN 1.8; A RN-13; BR C11",
    "a",
    "REST templates ref (FilterConfig field list), configure-exclusion-rules, release note 2026-09-28, go_lag sources; if the docs do not settle it, a template-create test decides",
    "M")
add("apigee_status",
    "Apigee SanitizeUserPrompt and SanitizeModelResponse policies: GA or Preview. No label on the Apigee integration page or on either policy page",
    "MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (shared [TBV] bullet); MA5 R4 (Apigee bullet); MA6 R4, MA6 R8; INV(b) Apigee Status; BR G8; queue (Apigee status to P5 resolver)",
    "a",
    "Apigee docs release notes, Apigee integration page, both policy reference pages, apigee-samples README at 2b1a9f00, Model Armor release notes",
    "M")
add("se_status",
    "GA date for Service Extensions on load balancers other than GKE and for Secure Web Proxy",
    "MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (shared [TBV] bullet); INV(b) Service Extensions Status",
    "a",
    "Model Armor release notes, networking integration page, Cloud Load Balancing and Secure Web Proxy release notes",
    "L")
add("mcp_status",
    "MCP integration status: release note 2026-04-22 says GA; the floor-settings page links it as '(Preview)'. MA6 R4 holds both as a labelled pair; MA1 to MA4, MA7 and MA8 R4 and INV(b) MCP row state GA from the release note only",
    "MA6 R4 (2 bullets), MA6 R8; MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (release-status bullet); INV(b) MCP Status; INV(c) Floor-setting inline Status; B RN-2.6; queue (release note beats undated page label)",
    "a",
    "Queue ruling already prefers the dated release note and keeps both as a labelled pair; apply that pair in every location, not only MA6. Floor-settings page and MCP page to re-read",
    "M")
add("rule_s",
    "Inventory status rule S: 21 cells carry 'GA [Inferred] (status rule S)' (INV(a) 7 rows, INV(b) direct REST 1, INV(c) 13 rows) because no Pre-GA banner exists; the rule is applied unevenly (Apigee [TBV], gcloud, console, Terraform, SCC [ND] although they also lack a banner)",
    "INV intro; INV(a) RAI, CSAM, PI, URL, SDP basic, SDP advanced, Document extraction Status; INV(b) Direct REST Status; INV(c) 13 Status cells; INV RN 3",
    "a",
    "Release notes (earliest Model Armor GA entry), overview, product page: does any page state GA for the base service? If not, keep [Inferred] with the premise or use the column's own 'Not documented' value consistently",
    "M")
add("terraform",
    "Terraform resource page for Model Armor templates and floor settings not read; only release note 2025-07-29 supports the row. registry.terraform.io is HashiCorp's, not an official source (queue ruling)",
    "INV(b) Terraform row (Status [ND]; Limitations [TBV]; Source URL release notes only); BR G12; queue (Terraform registry not official)",
    "a",
    "Google's own Terraform documentation on docs.cloud.google.com (provider reference page for the Model Armor resources) and release note 2025-07-29; if none is found, keep [TBV]",
    "M")
add("lib_versions",
    "Java, Node.js, PHP and Python library versions are [ND]; Go module 1.3.0 against C# 1.0.0-beta05 (pre-release); Go apiv1 package lags the docs",
    "MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (client libraries bullet); INV(b) Client libraries row",
    "a",
    "reference/libraries; googleapis repos for java, nodejs, php, python by shallow clone (R013)",
    "L")
add("deid_forward",
    "Whether Agent Gateway and Service Extensions forward de-identified text: Agent Gateway intro says 'block and redact', its flow text says 'allows or blocks'; networking page says 'allow, block, or modify'. Only Apigee documents extracting redacted data",
    "MA5 R4 (ND bullet); MA6 R4, MA6 R8; INV(b) Agent Gateway ingress; INV(b) Agent Gateway egress; INV(b) Service Extensions; B RN-2.5",
    "a",
    "Agent Gateway, networking and integrations pages (re-read the flow text); if silent, falls to testing (needs those routes)",
    "M")

# ---------------------------------------------------------------- honest gaps and measurements
add("model_id",
    "Backing model, architecture, training data and labelling for the RAI and PI filters, and whether the input and output sides share a model or configuration. The R4 Summaries carry [Not disclosed]",
    "MA1 R4 (Summary), MA1 R8; MA2 R4 (Summary; 2 ND bullets), MA2 R8; MA3 R4 (Summary), MA3 R8; MA4 R4 (Summary), MA4 R8; INV(a) intro; INV(a) RAI row; INV(a) PI row; BR G1",
    "b",
    "Honest gap: managed Google service; checked overview, product page, filter-version pages, release notes, REST refs, blog, best practices. Only release-note phrases ('uses a new model') exist. No public document is expected to answer",
    "H", hg=True)
add("url_source",
    "Malicious URL reputation source, categories, refresh rate, whether pages are fetched, and which separate service the filter depends on (it is unavailable in limited-support locations)",
    "MA7 R2 (ND), MA7 R4 (Summary; 2 ND bullets), MA7 R8; MA8 R2 (ND), MA8 R4 (Summary), MA8 R8; INV(a) URL row; INV(d) Supported filters column",
    "b",
    "Honest gap: checked overview, templates page, product page, REST refs, release notes, blog, MCP page. The data-residency and feature-availability pages only say 'dependencies on services' without naming them",
    "H", hg=True)
add("ocr_engine",
    "OCR engine, image models and the document text extractor are not described; R4 Summaries of MA9 and MA10 say so under a [Documented] label",
    "MA9 R2 (ND bullet), MA9 R4 (Summary; ND bullet), MA9 R8; MA10 R4 (Summary; ND bullet), MA10 R8",
    "b",
    "Honest gap: checked overview, sanitize page, templates reference, product page, release notes, blog",
    "H", hg=True)
add("accuracy",
    "Published accuracy, recall, F1 or false-positive rates for every filter and for OCR and extraction: none. The R5 Summaries of MA5, MA6, MA9 and MA10 state that no score or accuracy figure is published; other columns carry the [ND] bullet in Detail",
    "MA1 R5, MA1 R8; MA2 R5, MA2 R8; MA3 R5, MA3 R8; MA4 R5, MA4 R8; MA5 R5 (Summary), MA5 R8; MA6 R5 (Summary), MA6 R8; MA7 R5, MA7 R8; MA8 R5, MA8 R8; MA9 R5 (Summary), MA9 R8; MA10 R5 (Summary; ND bullet), MA10 R8; INV(a) intro; BR G2",
    "b",
    "Needs testing: labelled benchmark per category, level, language and modality (Google advises testing 'against a representative dataset'). Absence claims name the pages checked",
    "H")
add("latency",
    "Latency per call and any SLA for the Model Armor API: no figure; best-practices only says unnecessary detectors can increase latency. SLA exists only on the Gemini Enterprise page",
    "MA1 R8, MA2 R8, MA3 R8, MA4 R8, MA7 R8, MA8 R8 (latency bullet); MA5 R8; MA6 R8; BR G3",
    "b",
    "Needs testing: repeated timed calls per filter, per modality, per location (cloud network effects). Honest gap for any vendor figure",
    "M", hg=True)
add("lang",
    "Language coverage beyond the nine tested languages (Singlish, Malay, Tamil), and non-English behaviour in asia-southeast1 (the Skipped Detection note names only asia-south1 and northamerica-northeast2)",
    "MA1 R7, MA1 R8; MA2 R7, MA2 R8; MA3 R7, MA3 R8 (asia-southeast1 bullet); MA4 R7",
    "b",
    "Needs testing in a full-support location and in asia-southeast1 with residency on and off; doc half is {k:skipped_regions}",
    "M")
add("skipped_regions",
    "Skipped Detection for non-English content is documented for two locations only; the feature table shows Multi-language 'No' for all seven limited-support locations; INV(d) repeats the note for two rows",
    "MA1 R2, MA2 R2, MA3 R2, MA4 R2 (sanitize-page bullet); MA3 R8; INV(d) asia-south1 and northamerica-northeast2 Multi-language; INV RN 1.12; A RN-18",
    "a",
    "sanitize page, feature-availability, data-residency, release notes 2026-06-22 and 2026-08-27",
    "M")
add("tool_json",
    "Whether structured tool output (JSON, code) causes PI false positives, given the MCP tip to enable the filter only for natural-language traffic",
    "MA4 R7, MA4 R8; INV(b) MCP row Limitations",
    "b",
    "Needs testing with JSON and code tool results",
    "L")

# ---------------------------------------------------------------- topic, absence, URL
add("topic",
    "Topic enforcement (C10): overview scenario 'Enforce custom topics' and the 'topicality' mention against no configuration setting or page",
    "MA1 R2 (2 bullets), MA1 R8; MA2 R2 (2 bullets), MA2 R8; INV(a) intro; A RN-12; BR C10",
    "a",
    "Re-read overview scenario and confidence-level paragraph, exclusion rules page and SDP custom infoType pages; if still no setting keep [ND]. Brief rules out a column or row",
    "M")
add("absence",
    "Absence claims for functions Model Armor does not offer: hallucination or grounding, refusal detection, system-prompt leakage, topic enforcement",
    "MA1 R2 (refusal bullet); MA2 R2 (hallucination and refusal bullets); MA4 R2 (system-prompt leakage bullet); INV(a) intro",
    "a",
    "Low risk. Re-run the page searches on the final docs at P5 (REST FilterConfig, overview filter list, templates detection list, blog)",
    "L")
add("url_input",
    "Overview frames the malicious URL filter mainly around returned URLs; templates page, product page and blog say prompts and responses. MA7 R1 Summary repeats the 'mainly' reading",
    "MA7 R1 (Summary; 2 bullets), MA7 R8",
    "a",
    "overview, manage-templates, product page, blog; reword Summary or label the 'mainly' judgement [Inferred]",
    "L")
add("url_order",
    "Which URLs count when a prompt or response has more than 256 (order of appearance is assumed)",
    "MA7 R2 (Inferred bullet), MA7 R7, MA7 R8; MA8 R2 (Inferred bullet), MA8 R7, MA8 R8; INV(e) URLs scanned",
    "b",
    "Needs testing: malicious URL after 255, 256 and 257 benign URLs",
    "M")
add("url_variants",
    "Handling of shortened, redirecting, defanged, encoded and internationalised URLs; whether the filter fetches pages",
    "MA7 R2 (ND bullet), MA7 R7, MA7 R8; MA8 R2 (ND bullet), MA8 R7, MA8 R8",
    "b",
    "Needs testing with safe test URLs (Google's own phishing test URL in the MCP docs); do not open URLs from the test machine",
    "M")
add("url_stream",
    "URL split across two streamed chunks in real-time mode",
    "MA8 R3 (Inferred bullet), MA8 R7, MA8 R8",
    "b",
    "Needs testing with StreamSanitizeModelResponse in real-time mode",
    "L")

# ---------------------------------------------------------------- SDP (MA5, MA6)
add("basic_count_doc",
    "Basic SDP infoTypes: six (overview, REST 'fixed set of six') or seven (sanitize page adds PASSWORD; SSN and ITIN only for 'US-based regions'). MA5 R2 Summary says the pages disagree",
    "MA5 R2 (Summary; 4 bullets), MA5 R8 (Summary; bullet 1); MA6 R2 (conflict bullet), MA6 R8; INV(a) SDP basic Levels; INV RN 1.2; B RN-2.4; BR C2",
    "a",
    "overview, REST templates ref, sanitize page, Go proto comment for SdpBasicConfig at 37f936ac, release notes (when was PASSWORD added?)",
    "H")
add("basic_count_test",
    "Live basic-mode infoType list per location (six or seven, PASSWORD present, SSN and ITIN only in US locations)",
    "MA5 R8; MA6 R8 (via basic-list bullet); INV(a) SDP basic Levels",
    "b",
    "Needs testing: one string per infoType through a basic-mode template in a US and a non-US location. Doc half is {k:basic_count_doc}",
    "M")
add("us_regions",
    "Which locations count as 'US-based regions' for the SSN and ITIN detectors",
    "MA5 R2 (ND bullet), MA5 R8; INV(a) SDP basic Levels",
    "a",
    "sanitize page, overview, feature-availability, data-residency; if undefined it joins {k:basic_count_test}",
    "M")
add("basic_resp",
    "Whether the basic infoType list also applies to responses (the page introduces the lists as 'scanned in the prompt'); MA6 R2 Summary says the docs do not say",
    "MA6 R2 (Summary; ND bullet), MA6 R8; INV(a) SDP basic Applies to; B RN-2.4",
    "b",
    "Needs testing: response containing a PASSWORD or card string through a basic-mode template. Honest gap on the docs side (sanitize page, overview, templates page and REST ref checked)",
    "H")
add("sdp_resp_result",
    "No documented response-side de-identification example: shape of a response-side deidentifyResult and findings is unknown (the sanitizeModelResponse example has no sdp result)",
    "MA6 R3 (Summary; 2 ND bullets), MA6 R5 (ND bullet), MA6 R7 (first test), MA6 R8; INV(a) SDP advanced Result field",
    "b",
    "Needs testing with an advanced template plus de-identify template on sanitizeModelResponse",
    "H")
add("likelihood",
    "How a likelihood becomes a match and whether a hidden minimum-likelihood threshold exists in basic mode (belongs to SDP; Model Armor overview points to 'match likelihood')",
    "MA5 R5 (Inferred bullet), MA5 R8; MA6 R5",
    "b",
    "Needs testing in basic mode; SDP internals are covered by the SDP product columns (R012)",
    "M")
add("filterresults_shape",
    "filterResults shape: REST reference says a keyed map; the sanitize page SDP examples show an array of objects",
    "MA5 R5 (2 bullets), MA5 R8; MA6 R5 (bullet); B RN-3",
    "a",
    "SanitizationResult ref, Go proto field type for filter_results at 37f936ac, sanitize page examples; test if the code does not settle it",
    "M")
add("findings_with_deid",
    "Whether a findings list with positions is returned together with a de-identified copy",
    "MA5 R5 (ND bullet), MA5 R8; INV(a) SDP advanced Result field",
    "b",
    "Needs testing with inspect plus de-identify templates",
    "M")
add("deid_inspect_only",
    "Whether de-identified text, or redactedImage, is returned when enforcement is INSPECT_ONLY",
    "MA5 R8; MA6 R8; MA10 R8",
    "b",
    "Needs testing with enforcement INSPECT_ONLY",
    "M")
add("floor_adv",
    "Whether floor settings accept an advanced inspect template (same-location rule, global floor-setting location, floor settings do not check SDP conformance)",
    "MA5 R6 (floor-settings bullets), MA5 R8",
    "a",
    "configure-floor-settings, Agent Platform integration page; test if silent",
    "M")
add("sdp_quota",
    "SDP quota use, added latency and any effect of multi-language detection on the SDP filter",
    "MA5 R6 (2 ND bullets), MA5 R8; MA6 R6 (ND bullet), MA6 R8",
    "b",
    "Honest gap on quota (quotas page, integrations page checked); the rest needs testing",
    "L", hg=True)
add("token_semantics",
    "Over-limit behaviour is stated as 'skipped' in MA5 and MA6 R6 Summaries ('Text over 130,000 tokens is skipped') and in R6 Detail of MA1 to MA4, MA9; the quotas page (and INV(e)) say a filter that finds a match still returns MATCH_FOUND and EXECUTION_SKIPPED appears only when no match was found within the limit",
    "MA1 R6, MA2 R6, MA3 R6, MA4 R6 (over-limit bullet); MA5 R5, MA5 R6 (Summary; bullet); MA6 R5, MA6 R6 (Summary; bullet); MA9 R5, MA9 R6; INV(a) RAI, CSAM, PI Limit; INV(e) token limit rows",
    "a",
    "quotas page ('If a filter detects a match, it returns MATCH_FOUND. If a filter doesn't detect a match, the value it returns depends on whether the prompt or response exceeds the filter's token limit'); the drafter's local copy already shows it. Reword the Summaries",
    "H")
add("limit_int",
    "Whether the 130,000-token SDP limit applies to the text sent by integrations (Gemini Enterprise is exempt per quotas page)",
    "MA5 R8, MA5 R6",
    "a",
    "quotas page, integrations page",
    "L")
add("chunk",
    "Real-time streaming 'unlimited tokens' is stated without the sanitize-page caveat that individual chunks must not exceed the token limits (INV(e) has the caveat)",
    "MA1 R6, MA2 R6, MA3 R6, MA4 R6 (streaming bullet); MA5 R6; MA6 R3 (streaming bullet); INV(e) Real-time streaming row",
    "a",
    "quotas page and sanitize page ('make sure that individual chunks don't exceed the token limits')",
    "M")
add("sg_nric",
    "R7 says a Singapore NRIC test needs an advanced template with a custom detector; the SDP drafts document a built-in SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER infoType available in all locations (sdp_cols_a.md SD1 R2; sdp_cols_b.md). Cross-product contradiction",
    "MA5 R7 (Summary context; Inferred bullet); MA6 R7 (Inferred bullet); sdp_cols_a.md line 27; sdp_cols_b.md line 229",
    "a",
    "SDP infoTypes reference (via the SDP drafts and their resolver); reword R7 so a built-in infoType placed in an inspect template is the route. No Model Armor page needed",
    "M")
add("sdp_xref",
    "Forward references to 'the Sensitive Data Protection columns on sheet 3' (R012) depend on the SDP CP1 outcome (column split, prefix); the [Inferred] premise that Model Armor docs link out to SDP docs",
    "MA5 R1 (Inferred bullet), MA5 R7; MA6 R1 (Inferred bullet); MA10 R1 (Inferred bullet), MA10 R2; B RN-4",
    "a",
    "INV RN 5 says link targets on overview, integrations and MCP pages were read from raw HTML; re-check the premise, then confirm wording after the SDP CP1 ruling",
    "L")

# ---------------------------------------------------------------- documents and images
add("antivirus",
    "Antivirus scanning: result type virusScanFilterResult (PDF only), region-table row, release note 2026-04-10 and the product-page line 'Detects malicious files, malware' exist, but no configuration setting or page was found. MA9 R1 and R2 Summaries do not mention it; MA7 and MA8 call it 'a separate capability' [Documented]",
    "MA9 R1 ([TBV] bullet; 2 bullets), MA9 R4 (2 bullets), MA9 R8; MA7 R2 (last bullet); MA8 R2 (last bullet); INV(a) Antivirus row; INV(d) Antivirus column; INV RN 1.7; A RN-19; BR C7, G6",
    "a",
    "Re-read templates page, REST FilterConfig, overview, release notes (2026-04-10 and earlier), product page and Security Command Center docs for an antivirus setting. If real, MA9 R1/R2 Summaries need a clause; CP1 decision D4",
    "H")
add("embedded_doc",
    "Images embedded in files (C4): overview 'doesn't screen images embedded within files'; integrations page says the same for Gemini Enterprise; Gemini Enterprise page says it screens images contained inside uploaded files. MA9 R2 Summary notes it",
    "MA9 R2 (Summary; 3 bullets), MA9 R8; MA10 R2 (2 bullets), MA10 R8; INV(a) Image OCR Limit; INV(b) Gemini Enterprise Limitations; INV RN 1.4; B RN-3; BR C4",
    "a",
    "overview image section, integrations page, Gemini Enterprise page, release notes 2025-09-16. Note INV(a) OCR Limit cell states only the overview side",
    "H")
add("embedded_test",
    "Embedded image in a PDF or DOCX: screened or not, by the REST API and by Gemini Enterprise",
    "MA9 R7, MA9 R8; MA10 R8",
    "b",
    "Needs testing in both routes; the Gemini Enterprise route needs a Gemini Enterprise subscription (separate access). Doc half is {k:embedded_doc}",
    "M")
add("ge_modal",
    "Gemini Enterprise modalities: integrations options table lists 'Text, documents'; its own page also lists images uploaded directly and inside files",
    "MA9 R8; MA10 R3 (2 bullets), MA10 R4, MA10 R8; INV(b) Gemini Enterprise Modalities; B RN-2.3",
    "a",
    "integrations page, Gemini Enterprise integration page, release notes 2025-09-16 and 2026-06-25",
    "M")
add("resp_files",
    "Response-side file and image support (G7; CP1 alt (e)): schema (modelResponseData is a DataItem), Go types, overview ('prompts and responses') and release note 2026-06-25 say yes; no request body or result for a response file or image is shown anywhere. Both MA9 R3 and MA10 R3 Summaries state the gap",
    "MA9 R3 (Summary; 2 bullets), MA9 R7, MA9 R8; MA10 R3 (Summary; 5 bullets), MA10 R7, MA10 R8; MA2 R2 (response-side bullet), MA2 R8; MA6 R3 (files bullet); MA8 R2 (generated images), MA8 R8; INV(a) OCR, Visual scanning, Document extraction Applies to; B RN-1; BR Q-A",
    "b",
    "Needs testing: file and image in modelResponseData via REST (us or eu for images). The documentation ceiling is reached (B read method page, DataItem page, release notes). Decides CP1 alt (e): 10 versus 14 columns",
    "H")
add("extractor",
    "Document extractor behaviour: scanned or image-only PDFs, tables, hidden text, comments, password-protected and corrupt files",
    "MA9 R2 (ND bullet), MA9 R8",
    "b",
    "Needs testing with crafted files; vendor internals are covered by {k:ocr_engine}",
    "M")
add("oversize",
    "Result returned for a file over 4 MB (skipped how: error or filter result); release note 2025-09-27 speaks of a 4 MB limit for 'files and text'",
    "MA9 R5 (ND bullet), MA9 R6 (release-note bullet), MA9 R8; MA10 R6; INV(e) File and image size",
    "b",
    "Needs testing with a 4 MB plus file and a 4 MB plus text; doc half: quotas page, overview, release notes",
    "M")
add("formats",
    "Older Office formats, RTF, HTML, GIF, WebP, TIFF, HEIC: ignored, rejected or failed",
    "MA9 R2 (ND bullet), MA9 R8; MA10 R2 (ND bullet), MA10 R8",
    "b",
    "Needs testing",
    "L")
add("file_tokens",
    "How files, extracted text and images are counted in tokens for limits, quotas and billing",
    "MA9 R4 (ND bullet), MA9 R8; MA10 R4 (ND bullet), MA10 R6 (ND bullet), MA10 R8; INV(e) Token definition",
    "b",
    "Honest gap: pricing page, quotas page and overview checked, not stated; metering needs a billing report after test runs",
    "M", hg=True)
add("rich_doc",
    "Rich documents with metadata labels (release note 2026-04-06): request fields beyond a custom infoType in an advanced SDP configuration",
    "MA9 R2 (bullet), MA9 R8; INV(a) Document extraction",
    "a",
    "Release note 2026-04-06, sanitize page, SDP docs on metadata-label infoTypes",
    "L")
add("xltm",
    "REST enum text reads XLYM where overview and release notes read XLTM (typo-like)",
    "MA9 R2 (bullet); B RN-2.2",
    "a",
    "DataItem reference vs overview; record as a vendor typo if no correction exists",
    "L")
add("file_result",
    "File result details: which response field returns fileLabel, whether filters report page or sheet, and regional limits for documents (the region tables do not list documents)",
    "MA9 R5 (ND bullet), MA9 R6 (ND bullet), MA9 R8",
    "a",
    "SanitizationResult ref, DataItem ref, feature-availability; test if silent",
    "L")
add("langchain",
    "Whether LangChain 'scans only the extracted text' means document support or text extracted client-side",
    "MA9 R3 (bullet), MA9 R8; INV(b) LangChain row",
    "b",
    "Honest gap and out of scope: LangChain internals beyond the Model Armor page are excluded by the brief",
    "L", hg=True)
add("bbox",
    "Image finding location: REST reference gives boundingBoxes (list); sanitize page example shows boundingBox (object)",
    "MA10 R5 (2 bullets), MA10 R8; INV(a) Visual scanning Result field",
    "a",
    "SanitizationResult ref and Go proto ImageFindingLocation at 37f936ac; test if the code does not settle it",
    "M")
add("include_findings",
    "What include_findings in the SDP template is and where it is set (redact-result findings appear only when true)",
    "MA10 R5 (2 bullets), MA10 R8; B RN-2.10",
    "a",
    "SanitizationResult ref, Go comment at 37f936ac:3586, SDP docs (SDP product columns)",
    "M")
add("csam_pixels",
    "Whether the CSAM filter analyses image pixels (the image example output has a csam result)",
    "MA10 R2 (ND bullet), MA10 R8; INV(a) CSAM row",
    "b",
    "Honest gap: overview and sanitize page checked, not stated; CSAM material may not be built, so only benign-image result structure can be tested",
    "M", hg=True)
add("ocr_lang",
    "OCR languages, handwriting, rotated and low-resolution text",
    "MA10 R2 (ND bullet), MA10 R6 (ND bullet), MA10 R8",
    "b",
    "Needs testing with image sets per language",
    "M")
add("image_ga",
    "When image screening reaches GA and other locations",
    "MA10 R8; INV(a) OCR and Visual scanning Status",
    "b",
    "Honest gap: release notes checked, no date; future statement",
    "L", hg=True)
add("two_images",
    "Behaviour when a second image is sent in one request",
    "MA10 R6; INV(e) Images per request [ND]",
    "b",
    "Needs testing",
    "L")
add("modality_unspec",
    "MODALITY_UNSPECIFIED is 'all modalities' in the REST reference while an empty modalities field scans text only",
    "MA9 R6; MA10 R6; INV(a) Image OCR Default; INV(c) modalities; B RN-2.12",
    "a",
    "REST templates ref vs manage-templates; record both as already done",
    "L")

# ---------------------------------------------------------------- locations, dates, logging, pricing
add("useast7",
    "FAR table has 20 rows (adds us-east7 and global) while locations and data-residency pages list 16 regions and 2 multi-regions (18). INV(d) has 18 rows and no row for them; queue ruling: block (d) lists the union (20) with a labelled note. Row values for the two extra rows are not in INV",
    "MA7 R6, MA7 R8; MA8 R6, MA8 R8; INV(d) intro and row count; INV RN 1.12; INV RN 3; A RN-5; B RN-2.7; queue C15",
    "a",
    "feature-availability-by-region (the two rows), locations, data-residency, floor-settings page (global location), release notes for us-east7. Merger adds two rows with [ND] for description and jurisdiction if absent. P8 config BLOCKS becomes 10/15/16/20/16",
    "H")
add("rn1010",
    "Release-note entry dated 2026-10-10 (Workspace data PI protection) present on 2026-10-09; not used as a fact in INV. What it changes for ordinary prompts is unknown",
    "MA3 R2 (bullet), MA3 R8; MA4 R2 (bullet); INV RN 2; A RN-11; BR C9",
    "a",
    "Re-fetch release notes at P5 and record the as-read date; the effect on ordinary prompts is a test question (b)",
    "L")
add("logsan",
    "logSanitizeOperations: logging page says the full content of prompts and responses is logged; overview says event details 'might include metadata or snippets'. A and B state the full-content side only",
    "MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (data-handling bullet); MA5 R4, MA6 R4 (logging caveat); INV(c) logSanitizeOperations Effect; INV RN 1.10",
    "a",
    "configure-logging, overview; carry both sides in the columns as INV does",
    "M")
add("footer_dates",
    "Docs page 'Last updated' dates: INV intro says every docs page reads 2026-10-06 except release notes (2026-10-07); A RN-2 reports the REST templates reference at 2026-09-07, client libraries at 2026-10-05 and both Apigee pages at 2026-10-07. The brief repeats the blanket 2026-10-06",
    "INV intro; A RN-2; BR (Pin rule)",
    "a",
    "Re-read the footers on the pages cited at P5; the read date (2026-10-09) is the pin, so wording only",
    "L")
add("scc",
    "Security Command Center findings: integrations page says a floor-setting violation sends a finding; SCC findings page lists only FLOOR_SETTINGS_VIOLATION (template fails conformance)",
    "INV(b) Security Command Center findings row; INV RN 1.9",
    "a",
    "integrations page, SCC findings concepts page (SCC docs, not Model Armor docs)",
    "L")
add("pricing",
    "Pricing wording: scope of the 'up to 2 million tokens per month' allowance (project, organisation or billing account) is not stated; token definition 'four characters excluding white space' (pricing) against 'about 4 characters' (overview, quotas); INV(e) SCC tier row wording against the pricing table",
    "MA1 R4, MA2 R4, MA3 R4, MA4 R4, MA7 R4, MA8 R4 (pricing bullet); MA1 R7, MA2 R7, MA3 R7, MA4 R7, MA7 R7, MA8 R7 (Summary '2 million tokens a month'); MA5 R7, MA6 R7, MA9 R7, MA10 R7 (cost bullet); INV(e) Standalone price, SCC tier allowances, Token definition",
    "a",
    "cloud.google.com/security-command-center/pricing (no last-updated line; record the as-read date); overview and quotas wording",
    "M")
add("row_counts",
    "Inventory row counts: block (b) 15 against brief target 12; block (d) 18 becomes 20 after the C15 ruling; P8 config BLOCKS and markers tuple must follow",
    "INV RN 3; INV(b); INV(d); queue (BLOCKS 10/15/16/18/16)",
    "a",
    "Merger and xlsx-writer bookkeeping: config module build_modelarmor_inventory.py (counts, covered header, markers incl. R011)",
    "L")
add("naming",
    "Naming drift: docs say 'Gemini Enterprise Agent Platform' (short form Agent Platform used in A, B, INV), 'Gemini API in Vertex AI' and VERTEX_AI in gcloud flags; 'Agent Platform' sits close to the separate product 'Gemini Enterprise'",
    "INV intro (Naming); MA1 R3, MA2 R3, MA3 R3, MA4 R3 (Agent Platform route); MA5 R4; MA6 R4; INV(b) Agent Platform row",
    "a",
    "Overview, Vertex integration page: state the full name once per column (R4) and keep the short form after that",
    "L")

# ---------------------------------------------------------------- licensing and terms
add("prega",
    "Pre-GA Offerings Terms for Preview features (image screening, modalities, exclusion rules, LangChain, console modality selection): 'as is', limited support; not reflected in R4 or R7 except a one-line mention in MA10 R1",
    "MA10 R1 (bullet); MA3 R5 (exclusion rules bullets); MA4 R5; INV(a) Image OCR and Visual scanning Status; INV(c) modalities and filterRuleSettings Status; INV(b) LangChain",
    "c",
    "General Service Terms 'Pre-GA Offerings Terms' (linked from overview, manage-templates, LangChain and exclusion-rules pages); decide whether the bench may rely on Preview features",
    "M")
add("live_terms",
    "Terms for live testing: Google Cloud project with billing, acceptable-use rules for sending harmful, jailbreak or injection test content to the API, cross-jurisdiction transfer when residency enforcement is off or when a Singapore tester must call a us or eu endpoint for images, and Cloud Logging storing raw prompts",
    "MA1 R7 (CSAM caution); MA7 R7; MA8 R7; MA10 R7 (Singapore bullet); MA1 R4 and MA5 R4 (logging bullets); INV(c) dataResidencyCompliant Effect; INV(c) logSanitizeOperations Effect",
    "c",
    "Google Cloud Terms of Service, Acceptable Use Policy, Data Processing and Security Terms, data-residency page; user decision D6 (hard rule 5 forbids vendor API calls during research)",
    "M")
add("lib_licence",
    "(suggested, not in drafts) Licence of google-cloud-go (client library cited at 37f936ac) and of apigee-samples; no licence statement appears in any draft",
    "not in drafts; relevant to INV(b) Client libraries row and Apigee row",
    "c",
    "LICENSE files at the pinned shas",
    "L")
