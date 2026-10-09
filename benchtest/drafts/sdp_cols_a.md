## Column SD1: Sensitive Data Protection: Sensitive-data detection in text (infoType inspection)
### R1
Summary: **Sensitive-data detection in text.** The inspect method scans a string, table or conversation for built-in information types, such as names, ID numbers and keys, and returns each match with a likelihood and position. It returns findings, not a verdict. **[Documented]**
Detail:
• Sensitive Data Protection (SDP) is described as a service that "helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud" (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Formerly Cloud DLP: the docs pages carry the banner "Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API)." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• The synchronous text method is `content.inspect`: "The content.inspect method of the DLP API lets you send data directly to the DLP API for inspection. The response contains the inspection findings." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• For text input the API "returns details about any infoTypes found in the text, a likelihood value, and offset information" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• A content item can be a string (`value`), a table, bytes (`byteItem`), a `conversation` or a `batchContentItem`, plus optional `contentMetadata` (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• Conversation support: "Added support for inspecting and de-identifying conversational content. You can now include a Conversation in your ContentItem requests." (release note dated 2026-06-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• Batch support: "Added support for inspecting and de-identifying batched content. You can now include a BatchContentItem in your ContentItem requests." (release note dated 2026-06-12; SDP docs, release notes, read 2026-10-09) **[Documented]**
• The overview lists LLM prompts as a use case: "Inspect and redact sensitive tokens (such as PII or credentials) from streaming API payloads, user forms, and LLM prompt inputs before storing the data." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• The text page suggests using findings for routing: "Classify text to extract infoTypes and likelihood ratings and use this information in custom workflows to route or flag high-risk messages." (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• `content.inspect` returns findings and not a verdict; the docs contrast it with content policies: "a content policy doesn't return a list of findings. Instead, a content policy returns a single ALLOW or BLOCK verdict." (SDP docs, content-policy overview page, read 2026-10-09) **[Documented]**
• The client response type `InspectContentResponse` has a single field `result` holding the findings, with no allow or block field (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:3175` "result (google.cloud.dlp_v2.types.InspectResult):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Any blocking, masking or logging decision after a finding is made by the calling application, since the response carries only findings (premise: the response fields above) **[Inferred]**
• The other way to inspect is an inspection or hybrid job: "The results of inspection and hybrid jobs are stored in Google Cloud." Jobs are outside this column (inventory only) (SDP docs, overview page, read 2026-10-09) **[Documented]**
### R2
Summary: **Personal, financial, health and credential data.** Built-in detectors cover names, contact details, government IDs for many countries including Singapore NRIC and passport numbers, card and bank numbers, health terms, and cloud and AI-provider keys. Language coverage is only broadly stated. **[Documented]**
Detail:
• An infoType is defined as "a type of sensitive data, such as a name, email address, telephone number, identification number, credit card number, and so on" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Built-ins "include detectors for country- or region-specific sensitive data types" as well as global ones such as person name, telephone number, email address and credit card number (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• The reference table "InfoType descriptions" has 522 name and description cells, which pairs to 261 infoTypes (counted from the fetched page text by pairing the two cells after the Name and Description header; Google gives no total) **[Inferred]**
• The reference says the list moves: "The Sensitive Data Protection team releases new infoType detectors and groups periodically. To get the latest list of built-in infoTypes, call the infoTypes.list method" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The reference has a location filter with 51 entries, GLOBAL plus 50 country names (counted from the fetched page text) **[Inferred]**
• The reference filters name these groups: Finance, Health, Communications, PII, SPII, Demographic, Credential, Government ID, Document and Contextual information (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Singapore NRIC: `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` is "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card." Availability is `ANY_LOCATION` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Singapore passport: `SINGAPORE_PASSPORT` is "A Singaporean passport number." Availability is `ANY_LOCATION` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The generic `PASSPORT` infoType matches passport numbers for a list of countries that includes "Russia, Singapore, Spain" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• No other Singapore-named infoType exists: searched the fetched reference text for the string singapor and found only the NRIC row, the passport row and the `PASSPORT` country list, so no FIN, UEN or address infoType is named (checked the reference and concepts pages) **[Not disclosed]**
• Whether the NRIC detector also covers FIN numbers is not stated; the description names only the NRIC card **[To be verified]**
• `PHONE_NUMBER` is described only as "A telephone number." with no country scope (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Whether Singapore +65 numbers are detected as `PHONE_NUMBER` is not stated and needs a test **[To be verified]**
• The reference has a secrets group: "The following infoType detectors detect credentials and other secret data." (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The secrets group lists 21 names (counted from the fetched page text by listing the entries between the Secrets heading and the Image-based infoTypes heading) **[Inferred]**
• LLM-provider keys are named infoTypes: `ANTHROPIC_API_KEY` ("API key used to authenticate requests to Anthropic APIs."), `GEMINI_API_KEY` and `OPENAI_API_KEY` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Release note dated 2026-08-13: "The ANTHROPIC_API_KEY, GEMINI_API_KEY, and OPENAI_API_KEY infoType detectors are available in all regions." (SDP docs, release notes, read 2026-10-09) **[Documented]**
• Other secrets in the same group include `AWS_CREDENTIALS`, `GCP_API_KEY`, `GCP_CREDENTIALS`, `JSON_WEB_TOKEN`, `OAUTH_CLIENT_SECRET`, `PASSWORD` and `HTTP_COOKIE` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• General infoTypes bundle many specific ones: "the GOVERNMENT_ID infoType detector alone includes more than 100 different infoType detectors" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Document-category infoTypes: "Sensitive Data Protection can classify documents into enterprise, sensitive, and regulated content categories." The `DOCUMENT_TYPE/CONTEXT/*` names include `OFFENSIVE` ("Content contains offensive topics."), `OBSCENE`, `POLITICS` and `SEXUAL` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The `DOCUMENT_TYPE/CONTEXT/*` infoTypes are listed as limited-availability, with the Availability column showing regional europe, global and us (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Whether the `DOCUMENT_TYPE/CONTEXT/*` classifiers run on a plain text string sent to `content.inspect`, rather than on whole documents, is not stated **[To be verified]**
• Languages: "Country-specific infoTypes support the English language and the respective country's languages. Most global infoTypes work with multiple languages." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• No per-infoType language table exists (checked the infoTypes concepts, reference and infoTypes.list pages) **[Not disclosed]**
• Chinese, Malay, Tamil and Singlish text support for global infoTypes such as `PERSON_NAME` is not stated and needs a test **[To be verified]**
• Context matters: "Many infoType detectors require contextual clues to be present before they identify a match." Google suggests `GENERIC_ID` or a custom infoType when clues are absent (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Out of purpose: the docs describe the product as discovering, classifying and de-identifying sensitive data and name no prompt-injection, jailbreak, toxicity or topic-drift detector (checked the overview, infoTypes concepts and reference pages); this is a scope judgement from that purpose statement **[Inferred]**
• The reference notes that "all other infoType detectors are text-based; when analyzing images, they first extract text from images and then analyze the text" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
### R3
Summary: **Any text string, table or conversation.** One request carries one content item; there is no input or output setting, so prompts, responses, retrieved text and tool inputs or outputs are all treated the same way. Requests are stateless and results are not stored. **[Inferred]**
Detail:
• The content item is one of `value`, `table`, `byteItem`, `conversation` or `batchContentItem` (mutually exclusive), plus `contentMetadata` (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The request body has only `inspectConfig`, `item`, `inspectTemplateName` and `locationId` (deprecated, "Deprecated. This field has no effect."), with no input or output flag (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• The client request type has the same fields: `parent`, `inspect_config`, `item`, `inspect_template_name`, `location_id` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:3144` "Deprecated. This field has no effect.") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• This column therefore applies equally to prompts, responses, retrieved text, tool inputs and tool outputs: the caller decides which text to send, and nothing in the request marks a direction (premise: the request fields above) **[Inferred]**
• Conversation: "The maximum number of messages allowed is 50k. The order of the messages is assumed to be chronological and will be used to index findings in the response." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• Each message has `messageType`, an optional `participantId` such as 'test-user' or 'gemini', and its text in `messageParts` (at most a single text item); `content` is marked deprecated (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The client at the tag has only `content`, `message_type` and `participant_id` on a message and no `messageParts` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1772` "class ConversationMessage(proto.Message):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• `participantId` is a free identifier, lowercase letters, numbers and hyphens, at most 63 characters; it is not a role field, so prompt versus response is not flagged (premise: the field description and the absence of a role enum in the client message type) **[Inferred]**
• `messageType` CONTEXT: "Message contains context only and will not have findings reported from it during inspection or redacted from it during de-identification." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The client enum has the same two values (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1799` "Message contains context only and will not") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No system prompt or user prompt is needed as context; the request has no such parameter (premise: the request and message fields above) **[Inferred]**
• Batch: `stringValueBatch` carries a list of strings: "Represents a batch of string values to inspect or redact." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• Table: "Up to 50,000 Values per request allowed." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• Inspecting as a table helps: "the structure and columns provide Sensitive Data Protection with additional clues that may enable it to provide better results for some use cases" (SDP docs, inspecting structured text page, read 2026-10-09) **[Documented]**
• Byte items: the client enum `ByteContentItem.BytesType` includes `TEXT_UTF8`, `WORD_DOCUMENT`, `PDF`, `POWERPOINT_DOCUMENT`, `EXCEL_DOCUMENT`, `AVRO`, `CSV` and `TSV` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1593` "TEXT_UTF8 (5):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The metadata-label page shows a `content.inspect` request that sends a PDF as `byteItem`, so file bytes are accepted on this method (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Statelessness: "Content methods are synchronous, stateless methods." and "Request data is encrypted in transit and is not stored." (SDP docs, method types page, read 2026-10-09) **[Documented]**
• Results: "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Templates are stored configuration, not stored data: a request may name an inspection template that lives in the project (SDP docs, templates page, read 2026-10-09) **[Documented]**
• For data outside Google Cloud the docs say to "use the API methods content.inspect and content.deidentify to scan the content" without "persisting the content outside of your local storage" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
### R4
Summary: **Rules, checksums, context and machine learning.** Built-in detectors combine pattern matching, checksum checks, context clues and machine learning. They run in a Google-hosted API with global or regional endpoints and client libraries. The service was formerly called Cloud DLP. **[Documented]**
Detail:
• Formerly Cloud DLP: the API keeps the old name, "Cloud Data Loss Prevention API (DLP API)", its host `dlp.googleapis.com`, the role `roles/dlp.user` and the package `google-cloud-dlp` (SDP docs, overview, API endpoints and roles pages, read 2026-10-09) **[Documented]**
• Techniques: "Sensitive Data Protection uses various techniques including pattern matching, checksum validation, machine learning, and context analysis." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Credit card example: Sensitive Data Protection "checks for known issuer prefixes, validates checksums, analyzes character lengths, and considers the context in which the potential credit card number appears" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• `PERSON_NAME` "attempts to detect, for example, names like Jane, Jane Smith, and Jane Marie Smith using various technologies, including natural language understanding" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• A name dictionary is part of `PERSON_NAME`: "A new version with an updated name dictionary is available for the PERSON_NAME infoType detector." (release note dated 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• The backing model, training data or dictionary contents for `PERSON_NAME` and other machine-learning detectors are not named (checked the infoTypes concepts, reference, likelihood, overview and release-note pages and the client repo) **[Not disclosed]**
• Likelihood comes from signals: "Likelihood is calculated based on the number of signals a finding has that implies that the finding matches the infoType." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Context moves a finding up or down: positive context raises and negative context lowers the likelihood, and a finding that fails a checksum may not be reported (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Versioning: release notes show `InfoType.version` values `stable`, `latest` and `legacy` and say a new `PERSON_NAME` version is promoted to stable "In 30 days" (release note dated 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• The client field is `version`: "Optional version name for this InfoType." (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:194`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Detector behaviour therefore changes between read dates without a product version, so findings for `PERSON_NAME` depend on the date and on the version setting (premise: the dated release notes) **[Inferred]**
• REST path: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/content:inspect`, and "The URLs use gRPC Transcoding syntax." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Global endpoint: "The global endpoint of Sensitive Data Protection is dlp.googleapis.com." Regional endpoints follow "dlp.REGION.rep.googleapis.com" (SDP docs, API endpoints page, read 2026-10-09) **[Documented]**
• Client libraries are listed for C#, Go, Java, Node.js, PHP, Python and Ruby (SDP docs, client libraries page, read 2026-10-09) **[Documented]**
• The Python package `google-cloud-dlp` is at version 3.40.0 at the pinned tag (`packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16` `__version__ = "3.40.0"`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client method is `inspect_content` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:872` "def inspect_content(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, content policy (separate resource, not part of this column by default): "A Sensitive Data Protection content policy is a reusable resource that you can use to evaluate content and determine whether to allow or block it based on its sensitivity." General availability is dated 2026-08-31 (SDP docs, content-policy overview and release notes, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 1: the overview promises "Get immediate, synchronous verdicts on content to enforce organizational data policies." (SDP docs, content-policy overview page, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 2a: the REST resource page for `projects.locations.contentPolicies` lists only the methods create, delete, get, list and patch (SDP docs, REST content policies page, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 2b: the client at the tag has `create_content_policy` and sibling methods with no evaluate method (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:7363` "def create_content_policy(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No documented way to submit an arbitrary string to a content policy was found (checked the content-policy, manage-policies and REST resource pages and the client methods) **[Not disclosed]**
• Cross-reference, Model Armor docs, not SDP docs: "Sensitive Data Protection can identify sensitive elements, context, and documents to help you reduce the risk of data leakage going into and out of AI workloads." Model Armor offers a basic and an advanced configuration (Model Armor overview, read 2026-10-09) **[Documented]**
• For how Model Armor calls SDP, see the Model Armor columns `Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)` and the matching Output-level column (provisional headers; ruling R012 keeps those internals out of this column) **[Inferred]**
• Open-source and managed-cloud analogues for comparison only: `Presidio: PII detection in text (Analyzer)` (provisional header) and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either **[Inferred]**
### R5
Summary: **Findings with a likelihood bucket, no verdict.** Each finding gives the information type, one of five likelihood levels, its position and an optional quote. A minimum-likelihood setting filters the list; the default is Possible. **[Documented]**
Detail:
• The sample response has `quote`, `infoType`, `likelihood`, `location` (`byteRange` and `codepointRange`) and `createTime` for each finding (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• The client `Finding` type has `quote`, `info_type`, `likelihood`, `location`, `create_time` and `quote_info`, and `InspectResult` has `findings` and `findings_truncated` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2016` "findings_truncated (bool):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Likelihood is bucketed, not numeric: "Sensitive Data Protection uses a bucketized representation of likelihood" with five levels VERY_UNLIKELY, UNLIKELY, POSSIBLE, LIKELY and VERY_LIKELY (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• VERY_LIKELY is "Characterized by having many strong signals for a given infoType." (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• Threshold: "Only returns findings equal to or above this threshold. The default is POSSIBLE." and "LIKELIHOOD_UNSPECIFIED | Default value; same as POSSIBLE." (SDP docs, REST InspectConfig and likelihood pages, read 2026-10-09) **[Documented]**
• Guidance is qualitative: POSSIBLE is "Useful if you want a balance of precision and recall." and VERY_UNLIKELY is "Useful if you need the highest recall. This minimum likelihood level generates the most noise." (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• No recommended minimum likelihood for LLM prompt or response screening is given (checked the likelihood, concepts, inspecting text and text redaction pages) **[Not disclosed]**
• Per-type thresholds: `minLikelihoodPerInfoType` exists "if you want to lower the precision for PERSON_NAME without lowering the precision for the other infotypes in the request" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Quotes are off by default: "Quotes are potentially sensitive, so by default Sensitive Data Protection does not include them in responses." Set `includeQuote` to receive them (SDP docs, quote page, read 2026-10-09) **[Documented]**
• In the client, a quote may be omitted for long findings (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2052` "exceeds 4096 bytes in length, the quote may be omitted.") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• `excludeInfoTypes`: "When true, excludes type information of the findings." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Conversation findings carry the message position through `ConversationLocation` with `message_index` or `all_messages` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2320` "class ConversationLocation(proto.Message):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Finding cap: if `maxFindingsPerRequest` is set in a content request, "the resulting maximum value is the value that you set or 3,000, whichever is lower." The value "isn't a hard limit" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• One string can produce several findings: "a single finding could match several types at lower likelihood" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Test data caution: "fake or sample data does not get reported because that fake or sample data is not passing enough checks to report" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Accuracy disclaimer: "Built-in infoType detectors are not a perfectly accurate detection method. For example, they can't guarantee compliance with regulatory requirements." (SDP docs, infoTypes concepts and reference pages, read 2026-10-09) **[Documented]**
• Published precision, recall or F1 for any built-in infoType, including Singapore NRIC, is not given (checked the infoTypes concepts, reference, likelihood, overview and release-note pages) **[Not disclosed]**
### R6
Summary: **A project, a location and a list of infoTypes.** Send the text, the information types to look for and an optional minimum likelihood. The caller needs billing, the API enabled and the DLP User role. Requests are capped at 0.5 MB and 3,000 findings. **[Documented]**
Detail:
• Parent: "Projects scope, no location specified (defaults to global): projects/{projectId}", or `projects/{projectId}/locations/{locationId}` to choose a processing location (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Config: `inspectConfig` overrides a named template: "Any configuration directly specified in inspectConfig will override those set in the template." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Name the infoTypes: "Always specify infoTypes explicitly. Do not use an empty infoTypes list." (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Default list, source 1: "If you don't specify any infoTypes, Sensitive Data Protection uses a default infoTypes list that is intended for testing purposes only." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Default list, source 2: "the system may automatically choose a default list of detectors to run, which may change over time." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Default list, source 3: "Otherwise, Sensitive Data Protection scans for a default set of infoTypes (ALL_BASIC)" (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• A 2019 release note says "Updated the default list of infotypes included in ALL_BASIC.", so the default set has changed before (release note dated 2019-02-11; SDP docs, release notes, read 2026-10-09) **[Documented]**
• Auth: the REST method requires "serviceusage.services.use" on the parent and the OAuth scope `https://www.googleapis.com/auth/cloud-platform` (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Role: `roles/dlp.user` is "Inspect, Redact, and De-identify Content" and its listed permissions are `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*` and `serviceusage.services.use` (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**
• Setup steps: "Verify that billing is enabled for your Google Cloud project." and `gcloud services enable dlp.googleapis.com` (SDP docs, JSON quickstart page, read 2026-10-09) **[Documented]**
• Credentials: "To authenticate to Sensitive Data Protection, set up Application Default Credentials." (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Content limits table (SDP docs, quotas and limits page, read 2026-10-09; the page says "Quotas and limits specified in this document are subject to change.") **[Documented]**
  – Maximum size of each request, except projects.image.redact | 0.5 MB
  – Maximum number of findings per request | 3,000
  – Maximum number of table values | 50,000
  – Maximum size of each quote (a contextual snippet, returned with findings, of the text that triggered a match) | 4 KB
  – Maximum number of built-in and custom infoTypes per request | 150
• Larger inputs: "If you need to inspect files that are larger than these limits, store those files on Cloud Storage and run an inspection job." (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Rate quotas: 10,000 requests per minute in total; 600 per minute per region for "Requests made to the global endpoint (dlp.googleapis.com) where a location is specified"; 100 per minute per region for "Requests made to a regional endpoint (dlp.REGION.rep.googleapis.com)" (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Quotas can be raised: "You can edit your quotas up to their maximum values on the Quotas & System Limits page for your project." (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Slower infoTypes: `PERSON_NAME`, `FEMALE_NAME`, `MALE_NAME`, `FIRST_NAME`, `LAST_NAME`, `DATE_OF_BIRTH`, `LOCATION`, `STREET_ADDRESS` and `ORGANIZATION_NAME` "can make requests run much more slowly than requests that do not include them" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Many infoTypes can be noisy: `DATE`, `TIME`, `DOMAIN_NAME` and `URL` "detect a broad range of findings and may not be useful to turn on" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Singapore: `asia-southeast1` is listed as Singapore with regional endpoint support "Yes" (SDP docs, locations page, read 2026-10-09) **[Documented]**
• Residency: regional endpoints "guarantee data residency by ensuring that your data at rest, in use, and in transit isn't moved out of the location specified by the endpoint", while for the global endpoint with a location "There is no guarantee that the data in transit remains in the processing region" (SDP docs, API endpoints page, read 2026-10-09) **[Documented]**
• Availability column: "The value ANY_LOCATION means that the infoType is available in all regions." (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Limited-availability infoTypes "can cause scanning issues if you use them to scan data in unsupported regions" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Pricing: content inspected costs "$0.00 (Free)" for the first gibibyte per month per account, then "$3.00" per gibibyte up to 1 tebibyte, then "$2.00"; "A minimum of 1 KB is billed per content inspect or transform request." (SDP pricing page, read 2026-10-09) **[Documented]**
• Availability objective: the SLA gives at least 99.5% monthly uptime for `content.inspect` in most regions and 99% in Mexico and Stockholm (Sensitive Data Protection SLA page, read 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, Application Default Credentials and the Python client or plain REST. Test on text with labelled character spans per information type, sweep the minimum likelihood, and re-run when detector versions change. **[Inferred]**
Detail:
• Minimum setup: one Google Cloud project with billing and the DLP API enabled, `roles/dlp.user` for the caller, Application Default Credentials, and either `pip install google-cloud-dlp` or plain REST calls to `content:inspect` in a chosen location, such as `asia-southeast1` (premise: the quickstart, roles, endpoint and library pages above) **[Inferred]**
• The first gibibyte of content inspected each month per account is free, so a small labelled test set costs nothing; billing information is still required: "Sensitive Data Protection requires billing information for all accounts before you can start using the service." (SDP pricing page, read 2026-10-09) **[Documented]**
• A cost warning is on the pricing page: "It is possible for costs to become very high, depending on the quantity of information that you instruct Sensitive Data Protection to scan." (SDP pricing page, read 2026-10-09) **[Documented]**
• The JSON quickstart gives the steps: create a project, enable billing, run `gcloud services enable dlp.googleapis.com` and grant `roles/dlp.user` (SDP docs, JSON quickstart page, read 2026-10-09) **[Documented]**
• No client library is required: "Sending JSON to Sensitive Data Protection REST endpoints does not require a client library." (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• The Python package is `google-cloud-dlp`, installed with `pip install google-cloud-dlp` (`packages/google-cloud-dlp/README.rst@google-cloud-dlp-v3.40.0:88` "pip install google-cloud-dlp") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Python version, source 1: the package needs Python 3.10 or later (`packages/google-cloud-dlp/setup.py@google-cloud-dlp-v3.40.0:95` `python_requires=">=3.10",`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Python version, source 2: the docs libraries page says "Samples are compatible with Python 2.7.x and 3.4 and higher." This refers to the samples, not the package, and looks out of date against the line above (SDP docs, client libraries page, read 2026-10-09) **[Documented]**
• Dependencies at the tag include `google-api-core[grpc] >= 2.28.0, <3.0.0` (`packages/google-cloud-dlp/setup.py@google-cloud-dlp-v3.40.0:45`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• A regional host for Singapore would be `dlp.asia-southeast1.rep.googleapis.com` (premise: the pattern "dlp.REGION.rep.googleapis.com" and `asia-southeast1` listed as supported) **[Inferred]**
• No offline or emulator mode exists in the docs or the client package (checked the overview, method types, libraries, endpoints and locations pages and the package README and docs folder); every test sends text to Google's API **[Not disclosed]**
• A web demo exists: "Sensitive Data Protection Demo is a web-based application that you can use to test built-in infoType detectors." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• There is no first-party evaluation toolkit for detection quality (checked the docs navigation, the quickstarts and the client repo); the docs say "Google recommends that you test your settings to make sure that your configuration meets your requirements." **[Not disclosed]**
• A labelled set needs ground-truth character spans per information type, plus negative near-misses; sweep the five minimum-likelihood levels and score each type separately (premise: findings carry type, bucket and range) **[Inferred]**
• Build positives that pass the checksum and context checks, because the docs say sample data that does not pass the checks is not reported (premise: the quoted behaviour in R5) **[Inferred]**
• Record the read date and the `InfoType.version` used: `PERSON_NAME` has a new version due to be promoted to stable about 30 days after 2026-10-03, so results may shift after about 2026-11-02 (premise: the dated release note) **[Inferred]**
• Test text leaves the tester's environment and is sent to Google's API; the docs say "Request data is encrypted in transit and is not stored." (SDP docs, method types page, read 2026-10-09) **[Documented]**
• For a large test set, the regional endpoint quota is 100 requests per minute per region, and each request is capped at 0.5 MB, so use the batch item or the global endpoint with a location (premise: the quotas in R6) **[Inferred]**
### R8
Summary: **Key open questions.** No published accuracy, recall or latency, unnamed backing models, per-language coverage, Singapore gaps (FIN, +65 phone), unclear default infoTypes, shifting person-name detector versions, and no verified way to apply a content policy to a string.
Detail:
• Accuracy, precision and recall for each infoType, for Singapore NRIC and passport and by language (checked the infoTypes concepts, reference, likelihood, overview and release-note pages and the client repo; none published; needs testing)
• Latency and throughput per request size and infoType set (checked the same pages, the limits page and the SLA; only an availability objective and a warning that some infoTypes are slow; needs measuring)
• Backing model or dictionary for `PERSON_NAME` and the document-category classifiers (checked the same pages; not stated)
• Per-infoType language coverage for Singlish, Chinese, Malay and Tamil text (checked the concepts and reference pages; one general sentence only; needs testing)
• Whether `PHONE_NUMBER` finds +65 numbers, and whether the NRIC detector covers FIN, including how it treats the check letter (checked the reference; not stated; needs testing)
• Which infoTypes run when none are listed: three pages give three wordings (testing-only default list, a list that may change, ALL_BASIC); the exact membership was not read from the API (read-only rule; needs `infoTypes.list` or a test)
• Effect of the `PERSON_NAME` version change on a fixed test set before and after promotion to stable (needs two test runs)
• Whether `DOCUMENT_TYPE/CONTEXT/*` classifiers work on a short plain-text string and in `asia-southeast1`; the Availability column shows europe, global and us (needs testing)
• Whether CONTEXT messages in a conversation improve detection in the other messages or are only ignored for findings (checked the REST ContentItem page; not stated; needs testing)
• Batch item behaviour: whether the 0.5 MB request cap and the 3,000-finding cap apply to the whole batch or per string (checked the REST ContentItem and limits pages; not stated)
• Content-policy evaluation: the REST resource and client have no evaluate method, but the roles page lists the permission `dlp.contentPolicies.apply` (also in `roles/dlp.user`) and a role described as "Apply content policies."; how a caller applies a policy to a string outside Gemini Enterprise is unknown (checked the content-policy, manage-policies, roles and REST resource pages and the client; needs a Gemini Enterprise check)
• Customer-data terms: whether content sent to the API can be used by Google beyond serving the request (not read; the docs say only that request data "is not stored")
• Per-method quotas not shown on the public limits page, and whether the listed limits change (the page says they are subject to change)
### R9
Summary: Google Cloud Sensitive Data Protection docs pages (read 2026-10-09), its pricing and SLA pages, and the pinned google-cloud-python client source at the google-cloud-dlp 3.40.0 tag.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/quote
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
• https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api
• https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/libraries
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions
• https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy
• https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://cloud.google.com/sensitive-data-protection/sla
• https://docs.cloud.google.com/model-armor/overview
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/storage.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/setup.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/README.rst
## Column SD2: Sensitive Data Protection: Custom detectors and inspection rules (custom infoTypes)
### R1
Summary: **Your own detectors and rules on top of the built-ins.** A request can add word-list, regular-expression, large-dictionary and metadata-label detectors, plus rules that exclude findings or raise or lower their likelihood. They run inside the same inspect call. **[Documented]**
Detail:
• Custom detectors are a documented option: "Sensitive Data Protection contains many built-in infoType detectors, but you can also create your own." (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• The overview lists the kinds of custom detector (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
  – "Regular custom dictionary detectors are simple word and phrase lists that Sensitive Data Protection matches on."
  – "Large custom dictionary detectors are generated by Sensitive Data Protection using large lists of words or phrases stored in either Cloud Storage or BigQuery."
  – "Regular expression (regex) detectors let Sensitive Data Protection detect matches based on a regular expression pattern."
  – "Metadata label detectors let Sensitive Data Protection detect matches based on the presence of specific metadata."
  – "Surrogate infoType detectors detect output from Sensitive Data Protection de-identification transformation CryptoReplaceFfxFpeConfig."
• Surrogate detectors exist only to reverse format-preserving encryption in `content.reidentify`, so they belong to the reversible-tokenisation column and are not described further here (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Custom detectors are set in `InspectConfig.customInfoTypes` and work in `projects.content.inspect` among other places: "Inspection using projects.content.inspect." (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• A custom detector can extend a built-in one: "CustomInfoType can either be a new infoType, or an extension of built-in infoType, when the name matches one of existing infoTypes and that infoType is specified in content.inspect.info_types field." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Inspection rules refine any detector: "Inspection rules help refine the scan results that the Sensitive Data Protection returns by modifying the detection mechanism of a given infoType detector." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Three rule types exist (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
  – "Exclusion rules, which help exclude false or unwanted findings."
  – "Hotword rules, which help detect additional findings in text content."
  – "Adjustment rules, which help adjust the likelihood of findings based on the context in which they appear."
• Large dictionaries are not inline: "Each large custom dictionary has two components" and "The dictionary files are stored in Cloud Storage and include a copy of the source phrase data plus bloom filters, which aids searching and matching." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Metadata-label detectors are recent: "You can configure Sensitive Data Protection to detect specific metadata labels in your content." (release note dated 2026-03-07), "…specific client-provided metadata." (2026-03-28) and "…specific file labels, which can represent Google Drive labels or Microsoft sensitivity labels." (2026-06-29) (SDP docs, release notes, read 2026-10-09) **[Documented]**
• Image-based rules arrived through release notes: "Image-based exclusion rules, which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings." (general availability note dated 2026-02-23); they are covered in the image columns (SDP docs, release notes, read 2026-10-09) **[Documented]**
### R2
Summary: **Organisation-specific terms, formats and labels.** Dictionaries match fixed word lists, regular expressions match formats such as internal IDs, metadata detectors match classification labels, and rules cut false positives or add context. The user creates and owns these detectors. **[Documented]**
Detail:
• Detectors are user-made: "Custom infoType detectors are detectors that you create yourself." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Dictionaries: "You can use a custom dictionary as a detector or as an exception list for built-in detectors." (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Dictionary use case: they "are useful when you want to scan for a list of words or phrases that are not easily matched by a regular expression or a built-in detector." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Regex use case: "suppose that you had medical record numbers in the form ###-#-#####." (SDP docs, custom regex page, read 2026-10-09) **[Documented]**
• Metadata use case: "This feature lets you use your existing classification taxonomies for content inspection and policy enforcement." (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Layering: "Combine metadata label detection with standard infoType detection for a multi-layered approach." (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Exclusion rules target noise: "You want to exclude duplicate scan matches in results that are caused by overlapping infoType detectors." and "You're experiencing noise in your scan results." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Hotword purpose: "A hotword rule instructs Sensitive Data Protection to adjust the likelihood of a finding, depending on whether a hotword occurs near that finding." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**
• Adjustment rules: "Adjustment rules can help you refine detection accuracy by increasing (also called boosting) or decreasing the likelihood values of findings based on the context in which they appear." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• The rules do not speed scans: "The methods described in this topic are not intended to speed scans, but they can help lessen noise by reducing the volume of output and the number of findings stored." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Singapore gaps in the built-ins (no FIN, UEN or address infoType) could be filled by a user-written regex or dictionary, but nothing in the docs says Google tests such detectors (premise: the regex and dictionary definitions; see the detection column for the built-in gaps) **[Inferred]**
• Out of purpose: dictionaries and regexes match literal text, so they hold no semantic model of prompt injection, jailbreaks or toxicity; a list of known attack phrases would only catch exact matches (premise: the dictionary and regex definitions) **[Inferred]**
• Words in a dictionary use Unicode letters and digits, so Chinese, Malay and Tamil words can be listed; whether a short word inside a longer unspaced run is found follows the "different type" boundary rule and is untested (premise: the matching rules quoted in R4) **[Inferred]**
### R3
Summary: **Same inputs as inspection, with rules per detector.** Custom detectors and rules sit in the inspect request's configuration, so they run on the same strings, tables, conversations and files, with no input or output setting. Only large dictionaries need stored resources. **[Inferred]**
Detail:
• Where custom detectors are set: "You specify a CustomInfoType in the InspectConfig object when configuring the following:" inspection with `projects.content.inspect`, inspection jobs, inspection templates, `projects.content.deidentify`, de-identification templates and `projects.content.reidentify` (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• The content item is the same as for built-in inspection: string, table, bytes, conversation or batch (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The request has no input or output flag, so custom detectors apply to prompts, responses, retrieved text, tool inputs and tool outputs alike, as in the detection column (premise: the request fields in the REST inspect page) **[Inferred]**
• Detection rules apply to some detector kinds only: "Only supported for the dictionary, regex, and storedType CustomInfoTypes." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Surrogate detectors take no rules: "This CustomInfoType does not support the use of detectionRules." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Rule sets do not apply to key-value metadata detectors: "Not supported for the metadataKeyValueExpression CustomInfoType." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Metadata-label detectors list "Inspection rule sets" and "De-identification transformations" under "Unsupported configurations" (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Client-provided metadata works on this method: "Scan metadata that your client application passes alongside the content, even if the metadata isn't embedded in the file." and "The following example shows a content.inspect request that includes both a PDF file and client-provided metadata." (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Supported metadata formats are Google Drive labels, Microsoft sensitivity labels on DOCX, PDF, PPTX and XLSX, and client-provided metadata (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• The content item carries the client metadata as `contentMetadata.properties` key-value pairs: "User provided key-value pairs of content metadata." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• Tables: "For record inspection of tables, column names are considered hotwords." and the `windowBefore` value "should be set to 1 if the hotword needs to be included in a column header." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Hotword windows: "The total length of the window cannot exceed 1000 characters." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Image rules do nothing on text: "This rule is silently ignored if the content being inspected is not an image." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Statelessness: inline dictionaries, regexes and rules travel in the request, while a stored infoType is a project resource, with its term list and generated dictionary files kept in Cloud Storage (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
### R4
Summary: **Literal matching, then rule passes.** Dictionary and regex detectors match text, each with a base likelihood. Hotword, exclusion and adjustment rules then raise, lower or drop findings by nearby text or overlap with other findings. **[Documented]**
Detail:
• Dictionary matching: "Dictionary words are case-insensitive." and "The characters surrounding any match must be of a different type (letters or digits) than the adjacent characters within the word." (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Dictionary characters: all characters other than Unicode Basic Multilingual Plane letters, digits and other alphabetic characters "are considered as whitespace when scanning for matches" (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Dictionary warning: "Dictionary words containing characters in the Supplementary Multilingual Plane of the Unicode standard can yield unexpected findings." (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Regex: "A Regex object consisting of a single pattern defining the regular expression." (SDP docs, custom regex page, read 2026-10-09) **[Documented]**
• Regex syntax: a code sample on the docs says "// Refer https://github.com/google/re2/wiki/Syntax for creating regular expression." The guide text itself names no regex engine (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**
• Base likelihood: "Defaults to VERY_LIKELY if not specified." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Hotword rules shift the likelihood: "Increase or decrease the likelihood by the specified number of levels." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Hotword example: "123-4-56789 would match as POSSIBLE. MRN 123-4-56789 would match as VERY_LIKELY." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**
• Exclusion by infoType overlap: "InfoType list in ExclusionRule rule drops a finding when it overlaps or contained within with a finding of an infoType from this list." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Adjustment by overlap: "Only MATCHING_TYPE_PARTIAL_MATCH is supported:" for `adjustByMatchingInfoTypes` (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• `exclusionType`: "A finding of this custom info type will be excluded from final results, but can still affect rule execution." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Rule order, source 1: "Sensitive Data Protection applies the rules in the order you specify them in the ruleset." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Rule order, source 2: "Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Rule order, context: release note dated 2026-02-23 puts "Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset" at general availability, so the REST text may be older (premise: the dated release note) **[Inferred]**
• Stored dictionaries rebuild in place: "Any scans that you run while the stored infoType is in pending state will be run using the old version of the stored infoType." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Key-value metadata detectors use two regexes: "The regular expression for the key. Key should be non-empty." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Dictionary size, source 1: "Use small custom dictionary detectors when you have a list of up to several tens of thousands of words or phrases." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Dictionary size, source 2: "Use regular custom dictionary detectors when you have at most several hundred thousand words." (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• The client at the tag has the same fields: `metadata_key_value_expression`, `file_label_info_type` and `exclusion_type` on `CustomInfoType` (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:334` "metadata_key_value_expression (google.cloud.dlp_v2.types.CustomInfoType.MetadataKeyValueExpression):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client has the image-rule enum value (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:676` "MATCHING_TYPE_RULE_SPECIFIC (4):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Model Armor: the metadata page says to "create an advanced Sensitive Data Protection configuration in Model Armor that references this custom metadata label detector" (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
### R5
Summary: **Same findings as inspection, under your detector name.** A custom match returns the name you chose and a likelihood you set, Very likely unless changed, after any rules have run. There is no verdict. **[Documented]**
Detail:
• Findings carry the custom name: the `infoType` field is the "name of the custom infoType detector" and the result uses the same finding shape as built-in inspection (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Base likelihood: if the likelihood field is omitted, the custom infoType detector "defaults to VERY_LIKELY" (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Rules then alter it: "Rules are applied in the order that they are specified." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• A relative adjustment is capped: "Likelihood may never drop below VERY_UNLIKELY or exceed VERY_LIKELY" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• A detector can be silent: with `EXCLUSION_TYPE_EXCLUDE` it "will not cause a finding to be returned. It still can be used for rules matching" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Sensitivity score is for profiling only: "If unset for a CustomInfoType, it will default to HIGH. This only applies to data profiling." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Metadata findings: "The finding's MetadataType for MetadataLocation is populated based on whether the match is embedded in the file (CONTENT_METADATA) or provided by the client (CLIENT_PROVIDED_METADATA)." (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Threshold guidance: "If you notice a regex custom infoType detector returning too many false positives, try reducing the base likelihood and using detection rules to boost the likelihood using contextual information." (SDP docs, custom regex page, read 2026-10-09) **[Documented]**
• The minimum-likelihood setting from the detection column applies to the final likelihood of a custom match (premise: the REST text says the system "only returns" findings at or above the threshold, with per-type thresholds available) **[Inferred]**
• No verdict is produced; the caller acts on findings (premise: the response shape is the same as built-in inspection) **[Inferred]**
• Accuracy of a custom detector depends on the user's list or pattern; Google publishes no precision or recall for custom detectors (checked the custom infoType, dictionary, regex, rules and likelihood pages) **[Not disclosed]**
### R6
Summary: **A CustomInfoType object inside the inspect request.** Give a name, a dictionary, regex or stored reference, an optional base likelihood and rules. Limits per request include 30 custom detectors, 10 regular dictionaries, 10 rule sets and 1000-character regexes. **[Documented]**
Detail:
• Parts of the object: a name in an `InfoType` object, one detector body (`dictionary`, `regex`, `storedType`, `metadataKeyValueExpression`, `fileLabelInfoType` or `surrogateType`), and optional `likelihood`, `detectionRules` and `sensitivityScore` (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Custom infoType limits (SDP docs, quotas and limits page, read 2026-10-09; the page says its limits "are subject to change") **[Documented]**
  – Maximum number of custom infoTypes per request | 30
  – Maximum number of built-in and custom infoTypes per request | 150
  – Maximum number of regular custom dictionaries per request | 10
  – Maximum size of word list passed directly in the request message per regular custom dictionary | 128 KB
  – Maximum size of word list specified as a file in Cloud Storage per regular custom dictionary | 512 KB
  – Maximum combined size of all stored custom dictionaries per request | 5 MB
  – Maximum length of regular expressions | 1000
  – Maximum number of detection rules per custom infoType | 5
• Rule limits in a content request (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
  – Maximum number of inspection rules per set | 10
  – Maximum number of inspection rule sets per inspection configuration | 10
• Stored infoType limits (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
  – Maximum number of stored infoTypes | 30
  – Maximum size of a single input file stored in Cloud Storage | 200 MB
  – Maximum number of input table rows in BigQuery | 5,000,000
  – Maximum size of output files | 500 MB
• Phrase components: "Maximum number of components (continuous sequences containing only letters, only digits, only non-letter characters, or only non-digit characters) per regular custom dictionary phrase | 40" (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Request-level caps from the detection column (0.5 MB, 3,000 findings, 50,000 table values) still apply (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• A large dictionary needs a term list first: either "a text file within Cloud Storage or a column in a BigQuery table", then a stored infoType with an output location (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Warning: "Do not alter custom dictionary files directly in Cloud Storage." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• A stored infoType is ready to use when "the status of the infoType shows Ready." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Custom detectors may also be kept in an inspection template named by `inspectTemplateName`, with request fields overriding the template (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• The caller's role `roles/dlp.user` lists only `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*` and `serviceusage.services.use`; whether reading a stored infoType needs another permission is not stated (SDP docs, roles and permissions page, read 2026-10-09) **[To be verified]**
• Auth, location and billing are as for built-in inspection (see the detection column) (premise: same method and parent) **[Inferred]**
### R7
Summary: **Minimum setup:** the same project, billing, DLP User role and credentials as built-in inspection. An inline dictionary, regex or hotword rule needs nothing else; a large dictionary also needs a Cloud Storage bucket. Test each rule with matched and near-miss strings, in each language you care about, and compare findings with and without rules. **[Inferred]**
Detail:
• Minimum setup: the project, billing, API and `roles/dlp.user` from the detection column, plus a request that carries a `customInfoTypes` list or `ruleSet`; no extra resource is created for inline detectors (premise: the REST fields and the overview page) **[Inferred]**
• A large dictionary needs a Cloud Storage bucket and a folder where the generated dictionary is written (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• The Python client has the custom-detector types (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:338` "file_label_info_type (google.cloud.dlp_v2.types.CustomInfoType.FileLabelInfoType):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• A sample inline dictionary request is on the docs page, for example a room-name word list of RM-Orange, RM-Yellow and RM-Green (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Test design: a labelled set of true matches and near-misses per detector, run once with no rules and once with each rule, to measure what the rule removes or boosts (premise: rules change only likelihood or presence) **[Inferred]**
• Test the boundary and case rules: words next to digits, letters or unspaced scripts, and mixed case (premise: the matching rules in R4) **[Inferred]**
• Test metadata detectors with a content item that carries `contentMetadata` key-value pairs and check that the finding location type reads client-provided metadata (premise: the metadata page example) **[Inferred]**
• No first-party tool tests custom detectors; the docs say only "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Cost and data handling match built-in inspection: content inspected is billed in bytes with the first gibibyte per month free, and request data "is not stored" (SDP docs, pricing and method types pages, read 2026-10-09) **[Documented]**
### R8
Summary: **Key open questions.** Which regex engine and syntax limits apply, conflicting dictionary and rule-order statements, permissions for stored infoTypes, behaviour on unspaced scripts, and no published accuracy for custom detectors.
Detail:
• Regex engine and unsupported constructs: only a docs code-sample comment points to RE2 syntax (checked the custom regex, overview and limits pages; needs testing)
• Dictionary capacity: two pages give "several tens of thousands" and "several hundred thousand" words, while the limits page gives 128 KB inline and 512 KB from Cloud Storage (needs a test with a real word list)
• Rule order: the guide says rules apply in the order written, the REST text says exclusion rules run last, and a 2026-02-23 release note announces enhanced ordering (needs a test of mixed rule sets)
• Whether `roles/dlp.user` is enough to use a stored infoType in `content.inspect` (checked the roles page; the listed permissions do not name stored infoTypes; needs a permission test)
• Behaviour of dictionaries and regex word boundaries on Chinese, Malay and Tamil text (checked the dictionary page; needs testing)
• Size limits for `contentMetadata` and how many labels a request may carry (checked the ContentItem and limits pages; not stated)
• Whether custom detectors can match across messages in a `Conversation`, or only within one message (checked the ContentItem page; not stated; needs testing)
• Region availability of metadata-label detectors and image rules (checked the locations and metadata pages; not stated)
• Accuracy, latency and recall for custom detectors, and the effect of many custom detectors on latency (checked the custom infoType, rules and limits pages; none published; needs measuring)
### R9
Summary: Google Cloud Sensitive Data Protection docs pages on custom infoTypes, rules, limits and release notes (read 2026-10-09), and the pinned google-cloud-python client source at the google-cloud-dlp 3.40.0 tag.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex
• https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect
• https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/storage.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
## Column SD3: Sensitive Data Protection: Sensitive-data masking and de-identification in text
### R1
Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method finds sensitive values, then redacts, replaces, masks, buckets, date-shifts or hashes them. It returns the item in the same format, plus a summary of what changed. **[Documented]**
Detail:
• Scope: "Sensitive Data Protection can de-identify sensitive data in text content, including text stored in container structures such as tables." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Definition: "De-identification is the process of removing identifying information from data. The API detects sensitive data such as personally identifiable information (PII), and then uses a de-identification transformation to mask, delete, or otherwise obscure the data." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• The method is `content.deidentify`: "To de-identify sensitive data, use Sensitive Data Protection's content.deidentify method." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Output shape: "The API returns the same items you gave it, in the same format, but any text identified as containing sensitive information according to your criteria has been de-identified." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• The transformation reference groups the techniques (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
  – "Redaction: Deletes all or part of a detected sensitive value."
  – "Replacement: Replaces a detected sensitive value with a specified surrogate value."
  – "Date shifting: Shifts sensitive date values by a random amount of time."
  – "Time extraction: Extracts or preserves specified portions of date and time values."
• The docs table lists 12 transformation objects: `RedactConfig`, `ReplaceValueConfig`, `ReplaceDictionaryConfig`, `ReplaceWithInfoTypeConfig`, `CharacterMaskConfig`, `CryptoHashConfig`, `CryptoReplaceFfxFpeConfig`, `CryptoDeterministicConfig`, `FixedSizeBucketingConfig`, `BucketingConfig`, `DateShiftConfig` and `TimePartConfig` (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• The two reversible crypto transformations (`CryptoReplaceFfxFpeConfig`, `CryptoDeterministicConfig`) are covered in the reversible-tokenisation column, not here (premise: the footnote "Reversible transformations can be reversed to re-identify the sensitive data using the content.reidentify method." in the transformation table) **[Inferred]**
• LLM use is named: "Mask sensitive text before external processing: De-identify or redact sensitive tokens from text strings synchronously before passing content to third-party APIs or large language models (LLMs)." (SDP docs, method types page, read 2026-10-09) **[Documented]**
• Prompt use is named: "Mask confidential data in generative AI prompts: Redact proprietary or regulated information from user prompts before sending content to public or third-party LLMs." (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• Automatic redaction is contrasted with findings: "Automatic redaction produces an output with sensitive data matches removed instead of giving you a list of findings." (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• De-identification in storage is a separate job path: "Create a de-identified copy of Cloud Storage data using an inspection job." It is outside this column (inventory only) (SDP docs, overview page, read 2026-10-09) **[Documented]**
### R2
Summary: **Sensitive values leaving for LLMs, logs and third parties.** It addresses exposure of personal, financial, health and credential data that the detectors can find, by removing or disguising the value. It does not judge content such as attacks or toxicity. **[Inferred]**
Detail:
• Detection uses the same built-in and custom infoTypes as the detection column; see that column for the taxonomy, Singapore ID types, language statements and LLM-provider key detectors (premise: `inspectConfig` is part of the de-identify request) **[Inferred]**
• Use cases on the text page: "Sanitize user input before database persistence", "Sanitize customer service transcripts and logs" and masking prompts for LLMs (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• Techniques named in the overview: "Various transformation methods are available, including masking, redaction, bucketing, date shifting, and tokenization." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Date shifting use: "Obfuscate patient admission and discharge dates to meet HIPAA Safe Harbor de-identification requirements while preserving temporal intervals between events." (SDP docs, date shifting page, read 2026-10-09) **[Documented]**
• No compliance guarantee: "You must decide what data is sensitive and how to best protect it." and detectors "can't guarantee compliance with regulatory requirements" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Re-identification risk is a separate service: "The risk analysis service lets you analyze structured BigQuery data to identify and visualize the risk that sensitive information will be revealed (re-identified)." It is inventory only (SDP docs, overview page, read 2026-10-09) **[Documented]**
• A value is changed only if a detector finds it, so a miss stays in the text; residual leakage therefore follows the detection recall, which is not published (premise: the three-part call in R4) **[Inferred]**
• Out of purpose: transformations replace or hide values and do not detect prompt injection, jailbreaks, toxicity or off-topic content (checked the overview, transformation reference and de-identifying pages; this is a scope judgement) **[Inferred]**
### R3
Summary: **Any text item, with no input or output setting.** The caller sends a string, table, conversation or batch and gets the same item back with values changed. Prompts, responses, retrieved text and tool outputs are all handled the same way, and nothing is stored. **[Inferred]**
Detail:
• The item is treated as text: "The item to de-identify. Will be treated as text." and it "must be of type Table if your deidentifyConfig is a RecordTransformations object." (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• Support for conversations and batches: "Added support for inspecting and de-identifying conversational content." (release note dated 2026-06-03) and "Added support for inspecting and de-identifying batched content." (2026-06-12) (SDP docs, release notes, read 2026-10-09) **[Documented]**
• The supported-file-types table shows "De-identify content" only against CSV or TSV and plain-text file types, with no transformation entry for PDF, Word, Excel or PowerPoint and "Redaction" against image types (SDP docs, supported file types page, read 2026-10-09) **[Documented]**
• Conversation messages of type CONTEXT are never changed: they "will not have findings reported from it during inspection or redacted from it during de-identification." (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The request has `deidentifyConfig`, `inspectConfig`, `item`, `inspectTemplateName`, `deidentifyTemplateName` and a deprecated `locationId`, with no input or output flag (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• The client request has the same fields (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2908` "The item to de-identify. Will be treated as text.") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The column therefore applies to prompts before they reach a model; applying it to model responses, retrieved text or tool outputs is the same call on different text, though only the prompt use is named in the docs (premise: no direction flag; LLM prompt use quoted in R1) **[Inferred]**
• Statelessness: "Content methods are synchronous, stateless methods." and "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, method types and overview pages, read 2026-10-09) **[Documented]**
• For text outside Google Cloud the docs say to use `content.inspect` and `content.deidentify` "to classify findings and pseudonymize content without persisting the content outside of your local storage" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Record transformations act on tables and can suppress whole records: "you can also instruct Sensitive Data Protection to de-identify data by simply suppressing records when certain suppression conditions evaluate to true." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
### R4
Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Each detected value is then redacted, replaced, masked, bucketed or date-shifted. **[Documented]**
Detail:
• Three parts: "The data to inspect", "What to inspect for" and "What to do with the inspection findings", the last being the `DeidentifyConfig` (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Detection is required: "An InspectConfig object is required in your request, with one exception." The exception is record transformations (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Two transformation categories: "InfoTypeTransformations: Transformations that are only applied to values within submitted text that are identified as a specific infoType." and RecordTransformations for tabular data (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• No infoType listed: "not specifying at least one infoType in an InspectConfig argument causes the transformation to apply to all built-in infoTypes that don't have a transformation provided. Doing so is not recommended, as it can cause decreased performance and increased cost." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Redaction: `RedactConfig` "Redacts a value by removing it." and the sample output leaves a gap: "My name is Alicia Abernathy, and my email address is ." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace with a value: `ReplaceValueConfig` "Replaces each input value with a given value." and the sample gives "My name is Alicia Abernathy, and my email address is [fake@example.com]." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace with the infoType name: `ReplaceWithInfoTypeConfig` "Replaces an input value with the name of its infoType." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace from a list: `ReplaceDictionaryConfig` "Replaces an input value with a value that is randomly selected from a word list." so output can vary between calls (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Character mask: `CharacterMaskConfig` "Masks a string either fully or partially by replacing a given number of characters with a specified fixed character." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Bucketing: "Sensitive Data Protection can bucket numerical input values based on fixed size ranges" (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Date shift and time part: `DateShiftConfig` "Shifts dates by a random number of days, with the option to be consistent for the same context." and `TimePartConfig` "Extracts or preserves a portion of Date, Timestamp, and TimeOfDay values." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash, source 1: the table says `CryptoHashConfig` "Replaces input values with a 32-byte hexadecimal string generated using a given data encryption key." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash, source 2: the same page's text says Sensitive Data Protection "outputs a base64-encoded representation of the hashed input value in the place of the original value." and "This transformation can't be reversed." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash scope: "Currently, only string and integer values can be hashed." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Input-type cells: redact, replace, mask and both bucketing objects read "Any"; the crypto hash reads "Strings or integers"; date shift and time part read "Dates/Times" (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• The date-shift, time-extraction and bucketing code samples use record (table) transformations and a context field; whether they work on infoType findings in free text is not stated (SDP docs, transformation reference page, read 2026-10-09) **[To be verified]**
• Transformation errors: the client `DeidentifyConfig` has `transformation_error_handling`, "Mode for handling transformation errors. If left" unspecified the default is `ThrowError`; the alternative is `LeaveUntransformed` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5449` "Mode for handling transformation errors. If left") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client has all 12 transformation classes and the `DeidentifyConfig` choice of `info_type_transformations`, `record_transformations` or `image_transformations` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5433` "Treat the dataset as free-form text and apply") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client method is `deidentify_content` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:1060` "def deidentify_content(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Endpoints are the same as for inspection: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/content:deidentify` (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• Templates: a de-identification template can be named in `deidentifyTemplateName`; the docs list "Apply the same de-identification or inspection policies across both real-time content API calls and scheduled storage repository scans" as a use (SDP docs, templates page, read 2026-10-09) **[Documented]**
• Cross-reference, Model Armor docs, not SDP docs: "Model Armor streaming methods don't support Sensitive Data Protection de-identification." and "Sensitive Data Protection de-identification is not supported for file-based prompts." (Model Armor sanitize page, read 2026-10-09) **[Documented]**
• For how Model Armor invokes SDP de-identification, see the Model Armor columns `Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)` and the matching Output-level column (provisional headers; ruling R012) **[Inferred]**
• Open-source and managed-cloud analogues for comparison only: `Presidio: PII anonymisation and masking in text (Anonymizer)` (provisional header) and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either **[Inferred]**
### R5
Summary: **The transformed item and a summary of changes.** The response holds the item with sensitive values changed, plus the bytes transformed and, per transformation, the infoType, count and result code. Over 3,000 findings returns an error message. **[Documented]**
Detail:
• Response parts: the client `DeidentifyContentResponse` has `item` ("The de-identified item.") and `overview` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2972` "The de-identified item.") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The sample response has `overview.transformedBytes` and `transformationSummaries` with `infoType`, `transformation`, `results` (a `count` and a `code` such as SUCCESS) and `transformedBytes` (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Result codes at the tag are SUCCESS and ERROR, with a `details` string for warnings or errors (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6895` "class TransformationResultCode(proto.Enum):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No findings list or original values are returned in the response fields (premise: the two response fields above) **[Inferred]**
• Only the requested infoTypes are changed: in the sample, a request for `EMAIL_ADDRESS` returns "My name is Alicia Abernathy, and my email address is [email-address]." with the name untouched (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Masking sample: with '#' and ignored common characters, the sample returns "My name is Alicia Abernathy, and my email address is ##########@#######.###." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Too many findings: "If your request has more than 3,000 findings, Sensitive Data Protection returns the following message: Too many findings to de-identify. Retry with a smaller request." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Partial results: "The list of findings that Sensitive Data Protection returns is an arbitrary subset of all findings in the request. To get all of the findings, break up your request into smaller batches." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Finding limits do not help here: `FindingLimits` is "not used for de-identification or data profiling." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• No verdict is returned; the caller decides whether to send the cleaned text on (premise: the response fields above) **[Inferred]**
• Billing follows `transformedBytes`: "Simple redaction, which includes the RedactConfig and ReplaceWithInfoTypeConfig transformations, is not counted against the number of bytes transformed when infoType inspection is also configured." (SDP pricing page, read 2026-10-09) **[Documented]**
• Published accuracy, residual-leak rate or utility measurements for de-identification are not given (checked the de-identifying, transformation reference, text redaction, likelihood and concepts pages) **[Not disclosed]**
### R6
Summary: **Data, detection settings and a transformation for each infoType.** Send the item, an inspect configuration and either a de-identify configuration or a template name. Limits include 0.5 MB per request, 100 transformations and 3,000 findings. The DLP User role covers it. **[Documented]**
Detail:
• Parent and location are as for inspection: `projects/{projectId}` or `projects/{projectId}/locations/{locationId}` (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• Config precedence: "Items specified here will override the template referenced by the deidentifyTemplateName argument." (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• Transformations are mandatory: "You must specify one or more transformations when you set the de-identification configuration" (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Mask options: `maskingCharacter`, `numberToMask`, `reverseOrder` and `charactersToIgnore`; "This transformation also works with number types such as long integers." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Limits for content requests (SDP docs, quotas and limits page, read 2026-10-09; the page says they "are subject to change") **[Documented]**
  – Maximum number of transformations per request | 100
  – Maximum size of each request, except projects.image.redact | 0.5 MB
  – Maximum number of findings per request | 3,000
  – Maximum number of table values | 50,000
• Auth and role: `roles/dlp.user` is "Inspect, Redact, and De-identify Content"; the method needs `serviceusage.services.use` on the parent (SDP docs, roles and REST pages, read 2026-10-09) **[Documented]**
• Rate quotas are the same as for inspection: 10,000 requests per minute in total, with per-region limits for regional and located global-endpoint requests (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Pricing: content transformed is "$0.00 (Free)" for the first gibibyte per month, then "$2.00" per gibibyte to 1 tebibyte, then "$1.00"; `content.deidentify` can also incur inspection charges, and "A minimum of 1 KB is billed per content inspect or transform request." (SDP pricing page, read 2026-10-09) **[Documented]**
• The crypto transformations note: "When you use Cloud KMS for cryptographic operations, charges apply." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Availability objective: at least 99.5% monthly uptime for `content.deidentify` in most regions and 99% in Mexico and Stockholm (Sensitive Data Protection SLA page, read 2026-10-09) **[Documented]**
• Regions: Singapore `asia-southeast1` is listed with regional endpoint support (SDP docs, locations page, read 2026-10-09) **[Documented]**
### R7
Summary: **Minimum setup:** the same project, billing, API, DLP User role and credentials as inspection. Send labelled prompts with known sensitive spans, de-identify them, then inspect the output for leftovers and check whether the model still answers well. Include a case over the finding cap. **[Inferred]**
Detail:
• Minimum setup: a Google Cloud project with billing and the DLP API enabled, `roles/dlp.user`, Application Default Credentials and either `pip install google-cloud-dlp` or REST calls to `content:deidentify` (premise: the quickstart, roles and library pages cited in the detection column) **[Inferred]**
• Transformed bytes are free for the first gibibyte per month per account, and inspection bytes are billed separately (SDP pricing page, read 2026-10-09) **[Documented]**
• Residual-leak test: run `content.deidentify` on labelled prompts, then run `content.inspect` on the output and count findings that remain (premise: the two methods share detectors) **[Inferred]**
• Utility test: compare an LLM answer on the cleaned prompt with the answer on the original, for a mask, a fixed replacement and an infoType-name replacement (premise: the transformations differ in what they leave in the text) **[Inferred]**
• Include prompts with more than 3,000 findings, tables and conversations with CONTEXT messages (premise: the limits and behaviours in R3 to R6) **[Inferred]**
• No offline or emulator mode and no first-party evaluation toolkit for de-identification were found (checked the overview, method types, libraries and de-identifying pages and the client package) **[Not disclosed]**
• The docs say to test: "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Request data is encrypted in transit and not stored, but test text is sent to Google's API (SDP docs, method types page, read 2026-10-09) **[Documented]**
• The Python package needs Python 3.10 or later (`packages/google-cloud-dlp/setup.py@google-cloud-dlp-v3.40.0:95` `python_requires=">=3.10",`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Record the read date and detector versions, since detectors change without a product version (see the detection column) **[Inferred]**
### R8
Summary: **Key open questions.** No published residual-leak or accuracy figures, unclear hash output format, whether bucketing, date shift and time part work on free text, how overlapping findings are resolved, and behaviour near the 3,000-finding cap.
Detail:
• Residual leakage after de-identification across infoTypes and languages, including Singapore NRIC (checked the de-identifying, transformation reference and concepts pages; none published; needs testing)
• Hash output format: the table says 32-byte hexadecimal and the text says base64 for `CryptoHashConfig` (needs a test)
• Whether `FixedSizeBucketingConfig`, `BucketingConfig`, `DateShiftConfig` and `TimePartConfig` apply to infoType findings in free text, or only to table fields (checked the transformation reference; samples use records; needs testing)
• How overlapping findings of different infoTypes are transformed when both have a transformation (checked the de-identifying and transformation reference pages; not stated; needs testing)
• Whether the 3,000-finding cap counts across all messages of a conversation or all strings of a batch, and whether a partial result is returned or only the error message (needs testing)
• Whether `LeaveUntransformed` error handling is reachable from REST and documented outside the client (checked the docs pages; only the client describes it)
• Latency and throughput for long prompts and many transformations (checked the pages above and the SLA; none published; needs measuring)
• Effect on LLM answer quality of each replacement style (needs testing; no Google guidance found)
• Whether CONTEXT messages affect detection in neighbouring messages (checked the ContentItem page; not stated)
• Customer-data terms: whether content sent to the API can be used by Google beyond serving the request (not read; the docs say only that request data "is not stored")
### R9
Summary: Google Cloud Sensitive Data Protection docs pages on de-identification and transformations (read 2026-10-09), its pricing and SLA pages, the Model Armor sanitize page, and the pinned google-cloud-python client source at the google-cloud-dlp 3.40.0 tag.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data
• https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-text-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text
• https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig
• https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://cloud.google.com/sensitive-data-protection/sla
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/setup.py
