from inv_common import *
HB=["Path","Status (GA/Preview)","Modalities","Mode (inline/API)","Direction","Config route (template/floor setting)","Limitations","Covered by Table 3 column","Source URL"]
R=[]
R.append(row([
"Direct REST API at the regional endpoint modelarmor.LOCATION.rep.googleapis.com: sanitizeUserPrompt, sanitizeModelResponse, StreamSanitizeUserPrompt and StreamSanitizeModelResponse [Documented] (SAN; DR)",
"Text methods: no GA or Preview statement and no Pre-GA banner, so GA [Inferred] (status rule S). Streaming: Preview 2026-05-12, GA 2026-07-10 [Documented] (RN). Image screening: Preview [Documented] (OV)",
"Text, documents and images ('The Model Armor REST API supports all modalities, including text, documents, and images') [Documented] (INT). Streaming methods take text only, not attachments [Documented] (SAN)",
"API: the service returns a verdict and the application enforces it; 'Model Armor functions only as a detector using templates' [Documented] (INT)",
"Input and Output through separate methods [Documented] (SAN)",
"Template named in the request path. The global endpoint modelarmor.googleapis.com manages floor settings only and cannot manage templates or sanitize [Documented] (TPL; DR)",
"Regional endpoint required; from a VPC network a Private Service Connect endpoint is needed [Documented] (OV). 1,200 queries per minute per project [Documented] (QUO). Do not send conversation history or the system prompt in userPromptData [Documented] (SAN)",
ALL]))
R.append(row([
"Client libraries for C#, Go, Java, Node.js, PHP and Python, wrapping the same REST methods [Documented] (LIB)",
"Go module 1.3.0, released 2026-09-23, after 1.0.0 on 2026-05-08 [Documented: repo googleapis/google-cloud-go@37f936ac] (GOCH; GOVER). C# package shown as pre-release 1.0.0-beta05 [Documented] (LIB). Versions of the Java, Node.js, PHP and Python libraries [Not disclosed] (LIB checked; install commands give no pin)",
"Same as the REST API [Inferred] (premise: the libraries wrap the same service methods)",
"API",
"Input and Output [Documented] (SAN has samples for sanitizing prompts and responses in each language)",
"Template; the endpoint is set per client, for example modelarmor.LOCATION.rep.googleapis.com [Documented] (TPL)",
"The Go apiv1 package defines the floor-setting integrated service AI_PLATFORM only; GOOGLE_MCP_SERVER appears in apiv1beta [Documented: repo googleapis/google-cloud-go@37f936ac] (GOPB1; GOPB1B). Docs samples import apiv1beta in one Go streaming sample and apiv1 elsewhere [Documented] (SAN)",
ALL]))
R.append(row([
"Google Cloud CLI: gcloud model-armor templates create and gcloud model-armor floorsettings describe and update [Documented] (TPL; FLR)",
"[Not disclosed] (no GA or Preview statement; checked TPL, FLR and RN)",
"Not applicable: configuration commands [Documented] (TPL; FLR). Whether gcloud can sanitize content [Not disclosed] (checked SAN, TPL and FLR; only REST and library samples are shown)",
"API (configuration only; no inline enforcement)",
"Not applicable",
"Both: templates create flags such as --rai-settings-filters and --pi-and-jailbreak-filter-settings-enforcement, and floorsettings update flags such as --full-uri and --add-integrated-services [Documented] (TPL; FLR)",
"Locations other than the default us multi-region need gcloud config set api_endpoint_overrides/modelarmor [Documented] (TPL)",
MARK]))
R.append(row([
"Terraform resources for Model Armor floor settings and templates [Documented] (RN 2025-07-29)",
"[Not disclosed] (the release note gives no GA or Preview label; the Terraform resource page was not read [To be verified])",
"Not applicable: configuration",
"API (infrastructure as code; no inline enforcement)",
"Not applicable",
"Both: floor settings and templates [Documented] (RN)",
"[To be verified] (resource page not read; fields and limits unknown)",
MARK]))
R.append(row([
"Gemini Enterprise Agent Platform, generateContent method, per request with a modelArmorConfig object or project-wide with floor settings [Documented] (VTX). The docs still say 'Gemini API in Vertex AI' for this method [Documented] (VTX; INT)",
"GA 2025-12-03 (Preview since 2025-07-29) [Documented] (RN)",
"Text only: documents and file uploads are not supported ('To screen documents, call the Model Armor REST API directly') [Documented] (VTX; INT)",
"Inline: Agent Platform calls Model Armor and enforces INSPECT_ONLY or INSPECT_AND_BLOCK [Documented] (VTX)",
"Input and Output: promptTemplateName for the prompt and responseTemplateName for the response [Documented] (VTX)",
"Both: templates per request or floor settings per project; request templates take precedence over floor settings, and floor settings use the Stable filter version by default [Documented] (VTX; FLR)",
"Gemini models, non-streaming [Documented] (INT). De-identified or masked data is not passed back; INSPECT_AND_BLOCK blocks instead [Documented] (VTX). Model Armor is skipped (fail-open) when it is unavailable, unreachable, errors, or is not present in the region [Documented] (VTX). Per-request template call supports europe-west1, europe-west2, europe-west3, asia-southeast1 and asia-south1 [Documented] (VTX)",
T18]))
R.append(row([
"Agent Gateway, Client-to-Agent (ingress) traffic to agents built with the Agent Development Kit (ADK) on Agent Runtime [Documented] (AGW)",
"Preview 2026-04-22, GA 2026-06-24 [Documented] (RN)",
"Text only; documents and file uploads are not supported [Documented] (INT; AGW)",
"Inline: Agent Gateway intercepts the request and the response and invokes Model Armor [Documented] (AGW)",
"Input and Output: client requests to the agent and agent responses to the client [Documented] (AGW)",
"Template only ('Only using templates'); the same template may serve ingress and egress [Documented] (INT; AGW)",
"Only reasoningEngines.streamQuery payloads of ADK agents are sent; non-ADK payloads such as LangChain are not [Documented] (AGW). Model Armor and the gateway must be in the same region [Documented] (AGW). Streaming sanitization is supported only for streamQuery on ADK agents [Documented] (AGW)",
T18]))
R.append(row([
"Agent Gateway, Agent-to-Anywhere (egress) traffic: A2A v1, MCP and OpenAI-format LLM services [Documented] (AGW)",
"Preview 2026-04-22, GA 2026-06-24 [Documented] (RN)",
"Text only [Documented] (INT)",
"Inline [Documented] (AGW)",
"Input and Output: agent requests to the external system and its responses back [Documented] (AGW)",
"Template only [Documented] (INT; AGW)",
"MCP: only tools/call and prompts/get requests and responses and tool execution errors are sanitized; tools/list, resources and notifications pass unsanitised [Documented] (AGW). A2A: only the v1 Send Message, Agent Card and Get Extended Agent Card operations are sanitized, over JSON-RPC and HTTP+JSON/REST bindings but not gRPC [Documented] (AGW). OpenAI format: chat completions (create, delete, get, list, update) and responses (create, get, delete) in non-streaming variants, get chat messages, OpenAI API errors, legacy completions, assistants, messages and threads, and embeddings create [Documented] (AGW). Everything not listed is allowed without sanitization [Documented] (AGW)",
MARK]))
R.append(row([
"Apigee API proxies with the SanitizeUserPrompt and SanitizeModelResponse policies [Documented] (APG; APU; APR). The Apigee samples repository names the same two policies [Documented: repo GoogleCloudPlatform/apigee-samples@2b1a9f00] (APSAMP)",
"[To be verified] (no GA or Preview label found on APG, APU or APR)",
"Text only [Documented] (INT)",
"Inline in the Apigee request flow and response flow; Apigee allows, blocks or redacts [Documented] (APG)",
"Input (SanitizeUserPrompt in the request flow) and Output (SanitizeModelResponse in the response flow) [Documented] (APG)",
"Template only; the policies name a Model Armor template [Documented] (INT; APG)",
"Needs an Intermediate or Comprehensive Apigee environment; Apigee and Model Armor should be in the same region; Model Armor token limits apply [Documented] (APG)",
T18]))
R.append(row([
"Gemini Enterprise: user prompts and assistant responses routed through Model Armor with a template [Documented] (GE; INT)",
"GA 2025-09-16 [Documented] (RN)",
"Text and documents on the INT options table [Documented] (INT). The GE page also lists images uploaded directly and images inside uploaded files, while INT says images embedded in documents are not screened [Documented] (GE; INT)",
"Inline: Gemini Enterprise acts on the verdict by blocking or allowing [Documented] (GE)",
"Input and Output: user inputs and assistant outputs [Documented] (GE)",
"Template only; the template must be in the same project and location as the Gemini Enterprise instance [Documented] (GE; INT)",
"No de-identification or masking: Gemini Enterprise blocks instead [Documented] (GE; INT). Custom agents (ADK, A2A, Dialogflow) are not screened [Documented] (GE). No token limits [Documented] (GE). A file or image that violates policy is discarded from the request [Documented] (GE)",
ALL]))
R.append(row([
"Google and Google Cloud MCP servers: sanitization of MCP tool calls and tool responses through floor settings [Documented] (MCPD)",
"Preview 2025-12-10, GA 2026-04-22 [Documented] (RN)",
"Text [Documented] (INT)",
"Inline: floor settings check requests sent to or from supported MCP servers [Documented] (FLR; MCPD)",
"Input and Output: tools/call and prompts/get requests and responses, plus MCP tool execution errors [Documented] (MCPD)",
"Floor setting only ('Only using floor settings'): integrated service GOOGLE_MCP_SERVER with an enforcement type and Cloud Logging flag [Documented] (INT; MCPD)",
"Do not enable the prompt injection and jailbreak filter unless MCP traffic carries natural language data [Documented] (MCPD). tools/list, resources, notifications, Streamable HTTP/SSE and protocol errors pass unsanitised [Documented] (MCPD). Floor settings do not apply to unsupported MCP servers; the supported-server list is in the MCP docs [Documented] (MCPD; MCPS). If agent and server are in different projects with floor settings in both, Model Armor is invoked twice [Documented] (MCPD)",
MARK]))
R.append(row([
"Service Extensions on Cloud Load Balancing (application load balancers), GKE Inference Gateway and Secure Web Proxy [Documented] (NET; INT)",
"Traffic extension on application load balancers incl. GKE Inference Gateway: Preview 2025-04-09; GKE integration GA 2025-09-15 [Documented] (RN). GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN and NET)",
"Text [Documented] (INT)",
"Inline: Service Extensions forward content to Model Armor, which tells the network service to allow, block or modify the traffic [Documented] (NET)",
"Input and Output: traffic to and from AI applications, MCP servers or models [Documented] (NET)",
"Template only [Documented] (INT). The template field customPromptSafetyErrorCode is described as returned to the end user by the service extension [Documented] (RT)",
"Requests to ExternalProcessor are limited to 600 queries per minute per project [Documented] (QUO). Covers OpenAI-format models, agents and MCP servers [Documented] (INT)",
T18]))
R.append(row([
"LangChain: ModelArmorSanitizePromptRunnable, ModelArmorSanitizeResponseRunnable and ModelArmorMiddleware in langchain-google-community 3.0.4 or later [Documented] (LC)",
"Preview [Documented] (LC)",
"Text only; for a document, only the extracted text is scanned [Documented] (LC)",
"API wrapper in the application (client side); a fail_open flag decides whether findings block [Documented] (LC)",
"Input (prompt runnable) and Output (response runnable); middleware applies them around agent tool use [Documented] (LC)",
"Template (project, location and template_id passed to the runnable) [Documented] (LC)",
"Changes the user makes to the response after the check are not filtered [Documented] (LC). An on_model_armor_finding event is dispatched for observability [Documented] (LC)",
T18]))
R.append(row([
"Security Command Center findings from Model Armor [Documented] (INT; SCCF)",
"[Not disclosed] (no GA or Preview label found on INT, SCCF or PRC)",
"Not applicable: findings and pricing tier, not a screening path",
"Reporting (not inline)",
"Not applicable",
"Floor settings: INT says a violation of a configured floor setting is blocked and a finding is sent to Security Command Center [Documented] (INT). The SCC findings page lists FLOOR_SETTINGS_VIOLATION (a template that fails floor-setting conformance, class Misconfiguration, Premium tier) as the Model Armor finding [Documented] (SCCF; Security Command Center docs, not Model Armor docs). The two descriptions differ",
"Model Armor is included in Security Command Center Enterprise and Premium tiers with a token allowance (see block e) [Documented] (PRC)",
MARK]))
R.append(row([
"Google Cloud console, Model Armor page: create templates, floor settings tab, monitoring tab [Documented] (TPL; FLR; MON)",
"[Not disclosed] (no GA or Preview label for the page). Console modality selection: Preview since 2026-07-01 [Documented] (RN)",
"Not applicable: configuration",
"API-side configuration (no inline enforcement)",
"Not applicable",
"Both: templates and floor settings. Floor settings UI is project-level only; organisation and folder floor settings need the API [Documented] (FLR)",
"The Select modality field is disabled for regions other than the us and eu multi-regions [Documented] (TPL)",
MARK]))
R.append(row([
"Monitoring dashboard (Cloud Monitoring) and Cloud Logging of sanitize and template operations [Documented] (MON; LOG)",
"Monitoring dashboard: Preview 2025-09-08, GA 2025-12-04 [Documented] (RN). Logging status [Not disclosed] (LOG checked)",
"Not applicable: reporting",
"Reporting (not inline)",
"Input and Output counts [Documented] (MON)",
"Template metadata flags logSanitizeOperations and logTemplateOperations; floor settings enableCloudLogging per integration [Documented] (LOG)",
"Cloud Monitoring metric types are request_count, pi_jb_request_count, rai_request_count, sdp_request_count, malicious_uri_request_count and used_token_count [Documented] (MON); the list has no CSAM or antivirus metric [Documented] (MON). Inspect only mode is useful only with Cloud Logging enabled [Documented] (OV)",
MARK]))
BLOCK_B=table(HB,R)
if __name__=="__main__":
    print(len(R))
