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
Summary: **Key open questions.** No published accuracy, recall or latency, unnamed backing models, per-language coverage, Singapore gaps (FIN, +65 phone), unclear default infoTypes, shifting PERSON_NAME versions, and no verified way to apply a content policy to a string.
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
