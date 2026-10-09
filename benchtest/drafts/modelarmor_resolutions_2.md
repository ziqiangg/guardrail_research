# Model Armor resolutions 2 (P5, resolver 2 of 2)

Date 2026-10-09. Resolver: gr-resolver. Product: modelarmor. Triage: `benchtest/drafts/modelarmor_triage.md`. Rulings applied: R007 (item 4: code at a pinned ref outranks page examples; item 5: absence is Not disclosed), R011, R012, R013, R015, R017 (ten columns; antivirus and tool-call screening inventory only; no response-side file or image split; Preview features included and labelled Preview with the date read), R018 (SD1 to SD6 exist, prefix `Sensitive Data Protection:`), R019 (read-only research; Google terms pages may be cited).

Items handled (range T44 to T87, class a and c, plus the priority class b items T44 and T45, and short doc-half checks on T49, T61 and T63): T44, T45, T47, T49, T50, T52, T53, T54, T55, T56, T57, T58, T60, T61, T63, T66, T67, T68, T70, T71, T76, T77, T78, T79, T80, T81, T82, T83, T84, T85, T86, T87. Class b items not touched (they stay open for the bench): T46, T48, T51, T59, T62, T64, T65, T69, T72, T73, T74, T75. T1 to T43 belong to modelarmor_resolutions_1.md; T41 appears only in the cross-range note at the end because the assignment named it as a priority.

## Method and access notes

- Every Google docs page was re-fetched live on 2026-10-09 with `python benchtest/tools/fetch_text.py` (raw text, status 200, final URL equal to the request unless noted) into `benchtest/scratchpad/resolver/ma2/`. The drafter's local copies in `scratchpad/drafter/ma_pages/` were not used as sources. One page differed from the drafter's copy: the release notes entry the drafts call "October 10, 2026" now reads "October 09, 2026" (T78).
- Page footers were read for every page cited (T80). Link targets were read from the raw HTML of the overview page with `scratchpad/resolver/ma2_hrefs.py` (stdlib GET; T56, T85).
- Code: `git clone --depth 1 --filter=blob:none --sparse https://github.com/googleapis/google-cloud-go` (R013), HEAD was exactly 37f936ac9d69e173da0ba4123e382c52b2dd741f (commit date 2026-10-08), `modelarmor` directory checked out; `GoogleCloudPlatform/apigee-samples` shallow clone, HEAD 2b1a9f00fabb4e837c39d80570ff50ebc3b1349e. Both clones are under the session scratchpad, not in the repo. No code was run.
- Google-owned pages outside the Model Armor docs, cited under R019 and the queue ruling on Google API pages: Sensitive Data Protection infoTypes reference and metadata-label page, the Security Command Center findings page, the dlp.googleapis.com discovery document, Google Cloud General Service Terms, Acceptable Use Policy, services list, data-residency services list and product launch stages page.
- Not readable or not used: nothing was unreadable. The GitHub API and github.com pages were not used (R015). No vendor API was called; the discovery document is a static GET.
- Short names (docs pages are under https://docs.cloud.google.com/model-armor/ unless stated): OV overview; TPL manage-templates; SAN sanitize-prompts-responses; FLR configure-floor-settings; QUO quotas; FAR feature-availability-by-region; DR data-residency; LOC locations; FV set-filter-version; RN release-notes; EXC configure-exclusion-rules; LOG configure-logging; INT integrations; GE model-armor-gemini-enterprise-integration; APG model-armor-apigee-integration; VTX model-armor-vertex-integration; AGW model-armor-agent-gateway-integration; LC model-armor-langchain-integration; RT reference/rest/v1/projects.locations.templates; RR reference/rest/v1/SanitizationResult; DI reference/rest/v1/DataItem; FS reference/rest/v1/FloorSetting. Other: PROD https://cloud.google.com/security/products/model-armor; PRC https://cloud.google.com/security-command-center/pricing; APR https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy; SDPI https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference; SDPM https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels; SCCF https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings; GST https://cloud.google.com/terms/service-terms; AUP https://cloud.google.com/terms/aup; TSV https://cloud.google.com/terms/services; TDR https://cloud.google.com/terms/data-residency; LST https://cloud.google.com/products.
- Pinned code URLs: GO = https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go (label `[Documented: repo googleapis/google-cloud-go@37f936ac]`); AS = https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml (label `[Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00]`).
- Draft line numbers below are those of the draft files as read on 2026-10-09 (`modelarmor_cols_a.md`, `modelarmor_cols_b.md`, `modelarmor_inventory.md`). Column order inside cols_a.md: MA1 line 1 onward, MA2 line 167 onward, MA3 line 335 onward, MA4 line 510 onward, MA7 line 680 onward, MA8 line 835 onward.

---

### T44 — Does the basic SDP infoType list also apply to responses
- Verdict: PARTLY RESOLVED (advanced mode on responses is documented; basic mode on responses stays not stated: checked the sanitize page, overview, templates page, REST references and Apigee policy page)
- Evidence:
  - SAN, basic section: "The following Sensitive Data Protection infoTypes are scanned in the prompt for all regions:" and "The following additional Sensitive Data Protection infoTypes are scanned in the prompt for US-based regions:". No response-side repeat of the list exists.
  - SAN, advanced section: "Model Armor screens the LLM prompts and responses using the advanced Sensitive Data Protection configuration setting."
  - TPL (Set Sensitive Data Protection settings, note): "Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding."
  - RT: `sdpSettings` is a member of `filterConfig` with only `basicConfig` or `advancedConfig`; no direction field (checked the SdpFilterSettings, SdpBasicConfig and SdpAdvancedConfig sections).
  - AS line 44: the Google Apigee sample tests `SanitizeModelResponse.SMR-Sanitize-Model-Response.sdpFilterResult.inspectResult.matchState = "MATCH_FOUND"` alongside the prompt-side condition (supporting sample only, R013).
- Label to use: advanced mode on responses `[Documented]`; sample condition `[Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00]`; basic list on responses is an absence `[Not disclosed]`; the working reading that basic mode runs on responses with the same list `[Inferred]` (premise: one template-level `sdpSettings` with no direction field serves both methods).
- Draft impact:
  - `modelarmor_cols_b.md` MA6 R2 Summary (line 168). Before: "The documented lists are written for prompts: a short, US-leaning fixed list in basic mode and the customer template in advanced mode. Model Armor docs do not say whether the basic list is the same for responses. **[Documented]**". After (38 words): `Summary: **Sensitive items a model might output.** The documented basic lists are written for prompts: a short, US-leaning fixed list. Advanced mode uses the customer's template. Google's pages do not say whether the basic list also applies to responses. **[Not disclosed]**`
  - MA6 R2, insert after line 173 (the "scanned in the prompt" bullet, keep it):
    - `• Advanced mode on responses: "Model Armor screens the LLM prompts and responses using the advanced Sensitive Data Protection configuration setting." (sanitize page, read 2026-10-09) **[Documented]**`
    - `• Template note: "Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding." (templates page, read 2026-10-09) **[Documented]**`
    - `• Google's Apigee sample checks the response-side result: its shared flow tests SanitizeModelResponse.SMR-Sanitize-Model-Response.sdpFilterResult.inspectResult.matchState for MATCH_FOUND (llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml:44) **[Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00]**`
    - `• Basic mode probably scans responses with the same list as prompts. Premise: the basic or advanced setting sits once in the template filter config, which has no direction field and is used by both sanitize methods (templates reference, read 2026-10-09) **[Inferred]**`
  - MA6 R8, bullet 1 (line 261). After: `• Whether the basic infoType list is the same for responses as for prompts (checked the sanitize page, overview, templates page, REST references and the Apigee policy page; the lists say "scanned in the prompt"; needs testing)`
  - MA6 R9: add `• https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/llm-security-v2/sharedflowbundles/ModelArmor-v2/sharedflowbundle/sharedflows/default.xml`
  - `modelarmor_inventory.md` (a) "Sensitive Data Protection (SDP), basic configuration", cell "Applies to (Input/Output)". Append: ` Whether the basic infoType list applies to responses [Not disclosed] (checked OV, SAN, TPL, RT, APR). The setting has no direction field in RT [Documented] (RT), so the same list on responses is probable [Inferred].`

### T45 — No documented response-side de-identification result
- Verdict: PARTLY RESOLVED (the docs state where response-side de-identified text appears; no response example exists, so the shape stays untested)
- Evidence:
  - TPL (same note as T44): "Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding."
  - APR (flow variables table): "Sdp filter de identify result execution state. Valid values include EXECUTION_SUCCESS and EXECUTION_SKIPPED." for `SanitizeModelResponse.POLICY_NAME.sdpFilterResult.deidentifyResult.executionState`, and the same for `.matchState`.
  - SAN: the sanitizeModelResponse examples ("IP address of the current network is ##.##.##.##", the exclusion-rule example) return `rai`, `pi_and_jailbreak`, `csam` and `malicious_uris` results and no `sdp` result; the only `deidentifyResult` examples are prompt-side (`data.text` "is there anything malicious running on [IP_ADDRESS]?").
  - RR: one `SdpFilterResult` type serves both methods (no response-specific type).
- Label to use: statements above `[Documented]`; absence of any response-side example `[Not disclosed]`; same shape as prompt side `[Inferred]` (premise: one result type, one template setting).
- Draft impact:
  - `modelarmor_cols_b.md` MA6 R3 Summary (line 181). Before: "...Documented examples for response-side de-identification are missing. **[Documented]**". After (32 words): `Summary: **The model response, sent in its own field.** The text goes to the regional response-sanitising method, with an optional field for the matching user prompt. Google shows no worked response-side de-identification example. **[Not disclosed]**`
  - MA6 R3, replace line 187 (currently `[Not disclosed]`, keep) and add after it: `• The templates page says the de-identified "prompts or responses" are returned in `deidentifyResult.data.text`, so response-side de-identified text is documented in prose but not by example (templates page, read 2026-10-09) **[Documented]**`
  - MA6 R8, bullet 2 (line 262). After: `• A real response-side `deidentifyResult` and findings (needs testing; the templates page names the field but the sanitize page has no response example)`
  - `modelarmor_inventory.md` (a) "SDP, advanced configuration", cell "Result field". Append: ` A response-side example of deidentifyResult [Not disclosed] (checked SAN, TPL, RR, APR).`

### T47 — filterResults shape: keyed map or array
- Verdict: RESOLVED (code at the pinned tag and the REST reference agree on a keyed map; six of eight sanitize-page examples are keyed; the two array examples are the outliers; a live call is still the final check)
- Evidence:
  - GO line 2559 to 2561: "Output only. Results for all filters where the key is the filter name - either of "csam", "malicious_uris", "rai", "pi_and_jailbreak" ,"sdp"." and `FilterResults map[string]*FilterResult`.
  - RR: `filterResults` is documented as a keyed object (csam, malicious_uris, rai, pi_and_jailbreak, sdp).
  - SAN: `"filterResults": {` (object) in six examples (lines 275, 680, 754, 807, 2526, 2847 of the raw text) and `"filterResults": [` (array) only in the basic and advanced SDP prompt examples (lines 2011 and 2483).
- Label to use: Go type `[Documented: repo googleapis/google-cloud-go@37f936ac]`; page examples `[Documented]`; "the array examples are probably an older or abbreviated sample format" `[Inferred]` (R007 item 4: prefer code at a pinned ref).
- Draft impact:
  - `modelarmor_cols_b.md` MA5 R5, replace bullet at line 87 and add two bullets after line 87:
    - `• The sanitize page shows `filterResults` as a keyed object in six of its eight example responses and as an array of single-key objects in the two Sensitive Data Protection prompt examples (basic and advanced) (sanitize page, read 2026-10-09) **[Documented]**`
    - `• The pinned Go library types the field as `map[string]*FilterResult` and describes it as "Results for all filters where the key is the filter name" (service.pb.go@37f936ac:2559) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
    - `• The REST reference and the pinned Go type agree on a keyed map, so the two array examples are probably an older or abbreviated sample format; the live shape is untested. Premise: code at the pinned tag outranks page examples **[Inferred]**`
  - MA5 R8 bullet 7 (line 126). After: `• Whether a live call returns `filterResults` as the keyed map in the REST reference and the Go library or as the array in two sample responses (needs one test call)`
  - MA6 R5 bullet at line 234 (conflict): same three bullets as MA5 R5 (replace the single bullet); MA6 R9 and MA5 R9 already contain the Go blob URL.
  - No Summary change (MA5 R5 and MA6 R5 Summaries do not mention the shape).

### T49 — De-identified text or redacted image when enforcement is INSPECT_ONLY
- Verdict: STILL OPEN (checked OV enforcement section, TPL, RT, SAN, GE and VTX; nothing ties returned de-identified data to the enforcement type; needs testing)
- Evidence: TPL: "If you specify Inspect template and De-identify template, Model Armor returns the de-identified sensitive data and sanitized version of prompts or responses in the deidentifyResult.data.text field of the finding." OV (Inspect only): "it doesn't stop the request or response from being processed by the integrated service." Neither sentence mentions de-identified output under Inspect only.
- Label to use: `[Not disclosed]` for the absence (names what was checked).
- Draft impact: none to text; the R8 bullets in MA5 (line 123), MA6 (line 268) and MA10 (line 555) stay as they are (they already say "needs testing"). Optional: append "checked OV, TPL, RT, SAN, GE and VTX" to the MA6 and MA10 bullets.

### T50 — Do floor settings accept an advanced inspect template
- Verdict: PARTLY RESOLVED (schema: yes by type; the same-location rule for a floor setting that lives at `locations/global` is not addressed)
- Evidence:
  - FS: `filterConfig` is "object (FilterConfig)" and "Required. ModelArmor filter configuration."
  - GO line 1128 to 1129: "Required. ModelArmor filter configuration." `FilterConfig *FilterConfig` in `FloorSetting`.
  - RT (SdpFilterSettings): `advancedConfig` is "Optional. Advanced Sensitive Data Protection configuration which enables use of Sensitive Data Protection templates." in the same `FilterConfig` type that FS reuses.
  - FLR: "Optional: If you select Sensitive Data Protection detection, configure the Sensitive Data Protection settings." and "Floor settings don't check templates for Sensitive Data Protection conformance."
  - VTX floor-setting example sets only `"sdpSettings": {"basicConfig": { "filterEnforcement": "ENABLED" }}`. SAN: "the Sensitive Data Protection templates must be in the same location as the Model Armor template." Floor settings are at `.../locations/global/floorSetting` (FLR, DR). No page says where the SDP templates must be for a floor setting.
- Label to use: type identity `[Documented]` and `[Documented: repo googleapis/google-cloud-go@37f936ac]`; "floor settings can carry an advanced inspect template" `[Inferred]` (premise: same FilterConfig type); the location rule `[Not disclosed]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA5 R6, insert after line 105:
    - `• A floor setting's `filterConfig` is the same `FilterConfig` type as a template's, which includes `sdpSettings.advancedConfig` (FloorSetting and templates REST references, read 2026-10-09) **[Documented]**`
    - `• The pinned Go `FloorSetting` has `FilterConfig *FilterConfig` (service.pb.go@37f936ac:1129) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
    - `• A floor setting can therefore carry an advanced inspect template. Premise: the shared FilterConfig type; no page shows an example, and the only floor-setting example uses basic mode **[Inferred]**`
    - `• Which location the inspect template must be in for a floor setting stored at `locations/global` is not stated (checked the floor settings, sanitize and Agent Platform pages and both REST references) **[Not disclosed]**`
  - MA5 R8 bullet 5 (line 124). After: `• Which location an advanced inspect template must have when it is used from a floor setting at locations/global (checked the floor settings page, Agent Platform page and REST references, not stated; needs testing)`
  - MA5 R9: add `• https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting`
  - No Summary change.

### T52 — Over-limit behaviour is "skipped" or "MATCH_FOUND is still returned"
- Verdict: CORRECTION (the R6 Summaries of MA5 and MA6 and the R6 and R5 bullets of MA1 to MA4, MA5, MA6 and MA9 overstate "skipped")
- Evidence (QUO, token system limits): "If a filter detects a match, it returns MATCH_FOUND." and "If a filter doesn't detect a match, the value it returns depends on whether the prompt or response exceeds the filter's token limit:" then "If the prompt or response exceeds the filter's token limit, the filter returns EXECUTION_SKIPPED and includes Detection skipped as token limit exceeded. in the filter result's messageItems field." The table gives 65,536 for prompt injection and jailbreak, responsible AI and CSAM and 130,000 for Sensitive Data Protection. RN 2025-07-28 (history): "MATCH_FOUND is returned if malicious content is found, and SKIP_DETECTION is returned if no malicious content is found." QUO does not say whether text beyond the limit is scanned.
- Label to use: `[Documented]` for the rule; "a payload longer than the limit may be only partly screened" `[Inferred]` (premise: QUO says Model Armor "screens text up to 65,536 tokens"); behaviour on a match located after the limit is untested.
- Draft impact:
  - New Summaries (word counts excluding the label):
    - MA5 R6, `modelarmor_cols_b.md` line 90 (44 words): `Summary: **Template, location and a per-mode setting.** Basic mode needs one switch; advanced mode needs inspect and optional de-identify templates in the same location. Cross-project use needs two Sensitive Data Protection roles. Past 130,000 tokens a match still counts; no match gives a skipped check. **[Documented]**`
    - MA6 R6, line 237 (45 words): `Summary: **Template, location and the response text.** Template settings, roles and the location rule are as for prompts; the response goes in its own field. Past 130,000 tokens a match still counts; no match gives a skipped check. Cross-project use needs two Sensitive Data Protection roles. **[Documented]**`
  - Detail bullets, replacing the sentence "Over the limit the filter returns `EXECUTION_SKIPPED` with the message ..." in MA1 R6 (line 103), MA2 R6 (line 270), MA3 R6 (line 436), MA4 R6 (line 610):
    - `• Over the limit, a filter that finds a match still returns MATCH_FOUND; a filter that finds no match returns `EXECUTION_SKIPPED` with "Detection skipped as token limit exceeded." in `messageItems` (quotas page, 2026-10-09) **[Documented]**`
    - `• A payload longer than the limit may be only partly screened. Premise: the quotas page says Model Armor "screens text up to 65,536 tokens" and states the skip result only for the no-match case **[Inferred]**`
  - MA5 R5 bullet line 83 and MA6 R5 bullet line 230: replace with `• Over the 130,000-token limit a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**`
  - MA5 R6 bullet line 98 and MA6 R6 bullet line 243: no change needed beyond the Summary.
  - MA9 R5 bullet line 373: replace with `• Token overflow in extracted text: a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**`
  - `modelarmor_inventory.md` (a), cell "Limit": RAI row, CSAM row, PI row. Replace "above that the filter returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.'" with "above that a filter that finds a match still returns MATCH_FOUND and a filter that finds none returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.'" (CSAM row says "same EXECUTION_SKIPPED behaviour as the RAI filter": leave). SDP basic and SDP advanced rows: append the same sentence after "130,000 tokens [Documented] (QUO)". (e) row "Sensitive Data Protection token limit", cell "When exceeded": replace "when no match was found within the limit" with "when the filter finds no match and the text exceeds the limit" (QUO does not say "within the limit").

### T53 — Does the 130,000-token SDP limit apply to the text sent by integrations
- Verdict: PARTLY RESOLVED (Gemini Enterprise exempt on two pages; Apigee stated as limited; other routes not stated)
- Evidence:
  - QUO: "Note: These token limits don't apply to the Model Armor integration with Gemini Enterprise."
  - GE: "There are no token limits when you use Model Armor with Gemini Enterprise."
  - APG: "Token limits: Model Armor has token limits for processing prompts and responses, which vary by filter. Content exceeding these limits might not be fully scanned."
  - Checked VTX, AGW (only "unlimited tokens in the stream" for real-time streaming), the networking page and the MCP page: no token statement.
- Label to use: Gemini Enterprise and Apigee `[Documented]`; Agent Platform, Agent Gateway (non-streaming), Service Extensions and MCP routes `[Not disclosed]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA5 R6, insert after line 98 (and MA6 R6 after line 243):
    - `• Apigee route: "Model Armor has token limits for processing prompts and responses, which vary by filter. Content exceeding these limits might not be fully scanned." (Apigee integration page, read 2026-10-09) **[Documented]**`
    - `• Whether the token limits apply on the Agent Platform, Agent Gateway (non-streaming), Service Extensions and MCP routes is not stated (checked the quotas page and the five integration pages) **[Not disclosed]**`
  - MA5 R8 bullet 9 (line 128). After: `• Whether the 130,000-token limit applies on the Agent Platform, Agent Gateway, Service Extensions and MCP routes (Gemini Enterprise is exempt and Apigee is limited per the integration pages; the others are not stated)`
  - `modelarmor_inventory.md` (b) rows for Agent Platform, Agent Gateway ingress, Service Extensions, MCP: append to "Limitations": ` Token limits on this route [Not disclosed] (checked QUO and the route page).`
  - No Summary change.

### T54 — Real-time streaming "unlimited tokens" without the chunk caveat
- Verdict: RESOLVED
- Evidence: QUO: "When you sanitize streaming text in real-time mode, Model Armor supports unlimited tokens. In contrast, buffered streaming mode is subject to the token limits listed in the preceding table." SAN: "To sanitize the content effectively, make sure that individual chunks don't exceed the token limits."
- Label to use: `[Documented]`.
- Draft impact:
  - `modelarmor_cols_a.md` R6 of MA1 (line 104), MA2 (line 271), MA3 (line 437), MA4 (line 611): replace the combined bullet (streaming plus Gemini Enterprise exemption) with three bullets:
    - `• In real-time streaming mode Model Armor "supports unlimited tokens"; buffered streaming mode keeps the token limits (quotas page, sanitize page, 2026-10-09) **[Documented]**`
    - `• For streamed content, "make sure that individual chunks don't exceed the token limits" (sanitize page, 2026-10-09) **[Documented]**`
    - `• The token limits "don't apply to the Model Armor integration with Gemini Enterprise" (quotas page, 2026-10-09) **[Documented]**`
  - `modelarmor_cols_b.md` MA5 R6 line 100: replace with the first two bullets above plus the existing clause "streaming does not de-identify" as its own bullet: `• Streaming methods do not support Sensitive Data Protection de-identification (sanitize page, read 2026-10-09) **[Documented]**`. MA6 R3 line 190 already carries the streaming de-identification fact; add the chunk bullet after it.
  - `modelarmor_inventory.md` (e) "Real-time streaming" row already carries the caveat: none.
  - No Summary change.

### T55 — Singapore NRIC: custom detector or built-in infoType
- Verdict: CORRECTION (MA5 R7 and MA6 R7 say a custom detector is needed; the built-in infoType exists)
- Evidence:
  - SDPI: "SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER" described as "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card." and listed with availability `ANY_LOCATION`, categories GOVERNMENT_ID, PII, SPII (raw text lines 406 and 1352). Consistent with `sdp_cols_a.md` line 27 and `sdp_cols_b.md` line 229.
  - TPL (advanced mode): an inspect template holds "Templates for saving configuration information for inspection scan jobs, including what predefined or custom detectors to use."
  - OV, SAN and RT basic mode: no Singapore identifier (the basic list is the six or seven US-leaning items, see T41).
  - FAR: asia-southeast1 lists Sensitive Data Protection as supported with data residency enforced.
- Label to use: infoType exists `[Documented]` (Google SDP docs, cited as the owner's page); route through an advanced inspect template `[Inferred]` (premise: inspect templates hold "predefined or custom detectors"; no Model Armor page shows a built-in non-US infoType in an inspect template).
- Draft impact:
  - `modelarmor_cols_b.md` MA5 R7, replace bullet line 114 with:
    - `• Singapore (asia-southeast1) lists Sensitive Data Protection as supported, but basic mode names only US national identifiers (feature availability page, overview and sanitize page, read 2026-10-09) **[Documented]**`
    - `• Singapore NRIC is a built-in Sensitive Data Protection infoType: SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER, "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card.", available in any location (Sensitive Data Protection infoTypes reference, read 2026-10-09) **[Documented]**`
    - `• A Singapore NRIC test therefore needs an advanced template whose inspect template lists that built-in infoType; no custom detector is needed. Premise: an inspect template holds "what predefined or custom detectors to use" (templates page) **[Inferred]**`
  - MA6 R7, replace bullet line 256 with the same three bullets, ending the third with "...on model output".
  - MA5 R9 and MA6 R9: add `• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference`.
  - No Summary change (neither R7 Summary names Singapore).
  - Cross-product note for the merger: the infoType reference is read by the sdp resolver; the SD1 R2 and SD5 wording needs no change.

### T56 — Forward references to the Sensitive Data Protection columns
- Verdict: RESOLVED (premise confirmed from the page HTML; the SD columns exist per R018)
- Evidence: OV raw HTML links: `/sensitive-data-protection/docs/infotypes-reference` ("infoTypes"), `/sensitive-data-protection/docs/likelihood` ("Sensitive Data Protection match likelihood") and `/sensitive-data-protection/docs/sensitive-data-protection-overview` ("Sensitive Data Protection overview"). R018 item 2: six columns SD1 to SD6, prefix `Sensitive Data Protection:`, no fold or split. R012: MA5 and MA6 stay and cross-reference.
- Label to use: link fact `[Documented]` (hrefs read from the overview page HTML, 2026-10-09); scope sentence stays `[Inferred]` but its premise is now sourced.
- Draft impact:
  - `modelarmor_cols_b.md` MA5 R1 line 11, MA6 R1 line 166, MA10 R1 line 452: split each into a `[Documented]` link bullet and the existing scope bullet, e.g. MA5 R1:
    - `• The overview links to the Sensitive Data Protection infoTypes reference, match likelihood and overview pages (overview page links, read 2026-10-09) **[Documented]**`
    - `• Sensitive Data Protection is a separate Google Cloud service that Model Armor calls; its infoType catalogue, transformation types and likelihood meaning are covered in the Sensitive Data Protection columns on sheet 3, so this column covers only how Model Armor invokes it. The premise is that the overview links out for these topics (previous bullet) **[Inferred]**`
  - Wording "the Sensitive Data Protection columns on sheet 3" stays correct. Mapping for the merger and the grouper: MA5 and MA6 relate to SD1 (text detection) and SD3 (text de-identification), and advanced-mode inspect templates may draw on SD2 custom detectors [Inferred]; MA10 relates to SD5 (images).
  - MA10 R1 bullet: same two-bullet pattern ending "...covered in the Sensitive Data Protection columns on sheet 3 for images".
  - MA5 R9, MA6 R9, MA10 R9: no new URL (overview already listed).

### T57 — Antivirus scanning: configuration setting and Summary impact
- Verdict: PARTLY RESOLVED (scope settled by R017 item 2: inventory only; configuration still not found; two label corrections needed)
- Evidence:
  - Checked and no antivirus setting: RT FilterConfig (raiSettings, sdpSettings, piAndJailbreakFilterSettings and maliciousUriFilterSettings only), FS, FLR, TPL, OV, SAN, QUO, INT, SCCF findings list (only FLOOR_SETTINGS_VIOLATION), the Go v1 `FilterConfig` (four fields, service.pb.go@37f936ac:1861 to 1873) and the Go v1beta `FilterConfig` (the same four fields, apiv1beta service.pb.go@37f936ac:1928 to 1934).
  - Present: PROD: "Detects malicious files, malware, and unsafe URLs within AI prompts and responses." FAR: "Antivirus scanning" listed among the filters of full-support regions and as a by-region column. RR: `VirusScanFilterResult` with `scannedContentType` and "PDF Scanning for only PDF is supported." RN 2026-04-10: "The level of detail provided in the virusDetails field of the Antivirus filter scan results has been updated."
- Label to use: the four facts above `[Documented]`; configuration not found `[Not disclosed]` (replaces `[To be verified]`); "antivirus is a separate capability outside the MA7 and MA8 columns" `[Inferred]` (premise: its own result type, no URL element, no setting, R017 item 2).
- Draft impact:
  - `modelarmor_cols_b.md` MA9 R1, replace bullet line 313: `• Antivirus scanning is covered only in the inventory sheet, not as a Table 3 column; no configuration for it (a template setting, enable flag or threshold) appears in the templates reference, the FilterConfig in the Go v1 library, the floor settings page, the templates page, the overview, the sanitize page or the Security Command Center findings page (checked all) **[Not disclosed]**`
  - `modelarmor_cols_a.md` MA7 R2 line 701 and MA8 R2 line 852: replace the single `[Documented]` bullet with:
    - `• The product page says Model Armor "Detects malicious files, malware, and unsafe URLs within AI prompts and responses", the region tables list "Antivirus scanning" and the result schema has a `virusScanFilterResult` for PDF (product page, feature availability page, REST result ref, 2026-10-09) **[Documented]**`
    - `• Antivirus scanning is a separate capability outside this column. Premise: it has its own result type, no URL element and no configuration setting, and the project covers it in the inventory only **[Inferred]**`
  - `modelarmor_inventory.md` (a) "Antivirus scanning", cell "Config key": change "(checked OV, TPL, SAN, FLR, FAR and RN; no configuration page found)" to "(checked OV, TPL, SAN, FLR, FAR, RN, QUO, INT and SCCF; no configuration page found) [Not disclosed]" and drop `[To be verified]` there; cell "Source URL": add `https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings`.
  - No Summary change (no R1 or R2 Summary of MA7, MA8 or MA9 mentions antivirus). CP1 decision D4 is covered by R017 item 2.

### T58 — Images embedded in files: three pages disagree
- Verdict: STILL OPEN (checked OV, INT, GE, RN 2025-09-16 and 2026-06-25, SAN and the Go comments; the conflict stands and no page reconciles it)
- Evidence:
  - OV (image screening limitations, direct methods): "Model Armor doesn't screen images embedded within files."
  - INT (Gemini Enterprise section): "However, images embedded in documents aren't screened."
  - GE: "Images contained inside other files and documents that you upload directly.", listed under files the integration screens.
  - GO lines 3431 to 3435 (`SdpContentLocation.ContainerName`): "Nested names could be absent if the embedded object has no string identifier (for example, an image contained within a document)." This is a result-schema comment, not a statement that Model Armor screens embedded images.
- Label to use: three page statements `[Documented]` (two bullets stay per README rule 4, plus a third for INT); the schema comment `[Documented: repo googleapis/google-cloud-go@37f936ac]`; "no page reconciles them" `[Not disclosed]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA9 R2, after line 327 add: `• No page reconciles the three statements on embedded images (checked the overview, integrations page, Gemini Enterprise page, release notes 2025-09-16 and 2026-06-25, and the sanitize page) **[Not disclosed]**` and `• The pinned Go comment for the finding container says nested names "could be absent if the embedded object has no string identifier (for example, an image contained within a document)", so the result schema allows an embedded-image container (service.pb.go@37f936ac:3433) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
  - MA10 R2, after line 463 add the INT bullet: `• Source conflict on embedded images (3): the integrations page says "images embedded in documents aren't screened" for the Gemini Enterprise integration (integrations page, read 2026-10-09) **[Documented]**` and the same "No page reconciles" bullet.
  - Summaries unchanged (MA9 R2 and MA10 R2 Summaries already state both sides).
  - `modelarmor_inventory.md` (a) "Image text extraction (OCR)", cell "Limit". Replace "images embedded in files are not screened;" with "images embedded in files are not screened per OV [Documented] (OV), and INT says the same for the Gemini Enterprise integration [Documented] (INT), while GE lists images inside uploaded files as screened [Documented] (GE), and no page reconciles them [Not disclosed] (checked OV, INT, GE, RN, SAN);".
  - The live test stays T59 (class b).

### T60 — Gemini Enterprise modalities: INT table says text and documents, GE page adds images
- Verdict: STILL OPEN (conflict confirmed and characterised; checked INT, GE, RN 2025-09-16 and 2026-06-25; no page reconciles it)
- Evidence: INT options table row "Gemini Enterprise | Only using templates | Text, documents | Yes | Yes". INT services section: "In addition to the modalities listed in Supported modalities, the Model Armor integration with Gemini Enterprise also supports documents." GE: "In addition to text prompts, the integration supports documents (such as PDFs) and images." RN 2025-09-16 and 2026-06-25 do not mention modalities for Gemini Enterprise.
- Label to use: `[Documented]` for each statement as two bullets; `[Not disclosed]` for the absence of a reconciling page.
- Draft impact:
  - `modelarmor_cols_b.md` MA10 R3, after line 486 add `• No page reconciles the two lists (checked the integrations page, the Gemini Enterprise page and release notes 2025-09-16 and 2026-06-25) **[Not disclosed]**`. MA10 R4 line 499 and MA10 R8 line 558: no change.
  - `modelarmor_inventory.md` (b) "Gemini Enterprise", cell "Modalities": append ` No page reconciles the two lists [Not disclosed] (checked INT, GE, RN).`
  - No Summary change.

### T61 — Response-side file and image support (CP1 alt (e))
- Verdict: STILL OPEN (column split settled by R017 item 3: no response-side split; the behaviour itself is a needs-testing item, no new doc evidence in this pass)
- Evidence: R017 item 3 ("No response-side file/image split (alt (e) rejected); T61 stays a needs-testing item"). RT, DI, SMR and GO line 2379 were re-read: `modelResponseData` is a `DataItem`; no response request body with a file or image appears.
- Label to use: unchanged (`[To be verified]` or `[Not disclosed]` as drafted).
- Draft impact: none.

### T63 — Result returned for a file over 4 MB
- Verdict: STILL OPEN (checked QUO, OV, RN 2025-09-27 and RR; the skip is stated, the returned code is not)
- Evidence: QUO: "If a file or image exceeds this limit, Model Armor skips scanning it." RN 2025-09-27: "Model Armor limits the maximum input size for files and text to 4 MB, automatically skipping any content that exceeds this threshold." Neither names an error or a filter result.
- Label to use: `[Not disclosed]` as drafted.
- Draft impact: none (MA9 R5 bullet line 371 and R8 bullet line 407 already say this).

### T66 — Rich documents with metadata labels: what the request needs
- Verdict: PARTLY RESOLVED (the Sensitive Data Protection page answers the configuration; no Model Armor request field for metadata exists)
- Evidence:
  - SDPM: "To use this feature with Model Armor—or services that use Model Armor like Gemini Enterprise—you must create an advanced Sensitive Data Protection configuration in Model Armor that references this custom metadata label detector."
  - SDPM, supported formats: "Google Drive labels", "Microsoft sensitivity labels on the following file types:" DOCX, PDF, PPTX, XLSX, and "Client-provided metadata". Unsupported: "Custom metadata label detectors aren't supported in the following:" Inspection rule sets; De-identification transformations.
  - SDPM: client-provided metadata is passed in the `ContentMetadata` field of the Sensitive Data Protection `ContentItem`. DI, SMR and the sanitizeUserPrompt reference list no metadata field (`byteItem` has `byteDataType`, `byteData`, `fileLabel`).
  - RN 2026-04-06: "Model Armor can sanitize data passed in as rich documents that have specific metadata labels."
- Label to use: SDP page statements `[Documented]` (Google Sensitive Data Protection docs); "no Model Armor field carries client-provided metadata" `[Not disclosed]` (checked DI, SMR, the sanitizeUserPrompt reference, SAN).
- Draft impact:
  - `modelarmor_cols_b.md` MA9 R2, replace bullet line 324 with:
    - `• Rich documents with metadata labels: release note 2026-04-06 says Model Armor "can sanitize data passed in as rich documents that have specific metadata labels" (release notes, read 2026-10-09) **[Documented]**`
    - `• It needs a custom metadata-label infoType in an advanced Sensitive Data Protection configuration of the Model Armor template; detected labels are Google Drive labels and Microsoft sensitivity labels on DOCX, PDF, PPTX and XLSX (Sensitive Data Protection custom metadata label page, read 2026-10-09) **[Documented]**`
    - `• Custom metadata label detectors are not supported in inspection rule sets or de-identification transformations (Sensitive Data Protection custom metadata label page, read 2026-10-09) **[Documented]**`
    - `• A Model Armor request field for client-provided metadata is not documented (checked the DataItem, sanitizeUserPrompt and sanitizeModelResponse references and the sanitize page) **[Not disclosed]**`
  - MA9 R8 bullet 9 (line 413): delete (answered) or reduce to `• Whether the rich-document metadata-label feature works through the direct REST API as well as Gemini Enterprise (needs testing)`.
  - MA9 R9: add `• https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels`.
  - `modelarmor_inventory.md` (a) "Document text extraction and screening of files", cell "Levels or options": append ` Metadata-label detection: Google Drive labels and Microsoft sensitivity labels on DOCX, PDF, PPTX and XLSX; not usable in inspection rule sets or de-identification transformations [Documented] (SDP custom metadata label page).` Source URL cell: add the SDPM URL.
  - No Summary change.

### T67 — XLYM against XLTM
- Verdict: RESOLVED (vendor typo is the likely reading; both spellings are on Google pages)
- Evidence: DI: "XLSX, XLSM, XLTX, XLYM". GO line 783: `// XLSX, XLSM, XLTX, XLYM`. OV: "Microsoft Excel sheets: XLSX, XLSM, XLTX, XLTM". RN 2025-06-08: "XLSX, XLSM, XLTX, XLTM spreadsheets".
- Label to use: spellings `[Documented]` and `[Documented: repo googleapis/google-cloud-go@37f936ac]`; typo judgement `[Inferred]` (premise: the overview and the release note, two Model Armor pages, both say XLTM; the REST text and the generated Go comment come from one source comment).
- Draft impact:
  - `modelarmor_cols_b.md` MA9 R2, keep line 320 and add: `• The pinned Go library repeats "XLSX, XLSM, XLTX, XLYM" in its comment for the Excel byte item type (service.pb.go@37f936ac:783) **[Documented: repo googleapis/google-cloud-go@37f936ac]**` and `• XLYM is probably a typo for XLTM. Premise: the overview and the release note both say XLTM and the REST text and the Go comment appear to share one source comment **[Inferred]**`
  - MA9 R2 Summary: no change.

### T68 — File result details: file label, page or sheet, regional limits for documents
- Verdict: PARTLY RESOLVED
- Evidence: DI: "Optional. Label of the file. This is used to identify the file in the response." RR (SdpContentLocation): "Name of the container where the finding is located. The top level name is the source file name or table name." GO lines 3222 to 3230: `ByteDataItem` at the pinned tag has only `ByteDataType` and `ByteData` (no `FileLabel`). GO lines 3426 to 3428: the container `Location` oneof lists `SdpContentLocation_ImageFindingLocation` as the only assigned type. FAR: no document column (checked).
- Label to use: DI and RR quotes `[Documented]`; Go absence of `FileLabel` `[Documented: repo googleapis/google-cloud-go@37f936ac]`; "`fileLabel` appears as the container name" `[Inferred]`; page or sheet reporting and regional limits for documents `[Not disclosed]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA9 R5, replace bullet line 369 with: `• The finding container name is "The top level name is the source file name or table name" (SanitizationResult reference, read 2026-10-09) **[Documented]**` and `• The file label is probably returned as that container name. Premise: both fields are described as identifying the file; no page names the response field **[Inferred]**` and `• The pinned Go v1 `ByteDataItem` has only `ByteDataType` and `ByteData`, no file label (service.pb.go@37f936ac:3222) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`
  - MA9 R8 last bullet (line 415). After: `• Whether filters report which page or sheet matched (checked the SanitizationResult reference and the Go comments; only a container name and text ranges are described)`
  - MA9 R6 line 392 (regional limits for documents): unchanged (`[Not disclosed]`).

### T70 — Image finding location: boundingBoxes list or boundingBox object
- Verdict: RESOLVED (list, by the REST reference and the pinned Go type; the sanitize-page example is the outlier)
- Evidence: RR: `"boundingBoxes": [ { object (SdpBoundingBox) } ]` with "Bounding boxes locating the pixels within the image containing the finding." GO line 3375 to 3376: "Bounding boxes locating the pixels within the image containing the finding." `BoundingBoxes []*SdpImageFindingLocation_SdpBoundingBox`. SAN redaction example: `"imageFindingLocation": { "boundingBox": { "top": 16, "left": 121, "width": 620, "height": 90 } }`.
- Label to use: REST and example `[Documented]`; Go `[Documented: repo googleapis/google-cloud-go@37f936ac]`; "the example is abbreviated or older" `[Inferred]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA10 R5, keep line 515 and replace line 516 with: `• The pinned Go library types `BoundingBoxes` as a list of boxes with `Top`, `Left`, `Width` and `Height` (service.pb.go@37f936ac:3376) **[Documented: repo googleapis/google-cloud-go@37f936ac]**`, then `• The sanitize page redaction example shows a single `boundingBox` object (top 16, left 121, width 620, height 90) (sanitize page, read 2026-10-09) **[Documented]**`, then `• The example is probably abbreviated or from an older format. Premise: the REST reference and the pinned Go type both give a list **[Inferred]**`
  - MA10 R8 bullet 9 (line 556). After: `• Whether a live redaction response returns `boundingBoxes` as a list as the REST reference and Go library say (one sample shows a single `boundingBox`; needs testing)`
  - `modelarmor_inventory.md` (a) "Image visual scanning", cell "Result field": replace "finding locations carry image bounding boxes" with "finding locations carry image bounding boxes as a list (boundingBoxes) per RR and the Go library, while one SAN example shows a single boundingBox object [Documented] (RR; SAN)".
  - MA10 R9 already has the Go blob URL.

### T71 — include_findings: what it is and where it is set
- Verdict: PARTLY RESOLVED (meaning and origin found; where Model Armor sets it is not stated)
- Evidence:
  - RR (redactResult.findings): "Output only. The findings. This field is populated in the response only when include_findings in the SDP template is set to true." Same text at GO line 3585 to 3586.
  - dlp.googleapis.com discovery document (static GET, `https://dlp.googleapis.com/$discovery/rest?version=v2`): `includeFindings` occurs once, in `GooglePrivacyDlpV2RedactImageRequest`: "Whether the response should include findings along with the redacted image."
  - SDP image redaction guide (https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images): "To enable this functionality, set includeFindings to true in your request to image.redact."
  - Model Armor docs: no setting named `include_findings` or `includeFindings` in RT, TPL, SAN, FLR (searched the page text).
- Label to use: Model Armor quotes `[Documented]` and `[Documented: repo googleapis/google-cloud-go@37f936ac]`; SDP facts `[Documented]` (Google SDP docs and API discovery document); where Model Armor sets it `[Not disclosed]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA10 R5, after line 514 add: `• In the Sensitive Data Protection API, `includeFindings` is a field of the image redact request ("Whether the response should include findings along with the redacted image."), not of an inspect or de-identify template (Sensitive Data Protection API discovery document, read 2026-10-09) **[Documented]**` and `• Where Model Armor sets `include_findings`, and whether a template setting controls it, is not stated (checked the templates reference, templates page, sanitize page and floor settings page) **[Not disclosed]**`
  - MA10 R8 bullet 7 (line 554). After: `• Where include_findings is set when Model Armor calls Sensitive Data Protection (the Model Armor reference says "in the SDP template", but in the Sensitive Data Protection API it is an image redact request field; checked the Model Armor pages, not stated; needs testing)`
  - MA10 R9: add `• https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images`.

### T76 — MODALITY_UNSPECIFIED against an empty modalities field
- Verdict: PARTLY RESOLVED (both statements confirmed; they describe two different inputs; passing the enum value explicitly is not shown)
- Evidence: RT (modalities): "Optional. Specifies the modalities to scan. If empty, only text modality will be scanned." RT (Modality enum): "Unspecified modality. If specified, all modalities will be sanitized." GO line 453 to 454 repeats the enum text. TPL: image modality is Preview, console field disabled outside us and eu.
- Label to use: both `[Documented]` as separate bullets; "listing the unspecified value explicitly is a way to scan all modalities" `[Inferred]`.
- Draft impact:
  - `modelarmor_cols_b.md` MA10 R6, after line 527 add: `• The enum value MODALITY_UNSPECIFIED is described as "Unspecified modality. If specified, all modalities will be sanitized." (templates reference, read 2026-10-09) **[Documented]**` and `• Listing MODALITY_UNSPECIFIED explicitly would scan all modalities, while omitting the field scans text only. Premise: the two REST descriptions; no example shows it **[Inferred]**`. MA9 R6 line 391: same two bullets.
  - `modelarmor_inventory.md` (c) "modalities" already states both (Values and Default cells): append to "Values": ` (listed explicitly; omitting the field scans text only) [Inferred]` after "MODALITY_UNSPECIFIED sanitizes all modalities [Documented] (RT)" only if the merger wants the premise; otherwise none.

### T77 — Block (d) lists 18 locations; the feature table has 20 rows
- Verdict: RESOLVED (values for the two extra rows read from the feature table; descriptions and jurisdiction are not stated anywhere)
- Evidence:
  - FAR supported-features table, 20 rows. Row `us-east7`: filters Responsible AI, Sensitive Data Protection, Prompt injection and jailbreak, Malicious URL; Multi-language Yes; CSAM Yes; Image No; Antivirus Yes. Row `global`: same filters; Multi-language Yes; CSAM Yes; Image Yes; Antivirus Yes.
  - LOC lists 16 regions and the multi-regions eu and us; neither `us-east7` nor `global`. DR jurisdiction table: 18 rows, neither location. FV and VH timelines list neither.
  - DR: "The global Model Armor endpoint doesn't support managing Model Armor templates or sanitizing prompts and responses." OV: "Image screening is supported only in the us and eu multi-regions."
- Label to use: row values `[Documented]` (FAR); description, jurisdiction, support level, residency states and filter versions `[Not disclosed]` (checked LOC, DR, FAR, FV, VH); the `global` conflicts (FAR Image Yes and template rows against DR and OV) as two labelled facts.
- Draft impact (`modelarmor_inventory.md` block (d)):
  - Intro paragraph, replace the last sentence ("FAR also lists rows for us-east7 and global that LOC and DR do not list [Documented] (FAR); they are not given a row here.") with: `FAR also lists rows for us-east7 and global that LOC, DR and FV do not list [Documented] (FAR); they are given rows here with the FAR values only, and every other cell is [Not disclosed] (checked LOC, DR, FAR, FV, VH). DR says the global endpoint cannot manage templates or sanitize [Documented] (DR), and OV says image screening is supported only in the us and eu multi-regions [Documented] (OV), so FAR listing global with Image Yes conflicts with both; whether either location accepts a template is [Not disclosed] (checked LOC, DR, FAR).` Also change "16 regions and the us and eu multi-regions, as on LOC" to "16 regions and the us and eu multi-regions as on LOC, plus two FAR-only rows".
  - Add after the `europe-west9`/`eu` rows (any position; the table is not sorted by name):
    - `| us-east7 [Documented] (FAR) | [Not disclosed] (checked LOC, DR and FAR; no description) | [Not disclosed] (checked DR and FAR) | [Not disclosed] (checked the full-support and limited-support lists in DR and FAR) | [Not disclosed] (checked DR and FAR; no residency row) | Responsible AI, Sensitive Data Protection, Prompt injection and jailbreak, Malicious URL [Documented] (FAR) | Yes [Documented] (FAR) | Yes [Documented] (FAR) | No [Documented] (FAR) | Yes [Documented] (FAR) | [Not disclosed] (checked FV and VH; neither lists this location) | https://docs.cloud.google.com/model-armor/feature-availability-by-region ; https://docs.cloud.google.com/model-armor/locations ; https://docs.cloud.google.com/model-armor/data-residency ; https://docs.cloud.google.com/model-armor/set-filter-version |`
    - `| global [Documented] (FAR) | [Not disclosed] (checked LOC, DR and FAR; no description). DR says the global endpoint is supported only for managing floor settings and does not manage templates or sanitize [Documented] (DR) | [Not disclosed] (checked DR and FAR) | [Not disclosed] (checked the full-support and limited-support lists in DR and FAR) | [Not disclosed] (checked DR and FAR; no residency row) | Responsible AI, Sensitive Data Protection, Prompt injection and jailbreak, Malicious URL [Documented] (FAR) | Yes [Documented] (FAR) | Yes [Documented] (FAR) | Yes [Documented] (FAR). OV says image screening is supported only in the us and eu multi-regions [Documented] (OV) | Yes [Documented] (FAR) | [Not disclosed] (checked FV and VH; neither lists this location) | https://docs.cloud.google.com/model-armor/feature-availability-by-region ; https://docs.cloud.google.com/model-armor/locations ; https://docs.cloud.google.com/model-armor/data-residency ; https://docs.cloud.google.com/model-armor/overview ; https://docs.cloud.google.com/model-armor/set-filter-version |`
  - Row count of block (d): 20. P8 config BLOCKS: (a) 10, (b) 15, (c) 16, (d) 20, (e) 16 (see T83).
  - `modelarmor_cols_a.md` MA7 R6 lines 764 and 766, MA8 R6 lines 918 and 920: unchanged. MA7 R8 line 789 and MA8 R8 line 946: after: `• Whether us-east7 and global in the feature availability table are locations where a template can be created (the locations page lists 16 regions and 2 multi-regions; the data residency page says the global endpoint cannot manage templates; checked both, not stated)`.

### T78 — Release-note entry on Workspace data
- Verdict: CORRECTION (the entry is dated October 09, 2026 on the live page; the drafts carry October 10, 2026)
- Evidence: RN, re-fetched twice on 2026-10-09 (system time 05:29 UTC): heading "October 09, 2026" then "Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data." and "This capability is available on multi-region endpoints in the US (us) and EU (eu) for templates and floor setting configured with filter version v3 or later, including the Stable and Latest aliases." The drafter's local copy (`scratchpad/drafter/ma_pages/release-notes.txt`) read "October 10, 2026". The page footer still reads "Last updated 2026-10-07 UTC".
- Label to use: `[Documented]`. What the capability changes for ordinary prompts is not stated `[Not disclosed]` (the note scopes it to "Workspace content, such as emails, documents, and files").
- Draft impact:
  - `modelarmor_cols_a.md` MA3 R2 line 352 and MA4 R2 line 520. After: `• Release note dated 2026-10-09: "Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data", on the us and eu multi-regions with filter version v3 or later (release notes, read 2026-10-09) **[Documented]**`
  - Add `• What the Workspace data enhancement changes for ordinary prompts is not stated; the note scopes it to emails, documents and files from Workspace (checked the release note) **[Not disclosed]**` and delete the R8 bullet at line 469 (MA3) and the matching MA4 R8 bullet, or keep it as "needs testing".
  - `modelarmor_inventory.md` Reviewer note 2 and `modelarmor_cols_a.md` Reviewer note 11 (line 990): record in `modelarmor_changes.md` that the date reads 2026-10-09 on the live page and the conflict C28 is closed. No fact in INV used the entry.

### T79 — logSanitizeOperations: full content or snippets
- Verdict: RESOLVED (three Google statements, none reconciled; carry them as separate bullets)
- Evidence: LOG: "log_sanitize_operations: A boolean value that lets you log the full content of user prompts and model responses during sanitize operations." LOG: "Enabling logging in a template writes raw prompts and responses to Logging." OV: "event details—which might include metadata or snippets of the analyzed content as configured—are sent to your designated Cloud Logging destination." RT: "logSanitizeOperations ... Optional. If true, log sanitize operations."
- Label to use: each `[Documented]`; the two differ in strength of wording.
- Draft impact:
  - `modelarmor_cols_a.md` R4 data-handling bullet in MA1 (line 67), MA2 (line 232), MA3 (line 401), MA4 (line 573), MA7 (line 732), MA8 (line 885): replace the one bullet with three:
    - `• Model Armor "operates as a stateless service, processing all prompts and model responses entirely in memory" (overview, 2026-10-09) **[Documented]**`
    - `• The logging page says `log_sanitize_operations` lets you "log the full content of user prompts and model responses during sanitize operations" (logging page, 2026-10-09) **[Documented]**`
    - `• The overview says that with Cloud Logging enabled, event details "might include metadata or snippets of the analyzed content as configured" (overview, 2026-10-09) **[Documented]**`
  - `modelarmor_cols_b.md` MA5 R4 line 65 and MA6 R4 line 217: keep the logging-page bullet and add the overview bullet above.
  - `modelarmor_inventory.md` (c) logSanitizeOperations already holds both sides: add to "Effect" the RT wording `RT only says 'If true, log sanitize operations.' [Documented] (RT)`.

### T80 — Docs page "Last updated" dates
- Verdict: CORRECTION (the inventory intro's blanket statement is wrong for the REST and library pages)
- Evidence (raw page footers, read 2026-10-09): "Last updated 2026-10-06 UTC" on OV, TPL, SAN, FLR, QUO, FAR, DR, LOC, FV, VH, EXC, best practices, INT, GE, APG, AGW, VTX, LC, LOG, MON, retry strategy, networking and MCP pages; "Last updated 2026-10-07 UTC" on RN, the two Apigee policy pages, SDPI and SDPM; "Last updated 2026-10-05 UTC" on LIB; "Last updated 2026-09-24 UTC" on RR; "Last updated 2026-09-07 UTC" on RT and DI; "Last updated 2026-08-19 UTC" on the sanitizeUserPrompt and sanitizeModelResponse method pages. The RN page lists an entry dated October 09, 2026 while its footer says 2026-10-07.
- Label to use: `[Documented]`.
- Draft impact:
  - `modelarmor_inventory.md` intro paragraph (line 3). Before: "every docs page footer reads 'Last updated 2026-10-06 UTC' except the release notes page ('Last updated 2026-10-07 UTC'); the product page and the pricing page carry no last-updated line." After: `page footers read 'Last updated 2026-10-06 UTC' for OV, TPL, SAN, FLR, QUO, FAR, DR, LOC, FV, VH, EXC, BP, INT, GE, APG, AGW, VTX, LC, LOG, MON, RTY, NET and MCPD; 'Last updated 2026-10-07 UTC' for RN, APU and APR; 'Last updated 2026-10-05 UTC' for LIB; 'Last updated 2026-09-24 UTC' for RR; 'Last updated 2026-09-07 UTC' for RT and the DataItem reference; and 'Last updated 2026-08-19 UTC' for the two sanitize method pages; the product page and the pricing page carry no last-updated line, and the RN footer lags its newest entry, dated October 09, 2026. The read date 2026-10-09 is the pin for every docs fact.`
  - `modelarmor_brief.md` (not a final source) carries the same blanket claim: record in `modelarmor_changes.md`.

### T81 — Security Command Center findings
- Verdict: RESOLVED (documented difference between pages; carry as separate facts)
- Evidence: INT: "When Model Armor detects a violation of a configured floor setting, it blocks the prompt or response and sends a finding to Security Command Center." SCCF (Model Armor findings): "Floor settings violation Category name in the API: FLOOR_SETTINGS_VIOLATION" with "A floor setting violation that occurs when a Model Armor template fails to meet the minimum security standards defined by the resource hierarchy floor settings." and "Finding class: Misconfiguration", "Pricing tier: Premium". AGW: "These findings are also surfaced in Security Command Center." (violations logged through Agent Gateway). The INT link target is `/security-command-center/docs/concepts-vulnerabilities-findings#model-armor-findings`.
- Label to use: each `[Documented]` (SCCF is Security Command Center docs, not Model Armor docs); "the INT sentence describes runtime violations while SCCF lists only a template-conformance finding" `[Inferred]`.
- Draft impact:
  - `modelarmor_inventory.md` (b) "Security Command Center findings from Model Armor", cell "Limitations": append ` AGW says violations detected through Agent Gateway are 'also surfaced in Security Command Center' [Documented] (AGW). SCCF lists no per-prompt finding type [Documented] (SCCF), so the INT and AGW sentences describe more than SCCF lists [Inferred] (premise: SCCF table is the finding catalogue).` Source URL: add `https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration`. Reviewer note 1.9 moves to `modelarmor_changes.md`.

### T82 — Pricing wording
- Verdict: RESOLVED (INV(e) matches the pricing page; the scope of the standalone allowance is not stated)
- Evidence: PRC: "Model Armor uses the same token definition as Gemini Enterprise Agent Platform: four characters (using UTF-8 code points) per token excluding white space." OV and QUO: "A token is equivalent to about 4 characters." PRC standalone: "there is no cost for using Model Armor up to 2 million tokens per month." PRC table: Enterprise subscription 3 billion tokens per month, Premium subscription 3 billion, Premium activated at an organization level 2 million, Premium activated at a project level 2 million, each at $0.10 per additional million tokens. PRC: "When Sensitive Data Protection is enabled within Model Armor, there are no additional charges to use it." OV: "You aren't charged for data that is skipped." PRC has no last-updated line.
- Label to use: price and allowance facts `[Documented]`; scope of the standalone allowance (project, organisation or billing account) `[Not disclosed]` (checked PRC, OV, QUO); the two token definitions as two bullets `[Documented]`.
- Draft impact:
  - `modelarmor_inventory.md` (e) "Standalone price", cell "Applies to": append ` Whether the 2 million token allowance is per project, organisation or billing account [Not disclosed] (checked PRC, OV, QUO).` The SCC-tier row already matches PRC row for row: no change. The "Token definition" row already has both statements.
  - `modelarmor_cols_a.md` R4 pricing bullet in MA1 (line 66), MA2 (231), MA3 (400), MA4 (572), MA7 (731), MA8 (884): split the combined bullet in two (one fact per bullet): `• Standalone use has "no cost for using Model Armor up to 2 million tokens per month" and then "$0.10 per million tokens" (pricing page, 2026-10-09) **[Documented]**` and `• "Security Command Center includes Model Armor with a predefined number of tokens per month at no additional cost" (pricing page, 2026-10-09) **[Documented]**`, then add `• Whether the standalone allowance applies per project, organisation or billing account is not stated (checked the pricing page, overview and quotas page) **[Not disclosed]**`.
  - R7 Summaries ("Standalone use is free to 2 million tokens a month") stay accurate: no Summary change.

### T83 — Inventory row counts and P8 config
- Verdict: RESOLVED (bookkeeping, counts verified by parsing the draft)
- Evidence: parsed `modelarmor_inventory.md` on 2026-10-09: (a) 10, (b) 15, (c) 16, (d) 18, (e) 16 data rows. No `build_modelarmor_inventory.py` and no `modelarmor` entry in `benchtest/products.py` exist yet.
- Label to use: not applicable (no source fact).
- Draft impact: after T77 the block counts are 10, 15, 16, 20, 16. The xlsx-writer config module needs BLOCKS `(a) 10`, `(b) 15`, `(c) 16`, `(d) 20`, `(e) 16` and the `markers` tuple with the legacy, planned and inventory-only markers (R011). The brief target of 12 rows for block (b) is not binding (queue ruling). No change to draft text.

### T84 — Naming drift for Vertex AI and Gemini Enterprise
- Verdict: RESOLVED
- Evidence: VTX title: "Integrate Model Armor with Gemini Enterprise Agent Platform". VTX: "Model Armor provides prompt and response protection within Gemini API in Vertex AI for the generateContent method." VTX gcloud: `--add-integrated-services=VERTEX_AI`, `--vertex-ai-enforcement-type=INSPECT_AND_BLOCK`. INT options table lists "Gemini Enterprise" and "Gemini Enterprise Agent Platform" as two separate rows; INT text mentions "Gemini Enterprise, Agent Runtime, and Apigee". FLR: "Gemini Enterprise, and Agent Runtime."
- Label to use: `[Documented]`.
- Draft impact: at the first bullet in each column that names the route (cols_a R3 or R4 of MA1 to MA4, MA7, MA8; cols_b MA5 R4, MA6 R4, MA9 R3, MA10 R4), write the full name once and use "Agent Platform" afterwards. Drop-in bullet for the first mention: `• Naming: the docs call the Vertex AI route "Gemini Enterprise Agent Platform"; they still say "Gemini API in Vertex AI" for the generateContent method and use VERTEX_AI in gcloud flags, and list "Gemini Enterprise" as a separate integration (integrations page, Agent Platform integration page, 2026-10-09) **[Documented]**`. `modelarmor_inventory.md` intro "Naming" sentence already says this; no change.

### T85 — Pre-GA Offerings Terms for Preview features
- Verdict: RESOLVED (terms read; reliance on Preview features is decided by R017 item 5 with the Preview label and date read)
- Evidence:
  - GST, Pre-GA Offerings Terms (last modified October 08, 2026): "PRE-GA OFFERINGS ARE PROVIDED “AS IS” WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND." and "(i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity."
  - GST: "no data processing terms (including the Cloud Data Processing Addendum) apply to Pre-GA Offerings and Customer should not use Pre-GA Offerings to process personal data or other data subject to legal or regulatory compliance requirements." and "the Data Location Section above will not apply to Pre-GA Offerings", each "Except as otherwise expressly indicated in a written notice or Google documentation".
  - GST: use of "a Pre-GA Offering component (such as a feature or model) included in a generally available Service or Software does not negate unrelated commitments that Google makes for its Services and Software."
  - LST: "Unless stated otherwise by Google, Preview offerings are intended for use in test environments only."
  - TSV lists "Model Armor" as a Service under Security and Identity. Preview banner "subject to the "Pre-GA Offerings Terms"" on OV (image screening), EXC (exclusion rules) and LC (LangChain); RN labels image screening 2026-06-25, console modality selection 2026-07-01, exclusion rules 2026-09-28.
- Label to use: clauses `[Documented]`; "only the Preview components of Model Armor are Pre-GA Offerings" `[Inferred]` (premise: Model Armor is a listed Service and the terms treat a Pre-GA component of a GA Service separately).
- Draft impact:
  - `modelarmor_cols_b.md` MA10 R1 line 448 stays; add to MA10 R4 (after line 504) and MA10 R7 (after line 543):
    - `• Preview features are Pre-GA Offerings: "PRE-GA OFFERINGS ARE PROVIDED “AS IS” WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND." (Google Cloud General Service Terms, Pre-GA Offerings Terms, read 2026-10-09) **[Documented]**`
    - `• Unless Google's documentation says otherwise, "no data processing terms (including the Cloud Data Processing Addendum) apply to Pre-GA Offerings and Customer should not use Pre-GA Offerings to process personal data or other data subject to legal or regulatory compliance requirements" (Google Cloud General Service Terms, read 2026-10-09) **[Documented]**`
    - `• Google's launch-stage description says "Unless stated otherwise by Google, Preview offerings are intended for use in test environments only." (Google Cloud products page, read 2026-10-09) **[Documented]**`
    - R7 only: `• Image tests should use synthetic images only, because the Pre-GA terms advise against processing personal data in Pre-GA Offerings **[Inferred]**`
  - `modelarmor_cols_a.md` MA3 R5 and MA4 R5 exclusion-rule bullets: append the same first bullet (Preview, Pre-GA terms) once per column; MA3 line ~92 and MA4 R5 equivalents already say "(Preview)".
  - `modelarmor_inventory.md` intro: add `GST = https://cloud.google.com/terms/service-terms` to the short-name list and the sentence `Preview features are Pre-GA Offerings under the General Service Terms: provided 'as is', not covered by any SLA, with no data processing terms applying unless Google's documentation says otherwise [Documented] (GST; read 2026-10-09).` Status cells for image OCR, visual scanning, modalities and exclusion rules already say Preview; add ` Pre-GA Offerings Terms apply [Documented] (GST)` to the (a) OCR and visual scanning rows and the (c) modalities and filterRuleSettings rows. (b) LangChain row: same. Source URL cells of those rows: add `https://cloud.google.com/terms/service-terms`.
  - R9 of MA10 (and MA3, MA4 if their R5 bullet is added): add `• https://cloud.google.com/terms/service-terms` and `• https://cloud.google.com/products`.

### T86 — Terms for live testing
- Verdict: PARTLY RESOLVED (terms located and quoted; whether detection benchmarking is permitted under the Acceptable Use Policy is a legal reading that needs the user)
- Evidence:
  - AUP (last modified June 23, 2026): "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement". Also: "to engage in, promote, or encourage illegal activity, including child sexual exploitation, child abuse, or terrorism or violence that can cause death, serious harm, or injury to individuals or groups of individuals".
  - GST (Data Location): "Google will store Customer Data for that Service at rest only within the selected Region or Multi-Region" and "The Services do not limit the locations from which Customer or Customer End Users may access Customer Data or to which they may move Customer Data."
  - TDR lists "Model Armor" among Services that may be configured for data location. TSV lists "Model Armor" under Security and Identity, not among the named Generative AI Services.
  - DR and RN 2026-08-27: disabling data residency enforcement "allows cross-jurisdictional routing". LOG: "Enabling logging in a template writes raw prompts and responses to Logging."
  - APG: "Verify that billing is enabled for your Google Cloud project."
- Label to use: clauses `[Documented]`; "sending jailbreak and injection prompts to measure detection may fall under the AUP testing clause" `[Inferred]` (premise: the clause covers testing Services to find limitations or evade filtering; the AUP does not define a benchmark exception); "the Agreement expressly permits it" `[Not disclosed]` (checked AUP and GST).
- Draft impact:
  - `modelarmor_cols_a.md` R7 of MA1 (line 120 area), MA3, MA4, MA7, MA8 and `modelarmor_cols_b.md` MA10 R7: add `• Google's Acceptable Use Policy bars using the Services "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement" (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**`, `• Whether sending jailbreak, injection or harmful-content prompts to measure detection rates is "expressly permitted" is not stated (checked the Acceptable Use Policy and the General Service Terms) **[Not disclosed]**`. MA1 R7 (CSAM caution): add `• The Acceptable Use Policy lists "child sexual exploitation, child abuse" among illegal activity (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**`.
  - `modelarmor_cols_b.md` MA10 R7 Singapore bullet (line 542): keep, and add `• The General Service Terms commit to storing Customer Data at rest only in the selected region or multi-region and "do not limit the locations from which Customer or Customer End Users may access Customer Data" (Google Cloud General Service Terms, read 2026-10-09) **[Documented]**` so the cross-jurisdiction point has a source.
  - R8 additions: MA1 R8, MA7 R8, MA8 R8, MA10 R8: `• Whether the Acceptable Use Policy testing clause covers detection benchmarks (checked the Acceptable Use Policy and General Service Terms, not stated; needs the project owner's reading)`.
  - R9 of those columns: add `• https://cloud.google.com/terms/aup` and `• https://cloud.google.com/terms/service-terms`.

### T87 — Licences of google-cloud-go and apigee-samples
- Verdict: RESOLVED
- Evidence:
  - googleapis/google-cloud-go@37f936ac: root `LICENSE` begins "Apache License Version 2.0, January 2004"; `modelarmor/apiv1/version.go` header: "Licensed under the Apache License, Version 2.0 (the "License");". Module path: `cloud.google.com/go/modelarmor` (`modelarmor/go.mod` line 1).
  - GoogleCloudPlatform/apigee-samples@2b1a9f00: the README License section states that all solutions in the repository are provided under the Apache 2.0 license (link text, not a single quotable line) and `LICENSE.txt` begins "Apache License Version 2.0, January 2004". The `llm-security-v2` folder has no separate licence file.
  - Docs pages: footer "the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License."
- Label to use: `[Documented: repo googleapis/google-cloud-go@37f936ac]` and `[Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00]`; docs footer `[Documented]`.
- Draft impact (`modelarmor_inventory.md` block (b)):
  - "Client libraries ..." row, cell "Limitations": append ` Licence: Apache License 2.0 for the Go module cloud.google.com/go/modelarmor [Documented: repo googleapis/google-cloud-go@37f936ac] (LICENSE; modelarmor/apiv1/version.go header). Docs code samples are Apache 2.0 and docs text is CC BY 4.0 [Documented] (page footers).` Source URL cell: add `https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/LICENSE`.
  - "Apigee API proxies ..." row, cell "Limitations": append ` Samples licence: Apache 2.0 [Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00] (README License section; LICENSE.txt).` Source URL cell: add `https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/LICENSE.txt`.
  - `modelarmor_cols_*`: no change (library licences are not a column fact).

---

## Cross-range note (T41, owned by modelarmor_resolutions_1.md)

The assignment named T41 as a priority; it lies in the other resolver's range, so no `### T41` entry is written here. Evidence gathered for it while resolving T44 and T55, for whoever merges: OV lists six basic categories (credit card number, US SSN, financial account number, US ITIN, Google Cloud credentials, Google Cloud API key); RT says "Basic Sensitive Data Protection configuration inspects the content for sensitive data using a fixed set of six info-types" and the pinned Go comment at service.pb.go@37f936ac:2160 repeats "a fixed set of six info-types"; SAN lists five infoTypes "for all regions" (CREDIT_CARD_NUMBER, FINANCIAL_ACCOUNT_NUMBER, GCP_CREDENTIALS, GCP_API_KEY, PASSWORD) plus two "for US-based regions" (US_SOCIAL_SECURITY_NUMBER, US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER). Three sources say six, one says seven (PASSWORD is the extra item); no release note (searched RN for PASSWORD and basic) says when PASSWORD was added. The conflict stands as two labelled bullets.

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T44 | PARTLY RESOLVED | Documented (advanced on responses); Not disclosed (basic on responses); Inferred (same list) | Yes: MA6 R2 |
| T45 | PARTLY RESOLVED | Documented (field named in prose); Not disclosed (no example) | Yes: MA6 R3 |
| T47 | RESOLVED | Documented: repo googleapis/google-cloud-go@37f936ac; Inferred (array examples stale) | No |
| T49 | STILL OPEN | Not disclosed | No |
| T50 | PARTLY RESOLVED | Documented (type identity); Inferred (advanced accepted); Not disclosed (location rule) | No |
| T52 | CORRECTION | Documented; Inferred (partial screening) | Yes: MA5 R6, MA6 R6 |
| T53 | PARTLY RESOLVED | Documented (Gemini Enterprise exempt, Apigee limited); Not disclosed (other routes) | No |
| T54 | RESOLVED | Documented | No |
| T55 | CORRECTION | Documented (built-in infoType); Inferred (route via advanced template) | No |
| T56 | RESOLVED | Documented (links); Inferred (scope sentence) | No |
| T57 | PARTLY RESOLVED | Documented (result type, region table, release note); Not disclosed (setting); Inferred (scope) | No |
| T58 | STILL OPEN | Documented (three statements); Not disclosed (no reconciliation) | No |
| T60 | STILL OPEN | Documented (two lists); Not disclosed (no reconciliation) | No |
| T61 | STILL OPEN | unchanged (ruling R017 item 3 settles the split) | No |
| T63 | STILL OPEN | Not disclosed | No |
| T66 | PARTLY RESOLVED | Documented (SDP page, release note); Not disclosed (no request field) | No |
| T67 | RESOLVED | Documented; Documented: repo googleapis/google-cloud-go@37f936ac; Inferred (typo) | No |
| T68 | PARTLY RESOLVED | Documented; Documented: repo googleapis/google-cloud-go@37f936ac; Inferred (label to container); Not disclosed (page or sheet) | No |
| T70 | RESOLVED | Documented: repo googleapis/google-cloud-go@37f936ac; Inferred (example stale) | No |
| T71 | PARTLY RESOLVED | Documented (SDP field origin); Not disclosed (where Model Armor sets it) | No |
| T76 | PARTLY RESOLVED | Documented (two statements); Inferred (explicit value scans all) | No |
| T77 | RESOLVED | Documented (FAR values); Not disclosed (all other cells) | No |
| T78 | CORRECTION | Documented; Not disclosed (effect on ordinary prompts) | No |
| T79 | RESOLVED | Documented (three statements) | No |
| T80 | CORRECTION | Documented | No |
| T81 | RESOLVED | Documented (two pages); Inferred (reading of difference) | No |
| T82 | RESOLVED | Documented; Not disclosed (allowance scope) | No |
| T83 | RESOLVED | n/a (bookkeeping) | No |
| T84 | RESOLVED | Documented | No |
| T85 | RESOLVED | Documented (terms); Inferred (only Preview components are Pre-GA) | No |
| T86 | PARTLY RESOLVED | Documented (clauses); Inferred (relevance); Not disclosed (express permission) | No |
| T87 | RESOLVED | Documented: repo googleapis/google-cloud-go@37f936ac; Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00; Documented | No |

## Report

1. Counts per verdict (32 entries): RESOLVED 13 (T47, T54, T56, T67, T70, T77, T79, T81, T82, T83, T84, T85, T87), PARTLY RESOLVED 10 (T44, T45, T50, T53, T57, T66, T68, T71, T76, T86), STILL OPEN 5 (T49, T58, T60, T61, T63), CORRECTION 4 (T52, T55, T78, T80).
2. CORRECTION items: T52 (R6 Summaries of MA5 and MA6 and several bullets say "skipped" although a match is still returned over the limit), T55 (R7 of MA5 and MA6 say a custom detector is needed for Singapore NRIC; a built-in infoType exists), T78 (the release-note entry reads October 09, 2026, not October 10, 2026), T80 (the inventory intro's blanket page-date statement is wrong for the REST, library, Apigee and SDP pages).
3. Summaries that must change: `modelarmor_cols_b.md` MA5 R6 (line 90), MA6 R6 (line 237), MA6 R2 (line 168, label to Not disclosed), MA6 R3 (line 181, label to Not disclosed). New text is in T52, T44 and T45.
4. Still open after this pass (class b or unreconcilable docs): T49, T58, T60, T61, T63, plus the b items not touched.
