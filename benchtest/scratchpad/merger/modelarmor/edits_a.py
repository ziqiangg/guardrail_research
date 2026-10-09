"""Column edits for MA1-MA4, MA7, MA8 (cols_a). Text is from the resolutions unless a comment says otherwise."""
from lib import rep, edit, ins_after, ins_before, dele, setsum, editsum, r9add, r9sum

D = " **[Documented]**"
I = " **[Inferred]**"
ND = " **[Not disclosed]**"
TBV = " **[To be verified]**"
GO = " **[Documented: repo googleapis/google-cloud-go@modelarmor/v1.3.0]**"
JV = " **[Documented: repo googleapis/google-cloud-java@v1.93.0]**"

A6 = ["MA1", "MA2", "MA3", "MA4", "MA7", "MA8"]
URL_GO_B = "https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/apiv1beta/modelarmorpb/service.pb.go"
URL_JAVA = "https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto"
URL_APG_RN = "https://docs.cloud.google.com/apigee/docs/release-notes"
URL_SMR = "https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse"
URL_BLOG = "https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps"
URL_GST = "https://cloud.google.com/terms/service-terms"
URL_AUP = "https://cloud.google.com/terms/aup"


def apply(C):
    # ------------------------------------------------------------------ shared R3 / R4 edits (six columns)
    naming = ('• Naming: the docs call the Vertex AI route "Gemini Enterprise Agent Platform" (short form Agent Platform below); '
              'they still say "Gemini API in Vertex AI" for the generateContent method and use VERTEX_AI in gcloud flags, and list '
              '"Gemini Enterprise" as a separate integration (integrations page, Agent Platform integration page, 2026-10-09)' + D)
    for c in A6:
        ins_before(C, c, 3, "• Routes ", naming, "T84 naming bullet (full name once per column)")

        rep(C, c, 4, "Pricing: standalone use has", [
            '• Pricing: standalone use has "no cost for using Model Armor up to 2 million tokens per month" and then "$0.10 per million tokens" (pricing page, 2026-10-09)' + D,
            '• Pricing: "Security Command Center includes Model Armor with a predefined number of tokens per month at no additional cost" (pricing page, 2026-10-09)' + D,
            '• Whether the standalone allowance applies per project, organisation or billing account is not stated (checked the pricing page, overview and quotas page)' + ND,
        ], "T82 + hygiene (one fact per bullet)")

        rep(C, c, 4, "Data handling: Model Armor", [
            '• Data handling: Model Armor "operates as a stateless service, processing all prompts and model responses entirely in memory"; content is stored only if Cloud Logging is enabled (overview, 2026-10-09)' + D,
            '• The logging page says `log_sanitize_operations` lets you "log the full content of user prompts and model responses during sanitize operations" (logging page, 2026-10-09)' + D,
            '• The overview says that with Cloud Logging enabled, event details "might include metadata or snippets of the analyzed content as configured" (overview, 2026-10-09)' + D,
        ], "T79 + hygiene (one fact per bullet)")

        rep(C, c, 4, "Client libraries exist for C#",
            '• Client libraries exist for C#, Go, Java, Node.js, PHP and Python; the page shows Java 0.40.0 in its sbt line and a pre-release C# package (`--version 1.0.0-beta05`) (client libraries page, 2026-10-09)' + D,
            "T25 (main ruling: versions of the other libraries in the inventory only; one short R4 bullet)")

        rep(C, c, 4, "Release status of routes:", [
            '• Release status of routes (release notes unless stated, 2026-10-09)' + D,
            '  – Agent Platform: GA (release note 2025-12-03)',
            '  – Agent Gateway: GA (release note 2026-06-24)',
            '  – Gemini Enterprise: GA (release note 2025-09-16)',
            '  – Google and Google Cloud MCP servers: GA (release note 2026-04-22)',
            '  – GKE integration: GA (release note 2025-09-15)',
            '  – Streaming sanitization: GA (release note 2026-07-10)',
            '  – LangChain: Preview (LangChain page)',
            '• The floor settings page still labels the Google Cloud MCP servers integration "(Preview)" (floor settings page, 2026-10-09); the dated release note 2026-04-22 says General Availability and is preferred, because the page label is undated' + D,
        ], "hygiene (one bullet, seven facts -> parent with sub-bullets) + T22 (MCP pair)")

        rep(C, c, 4, "Apigee policies `SanitizeUserPrompt`", [
            '• Apigee policies `SanitizeUserPrompt` and `SanitizeModelResponse`: Public Preview on 2025-05-22 and Generally Available on 2025-09-04 on Apigee X (Apigee release notes, Apigee docs not Model Armor docs, 2026-10-09)' + D,
            '• Service Extensions on application load balancers: Preview in release note 2025-04-09; the GKE Inference Gateway integration is Generally Available from release note 2025-09-15 (release notes, 2026-10-09)' + D,
            '• A GA date for other load balancers and for Secure Web Proxy (checked the release notes, the networking page and the integrations page; the Service Extensions configuration page returned no text through the raw fetch, so it is unread)' + TBV,
        ], "T20 + T21 (T21 label To be verified per main: summarising fetch cannot carry a label)")

        r9add(C, c, URL_APG_RN, "T20 (Apigee release notes)")

    # ------------------------------------------------------------------ R7 first bullet: no full stop before the label
    for c in A6:
        det = C[c]["rows"][7]["detail"]
        assert det[0].startswith("• **Minimum setup:**") and det[0].endswith(". **[Inferred]**"), c
        edit(C, c, 7, "**Minimum setup:**", ". **[Inferred]**", " **[Inferred]**", "style 10 (no full stop before the label)")

    # ------------------------------------------------------------------ MA1 -----------------------------------------------------
    setsum(C, "MA1", 1,
           "**Input-level responsible AI safety filtering.** Model Armor screens a user prompt for hate speech, harassment, sexually explicit and dangerous content at a per-category confidence level. A CSAM check is on by default but unavailable in limited-support locations with residency enforced. The caller enforces any block. **[Documented]**",
           "T9 (CSAM caveat in Summary)")
    csam_bullets = lambda: [
        '• Overview: the CSAM filter "is applied by default and cannot be turned off" (overview, 2026-10-09)' + D,
        '• Feature table for templates with data residency enforcement enabled: CSAM support is "No" in asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2 and northamerica-northeast2, and "Yes" in the full-support locations (feature availability page, 2026-10-09)' + D,
        '• Disabling data residency enforcement "allows cross-jurisdictional routing to enable Model Armor features that are otherwise unavailable in limited-support regions"; floor-setting configurations have all features available (release note 2026-08-27, feature availability page, 2026-10-09)' + D,
        '• CSAM detection is therefore expected to run in a limited-support location when enforcement is off; the pages do not name CSAM in that sentence' + I,
    ]
    for c in ("MA1", "MA2"):
        rep(C, c, 2, "Docs state the CSAM filter", csam_bullets(), "T9 + hygiene (two sources on opposite sides -> separate bullets)")
    for c in ("MA1", "MA2", "MA3", "MA4"):
        ins_after(C, c, 2, "In asia-south1 and northamerica-northeast2", [
            '• The feature table shows multi-language detection as "No" in all seven limited-support locations when data residency is enforced, while the Skipped Detection note names only asia-south1 and northamerica-northeast2 (feature availability page, sanitize page, 2026-10-09)' + D,
            '• What a non-English prompt returns in the other five limited-support locations, including asia-southeast1 (checked the sanitize, feature availability, data residency and release notes pages)' + ND,
        ], "T33")
    for c in ("MA1", "MA2"):
        ins_after(C, c, 2, "Topic enforcement configuration:", [
            '• The overview and the blog place "topicality" inside the sensitive data protection filter ("sensitive data protection (including topicality)") (overview, Google Cloud blog, 2026-10-09)' + D,
            '• Topic rules are probably custom detectors in a Sensitive Data Protection template; the premise is the "including topicality" phrase and the absence of any topic setting' + I,
        ], "T35")

    def ocr_pair(filter_name, extra=""):
        return [
            '• The REST modality reference says the text content of an image is sanitized "depending on the filter configuration" (REST templates ref, 2026-10-09)' + D,
            f'• Whether the {filter_name} filter examines text read out of images by OCR is not stated (checked the overview image section, the sanitize page image examples, which show only `csam` and `sdp` results, the templates page, the REST references and release notes 2026-06-25 and 2026-07-01)' + ND,
        ]
    rep(C, "MA1", 3, "Whether the responsible AI filter is applied to text read out of images", ocr_pair("responsible AI"), "T11 (one treatment in all columns)")
    rep(C, "MA3", 3, "Whether the filter runs on text read out of images by OCR", ocr_pair("prompt injection and jailbreak"), "T11")
    rep(C, "MA7", 2, "Whether URLs inside images are extracted by OCR", ocr_pair("malicious URL"), "T11")
    rep(C, "MA8", 2, "Whether URLs inside generated images are extracted", [
        ocr_pair("malicious URL")[0],
        '• Whether the malicious URL filter extracts and checks URLs inside generated images is not stated (checked the overview image section, the sanitize page image examples, which show only `csam` and `sdp` results, the templates page, the REST references and release notes 2026-06-25 and 2026-07-01)' + ND,
    ], "T11")

    # MA1 / MA2 R5
    for c in ("MA1", "MA2"):
        ins_after(C, c, 5, "Default level, REST:",
                  '• Default level, floor settings console: "If you don\'t specify a confidence level, it defaults to Medium and above." (floor settings page, console steps, 2026-10-09)' + D,
                  "T2")
        rep(C, c, 5, "The two default statements differ",
            '• The three default statements differ (High on the templates page; unspecified equals LOW_AND_ABOVE or "a reasonable default level based on the filterType" in the REST reference; Medium and above on the floor settings page) and no page says which applies to a template created through the API without a level (checked the templates page, floor settings page, REST templates reference and overview)' + TBV,
            "T2 / T1 (documentation half; effective default stays open)")
        rep(C, c, 5, "The false-positive risk ratings in the overview table",
            '• The overview table rates the false-positive risk per level in words (very low, moderate, high) (overview, 2026-10-09)' + D,
            "hygiene ([Inferred] used for an absence; the absence is already the next [Not disclosed] bullet)")
        rep(C, c, 6, "Over the limit the filter returns", [
            '• Over the limit, a filter that finds a match still returns `MATCH_FOUND`; a filter that finds no match returns `EXECUTION_SKIPPED` with "Detection skipped as token limit exceeded." in `messageItems` (quotas page, 2026-10-09)' + D,
            '• A payload longer than the limit may be only partly screened. Premise: the quotas page says Model Armor "screens text up to 65,536 tokens" and states the skip result only for the no-match case' + I,
        ], "T52 (CORRECTION)")
        rep(C, c, 6, "Unlimited tokens apply in real-time streaming mode", [
            '• In real-time streaming mode Model Armor "supports unlimited tokens"; buffered streaming mode keeps the token limits (quotas page, sanitize page, 2026-10-09)' + D,
            '• For streamed content, "make sure that individual chunks don\'t exceed the token limits" (sanitize page, 2026-10-09)' + D,
            '• The token limits "don\'t apply to the Model Armor integration with Gemini Enterprise" (quotas page, 2026-10-09)' + D,
        ], "T54")
        edit(C, c, 8, "Default confidence level when the field is omitted", "High (templates page console note) or the same as Low and above (REST reference); needs testing",
             "High (templates page console note), Medium and above (floor settings page) or the same as Low and above (REST reference); needs testing",
             "T1 / T2 (R8 wording follows the three documented statements)")
    editsum(C, "MA1", 5, "Google states two different defaults for an omitted level.", "Google's pages state three different defaults for an omitted level.", "T2 (Summary)")
    setsum(C, "MA2", 5,
           "**Match states per category.** The result gives an overall match state and one for each of the four categories, sometimes with a confidence level. Google's pages state three different defaults for an omitted level. **[Documented]**",
           "style 3c / T8 (Summary led with a sample the Detail says is not evidence; Summary now follows the documented defaults; the sample stays in Detail and R8)")

    setsum(C, "MA2", 1,
           "**Output-level responsible AI safety filtering.** Model Armor screens a model response for hate speech, harassment, sexually explicit and dangerous content at a per-category confidence level. A CSAM check is on by default but unavailable in limited-support locations with residency enforced. The caller enforces any block. **[Documented]**",
           "T9 (CSAM caveat in Summary)")

    # ------------------------------------------------------------------ MA2 -----------------------------------------------------
    rep(C, "MA2", 2, "Hallucination, grounding or factuality checks on responses",
        '• Hallucination, grounding or factuality filter or setting: none described (checked the overview filter section, templates page detection list, REST `FilterConfig`, blog capabilities, product page features and best practices)' + ND,
        "T36")
    ins_after(C, "MA2", 2, "Hallucination, grounding or factuality filter", [
        '• The product page lists "providing incorrect policy information" and "generating inaccurate, offensive, or off-brand material" among chatbot and marketing risks and says Model Armor "helps mitigate these threats" and "helps ensure brand safety and integrity" (product page, marketing text, 2026-10-09)' + D,
        '• No accuracy or factuality check is named behind those marketing lines; the premise is that FilterConfig and the filter lists name none' + I,
    ], "T36")
    setsum(C, "MA2", 3,
           "**The model response text, sent on its own.** The caller posts it to the sanitize-model-response method of a regional endpoint with a template name. The docs examples send no user prompt, though the REST method reference lists an optional field for one. **[Documented]**",
           "T16 (CORRECTION)")

    def userprompt_bullets():
        return [
            '• The REST method reference for sanitizeModelResponse lists an optional `userPrompt` string, "User Prompt associated with Model response." (sanitizeModelResponse reference, 2026-10-09)' + D,
            '• The Go client request struct has the same optional `UserPrompt` field (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:2380-2381)' + GO,
            '• The Apigee SanitizeModelResponse policy has a required `<UserPromptSource>` element and sets a `userPrompt` flow variable (Apigee policy ref, Apigee docs not Model Armor docs, 2026-10-09)' + D,
        ]
    for c in ("MA2", "MA4", "MA8"):
        rep(C, c, 3, "The Go client request struct for the response method has an optional", userprompt_bullets(), "T16 (CORRECTION: field is in the REST method reference and the Apigee policy page)")
        if c in ("MA2", "MA4"):
            edit(C, c, 3, "Whether any filter uses that prompt as context", "(checked the sanitize page, the REST template reference, the overview and the Go client comments; none says)",
                 "(checked the sanitize page, the REST method and templates references, the overview, the Apigee policy page and the Go client comments; none says)",
                 "T16 / T17 (checked list extended)")
        r9add(C, c, URL_SMR, "T16 (method page URL)")
    for c in ("MA2", "MA4"):
        rep(C, c, 6, "Optional `UserPrompt` string in the Go client request",
            '• Optional `userPrompt` string in the request body of this method (sanitizeModelResponse reference, 2026-10-09)' + D, "T16")
    r8key = {"MA2": "Whether any filter uses the optional `userPrompt` field",
             "MA4": "Whether the optional `userPrompt` field of the response request",
             "MA8": "Whether the Go client's optional `userPrompt` field"}
    r8new = {"MA2": "• Whether any filter uses the optional `userPrompt` field of the response request (the REST method reference and the Apigee policy page list the field; none says what it changes)",
             "MA4": "• Whether the optional `userPrompt` field of the response request changes any result (the REST method reference and the Apigee policy page list the field; none says what it changes)",
             "MA8": "• Whether the optional `userPrompt` field of the response request changes the result for this filter (the REST method reference and the Apigee policy page list the field; none says what it changes)"}
    for c in ("MA2", "MA4", "MA8"):
        rep(C, c, 8, r8key[c], r8new[c], "T16 / T17 (R8 wording; the Go-client-only claim is wrong)")

    # ------------------------------------------------------------------ MA3 -----------------------------------------------------
    rep(C, "MA3", 2, "Release note 2026-10-10", [
        '• Release note dated 2026-10-09: "Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data", on the us and eu multi-regions with filter version v3 or later (release notes, 2026-10-09)' + D,
        '• What the Workspace data enhancement changes for ordinary prompts is not stated; the note scopes it to emails, documents and files from Workspace (checked the release note)' + ND,
    ], "T78 (CORRECTION: entry is dated 2026-10-09 on the live page)")
    rep(C, "MA4", 2, "Release note 2026-10-10", [
        '• Release note dated 2026-10-09: "Model Armor includes enhanced prompt injection and jailbreak protection for Workspace data", on the us and eu multi-regions with filter version v3 or later (release notes, 2026-10-09)' + D,
        '• What the Workspace data enhancement changes for ordinary prompts is not stated; the note scopes it to emails, documents and files from Workspace (checked the release note)' + ND,
    ], "T78 (CORRECTION)")
    edit(C, "MA3", 8, "What the Workspace data enhancement of 2026-10-10", "What the Workspace data enhancement of 2026-10-10 changes for ordinary prompts",
         "What the Workspace data enhancement of 2026-10-09 changes for ordinary prompts (needs testing; the release note scopes it to Workspace content)", "T78 (date; class b stays in R8)")

    # T18 (Go and Java clients)
    for c in ("MA3", "MA4"):
        rep(C, c, 4, "The Go client at v1.3.0 has no field", [
            '• The Go v1 `FilterConfig` has four fields (`RaiSettings`, `SdpSettings`, `PiAndJailbreakFilterSettings`, `MaliciousUriFilterSettings`); the strings FilterVersion, FilterRule, ExclusionRule and DataResidency occur 0 times in the apiv1 and apiv1beta `service.pb.go`, while the docs describe filter versions, exclusion rules and data residency (modelarmor/apiv1/modelarmorpb/service.pb.go@modelarmor/v1.3.0:1861)' + GO,
            '• The Java v1 proto has the same four `FilterConfig` fields and none of the filter-version, exclusion-rule or data-residency fields (java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto@v1.93.0:622)' + JV,
            '• The docs and REST reference describe these fields, so the client libraries lag the documented API; the premise is that the clients are generated from the same API definition' + I,
        ], "T18 + pin change (tag modelarmor/v1.3.0, main ruling) + hygiene (absence from a code grep cited with both packages)")
        r9add(C, c, [URL_GO_B, URL_JAVA], "T18 (apiv1beta and Java proto URLs)")

    # T3 / T4 / T19 / T85 (PI columns)
    D_adv = '• Threshold advice D, overview considerations: "for both prompt injection and jailbreak detection and general content safety (hate speech, harassment, dangerous content), start with High or Medium and above to minimize false positives." (overview, 2026-10-09)' + D
    for c in ("MA3", "MA4"):
        ins_after(C, c, 5, "Threshold advice C, overview table", D_adv, "T4 (fourth statement)")
        rep(C, c, 5, "Default when the level is omitted", [
            '• Floor settings: "If you don\'t specify the prompt injection and jailbreak detection confidence level, the confidence level defaults to LOW_AND_ABOVE for all levels: project, organization, or folder." (floor settings page, 2026-10-09)' + D,
            '• Template without a level: the REST enum says unspecified is "Same as LOW_AND_ABOVE" and the filter field states no default of its own, so an omitted level on a template would behave as Low and above; the premise is that the enum text applies to every filter that uses it' + I,
        ], "T3 / hygiene ([Inferred] used for a documented fact)")
        rep(C, c, 5, "The exclusion rules page shows `filterConfig.filterRuleSettings`", [
            '• The exclusion rules page and the templates page use `filterConfig.filterRuleSettings` in v1 requests and update masks (exclusion rules page, templates page, 2026-10-09)' + D,
            '• The REST `FilterConfig` lists only `raiSettings`, `sdpSettings`, `piAndJailbreakFilterSettings` and `maliciousUriFilterSettings`, and the page footer reads "Last updated 2026-09-07 UTC", before release note 2026-09-28 that introduced exclusion rules (REST templates ref, release notes, 2026-10-09)' + D,
            '• The REST reference probably lags the feature; the premise is the footer date before the release note' + I,
            '• Whether the v1 template API accepts `filterRuleSettings` (needs testing; the Go and Java v1 clients at the pins in R4 do not have the field)' + TBV,
        ], "T19")
        ins_after(C, c, 5, "Template-specific exclusion rules (Preview)",
                  '• Exclusion rules are a Preview feature and Preview offerings are Pre-GA Offerings: "PRE-GA OFFERINGS ARE PROVIDED “AS IS” WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES OR REPRESENTATIONS OF ANY KIND." (Google Cloud General Service Terms, Pre-GA Offerings Terms, 2026-10-09)' + D,
                  "T85")
        r9add(C, c, URL_GST, "T85 / T86 (General Service Terms)")
    setsum(C, "MA3", 5,
           "**Match flag plus a confidence level.** The result gives an execution state, a match state and a confidence level. Google's pages advise Medium or High as the setting, and Low and above for high-stakes categories. **[Documented]**",
           "T4 (Summary)")
    setsum(C, "MA4", 5,
           "**Match flag plus a confidence level field.** The result type has an execution state, a match state and a confidence level, though the docs' response example shows no level. Google's pages advise Medium or High as the setting. **[Documented]**",
           "T4 (Summary; MA4 response example shows no confidence field)")
    for c in ("MA3", "MA4"):
        edit(C, c, 8, "Default level when the field is omitted", "Default level when the field is omitted (inferred as Low and above from the enum; needs testing)",
             "Default level of a template that omits the field (floor settings default to Low and above; the template default is inferred from the enum; needs testing)", "T3 (R8)")
        rep(C, c, 6, "Over the limit the filter returns", [
            '• Over the limit, a filter that finds a match still returns `MATCH_FOUND`; a filter that finds no match returns `EXECUTION_SKIPPED` with "Detection skipped as token limit exceeded." in `messageItems` (quotas page, 2026-10-09)' + D,
            '• A payload longer than the limit may be only partly screened. Premise: the quotas page says Model Armor "screens text up to 65,536 tokens" and states the skip result only for the no-match case' + I,
        ], "T52 (CORRECTION)")
        rep(C, c, 6, "Unlimited tokens apply in real-time streaming mode", [
            '• In real-time streaming mode Model Armor "supports unlimited tokens"; buffered streaming mode keeps the token limits (quotas page, sanitize page, 2026-10-09)' + D,
            '• For streamed content, "make sure that individual chunks don\'t exceed the token limits" (sanitize page, 2026-10-09)' + D,
            '• The token limits "don\'t apply to the Model Armor integration with Gemini Enterprise" (quotas page, 2026-10-09)' + D,
        ], "T54")

    # ------------------------------------------------------------------ MA4 -----------------------------------------------------
    setsum(C, "MA4", 1,
           "**Output-level prompt injection and jailbreak detection.** The overview says the filter scans prompts and responses, and a sample response result shows it running. The templates page describes it for prompts only. The calling service enforces any block. **[Documented]**",
           "T13 (Summary label stays Documented: it rests on the overview sentence and the sample result)")
    rep(C, "MA4", 1, "Taken together, the overview, the sample output and the Apigee variables",
        '• The overview sentence is a direct statement; the templates page wording "in a prompt" is narrower and the docs do not say which reading is intended, so treating the filter as active on responses rests on the overview sentence and the sample result' + I,
        "T13")
    editsum(C, "MA4", 2, "The docs name MCP tool results as a target for injection by malicious tool authors",
            "The docs name MCP tool execution errors as a target for injection by malicious tool authors",
            "style 3a (Summary not entailed: Detail quotes tool execution errors)")
    edit(C, "MA4", 2, "System-prompt leakage detection on responses", "templates page detection list, REST `FilterConfig`, product page features and blog capabilities)",
         "templates page detection list, REST `FilterConfig`, product page features, best practices and blog capabilities)", "T36 (best practices added to the checked list)")

    # ------------------------------------------------------------------ MA7 -----------------------------------------------------
    setsum(C, "MA7", 1,
           "**Input-level malicious URL detection.** Model Armor scans the URLs in a user prompt to identify phishing or malware links. The overview gives both a URL inside a PDF and a link returned in a response as examples. The calling service enforces any block. **[Documented]**",
           "T37")
    rep(C, "MA7", 1, "The overview frames the filter mainly around output", [
        '• The overview section says the filter lets you "prevent malicious URLs from being returned" and speaks of "downstream systems processing LLM outputs"; its input-template focus does not name URLs while its output-template focus does (overview, 2026-10-09)' + D,
        '• The same section also gives a URL embedded in a PDF as its example and limits scanning to "the first 256 URLs found in prompts and responses", so the filter is not output-only; "mainly output" is a reading' + I,
    ], "T37 + hygiene ([Documented] used for a judgement)")
    antivirus = lambda: [
        '• The product page says Model Armor "Detects malicious files, malware, and unsafe URLs within AI prompts and responses", the region tables list "Antivirus scanning" and the result schema has a `virusScanFilterResult` for PDF (product page, feature availability page, REST result ref, 2026-10-09)' + D,
        '• Antivirus scanning is a separate capability outside this column. Premise: it has its own result type, no URL element and no configuration setting, and the project covers it in the inventory only' + I,
    ]
    rep(C, "MA7", 2, "The product page and the region tables also mention malware and antivirus scanning", antivirus(), "T57 + hygiene ([Documented] used for a scope judgement)")
    rep(C, "MA8", 2, "Malicious files and malware are a separate antivirus capability", antivirus(), "T57 + hygiene")
    rep(C, "MA7", 8, "Whether `us-east7` and `global` rows",
        '• Whether us-east7 and global in the feature availability table are locations where a template can be created (the locations page lists 16 regions and 2 multi-regions; the data residency page says the global endpoint cannot manage templates; checked both, not stated)', "T77")
    rep(C, "MA8", 8, "Whether `us-east7` and `global` rows",
        '• Whether us-east7 and global in the feature availability table are locations where a template can be created (the locations page lists 16 regions and 2 multi-regions; the data residency page says the global endpoint cannot manage templates; checked both, not stated)', "T77")
    rep(C, "MA7", 8, "Whether input-side use is intended",
        "• Whether input-side use is intended (the overview gives both a URL inside a PDF and a returned link as examples; its input-template focus does not name URLs)", "T37 (R8 wording)")

    # ------------------------------------------------------------------ AUP / terms (T86) ---------------------------------------
    aup = [
        '• Google\'s Acceptable Use Policy bars using the Services "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement" (Google Cloud Acceptable Use Policy, 2026-10-09)' + D,
        '• Whether sending jailbreak, injection or harmful-content prompts to measure detection rates is "expressly permitted" is not stated (checked the Acceptable Use Policy and the General Service Terms)' + ND,
    ]
    for c in ("MA1", "MA2", "MA3", "MA4", "MA7", "MA8"):
        det = C[c]["rows"][7]["detail"]
        det.extend(aup)
        from lib import OPS
        OPS.append(dict(loc=f"{c} R7", kind="insert", before="(none)", after=aup, reason="T86 (terms for live testing; applied to MA2, MA3, MA4 as well as the columns the resolution names, same test content)"))
        det8 = C[c]["rows"][8]["detail"]
        r8 = "• Whether the Acceptable Use Policy testing clause covers detection benchmarks (checked the Acceptable Use Policy and General Service Terms, not stated; needs the project owner's reading)"
        det8.append(r8)
        OPS.append(dict(loc=f"{c} R8", kind="insert", before="(none)", after=[r8], reason="T86 (class c; user question open at CP2)"))
        r9add(C, c, [URL_AUP, URL_GST], "T86 (terms URLs)")
    for c in ("MA1", "MA2"):
        ins_after(C, c, 7, "Do not build CSAM test material",
                  '• The Acceptable Use Policy lists "child sexual exploitation, child abuse" among illegal activity (Google Cloud Acceptable Use Policy, 2026-10-09)' + D,
                  "T86 (CSAM caution; MA2 added for consistency with MA1)")

    # blog URL in R9 of MA1-MA4 (absence bullets name "blog" among the pages checked)
    r9add(C, ["MA1", "MA2", "MA3", "MA4"], URL_BLOG, "hygiene (R9 omits the blog URL that the absence bullets cite)")

    # R9 summaries
    r9sum(C, "MA1", "Model Armor documentation pages on docs.cloud.google.com, the product page, the Security Command Center pricing page, the Google Cloud blog, the Apigee policy reference and release notes, and Google's terms pages.")
    r9sum(C, "MA2", "Model Armor documentation pages on docs.cloud.google.com, the product page, the pricing page, the blog, the Apigee policy reference and release notes, the Go client source and Google's terms pages.")
    r9sum(C, "MA3", "Model Armor documentation pages on docs.cloud.google.com, the product page, the pricing page, the blog, the Apigee policy reference and release notes, Go and Java client sources and Google's terms pages.")
    r9sum(C, "MA4", "Model Armor documentation pages on docs.cloud.google.com, the product page, the pricing page, the blog, the Apigee policy reference and release notes, Go and Java client sources and Google's terms pages.")
    r9sum(C, "MA7", "Model Armor documentation pages on docs.cloud.google.com, the product page, the pricing page, the Google Cloud blog, the Apigee policy reference and release notes, and Google's terms pages.")
    r9sum(C, "MA8", "Model Armor documentation pages on docs.cloud.google.com, the product page, the pricing page, the blog, the Apigee policy reference and release notes, the Go client source and Google's terms pages.")
