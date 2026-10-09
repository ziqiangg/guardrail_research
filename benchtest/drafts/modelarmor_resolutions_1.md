# Model Armor resolutions 1 (P5): T1 to T43, class (a) and (c) items

Date 2026-10-09. Resolver: gr-resolver. Inputs: `benchtest/drafts/modelarmor_triage.md`, `modelarmor_cols_a.md`, `modelarmor_cols_b.md`, `modelarmor_inventory.md`, rulings R017 (CP1), R012, R013, R015, R019, queue answers for modelarmor P2.

Items handled (22, all class a; there is no class c item in T1 to T43; T85 to T87 belong to resolutions_2): T2, T3, T4, T9, T11, T13, T16, T18, T19, T20, T21, T22, T23, T24, T25, T26, T33, T35, T36, T37, T41, T43.

Class b items in this range are left open as instructed (they stay needs-testing): T1, T5, T6, T7, T8, T10, T12, T14, T15, T17, T27, T28, T29, T30, T31, T32, T34, T38, T39, T40, T42. Where a class b item has a documentation half, that half is handled under its class a partner (T1 under T2; T5 under T4; T10 under T9; T12 under T11; T14 under T13; T17 under T16; T32 under T33; T42 under T41).

Short names used below. DOCS = https://docs.cloud.google.com/model-armor/ . OV overview; TPL manage-templates; FLR configure-floor-settings; SAN sanitize-prompts-responses; QUO quotas; FAR feature-availability-by-region; DR data-residency; RN release-notes; EXC configure-exclusion-rules; INT integrations; NET model-armor-networking-integration; AGW model-armor-agent-gateway-integration; APG model-armor-apigee-integration; MCPD model-armor-mcp-google-cloud-integration; LIB reference/libraries; RT reference/rest/v1/projects.locations.templates; RR reference/rest/v1/SanitizationResult; RMR reference/rest/v1/projects.locations.templates/sanitizeModelResponse. A = modelarmor_cols_a.md, B = modelarmor_cols_b.md, INV = modelarmor_inventory.md. `Ln` after A, B or INV is the line number in the draft file as it stands today (cols_a 1001 lines, cols_b 611 lines, inventory 139 lines).

## Method and access notes

- Every Google docs page was read as raw text with `python benchtest/tools/fetch_text.py <url>` on 2026-10-09 (HTTP 200 for all pages listed below) and kept under `benchtest/scratchpad/resolver/ma1/`. Footers read: OV, TPL, FLR, FAR, DR, EXC, AGW, APG, MCPD, SAN and QUO "Last updated 2026-10-06 UTC"; RN and the Apigee release notes "2026-10-07" and "2026-10-09"; RT "2026-09-07"; RMR and the sanitizeUserPrompt reference "2026-08-19"; the two Apigee policy pages "2026-10-07"; the SCC Terraform page "2026-10-07". These are read dates, not pins; no docs pin exists (README section 3 rule 8).
- Code and tags (R013, R015): shallow, filtered, sparse clones of googleapis/google-cloud-go (HEAD 37f936ac9d69e173da0ba4123e382c52b2dd741f, module modelarmor 1.3.0) and googleapis/google-cloud-java at tag v1.93.0 (976d5888de5152ed93af51d58a669710fbaed9ec), plus `git ls-remote --tags` on googleapis/google-cloud-python, google-cloud-node, google-cloud-php-modelarmor and google-cloud-dotnet. Clones live in the session scratchpad, not in the repo. The tag modelarmor/v1.3.0 of google-cloud-go is 8a17bee208939e0166936a59675414439c47e341; `git diff` between it and 37f936ac touches only apiv1/model_armor_client.go, apiv1beta/model_armor_client.go, go.mod and go.sum, so every `service.pb.go` fact in the drafts holds at the tag too (see QUESTIONS Q1).
- One fact came from a summarising fetch and is labelled as such: the Service Extensions page `service-extensions/docs/configure-extensions-to-google-services` returned empty text through `fetch_text.py` (script-rendered), so WebFetch was asked whether it states a launch stage for the Model Armor extension; it answered that it does not. That is used only as supporting context in T21 and does not carry a label by itself.
- Not reachable or not used: registry.terraform.io (not official, queue ruling); github.com pages (403, per R015); the Google sample repos.
- Observation outside the assigned items: `https://docs.cloud.google.com/model-armor/pricing` returns HTTP 404 (observed 2026-10-09). The drafts cite the SCC pricing page and the overview for pricing, so no change is needed, but no draft R9 may cite the 404 URL.

## Items

### T2 — RAI default confidence level: three Google statements, not two
- Verdict: RESOLVED (documentation half). The effective default of an API-created template stays with T1 (needs testing, [To be verified]).
- Evidence:
  - TPL console steps: "Note: If you don't specify a confidence level, it is set to High by default." https://docs.cloud.google.com/model-armor/manage-templates (read 2026-10-09)
  - FLR console steps: "Note: If you don't specify a confidence level, it defaults to Medium and above." https://docs.cloud.google.com/model-armor/configure-floor-settings (read 2026-10-09)
  - RT: "If the confidence level is unspecified (i.e., 0), the system will use a reasonable default level based on the filterType." and enum "DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED | Same as LOW_AND_ABOVE." https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates (read 2026-10-09)
  - OV (checked, no default level stated): https://docs.cloud.google.com/model-armor/overview
- Label to use: [Documented] for each of the three statements (one bullet each); [To be verified] for which one applies to an API-created template (separate bullet, test pending, T1).
- Draft impact:
  - A MA1 R5 and MA2 R5 (L73 to L92; L239 to L260): after the bullet "Default level, REST: ..." insert
    `• Default level, floor settings console: "If you don't specify a confidence level, it defaults to Medium and above." (floor settings page, console steps, 2026-10-09) **[Documented]**`
  - A MA1 R5 and MA2 R5, bullet "The two default statements differ and no page says which applies to an API call that omits the level **[To be verified]**" becomes
    `• The three default statements differ (High on the templates page; unspecified equals LOW_AND_ABOVE or "a reasonable default level based on the filterType" in the REST reference; Medium and above on the floor settings page) and no page says which applies to a template created through the API without a level (checked the templates page, floor settings page, REST templates reference and overview) **[To be verified]**`
  - A MA1 R5 Summary (L74) [Summary changes], new text (34 words before the label):
    `Summary: **Match states per category.** The result gives an overall match state and one for each of the four categories, sometimes with a confidence level. Google's pages state three different defaults for an omitted level. **[Documented]**`
  - A MA2 R5 Summary does not mention defaults; no Summary change for MA2 (its Summary is covered by T8, class b).
  - INV(a) RAI row, Default cell (L11): already lists all three statements; no text change. Keep the last fact "Effective default of a template [To be verified] (needs testing)".
  - B, INV(c) raiSettings Default and Floor-setting levels Default: no change needed; they carry the three statements already.

### T3 — PI and jailbreak default level when omitted
- Verdict: PARTLY RESOLVED. The floor-setting default is documented; the template default is still an inference from the REST enum.
- Evidence:
  - FLR: "Note: If you don't specify the prompt injection and jailbreak detection confidence level, the confidence level defaults to LOW_AND_ABOVE for all levels: project, organization, or folder." https://docs.cloud.google.com/model-armor/configure-floor-settings (read 2026-10-09)
  - RT enum: "DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED | Same as LOW_AND_ABOVE." The PI field text ("Optional. Confidence level for this filter...") states no default. https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
  - TPL: only the RAI console step states a default (see T2); checked all "default" and "confidence" lines, no PI default.
- Label to use: floor-setting default [Documented]; template default [Inferred] with the premise named (the unspecified enum value applies to every filter that uses DetectionConfidenceLevel).
- Draft impact:
  - A MA3 R5 and MA4 R5 (L419, L591) replace the bullet "Default when the level is omitted: ... **[Inferred]**" with two bullets:
    `• Floor settings: "If you don't specify the prompt injection and jailbreak detection confidence level, the confidence level defaults to LOW_AND_ABOVE for all levels: project, organization, or folder." (floor settings page, 2026-10-09) **[Documented]**`
    `• Template without a level: the REST enum says unspecified is "Same as LOW_AND_ABOVE" and the filter field states no default of its own, so an omitted level on a template would behave as Low and above; the premise is that the enum text applies to every filter that uses it **[Inferred]**`
  - A MA3 R8 and MA4 R8 bullet "Default level when the field is omitted (inferred as Low and above from the enum; needs testing)" becomes `Default level of a template that omits the field (floor settings default to Low and above; the template default is inferred from the enum; needs testing)`.
  - A MA3 R7 and MA4 R7: no change ("compare a template that omits the level" stays).
  - INV(a) PI row Default cell and INV(c) piAndJailbreakFilterSettings Default: they record the floor-setting default as [Documented]; add to the template fact "[Inferred] (premise: the enum text applies to every filter that uses it)" if it is not already split.
  - Summaries: none change.

### T4 — PI and jailbreak threshold advice: four statements, not three
- Verdict: RESOLVED (documentation half; the live trade-off per level and version is T5, needs testing). One addition: a fourth statement in the OV considerations text.
- Evidence:
  - OV example strategy: "Set prompt injection and jailbreak detection filters to Medium. For applications like Gemini Enterprise, set the threshold to High to avoid false positives." https://docs.cloud.google.com/model-armor/overview
  - OV category tuning (new): "for both prompt injection and jailbreak detection and general content safety (hate speech, harassment, dangerous content), start with High or Medium and above to minimize false positives."
  - OV table: Low and above is "Use with caution. Potentially suitable for high-stakes categories like prompt injection and jailbreak detection, where preventing false negatives is critical, even at the risk of accepting false positives."
  - TPL: "We recommend that you set the confidence level to High to minimize false positives and ensure consistent detection behavior." https://docs.cloud.google.com/model-armor/manage-templates
  - FLR illustration: "must use prompt injection and jailbreak detection with medium confidence"; the FLR finding example shows piAndJailbreakFilterSettings floorSettings LOW_AND_ABOVE with template HIGH. https://docs.cloud.google.com/model-armor/configure-floor-settings
  - Release notes (all entries read) and best-practices page contain no PI threshold advice, so no later page changes the advice.
- Label to use: [Documented] for each statement. No page reconciles them (the conflict stays; the existing wording "advice A, B, C" already keeps them apart).
- Draft impact:
  - A MA3 R5 and MA4 R5 (after L417 and after L590): after "Threshold advice C" insert
    `• Threshold advice D, overview considerations: "for both prompt injection and jailbreak detection and general content safety (hate speech, harassment, dangerous content), start with High or Medium and above to minimize false positives." (overview, 2026-10-09) **[Documented]**`
  - A MA3 R5 Summary (L408) [Summary changes], new text (35 words):
    `Summary: **Match flag plus a confidence level.** The result gives an execution state, a match state and a confidence level. Google's pages advise Medium or High as the setting, and Low and above for high-stakes categories. **[Documented]**`
  - A MA4 R5 Summary (L581) [Summary changes]. MA4's own response example shows no confidence field (L584), so the shared sentence is also wrong in substance; new text (38 words):
    `Summary: **Match flag plus a confidence level field.** The result type has an execution state, a match state and a confidence level, though the docs' response example shows no level. Google's pages advise Medium or High as the setting. **[Documented]**`
  - INV(a) PI row Levels cell and INV(c) piAndJailbreakFilterSettings Effect: add the fourth statement as a separate [Documented] fact (OV considerations).
  - A MA3/MA4 R8: "Which confidence level to use: Medium (overview example strategy) or High (templates page recommendation); needs testing" stays.

### T9 — CSAM filter: "cannot be turned off" against "No" in limited-support locations
- Verdict: RESOLVED (documentation half). The two statements are conditional, not contradictory: the feature table applies to templates with data residency enforcement enabled, and Google says disabling enforcement enables features otherwise unavailable. Observed behaviour is T10 (needs testing).
- Evidence:
  - OV: "CSAM | Contains references to child sexual abuse material (CSAM). This filter is applied by default and cannot be turned off." https://docs.cloud.google.com/model-armor/overview
  - FAR: "This section shows the regional capabilities and supported filters for each region or multi-region when you configure Model Armor using a template that has data residency enforcement enabled." The CSAM support column reads "No" for asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2 and northamerica-northeast2, and "Yes" in the full-support rows. https://docs.cloud.google.com/model-armor/feature-availability-by-region
  - FAR: "If you must use a limited-support region but you want to prioritize comprehensive security filtering over strict data residency, you can disable data residency enforcement for in-use and in-transit data in your Model Armor template."
  - FAR note: "For Model Armor configurations that use floor settings, all features are available, but data residency enforcement for data in use and in transit varies by region."
  - RN 2026-08-27: "Disabling data residency enforcement allows cross-jurisdictional routing to enable Model Armor features that are otherwise unavailable in limited-support regions." https://docs.cloud.google.com/model-armor/release-notes
  - RN 2026-09-04: "To use other Model Armor features in these regions, disable data residency enforcement in the template." (Melbourne and Seoul clarification).
  - Not stated anywhere: that CSAM specifically is among the enabled features after disabling (CSAM is not named in the RN or DR sentences; the FAR full-support list names it).
- Label to use: the table fact [Documented]; "CSAM is available in a limited-support location once enforcement is disabled" [Inferred] (premise: RN 2026-08-27 and DR say disabling enforcement enables the features that are unavailable; FAR lists CSAM among the full-support features).
- Draft impact:
  - A MA1 R1 and MA2 R1 Summary (L3, L164) [Summary changes], new text for MA1 (45 words before the label, at the limit):
    `Summary: **Input-level responsible AI safety filtering.** Model Armor screens a user prompt for hate speech, harassment, sexually explicit and dangerous content at a per-category confidence level. A CSAM check is on by default but unavailable in limited-support locations with residency enforced. The caller enforces any block. **[Documented]**`
    MA2 R1 the same with "Output-level" and "a model response" in place of "Input-level" and "a user prompt" (also 45 words).
  - A MA1 R1 bullet L11 and MA2 R1 equivalent: keep the overview quote bullet; it is one-sided but accurate to its page.
  - A MA1 R2 and MA2 R2 bullet "Docs state the CSAM filter 'cannot be turned off' (overview) but the feature table ... **[Documented]**" (L28; MA2 equivalent) split into three bullets:
    `• Overview: the CSAM filter "is applied by default and cannot be turned off" (overview, 2026-10-09) **[Documented]**`
    `• Feature table for templates with data residency enforcement enabled: CSAM support is "No" in asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2 and northamerica-northeast2, and "Yes" in the full-support locations (feature availability page, 2026-10-09) **[Documented]**`
    `• Disabling data residency enforcement "allows cross-jurisdictional routing to enable Model Armor features that are otherwise unavailable in limited-support regions"; floor-setting configurations have all features available (release note 2026-08-27, feature availability page, 2026-10-09) **[Documented]**`
    `• CSAM detection is therefore expected to run in a limited-support location when enforcement is off; the pages do not name CSAM in that sentence **[Inferred]**`
  - A MA1 R8 and MA2 R8: keep the "observed behaviour" bullet (T10).
  - INV(a) CSAM row Default cell (L12): replace "Always on: 'This filter is applied by default and cannot be turned off.' [Documented] (OV)" with
    `On by default: 'This filter is applied by default and cannot be turned off.' [Documented] (OV). With data residency enforcement on, not available in the seven limited-support locations [Documented] (FAR). Available there with enforcement off [Inferred] (premise: RN 2026-08-27 says disabling enforcement enables features otherwise unavailable; CSAM is not named in that sentence)`
  - INV(a) CSAM row Limit cell (L12) already says "Not available in limited-support regions when data residency enforcement is on [Documented] (FAR)": keep.
  - INV(d) CSAM column: no change (the seven "No" cells are correct for enforcement on); add to the block (d) intro one sentence: `The Supported filters, Multi-language, CSAM, Image and Antivirus columns describe templates with data residency enforcement enabled [Documented] (FAR).`
  - A RN-4 (C14): record as reconciled by condition.

### T11 — RAI, PI and malicious URL filters on OCR text from images
- Verdict: PARTLY RESOLVED. The documented sentence says only that the text content of an image is sanitized "depending on the filter configuration"; no page names which filters examine OCR text. The five columns carry three different treatments; align them to one.
- Evidence:
  - RT Modality enum: "MODALITY_IMAGE | Represents image modality. If specified, it will sanitize image files. The visual content and the text content in the image will be sanitized depending on the filter configuration." https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates (read 2026-10-09)
  - OV: "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." and "Optical character recognition (OCR): Screens the text within images." https://docs.cloud.google.com/model-armor/overview
  - OV use case: "Inspect visual content and text within images to detect embedded threats, sensitive information types (infoTypes), or policy violations."
  - Absence (checked OV image section and use cases, SAN "Prompts containing images" section whose two example responses show only `csam` and `sdp` results, TPL modality steps, RT, RN 2026-06-25 and 2026-07-01, RR, and the DataItem reference): no sentence lists RAI, PI or malicious URL filters for OCR text.
- Label to use: the "depending on the filter configuration" quote [Documented]; which filters examine OCR text [Not disclosed] (checked list above); "the template's filters decide" is not a quote, so any cell that says "follows the template" is [Inferred].
- Draft impact (replace the five divergent treatments with the same two bullets):
  - A MA1 R3 (L51), MA3 R3 (L377), A MA7 R2 (L700), A MA8 R2 (L851): replace the bullet that carries [To be verified] with
    `• The REST modality reference says the text content of an image is sanitized "depending on the filter configuration" (REST templates ref, 2026-10-09) **[Documented]**`
    `• Whether the <responsible AI | prompt injection and jailbreak | malicious URL> filter examines text read out of images by OCR is not stated (checked the overview image section, the sanitize page image examples, which show only csam and sdp results, the templates page, the REST references and release notes 2026-06-25 and 2026-07-01) **[Not disclosed]**`
    (choose the filter name per column; MA8 reads "URLs inside generated images").
  - A MA1, MA3, MA7, MA8 R8: wording unchanged (still open, test T12).
  - B MA10 R2 (the two bullets on OCR text): keep the [Not disclosed] bullet; the [Inferred] bullet "safety, prompt injection and malicious URL checks probably run only on OCR text, not on pixels" stays [Inferred] with its premise (the word "only" in the visual scanning sentence). The MA10 R2 Summary draws only on [Documented] bullets and stays [Documented].
  - INV(a) Image OCR row Result field / Limit cell (L18), the fact "Which filters run on the text follows the template: 'depending on the filter configuration' [Documented] (RT)" splits into
    `Text content of an image is sanitized 'depending on the filter configuration' [Documented] (RT). Which of the RAI, prompt injection and malicious URL filters run on OCR text [Not disclosed] (checked OV, SAN, TPL, RT, RN)`
  - INV(a) Image visual row: unchanged (visual scanning uses only the advanced SDP filter [Documented] (OV)).
  - Summaries: none change.

### T13 — PI and jailbreak filter on model responses
- Verdict: RESOLVED (wording and label). The overview states response scanning directly, so the Summary can stay [Documented] if it rests on that sentence; the sample result and Apigee variables support it but do not add a statement. A positive response-side example and observed behaviour stay open (T14, needs testing).
- Evidence:
  - OV: "When prompt injection and jailbreak detection is enabled, Model Armor scans prompts and responses for malicious content. If detected, Model Armor blocks the prompt or response." https://docs.cloud.google.com/model-armor/overview
  - TPL: "Prompt injection and jailbreak detection: Detects malicious content and jailbreak attempts in a prompt." (same sentence block opens "Model Armor performs the following detection checks on prompts and responses") https://docs.cloud.google.com/model-armor/manage-templates
  - SAN (sanitizeModelResponse example): `"pi_and_jailbreak": { "piAndJailbreakFilterResult": { "executionState": "EXECUTION_SUCCESS", "matchState": "NO_MATCH_FOUND" } }`
  - Apigee SanitizeModelResponse policy: "SanitizeModelResponse.POLICY_NAME.promptInjectionDetected | Boolean value indicating whether the prompt injection filter matched." https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy (Apigee docs, not Model Armor docs)
  - RMR: the response body is the same SanitizationResult as for prompts; no per-filter direction statement. https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse
- Label to use: [Documented] (overview sentence, templates sentence, sample result, Apigee variables, each as its own fact); the reading "so the filter runs on responses despite the templates wording" is [Inferred].
- Draft impact:
  - A MA4 R1 Summary (L504) [Summary changes], new text (37 words):
    `Summary: **Output-level prompt injection and jailbreak detection.** The overview says the filter scans prompts and responses, and a sample response result shows it running. The templates page describes it for prompts only. The calling service enforces any block. **[Documented]**`
  - A MA4 R1 bullet L510 ("Taken together, the overview, the sample output and the Apigee variables show the filter runs on responses; ... **[Inferred]**") is rewritten:
    `• The overview sentence is a direct statement; the templates page wording "in a prompt" is narrower and the docs do not say which reading is intended, so treating the filter as active on responses rests on the overview sentence and the sample result **[Inferred]**`
  - INV(a) PI row Applies to cell: already "Input and Output [Documented]"; no change.
  - A RN-14 (C12): record as reconciled in wording.

### T16 — Optional userPrompt field of sanitizeModelResponse is documented in the REST method reference and the Apigee policy page (CORRECTION to A)
- Verdict: CORRECTION. A (MA2, MA4, MA8 R3, R6, R8 and A RN-3) says only the Go client documents the field and that "the docs pages do not mention it". Google's own REST method reference and the Apigee policy page do. B (MA6) is right.
- Evidence:
  - RMR request body: `"userPrompt": string` and "Optional. User Prompt associated with Model response." https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse (read 2026-10-09, page footer 2026-08-19)
  - Apigee SanitizeModelResponse: "SanitizeModelResponse.POLICY_NAME.userPrompt | Specifies the prompt content used for the call to Model Armor to sanitize the content." and the element "<UserPromptSource> ... Required ... The location of the payload for the user prompt text to be extracted." https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy
  - Code: Go `SanitizeModelResponseRequest.UserPrompt` (service.pb.go@37f936ac:2380) and the Java proto field `string user_prompt = 4 [(google.api.field_behavior) = OPTIONAL];` (google-cloud-java@v1.93.0, java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto:811).
  - What the field changes: the same RMR page, the sanitize page, the overview and the Apigee page were checked and none says whether any filter uses it (stays [Not disclosed], T17).
  - The sanitize page examples for sanitizeModelResponse send `modelResponseData` only (no sample uses the field).
- Label to use: field exists and is optional [Documented] (REST method reference); Apigee policy requires a prompt source and exposes it as a flow variable [Documented] (Apigee docs, not Model Armor docs); effect of the field [Not disclosed].
- Draft impact:
  - A MA2 R3 Summary (L197) [Summary changes], new text (42 words):
    `Summary: **The model response text, sent on its own.** The caller posts it to the sanitize-model-response method of a regional endpoint with a template name. The docs examples send no user prompt, though the REST method reference lists an optional field for one. **[Documented]**`
  - A MA2 R3 (L202), MA4 R3 (L536), MA8 R3 (L860): the Go-only bullet becomes two bullets:
    `• The REST method reference for sanitizeModelResponse lists an optional `userPrompt` string, "User Prompt associated with Model response." (sanitizeModelResponse reference, 2026-10-09) **[Documented]**`
    `• The Go client request struct has the same optional `UserPrompt` field (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:2380-2381) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
  - Add one bullet in the same row: `• The Apigee SanitizeModelResponse policy has a required `<UserPromptSource>` element and sets a `userPrompt` flow variable (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**`
  - A MA2 R6 (L268), MA4 R6 (L608): replace "Optional `UserPrompt` string in the Go client request for this method ..." with `Optional `userPrompt` string in the request body of this method (sanitizeModelResponse reference, 2026-10-09) **[Documented]**`.
  - A MA2 R8 (L297), MA4 R8 (L638), MA8 R8 (L944): replace "(the Go client documents it; the docs pages do not mention it)" with "(the REST method reference and the Apigee policy page list the field; none says what it changes)".
  - A MA2, MA4, MA8 R9: add `• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse` (MA2 and MA4 R9 already list the Apigee response-policy URL; MA8 R9 lists it too at L977).
  - A RN-3 (L982): delete "not shown anywhere in the docs" for `UserPrompt`; the second use (absence of filter-version, exclusion-rule and data-residency fields in the v1 client) stays (T18).
  - B MA6 R3 Summary (L181) and MA6 R6: no change (already correct).

### T18 — Docs describe fields the Go v1 client does not have; the Java v1 proto lags the same way
- Verdict: PARTLY RESOLVED. The absence is confirmed in a second official client (Java); the reason ("client lags") is still an inference.
- Evidence:
  - Go: `type FilterConfig struct {` lists RaiSettings, SdpSettings, PiAndJailbreakFilterSettings, MaliciousUriFilterSettings only (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:1861). Counts of the strings FilterVersion, FilterRule, ExclusionRule and DataResidency in apiv1 and apiv1beta service.pb.go: 0; GOOGLE_MCP_SERVER: 0 in apiv1, present in apiv1beta (`FloorSetting_GOOGLE_MCP_SERVER`, service.pb.go@37f936ac:511).
  - Java v1: `message FilterConfig {` has the same four fields (java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto@v1.93.0:622); no filter_version, FilterRule, exclusion or data_residency string in the v1 or v1beta service.proto; GOOGLE_MCP_SERVER only in v1beta.
  - Docs side: RT lists "filterVersionSelector" and "dataResidencyCompliant" in TemplateMetadata; EXC and TPL use `filterConfig.filterRuleSettings`. https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
  - SAN uses apiv1beta in one Go streaming sample (already in INV).
- Label to use: absence in each client [Documented: repo googleapis/google-cloud-go@37f936ac] and [Documented: repo googleapis/google-cloud-java@v1.93.0] (one label per repo, split bullets); "docs are ahead of the generated clients" [Inferred] (premise: both clients are generated from the same API protos and the docs, REST reference and gcloud flags describe fields they lack).
- Draft impact:
  - A MA3 R4 (L399) and MA4 R4 (L571) ND bullet about the Go client: keep as one [Documented: repo googleapis/google-cloud-go@37f936ac] absence bullet, add a second bullet
    `• The Java v1 proto has the same four FilterConfig fields and none of the filter-version, exclusion-rule or data-residency fields (java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto@v1.93.0:622) **[Documented: repo googleapis/google-cloud-java@v1.93.0]**`
    and a third `• The docs and REST reference describe these fields, so the client libraries read lag the documented API; the premise is that the clients are generated from the same API definition **[Inferred]**`
  - A MA3 R9 and MA4 R9: add `• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1beta/modelarmorpb/service.pb.go` and `• https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto`.
  - INV(b) Client libraries row Limitations (L29): append `The Java v1 proto at googleapis/google-cloud-java@v1.93.0 has the same four FilterConfig fields and none of the filter-version, exclusion-rule or data-residency fields [Documented: repo googleapis/google-cloud-java@v1.93.0]`; add the Java proto blob URL to the Source URL cell.
  - INV(c) filterVersionSelector row and INV RN 1.11: same one-line addition.

### T19 — Exclusion rules schema gap (filterRuleSettings)
- Verdict: PARTLY RESOLVED. The gap is a dating effect on the REST page that is documented; whether the v1 API accepts the field remains a test.
- Evidence:
  - EXC: "To create a template with exclusion rules, include the filterRuleSettings object within filterConfig in a POST request." and the Preview banner. https://docs.cloud.google.com/model-armor/configure-exclusion-rules
  - TPL update mask text: "such as filterConfig, filterConfig.piAndJailbreakFilterSettings, or filterConfig.filterRuleSettings." https://docs.cloud.google.com/model-armor/manage-templates
  - RT FilterConfig lists only raiSettings, sdpSettings, piAndJailbreakFilterSettings, maliciousUriFilterSettings; page footer "Last updated 2026-09-07 UTC" (read 2026-10-09). https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
  - RN 2026-09-28: "Template-specific exclusion rules are available in Preview." The REST page footer date (2026-09-07) is earlier than this release note.
  - Go and Java v1 clients: no filterRuleSettings (see T18).
- Label to use: EXC and TPL use the field [Documented]; REST FilterConfig lacks it [Documented]; REST page predates the release note [Documented] (footer date versus release note date); "the REST page is stale" [Inferred] (premise: the footer date precedes the release); whether the live v1 API accepts it [To be verified] (test: create a template with the field).
- Draft impact:
  - A MA3 R5 (L424), MA4 R5 (L598) [TBV] bullet becomes three bullets:
    `• The exclusion rules page and the templates page use `filterConfig.filterRuleSettings` in v1 requests and update masks (exclusion rules page, templates page, 2026-10-09) **[Documented]**`
    `• The REST `FilterConfig` lists only `raiSettings`, `sdpSettings`, `piAndJailbreakFilterSettings` and `maliciousUriFilterSettings`, and the page footer reads "Last updated 2026-09-07 UTC", before release note 2026-09-28 that introduced exclusion rules (REST templates ref, release notes, 2026-10-09) **[Documented]**`
    `• The REST reference probably lags the feature; the premise is the footer date before the release note **[Inferred]**`
    and keep `• Whether the v1 template API accepts `filterRuleSettings` (needs testing; the Go and Java v1 clients at the pins in R4 do not have the field) **[To be verified]**`.
  - INV(c) filterRuleSettings Where set cell and INV RN 1.8: same split.
  - A RN-13 (C11): record the footer-date evidence.

### T20 — Apigee SanitizeUserPrompt and SanitizeModelResponse: GA
- Verdict: RESOLVED.
- Evidence:
  - Apigee release notes, Apigee X, 2025-09-04: "Apigee policies for LLM/GenAI workloads are Generally Available (GA) ... Four new Apigee policies supporting LLM/GenAI workloads are now GA: ... SanitizeUserPrompt SanitizeModelResponse". https://docs.cloud.google.com/apigee/docs/release-notes (read 2026-10-09)
  - Same page, 2025-05-22: "Public Preview of Apigee policies for LLM/GenAI workloads".
  - Neither Apigee policy page nor the Model Armor Apigee integration page carries a Preview banner (checked for "Preview", "Pre-GA", "beta").
  - Apigee hybrid: a hybrid release note lists the same two policies as supported ("Apigee hybrid now supports the following Apigee policies ..."; limited to installations on Google Cloud, no forward proxy), date not read, so not used.
- Label to use: [Documented] (Apigee docs, not Model Armor docs).
- Draft impact:
  - A R4 of MA1, MA2, MA3, MA4, MA7, MA8 (L70, L236, L405, L578, L736, L890): the shared bullet "Apigee policies ... and load-balancer Service Extensions other than GKE: no GA or Preview label found on the pages read **[To be verified]**" is replaced by (see also T21)
    `• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse`: Public Preview on 2025-05-22 and Generally Available on 2025-09-04 on Apigee X (Apigee release notes, Apigee docs not Model Armor docs, 2026-10-09) **[Documented]**`
  - A MA5 R4 Apigee bullet and MA6 R4, MA6 R8 (B): same fact; remove the open question.
  - INV(b) Apigee row Status (L35): replace "[To be verified] (no GA or Preview label found on APG, APU or APR)" with `Preview 2025-05-22, GA 2025-09-04 on Apigee X [Documented] (Apigee release notes, Apigee docs not Model Armor docs)`; add `https://docs.cloud.google.com/apigee/docs/release-notes` to the Source URL cell.
  - A and B R9: add `• https://docs.cloud.google.com/apigee/docs/release-notes` to each column that carries the bullet.
  - Summaries: none change. Triage BR G8 closed.

### T21 — Service Extensions on load balancers other than GKE, and Secure Web Proxy: GA date
- Verdict: STILL OPEN (checked RN, NET, INT, the Service Extensions configuration page via a summarising fetch; no GA statement). One part is documented: the 2025-04-09 Preview note and the GKE GA.
- Evidence:
  - RN 2025-04-09: "Model Armor enforces security policies uniformly on generative AI inference traffic using a traffic extension. This applies to all application load balancers, including Google Kubernetes Engine Inference Gateway. This feature is in Preview." https://docs.cloud.google.com/model-armor/release-notes
  - RN 2025-09-15: "Model Armor integration with Google Kubernetes Engine is available in General Availability."
  - NET (Cloud Load Balancing, GKE Inference Gateway and Secure Web Proxy rows): no launch-stage word on the page. https://docs.cloud.google.com/model-armor/model-armor-networking-integration
  - RN contains no entry mentioning Secure Web Proxy or a GA for load balancers other than GKE (all 2025 to 2026 entries read; grep for "Secure Web Proxy", "load balanc", "traffic extension", "Inference Gateway").
- Label to use: Preview 2025-04-09 and GKE GA 2025-09-15 [Documented]; GA date for the other load balancers and Secure Web Proxy [Not disclosed] (checked RN, NET, INT, Service Extensions page by summarising fetch).
- Draft impact:
  - A R4 of MA1, MA2, MA3, MA4, MA7, MA8: add after the Apigee bullet of T20
    `• Service Extensions on application load balancers: Preview in release note 2025-04-09; the GKE Inference Gateway integration is Generally Available from release note 2025-09-15 (release notes, 2026-10-09) **[Documented]**`
    `• A GA date for other load balancers and for Secure Web Proxy (checked the release notes, the networking and integrations pages and the Service Extensions configuration page) **[Not disclosed]**`
  - INV(b) Service Extensions row Status (L38): replace "GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN and NET)" with `GA date for other load balancers and Secure Web Proxy [Not disclosed] (checked RN, NET, INT)`.
  - Summaries: none change.

### T22 — MCP integration status: Preview label on the floor-settings page against GA in the release note
- Verdict: RESOLVED (documentation). Both statements exist; the queue ruling prefers the dated release note and keeps both as a labelled pair. Apply the pair in every location, not only MA6.
- Evidence:
  - RN 2026-04-22: "Model Armor integration with Google and Google Cloud MCP servers is in General Availability." Earlier RN 2025-12-10 and 2025-12-15 say Preview. https://docs.cloud.google.com/model-armor/release-notes
  - FLR (footer 2026-10-06): "For more information, see Model Armor integration with Google Cloud MCP servers (Preview)." https://docs.cloud.google.com/model-armor/configure-floor-settings
  - MCPD carries no Preview banner (checked). https://docs.cloud.google.com/model-armor/model-armor-mcp-google-cloud-integration
- Label to use: both statements [Documented], two bullets, note that the dated release note is preferred (queue ruling; the page link text is undated).
- Draft impact:
  - A R4 of MA1, MA2, MA3, MA4, MA7, MA8, bullet "Release status of routes ..." (L69 etc.): where it lists "Google and Google Cloud MCP servers GA (2026-04-22)", add a bullet after it
    `• The floor settings page still labels the Google Cloud MCP servers integration "(Preview)" (floor settings page, 2026-10-09); the dated release note 2026-04-22 says General Availability and is preferred, because the page label is undated **[Documented]**`
  - INV(b) MCP row Status (L37): `Preview 2025-12-10, GA 2026-04-22 [Documented] (RN). The floor settings page still labels the link '(Preview)' [Documented] (FLR); the dated release note is preferred (queue ruling)`.
  - INV(c) Floor-setting inline enforcement Status (L65): same addition.
  - B MA6 R4: unchanged (pair already there).

### T23 — Status rule S ("GA [Inferred]")
- Verdict: PARTLY RESOLVED. No page states GA for the base service, so the inference stays [Inferred]; the premise can now be stated with evidence, and the rule is better applied evenly.
- Evidence:
  - Preview features carry an in-page banner: on OV "Image screening ... Preview. This feature is subject to the 'Pre-GA Offerings Terms' in the General Service Terms section of the Service Specific Terms." and on EXC "Preview". https://docs.cloud.google.com/model-armor/overview ; https://docs.cloud.google.com/model-armor/configure-exclusion-rules
  - The first RN entry (2025-02-03) reads: "Model Armor is a Google Cloud service that lets you to apply content safety and content security controls to LLM prompts and responses ..." with no stage word. https://docs.cloud.google.com/model-armor/release-notes
  - Checked for a GA statement of the base service on OV, the product page (https://cloud.google.com/security/products/model-armor) and the Google Cloud blog post (https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps): none ("generally available", "GA", "Preview" return no hit on the product page or the blog).
- Label to use: [Inferred], premise "no stage statement and no Pre-GA banner on the page, while Google marks Preview features with a banner".
- Draft impact:
  - INV intro (L3), rule S statement: state the premise once, `Status rule S: a feature with no stated stage and no Pre-GA banner on its page is shown as GA [Inferred] (premise: Google marks Preview features with a banner, for example image screening on the overview and exclusion rules on their page; no page states GA for the base service, first release note 2025-02-03)`.
  - Apply the rule evenly (INV RN 3 and Label hygiene): rows now [Not disclosed] for gcloud, console, SCC findings (INV(b)) and Terraform (see T24) have no banner either; either mark them `GA [Inferred] (status rule S)` or keep [Not disclosed] for every row whose page does not state a stage. Recommended: keep [Not disclosed] for rows whose stage is unstated and whose page was not read for a banner (Terraform), and apply rule S only where a page was read and found banner-free. A decision for main; no label is upgraded either way.
  - Apigee rows leave rule S (T20: [Documented] GA).
  - Summaries: none change.

### T24 — Terraform resources for Model Armor (Google's own documentation)
- Verdict: PARTLY RESOLVED. A Google Cloud docs page lists the two resources; stage and field coverage are not stated.
- Evidence:
  - SCC Terraform page, "Terraform resources for Security Command Center", section Model Armor: "google_model_armor_floorsetting google_model_armor_template". https://docs.cloud.google.com/security-command-center/docs/terraform (read 2026-10-09, footer 2026-10-07)
  - RN 2025-07-29: "You can use Terraform to manage Model Armor floor settings and templates." with link text "Terraform resources for Model Armor" to `/security-command-center/docs/terraform#resources`. https://docs.cloud.google.com/model-armor/release-notes
  - Neither page states a launch stage or the arguments supported. registry.terraform.io not used (HashiCorp's, queue ruling).
- Label to use: resource names [Documented]; stage [Not disclosed] (checked RN 2025-07-29 and the SCC Terraform page); arguments and limits [To be verified] (the provider reference is on the HashiCorp registry, outside the official-source list).
- Draft impact:
  - INV(b) Terraform row (L31): first cell `Terraform resources google_model_armor_floorsetting and google_model_armor_template [Documented] (SCCTF; RN 2025-07-29)`; Status unchanged `[Not disclosed] (the release note and the SCC Terraform page give no GA or Preview label)`; Limitations `[To be verified] (the argument reference is on the HashiCorp provider registry page, not read; not an official source)`; Source URL cell add `https://docs.cloud.google.com/security-command-center/docs/terraform`.
  - INV intro and INV RN 4: delete "the Terraform resource page" from the not-read list; add short name `SCCTF = https://docs.cloud.google.com/security-command-center/docs/terraform`.
  - A/B: no column mentions Terraform. Summaries: none change.

### T25 — Client library versions
- Verdict: PARTLY RESOLVED. Java, Python, Node.js, PHP and C# versions can now be stated from Google's pages and repo tags; C# page-versus-tag drift is new.
- Evidence:
  - LIB sbt line: `libraryDependencies += "com.google.cloud" % "google-cloud-modelarmor" % "0.40.0"`, Maven BOM `libraries-bom` `26.86.0`, and for C# `dotnet add package Google.Cloud.ModelArmor.V1 --version 1.0.0-beta05`. https://docs.cloud.google.com/model-armor/reference/libraries (read 2026-10-09)
  - Java: `<version>0.40.0</version>` for google-cloud-modelarmor-parent in java-modelarmor/pom.xml@v1.93.0:7 (googleapis/google-cloud-java).
  - Tags (`git ls-remote --tags`, highest by version sort, 2026-10-09): googleapis/google-cloud-python `google-cloud-modelarmor-v0.7.2` (69401247a72c0f0786741ac937c3c5aa2afc8ead); googleapis/google-cloud-node `modelarmor-v0.10.0` (703154ba1720ff2d1a5832ad0683a3c3bcbbadd1); googleapis/google-cloud-php-modelarmor `v0.8.3` (00a3ea17fc5b609a4d5957ab2c5f82d5aa98a39e); googleapis/google-cloud-dotnet `Google.Cloud.ModelArmor.V1-1.0.0-beta07` (c7114485489c266694f66289c29f8ec3333609c5); Go module 1.3.0 (already in the drafts).
  - Not read: release notes or changelogs of the Python, Node.js, PHP and C# repos (github.com pages are not reachable); versions come from tag names only.
- Label to use: Java 0.40.0 [Documented] (LIB) and [Documented: repo googleapis/google-cloud-java@v1.93.0]; Python, Node.js, PHP and C# latest tags [Documented: repo <repo>@<tag>] (tag names); "pre-release" status for the Python, Node.js and PHP 0.x versions is [Inferred] (premise: version below 1.0).
- Draft impact:
  - A R4 of MA1, MA2, MA3, MA4, MA7, MA8, bullet "Client libraries exist for C#, Go, Java, Node.js, PHP and Python; the C# install line is a pre-release package ..." (L71): keep, then add
    `• The client libraries page shows Java google-cloud-modelarmor 0.40.0 in its sbt line, and the Java parent pom at googleapis/google-cloud-java v1.93.0 reads 0.40.0 (client libraries page, 2026-10-09) **[Documented]**`
    `• Latest tags read: Python google-cloud-modelarmor-v0.7.2, Node.js modelarmor-v0.10.0, PHP v0.8.3 and C# Google.Cloud.ModelArmor.V1-1.0.0-beta07, while the client libraries page shows C# 1.0.0-beta05 **[Documented]**` (one label per repo: split into four bullets, each `**[Documented: repo googleapis/google-cloud-python@google-cloud-modelarmor-v0.7.2]**`, `...google-cloud-node@modelarmor-v0.10.0]`, `...google-cloud-php-modelarmor@v0.8.3]`, `...google-cloud-dotnet@Google.Cloud.ModelArmor.V1-1.0.0-beta07]`)
    Add the repo URLs to R9: `https://github.com/googleapis/google-cloud-python/tree/google-cloud-modelarmor-v0.7.2`, `https://github.com/googleapis/google-cloud-node/tree/modelarmor-v0.10.0`, `https://github.com/googleapis/google-cloud-php-modelarmor/tree/v0.8.3`, `https://github.com/googleapis/google-cloud-dotnet/tree/Google.Cloud.ModelArmor.V1-1.0.0-beta07`, `https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/pom.xml` (only in the columns that carry the bullets; to avoid a six-column repeat, main may keep the versions in INV(b) only; see QUESTIONS Q2).
  - INV(b) Client libraries row (L29): replace "Versions of the Java, Node.js, PHP and Python libraries [Not disclosed] (LIB checked; install commands give no pin)" with `Java google-cloud-modelarmor 0.40.0 [Documented] (LIB) [Documented: repo googleapis/google-cloud-java@v1.93.0]; Python 0.7.2, Node.js 0.10.0, PHP 0.8.3 and C# 1.0.0-beta07 as the latest repo tags [Documented: repo googleapis/google-cloud-python@google-cloud-modelarmor-v0.7.2] ...` (one label per repo in separate facts).
  - Summaries: none change.

### T26 — Whether Agent Gateway and Service Extensions forward de-identified (redacted) text
- Verdict: PARTLY RESOLVED. The conflicting statements are all documented and none shows a redacted payload being forwarded; Apigee alone documents extracting redacted data.
- Evidence:
  - AGW intro: "You can configure your template to either block and redact content that violates policies, or to only inspect content and log any violations that are detected." https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
  - AGW flow (ingress): "Model Armor screens the response, and Agent Gateway either allows or blocks it based on the verdict." ; (egress) "Agent Gateway either allows it to reach the agent or blocks it."
  - NET: "Model Armor instructs the networking service to either allow, block, or modify the traffic" https://docs.cloud.google.com/model-armor/model-armor-networking-integration
  - APG: "Apigee allows, blocks, or redacts the request or response. If the request or response is redacted, extract the redacted data using ..." https://docs.cloud.google.com/model-armor/model-armor-apigee-integration
- Label to use: each quote [Documented] (separate bullets, naming the page); whether a de-identified payload is forwarded by Agent Gateway or Service Extensions [Not disclosed] (checked AGW, NET, INT, APG).
- Draft impact:
  - B MA5 R4 ND bullet (Agent Gateway/Service Extensions de-identified forwarding) and MA6 R4/R8: reword as
    `• Agent Gateway page: a template can "block and redact content that violates policies", yet its flow text says the gateway "either allows or blocks it based on the verdict"; the networking page says Model Armor instructs the service to "allow, block, or modify" traffic (Agent Gateway and networking pages, 2026-10-09) **[Documented]**`
    `• Whether Agent Gateway or Service Extensions forward the de-identified text rather than only blocking (checked the Agent Gateway, networking and integrations pages) **[Not disclosed]**`
    Apigee bullet unchanged ("Apigee allows, blocks, or redacts ... extract the redacted data") **[Documented]**.
  - INV(b) Agent Gateway ingress, Agent Gateway egress and Service Extensions rows: add the same pair as a Limitations fact; label as above.
  - Summaries: none change.

### T33 — Skipped Detection for non-English content: two locations named, seven locations without multi-language support
- Verdict: PARTLY RESOLVED. Both statements are documented; no page extends the Skipped Detection note to the other five limited-support locations.
- Evidence:
  - SAN: "Note: In regions with limited multi-language detection support (asia-south1 and northamerica-northeast2), if you send non-English content to detectors like prompt injection and jailbreak or RAI, Model Armor returns a verdict of Skipped Detection for those specific checks." https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
  - FAR: Multi-language detection column "No" for all seven limited-support locations (asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2, northamerica-northeast2) and "Yes" for the full-support locations; the table applies to templates with data residency enforcement on. https://docs.cloud.google.com/model-armor/feature-availability-by-region
  - RN 2026-08-27 (disabling enforcement enables features otherwise unavailable), RN 2026-06-22 and 2026-06-16 (version v3 entries): no multi-language statement.
- Label to use: both quoted facts [Documented]; behaviour in the other five locations [Not disclosed] (checked SAN, FAR, DR, RN).
- Draft impact:
  - A MA1 R2, MA2 R2, MA3 R2, MA4 R2 sanitize-page bullet (L25, L187, L354, L526): keep; add
    `• The feature table shows multi-language detection as "No" in all seven limited-support locations when data residency is enforced, while the Skipped Detection note names only asia-south1 and northamerica-northeast2 (feature availability page, sanitize page, 2026-10-09) **[Documented]**`
    `• What a non-English prompt returns in the other five limited-support locations, including asia-southeast1 (checked the sanitize, feature availability, data residency and release notes pages) **[Not disclosed]**`
  - INV(d) asia-south1 and northamerica-northeast2 Multi-language cells: unchanged; INV RN 1.12: unchanged.
  - A MA3 R8 asia-southeast1 bullet: unchanged (test T32).
  - Summaries: none change.

### T35 — Topic enforcement (C10)
- Verdict: STILL OPEN (checked OV, TPL, EXC, FLR, RT FilterConfig, best-practices, product page, blog; no topic setting, and FLR has no mention of topics). One new observation: "topicality" appears only as a parenthesis on sensitive data protection.
- Evidence:
  - OV scenario: "Enforce custom topics: Scenario: A company's support bot is configured using custom rules to not discuss competitors." https://docs.cloud.google.com/model-armor/overview
  - OV: "...prompt injection and jailbreak detection, and sensitive data protection (including topicality)." and the blog repeats "sensitive data protection (including topicality.)". https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps
  - RT FilterConfig has four settings and no topic setting. https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
- Label to use: scenario and "including topicality" quotes [Documented]; the configuration route [Not disclosed] (checked the pages above); that topic rules would be custom dictionary or regex detectors in an SDP inspect template is [Inferred] (premise: the only parenthesis tying topicality to a filter is sensitive data protection; custom rules are not otherwise described).
- Draft impact:
  - A MA1 R2 and MA2 R2 (L30 to L31; L193 to L194): keep the two bullets; add `• The overview and the blog place "topicality" inside the sensitive data protection filter ("sensitive data protection (including topicality)") (overview, Google Cloud blog, 2026-10-09) **[Documented]**` and `• Topic rules are probably custom detectors in a Sensitive Data Protection template; the premise is the "including topicality" phrase and the absence of any topic setting **[Inferred]**`.
  - INV(a) intro (L7): add "topicality is mentioned only inside the sensitive data protection filter [Documented] (OV)".
  - Summaries: none change.

### T36 — Absence claims for functions Model Armor does not offer
- Verdict: PARTLY RESOLVED. Re-running the searches confirms no filter or setting for hallucination or grounding, refusal, system-prompt leakage or topic enforcement; the product page does market two accuracy-related risks, which the drafts should mention so the absence claim is not read as silence.
- Evidence:
  - Search of OV, TPL, FLR, RT, best-practices, product page and blog for "hallucinat", "grounding", "system prompt", "refus", "leak": no filter. Only: OV "A model's refusal is separate from a Model Armor block"; INT mentions "grounding data" as content that integrations sanitize (a data source, not a check).
  - Product page: "LLM-powered chatbots are fundamental for businesses, but they pose risks like inadvertently leaking sensitive customer PII, providing incorrect policy information, or damaging brand reputation with offensive responses. Model Armor helps mitigate these threats." https://cloud.google.com/security/products/model-armor
  - Product page: "Risks include generating inaccurate, offensive, or off-brand material that could lead to negative public sentiment. Model Armor helps ensure brand safety and integrity."
- Label to use: absence of a filter [Not disclosed] (pages named); the two marketing quotes [Documented]; reading them as not implying a factuality check [Inferred] (premise: the filter list and FilterConfig name none).
- Draft impact:
  - A MA2 R2 (L191), hallucination bullet: `• Hallucination, grounding or factuality filter or setting: none described (checked the overview filter section, templates page detection list, REST `FilterConfig`, blog capabilities, product page features and best practices) **[Not disclosed]**`; add `• The product page lists "providing incorrect policy information" and "generating inaccurate, offensive, or off-brand material" among chatbot and marketing risks and says Model Armor "helps mitigate these threats" and "helps ensure brand safety and integrity" (product page, marketing text, 2026-10-09) **[Documented]**` and `• No accuracy or factuality check is named behind those marketing lines; the premise is that FilterConfig and the filter lists name none **[Inferred]**`.
  - A MA4 R2 (L523) system-prompt-leakage bullet and INV(a) intro: add "best practices" to the pages checked; otherwise unchanged.
  - Summaries: none change.

### T37 — Malicious URL filter: input or output framing
- Verdict: RESOLVED (wording). The overview names both an input-side example (a URL inside a PDF) and an output-side one, so "mainly output" is a judgement, not a quoted fact.
- Evidence:
  - OV: "For example, if a PDF contains an embedded malicious URL, it can be used to compromise any downstream systems processing LLM outputs." ; "This lets you take action and prevent malicious URLs from being returned." ; "scans only the first 256 URLs found in prompts and responses." https://docs.cloud.google.com/model-armor/overview
  - OV document screening: "Model Armor can screen the following types of documents for safety, prompt injection and jailbreak attempts, sensitive data, and malicious URLs".
  - TPL: Malicious URL detection listed among checks "on prompts and responses"; product page: "malicious URLs embedded in prompts or responses"; blog: "in both the input and output".
- Label to use: the quotes [Documented]; "the overview frames the filter mainly around returned URLs" [Inferred] (premise: the section's own wording "returned" and "downstream systems processing LLM outputs").
- Draft impact:
  - A MA7 R1 Summary (L675) [Summary changes], new text (43 words):
    `Summary: **Input-level malicious URL detection.** Model Armor scans the URLs in a user prompt to identify phishing or malware links. The overview gives both a URL inside a PDF and a link returned in a response as examples. The calling service enforces any block. **[Documented]**`
  - A MA7 R1 bullet "The overview frames the filter mainly around output: ... **[Documented]**" becomes two bullets:
    `• The overview section says the filter lets you "prevent malicious URLs from being returned" and speaks of "downstream systems processing LLM outputs" (overview, 2026-10-09) **[Documented]**`
    `• The same section also gives a URL embedded in a PDF as its example and limits scanning to "the first 256 URLs found in prompts and responses", so the filter is not output-only; "mainly output" is a reading **[Inferred]**`
  - A MA8 R1 (L824): no change needed (its Summary already speaks of a returned link).

### T41 — Basic SDP infoTypes: six or seven
- Verdict: PARTLY RESOLVED. The disagreement is real and unreconciled in Google's docs; a code comment confirms "six". The live list is T42 (needs testing).
- Evidence:
  - OV lists six categories (credit card number, US SSN, financial account number, US ITIN, Google Cloud credentials, Google Cloud API key); no PASSWORD. https://docs.cloud.google.com/model-armor/overview
  - RT: "Basic Sensitive Data Protection configuration inspects the content for sensitive data using a fixed set of six info-types." https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
  - Code comment: "content for sensitive data using a fixed set of six info-types. Sensitive" (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:2160).
  - SAN: "The following Sensitive Data Protection infoTypes are scanned in the prompt for all regions: CREDIT_CARD_NUMBER ... FINANCIAL_ACCOUNT_NUMBER ... GCP_CREDENTIALS ... GCP_API_KEY ... PASSWORD: Clear text passwords in configs, code, and other text." and "scanned in the prompt for US-based regions: US_SOCIAL_SECURITY_NUMBER ... US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER". Five plus two makes seven. https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
  - RN: no entry mentions PASSWORD or a change to the basic list (all entries read).
- Label to use: six (OV, RT), six (Go comment) and seven (SAN) each [Documented] (the Go comment [Documented: repo googleapis/google-cloud-go@37f936ac]); "no page reconciles them" [Not disclosed] (checked OV, RT, SAN, RN, Go comment).
- Draft impact:
  - B MA5 R2 bullet "Source conflict: ... no page reconciles the two counts ... **[Documented]**" (cols_b L19 equivalent) and MA6 R2 conflict bullet become
    `• Source conflict: the overview and the REST reference say six items, the sanitize page lists seven (it adds PASSWORD) (overview, REST reference, sanitize page, read 2026-10-09) **[Documented]**`
    `• A Go client comment on the basic configuration also says "a fixed set of six info-types" (modelarmor/apiv1/modelarmorpb/service.pb.go@37f936ac:2160) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
    `• Which count is current: no page reconciles them and no release note mentions PASSWORD (checked the overview, REST reference, sanitize page and release notes) **[Not disclosed]**`
  - B MA5 and MA6 R9: add the service.pb.go blob URL at 37f936ac (apiv1) if not present.
  - INV(a) SDP basic Levels cell and INV RN 1.2: same split.
  - MA5 R2 Summary ("Google's pages disagree on six or seven items") stays valid; no Summary change.

### T43 — Which locations count as "US-based regions"
- Verdict: STILL OPEN (checked SAN, OV, FAR, DR, LOC). No page defines the term.
- Evidence:
  - SAN: "The following additional Sensitive Data Protection infoTypes are scanned in the prompt for US-based regions:" (only occurrence of "US-based" in the pages read). https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
  - OV strategy text: "basic Sensitive Data Protection provides limited infotypes, mainly addressed to the US region."
  - DR and FAR list jurisdiction "United States" for us, us-central1, us-east1, us-east4 and us-west1 (us-east7 appears only in the FAR feature table, without a jurisdiction row).
- Label to use: absence [Not disclosed]; reading "US-based regions means the locations whose jurisdiction is United States" [Inferred] (premise: DR and FAR jurisdiction column; the sanitize page does not say so).
- Draft impact:
  - B MA5 R2 ND bullet (cols_b L20 equivalent): keep; add `• "US-based regions" is probably the set of locations whose jurisdiction is the United States (the us multi-region, us-central1, us-east1, us-east4, us-west1); the premise is the jurisdiction column of the data residency page **[Inferred]**`.
  - INV(a) SDP basic Levels cell: add the same inferred fact; test T42.
  - Summaries: none change.

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T2 | RESOLVED (doc half; effective default stays T1) | three statements [Documented]; applicable default [To be verified] | Yes: MA1 R5 |
| T3 | PARTLY RESOLVED | floor-setting default [Documented]; template default [Inferred] | No |
| T4 | RESOLVED (doc half; trade-off stays T5) | four statements [Documented] | Yes: MA3 R5, MA4 R5 |
| T9 | RESOLVED (doc half; observation stays T10) | table and overview [Documented]; CSAM runs when enforcement off [Inferred] | Yes: MA1 R1, MA2 R1 |
| T11 | PARTLY RESOLVED | quote [Documented]; which filters run on OCR text [Not disclosed] | No |
| T13 | RESOLVED (wording; positive example stays T14) | [Documented]; intended reading [Inferred] | Yes: MA4 R1 |
| T16 | CORRECTION (A is wrong; B is right) | [Documented]; effect of the field [Not disclosed] | Yes: MA2 R3 |
| T18 | PARTLY RESOLVED | absence in Go and Java clients [Documented: repo]; "client lags" [Inferred] | No |
| T19 | PARTLY RESOLVED | usage [Documented]; REST page predates feature [Inferred]; API acceptance [To be verified] | No |
| T20 | RESOLVED | [Documented] (Apigee release notes) | No |
| T21 | STILL OPEN (checked RN, NET, INT, Service Extensions page) | Preview and GKE GA [Documented]; other GA [Not disclosed] | No |
| T22 | RESOLVED (queue ruling plus evidence) | both statements [Documented] | No |
| T23 | PARTLY RESOLVED | rule S stays [Inferred], premise now evidenced | No |
| T24 | PARTLY RESOLVED | resource names [Documented]; stage [Not disclosed]; arguments [To be verified] | No |
| T25 | PARTLY RESOLVED | Java [Documented] and [Documented: repo]; other libraries [Documented: repo] (tags) | No |
| T26 | PARTLY RESOLVED | quotes [Documented]; forwarding of redacted text [Not disclosed] | No |
| T33 | PARTLY RESOLVED | both facts [Documented]; other five locations [Not disclosed] | No |
| T35 | STILL OPEN (checked OV, TPL, EXC, FLR, RT, best practices, product page, blog) | scenario [Documented]; setting [Not disclosed]; route via SDP [Inferred] | No |
| T36 | PARTLY RESOLVED | absence [Not disclosed]; two product-page quotes [Documented] | No |
| T37 | RESOLVED (wording) | quotes [Documented]; "mainly output" [Inferred] | Yes: MA7 R1 |
| T41 | PARTLY RESOLVED | six and seven [Documented]; no reconciliation [Not disclosed] | No |
| T43 | STILL OPEN (checked SAN, OV, FAR, DR, LOC) | [Not disclosed]; reading via jurisdiction [Inferred] | No |

## Report

### Counts per verdict (22 items, all class a; the range has no class c item)
- RESOLVED: 7 (T2, T4, T9, T13, T20, T22, T37)
- PARTLY RESOLVED: 11 (T3, T11, T18, T19, T23, T24, T25, T26, T33, T36, T41)
- STILL OPEN: 3 (T21, T35, T43; each names the pages checked)
- CORRECTION: 1 (T16)
- Class b items T1, T5, T6, T7, T8, T10, T12, T14, T15, T17, T27 to T32, T34, T38 to T40, T42 were not researched (21 items; they stay needs-testing or honest gap).

### CORRECTION items
- T16: A (MA2, MA4, MA8 R3, R6, R8; A RN-3) says the optional `userPrompt` field of sanitizeModelResponse is documented only by the Go client; Google's REST method reference and the Apigee SanitizeModelResponse policy page document it. B (MA6) was already right.

### Summary lines that must change (new text is under each item)
- MA1 R5 (T2): "two different defaults" becomes "three different defaults".
- MA3 R5 and MA4 R5 (T4): add the Low and above advice; MA4 R5 also drops the claim that its response example shows a confidence level.
- MA1 R1 and MA2 R1 (T9): CSAM "cannot be turned off" gets the limited-support-location caveat.
- MA4 R1 (T13): "all show the filter running" reworded to rest on the overview sentence and the sample result.
- MA2 R3 (T16): "the client library has an optional field" becomes "the REST method reference lists an optional field".
- MA7 R1 (T37): "mainly around URLs returned in output" replaced by the two overview examples.
- No other Summary changes. All new Summaries are within 45 words (counts in each item; checked by script on the text as written).

### Items still open
- T21 (GA date for load balancers other than GKE and Secure Web Proxy): Preview 2025-04-09 and GKE GA 2025-09-15 are documented; no GA statement found (RN, NET, INT, Service Extensions page by summarising fetch).
- T35 (topic enforcement configuration): none found; "topicality" appears only inside the sensitive data protection phrase.
- T43 ("US-based regions"): not defined on any page read.
- Partly resolved items that still need a test or another source: effective default levels (T1, behind T2 and T3), live CSAM behaviour in limited locations (T10), RAI, PI and URL filters on OCR text (T12), live acceptance of `filterRuleSettings` (T19), arguments of the Terraform resources (T24), forwarding of redacted text by Agent Gateway and Service Extensions (T26), non-English behaviour in the other five limited-support locations (T32), the live basic infoType list (T42).

### Checks run
- Page reads: about 30 Google docs URLs fetched with `fetch_text.py`, all HTTP 200 except `.../model-armor/pricing` (404, noted above).
- Summary word counts: the seven proposed Summary texts (MA1 R5, MA3 R5, MA4 R5, MA1 R1, MA4 R1, MA2 R3, MA7 R1) counted by script at 34, 35, 38, 45, 37, 42 and 43 words before the label; the MA2 R1 text is the MA1 R1 text with two word swaps (45 words).
- Every quote in the Evidence lines was copied from the fetched text or the cloned files; none exceeds 40 words.

## QUESTIONS

1. Pin form for code facts (main). README section 3 rule 8 says to pin code to the latest release tag; the drafts pin to googleapis/google-cloud-go@37f936ac (repository HEAD of 2026-10-08), while the latest tag is `modelarmor/v1.3.0` (8a17bee208939e0166936a59675414439c47e341). `service.pb.go` for apiv1 and apiv1beta is byte-identical between the two (the diff touches only the two client files, go.mod and go.sum), so every Documented-repo fact holds at the tag. Re-pin to `googleapis/google-cloud-go@modelarmor/v1.3.0` at merge, or keep the sha with a note? (This resolution file keeps 37f936ac so the labels match the drafts.)
2. T25 placement (main). Add the Java, Python, Node.js, PHP and C# versions to the six A R4 columns (five new repo labels and R9 URLs per column) or only to INV(b) Client libraries? Recommended: INV(b) only, one short R4 bullet in A.
3. T23 status rule S (main). Apply it to every banner-free row, or keep [Not disclosed] where the page was not read? No label is upgraded either way.
4. Shared scratch folder (main). `benchtest/scratchpad/resolver/` is shared with the other resolvers; this resolver's files are under `benchtest/scratchpad/resolver/ma1/` only. Another agent's files sit in the parent folder.
5. Service Extensions page (main). `fetch_text.py` returns empty text for `docs.cloud.google.com/service-extensions/...`; only a summarising fetch was possible. If a verbatim read of that page matters for T21, try the page's HTML through a different route.
