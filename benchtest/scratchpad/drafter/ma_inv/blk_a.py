from inv_common import *
HA=["Filter","Config key","Levels or options","Default","Applies to (Input/Output)","Result field","Limit","Status (GA/Preview/Not documented)","Covered by Table 3 column","Source URL"]
GAI="GA [Inferred] (status rule S)"
R=[]
R.append(row([
"Responsible AI (RAI) safety filter: hate speech, harassment, sexually explicit and dangerous content [Documented] (OV)",
"filterConfig.raiSettings.raiFilters[] with filterType HATE_SPEECH, HARASSMENT, SEXUALLY_EXPLICIT or DANGEROUS and a confidenceLevel [Documented] (RT). To enable the filter, configure at least one category in raiSettings.raiFilters [Documented] (EXC)",
"LOW_AND_ABOVE, MEDIUM_AND_ABOVE or HIGH; a positive match is reported when detection confidence is equal to or greater than the configured level [Documented] (RT). The console also lists None, meaning no content is detected [Documented] (TPL). Google calls Low and above 'Not recommended for general responsible AI content categories' [Documented] (OV)",
"Not stated consistently. Templates page (console note): High when no level is given [Documented] (TPL). REST reference: an unspecified level is the same as LOW_AND_ABOVE, and for RAI the system uses 'a reasonable default level based on the filterType' [Documented] (RT). Floor-settings page (console note): Medium and above [Documented] (FLR). Effective default of a template [To be verified] (needs testing)",
"Input and Output: sanitizeUserPrompt with userPromptData and sanitizeModelResponse with modelResponseData both return an rai result [Documented] (SAN)",
"filterResults key rai holds raiFilterResult: executionState, messageItems, matchState and raiFilterTypeResults (sexually_explicit, hate_speech, harassment, dangerous, each with matchState) [Documented] (RR). A numeric score field [Not disclosed] (searched RR for a score field; the schema has enums only)",
"65,536 tokens (about 262,144 characters); above that the filter returns EXECUTION_SKIPPED with the message 'Detection skipped as token limit exceeded.' [Documented] (QUO). Real-time streaming is unlimited and the Gemini Enterprise integration has no token limit [Documented] (QUO; GE)",
GAI,
cov(1,2)]))
R.append(row([
"Child sexual abuse material (CSAM) filter [Documented] (OV)",
"No config key: FilterConfig lists raiSettings, sdpSettings, piAndJailbreakFilterSettings and maliciousUriFilterSettings only [Documented] (RT). The Go v1 FilterConfig has the same four fields [Documented: repo googleapis/google-cloud-go@37f936ac] (GOPB1)",
"No levels: 'You can set confidence levels only for prompt injection and jailbreak detection and responsible AI safety filters.' [Documented] (OV)",
"Always on: 'This filter is applied by default and cannot be turned off.' [Documented] (OV)",
"Input and Output: the OV use case covers user inputs and model outputs, and both SAN example responses include a csam result [Documented] (OV; SAN)",
"filterResults key csam holds csamFilterFilterResult with executionState, messageItems and matchState [Documented] (RR)",
"65,536 tokens, same EXECUTION_SKIPPED behaviour as the RAI filter [Documented] (QUO). Not available in limited-support regions when data residency enforcement is on (see block d) [Documented] (FAR)",
GAI,
cov(1,2)]))
R.append(row([
"Prompt injection and jailbreak detection [Documented] (OV)",
"filterConfig.piAndJailbreakFilterSettings with filterEnforcement (ENABLED or DISABLED) and confidenceLevel [Documented] (RT)",
"Confidence LOW_AND_ABOVE, MEDIUM_AND_ABOVE or HIGH. Google's advice differs: the example strategy says to set Medium (High for Gemini Enterprise) [Documented] (OV), while the templates page says 'We recommend that you set the confidence level to High' [Documented] (TPL). The overview also calls Low and above potentially suitable for high-stakes categories such as this one [Documented] (OV)",
"Filter is off unless filterEnforcement is ENABLED (unspecified means Disabled) [Documented] (RT). Confidence level when not given: floor settings default to LOW_AND_ABOVE [Documented] (FLR); the REST reference treats an unspecified level as LOW_AND_ABOVE [Documented] (RT)",
"Input and Output: OV says the filter 'scans prompts and responses for malicious content' [Documented] (OV). TPL describes detection 'in a prompt' [Documented] (TPL). The sanitizeModelResponse example output includes a pi_and_jailbreak result [Documented] (SAN)",
"filterResults key pi_and_jailbreak holds piAndJailbreakFilterResult with executionState, messageItems, matchState and confidenceLevel [Documented] (RR)",
"65,536 tokens (EXECUTION_SKIPPED above that) and a three-word minimum: fewer than three words returns NO_MATCH_FOUND [Documented] (QUO; OV). Exclusion rules (Preview) can suppress false positives for this filter [Documented] (EXC)",
GAI,
cov(3,4)]))
R.append(row([
"Malicious URL detection [Documented] (OV)",
"filterConfig.maliciousUriFilterSettings.filterEnforcement (ENABLED or DISABLED) [Documented] (RT)",
"On or off only: no confidence level [Documented] (OV). Not affected by filter versions [Documented] (FV)",
"Off unless ENABLED (unspecified means Disabled) [Documented] (RT)",
"Input and Output: the filter scans URLs in prompts and responses [Documented] (OV); both SAN example responses include a malicious_uris result [Documented] (SAN)",
"filterResults key malicious_uris holds maliciousUriFilterResult with executionState, messageItems, matchState and maliciousUriMatchedItems (uri and locations; locations are supported only for PLAINTEXT_UTF8 content) [Documented] (RR)",
"First 256 URLs only: extraction stops at 256 URLs or the end of the payload; token limits do not apply [Documented] (QUO; OV). Not available in limited-support regions when data residency enforcement is on [Documented] (FAR)",
GAI,
cov(7,8)]))
R.append(row([
"Sensitive Data Protection (SDP), basic configuration [Documented] (OV)",
"filterConfig.sdpSettings.basicConfig.filterEnforcement (ENABLED or DISABLED; unspecified is the same as Disabled) [Documented] (RT)",
"Fixed infoTypes, inspection only, no SDP templates [Documented] (OV; RT). The overview lists six categories (credit card number, US SSN, financial account number, US ITIN, Google Cloud credentials, Google Cloud API key) [Documented] (OV). The sanitize page lists CREDIT_CARD_NUMBER, FINANCIAL_ACCOUNT_NUMBER, GCP_CREDENTIALS, GCP_API_KEY and PASSWORD for all regions, plus US_SOCIAL_SECURITY_NUMBER and US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER for US-based regions [Documented] (SAN). Count differs: six categories on OV and RT, seven infoTypes on SAN [Documented] (OV; RT; SAN)",
"Off unless ENABLED [Documented] (RT)",
"Input and Output: OV describes redacting sensitive data in prompts and model responses [Documented] (OV); the basic infoType list on SAN is written for the prompt [Documented] (SAN)",
"filterResults key sdp holds sdpFilterResult.inspectResult with executionState, messageItems, matchState, findings[], findingsTruncated and extractedImageText [Documented] (RR)",
"130,000 tokens [Documented] (QUO)",
GAI,
cov(5,6)]))
R.append(row([
"Sensitive Data Protection (SDP), advanced configuration [Documented] (OV)",
"filterConfig.sdpSettings.advancedConfig.inspectTemplate and optional deidentifyTemplate, given as SDP resource names projects/PROJECT/locations/LOCATION/inspectTemplates/NAME and deidentifyTemplates/NAME [Documented] (RT)",
"Inspect only when just an inspect template is given (SdpFinding list returned); inspect plus de-identify when a de-identify template is also given, and every infoType in the de-identify template must be in the inspect template [Documented] (RT). SDP templates must be in the same location as the Model Armor template [Documented] (SAN)",
"Off unless configured [Documented] (RT)",
"Input and Output [Documented] (OV; SAN). De-identified text is returned in deidentifyResult.data.text and is not passed back by the Gemini Enterprise or Agent Platform integrations, which block instead [Documented] (TPL; GE; VTX)",
"sdpFilterResult.inspectResult, deidentifyResult (data, transformedBytes, infoTypes) or redactResult (redactedImage, findings, extractedImageText), at most one per response [Documented] (RR)",
"130,000 tokens [Documented] (QUO). Not supported: streaming de-identification, de-identification of file-based prompts [Documented] (SAN). If the SDP templates are in another project, the Model Armor service agent needs roles/dlp.user and roles/dlp.reader there [Documented] (TPL; SAN)",
GAI,
cov(5,6)]))
R.append(row([
"Antivirus scanning [Documented] (FAR; RR)",
"No config key found: FilterConfig has no antivirus setting [Documented] (RT). How antivirus is switched on [To be verified] (checked OV, TPL, SAN, FLR, FAR and RN; no configuration page found)",
"No confidence level in the result type [Documented] (RR). ScannedContentType values UNKNOWN, PLAINTEXT and PDF, with the note 'PDF Scanning for only PDF is supported.' [Documented] (RR)",
"[Not disclosed] (checked OV, TPL, SAN, FLR, FAR and RN)",
"Prompts and responses per the product page text 'within AI prompts and responses' [Documented] (PROD). Which request fields carry files for this filter [To be verified]",
"FilterResult has virusScanFilterResult with executionState, messageItems, matchState, scannedContentType, virusDetails[] (vendor, names, threatType) and scannedSize [Documented] (RR). The filterResults key list on RR does not name an antivirus key [Documented] (RR). Release note 2026-04-10: virusDetails no longer carries security-vendor names or threat signatures [Documented] (RN)",
"[Not disclosed] (no antivirus-specific size or token limit; checked QUO, OV and RR). The general 4 MB file limit is documented but not tied to this filter [Documented] (QUO)",
"Not documented: no GA or Preview statement found [Not disclosed] (checked RN, FAR, RR, OV). Listed as a filter for full-support regions only [Documented] (FAR)",
MARK]))
R.append(row([
"Image text extraction (optical character recognition, OCR) [Documented] (OV)",
"filterConfig is unchanged; templateMetadata.modalities includes MODALITY_IMAGE (MODALITY_UNSPECIFIED means all modalities) and the request sets byteItem byteDataType IMAGE [Documented] (RT; SAN). A separate OCR switch [Not disclosed] (checked OV, TPL, SAN, RT)",
"Method listed as 'Optical character recognition (OCR): Screens the text within images.' [Documented] (OV). Which filters run on the text follows the template: 'depending on the filter configuration' [Documented] (RT)",
"Modalities empty means text only [Documented] (TPL; RT)",
"Prompts and responses per OV [Documented] (OV). Only a sanitizeUserPrompt image example is shown; the response-side request shape [To be verified] (checked SAN)",
"Extracted text is returned in extractedImageText inside the SDP inspect and redact results [Documented] (RR). The SAN image example shows csam and sdp results [Documented] (SAN)",
"JPEG, PNG and BMP only; 4 MB or smaller; one image per request; images embedded in files are not screened; text plus image in one request is not supported by SanitizeUserPrompt and SanitizeModelResponse; us and eu multi-regions only (a regional endpoint without image support returns invocation_result FAILURE) [Documented] (OV)",
"Preview [Documented] (OV; RN 2026-06-25)",
cov(10)]))
R.append(row([
"Image visual scanning (advanced SDP filter only) [Documented] (OV)",
"Advanced SDP config with an inspect template and, for redaction, a de-identify template that has image redaction configured; modalities includes MODALITY_IMAGE [Documented] (SAN; RT)",
"'Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter.' [Documented] (OV). The BASIC_AUTH_HEADER infoType may be reported in advanced mode even if the inspect template does not include it [Documented] (SAN)",
"Off unless modalities, the advanced SDP config and the de-identify template are set [Documented] (SAN; TPL)",
"Prompts and responses per OV; only the prompt-side request is shown [Documented] (OV; SAN). Response-side request shape [To be verified]",
"redactResult with redactedImage (base64), findings (only when include_findings is true in the SDP template) and extractedImageText; finding locations carry image bounding boxes [Documented] (RR)",
"Same image limits as OCR: JPEG, PNG, BMP, 4 MB, one image, us and eu only [Documented] (OV)",
"Preview [Documented] (OV; RN 2026-06-25)",
cov(5,6,10)]))
R.append(row([
"Document text extraction and screening of files [Documented] (OV)",
"No separate switch: the request sets byteItem byteDataType to PLAINTEXT_UTF8, PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT or CSV, and the field is required because 'Model Armor doesn't automatically detect the file type' [Documented] (SAN). Modality TEXT scans text embedded in supported file formats [Documented] (TPL)",
"Formats: PDF, CSV, TXT, DOCX, DOCM, DOTX, DOTM, PPTX, PPTM, POTX, POTM, POT, XLSX, XLSM, XLTX, XLTM [Documented] (OV). Documents are screened for safety, prompt injection and jailbreak, sensitive data and malicious URLs [Documented] (OV). Rich documents with specific metadata labels can be sanitized through a custom metadata-label infoType in advanced SDP (release note 2026-04-06) [Documented] (RN)",
"Text only unless modalities says otherwise [Documented] (TPL)",
"Input documented (userPromptData byteItem examples); response-side file requests [To be verified] (SAN shows no modelResponseData file example)",
"Same filter results as text; the malicious URL locations field is supported only for PLAINTEXT_UTF8 [Documented] (RR; OV)",
"4 MB (larger files are skipped); files under 69 bytes are rejected with InvalidDocumentInputException; extracted text is subject to the token limits [Documented] (QUO; OV). No SDP de-identification for file-based prompts [Documented] (SAN)",
GAI,
cov(9)]))
BLOCK_A=table(HA,R)
if __name__=="__main__":
    print(len(R)); print(BLOCK_A[:600])
