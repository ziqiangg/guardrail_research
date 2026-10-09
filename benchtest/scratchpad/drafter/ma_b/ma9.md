
## Column MA9: Model Armor: Document screening (PDF, CSV, text and Office files)
### R1
Summary: **Screens the text inside uploaded documents.** Model Armor extracts text from supported PDF, CSV, text and Office files and runs the template's filters on it. Only the direct API and the Gemini Enterprise integration accept documents; other integrations take text only. **[Documented]**
Detail:
• Overview: "Model Armor can screen the following types of documents for safety, prompt injection and jailbreak attempts, sensitive data, and malicious URLs" (overview, read 2026-10-09) **[Documented]**
• Overview: "Text extracted from supported files is subject to the token system limits." (overview, read 2026-10-09) **[Documented]**
• The REST modality reference says the text modality will "sanitize text fields, and text extracted from rich text files (like PDFs, DOCs) and plain text files (like TXT)" (templates reference, read 2026-10-09) **[Documented]**
• Vendor blog (supporting only): "Document screening: It can also screen text in documents, including PDFs and Microsoft Office files, for malicious and sensitive content." (Google Cloud blog 2025-10-22, read 2026-10-09) **[Documented]**
• Release note 2025-06-08 first listed the Office types: "Model Armor supports screening text in the following document types for malicious content" (release notes, read 2026-10-09) **[Documented]**
• Direct REST API supports "all modalities, including text, documents, and images"; in integrations "only the Gemini Enterprise integration supports documents. All other integrations scan and sanitize only text." (integrations page, read 2026-10-09) **[Documented]**
• Product page: "Detects malicious files, malware, and unsafe URLs within AI prompts and responses." (product page, read 2026-10-09) **[Documented]**
• The REST result schema has a `virusScanFilterResult` type whose scanned content type note reads "PDF Scanning for only PDF is supported." (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Antivirus scanning is covered only in the inventory sheet, not as a Table 3 column; its configuration (a template setting, enable flag or threshold) is not found in the template reference, manage-templates page or overview (checked all three) **[To be verified]**
### R2
Summary: **Threats hidden in documents.** Targets safety violations, prompt injection, sensitive data and malicious URLs in a file's text. Listed types are PDF, CSV, TXT and modern Word, PowerPoint and Excel files. Images embedded in files are not screened, though one Google page says otherwise. **[Documented]**
Detail:
• Overview example: "if a PDF contains an embedded malicious URL, it can be used to compromise any downstream systems processing LLM outputs" (overview, read 2026-10-09) **[Documented]**
• Product page: "Stop embedded threats like indirect prompt injection where safe and legitimate prompts may be contaminated with malicious files and URLs." (product page, read 2026-10-09) **[Documented]**
• Supported types: PDF; CSV; TXT; Word DOCX, DOCM, DOTX, DOTM; PowerPoint PPTX, PPTM, POTX, POTM, POT; Excel XLSX, XLSM, XLTX, XLTM (overview, read 2026-10-09) **[Documented]**
• The REST enum for Excel lists "XLSX, XLSM, XLTX, XLYM" where the overview says XLTM, which looks like a typo in the enum description (DataItem reference and overview, read 2026-10-09) **[Documented]**
• Older binary Office formats (DOC, XLS, PPT), RTF, HTML, JSON, Markdown and archives are not in the list; no statement that they are rejected or ignored (checked the overview, sanitize page and DataItem reference) **[Not disclosed]**
• Filters that run on the extracted text: safety, prompt injection and jailbreak, sensitive data and malicious URLs, as listed in the overview sentence (overview, read 2026-10-09) **[Documented]**
• Sensitive Data Protection de-identification does not work on files: "Sensitive Data Protection de-identification is not supported for file-based prompts." (sanitize page, read 2026-10-09) **[Documented]**
• Rich documents with metadata labels: release note 2026-04-06 says Model Armor "can sanitize data passed in as rich documents that have specific metadata labels", using a custom metadata-label infoType in an advanced Sensitive Data Protection configuration (release notes, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (1): "Model Armor doesn't screen images embedded within files." (overview, image screening section, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (2): the integrations page says "images embedded in documents aren't screened" for Gemini Enterprise (integrations page, read 2026-10-09) **[Documented]**
• Source conflict on embedded images (3): the Gemini Enterprise page says it screens "Images contained inside other files and documents that you upload directly" (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Encoded content is not decoded: Base64, hexadecimal, URL-encoded and ciphertext inputs are not inspected (overview limitations, read 2026-10-09) **[Documented]**
• Audio and video are not supported (overview limitations, read 2026-10-09) **[Documented]**
• Scanned PDFs that hold only page images have no extractable text; whether any OCR is applied is not stated (checked the overview, sanitize page and quotas page) **[Not disclosed]**
### R3
Summary: **A base64 file in the prompt field.** The file goes in a byte item inside the prompt field, with its type set by hand. The result schema also lets a response carry a file, but the docs show no response-side example. Template modality must include text. **[Documented]**
Detail:
• Prompt side: `{"userPromptData":{"byteItem":{"byteDataType":"FILE_TYPE","byteData":"<base64>"}}}` posted to `:sanitizeUserPrompt` (sanitize page, file-based prompts section, read 2026-10-09) **[Documented]**
• "Model Armor doesn't automatically detect the file type. You must explicitly set the byteDataType field to indicate the file format." (sanitize page, read 2026-10-09) **[Documented]**
• Response side: the request field `modelResponseData` has the same data item type as `userPromptData`, which can be text or a byte item (sanitizeModelResponse and DataItem references, read 2026-10-09) **[Documented]**
• The generated Go request type has `ModelResponseData *DataItem`, the same type as the prompt field (service.pb.go@37f936ac:2379) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• No example in the sanitize page sends a document through `modelResponseData`; its response examples are text only (checked the sanitize page, overview and templates page) **[Not disclosed]**
• Whether a document in a model response is accepted, and how an LLM would produce one, is not stated; the overview example of a PDF "processing LLM outputs" is about downstream systems **[To be verified]**
• Template modality must allow text: `TEXT` "Scans text strings and text embedded in the supported file formats" and an empty `modalities` field scans only text (templates page and templates reference, read 2026-10-09) **[Documented]**
• With a single modality set, the other is skipped: "If you specify a single modality (IMAGE or TEXT), Model Armor skips the other and returns EXECUTION_SKIPPED." So an image-only template should skip documents **[Inferred]**
• Streaming methods are text only: "Model Armor streaming methods support only textual input, not attachments like images and files." (sanitize page, read 2026-10-09) **[Documented]**
• Integrations: Gemini Enterprise screens documents (such as PDFs) only when users upload them to the assistant; Agent Platform and Agent Gateway say documents or file uploads are not supported (integration pages, read 2026-10-09) **[Documented]**
• LangChain (Preview): the runnables "are limited to text screening. If a prompt includes a document, the system scans only the extracted text." (LangChain page, read 2026-10-09) **[Documented]**
• Model Armor inspects each file as a single-turn request, without history (overview, read 2026-10-09) **[Documented]**
### R4
Summary: **Text extraction then the ordinary filters.** Extraction happens inside the managed service on the direct API path and in the Gemini Enterprise integration, which discards a violating file whole. The extractor, its OCR and its handling of layout are not described. Preview or GA status for the file feature is unstated. **[Documented]**
Detail:
• Extraction engine, parser identity and handling of tables, headers, comments, hidden text or embedded objects are not described (checked the overview, sanitize page, templates reference, product page and release notes) **[Not disclosed]**
• Direct REST API and client libraries accept documents; the generated Go library defines the file types as enum values PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT, CSV, PLAINTEXT_UTF8 and IMAGE (service.pb.go@37f936ac:776) **[Documented: repo googleapis/google-cloud-go@37f936ac]**
• GA or Preview status for document screening is not labelled on the overview or sanitize pages (checked both and the release notes; the image feature is labelled Preview, documents are not) **[Not disclosed]**
• Gemini Enterprise route (GA 2025-09-16 per release notes): screens PDFs and other documents the user uploads; "If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise screens only uploads to the assistant, employee-made and Google-made agents; "Interactions with custom agents from your organization (such as ADK, A2A, and Dialogflow) are not screened." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise page: "There are no token limits when you use Model Armor with Gemini Enterprise." (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Gemini Enterprise does not de-identify: it blocks the request instead of masking content that triggers a Sensitive Data Protection infoType (integrations page and Gemini Enterprise page, read 2026-10-09) **[Documented]**
• Antivirus: the supported-features page lists "Antivirus scanning" as a filter in full-support regions and a column in the by-region table; the result type covers PDF only (feature availability page and SanitizationResult reference, read 2026-10-09) **[Documented]**
• Release note 2026-04-10 says the antivirus `virusDetails` field no longer includes security vendor names or threat signatures (release notes, read 2026-10-09) **[Documented]**
• Pricing: the pricing page counts "the total number of tokens in AI prompts and responses"; how files and extracted text are counted is not stated (pricing page, read 2026-10-09) **[Not disclosed]**
• Data handling: core data "includes prompts, responses, and input files", processed but not stored at rest (data residency page, read 2026-10-09) **[Documented]**
• Self-hosted or offline document screening is not described (checked the overview, product page and integrations page) **[Not disclosed]**
### R5
Summary: **The standard verdict, with limited location detail.** Output is the same per-filter result as for text. Malicious URL positions exist only for plain text, and sensitive data positions refer to the extracted text. Oversize files are skipped and tiny files are rejected. No score or accuracy figure is published. **[Documented]**
Detail:
• Output is the normal `sanitizationResult` with `filterMatchState`, `invocationResult` and per-filter results (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Malicious URL locations: "The locations field is supported only for plaintext content i.e. ByteItemType.PLAINTEXT_UTF8" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Sensitive data positions: "when the content is not textual, this references the UTF-8 encoded textual representation of the content" (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Finding containers: "The top level name is the source file name or table name." (SanitizationResult reference, read 2026-10-09) **[Documented]**
• Optional `fileLabel` on the byte item is "used to identify the file in the response" (DataItem reference, read 2026-10-09) **[Documented]**
• Which response field returns the file label is not shown (checked the SanitizationResult reference and sanitize page) **[Not disclosed]**
• Oversize file: "If a file exceeds this limit, Model Armor skips scanning the file." The result code or message for a skipped file is not stated (overview and quotas page, read 2026-10-09) **[Not disclosed]**
• Tiny file: requests for files under 69 bytes are rejected with an `InvalidDocumentInputException` error (overview and quotas page, read 2026-10-09) **[Documented]**
• Token overflow in extracted text: the filter returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, read 2026-10-09) **[Documented]**
• Gemini Enterprise acts on the verdict by discarding the whole file (Gemini Enterprise integration page, read 2026-10-09) **[Documented]**
• Antivirus result fields: `matchState`, `scannedContentType` (UNKNOWN, PLAINTEXT, PDF), `virusDetails`, `scannedSize` (SanitizationResult reference, read 2026-10-09) **[Documented]**
• No numeric score field exists in the SanitizationResult reference (searched the page text for "score") **[Not disclosed]**
• Published extraction accuracy or detection rates for documents are not given (checked the overview, product page, blog and release notes) **[Not disclosed]**
### R6
Summary: **Base64 bytes, a stated type and a 4 MB cap.** The byte data type must be set; files under 69 bytes fail and files over 4 MB are skipped. Extracted text counts against the filter token limits. Callers need the user role. **[Documented]**
Detail:
• `byteDataType` is required; the sanitize page lists PLAINTEXT_UTF8, PDF, WORD_DOCUMENT, EXCEL_DOCUMENT, POWERPOINT_DOCUMENT, TXT and CSV, and "If the field is missing or not specified, the request fails." (sanitize page, read 2026-10-09) **[Documented]**
• The REST enum adds IMAGE and maps WORD_DOCUMENT to DOCX, DOCM, DOTX, DOTM; EXCEL_DOCUMENT to XLSX, XLSM, XLTX; POWERPOINT_DOCUMENT to PPTX, PPTM, POTX, POTM, POT (DataItem reference, read 2026-10-09) **[Documented]**
• Size: "Supported files are limited to 4 MB in size." and the system limit table gives 4 MB for "All supported files and images" (overview and quotas page, read 2026-10-09) **[Documented]**
• Release note 2025-09-27 first set the 4 MB limit for files and text (release notes, read 2026-10-09) **[Documented]**
• Minimum size: files under 69 bytes are rejected "because such files are highly likely to be invalid" (overview, read 2026-10-09) **[Documented]**
• Token limits on extracted text: 65,536 for prompt injection, responsible AI and CSAM, 130,000 for Sensitive Data Protection, no limit in the Gemini Enterprise integration (quotas page, read 2026-10-09) **[Documented]**
• Malicious URL detection scans only the first 256 URLs in the extracted text (overview, read 2026-10-09) **[Documented]**
• Example command: `base64 -w 0 -i sample.pdf` piped into `jq` to build the JSON body (sanitize page, read 2026-10-09) **[Documented]**
• Roles: `roles/modelarmor.user` to sanitize; `roles/modelarmor.admin` to manage templates (sanitize page, read 2026-10-09) **[Documented]**
• Quota: 1,200 queries per minute per project; each file is one request (quotas page, read 2026-10-09) **[Documented]**
• The template's `modalities` field is optional; empty means text only (templates reference, read 2026-10-09) **[Documented]**
• Regional limits for documents are not stated separately; the by-region table lists filter, multi-language, CSAM, image and antivirus support, not documents (checked the feature availability page) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a project with the Model Armor API enabled, a template in a full-support region with the wanted filters, the user role, and base64 test files of each type. Use files of 69 bytes to 4 MB with planted injection text, fake sensitive data and test URLs, then call the prompt method. **[Inferred]**
Detail:
• **Minimum setup:** a project with billing and the Model Armor API enabled, a regional template with the filters you want to test (use a full-support region such as `us-central1` or the `us` multi-region, because limited-support regions drop some filters), `roles/modelarmor.user`, and base64-encoded files posted with `byteDataType` set to the file format **[Inferred]**
• Test files: one clean and one planted file per type (PDF, DOCX, XLSX, PPTX, CSV, TXT), with prompt-injection text, fake card numbers or SSNs, and a safe test URL; plus boundary files just under 69 bytes, around 4 MB, and a file with an embedded image **[Inferred]**
• Singapore (asia-southeast1) lists no malicious URL filter with data residency enforced, so URL tests there need the template's data residency enforcement turned off (feature availability page and release notes 2026-08-27, read 2026-10-09) **[Documented]**
• Standalone use costs nothing up to 2 million tokens per month, then $0.10 per million tokens (Security Command Center pricing page, read 2026-10-09) **[Documented]**
• Response-side document tests are exploratory because the docs show no example **[Inferred]**
• No self-hosted or offline option is documented (checked the overview, product page and integrations page) **[Not disclosed]**
### R8
Summary: **Key open questions.** Whether responses can carry documents, what the extractor does with scans and layout, what a skipped oversize file returns, whether embedded images are screened, how antivirus is configured, and what accuracy to expect.
Detail:
• Whether a model response can be sent as a file in `modelResponseData` (schema allows it; checked the sanitize page, overview, REST references and release notes, no example)
• The text extractor: scanned or image-only PDFs, tables, hidden text, comments, password-protected and corrupt files (checked the overview, quotas page and sanitize page, not stated)
• What the API returns for a file over 4 MB: an error, or a skipped filter result and which one (checked the overview and quotas page, not stated)
• Embedded images in files: not screened per the overview, screened per the Gemini Enterprise page (needs testing in both routes)
• Antivirus: configuration, supported file types beyond PDF, and whether it runs on documents sent through the REST API (checked the REST references, overview, manage-templates and release notes; only the result type, region table and 2026-04-10 note exist)
• Whether the Gemini Enterprise integration lists documents only (integrations table) or documents and images (Gemini Enterprise page)
• How files and extracted text are billed in tokens (checked the pricing page, not stated)
• Older Office formats and other file types: ignored, rejected or failed (needs testing)
• Whether the rich-document metadata-label feature needs special request fields beyond a custom infoType in an advanced Sensitive Data Protection template (checked the release note only)
• Whether LangChain's "scans only the extracted text" means document support or only text extracted client-side (checked the LangChain page, not stated)
• Whether filters report which page or sheet matched (checked the SanitizationResult reference; only character ranges and a container name)
### R9
Summary: Model Armor docs (overview, sanitize, templates, quotas, integrations, release notes, REST references, data residency, feature availability), the product and pricing pages, the Google Cloud blog, and the pinned Google Go client library.
Detail:
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/model-armor/sanitize-prompts-responses
• https://docs.cloud.google.com/model-armor/manage-templates
• https://docs.cloud.google.com/model-armor/quotas
• https://docs.cloud.google.com/model-armor/integrations
• https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
• https://docs.cloud.google.com/model-armor/model-armor-vertex-integration
• https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
• https://docs.cloud.google.com/model-armor/model-armor-langchain-integration
• https://docs.cloud.google.com/model-armor/feature-availability-by-region
• https://docs.cloud.google.com/model-armor/data-residency
• https://docs.cloud.google.com/model-armor/release-notes
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates
• https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates/sanitizeModelResponse
• https://docs.cloud.google.com/model-armor/reference/rest/v1/DataItem
• https://docs.cloud.google.com/model-armor/reference/rest/v1/SanitizationResult
• https://cloud.google.com/security/products/model-armor
• https://cloud.google.com/security-command-center/pricing
• https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps
• https://github.com/googleapis/google-cloud-go/blob/37f936ac9d69e173da0ba4123e382c52b2dd741f/modelarmor/apiv1/modelarmorpb/service.pb.go
