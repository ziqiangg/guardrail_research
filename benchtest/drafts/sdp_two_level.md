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
• The reference table "InfoType descriptions" has 522 name and description cells, which pairs to 261 infoTypes (premise: one name cell and one description cell per infoType, paired after the Name and Description header in the page text; Google gives no total) **[Inferred]**
• The reference says the list moves: "The Sensitive Data Protection team releases new infoType detectors and groups periodically. To get the latest list of built-in infoTypes, call the infoTypes.list method" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The reference has a location filter with 51 entries, GLOBAL plus 50 country names (premise: the filter list on the reference page, counted in the page text) **[Inferred]**
• The reference filters name these groups: Finance, Health, Communications, PII, SPII, Demographic, Credential, Government ID, Document and Contextual information (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Singapore NRIC: `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` is "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card." Availability is `ANY_LOCATION` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Singapore passport: `SINGAPORE_PASSPORT` is "A Singaporean passport number." Availability is `ANY_LOCATION` (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The generic `PASSPORT` infoType matches passport numbers for a list of countries that includes "Russia, Singapore, Spain" (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• No other Singapore-named infoType is named in the reference: a search of the reference text for the string singapor found only the NRIC row, the passport row and the `PASSPORT` country list, so no FIN, UEN or address infoType is named (checked the reference and concepts pages) **[Not disclosed]**
• Whether the NRIC detector also covers FIN numbers is not stated; the description names only the NRIC card **[To be verified]**
• `PHONE_NUMBER` is described only as "A telephone number." with no country scope (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• Whether Singapore +65 numbers are detected as `PHONE_NUMBER` is not stated and needs a test **[To be verified]**
• The reference has a secrets group: "The following infoType detectors detect credentials and other secret data." (SDP docs, infoType detector reference page, read 2026-10-09) **[Documented]**
• The secrets group lists 21 names (premise: the entries listed between the Secrets heading and the Image-based infoTypes heading, counted in the page text) **[Inferred]**
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
• Purpose: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Out of purpose: the docs name no prompt-injection, jailbreak, toxicity or topic-drift detector (checked the overview, infoTypes concepts and reference pages); a scope judgement (premise: the purpose sentence above) **[Inferred]**
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
• The metadata-label page shows a `content.inspect` request that sends a PDF as a `byteItem` of type `PDF` (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• PDF byte items are accepted by `content.inspect`; which other file types are accepted is not stated per method (premise: the documented example; the supported-file-types table has no per-method column) **[Inferred]**
• Statelessness: "Content methods are synchronous, stateless methods." and "Request data is encrypted in transit and is not stored." (SDP docs, method types page, read 2026-10-09) **[Documented]**
• Results: "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Templates are stored configuration, not stored data: a request may name an inspection template that lives in the project (SDP docs, templates page, read 2026-10-09) **[Documented]**
• For data outside Google Cloud the docs say to "use the API methods content.inspect and content.deidentify to scan the content" without "persisting the content outside of your local storage" (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
### R4
Summary: **Rules, checksums, context and machine learning.** Built-in detectors combine pattern matching, checksum checks, context clues and machine learning. They run in a Google-hosted API with global or regional endpoints and client libraries. **[Documented]**
Detail:
• Formerly Cloud DLP: the API keeps the old name, "Cloud Data Loss Prevention API (DLP API)", its host `dlp.googleapis.com`, the role `roles/dlp.user` and the package `google-cloud-dlp` (SDP docs, overview, API endpoints and roles pages, read 2026-10-09) **[Documented]**
• Techniques: "Sensitive Data Protection uses various techniques including pattern matching, checksum validation, machine learning, and context analysis." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Credit card example: Sensitive Data Protection "checks for known issuer prefixes, validates checksums, analyzes character lengths, and considers the context in which the potential credit card number appears" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• `PERSON_NAME` "attempts to detect, for example, names like Jane, Jane Smith, and Jane Marie Smith using various technologies, including natural language understanding" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• A name dictionary is part of `PERSON_NAME`: "A new version with an updated name dictionary is available for the PERSON_NAME infoType detector." (release note dated 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• The backing model, training data or dictionary contents for `PERSON_NAME` and other machine-learning detectors are not named (checked the infoTypes concepts, reference, likelihood, overview and release-note pages and the client repo) **[Not disclosed]**
• Likelihood comes from signals: "Likelihood is calculated based on the number of signals a finding has that implies that the finding matches the infoType." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Context moves a finding up or down: positive context raises and negative context lowers the likelihood, and a finding that fails a checksum may not be reported (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• `InfoType.version` values: release notes show `stable`, `latest` and `legacy` (release notes dated 2026-07-13 and 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• For the new `PERSON_NAME` version the note says "In 30 days, the new version will be promoted to stable." (release note dated 2026-10-03; SDP docs, release notes, read 2026-10-09) **[Documented]**
• The client field is `version`: "Optional version name for this InfoType." (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:194`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Detector behaviour therefore changes between read dates without a product version, so findings for `PERSON_NAME` depend on the date and on the version setting (premise: the dated release notes) **[Inferred]**
• REST path: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/content:inspect`, and "The URLs use gRPC Transcoding syntax." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Global endpoint: "The global endpoint of Sensitive Data Protection is dlp.googleapis.com." Regional endpoints follow "dlp.REGION.rep.googleapis.com" (SDP docs, API endpoints page, read 2026-10-09) **[Documented]**
• Client libraries are listed for C#, Go, Java, Node.js, PHP, Python and Ruby (SDP docs, client libraries page, read 2026-10-09) **[Documented]**
• The Python package `google-cloud-dlp` is at version 3.40.0 at the pinned tag (`google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16` `__version__ = "3.40.0"`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client method is `inspect_content` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:872` "def inspect_content(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, content policy (separate resource, not part of this column by default): "A Sensitive Data Protection content policy is a reusable resource that you can use to evaluate content and determine whether to allow or block it based on its sensitivity." General availability is dated 2026-08-31 (SDP docs, content-policy overview and release notes, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 1: the overview promises "Get immediate, synchronous verdicts on content to enforce organizational data policies." (SDP docs, content-policy overview page, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 2a: the REST resource page for `projects.locations.contentPolicies` lists only the methods create, delete, get, list and patch (SDP docs, REST content policies page, read 2026-10-09) **[Documented]**
• Content-policy conflict, source 2b: the client at the tag has `create_content_policy`, `update_content_policy`, `get_content_policy`, `list_content_policies` and `delete_content_policy` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:7363` "def create_content_policy(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No documented way to submit an arbitrary string to a content policy was found (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages, release notes and the client methods) **[Not disclosed]**
• The roles page defines the permission `dlp.contentPolicies.apply` and the role DLP Content Policies Consumer ("Apply content policies."), and the manage page tells the administrator to grant `roles/dlp.user` to the Gemini Enterprise service account to apply policies (SDP docs, roles and permissions page and manage content policies page, read 2026-10-09) **[Documented]**
• Cross-reference, Model Armor docs, not SDP docs: "Sensitive Data Protection can identify sensitive elements, context, and documents to help you reduce the risk of data leakage going into and out of AI workloads." Model Armor offers a basic and an advanced configuration (Model Armor overview, read 2026-10-09) **[Documented]**
• For how Model Armor calls SDP, see the Model Armor columns "Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)" and "Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)"; those internals are not repeated here (premise: a pointer to the owning columns, not a source fact) **[Inferred]**
• Open-source and managed-cloud analogues for comparison only: `Presidio: PII detection in text (Analyzer)` and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either (premise: a pointer to the sibling columns only) **[Inferred]**
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
Summary: **A project, a location and a list of infoTypes.** Send the text, the infoTypes and an optional minimum likelihood. The caller needs billing, the API enabled and the DLP User role. Requests are capped at 0.5 MB; REST calls the 3,000-finding limit not hard. **[Documented]**
Detail:
• Parent: "Projects scope, no location specified (defaults to global): projects/{projectId}", or `projects/{projectId}/locations/{locationId}` to choose a processing location (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Config: `inspectConfig` overrides a named template: "Any configuration directly specified in inspectConfig will override those set in the template." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• Name the infoTypes: "Always specify infoTypes explicitly. Do not use an empty infoTypes list." (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• Default list, source 1: "If you don't specify any infoTypes, Sensitive Data Protection uses a default infoTypes list that is intended for testing purposes only." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Default list, source 2: "the system may automatically choose a default list of detectors to run, which may change over time." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Default list, source 3: "Otherwise, Sensitive Data Protection scans for a default set of infoTypes (ALL_BASIC)" (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Default list, source 4: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• The members of ALL_BASIC are not defined on any page checked (concepts, REST InspectConfig, content.inspect, content.deidentify and image.redact method pages, image guides, infoType reference, infoTypes.list page, release notes) **[Not disclosed]**
• A 2019 release note says "Updated the default list of infotypes included in ALL_BASIC." (release note dated 2019-02-11; SDP docs, release notes, read 2026-10-09) **[Documented]**
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
• Findings limit, second source: "If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower. This value isn't a hard limit." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
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
• **Minimum setup:** one Google Cloud project with billing and the DLP API enabled, `roles/dlp.user` for the caller, Application Default Credentials, and either `pip install google-cloud-dlp` or plain REST calls to `content:inspect` in a chosen location, such as `asia-southeast1` (premise: the quickstart, roles, endpoint and library pages above) **[Inferred]**
• The first gibibyte of content inspected each month per account is free, so a small labelled test set costs nothing; billing information is still required: "Sensitive Data Protection requires billing information for all accounts before you can start using the service." (SDP pricing page, read 2026-10-09) **[Documented]**
• A cost warning is on the pricing page: "It is possible for costs to become very high, depending on the quantity of information that you instruct Sensitive Data Protection to scan." (SDP pricing page, read 2026-10-09) **[Documented]**
• The JSON quickstart gives the steps: create a project, enable billing, run `gcloud services enable dlp.googleapis.com` and grant `roles/dlp.user` (SDP docs, JSON quickstart page, read 2026-10-09) **[Documented]**
• No client library is required: "Sending JSON to Sensitive Data Protection REST endpoints does not require a client library." (SDP docs, inspecting text page, read 2026-10-09) **[Documented]**
• The Python package is `google-cloud-dlp`, installed with `pip install google-cloud-dlp` (`README.rst@google-cloud-dlp-v3.40.0:88` "pip install google-cloud-dlp") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Python version, source 1: the package needs Python 3.10 or later (`setup.py@google-cloud-dlp-v3.40.0:95` `python_requires=">=3.10",`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Python version, source 2: the docs libraries page says "Samples are compatible with Python 2.7.x and 3.4 and higher." This refers to the samples, not the package, and looks out of date against the line above (SDP docs, client libraries page, read 2026-10-09) **[Documented]**
• Dependencies at the tag include `google-api-core[grpc] >= 2.28.0, <3.0.0` (`setup.py@google-cloud-dlp-v3.40.0:45`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• A regional host for Singapore would be `dlp.asia-southeast1.rep.googleapis.com` (premise: the pattern "dlp.REGION.rep.googleapis.com" and `asia-southeast1` listed as supported) **[Inferred]**
• No offline or emulator mode was found in the docs or the client package (checked the overview, method types, libraries, endpoints and locations pages and the package README and docs folder); every test sends text to Google's API **[Not disclosed]**
• A web demo exists: "Sensitive Data Protection Demo is a web-based application that you can use to test built-in infoType detectors." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• What the web demo does with text entered into it is not described (checked the demo page, the SDP docs navigation and the infoTypes concepts page) **[Not disclosed]**
• There is no first-party evaluation toolkit for detection quality (checked the docs navigation, the quickstarts and the client repo) **[Not disclosed]**
• The docs say: "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• A labelled set needs ground-truth character spans per information type, plus negative near-misses; sweep the five minimum-likelihood levels and score each type separately (premise: findings carry type, bucket and range) **[Inferred]**
• Build positives that pass the checksum and context checks, because the docs say sample data that does not pass the checks is not reported (premise: the quoted behaviour in R5) **[Inferred]**
• Record the read date and the `InfoType.version` used: `PERSON_NAME` has a new version due to be promoted to stable about 30 days after 2026-10-03, so results may shift after about 2026-11-02 (premise: the dated release note) **[Inferred]**
• No promotion note for the new `PERSON_NAME` version had appeared (checked the release notes, whose newest entry is dated 2026-10-03, read 2026-10-09) **[Not disclosed]**
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
• Which infoTypes run when none are listed: the docs give several wordings (a testing-only default list, a list that may change, ALL_BASIC, the most common infoTypes for images, all built-in infoTypes in de-identification) and no page defines ALL_BASIC; the exact membership needs an `infoTypes.list` call or a test
• Effect of the `PERSON_NAME` version change on a fixed test set before and after promotion to stable (needs two test runs)
• Whether `DOCUMENT_TYPE/CONTEXT/*` classifiers work on a short plain-text string and in `asia-southeast1`; the Availability column shows europe, global and us (needs testing)
• Whether CONTEXT messages in a conversation improve detection in the other messages or are only ignored for findings (checked the REST ContentItem page; not stated; needs testing)
• Batch item behaviour: whether the 0.5 MB request cap and the 3,000-finding cap apply to the whole batch or per string (checked the REST ContentItem and limits pages; not stated)
• Content-policy evaluation: the discovery document, RPC reference, REST resource and client list no apply or evaluate method, although the roles page defines the permission `dlp.contentPolicies.apply` and a role "Apply content policies."; how a caller outside Gemini Enterprise submits a string is not documented (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages and the client; needs a Gemini Enterprise check)
• Customer-data terms: the Google Cloud terms limit Google's processing of Customer Data to what the Data Processing Addendum allows, and the Service Specific Terms have no Sensitive Data Protection section; whether any SDP-specific use of content applies is not stated (checked the terms of service, Data Processing Addendum, Service Specific Terms and services list; the docs say request data "is not stored")
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
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.privacy.dlp.v2
• https://cloud.google.com/terms
• https://cloud.google.com/terms/data-processing-addendum
• https://cloud.google.com/terms/service-terms
• https://cloud.google.com/terms/services
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
• The InspectConfig reference has the description "Message for detecting output from deidentification transformations that support reversing." for surrogate detection (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Surrogate detectors go with the reversible transformations and are described in the reversible tokenisation and re-identification column, not here (premise: the surrogate-type description above) **[Inferred]**
• Custom detectors are set in `InspectConfig.customInfoTypes` and work in `projects.content.inspect` among other places: "Inspection using projects.content.inspect." (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• A custom detector can extend a built-in one: "CustomInfoType can either be a new infoType, or an extension of built-in infoType, when the name matches one of existing infoTypes and that infoType is specified in content.inspect.info_types field." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Inspection rules refine any detector: "Inspection rules help refine the scan results that the Sensitive Data Protection returns by modifying the detection mechanism of a given infoType detector." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Three rule types exist (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
  – "Exclusion rules, which help exclude false or unwanted findings."
  – "Hotword rules, which help detect additional findings in text content."
  – "Adjustment rules, which help adjust the likelihood of findings based on the context in which they appear."
• Large dictionaries are not inline: "Each large custom dictionary has two components" and "The dictionary files are stored in Cloud Storage and include a copy of the source phrase data plus bloom filters, which aids searching and matching." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Metadata-label detectors are recent: "You can configure Sensitive Data Protection to detect specific metadata labels in your content." (release note dated 2026-03-07), "…specific client-provided metadata." (2026-03-28) and "…specific file labels, which can represent Google Drive labels or Microsoft sensitivity labels." (2026-06-29) (SDP docs, release notes, read 2026-10-09) **[Documented]**
• Image-based rules arrived through release notes: "Image-based exclusion rules, which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings." (general availability note dated 2026-02-23); they are covered in the image detection and redaction and the image safety classification columns (SDP docs, release notes, read 2026-10-09) **[Documented]**
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
• Singapore gaps in the built-ins (no FIN, UEN or address infoType) could be filled by a user-written regex or dictionary, but nothing in the docs says Google tests such detectors (premise: the regex and dictionary definitions; see the sensitive-data detection in text column for the built-in gaps) **[Inferred]**
• Out of purpose: dictionaries and regexes match literal text, so they hold no semantic model of prompt injection, jailbreaks or toxicity; a list of known attack phrases would only catch exact matches (premise: the dictionary and regex definitions) **[Inferred]**
• Words in a dictionary use Unicode letters and digits, so Chinese, Malay and Tamil words can be listed; whether a short word inside a longer unspaced run is found follows the "different type" boundary rule and is untested (premise: the matching rules quoted in R4) **[Inferred]**
### R3
Summary: **Same inputs as inspection, with rules per detector.** Custom detectors and rules sit in the inspect request's configuration, so they run on the same strings, tables, conversations and files, with no input or output setting. Only large dictionaries need stored resources. **[Inferred]**
Detail:
• Where custom detectors are set: "You specify a CustomInfoType in the InspectConfig object when configuring the following:" inspection with `projects.content.inspect`, inspection jobs, inspection templates, `projects.content.deidentify`, de-identification templates and `projects.content.reidentify` (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• The content item is the same as for built-in inspection: string, table, bytes, conversation or batch (SDP docs, REST ContentItem page, read 2026-10-09) **[Documented]**
• The request has no input or output flag, so custom detectors apply to prompts, responses, retrieved text, tool inputs and tool outputs alike, as in the sensitive-data detection in text column (premise: the request fields in the REST inspect page) **[Inferred]**
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
• Regex syntax: the REST Regex reference says "Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub." (SDP docs, REST Regex page, read 2026-10-09) **[Documented]**
• A docs code sample comment also says "Refer https://github.com/google/re2/wiki/Syntax for creating regular expression." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**
• Base likelihood: "Defaults to VERY_LIKELY if not specified." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Hotword rules shift the likelihood: "Increase or decrease the likelihood by the specified number of levels." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Hotword example: "123-4-56789 would match as POSSIBLE. MRN 123-4-56789 would match as VERY_LIKELY." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**
• Exclusion by infoType overlap: "InfoType list in ExclusionRule rule drops a finding when it overlaps or contained within with a finding of an infoType from this list." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Adjustment by overlap: "Only MATCHING_TYPE_PARTIAL_MATCH is supported:" for `adjustByMatchingInfoTypes` (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• `exclusionType`: "A finding of this custom info type will be excluded from final results, but can still affect rule execution." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Rule order, source 1: "Sensitive Data Protection applies the rules in the order you specify them in the ruleset." (SDP docs, inspection rules page, read 2026-10-09) **[Documented]**
• Rule order, source 2: "Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Rule order, worked example: "If you specify the exclusion rule first, then the DOCUMENT_TYPE/CONTEXT/HEALTH findings are excluded from the result set before they can be used to provide context to the adjustment rule." (SDP docs, creating custom infoTypes rules page, read 2026-10-09) **[Documented]**
• Rule order, release note 2026-02-23 puts "Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset" at general availability; the REST page that says exclusion rules run last has a later footer date (2026-09-05), so it may be unchanged text rather than older text (premise: footer dates; they do not prove edits) **[Inferred]**
• Stored dictionaries rebuild in place: "Any scans that you run while the stored infoType is in pending state will be run using the old version of the stored infoType." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Key-value metadata detectors use two regexes: "The regular expression for the key. Key should be non-empty." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Dictionary size, source 1: "Use small custom dictionary detectors when you have a list of up to several tens of thousands of words or phrases." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Dictionary size, source 2: "Use regular custom dictionary detectors when you have at most several hundred thousand words." (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• The client at the tag has the same fields: `metadata_key_value_expression`, `file_label_info_type` and `exclusion_type` on `CustomInfoType` (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:334` "metadata_key_value_expression (google.cloud.dlp_v2.types.CustomInfoType.MetadataKeyValueExpression):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client has the image-rule enum value (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:676` "MATCHING_TYPE_RULE_SPECIFIC (4):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Model Armor: the metadata page says to "create an advanced Sensitive Data Protection configuration in Model Armor that references this custom metadata label detector" (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
### R5
Summary: **Same findings as inspection, under your detector name.** A custom match returns the name you chose and a likelihood you set, Very likely unless changed, after any rules have run. The response holds only the findings. **[Documented]**
Detail:
• Findings carry the custom name: the `infoType` field is the "name of the custom infoType detector" and the result uses the same finding shape as built-in inspection (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Base likelihood: if the likelihood field is omitted, the custom infoType detector "defaults to VERY_LIKELY" (SDP docs, custom infoType detectors overview page, read 2026-10-09) **[Documented]**
• Rules then alter it: "Rules are applied in the order that they are specified." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• A relative adjustment is capped: "Likelihood may never drop below VERY_UNLIKELY or exceed VERY_LIKELY" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• A detector can be silent: with `EXCLUSION_TYPE_EXCLUDE` it "will not cause a finding to be returned. It still can be used for rules matching" (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Sensitivity score is for profiling only: "If unset for a CustomInfoType, it will default to HIGH. This only applies to data profiling." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• Metadata findings: "The finding's MetadataType for MetadataLocation is populated based on whether the match is embedded in the file (CONTENT_METADATA) or provided by the client (CLIENT_PROVIDED_METADATA)." (SDP docs, custom metadata label page, read 2026-10-09) **[Documented]**
• Threshold guidance: "If you notice a regex custom infoType detector returning too many false positives, try reducing the base likelihood and using detection rules to boost the likelihood using contextual information." (SDP docs, custom regex page, read 2026-10-09) **[Documented]**
• The minimum-likelihood setting from the sensitive-data detection in text column applies to the final likelihood of a custom match (premise: the REST text says the system "only returns" findings at or above the threshold, with per-type thresholds available) **[Inferred]**
• The inspect response has the single field `result`, "The findings." (SDP docs, REST InspectContentResponse page, read 2026-10-09) **[Documented]**
• No verdict is produced; the caller acts on findings (premise: the response shape is the same as built-in inspection) **[Inferred]**
• Accuracy of a custom detector depends on the user's list or pattern; Google publishes no precision or recall for custom detectors (checked the custom infoType, dictionary, regex, rules and likelihood pages) **[Not disclosed]**
### R6
Summary: **A CustomInfoType object inside the inspect request.** Give a name, a dictionary, regex or stored reference, an optional base likelihood and rules. Limits per request include 30 custom detectors, 10 regular dictionaries, 10 rule sets and a regex length of 1000. **[Documented]**
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
  – Maximum combined size of all input files stored in Cloud Storage | 1 GB
  – Maximum number of input files stored in Cloud Storage | 100
  – Maximum size of an input column in BigQuery | 1 GB
  – Maximum number of input table rows in BigQuery | 5,000,000
  – Maximum size of output files | 500 MB
• Phrase components: "Maximum number of components (continuous sequences containing only letters, only digits, only non-letter characters, or only non-digit characters) per regular custom dictionary phrase | 40" (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• Request-level caps from the sensitive-data detection in text column (0.5 MB, 3,000 findings, 50,000 table values) still apply (SDP docs, quotas and limits page, read 2026-10-09) **[Documented]**
• A large dictionary needs a term list first: either "a text file within Cloud Storage or a column in a BigQuery table", then a stored infoType with an output location (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Warning: "Do not alter custom dictionary files directly in Cloud Storage." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• A stored infoType is ready to use when "the status of the infoType shows Ready." (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• Custom detectors may also be kept in an inspection template named by `inspectTemplateName`, with request fields overriding the template (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**
• `roles/dlp.user` is "Inspect, Redact, and De-identify Content" and lists `dlp.contentPolicies.apply`, `dlp.kms.encrypt`, `dlp.locations.*` and `serviceusage.services.use`, with no `dlp.storedInfoTypes.*` permission (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**
• `dlp.storedInfoTypes.get` and `dlp.storedInfoTypes.list` are listed under DLP Reader (`roles/dlp.reader`) and DLP Viewer (`roles/dlp.viewer`), and the REST `content.inspect` page names only `serviceusage.services.use` on the parent (SDP docs, roles and permissions and REST projects.content.inspect pages, read 2026-10-09) **[Documented]**
• Whether a request that names a stored infoType needs `dlp.storedInfoTypes.get` on top of `roles/dlp.user` (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; not stated) **[Not disclosed]**
• Auth, location and billing are as for built-in inspection (see the sensitive-data detection in text column) (premise: same method and parent) **[Inferred]**
### R7
Summary: **Minimum setup:** the same project, billing, DLP User role and credentials as built-in inspection. An inline dictionary, regex or hotword rule needs nothing else; a large dictionary also needs a Cloud Storage bucket. Test each rule with matched and near-miss strings, in each language you care about, and compare findings with and without rules. **[Inferred]**
Detail:
• **Minimum setup:** the project, billing, API and `roles/dlp.user` from the sensitive-data detection in text column, plus a request that carries a `customInfoTypes` list or `ruleSet`; no extra resource is created for inline detectors (premise: the REST fields and the overview page) **[Inferred]**
• A large dictionary needs a Cloud Storage bucket and a folder where the generated dictionary is written (SDP docs, large custom dictionary page, read 2026-10-09) **[Documented]**
• The Python client has the custom-detector types (`google/cloud/dlp_v2/types/storage.py@google-cloud-dlp-v3.40.0:338` "file_label_info_type (google.cloud.dlp_v2.types.CustomInfoType.FileLabelInfoType):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• A sample inline dictionary request is on the docs page, for example a room-name word list of RM-Orange, RM-Yellow and RM-Green (SDP docs, regular custom dictionary page, read 2026-10-09) **[Documented]**
• Test design: a labelled set of true matches and near-misses per detector, run once with no rules and once with each rule, to measure what the rule removes or boosts (premise: rules change only likelihood or presence) **[Inferred]**
• Test the boundary and case rules: words next to digits, letters or unspaced scripts, and mixed case (premise: the matching rules in R4) **[Inferred]**
• Test metadata detectors with a content item that carries `contentMetadata` key-value pairs and check that the finding location type reads client-provided metadata (premise: the metadata page example) **[Inferred]**
• No first-party tool tests custom detectors; the docs say only "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Cost and data handling match built-in inspection: content inspected is billed in bytes with the first gibibyte per month free, and request data "is not stored" (SDP docs, pricing and method types pages, read 2026-10-09) **[Documented]**
• No offline or emulator mode applies to custom detectors; they run inside the same hosted inspect call as built-in detectors, for which none was found (checked the overview, method types, libraries, endpoints and locations pages and the package README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Unsupported regex constructs, conflicting dictionary and rule-order statements, permissions for stored infoTypes, behaviour on unspaced scripts, and no published accuracy for custom detectors.
Detail:
• Which RE2 constructs are accepted by the service and what happens with unsupported ones (the reference names RE2 syntax only; needs testing)
• Dictionary capacity: two pages give "several tens of thousands" and "several hundred thousand" words, while the limits page gives 128 KB inline and 512 KB from Cloud Storage (needs a test with a real word list)
• Rule order: the guide says rules apply in the order written, the REST text says exclusion rules run last, and a 2026-02-23 release note announces enhanced ordering (needs a test of mixed rule sets)
• Whether `roles/dlp.user` alone is enough to use a stored infoType in `content.inspect`: the role holds no stored-infoType permission and no page states what the request needs (checked the roles, REST inspect, ContentItem, stored-infoType and audit-logging pages; needs a permission test)
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
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectContentResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DeidentifyContentResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse
## Column SD3: Sensitive Data Protection: Sensitive-data masking and de-identification in text
### R1
Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method finds sensitive values, then redacts, replaces, masks or hashes them. Bucketing and date shifting are offered but shown only on table fields. It returns the item and a summary of changes. **[Documented]**
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
• The date-shift, time-extraction and bucketing code samples on the transformation reference page use record (table) transformations (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• The two reversible crypto transformations (`CryptoReplaceFfxFpeConfig`, `CryptoDeterministicConfig`) are covered in the reversible tokenisation and re-identification column, not here (premise: the footnote "Reversible transformations can be reversed to re-identify the sensitive data using the content.reidentify method." in the transformation table) **[Inferred]**
• LLM use is named: "Mask sensitive text before external processing: De-identify or redact sensitive tokens from text strings synchronously before passing content to third-party APIs or large language models (LLMs)." (SDP docs, method types page, read 2026-10-09) **[Documented]**
• Prompt use is named: "Mask confidential data in generative AI prompts: Redact proprietary or regulated information from user prompts before sending content to public or third-party LLMs." (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• Automatic redaction is contrasted with findings: "Automatic redaction produces an output with sensitive data matches removed instead of giving you a list of findings." (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• De-identification in storage is a separate job path: "Create a de-identified copy of Cloud Storage data using an inspection job." It is outside this column (inventory only) (SDP docs, overview page, read 2026-10-09) **[Documented]**
### R2
Summary: **Sensitive values leaving for LLMs, logs and third parties.** It addresses exposure of personal, financial, health and credential data that the detectors can find, by removing or disguising the value. It does not judge content such as attacks or toxicity. **[Inferred]**
Detail:
• Detection uses the same built-in and custom infoTypes as the sensitive-data detection in text column; see that column for the taxonomy, Singapore ID types, language statements and LLM-provider key detectors (premise: `inspectConfig` is part of the de-identify request) **[Inferred]**
• Use cases on the text page: "Sanitize user input before database persistence", "Sanitize customer service transcripts and logs" and masking prompts for LLMs (SDP docs, text classification and redaction page, read 2026-10-09) **[Documented]**
• Techniques named in the overview: "Various transformation methods are available, including masking, redaction, bucketing, date shifting, and tokenization." (SDP docs, overview page, read 2026-10-09) **[Documented]**
• Date shifting use: "Obfuscate patient admission and discharge dates to meet HIPAA Safe Harbor de-identification requirements while preserving temporal intervals between events." (SDP docs, date shifting page, read 2026-10-09) **[Documented]**
• No compliance guarantee: "You must decide what data is sensitive and how to best protect it." and detectors "can't guarantee compliance with regulatory requirements" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Re-identification risk is a separate service: "The risk analysis service lets you analyze structured BigQuery data to identify and visualize the risk that sensitive information will be revealed (re-identified)." It is inventory only (SDP docs, overview page, read 2026-10-09) **[Documented]**
• A value is changed only if a detector finds it, so a miss stays in the text; residual leakage therefore follows the detection recall, which is not published (premise: the three-part call in R4) **[Inferred]**
• Out of purpose: transformations replace or hide values and do not detect prompt injection, jailbreaks, toxicity or off-topic content (checked the overview, transformation reference and de-identifying pages; a scope judgement; premise: the overview's purpose sentence "discover, classify, and de-identify sensitive data") **[Inferred]**
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
Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Each detected value is then redacted, replaced, masked or hashed; bucketing and date shifting are shown only on table fields. **[Documented]**
Detail:
• Three parts: "The data to inspect", "What to inspect for" and "What to do with the inspection findings", the last being the `DeidentifyConfig` (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Detection is required: "An InspectConfig object is required in your request, with one exception." The exception is record transformations (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Two transformation categories: "InfoTypeTransformations: Transformations that are only applied to values within submitted text that are identified as a specific infoType." and RecordTransformations for tabular data (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• No infoType listed: "not specifying at least one infoType in an InspectConfig argument causes the transformation to apply to all built-in infoTypes that don't have a transformation provided. Doing so is not recommended, as it can cause decreased performance and increased cost." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Inspection default quoted on the de-identifying page: "Otherwise, Sensitive Data Protection scans for a default set of infoTypes (ALL_BASIC), some of which you might not need." (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• When a string matches both a general and a specific infoType and both are requested, inspection reports two findings for it: "you get two findings for the same string" (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• How de-identification applies two transformations to overlapping findings of different infoTypes is not described (checked the de-identifying, transformation reference, text redaction and infoTypes concepts pages and the REST deidentify and InfoTypeTransformations references) **[Not disclosed]**
• Redaction: `RedactConfig` "Redacts a value by removing it." and the sample output leaves a gap: "My name is Alicia Abernathy, and my email address is ." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace with a value: `ReplaceValueConfig` "Replaces each input value with a given value." and in the sample the email address is replaced by the fixed text "fake@example.com" (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace with the infoType name: `ReplaceWithInfoTypeConfig` "Replaces an input value with the name of its infoType." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Replace from a list: `ReplaceDictionaryConfig` "Replaces an input value with a value that is randomly selected from a word list." so output can vary between calls (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Character mask: `CharacterMaskConfig` "Masks a string either fully or partially by replacing a given number of characters with a specified fixed character." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Bucketing: "Sensitive Data Protection can bucket numerical input values based on fixed size ranges" (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Date shift and time part: `DateShiftConfig` "Shifts dates by a random number of days, with the option to be consistent for the same context." and `TimePartConfig` "Extracts or preserves a portion of Date, Timestamp, and TimeOfDay values." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash, source 1: the table says `CryptoHashConfig` "Replaces input values with a 32-byte hexadecimal string generated using a given data encryption key." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash, source 2: the same page's text says Sensitive Data Protection "outputs a base64-encoded representation of the hashed input value in the place of the original value." and "This transformation can't be reversed." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Hash scope: "Currently, only string and integer values can be hashed." (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Input-type cells: redact, replace, mask and both bucketing objects read "Any"; the crypto hash reads "Strings or integers"; date shift and time part read "Dates/Times" (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• The API accepts `fixedSizeBucketingConfig`, `bucketingConfig`, `dateShiftConfig` and `timePartConfig` inside an infoType transformation, and describes them for numeric, timestamp and date values; `dateShiftConfig.cryptoKey` "Can only be applied to table items." (API discovery document revision 20261006, schemas PrimitiveTransformation, DateShiftConfig and TimePartConfig) **[Documented]**
• The date-shift, time-extraction and bucketing code samples use record (table) transformations and a context field (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**
• Whether the bucketing, date-shift and time-extraction transformations work on infoType findings in free text is not stated (checked the transformation reference; the docs table says Any or Dates/Times) **[To be verified]**
• Transformation errors: the client `DeidentifyConfig` has `transformation_error_handling`, "Mode for handling transformation errors. If left" unspecified the default is `ThrowError`; the alternative is `LeaveUntransformed` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5449` "Mode for handling transformation errors. If left") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The REST reference documents the same field on `DeidentifyConfig`: "Mode for handling transformation errors. If left unspecified, the default mode is TransformationErrorHandling.ThrowError."; `LeaveUntransformed` "Skips the data without modifying it if the requested transformation would cause an error." (SDP docs, REST deidentifyTemplates page, read 2026-10-09) **[Documented]**
• The client has all 12 transformation classes and the `DeidentifyConfig` choice of `info_type_transformations`, `record_transformations` or `image_transformations` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5433` "Treat the dataset as free-form text and apply") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client method is `deidentify_content` (`google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:1060` "def deidentify_content(") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Endpoints are the same as for inspection: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/content:deidentify` (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• Templates: a de-identification template can be named in `deidentifyTemplateName`; the docs list "Apply the same de-identification or inspection policies across both real-time content API calls and scheduled storage repository scans" as a use (SDP docs, templates page, read 2026-10-09) **[Documented]**
• Cross-reference, Model Armor docs, not SDP docs: "Model Armor streaming methods don't support Sensitive Data Protection de-identification." and "Sensitive Data Protection de-identification is not supported for file-based prompts." (Model Armor sanitize page, read 2026-10-09) **[Documented]**
• For how Model Armor invokes SDP de-identification, see the Model Armor columns "Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)" and "Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)"; those internals are not repeated here (premise: a pointer to the owning columns, not a source fact) **[Inferred]**
• Open-source and managed-cloud analogues for comparison only: `Presidio: PII anonymisation and masking in text (Anonymizer)` and `GovTech Sentinel: PII detection and masking (AWS Bedrock)`; no claim is made here about either (premise: a pointer to the sibling columns only) **[Inferred]**
### R5
Summary: **The transformed item and a summary of changes.** The response holds the item with sensitive values changed, plus the bytes transformed and, per transformation, the infoType, count and result code. Over 3,000 findings returns an error message. **[Documented]**
Detail:
• Response parts: the client `DeidentifyContentResponse` has `item` ("The de-identified item.") and `overview` (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2972` "The de-identified item.") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The sample response has `overview.transformedBytes` and `transformationSummaries` with `infoType`, `transformation`, `results` (a `count` and a `code` such as SUCCESS) and `transformedBytes` (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
• Result codes at the tag are SUCCESS and ERROR, with a `details` string for warnings or errors (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6895` "class TransformationResultCode(proto.Enum):") **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No findings list or original values are returned in the response fields (premise: the two response fields above) **[Inferred]**
• Only the requested infoTypes are changed: in the sample, a request for `EMAIL_ADDRESS` returns the sentence with the email address replaced by its infoType name in brackets and the name untouched (SDP docs, de-identifying page, read 2026-10-09) **[Documented]**
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
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, `roles/dlp.user`, Application Default Credentials and either `pip install google-cloud-dlp` or REST calls to `content:deidentify` (premise: the quickstart, roles and library pages cited in the sensitive-data detection in text column) **[Inferred]**
• Transformed bytes are free for the first gibibyte per month per account, and inspection bytes are billed separately (SDP pricing page, read 2026-10-09) **[Documented]**
• Residual-leak test: run `content.deidentify` on labelled prompts, then run `content.inspect` on the output and count findings that remain (premise: the two methods share detectors) **[Inferred]**
• Utility test: compare an LLM answer on the cleaned prompt with the answer on the original, for a mask, a fixed replacement and an infoType-name replacement (premise: the transformations differ in what they leave in the text) **[Inferred]**
• Include prompts with more than 3,000 findings, tables and conversations with CONTEXT messages (premise: the limits and behaviours in R3 to R6) **[Inferred]**
• No offline or emulator mode and no first-party evaluation toolkit for de-identification were found (checked the overview, method types, libraries and de-identifying pages and the client package) **[Not disclosed]**
• The docs say to test: "Google recommends that you test your settings to make sure that your configuration meets your requirements." (SDP docs, infoTypes concepts page, read 2026-10-09) **[Documented]**
• Request data is encrypted in transit and not stored, but test text is sent to Google's API (SDP docs, method types page, read 2026-10-09) **[Documented]**
• The Python package needs Python 3.10 or later (`setup.py@google-cloud-dlp-v3.40.0:95` `python_requires=">=3.10",`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Record the read date and detector versions, since detectors change without a product version (premise: the dated release notes cited in the sensitive-data detection in text column) **[Inferred]**
### R8
Summary: **Key open questions.** No published residual-leak or accuracy figures, unclear hash output format, whether bucketing, date shift and time part work on free text, how overlapping findings are resolved, and behaviour near the 3,000-finding cap.
Detail:
• Residual leakage after de-identification across infoTypes and languages, including Singapore NRIC (checked the de-identifying, transformation reference and concepts pages; none published; needs testing)
• Hash output format: the table says 32-byte hexadecimal and the text says base64 for `CryptoHashConfig` (needs a test)
• Whether `FixedSizeBucketingConfig`, `BucketingConfig`, `DateShiftConfig` and `TimePartConfig` apply to infoType findings in free text, or only to table fields (checked the transformation reference; samples use records; needs testing)
• How overlapping findings of different infoTypes are transformed when both have a transformation (checked the de-identifying and transformation reference pages; not stated; needs testing)
• Whether the 3,000-finding cap counts across all messages of a conversation or all strings of a batch, and whether a partial result is returned or only the error message (needs testing)
• Whether `LeaveUntransformed` behaves as documented on a plain `content.deidentify` request, for example for a date shift applied to an IP address (the REST reference documents the field; needs testing)
• Latency and throughput for long prompts and many transformations (checked the pages above and the SLA; none published; needs measuring)
• Effect on LLM answer quality of each replacement style (needs testing; no Google guidance found)
• Whether CONTEXT messages affect detection in neighbouring messages (checked the ContentItem page; not stated)
• Customer-data terms: the Google Cloud terms limit Google's processing of Customer Data to what the Data Processing Addendum allows, and the Service Specific Terms have no Sensitive Data Protection section; whether any SDP-specific use of content applies is not stated (checked the terms of service, Data Processing Addendum, Service Specific Terms and services list; the docs say request data "is not stored")
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
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates
• https://cloud.google.com/terms
• https://cloud.google.com/terms/data-processing-addendum
• https://cloud.google.com/terms/service-terms
• https://cloud.google.com/terms/services
## Column SD4: Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE)
### R1
Summary: **Reversible tokens for detected values.** De-identification can swap each detected value for an encrypted token, and a later re-identify call turns the token back into the original using the same key. Two reversible methods exist: AES-SIV and format-preserving encryption. **[Documented]**
Detail:
• "Pseudonymization is a de-identification technique that replaces sensitive data values with cryptographically generated tokens." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Pseudonymization is sometimes referred to as tokenization or surrogate replacement." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Pseudonymization techniques enable either one-way or two-way tokens. A one-way token has been transformed irreversibly, while a two-way token can be reversed." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• The page's summary table marks deterministic encryption with AES-SIV and format preserving encryption (FPE-FFX) as Reversible and cryptographic hashing as not Reversible (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Reversal is the `content.reidentify` method: "Re-identifies content that has been de-identified." (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• The method accepts only two transformations: "This requires that only reversible transformations be provided here. The reversible transformations are:" followed by `CryptoDeterministicConfig` (AES-SIV) and `CryptoReplaceFfxFpeConfig` (FPE) (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• Google recommends AES-SIV: "We recommend this method, because it provides the highest level of security among all the reversible cryptographic methods that Sensitive Data Protection supports." (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• The content-methods page lists the use case "Re-identify tokenized data on demand: De-tokenize previously pseudonymized tokens in authorized server-side workflows when an authenticated business user requires access to the original plaintext." (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• The same page lists "De-identify or redact sensitive tokens from text strings synchronously before passing content to third-party APIs or large language models (LLMs)." as a use of content methods generally (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• Tokenising a prompt before the model and re-identifying the reply afterwards is one way to apply this to an LLM flow; no LLM round trip is described on the pages cited for this column, and it needs the model to return the tokens unchanged (premise: content methods accept any string, per the item types in R3) **[Inferred]**
• Cryptographic hashing is the one-way contrast: "Unlike other types of crypto-based transformations, this type of transformation isn't reversible." (SDP docs, transformations-reference page, read 2026-10-09); its row belongs to the masking and de-identification in text column **[Documented]**
• The Python client at v3.40.0 exposes `reidentify_content` and `deidentify_content` (google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:1151 and google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:1060) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R2
Summary: **Keeps raw values away from downstream systems.** Tokens replace detected personal or secret values, repeat consistently for the same key, and can be reversed only with that key. Which values are tokenised depends on the detectors in the request. **[Documented]**
Detail:
• "Enable secure reversibility for authorized workflows: Use two-way encryption (such as AES-SIV or FPE) with keys stored in Cloud Key Management Service so that only authenticated and privileged backend services can de-tokenize the original values when legally required." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Preserve referential integrity across analytical datasets: Replace customer IDs and primary keys with consistent cryptographic tokens so teams can join and aggregate tables in BigQuery without exposing sensitive identifiers." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Referential integrity is defined as "Given the same crypto key and context tweak, a table of data will be replaced with the same obfuscated form each time it is transformed" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Transient cryptographic keys only keep integrity per API request." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Repeated values leak equality, and the docs say so: "In situations where repetitive data or data patterns might occur, the risk of re-identification increases." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• For FPE the docs add: "In situations where the number of possible character strings is small, either increase the radix of the alphabet or use a context tweak." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Values are chosen by detection: "The most common way to do this is to use a built-in or custom infoType detector to match on the desired sensitive data values." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Structured data can also be tokenised by whole column: "you can also perform tokenization on entire columns of data using record transformations" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Detection coverage (PII, government IDs including Singapore NRIC and passport, credentials) is the subject of the sensitive-data detection in text and custom detector columns; a value the detectors miss is not tokenised, (premise: transformations are applied to findings) **[Inferred]**
• An infoType transformation names the infoTypes it applies to, so tokenising a Singapore NRIC means listing its infoType in the transformation; the docs examples use PHONE_NUMBER and EMAIL_ADDRESS, not a Singapore type (premise: an infoType transformation lists the infoTypes it applies to; SDP docs, transformations-reference page, read 2026-10-09) **[Inferred]**
• "Country-specific infoTypes support the English language and the respective country's languages. Most global infoTypes work with multiple languages." This covers the detection step that feeds tokenisation (SDP docs, concepts-infotypes page, read 2026-10-09) **[Documented]**
• FPE exists for fixed formats: "This allows the output to be used in systems that have format validation on length. This is useful for legacy systems where string length must be maintained." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• Scope statement: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (SDP docs, sensitive-data-protection-overview page, read 2026-10-09) **[Documented]**
• Out of purpose: prompt injection, jailbreaks, toxicity and topic control are not named on any page checked (overview, method-types, pseudonymization, transformation-reference and quickstart); this is a scope judgement (premise: the purpose sentence in the overview, "discover, classify, and de-identify sensitive data") **[Inferred]**
### R3
Summary: **One text or table item per call, with no input or output flag.** Prompts, responses, retrieved text and tool results all go through the same two calls. Content methods are stateless and results are not stored in Google Cloud. **[Inferred]**
Detail:
• For `content.deidentify` the REST reference says "The item to de-identify. Will be treated as text." and "This value must be of type Table if your deidentifyConfig is a RecordTransformations object." (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• For `content.reidentify`: "The item to re-identify. Will be treated as text." (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• Whether `content.reidentify` accepts conversation and batch items is not stated: its item is "treated as text", and the release notes announce conversation and batch support for inspecting and de-identifying only (checked the REST reidentify and ContentItem pages, the release notes and the client request type) **[Not disclosed]**
• The `content.deidentify` request body has the fields `deidentifyConfig`, `inspectConfig`, `item`, `inspectTemplateName`, `deidentifyTemplateName` and `locationId` (SDP docs, REST projects.content.deidentify page, read 2026-10-09) **[Documented]**
• The `content.reidentify` request body has the fields `reidentifyConfig`, `inspectConfig`, `item`, `inspectTemplateName`, `reidentifyTemplateName` and `locationId` (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• Neither request has a field for direction, message role or prompt type, so the caller decides what string to send; the column therefore applies to prompts, responses, retrieved text, tool inputs and tool outputs alike (premise: the REST request bodies for deidentify and reidentify list no such field) **[Inferred]**
• The client request class at the tag matches the REST body: google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2989 **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "Content methods are synchronous, stateless methods." (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• "Request data is encrypted in transit and is not stored." (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, sensitive-data-protection-overview page, read 2026-10-09) **[Documented]**
• Reversal needs the whole token and the key, not a lookup table: "To re-identify the de-identified content, you pass the entire token in the re-identify request." (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• "Reversible: Can be re-identified using the cryptographic key, surrogate annotation, and any context tweak." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "A surrogate annotation is required for re-identification of unstructured data." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• For tables the annotation is optional: "Sensitive Data Protection can perform both de-identification and re-identification on an entire column using a RecordTransformation without a surrogate annotation." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Context tweaks apply to structured data only: the step is titled "Step 5 (Format preserving and deterministic encryption with AES-SIV of structured data only)" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• For plain strings with no record, the client docstring says the context is ignored: "plaintext would be used as is for encryption." (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5905) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Nothing in the request carries a system prompt or conversation roles, so no prompt context is needed to tokenise or restore a string (premise: the request fields listed above) **[Inferred]**
### R4
Summary: **Standard keyed encryption, not a model.** AES-SIV gives base64 tokens, and the docs disagree on whether the length is kept; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. **[Documented]**
Detail:
• "Sensitive Data Protection supports three pseudonymization techniques, all of which use cryptographic keys." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• AES-SIV: the value is "encrypted using the AES-SIV encryption algorithm with a cryptographic key, encoded using base64, and then prepended with a surrogate annotation, if specified" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• The client docstring for `CryptoDeterministicConfig`: "representation of the encrypted output. Uses AES-SIV based on" the RFC 5297 link on the next line (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5841) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Key handling for AES-SIV: "provided key is internally expanded to 64 bytes" (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5848) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• FPE: "By design, FPE-FFX preserves the length and character set of the input text." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "This means that it lacks authentication and an initialization vector, which would cause a length expansion in the output token." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "FPE provides fewer security guarantees compared to other deterministic encryption methods such as deterministic encryption with AES-SIV." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Other methods like deterministic encryption using AES-SIV provide these stronger security guarantees and are recommended for tokenization use cases unless length and character set preservation are strict requirements" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "Important: Don't use the CryptoReplaceFfxFpeConfig method, except when preserving the input alphabet space and size is a requirement." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• "The CryptoReplaceFfxFpeConfig method can run very slowly, and it has limitations on the size of the alphabet and number of tokens" (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• "The CryptoDeterministicConfig method has no limitations on the input and is much faster." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• The client docstring agrees: "plus warrant referential integrity. FPE incurs significant latency" (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6244) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• FPE security limits recommended by NIST, quoted from the page: "radix^max_size <= 2^128." and "radix^min_len >= 100" (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• FPE alphabet choices: "Use one of four enumerated values that represent the four most common character sets/alphabets." Other choices are a radix from 2 to 95 or an explicit character list (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Three key types exist: Cloud KMS wrapped, transient and unwrapped; the page calls the wrapped key "the most secure type of cryptographic key available to use with the Sensitive Data Protection de-identification methods" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• "A Cloud KMS wrapped key consists of a 128-, 192-, or 256-bit cryptographic key that has been encrypted using another key." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• A transient key "is generated by Sensitive Data Protection at the time of de-identification, and then discarded" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• A transient key therefore cannot support later reversal (premise: the key is discarded after de-identification) **[Inferred]**
• Raw keys: "Because of the risk of accidentally leaking the key, these types of keys are not recommended." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• The client defines `CryptoKey` with a one-of of transient, unwrapped and kms_wrapped sources (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6435) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client docstring names the permission needed for a KMS-wrapped key: google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6484 lists "dlp.kms.encrypt" **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The REST KmsWrappedCryptoKey schema says: "Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt" (SDP docs, REST deidentifyTemplates page, read 2026-10-09) **[Documented]**
• The IAM page lists `dlp.kms.encrypt` in DLP User (`roles/dlp.user`) (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**
• Reversal finds tokens with a custom infoType: "Message for detecting output from deidentification transformations that support reversing." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**
• The quickstart re-identify request pairs a `customInfoTypes` entry holding `surrogateType` with the same `cryptoDeterministicConfig` and `surrogateInfoType` used to tokenise (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• Pick a surrogate name that cannot occur in data: "info type must not occur naturally anywhere in your data;" (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5873) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Failure modes named by the same docstring: inspection may "reverse a surrogate that does not correspond to an actual" identifier, or be unable to parse the surrogate and return an error (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5876) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cloud KMS key placement: "When you create a Cloud KMS key, you must store it in either global or in the same region that you will use for your Sensitive Data Protection requests. Otherwise, the Sensitive Data Protection requests will fail." (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• Access is by the DLP API over REST (global endpoint `dlp.googleapis.com`, regional endpoint `dlp.REGION.rep.googleapis.com`), through `projects.content.reidentify` or `projects.locations.content.reidentify` (SDP docs, REST projects.locations.content.reidentify page, read 2026-10-09) **[Documented]**
• In the REST bodies the `locationId` field is described as "Deprecated. This field has no effect." and the location is carried by `parent` (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• "There is no guarantee that the data in transit remains in the processing region that you specified." applies to the global endpoint with a location; regional endpoints "guarantee data residency" for data at rest, in use and in transit (SDP docs, api-endpoints page, read 2026-10-09) **[Documented]**
• Python client: package `google-cloud-dlp` version 3.40.0 (google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Tokenisation itself uses a cryptographic algorithm and no machine-learning model; what is tokenised depends on infoType detectors, whose backing models are covered in the sensitive-data detection in text column (premise: the pseudonymization page names AES-SIV and FPE-FFX as the techniques) **[Inferred]**
• Conflict on AES-SIV output length, statement 1: the transformation table row says CryptoDeterministicConfig "Replaces an input value with a token, or surrogate value, of the same length using AES in Synthetic Initialization Vector mode (AES-SIV)." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• Conflict on AES-SIV output length, statement 2: the same page's deterministic-encryption section says the token "Does not preserve the character set ("alphabet") or length of the input value post-encryption." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• Conflict on AES-SIV output length, statement 3: "This method produces a hashed value, so it does not preserve the character set or the length of the input value." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• The client docstring supports statements 2 and 3 on format (base64 output) but says nothing on length: google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:5840; behaviour needs a test **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R5
Summary: **Transformed text plus a summary of changes.** The response returns the item with tokens or restored values and an overview listing each transformation with success or error counts. A token is a surrogate name, a length and the encrypted value. **[Documented]**
Detail:
• `content.deidentify` returns `item` (the de-identified item) and `overview` (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2967) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• `content.reidentify` returns `item` (the re-identified item) and `overview` (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:3084) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Token form: "SURROGATE_INFOTYPE(SURROGATE_VALUE_LENGTH):SURROGATE_VALUE" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Documented example token for an email address: "EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q." (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• Without an annotation: "If you do not specify a surrogate annotation, the resulting token is equal to the transformed value" (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• The quickstart response overview holds `transformedBytes` and `transformationSummaries[]`, each with `infoType`, `transformation`, `results[]` (`count`, `code`) and `transformedBytes` (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• In that example the summary echoes the transformation configuration, including `kmsWrapped.wrappedKey` (the wrapped, encrypted key) and `cryptoKeyName` (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• The re-identify response in the quickstart returns the restored sentence in `item.value` and an `overview` of the same shape (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• Each summary result carries a code and a free-text field: `details` is "A place for warnings or errors to show up if" a transformation did not work as expected (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6922) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Result codes are `SUCCESS` and `ERROR` (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:6902) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Documented FPE error text for values outside the alphabet: "CryptoReplaceFfxFpeConfig's 'alphabet' does not include all the characters in the value being transformed" (SDP docs, release-notes page, read 2026-10-09) (change of 2018-12-12) **[Documented]**
• Too many findings: "Too many findings to de-identify. Retry with a smaller request." (SDP docs, deidentify-sensitive-data page, read 2026-10-09) **[Documented]**
• The REST response for `content.reidentify` has the fields `item` ("The re-identified item.") and `overview` ("An overview of the changes that were made to the item.") (SDP docs, REST ReidentifyContentResponse page, read 2026-10-09) **[Documented]**
• The call returns no score, likelihood or allow or block verdict for the transformation; the caller decides what to do with the output, (premise: the response fields `item` and `overview` above) **[Inferred]**
• Which values are transformed is filtered by minimum likelihood: "If you don't set a minimum likelihood in your request, or if you set it to LIKELIHOOD_UNSPECIFIED, Sensitive Data Protection returns only the findings with a likelihood of POSSIBLE and higher." (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• The likelihood page describes the trade-off at each level (for example VERY_LIKELY gives "the highest precision at the expense of recall") but names no recommended value for tokenisation (SDP docs, likelihood page, read 2026-10-09) **[Not disclosed]**
• No published measure of round-trip correctness, token collision rate or throughput (checked the pseudonymization, transformation-reference, quickstart, pricing, limits, SLA and release-note pages) **[Not disclosed]**
### R6
Summary: **Needs a key, a surrogate name and a supported input.** Requests need a Cloud KMS wrapped key in a matching region, a surrogate annotation for free text, and values within AES-SIV or FPE limits. API keys cannot be used with wrapped keys. **[Documented]**
Detail:
• Parent resource: `projects/{projectId}` or `projects/{projectId}/locations/{locationId}`; "Authorization requires the following IAM permission on the specified resource parent: serviceusage.services.use" (SDP docs, REST projects.content.reidentify page, read 2026-10-09) **[Documented]**
• DLP User (`roles/dlp.user`) is described as "Inspect, Redact, and De-identify Content" and holds `dlp.kms.encrypt` and `serviceusage.services.use` (SDP docs, roles and permissions page, read 2026-10-09) **[Documented]**
• The quickstart asks for Cloud KMS Admin, Cloud KMS CryptoKey Encrypter and DLP User on the project to wrap a key, de-identify and re-identify (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• Setup commands: verify billing is enabled and run `gcloud services enable dlp.googleapis.com cloudkms.googleapis.com` (SDP docs, quickstart De-identify and re-identify sensitive data page, read 2026-10-09) **[Documented]**
• "Note: When a Cloud Key Management Service wrapped key is used on deidentify or reidentify requests, API keys can't be used for authentication." (SDP docs, auth page, read 2026-10-09) **[Documented]**
• Key material: a 128-, 192- or 256-bit AES key, wrapped by a Cloud KMS key, passed as `kmsWrapped` with `cryptoKeyName` and `wrappedKey`; the wrapped key is base64 by default and clients must decode it to bytes (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• Key location: the Cloud KMS key must be in global or in the same region as the Sensitive Data Protection request (SDP docs, create-wrapped-key page, read 2026-10-09) **[Documented]**
• Cloud KMS: "Rotating keys creates new active key versions, but doesn't re-encrypt your data and doesn't disable or delete previous key versions." (Cloud KMS docs, not SDP docs, key rotation page, read 2026-10-09) **[Documented]**
• Cloud KMS: "After a key is destroyed, data that was encrypted with the key version can't be decrypted." (Cloud KMS docs, not SDP docs, destroy and restore page, read 2026-10-09) **[Documented]**
• Destroying the key version that wrapped the data key would stop re-identification, while rotation alone would not (premise: the wrapped key is a data encryption key encrypted by a Cloud KMS key, per the wrapped-key page and the REST CryptoKey schema, and the quickstart warns that destroying a key version stops decryption) **[Inferred]**
• A Singapore key and the Singapore endpoint satisfy the placement rule (premise: the rule asks for the key in global or in the request region, and Cloud KMS and SDP both list asia-southeast1) **[Inferred]**
• "When you use Cloud KMS for cryptographic operations, charges apply." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Free-text reversal needs the surrogate name: "To re-identify unstructured data, this entire token is required, including the surrogate annotation." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• Context must match: "If a context tweak is used to create the token, then this context tweak is also required for the de-identification transformations to be reversed." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• AES-SIV input rule: the summary table gives "At least 1 char long; no character set limitations." (SDP docs, pseudonymization page, read 2026-10-09) **[Documented]**
• FPE input rule: "At least 2 chars long; must be encoded as ASCII." and the alphabet "must be made up of at least 2 characters and contain no more than 95" (SDP docs, pseudonymization page, read 2026-10-09) and (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• "For input that varies in length or has length greater than 32 bytes, use CryptoDeterministicConfig." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**
• Content request limits: 0.5 MB per request, 3,000 findings, 100 transformations and 50,000 table values per request (SDP docs, limits page, read 2026-10-09) **[Documented]**
• The limits table is headed as covering "inspecting and de-identifying content sent directly to the DLP API" and does not name re-identification; the same limits probably also apply to `content.reidentify` (premise: re-identification is a content method with the same request shape) **[Inferred]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint (SDP docs, limits page, read 2026-10-09) **[Documented]**
• "Note: Quotas and limits specified in this document are subject to change." (SDP docs, limits page, read 2026-10-09) **[Documented]**
• Billing: the pricing page marks `projects.content.reidentify` and `projects.content.deidentify` as billed for both content inspection and content transformation (Sensitive Data Protection pricing page, read 2026-10-09) **[Documented]**
• The first 1 gibibyte per month per account of content inspected and of content transformed is $0.00 (Free); a minimum of 1 KB is billed per content inspect or transform request (Sensitive Data Protection pricing page, read 2026-10-09) **[Documented]**
• SLA: "Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests (Sensitive Data Protection SLA page, read 2026-10-09) **[Documented]**
• No uptime objective for `content.reidentify` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**
• The SDP audit-logging page lists InspectContent, DeidentifyContent, ReidentifyContent and RedactImage with audit log type "Data access" (SDP docs, audit-logging page, read 2026-10-09) **[Documented]**
• The Cloud Logging audit log reference says the request field "should never include user-generated data, such as file contents" (Cloud Logging docs, not SDP docs, read 2026-10-09) **[Documented]**
• Content strings, tokens and wrapped keys are therefore not expected in audit entries (premise: that rule applies to SDP audit logs; the SDP page does not restate it) **[Inferred]**
• Client install: `pip install google-cloud-dlp` (README.rst@google-cloud-dlp-v3.40.0:88) and Python 3.10 or later (setup.py@google-cloud-dlp-v3.40.0:95) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing, the DLP and Cloud KMS APIs enabled, a KMS key and wrapped AES key in the chosen region, the DLP User role, the Python client, and labelled strings with known original values. Tokenise, re-identify and compare with the originals. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP and Cloud KMS APIs enabled; a Cloud KMS key (global or the region used for requests, for example `asia-southeast1`); a 256-bit AES key wrapped with it; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; a script calling `deidentify_content` then `reidentify_content` **[Inferred]**
• Synthetic strings only (names, emails, phone numbers, NRIC-style numbers), each with its known original, because the request data goes to Google even though it is not stored **[Inferred]**
• Round trip: tokenise with AES-SIV and a surrogate name, re-identify, and check that the output equals the input character for character, including mixed text, punctuation and non-English words **[Inferred]**
• Determinism: tokenise the same value twice and with two keys; check same key gives the same token and different keys give different tokens **[Inferred]**
• FPE edge cases: one-character values, values outside the chosen alphabet, values longer than 32 bytes, and non-ASCII text, to see the documented errors **[Inferred]**
• AES-SIV token length against input length on several inputs, to settle the length conflict in R4 **[Inferred]**
• LLM round trip: send a tokenised prompt to a model and re-identify its reply; vary the prompt so the model quotes, truncates, rewrites or lower-cases the tokens, and record which survive **[Inferred]**
• Hostile cases: a token typed by a user, a token made with another key, and a token whose surrogate name appears in ordinary text; record whether the call errors, leaves text unchanged or restores something **[Inferred]**
• Limits and placement: requests over 0.5 MB, over 3,000 findings, a KMS key in a different region from the request, and global versus `asia-southeast1` regional endpoint timings **[Inferred]**
• Cost: bytes inspected and transformed (free for the first gibibyte per month) plus Cloud KMS charges; the pricing page gives no per-method surcharge for tokenisation **[Inferred]**
• No emulator or offline mode was found in the docs read, so tests need network access to Google Cloud (checked the libraries, method-types and quickstart pages and the client README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Latency and throughput of AES-SIV versus FPE, how altered or forged tokens behave, what happens to old tokens when keys change, and whether re-identify accepts conversation or batch items.
Detail:
• Latency and throughput of AES-SIV and FPE per request: no figures (checked the transformation reference, pseudonymization, quickstart, limits, pricing and SLA pages); needs testing
• Whether token length follows the transformation table (same length) or the pseudonymization page (not preserved) for AES-SIV; needs testing
• Whether `content.reidentify` accepts conversation and batch items, since the REST text says only that the item "will be treated as text" (checked the reidentify REST pages and the pseudonymization page; table re-identification is shown in the transformation reference)
• Whether the 3,000-findings error and limit also apply to `content.reidentify` (the message is documented only on the de-identification page)
• How the service reports a token altered by a model (truncated, case-changed, split by whitespace), a token made with another key, or a surrogate name that appears naturally in text: error, unchanged text, or wrong text (needs testing)
• Effect of rotating or destroying a Cloud KMS key version on tokens already issued: the Cloud KMS pages say rotation does not disable earlier versions and destruction makes data encrypted with that version undecryptable, but no SDP page says how re-identification behaves (checked the quickstart, create-wrapped-key, pseudonymization and REST pages; needs testing)
• Which identity needs a Cloud KMS decrypt or use permission at request time: the REST schema names `dlp.kms.encrypt` for the sender of the request, the quickstart grants the caller KMS Admin, CryptoKey Encrypter and DLP User, and no page says whether the DLP service agent or the caller unwraps the key (checked the quickstart, create-wrapped-key, roles, auth pages and the REST schemas)
• Whether request bodies, tokens or wrapped keys appear in Cloud Audit Logs: the SDP page lists the content methods as Data Access audit methods and does not say what the entries contain (checked the audit-logging page; the general audit log reference says request fields should never include user-generated data; needs a look at a real log entry)
• Whether tokenised output and the key reach any Google training or product-improvement use: the general Google Cloud terms limit processing to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)
• SLO, latency and quota values for `content.reidentify` in particular (the SLA covers only inspect and deidentify; the limits page lists no per-method quota)
• Whether a key in `asia-southeast1` works end to end with the `asia-southeast1` regional endpoint (the wrapped-key page requires the key in global or the request region; test the Singapore pair)
### R9
Summary: Sensitive Data Protection docs (pseudonymization, transformation reference, quickstart, wrapped key, REST references, auth, roles, locations, limits), pricing and SLA pages, and the Python client source at tag 3.40.0.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization
• https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify
• https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key
• https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/reidentify
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/auth
• https://docs.cloud.google.com/sensitive-data-protection/docs/access-control/roles-permissions
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://cloud.google.com/sensitive-data-protection/sla
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/setup.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/README.rst
• https://docs.cloud.google.com/kms/docs/key-rotation
• https://docs.cloud.google.com/kms/docs/destroy-restore
• https://docs.cloud.google.com/kms/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/audit-logging
• https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DeidentifyContentResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectContentResponse
• https://cloud.google.com/terms
• https://cloud.google.com/terms/data-processing-addendum
• https://cloud.google.com/terms/service-terms
• https://cloud.google.com/terms/services
## Column SD5: Sensitive Data Protection: Sensitive-data detection and redaction in images
### R1
Summary: **Finds and blanks sensitive text and objects in images.** The service reads text in an image with OCR and also detects objects such as passports, photo ID cards, licence plates and faces (Preview). It returns boxes, or the image with opaque rectangles over matches. **[Documented]**
Detail:
• "Using infoType detectors, Sensitive Data Protection inspects a base64-encoded image and detects sensitive data within the image." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "Inspection and redaction are two distinct operations:" and the page defines both, so one image can be inspected without being changed (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Inspection "returns the detected InfoTypes, along with one or more set of pixel coordinates and dimensions." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Redaction "returns the redacted base64-encoded image in the same image format as the original image." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "In the returned image, the detected sensitive data elements are obscured by an opaque rectangle." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• "By default, Sensitive Data Protection uses black rectangles to obscure the redacted content, but you can specify a color for each infoType in your image redaction configuration." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection uses optical character recognition (OCR) to detect text within images." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection can classify and redact objects in images." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• An option redacts every piece of text found: "Sensitive Data Protection also contains an option to redact all detected text in an image." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• The release notes of 2025-07-04 add object redaction: "Sensitive Data Protection can detect and redact the following object infoTypes in images:" barcode, licence plate, person and whiteboard (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• Later object detectors: passport and photo ID card (2025-11-03), face in Preview (2025-12-15) and signature (2026-06-08) (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• The Python client at v3.40.0 exposes `redact_image` and `inspect_content` (google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:965 and google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:872) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Image safety classification uses the same two methods and is covered by the image safety classification column (premise: the image context infoTypes are requested through the same inspect and redact calls) **[Inferred]**
### R2
Summary: **Sensitive text and ID-type objects in pictures.** Text infoTypes run on text read from the image, and object detectors cover faces (Preview), passports, photo ID cards, signatures, licence plates, barcodes and whiteboards. **[Documented]**
Detail:
• "To detect text in images, specify any text-based infoType, such as PERSON_NAME and CREDIT_CARD_NUMBER in your inspection or redaction configuration." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "all other infoType detectors are text-based; when analyzing images, they first extract text from images and then analyze the text." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• The reference lists eight object infoTypes that "analyze image pixels and features directly" and describes them (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
  – `OBJECT_TYPE/PERSON/PASSPORT`: "Image of a person's passport card or passport booklet, which is often used for identification and travel purposes. Note that images of the inner visa-stamped pages might not be identified."
  – `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`: "Image of a person's photo ID card, which can be government-issued (for example, driver's license) or non-government-issued (for example, school ID or employee ID)."
  – `OBJECT_TYPE/PERSON/SIGNATURE`: "Image of a signature which is done by a human on some document for their identity verification."
  – `OBJECT_TYPE/PERSON/FACE`: "Image of a person's face." and `OBJECT_TYPE/PERSON`: "Image of a human-like figure, which can include a full body, a face, or other body parts."
  – `OBJECT_TYPE/LICENSE_PLATE`: "Image of a license plate, which is a government-issued vehicle identifier."
  – `OBJECT_TYPE/BARCODE`: "Image of a 1D or 2D barcode, which is a machine-readable image that represents a piece of data." and `OBJECT_TYPE/WHITEBOARD`: "Image of a whiteboard."
• The face detector is not generally available: "This infoType detector is in Preview." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• Preview features fall under the Pre-GA Offerings Terms, which exclude them from any SLA: "Pre-GA Offerings (i) may be changed, suspended or discontinued at any time without prior notice to Customer and (ii) are not covered by any SLA or Google indemnity." (Google Cloud Service Specific Terms, General Service Terms section 5, read 2026-10-09) **[Documented]**
• The face detector's use therefore carries no SLA (premise: the detector is a Pre-GA Offering because the docs call it Preview) **[Inferred]**
• "Default infoTypes don't include objects in images." so object detectors must be requested by name (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Documented use case: "Sanitize customer support uploads: Automatically redact account numbers and personal contact details in user-submitted screenshots before tickets are routed to support agents." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Documented use case: "Obfuscate sensitive data in scanned documents: Mask driver's licenses, national identity cards, and credit card numbers from uploaded PDF or image attachments before processing in downstream workflows." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• The redaction walkthrough uses an image with a handwritten Social Security number and notes "Sensitive Data Protection also redacted the year." (a match the author did not ask for) (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Default sensitivity scores of the object infoTypes (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
  – SENSITIVITY_HIGH: `OBJECT_TYPE/PERSON/FACE`, `OBJECT_TYPE/PERSON/PASSPORT`, `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`, `OBJECT_TYPE/PERSON/SIGNATURE`
  – SENSITIVITY_MODERATE: `OBJECT_TYPE/PERSON`, `OBJECT_TYPE/LICENSE_PLATE`
  – SENSITIVITY_LOW: `OBJECT_TYPE/BARCODE`, `OBJECT_TYPE/WHITEBOARD`
• Singapore: the text infoTypes `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` and `SINGAPORE_PASSPORT` are available in all locations (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• A Singapore NRIC printed in an image is therefore reachable by OCR followed by the text detector; this needs a test because no Singapore image example is given (premise: text infoTypes run on text extracted from images and the NRIC infoType is a text infoType) **[Inferred]**
• The object detectors for passports and photo ID cards are global; the docs do not say whether they recognise Singapore passports or NRIC cards (checked the infoType reference, release notes and image pages) **[Not disclosed]**
• OCR language and script coverage, handwriting accuracy and rotated or low-resolution text: not stated (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages) **[Not disclosed]**
• "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (SDP docs, sensitive-data-protection-overview page, read 2026-10-09) **[Documented]**
• Out of purpose: prompt injection or jailbreak text inside an image is not named as something the service looks for (premise: the overview's purpose sentence and the image pages checked, which name only infoType detection and redaction) **[Inferred]**
### R3
Summary: **Image bytes only, with no input or output flag.** One image per call, whether from a prompt, a response, a retrieved file or a tool result. Results are not stored in Google Cloud, and only the first frame of a multiframe image is used. **[Inferred]**
Detail:
• "To inspect an image for sensitive data, you submit a base64-encoded image to the content.inspect method." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• "To redact sensitive data from an image, submit the image to the DLP API's image.redact method." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• The client type is described as "Container for bytes to inspect or redact." and `ContentItem` carries it as `byte_item` beside `value` and `table` (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1562 and google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1671) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The `projects.image.redact` request body has `locationId`, `inspectConfig`, `imageRedactionConfigs[]`, `includeFindings`, `byteItem`, `inspectTemplate` and `deidentifyTemplate` (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• None of these fields marks direction, role or prompt type, so the same call is used for images from prompts, responses, retrieved files and tool inputs or outputs, with the caller supplying the bytes (premise: the request body fields listed above) **[Inferred]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• For inspection the client enum says "Only the first frame of each multiframe image is inspected. Metadata" (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1577) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, sensitive-data-protection-overview page, read 2026-10-09) **[Documented]**
• "Content methods are synchronous, stateless methods." and "Request data is encrypted in transit and is not stored." (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• Documents with embedded images are a different route: the inspect guide says other formats such as PDF, DOCX, XLSX and PPTX "may generate mixed findings" and the redact guide says "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." (SDP docs, inspecting-images page, read 2026-10-09) and (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Image scanning runs only in listed locations (see R6); in other regions images and documents with images are scanned as binary files (SDP docs, locations page, read 2026-10-09) **[Documented]**
• No system prompt or conversation context is read; the service sees the image and the configuration only (premise: the request fields above) **[Inferred]**
### R4
Summary: **OCR for text, direct pixel analysis for objects.** Text infoTypes run on text extracted from the image; object detectors look at pixels and return a box. Both go through the DLP API over REST or client libraries, on a global or regional endpoint. **[Documented]**
Detail:
• "In regions that support image scanning, Sensitive Data Protection uses OCR to find text-based infoTypes in images." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• Object scanning: "This scanning mode focuses on locating a specific item within the image and produces a bounding box around it." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any object infoTypes that are specified in the inspection or redaction configuration." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• Names, versions, architecture and training data of the OCR and object-detection models (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages and the release notes) **[Not disclosed]**
• "Image redaction is similar to image inspection, with one additional step." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Redaction targets are set per entry in `imageRedactionConfigs[]`: an `infoType`, or `redactAllText`, plus an optional `redactionColor` (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2766) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• With no infoType listed and redact-all-text false, the docstring says the API "will redact all text that it matches against all info_types" found (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2743) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "Note: If you include infoTypes in the imageRedactionConfigs object, Sensitive Data Protection ignores them." when `redactAllText` is set (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Colours are RGB values from 0 to 1: "Each value is between 0 and 1, inclusive." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Templates can drive redaction: `deidentifyTemplate` "The request fails if the type of the template's deidentifyConfig is not imageTransformations." (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• An image transformation holds a colour and one of selected infoTypes, all infoTypes or all text: `selectedInfoTypes`, `allInfoTypes`, `allText` (SDP docs, REST organizations.deidentifyTemplates page, read 2026-10-09) **[Documented]**
• Image-based rules refine results by position: "Image-based exclusion rules, which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings." (general availability 2026-02-23) (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• Such a rule "is silently ignored if the content being inspected is not an image" (docstring) (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:986) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and the location form `{parent=projects/*/locations/*}/image:redact`; regional endpoint form `dlp.REGION.rep.googleapis.com` (SDP docs, REST projects.locations.image.redact page, read 2026-10-09) and (SDP docs, api-endpoints page, read 2026-10-09) **[Documented]**
• Regional endpoint support for `asia-southeast1` (Singapore) is listed as Yes (SDP docs, locations page, read 2026-10-09) **[Documented]**
• API keys are accepted: "The image.redact method also supports API keys." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 (google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Model Armor docs, not SDP docs: Model Armor image screening (see the Model Armor column `Model Armor: Image screening with OCR and visual scanning`) says "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." (Model Armor overview page, read 2026-10-09) **[Documented]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column (Gemini Enterprise protect-sensitive-data page, read 2026-10-09) **[Documented]**
### R5
Summary: **Bounding boxes or a redacted image, with a likelihood.** Inspection returns each detected infoType with a likelihood bucket and pixel boxes. Redaction returns the image with rectangles drawn and, if asked, the findings. There is no allow or block verdict. **[Documented]**
Detail:
• "The output of an inspection operation includes the detected infoTypes, the likelihood of the match, and pixel coordinates and length values that indicate the areas within which Sensitive Data Protection found the sensitive data." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• A finding in the guide's sample holds `infoType` (with `sensitivityScore`), `likelihood`, `location.contentLocations[].imageLocation.boundingBoxes[]` (`top`, `left`, `width`, `height`), `createTime` and `findingId` (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• "Be aware that Sensitive Data Protection often uses multiple boxes to indicate where a single instance of sensitive data is in the image." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• For object infoTypes "the inspection result doesn't include a quote for the detected object." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• Bounding-box origin, statement 1 (REST reference and client): "Top coordinate of the bounding box. (0,0) is upper left." (SDP docs, REST InspectResult page, read 2026-10-09) **[Documented]**
• Bounding-box origin, statement 2: "The coordinates at the bottom left corner of an image are (0,0)." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• Bounding-box origin, statement 3: boxes are described by "the bottom-left corner and the dimensions of bounding boxes, respectively." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• The client agrees with statement 1: google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2641 **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No match, inspection: "it returns an empty, successful HTTP 200 response." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• No match, redaction: "it returns the base64-encoded image unchanged." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Redaction response `redactedImage`: "The redacted image. The type will be the same as the original image." (SDP docs, REST RedactImageResponse page, read 2026-10-09) **[Documented]**
• Redaction response `extractedText`: "If an image was being inspected and the InspectConfig's includeQuote was set to true, then this field will include all text, if any, that was found in the image." (SDP docs, REST RedactImageResponse page, read 2026-10-09) **[Documented]**
• Redaction response `inspectResult`: "The findings. Populated when includeFindings in the request is true." (SDP docs, REST RedactImageResponse page, read 2026-10-09) **[Documented]**
• Setting `includeQuote` returns all recognised text to the caller, so the response itself holds the sensitive text that redaction was meant to hide (premise: the extractedText description above) **[Inferred]**
• Threshold: findings below `minLikelihood` are dropped and "returns only the findings with a likelihood of POSSIBLE and higher" when it is unset; five levels from VERY_UNLIKELY to VERY_LIKELY, no numeric score (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• The likelihood page describes each level (for example "Useful if you want a balance of precision and recall." for POSSIBLE) but gives no recommended level for images (SDP docs, likelihood page, read 2026-10-09) **[Not disclosed]**
• The redaction guide shows a request with `minLikelihood` set to LIKELY inside `inspectConfig` ("Code example with likelihood setting") (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Redaction responses carry no allow or block field, only the image, optional text and optional findings (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2845) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Published precision, recall, false-positive rate, OCR error rate or per-object detection accuracy (checked the image concepts, inspect, redact, likelihood and infoType reference pages and the release notes; the likelihood page only defines the terms) **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location, up to 4 MB; formats disagree.** The docs name PNG, JPEG and BMP most often, while SVG, GIF and TIFF appear on only some pages. Redaction requests are capped at 4 MB and other content requests at 0.5 MB. **[Documented]**
Detail:
• Format conflict, statement 1 (REST reference for `byteItem`): "The content must be PNG, JPEG, SVG or BMP." (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• Format conflict, statement 2 (redaction guide): "Sensitive Data Protection can redact sensitive data from many image types, including JPEG, BMP, and PNG." and "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Format conflict, statement 3 (supported file types, inspection and de-identification table, image row): extensions "bmp, gif, jpe, jpeg, jpg, png", scanning modes OCR, image content detection and image content classification, transformation support Redaction (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• Format conflict, statement 4 (inspect guide): "Sensitive Data Protection can inspect many image types for sensitive data, including JPEG, BMP, PNG, and SVG." (SDP docs, inspecting-images page, read 2026-10-09) **[Documented]**
• Format conflict, statement 5 (method-types page): "Redact sensitive data from uploaded images: Obfuscate sensitive text in image formats (such as JPEG, PNG, or TIFF)" (SDP docs, concepts-method-types page, read 2026-10-09) **[Documented]**
• Format conflict, statement 6 (client enum, surface only): `IMAGE` ("Any image type."), `IMAGE_JPEG`, `IMAGE_BMP`, `IMAGE_PNG` and `IMAGE_SVG`, and no GIF value (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1625) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client docstring for the redact request repeats the REST wording: "The content must be PNG, JPEG, SVG or BMP." (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2705`) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The supported-file-types page also has a discovery table whose Images cluster lists "bmp, gif, heic, ico, jpe, jpeg, jpg, pm, png, svg, tiff, webp" and says "Supported images (bmp, gif, jpe, jpeg, jpg, and png) smaller than 4 MiB are scanned using OCR"; this table is for discovery, not content methods (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• PNG, JPEG and BMP are the formats named by the REST reference, the redaction guide, the inspect guide and the client enum; SVG, GIF and TIFF are disputed, so tests should use PNG, JPEG and BMP first (premise: the REST reference, the redaction guide, the inspect guide and the client enum agree on these three) **[Inferred]**
• Size: "Maximum size of each projects.image.redact request | 4 MB" and "Maximum size of each request, except projects.image.redact | 0.5 MB" (SDP docs, limits page, read 2026-10-09) **[Documented]**
• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`, so larger images need `image.redact` or a storage inspection job (premise: the 0.5 MB limit is listed for content sent directly to the API and image.redact has its own 4 MB entry) **[Inferred]**
• "If you need to inspect files that are larger than these limits, store those files on Cloud Storage and run an inspection job." (SDP docs, limits page, read 2026-10-09) **[Documented]**
• Locations: "Image inspection and redaction are supported only in the following locations:" global, asia, asia-southeast1, europe, europe-north1, us, us-central1, us-east4, us-west1 (SDP docs, locations page, read 2026-10-09) **[Documented]**
• "If you attempt to inspect images or documents that contain images in a region that doesn't support image scanning, Sensitive Data Protection scans those files as binary files." (SDP docs, locations page, read 2026-10-09) **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22 (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• "When you redact data from images, you can't include limits in your inspection configuration." and "If you set the limits field in your request, Sensitive Data Protection generates an error." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Default detectors, statement 1: "Unless you specify specific information types (infoTypes) to search for, Sensitive Data Protection searches for the most common infoTypes." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Default detectors, statement 2: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated." (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• For images, the redaction guide says "Default infoTypes don't include objects in images." (SDP docs, redacting sensitive data in images page, read 2026-10-09) **[Documented]**
• Advice from the infoType concepts page: "Always specify infoType detectors explicitly. Don't use an empty infoTypes list." (SDP docs, concepts-infotypes page, read 2026-10-09) **[Documented]**
• Encoding and parameters: REST callers base64-encode the image; client libraries take bytes; optional `includeFindings`, `inspectConfig`, `imageRedactionConfigs`, `inspectTemplate` and `deidentifyTemplate` (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User (`roles/dlp.user`); an API key also works for `image.redact` (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• "You can use a Google Cloud console API key to authenticate to the DLP API for some methods, including all projects.content.* and projects.image.* methods." (SDP docs, auth page, read 2026-10-09) **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint; values "are subject to change" (SDP docs, limits page, read 2026-10-09) **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection and not for content transformation; the first 1 gibibyte per month is free, minimum 1 KB per request (Sensitive Data Protection pricing page, read 2026-10-09) **[Documented]**
• "Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests (Sensitive Data Protection SLA page, read 2026-10-09) **[Documented]**
• No uptime objective for `image.redact` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, the Python client, and a regional endpoint such as Singapore. Prepare synthetic images with known text and objects and hand-drawn box coordinates, send each to inspect and redact, and score matches and boxes. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; calls to `inspect_content` and `redact_image` in a supported location such as `asia-southeast1` through `dlp.asia-southeast1.rep.googleapis.com` **[Inferred]**
• Labelled set: synthetic images with the text type and pixel box marked for each item (names, emails, phone numbers, synthetic NRIC-style numbers, card numbers) and the object type and box marked for each passport, photo ID card, face, signature, licence plate, barcode and whiteboard **[Inferred]**
• Conditions to vary: screenshots, scans, photographs, rotated and skewed text, low resolution, small fonts, handwriting, non-English text, and AI-generated images **[Inferred]**
• Negative images with no sensitive content, and look-alikes (play money, sample ID cards, fake plates), to measure false positives **[Inferred]**
• Score boxes by overlap with the ground-truth box, because the docs say several boxes can describe one instance **[Inferred]**
• Formats: PNG, JPEG and BMP first, then SVG, GIF and TIFF, and an image just above and below 0.5 MB and 4 MB, to settle the format and size conflicts **[Inferred]**
• Compare `content.inspect` boxes with `image.redact` output, and check the coordinate origin of returned boxes (upper left or bottom left) **[Inferred]**
• Run the same images in a supported and an unsupported region to see what a non-supporting location returns **[Inferred]**
• Use only synthetic or consented images; the request data is not stored but is processed by Google, and bytes inspected count towards the free first gibibyte per month **[Inferred]**
• No emulator or offline mode was found, so every test needs network access to Google Cloud (checked the libraries, method-types and image pages and the client README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Which image formats really work, how accurate OCR and object detection are, which box origin is correct, whether Singapore IDs and non-English text are read, and what a non-supporting region does.
Detail:
• Which image formats `content.inspect` and `image.redact` accept (PNG, JPEG, BMP, SVG, GIF, TIFF); six statements disagree (needs testing)
• Whether the 4 MB and 0.5 MB limits apply to the base64 text or to the decoded bytes (checked the limits page and the REST references; not stated)
• Which bounding-box origin the API returns, upper left or bottom left (needs testing)
• Accuracy, recall and false-positive rates for text in images and for each object detector (checked the image and infoType reference pages and the release notes; none published)
• OCR languages and scripts, handwriting, rotated text and minimum text size (checked the same pages; not stated)
• Whether the passport and photo ID card detectors recognise Singapore passports and NRIC cards, and whether FIN cards are covered (needs testing with synthetic images)
• What `content.inspect` or `image.redact` returns in a region without image scanning: an error, a binary scan, or silently empty results (the locations page describes files, not content calls)
• Whether redaction of overlapping or adjacent findings leaves partial text visible, and how box padding is chosen (needs testing)
• Latency and throughput for images of different sizes (checked the limits, pricing and SLA pages; none published)
• Launch stage of the other object detectors and of the three image-context detectors: the reference marks only the face detector as Preview and the release notes say "available" without a stage (checked the reference and release notes of 2025-11-03, 2025-12-15, 2026-01-16 and 2026-06-08)
• Whether the redacted image strips metadata such as EXIF; the REST text says metadata is omitted for multiframe images only (needs testing)
• How a content policy or Model Armor image screening differs in practice from calling `image.redact` directly (cross-reference only; content policies are inventory-only)
• Customer data terms for images sent to the API: the general Google Cloud terms limit processing of Customer Data to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms)
### R9
Summary: Sensitive Data Protection docs (image concepts, inspect and redact guides, supported file types, locations, infoType reference, REST references, limits), pricing and SLA pages, release notes, and the Python client source at tag 3.40.0.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/auth
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://cloud.google.com/sensitive-data-protection/sla
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
• https://cloud.google.com/terms
• https://cloud.google.com/terms/data-processing-addendum
• https://cloud.google.com/terms/service-terms
• https://cloud.google.com/terms/services
## Column SD6: Sensitive Data Protection: Image safety classification (sexual and violent content)
### R1
Summary: **Whole-image safety labels for sexual and violent content.** Three image context detectors judge the overall subject of an image rather than objects inside it. Inspection reports a finding for the image, and redaction based on them blanks the entire image. **[Documented]**
Detail:
• "Sensitive Data Protection can classify and redact images based on their thematic content. This feature helps you identify images that contain sensitive or harmful subject matter according to predefined safety categories." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection analyzes an image's overall context and meaning to determine if it belongs to categories such as sexually explicit or violent content." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "You can use this feature to support content moderation and enforce acceptable use policies." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• The reference lists three image context infoTypes: `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`, `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE` and `IMAGE_TYPE/CONTEXT/VIOLENCE`, introduced as detectors that "analyze an entire image for sensitive or harmful subject matter" (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• "Unlike object detection, which identifies specific items within an image, this feature assesses the image's subject matter as a whole." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "If you configure redaction based on image safety, this feature redacts the entire image." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Release notes of 2026-01-16: "The following infoType detectors are available in global and the asia, europe, and us multi-regions:" the three image context detectors (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• Release notes of 2026-06-23: "Image safety classification infoTypes are now supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• The calls are the image inspection and redaction methods of the image detection and redaction column (`inspect_content` and `redact_image` in the Python client) (google/cloud/dlp_v2/services/dlp_service/client.py@google-cloud-dlp-v3.40.0:965) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R2
Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a one-sentence definition, and the docs describe the use as content moderation. **[Documented]**
Detail:
• `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`: "A finding of this type indicates that an image contains adult content of a sexual nature." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• Same entry: "Adult content might include elements such as nudity, specific contours or shapes of reproductive body parts, sexual activities, or pornographic images including photo-realistic or cartoon in nature." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE`: "A finding of this type indicates that an image contains racy or sexually suggestive content. Racy content might include elements like revealing clothing, lewd or provocative poses or themes, or other sexually suggestive material." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• `IMAGE_TYPE/CONTEXT/VIOLENCE`: "A finding of this type indicates that an image contains violent or gory content either real or fictionalized." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• Same entry: "Violent content might include imagery related to death, serious injury, or harm to an individual or group of individuals or animals." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• All three carry the default sensitivity score SENSITIVITY_HIGH and the category CONTEXTUAL_INFORMATION in the reference tables (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• The reference lists only these three image context detectors; categories such as hate symbols, self-harm, weapons or child safety are not named (checked the infoType reference, image concepts page and release notes) **[Not disclosed]**
• Generated images are a stated weak point: "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "their effectiveness in detecting all types of policy-violating content in AI-generated images can vary" (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• On AI-generated images the page says these might not be detected: nuanced or subtle content; context-dependent scenarios such as private settings; non-graphic depictions of sensitive themes (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "We recommend that you conduct thorough testing for your specific generative AI use cases to ensure that the results meet your safety requirements." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• The document-category infoTypes of the sensitive-data detection in text column include `DOCUMENT_TYPE/CONTEXT/SEXUAL` ("Content contains sex-related topics."), `DOCUMENT_TYPE/CONTEXT/OFFENSIVE` ("Content contains offensive topics.") and `DOCUMENT_TYPE/CONTEXT/OBSCENE` ("Content contains obscene topics.") (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• These are the text-side analogues of the image categories (premise: the descriptions refer to topics in documents; whether they run on a plain string is open, see the sensitive-data detection in text column) **[Inferred]**
• The reference introduces document classification as "To help with document risk assessment and policy enforcement, Sensitive Data Protection can classify documents into enterprise, sensitive, and regulated content categories." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• Out of purpose: prompt injection, jailbreaks, toxicity in text and topic control are not named on the image concepts, inspect, redact and infoType reference pages (premise: the overview's purpose sentence) **[Inferred]**
• Input basis: the classifier works on pixels, not on extracted text: "can analyze image pixels and features directly, rather than text extracted from images." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
### R3
Summary: **Whole images as bytes, with no input or output flag.** The same call can score a user upload or an image a model generated. The whole image is judged, multiframe images use the first frame only, and results are not stored in Google Cloud. **[Inferred]**
Detail:
• "When performing image safety classification, Sensitive Data Protection analyzes the entire image." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• The input is image bytes in the same `ByteContentItem` used by the image detection and redaction column: "Container for bytes to inspect or redact." (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:1562) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The image methods have no direction, role or prompt-type field (SDP docs, REST projects.image.redact page, read 2026-10-09), so uploads, model-generated images, retrieved images and tool outputs go through the same call (premise: the request body fields in the REST page) **[Inferred]**
• The docs name AI-generated images as an expected input, which is the response-side case: "If you use image context infoTypes on AI-generated images, the following might not be detected:" (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." (SDP docs, REST projects.image.redact page, read 2026-10-09) **[Documented]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." (SDP docs, sensitive-data-protection-overview page, read 2026-10-09) **[Documented]**
• The classification mode "can analyze image pixels and features directly, rather than text extracted from images." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• No system prompt or conversation context is read; the image and the configuration are the only inputs (premise: the request fields listed above) **[Inferred]**
### R4
Summary: **A classifier over the whole image.** Image context detectors run an image content classification mode that assigns one theme or category. The models are described as trained mainly on real-world images. Rules can use the findings from June 2026. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any image context infoType detectors that are specified in the inspection or redaction configuration." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• Model names, architecture, training data and evaluation sets for the image safety classifiers (checked the image concepts, supported-file-types, infoType reference and release-note pages) **[Not disclosed]**
• Image safety findings can act as context in rules: the 2026-06-23 release note says they are "supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." (SDP docs, release-notes page, read 2026-10-09) **[Documented]**
• "Sensitive Data Protection excludes a target infoType finding if the bounding box of a context infoType has the specified relationship with the target infoType finding." and "you must set the matchingType field to MATCHING_TYPE_RULE_SPECIFIC." (SDP docs, creating-custom-infotypes-rules page, read 2026-10-09) **[Documented]**
• The rules page shows no example that uses an image context infoType (checked the page for IMAGE_TYPE) **[Not disclosed]**
• Such a rule "is silently ignored if the content being inspected is not an image" (google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:986) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access is the DLP API over REST (`POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and `content:inspect`), global or regional endpoint, or the client libraries (SDP docs, REST projects.image.redact page, read 2026-10-09) and (SDP docs, api-endpoints page, read 2026-10-09) **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 (google/cloud/dlp/gapic_version.py@google-cloud-dlp-v3.40.0:16) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column (Gemini Enterprise protect-sensitive-data page, read 2026-10-09) **[Documented]**
### R5
Summary: **A rated finding for the image, or a fully blanked image.** The docs say classification produces a label, and give a likelihood bucket per finding rather than a number. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• The scanning-modes table lists ImageLocation as the additional location detail for image content classification, as it does for OCR and object detection; what box a whole-image finding carries is not shown (SDP docs, supported-file-types page, read 2026-10-09) **[Documented]**
• A finding carries `infoType`, `likelihood`, `location` and, when requested, `quote` (SDP docs, REST InspectResult page, read 2026-10-09) **[Documented]**
• Each category is its own infoType, so one image can in principle produce one finding per category (premise: each category is a separate infoType and a finding carries one infoType) **[Inferred]**
• Redaction by image safety replaces the whole image: "this feature redacts the entire image." and the response holds `redactedImage` of the same type as the original (SDP docs, concepts-image-redaction page, read 2026-10-09) and (SDP docs, REST RedactImageResponse page, read 2026-10-09) **[Documented]**
• With `includeFindings` set, the redact response also holds `inspectResult`: "The findings. Populated when includeFindings in the request is true." (SDP docs, REST RedactImageResponse page, read 2026-10-09) **[Documented]**
• In the client, `RedactImageResponse` has the fields `redacted_image`, `extracted_text` and `inspect_result` and no allow or block field (`google/cloud/dlp_v2/types/dlp.py@google-cloud-dlp-v3.40.0:2845` class RedactImageResponse) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The caller therefore maps findings to a decision (premise: the response holds only the image, the text and the findings) **[Inferred]**
• Threshold: findings below `minLikelihood` are dropped, with POSSIBLE as the default; five levels, no numeric score (SDP docs, likelihood page, read 2026-10-09) **[Documented]**
• A recommended minimum likelihood for image safety, or a calibrated threshold per category (checked the likelihood, image concepts and infoType reference pages) **[Not disclosed]**
• Worked request or response samples for `IMAGE_TYPE/CONTEXT/*` (checked the inspect guide, redact guide, image concepts page, supported-file-types page and REST references; the infoType names appear only in the reference and release notes) **[Not disclosed]**
• Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location; categories must be named.** Image context detectors have to be requested in the configuration, and image scanning runs only in listed locations, including Singapore. Format and size rules are those of other image calls, whose format statements conflict. **[Inferred]**
Detail:
• "To perform image safety classification, specify image context infoTypes in your inspection or redaction configuration." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**
• For images, the redaction guide says "Default infoTypes don't include objects in images." (SDP docs, redacting sensitive data in images page, read 2026-10-09) **[Documented]**
• Whether a request with no infoTypes also runs image context detectors is not stated; the quoted sentence is about objects and is silent on image context infoTypes (checked the redact, inspect and REST pages) **[Not disclosed]**
• Availability: "Availability indicates the regions or multi-regions where the infoType is supported." (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• For the three image context infoTypes the availability column lists asia, asia-southeast1, europe, europe-north1, global, us, us-central1, us-east4 and us-west1 (SDP docs, infotypes-reference page, read 2026-10-09) **[Documented]**
• "Image inspection and redaction are supported only in the following locations:" the same nine locations (SDP docs, locations page, read 2026-10-09) **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22, and the locations page lists a regional endpoint for it (SDP docs, release-notes page, read 2026-10-09) and (SDP docs, locations page, read 2026-10-09) **[Documented]**
• Input handling uses the same methods and body as the image detection and redaction column (image bytes, 4 MB for `image.redact`, 0.5 MB for other content requests, format statements that conflict), so those rules and that conflict carry over (premise: both columns call the same image methods with the same request body) **[Inferred]**
• "When you redact data from images, you can't include limits in your inspection configuration." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User; API keys are accepted for `projects.image.*` methods (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) and (SDP docs, auth page, read 2026-10-09) **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection only; the pricing page lists no separate price for image safety classification (Sensitive Data Protection pricing page, read 2026-10-09) **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint (SDP docs, limits page, read 2026-10-09) **[Documented]**
• Launch stage of the three detectors (general availability or Preview) is not stated beyond the release note that says they are "available" (checked the infoType reference, which marks only the face detector, and the release notes of 2026-01-16) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, the Python client, and an image-scanning location such as Singapore. Build a lawful, approved image set labelled by category, real and AI-generated, send each image asking for the three detectors, and compare findings with human labels at several thresholds. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; calls to `inspect_content` with the three `IMAGE_TYPE/CONTEXT/*` infoTypes in `asia-southeast1` or global **[Inferred]**
• Terms for the bench: the Service Specific Terms let the customer run benchmark tests itself and publish results only with all information needed to replicate them and a reciprocal right for Google (Google Cloud Service Specific Terms, General Service Terms section 7, read 2026-10-09) **[Documented]**
• Test images must not be illegal content or non-consensual explicit imagery under the Acceptable Use Policy (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**
• Labelled set: images that a reviewer marks as sexually explicit, sexually suggestive, violent or gory, or none of these; with ground truth at image level, since the classifier assigns a whole-image category **[Inferred]**
• Borderline and look-alike images: medical and anatomical drawings, classical art, swimwear and sport, news and war photography, film stills, cartoons and game screenshots, to measure false positives **[Inferred]**
• Real versus AI-generated images in equal numbers, because the docs warn that results on generated images can differ **[Inferred]**
• Threshold sweep over `minLikelihood` (POSSIBLE, LIKELY, VERY_LIKELY) per category, since no recommended level is published **[Inferred]**
• Redaction check: send images through `redact_image` with each detector and confirm that the entire image is covered, and that unflagged images come back unchanged **[Inferred]**
• Image variants: cropped, resized, compressed, watermarked, rotated, and text-only images with offensive words, to see what the classifier reacts to **[Inferred]**
• Handling: use only lawful sample images approved for testing and store them with access controls; the request data is not stored but is processed by Google, and bytes inspected count towards the free first gibibyte per month **[Inferred]**
• No emulator or offline mode was found, so tests need network access to Google Cloud (checked the libraries and image pages and the client README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Accuracy and thresholds per category, what a whole-image finding looks like, how generated images and local norms affect results, and whether text in an image or a missing infoType list changes the outcome.
Detail:
• Accuracy, precision and recall of each category on real and AI-generated images (checked the image concepts, infoType reference and release-note pages; none published)
• How strictly "racy" and "sexually suggestive" are defined, and whether the labels reflect Singapore community norms (the reference gives a one-sentence definition only)
• What a whole-image finding returns for location: a box covering the image, no box, or another value (needs testing)
• A recommended `minLikelihood` for moderation use, and whether several categories can fire on one image (needs testing)
• Whether text printed in an image (offensive words, captions) affects the classifier (the docs say it uses pixels and features rather than extracted text; needs testing)
• Whether a request with no infoTypes runs the image context detectors (needs testing)
• Launch stage of the three detectors and whether more categories are planned (checked the infoType reference and release notes)
• Behaviour in a region without image scanning for a content call (the locations page describes files, not content calls)
• Latency and throughput of image classification (checked limits, pricing and SLA pages; none published)
• How the image format conflict recorded in the image detection and redaction column applies here (needs testing)
• Whether findings on very small, very large or multi-subject images are reliable, including minimum image size (not stated)
• How content-policy rules over image safety, documented only in Gemini Enterprise docs, differ from calling the image methods directly (cross-reference; content policies are inventory-only)
• Customer data terms for images sent to the API: the general Google Cloud terms limit processing of Customer Data to the Data Processing Addendum and no SDP-specific clause was found (checked the terms of service, Data Processing Addendum and Service Specific Terms). Acceptable-use limits for explicit or violent test images: the Google Cloud Acceptable Use Policy bars illegal content including child sexual exploitation and non-consensual explicit imagery and does not mention other explicit or violent test images; which test images are acceptable is decided in the bench design
### R9
Summary: Sensitive Data Protection docs (image concepts, supported file types, infoType reference, redact and inspect guides, rules, locations, REST references, limits), pricing page, release notes, and the Python client source at tag 3.40.0.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/auth
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult
• https://cloud.google.com/terms/aup
• https://cloud.google.com/terms
• https://cloud.google.com/terms/data-processing-addendum
• https://cloud.google.com/terms/service-terms
• https://cloud.google.com/terms/services
