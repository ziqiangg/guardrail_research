import sys
sys.path.insert(0,'.')
from blk_a import BLOCK_A
from blk_b import BLOCK_B
from blk_c import BLOCK_C
from blk_d import BLOCK_D
from blk_e import BLOCK_E
SCOPE=("Scope: Google Cloud Model Armor, a managed Google Cloud service that screens LLM prompts and responses: filters, integration paths, template and floor-setting parameters, locations and limits. "
"Sensitive Data Protection (SDP) is a separate Google product: this sheet records only how Model Armor invokes it (basic and advanced configuration, templates, roles, limits, result fields); infoType catalogues and transformations belong to the SDP product. "
"Rows whose Covered by cell is the inventory-only marker are current and documented but deliberately not Table 3 columns. "
"All Google documentation pages were read on 2026-10-09; every docs page footer reads 'Last updated 2026-10-06 UTC' except the release notes page ('Last updated 2026-10-07 UTC'); the product page and the pricing page carry no last-updated line. No versioned docs or source repository exist for the service itself, so docs facts are [Documented] without a pin and no service version is claimed. "
"Google Cloud client library facts are pinned to googleapis/google-cloud-go at 37f936ac (shallow clone, HEAD of 2026-10-08, modelarmor module 1.3.0); Apigee sample facts to GoogleCloudPlatform/apigee-samples at 2b1a9f00 (HEAD of 2026-09-23). The repositories GoogleCloudPlatform/model-armor-samples and googleapis/python-modelarmor were not readable (the clone asked for credentials when tried at brief time) and are not used. "
"Docs host: the seed URL https://cloud.google.com/security-command-center/docs/model-armor-overview redirects (first hop HTTP 301) to https://docs.cloud.google.com/model-armor/overview with a final status of 200 [Documented] (observed 2026-10-09); https://cloud.google.com/model-armor/docs and https://docs.cloud.google.com/model-armor/pricing return HTTP 404 [Documented] (observed 2026-10-09). The owner is Google Cloud throughout. "
"Naming: the docs now call Vertex AI 'Gemini Enterprise Agent Platform' (Agent Platform) but still say 'Gemini API in Vertex AI' for the generateContent method and use VERTEX_AI in gcloud flags [Documented] (VTX; INT). "
"Status rule S: where a docs page or release note states GA or Preview, the cell says so [Documented]; where no page states GA and the relevant page section carries no Pre-GA banner, the cell says GA [Inferred] (premise: Google marks pre-GA features with a Pre-GA banner or a Preview label, as it does for image screening, modalities, exclusion rules and LangChain); where there is no basis, the cell says [Not disclosed]. "
"Model identity, training data, accuracy figures, latency and per-category scores for any filter are [Not disclosed] (checked OV, PROD, FV, VH, RN, QUO, BP and RR). "
"Short names for sources (all under https://docs.cloud.google.com/model-armor/ unless stated): OV = overview; TPL = manage-templates; SAN = sanitize-prompts-responses; FLR = configure-floor-settings; QUO = quotas; FAR = feature-availability-by-region; DR = data-residency; LOC = locations; FV = set-filter-version; VH = version-history; EXC = configure-exclusion-rules; LOG = configure-logging; BP = best-practices; INT = integrations; VTX = model-armor-vertex-integration; APG = model-armor-apigee-integration; AGW = model-armor-agent-gateway-integration; GE = model-armor-gemini-enterprise-integration; LC = model-armor-langchain-integration; MCPD = model-armor-mcp-google-cloud-integration; NET = model-armor-networking-integration; LIB = reference/libraries; RN = release-notes (entries cited by date); RT = reference/rest/v1/projects.locations.templates; RR = reference/rest/v1/SanitizationResult; MON = monitoring-dashboard; RTY = retry-strategy; MCPS = docs.cloud.google.com/mcp/model-armor-supported-products; SCCF = Security Command Center docs concepts-vulnerabilities-findings (SCC docs, not Model Armor docs); PROD = cloud.google.com/security/products/model-armor; PRC = cloud.google.com/security-command-center/pricing; APU and APR = Apigee docs pages for the SanitizeUserPrompt and SanitizeModelResponse policies; GOCH, GOVER, GOPB1 and GOPB1B = CHANGES.md, internal/version.go, apiv1 service.pb.go and apiv1beta service.pb.go of the google-cloud-go modelarmor module; APSAMP = apigee-samples llm-security-v2 README.")
A_INTRO=("One row per filter or detector that Model Armor runs. Each filter has the same schema and confidence semantics in both directions; the request field and method differ (userPromptData with sanitizeUserPrompt, modelResponseData with sanitizeModelResponse). "
"Not offered as filters: prompt or system-prompt leakage detection, topic or off-topic enforcement, hallucination or grounding checks and refusal detection [Not disclosed] (checked FilterConfig in RT, the filter list in OV and the detection list in TPL). "
"The OV usage scenarios do describe 'Enforce custom topics' [Documented] (OV), and the confidence-level paragraph mentions 'sensitive data protection (including topicality)' [Documented] (OV); a topic setting or page [Not disclosed] (checked RT, TPL, OV filters section).")
B_INTRO=("One row per way to reach or manage Model Armor, including configuration and reporting surfaces. Agent Gateway has two rows because the ingress path screens ordinary agent prompts and responses while the egress path screens tool, MCP, A2A and external LLM traffic. "
"Per INT, only the Gemini Enterprise integration supports documents ('only the Gemini Enterprise integration supports documents. All other integrations scan and sanitize only text.') [Documented] (INT). "
"INT also says the Gemini Enterprise Agent Platform, Agent Runtime and Apigee integrations sanitize the initial prompt, the final response and intermediate steps such as grounding data and web-search results [Documented] (INT).")
C_INTRO=("One row per template, filter-config or floor-setting parameter. JSON names follow the REST reference (camelCase); the docs also show snake_case spellings in some examples. Defaults that differ between pages are given as separate facts.")
D_INTRO=("One row per location: 16 regions and the us and eu multi-regions, as on LOC [Documented] (LOC). Support level and the four feature columns describe templates with data residency enforcement on. Floor-setting configurations make all features available, with residency varying by location [Documented] (FAR). "
"With enforcement off in a template, cross-jurisdictional routing enables all features except image modality, which stays us and eu only [Documented] (TPL; RN 2026-08-27). "
"FAR also lists rows for us-east7 and global that LOC and DR do not list [Documented] (FAR); they are not given a row here.")
E_INTRO=("Quotas, system limits and pricing as documented. Limits for exclusion rules are Preview. The pricing page carries no last-updated line, so prices are as read on 2026-10-09.")
NOTES="""## Reviewer notes

1. Source conflicts, each recorded in the cells as separate facts with their own label:
   - Prompt injection and jailbreak confidence advice: OV example strategy says Medium (High for Gemini Enterprise); TPL says High (block a, row 3).
   - Basic SDP infoTypes: OV and RT say six; SAN lists five for all regions plus two for US-based regions (block a, row 5).
   - Default confidence level: TPL console note says High; RT says unspecified equals LOW_AND_ABOVE and RAI uses a reasonable default by filterType; FLR console note says Medium and above for RAI and LOW_AND_ABOVE for prompt injection and jailbreak (block a row 1, block c). Effective template default needs testing.
   - Images inside documents: OV and INT say they are not screened; GE says images contained inside uploaded files are screened for Gemini Enterprise. The INT options table lists Text, documents for Gemini Enterprise, without images, while GE lists images (block b).
   - Token limits: RN history (2,000, 10,000, 65,536) versus the current QUO page; OV does not state the SDP 130,000 limit; QUO says its limits do not apply to the Gemini Enterprise integration (block e).
   - Filter version retirement: RN 2026-09-02 said v1 and v2 retire 2026-11-29; RN 2026-09-18 and FV say 2026-12-17. The later date is used and both are stated (block c).
   - Antivirus: PROD says 'Detects malicious files, malware, and unsafe URLs'; FAR lists Antivirus scanning as a feature; RR has virusScanFilterResult; RT FilterConfig has no antivirus setting and the RR filterResults key list omits an antivirus key; no configuration page was found (block a row 7).
   - Exclusion rules: EXC shows filterConfig.filterRuleSettings but the RT FilterConfig reference lists four settings only (block c).
   - Security Command Center: INT says a floor-setting violation sends a finding; SCCF lists only the FLOOR_SETTINGS_VIOLATION finding for Model Armor (a template that fails conformance), not per-prompt findings (block b).
   - logSanitizeOperations: LOG says full content is logged; OV says metadata or snippets as configured (block c).
   - Go client: the apiv1 package (google-cloud-go@37f936ac) has no GOOGLE_MCP_SERVER integrated service and no exclusion-rule types; apiv1beta has the MCP service. This lags the REST docs and gcloud flags (block b row 2).
   - FAR lists us-east7 and global rows absent from LOC and DR (block d intro). FAR says Multi-language No in asia-south1 and northamerica-northeast2 while SAN speaks of limited multi-language support there (block d).
2. Release-note entry dated 2026-10-10 (enhanced prompt injection and jailbreak protection for Workspace data) was present on 2026-10-09; it is not used as a fact in any row.
3. Judgement calls:
   - Row counts differ from the brief targets (10/12/16/18/16): block b has 15 rows (Agent Gateway split into ingress and egress, plus rows for the console and for the monitoring dashboard with Cloud Logging); the other blocks match.
   - Agent Gateway egress, Google and Google Cloud MCP servers, Security Command Center findings, gcloud, Terraform, the console and the monitoring dashboard use the inventory-only marker; Agent Gateway ingress lists the eight text columns (the brief listed Agent Gateway under MA1 to MA8 and also named its egress under the marker).
   - Status rule S makes GA an [Inferred] label for features with no stated stage; Apigee, Terraform, gcloud, the console and Security Command Center findings are [Not disclosed] or [To be verified] instead.
   - Visual scanning is covered by MA5, MA6 and MA10 as the brief directs; document extraction by MA9 only.
   - Block d shows both the template data-residency values and the Agent Platform floor-setting values, which differ in several regions.
4. Not read or not reachable: the whitepaper linked from PROD; the Terraform resource page; the Model Armor findings detail in SCC beyond the table on SCCF; GoogleCloudPlatform/model-armor-samples and googleapis/python-modelarmor (not retried in this run; the clone form was refused by the permission layer; the brief records the clone asking for credentials at P1).
5. No fact comes from a summarising fetch: pages were read with fetch_text.py; the OpenAI payload list on AGW and the link targets on OV, INT and MCPD were read from the raw HTML with curl; repository facts come from a shallow clone.
"""
def main():
    out=["# Model Armor inventory (draft for sheet 3x)","",SCOPE,"",
    "## (a) Filters and detectors","",A_INTRO,"",BLOCK_A,
    "## (b) Integration paths","",B_INTRO,"",BLOCK_B,
    "## (c) Template and floor-setting parameters","",C_INTRO,"",BLOCK_C,
    "## (d) Locations and feature availability","",D_INTRO,"",BLOCK_D,
    "## (e) Quotas, limits and pricing","",E_INTRO,"",BLOCK_E,
    NOTES]
    open('/home/user/guardrail_research/benchtest/drafts/modelarmor_inventory.md','w',encoding='utf-8').write("\n".join(out))
main()
