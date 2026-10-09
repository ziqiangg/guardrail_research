"""Inventory edits (sheet 3x). Applied after the global pin and hint normalisation."""
from lib import iedit, iapp, iintro, iaddrow

GOREPO = "[Documented: repo googleapis/google-cloud-go@modelarmor/v1.3.0]"
JAVAREPO = "[Documented: repo googleapis/google-cloud-java@v1.93.0]"

U_GO = "https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/apiv1/modelarmorpb/service.pb.go"
U_GO_B = "https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/modelarmor/apiv1beta/modelarmorpb/service.pb.go"
U_JAVA = "https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/proto-google-cloud-modelarmor-v1/src/main/proto/google/cloud/modelarmor/v1/service.proto"
U_POM = "https://github.com/googleapis/google-cloud-java/blob/v1.93.0/java-modelarmor/pom.xml"
U_PY = "https://github.com/googleapis/google-cloud-python/tree/google-cloud-modelarmor-v0.7.2"
U_NODE = "https://github.com/googleapis/google-cloud-node/tree/modelarmor-v0.10.0"
U_PHP = "https://github.com/googleapis/google-cloud-php-modelarmor/tree/v0.8.3"
U_NET = "https://github.com/googleapis/google-cloud-dotnet/tree/Google.Cloud.ModelArmor.V1-1.0.0-beta07"
U_LIC = "https://github.com/googleapis/google-cloud-go/blob/modelarmor/v1.3.0/LICENSE"
U_APG_RN = "https://docs.cloud.google.com/apigee/docs/release-notes"
U_APS_LIC = "https://github.com/GoogleCloudPlatform/apigee-samples/blob/2b1a9f00fabb4e837c39d80570ff50ebc3b1349e/LICENSE.txt"
U_SCCTF = "https://docs.cloud.google.com/security-command-center/docs/terraform"
U_SCCF = "https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings"
U_SDPM = "https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels"
U_AGW = "https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration"

OVERLIM_OLD = "above that the filter returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.'"
OVERLIM_NEW = "above that a filter that finds a match still returns MATCH_FOUND and a filter that finds none returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.'"
MATCHSENT = "Over the limit a filter that finds a match still returns MATCH_FOUND and one that finds none returns EXECUTION_SKIPPED [Documented] (QUO)."


def apply(pre, blocks):
    """pre: list of lines before the first block (index 1 is the Scope paragraph). Returns new pre."""
    # find the Scope paragraph
    k = [i for i, l in enumerate(pre) if l.startswith("Scope:")]
    assert len(k) == 1
    k = k[0]
    s = pre[k]

    def sub(old, new, reason):
        nonlocal s
        assert s.count(old) == 1, f"scope: {old[:60]!r} count {s.count(old)}"
        s = s.replace(old, new, 1)
        from lib import IOPS
        IOPS.append(dict(loc="Scope paragraph (not parsed)", kind="edit", before=old, after=new, reason=reason))

    # ---- T80: page footers (CORRECTION)
    sub("every docs page footer reads 'Last updated 2026-10-06 UTC' except the release notes page ('Last updated 2026-10-07 UTC'); the product page and the pricing page carry no last-updated line.",
        "page footers read 'Last updated 2026-10-06 UTC' for OV, TPL, SAN, FLR, QUO, FAR, DR, LOC, FV, VH, EXC, BP, INT, GE, APG, AGW, VTX, LC, LOG, MON, RTY, NET and MCPD; 'Last updated 2026-10-07 UTC' for RN, APU and APR; 'Last updated 2026-10-05 UTC' for LIB; 'Last updated 2026-09-24 UTC' for RR; 'Last updated 2026-09-07 UTC' for RT and the DataItem reference; and 'Last updated 2026-08-19 UTC' for the two sanitize method pages; the product page and the pricing page carry no last-updated line, and the RN footer lags its newest entry, dated October 09, 2026. The read date 2026-10-09 is the pin for every docs fact.",
        "T80 (CORRECTION: blanket footer statement was wrong for REST, library, Apigee and SDP pages)")
    # ---- pin sentence
    sub("Google Cloud client library facts are pinned to googleapis/google-cloud-go at modelarmor/v1.3.0 (shallow clone, HEAD of 2026-10-08, modelarmor module 1.3.0); Apigee sample facts to GoogleCloudPlatform/apigee-samples at 2b1a9f00 (HEAD of 2026-09-23).",
        "Google Cloud client library facts are pinned to googleapis/google-cloud-go at tag modelarmor/v1.3.0 (commit 8a17bee2, module 1.3.0; the sparse clone was taken at HEAD 37f936ac of 2026-10-08, whose service.pb.go is identical to the tag because the two differ only in the client wrapper files, go.mod and go.sum), to googleapis/google-cloud-java at tag v1.93.0, and for the other languages to the latest tags named in the client library row; Apigee sample facts to GoogleCloudPlatform/apigee-samples at 2b1a9f00 (HEAD of 2026-09-23).",
        "pin change to the release tag (main ruling on modelarmor P5 r1 Q1; README section 3 rule 8)")
    # ---- T23 rule S
    sub("Status rule S: where a docs page or release note states GA or Preview, the cell says so [Documented]; where no page states GA and the relevant page section carries no Pre-GA banner, the cell says GA [Inferred] (premise: Google marks pre-GA features with a Pre-GA banner or a Preview label, as it does for image screening, modalities, exclusion rules and LangChain); where there is no basis, the cell says [Not disclosed].",
        "Status rule S: where a docs page or release note states GA or Preview, the cell says so [Documented]; where no page states GA and the page that was read shows no launch-stage banner for the feature, the cell says GA [Inferred] (premise: Google marks Preview features with a banner, for example image screening on the overview and exclusion rules on their page; no page states GA for the base service and the first release note, 2025-02-03, carries no stage word); where the page was not read for a banner or there is no basis, the cell says [Not disclosed] or [To be verified].",
        "T23 + main ruling (banner-free rule)")
    # ---- T24 / T85 short names and Pre-GA sentence
    sub("APSAMP = apigee-samples llm-security-v2 README.",
        "APSAMP = apigee-samples llm-security-v2 README; SCCTF = https://docs.cloud.google.com/security-command-center/docs/terraform (SCC docs, not Model Armor docs); GST = https://cloud.google.com/terms/service-terms. Preview features are Pre-GA Offerings under the General Service Terms: provided 'as is', not covered by any SLA, with no data processing terms applying unless Google's documentation says otherwise [Documented] (GST; read 2026-10-09).",
        "T24 (SCCTF short name) + T85 (Pre-GA terms in the intro only, main ruling)")
    pre = list(pre)
    pre[k] = s

    # ============================================================ (a)
    iintro(blocks, "a", "mentions 'sensitive data protection (including topicality)' [Documented] (OV); a topic setting or page [Not disclosed] (checked RT, TPL, OV filters section).",
           "mentions 'sensitive data protection (including topicality)' [Documented] (OV), so topicality is named only inside the sensitive data protection filter [Documented] (OV); a topic setting or page [Not disclosed] (checked RT, TPL, EXC, FLR, BP, OV filters section, PROD and the Google Cloud blog).", "T35")
    iintro(blocks, "a", "(checked FilterConfig in RT, the filter list in OV and the detection list in TPL)",
           "(checked FilterConfig in RT, the filter list in OV, the detection list in TPL, BP, PROD and the Google Cloud blog)", "T36")
    RAI = "Responsible AI (RAI) safety filter"
    iedit(blocks, "a", RAI, "Limit", OVERLIM_OLD, OVERLIM_NEW, "T52 (CORRECTION)")
    iedit(blocks, "a", "Child sexual abuse material (CSAM) filter", "Default",
          "Always on: 'This filter is applied by default and cannot be turned off.' [Documented] (OV)",
          "On by default: 'This filter is applied by default and cannot be turned off.' [Documented] (OV). With data residency enforcement on, not available in the seven limited-support locations [Documented] (FAR). Available there with enforcement off [Inferred] (premise: RN 2026-08-27 says disabling enforcement enables features otherwise unavailable; CSAM is not named in that sentence)",
          "T9")
    PI = "Prompt injection and jailbreak detection"
    iapp(blocks, "a", PI, "Default", "A template that omits the level would behave as Low and above [Inferred] (premise: the enum text applies to every filter that uses it).", "T3")
    iapp(blocks, "a", PI, "Levels or options", "A fourth statement in the OV considerations: 'start with High or Medium and above to minimize false positives' for prompt injection and jailbreak detection and general content safety [Documented] (OV).", "T4")
    iedit(blocks, "a", PI, "Limit", "65,536 tokens (EXECUTION_SKIPPED above that)",
          "65,536 tokens (above that a filter that finds a match still returns MATCH_FOUND and one that finds none returns EXECUTION_SKIPPED)", "T52 (CORRECTION)")
    SB = "Sensitive Data Protection (SDP), basic configuration"
    iedit(blocks, "a", SB, "Levels or options",
          "Count differs: six categories on OV and RT, seven infoTypes on SAN [Documented] (OV; RT; SAN)",
          f"Count differs: six categories on OV and RT, seven infoTypes on SAN [Documented] (OV; RT; SAN). A Go client comment on the basic configuration also says 'a fixed set of six info-types' {GOREPO} (GOPB1). Which count is current [Not disclosed] (no page reconciles them; checked OV, RT, SAN, RN). 'US-based regions' is not defined [Not disclosed] (checked SAN, OV, FAR, DR, LOC); it probably means the locations whose jurisdiction is the United States [Inferred] (premise: the jurisdiction column of DR and FAR)",
          "T41 + T43 + hygiene (absence clause split from the documented count)")
    iapp(blocks, "a", SB, "Applies to", "Advanced mode screens prompts and responses [Documented] (SAN). Whether the basic infoType list applies to responses [Not disclosed] (checked OV, SAN, TPL, RT, APR). The setting has no direction field in RT [Documented] (RT), so the same list on responses is probable [Inferred].", "T44")
    iedit(blocks, "a", SB, "Limit", "130,000 tokens [Documented] (QUO)", "130,000 tokens [Documented] (QUO). " + MATCHSENT, "T52 (CORRECTION)")
    SA = "Sensitive Data Protection (SDP), advanced configuration"
    iapp(blocks, "a", SA, "Result field", "A response-side example of deidentifyResult [Not disclosed] (checked SAN, TPL, RR, APR).", "T45")
    iedit(blocks, "a", SA, "Limit", "130,000 tokens [Documented] (QUO). Not supported", "130,000 tokens [Documented] (QUO). " + MATCHSENT + " Not supported", "T52 (CORRECTION)")
    AV = "Antivirus scanning"
    iedit(blocks, "a", AV, "Config key", "[To be verified] (checked OV, TPL, SAN, FLR, FAR and RN; no configuration page found)",
          "[Not disclosed] (checked OV, TPL, SAN, FLR, FAR, RN, QUO, INT and SCCF; no configuration page found)", "T57 (label To be verified -> Not disclosed)")
    iapp(blocks, "a", AV, "Source URL", U_SCCF, "T57")
    OCR = "Image text extraction (optical character recognition, OCR)"
    iedit(blocks, "a", OCR, "Levels or options", "Which filters run on the text follows the template: 'depending on the filter configuration' [Documented] (RT)",
          "Text content of an image is sanitized 'depending on the filter configuration' [Documented] (RT). Which of the RAI, prompt injection and malicious URL filters run on OCR text [Not disclosed] (checked OV, SAN, TPL, RT, RN)", "T11")
    iedit(blocks, "a", OCR, "Limit", "images embedded in files are not screened;",
          "images embedded in files are not screened per OV [Documented] (OV), and INT says the same for the Gemini Enterprise integration [Documented] (INT), while GE lists images inside uploaded files as screened [Documented] (GE), and no page reconciles them [Not disclosed] (checked OV, INT, GE, RN, SAN);", "T58")
    iedit(blocks, "a", "Image visual scanning", "Result field", "finding locations carry image bounding boxes [Documented] (RR)",
          "finding locations carry image bounding boxes as a list (boundingBoxes) per RR and the Go library, while one SAN example shows a single boundingBox object [Documented] (RR; SAN)", "T70")
    DOC = "Document text extraction and screening of files"
    iapp(blocks, "a", DOC, "Levels or options", "Metadata-label detection: Google Drive labels and Microsoft sensitivity labels on DOCX, PDF, PPTX and XLSX; not usable in inspection rule sets or de-identification transformations [Documented] (SDP custom metadata label page).", "T66")
    iapp(blocks, "a", DOC, "Source URL", U_SDPM, "T66")

    # ============================================================ (b)
    LIBR = "Client libraries for C#, Go, Java"
    iedit(blocks, "b", LIBR, "Status",
          "Versions of the Java, Node.js, PHP and Python libraries [Not disclosed] (LIB checked; install commands give no pin)",
          f"Java google-cloud-modelarmor 0.40.0 in the sbt line [Documented] (LIB); the Java parent pom at v1.93.0 also reads 0.40.0 {JAVAREPO}. Latest repo tags (tag names read with git ls-remote on 2026-10-09): Python google-cloud-modelarmor-v0.7.2 [Documented: repo googleapis/google-cloud-python@google-cloud-modelarmor-v0.7.2]; Node.js modelarmor-v0.10.0 [Documented: repo googleapis/google-cloud-node@modelarmor-v0.10.0]; PHP v0.8.3 [Documented: repo googleapis/google-cloud-php-modelarmor@v0.8.3]; C# Google.Cloud.ModelArmor.V1-1.0.0-beta07, while LIB shows 1.0.0-beta05 [Documented: repo googleapis/google-cloud-dotnet@Google.Cloud.ModelArmor.V1-1.0.0-beta07]. Pre-release status of the Python, Node.js and PHP 0.x versions [Inferred] (premise: version below 1.0). Release notes and changelogs of these four repositories [Not disclosed] (not read; versions come from tag names only)",
          "T25 (main ruling: client versions in the inventory)")
    iapp(blocks, "b", LIBR, "Limitations",
         f"The Java v1 proto has the same four FilterConfig fields and none of the filter-version, exclusion-rule or data-residency fields {JAVAREPO}. Licence: Apache License 2.0 for the Go module cloud.google.com/go/modelarmor {GOREPO} (LICENSE; modelarmor/apiv1/version.go header). Docs code samples are Apache 2.0 and docs text is CC BY 4.0 [Documented] (page footers).",
         "T18 (Java) + T87 (licence)")
    for u, r in [(U_JAVA, "T18"), (U_POM, "T25"), (U_PY, "T25"), (U_NODE, "T25"), (U_PHP, "T25"), (U_NET, "T25"), (U_LIC, "T87")]:
        iapp(blocks, "b", LIBR, "Source URL", u, r)
    TF = "Terraform resources for Model Armor"
    iedit(blocks, "b", TF, "Path", "Terraform resources for Model Armor floor settings and templates [Documented] (RN 2025-07-29)",
          "Terraform resources google_model_armor_floorsetting and google_model_armor_template [Documented] (SCCTF; RN 2025-07-29)", "T24")
    iedit(blocks, "b", "Terraform resources", "Status", "[Not disclosed] (the release note gives no GA or Preview label; the Terraform resource page was not read [To be verified])",
          "[Not disclosed] (the release note and the SCC Terraform page give no GA or Preview label)", "T24 (not extended to rule S: no banner check was recorded for this page; see open items)")
    iedit(blocks, "b", "Terraform resources", "Limitations", "[To be verified] (resource page not read; fields and limits unknown)",
          "[To be verified] (the argument reference is on the HashiCorp provider registry page, not read; not an official source)", "T24")
    iapp(blocks, "b", "Terraform resources", "Source URL", U_SCCTF, "T24")
    iapp(blocks, "b", "Gemini Enterprise Agent Platform, generateContent", "Limitations", "Token limits on this route [Not disclosed] (checked QUO and VTX).", "T53")
    iapp(blocks, "b", "Agent Gateway, Client-to-Agent", "Limitations",
         "Agent Gateway page: a template can 'block and redact content that violates policies', yet its flow text says the gateway 'either allows or blocks it based on the verdict' [Documented] (AGW). Whether Agent Gateway forwards de-identified text rather than only blocking [Not disclosed] (checked AGW, NET, INT). Token limits on this route [Not disclosed] (checked QUO and AGW).", "T26 + T53")
    iapp(blocks, "b", "Agent Gateway, Agent-to-Anywhere", "Limitations",
         "Agent Gateway page: the intro says a template can 'block and redact content that violates policies', yet the egress flow text says the gateway 'either allows it to reach the agent or blocks it' [Documented] (AGW). Whether Agent Gateway forwards de-identified text rather than only blocking [Not disclosed] (checked AGW, NET, INT).", "T26")
    iedit(blocks, "b", "Apigee API proxies", "Status", "[To be verified] (no GA or Preview label found on APG, APU or APR)",
          "Preview 2025-05-22, GA 2025-09-04 on Apigee X [Documented] (Apigee release notes, Apigee docs not Model Armor docs)", "T20")
    iapp(blocks, "b", "Apigee API proxies", "Source URL", U_APG_RN, "T20")
    iapp(blocks, "b", "Apigee API proxies", "Limitations", f"Samples licence: Apache 2.0 [Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00] (README License section; LICENSE.txt).", "T87")
    iapp(blocks, "b", "Apigee API proxies", "Source URL", U_APS_LIC, "T87")
    iapp(blocks, "b", "Gemini Enterprise: user prompts", "Modalities", "No page reconciles the two lists [Not disclosed] (checked INT, GE, RN).", "T60")
    iedit(blocks, "b", "Google and Google Cloud MCP servers", "Status", "Preview 2025-12-10, GA 2026-04-22 [Documented] (RN)",
          "Preview 2025-12-10, GA 2026-04-22 [Documented] (RN). The floor settings page still labels the link '(Preview)' [Documented] (FLR). The dated release note is used because the page label is undated [Inferred] (premise: a dated entry is more current than an undated link label)", "T22")
    iapp(blocks, "b", "Google and Google Cloud MCP servers", "Limitations", "Token limits on this route [Not disclosed] (checked QUO and MCPD).", "T53")
    iedit(blocks, "b", "Service Extensions on Cloud Load Balancing", "Status",
          "GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN and NET)",
          "GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN, NET and INT; the Service Extensions configuration page returned no text through the raw fetch, so it is unread)", "T21 (main ruling: To be verified)")
    iapp(blocks, "b", "Service Extensions on Cloud Load Balancing", "Limitations",
         "NET says Model Armor instructs the networking service to 'allow, block, or modify the traffic' [Documented] (NET). Whether Service Extensions forward de-identified text rather than only blocking [Not disclosed] (checked NET, INT, AGW, APG). Token limits on this route [Not disclosed] (checked QUO and NET).", "T26 + T53")
    SCC = "Security Command Center findings from Model Armor"
    iapp(blocks, "b", SCC, "Limitations",
         "AGW says violations detected through Agent Gateway are 'also surfaced in Security Command Center' [Documented] (AGW). SCCF lists no per-prompt finding type [Documented] (SCCF), so the INT and AGW sentences describe more than SCCF lists [Inferred] (premise: the SCCF table is the finding catalogue).", "T81")
    iapp(blocks, "b", SCC, "Source URL", U_AGW, "T81")

    # ============================================================ (c)
    iapp(blocks, "c", "filterVersionSelector", "Effect",
         f"The Go v1 FilterConfig has no filter-version field {GOREPO} (GOPB1; GOPB1B) and the Java v1 proto has none {JAVAREPO}; the docs and REST reference describe it [Documented] (RT).", "T18")
    iapp(blocks, "c", "filterVersionSelector", "Source URL", U_GO, "T18")
    iapp(blocks, "c", "filterVersionSelector", "Source URL", U_JAVA, "T18")
    PJ = "piAndJailbreakFilterSettings"
    iapp(blocks, "c", PJ, "Default", "A template that omits the level would behave as Low and above [Inferred] (premise: the enum text applies to every filter that uses it).", "T3")
    iapp(blocks, "c", PJ, "Effect", "OV considerations add: 'start with High or Medium and above to minimize false positives' [Documented] (OV).", "T4")
    iedit(blocks, "c", "filterRuleSettings", "Where set", "this field in the REST reference [To be verified] (not shown there)",
          "this field is not in the REST list [Documented] (RT), whose page footer reads 'Last updated 2026-09-07 UTC', before release note 2026-09-28 that introduced exclusion rules [Documented] (RT; RN); the REST page probably lags the feature [Inferred] (premise: the footer date precedes the release note); whether the live v1 API accepts the field [To be verified] (needs testing)", "T19")
    iapp(blocks, "c", "logSanitizeOperations", "Effect", "RT only says 'If true, log sanitize operations.' [Documented] (RT).", "T79")
    iapp(blocks, "c", "Floor-setting inline enforcement", "Status",
         "The floor settings page still labels the MCP link '(Preview)' [Documented] (FLR). The dated release note is used because the page label is undated [Inferred] (premise: a dated entry is more current than an undated link label).", "T22")

    # ============================================================ (d)
    iintro(blocks, "d", "One row per location: 16 regions and the us and eu multi-regions, as on LOC [Documented] (LOC).",
           "One row per location: 16 regions and the us and eu multi-regions as on LOC [Documented] (LOC), plus two FAR-only rows.", "T77")
    iintro(blocks, "d", "FAR also lists rows for us-east7 and global that LOC and DR do not list [Documented] (FAR); they are not given a row here.",
           "FAR also lists rows for us-east7 and global that LOC, DR and FV do not list [Documented] (FAR); they are given rows here with the FAR values only, and every other cell is [Not disclosed] (checked LOC, DR, FAR, FV, VH). DR says the global endpoint cannot manage templates or sanitize [Documented] (DR), and OV says image screening is supported only in the us and eu multi-regions [Documented] (OV), so FAR listing global with Image Yes conflicts with both; whether either location accepts a template is [Not disclosed] (checked LOC, DR, FAR). The Supported filters, Multi-language, CSAM, Image and Antivirus columns describe templates with data residency enforcement enabled [Documented] (FAR).",
           "T77 + T9 (block (d) lists the union of 20 locations, main ruling on cols_a Q1)")
    base = "https://docs.cloud.google.com/model-armor/"
    row_east7 = ["us-east7 [Documented] (FAR)", "[Not disclosed] (checked LOC, DR and FAR; no description)", "[Not disclosed] (checked DR and FAR)",
                 "[Not disclosed] (checked the full-support and limited-support lists in DR and FAR)", "[Not disclosed] (checked DR and FAR; no residency row)",
                 "Responsible AI, Sensitive Data Protection, Prompt injection and jailbreak, Malicious URL [Documented] (FAR)",
                 "Yes [Documented] (FAR)", "Yes [Documented] (FAR)", "No [Documented] (FAR)", "Yes [Documented] (FAR)",
                 "[Not disclosed] (checked FV and VH; neither lists this location)",
                 f"{base}feature-availability-by-region ; {base}locations ; {base}data-residency ; {base}set-filter-version"]
    row_global = ["global [Documented] (FAR)", "[Not disclosed] (checked LOC, DR and FAR; no description). DR says the global endpoint is supported only for managing floor settings and does not manage templates or sanitize [Documented] (DR)",
                  "[Not disclosed] (checked DR and FAR)", "[Not disclosed] (checked the full-support and limited-support lists in DR and FAR)",
                  "[Not disclosed] (checked DR and FAR; no residency row)",
                  "Responsible AI, Sensitive Data Protection, Prompt injection and jailbreak, Malicious URL [Documented] (FAR)",
                  "Yes [Documented] (FAR)", "Yes [Documented] (FAR)", "Yes [Documented] (FAR). OV says image screening is supported only in the us and eu multi-regions [Documented] (OV)", "Yes [Documented] (FAR)",
                  "[Not disclosed] (checked FV and VH; neither lists this location)",
                  f"{base}feature-availability-by-region ; {base}locations ; {base}data-residency ; {base}overview ; {base}set-filter-version"]
    iaddrow(blocks, "d", row_east7, "T77 (FAR-only row; union of 20)", after_key="eu [Documented]")
    iaddrow(blocks, "d", row_global, "T77 (FAR-only row; union of 20)", after_key="us-east7")

    # ============================================================ (e)
    iapp(blocks, "e", "Standalone price", "Applies to", "Whether the 2 million token allowance is per project, organisation or billing account [Not disclosed] (checked PRC, OV, QUO).", "T82")
    iedit(blocks, "e", "Sensitive Data Protection token limit", "When exceeded",
          "EXECUTION_SKIPPED with the token-limit message when no match was found within the limit [Documented] (QUO)",
          "A filter that finds a match returns MATCH_FOUND; EXECUTION_SKIPPED with the token-limit message when the filter finds no match and the text exceeds the limit [Documented] (QUO)", "T52 (CORRECTION)")
    return pre
