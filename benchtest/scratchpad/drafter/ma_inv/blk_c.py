from inv_common import *
HC=["Parameter","Where set (template metadata, filter config, floor setting, request)","Values","Default","Effect","Status (GA/Preview)","Source URL"]
GAI="GA [Inferred] (status rule S)"
R=[]
R.append(row([
"enforcementType (snake_case enforcement_type in some examples) [Documented] (RT; TPL)",
"Template metadata: templateMetadata.enforcementType. Floor setting: per integration (aiPlatformFloorSetting inspectOnly or inspectAndBlock; GOOGLE_MCP_SERVER enforcement type) [Documented] (RT; VTX; MCPD)",
"INSPECT_ONLY or INSPECT_AND_BLOCK; ENFORCEMENT_TYPE_UNSPECIFIED is the same as INSPECT_AND_BLOCK [Documented] (RT)",
"INSPECT_AND_BLOCK for templates [Documented] (TPL). For the gcloud floor-setting command that adds the Agent Platform integration, INSPECT_ONLY is the default [Documented] (VTX)",
"INSPECT_ONLY logs detections to Cloud Logging and does not block, so Cloud Logging must be enabled to gain value; INSPECT_AND_BLOCK returns a block verdict and the calling service or integration point is responsible for blocking [Documented] (OV)",
GAI]))
R.append(row([
"filterVersionSelector [Documented] (RT)",
"Template metadata: templateMetadata.filterVersionSelector with either version (for example v3) or alias. It takes precedence over the deprecated filterVersion fields in RaiFilterSettings and PiAndJailbreakFilterSettings [Documented] (RT)",
"Version string such as v1 to v4, or alias FILTER_VERSION_ALIAS_STABLE or FILTER_VERSION_ALIAS_LATEST; LEGACY and RETIRED cannot be set on new templates [Documented] (RT; FV)",
"No version means Stable; an unspecified alias resolves to STABLE; floor settings use Stable by default [Documented] (FV; RT)",
"One version per template, not per filter; does not affect the Sensitive Data Protection and malicious URL filters. Legacy lasts 90 days after a new Stable. Retirement of v1 and v2 is 2026-12-17 [Documented] (FV; RN 2026-09-18); an earlier release note of 2026-09-02 gave 2026-11-29 [Documented] (RN)",
GAI]))
R.append(row([
"multiLanguageDetection [Documented] (RT)",
"Template metadata: templateMetadata.multiLanguageDetection.enableMultiLanguageDetection. Request: multiLanguageDetectionMetadata with enableMultiLanguageDetection and optional sourceLanguage. Floor setting: console option or gcloud --enable-multi-language-detection [Documented] (RT; SAN; FLR)",
"true or false; sourceLanguage is a language code [Documented] (SAN)",
"False [Documented] (TPL)",
"If a source language is given, Model Armor uses it and does not auto-detect (behaviour changed 2026-02-27) [Documented] (SAN; RN). Not available in limited-support regions with data residency enforcement on [Documented] (FAR)",
GAI]))
R.append(row([
"modalities [Documented] (RT; TPL)",
"Template metadata: templateMetadata.modalities (a list); console field 'Select modality' [Documented] (RT; TPL)",
"MODALITY_TEXT, MODALITY_IMAGE; MODALITY_UNSPECIFIED sanitizes all modalities [Documented] (RT)",
"Empty: only text is scanned [Documented] (TPL; RT)",
"Setting a single modality makes the other return EXECUTION_SKIPPED; image modality works only in the us and eu multi-regions and the console field is disabled elsewhere [Documented] (SAN; TPL)",
"Preview [Documented] (TPL)"]))
R.append(row([
"dataResidencyCompliant [Documented] (RT)",
"Template metadata: templateMetadata.dataResidencyCompliant; console option 'Enforce data residency' [Documented] (RT; TPL)",
"true or false [Documented] (RT)",
"True for new templates [Documented] (RT; TPL)",
"True disables features not hosted in the template's jurisdiction. False allows cross-jurisdictional routing for in-use and in-transit data and enables all features except image modality, which stays us and eu only; data at rest remains compliant [Documented] (TPL; RN 2026-08-27)",
GAI]))
R.append(row([
"ignorePartialInvocationFailures [Documented] (RT)",
"Template metadata: templateMetadata.ignorePartialInvocationFailures; gcloud --template-metadata-ignore-partial-invocation-failures [Documented] (RT; TPL)",
"true or false [Documented] (RT)",
"[Not disclosed] (checked RT and TPL)",
"'If true, partial detector failures should be ignored.' The value is echoed in sanitizationMetadata; invocationResult PARTIAL means some filters were skipped or failed [Documented] (RT; RR)",
GAI]))
R.append(row([
"Custom error code and message fields: customPromptSafetyErrorCode, customPromptSafetyErrorMessage, customLlmResponseSafetyErrorCode, customLlmResponseSafetyErrorMessage [Documented] (RT)",
"Template metadata; gcloud --template-metadata-custom-prompt-safety-error-code and the message, llm-response variants [Documented] (RT; TPL)",
"Integer code and string message for the prompt side and for the LLM response side [Documented] (RT)",
"[Not disclosed] (checked RT and TPL)",
"Returned to the end user when the prompt or the LLM response trips Model Armor filters; the prompt-side code is described as returned by the service extension [Documented] (RT)",
GAI]))
R.append(row([
"logSanitizeOperations [Documented] (RT)",
"Template metadata: templateMetadata.logSanitizeOperations (log_sanitize_operations in some examples) [Documented] (RT; LOG)",
"true or false [Documented] (LOG)",
"False [Documented] (TPL)",
"Logs sanitize operations to Cloud Logging. LOG says the full content of prompts and responses is logged, while OV says event details 'might include metadata or snippets of the analyzed content as configured' [Documented] (LOG; OV). Cloud Logging is the only place content-related data is stored [Documented] (OV)",
GAI]))
R.append(row([
"logTemplateOperations [Documented] (RT)",
"Template metadata: templateMetadata.logTemplateOperations (log_template_operations in some examples) [Documented] (RT; LOG)",
"true or false [Documented] (LOG)",
"False [Documented] (TPL)",
"Logs create, update, read and delete operations on templates [Documented] (LOG)",
GAI]))
R.append(row([
"raiSettings [Documented] (RT)",
"Filter config: filterConfig.raiSettings.raiFilters[] with filterType and confidenceLevel [Documented] (RT)",
"filterType HATE_SPEECH, HARASSMENT, SEXUALLY_EXPLICIT, DANGEROUS; confidenceLevel LOW_AND_ABOVE, MEDIUM_AND_ABOVE, HIGH [Documented] (RT)",
"No categories until listed; level default is documented inconsistently (see block a) [Documented] (EXC; TPL; RT; FLR)",
"A positive match is reported at or above the configured level. CSAM is not in this list and cannot be turned off [Documented] (RT; OV)",
GAI]))
R.append(row([
"piAndJailbreakFilterSettings [Documented] (RT)",
"Filter config: filterConfig.piAndJailbreakFilterSettings.filterEnforcement and confidenceLevel [Documented] (RT)",
"ENABLED or DISABLED; confidenceLevel LOW_AND_ABOVE, MEDIUM_AND_ABOVE, HIGH [Documented] (RT)",
"Unspecified enforcement is Disabled; floor settings default the level to LOW_AND_ABOVE [Documented] (RT; FLR)",
"The level is used only if the filter is enabled [Documented] (RT). Advice on the level: Medium on OV, High on TPL [Documented] (OV; TPL)",
GAI]))
R.append(row([
"maliciousUriFilterSettings [Documented] (RT)",
"Filter config: filterConfig.maliciousUriFilterSettings.filterEnforcement [Documented] (RT)",
"ENABLED or DISABLED [Documented] (RT)",
"Unspecified is Disabled [Documented] (RT)",
"Scans the first 256 URLs; no confidence level [Documented] (OV)",
GAI]))
R.append(row([
"sdpSettings [Documented] (RT)",
"Filter config: filterConfig.sdpSettings.basicConfig.filterEnforcement or advancedConfig with inspectTemplate and deidentifyTemplate; the two are mutually exclusive [Documented] (RT)",
"Basic: ENABLED or DISABLED. Advanced: SDP resource names [Documented] (RT)",
"Unspecified basic enforcement is the same as Disabled [Documented] (RT)",
"Basic inspects a fixed infoType set; advanced runs InspectContent, or DeidentifyContent too when a de-identify template is given [Documented] (RT; OV)",
GAI]))
R.append(row([
"filterRuleSettings (template-specific exclusion rules) [Documented] (EXC)",
"Filter config: filterConfig.filterRuleSettings.ruleSets[] with filterTypes, and rules[].exclusionRule holding a dictionary wordList or a regex pattern plus matchingScope [Documented] (EXC). The REST FilterConfig reference lists only four settings and does not show this field [To be verified] (RT)",
"filterTypes PROMPT_INJECTION_AND_JAILBREAK or RESPONSIBLE_AI; matchingScope MATCHING_SCOPE_PARTIAL_MATCH or MATCHING_SCOPE_FULL_MATCH [Documented] (EXC)",
"Partial match is the default scope [Documented] (EXC)",
"A matching rule overrides MATCH_FOUND or EXECUTION_SKIPPED to NO_MATCH_FOUND for the whole filter type. Not supported in streaming APIs or floor settings; evaluated on raw text before translation or de-identification; applies only to its own template [Documented] (EXC)",
"Preview [Documented] (EXC; RN 2026-09-28)"]))
R.append(row([
"Floor-setting levels: organisation, folder, project [Documented] (FLR)",
"Floor setting resource organizations/ID, folders/ID or projects/ID with /locations/global/floorSetting, managed on the global endpoint modelarmor.googleapis.com; the console works at project level only [Documented] (FLR; DR)",
"Fields include filterConfig and enableFloorSettingEnforcement (false disables inherited settings) [Documented] (FLR)",
"Floor settings use the Stable filter version; RAI level default in the console is Medium and above; PI level default is LOW_AND_ABOVE [Documented] (FLR)",
"Template conformance: a template cannot be created or updated if it is less strict than the floor settings; the lower level wins (project over folder over organisation). Sensitive Data Protection settings are not checked for conformance. Role roles/modelarmor.floorSettingsAdmin [Documented] (FLR)",
GAI]))
R.append(row([
"Floor-setting inline enforcement: integratedServices, aiPlatformFloorSetting, googleMcpServerFloorSetting, enableCloudLogging [Documented] (FLR; LOG)",
"Floor setting at project level: integratedServices (list containing AI_PLATFORM), aiPlatformFloorSetting {inspectOnly or inspectAndBlock, enableCloudLogging}; gcloud --add-integrated-services=GOOGLE_MCP_SERVER, --google-mcp-server-enforcement-type and --enable-google-mcp-server-cloud-logging [Documented] (VTX; MCPD; LOG)",
"AI_PLATFORM (gcloud name VERTEX_AI) and GOOGLE_MCP_SERVER; enforcement INSPECT_ONLY or INSPECT_AND_BLOCK; enableCloudLogging true or false [Documented] (VTX; MCPD)",
"Console: sanitize logging on by default for Agent Platform and off by default for MCP servers [Documented] (LOG). Enforcement for Agent Platform via gcloud: INSPECT_ONLY [Documented] (VTX)",
"Applies Model Armor to Agent Platform generateContent calls and supported Google and Google Cloud MCP servers without code changes; Agent Platform floor settings do not apply to Agent Platform multi-regional endpoints [Documented] (FLR; DR)",
"Agent Platform: GA 2025-12-03. MCP servers: Preview 2025-12-10, GA 2026-04-22 [Documented] (RN)"]))
BLOCK_C=table(HC,R)
if __name__=="__main__":
    print(len(R))
