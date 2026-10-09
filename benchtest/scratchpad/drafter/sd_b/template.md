## Column SD4: Sensitive Data Protection: Reversible tokenisation and re-identification (AES-SIV and FPE)
### R1
Summary: **Reversible tokens for detected values.** De-identification can swap each detected value for an encrypted token, and a later re-identify call turns the token back into the original using the same key. Two reversible methods exist: AES-SIV and format-preserving encryption. **[Documented]**
Detail:
• "Pseudonymization is a de-identification technique that replaces sensitive data values with cryptographically generated tokens." {{D:pseudonymization}} **[Documented]**
• "Pseudonymization is sometimes referred to as tokenization or surrogate replacement." {{D:pseudonymization}}; the column header uses the British spelling tokenisation **[Documented]**
• "Pseudonymization techniques enable either one-way or two-way tokens. A one-way token has been transformed irreversibly, while a two-way token can be reversed." {{D:pseudonymization}} **[Documented]**
• The page's summary table marks deterministic encryption with AES-SIV and format preserving encryption (FPE-FFX) as Reversible and cryptographic hashing as not Reversible {{D:pseudonymization}} **[Documented]**
• Reversal is the `content.reidentify` method: "Re-identifies content that has been de-identified." {{D:REST projects.content.reidentify}} **[Documented]**
• The method accepts only two transformations: "This requires that only reversible transformations be provided here. The reversible transformations are:" followed by `CryptoDeterministicConfig` (AES-SIV) and `CryptoReplaceFfxFpeConfig` (FPE) {{D:REST projects.content.reidentify}} **[Documented]**
• Google recommends AES-SIV: "We recommend this method, because it provides the highest level of security among all the reversible cryptographic methods that Sensitive Data Protection supports." {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• The content-methods page lists the use case "Re-identify tokenized data on demand: De-tokenize previously pseudonymized tokens in authorized server-side workflows when an authenticated business user requires access to the original plaintext." {{D:concepts-method-types}} **[Documented]**
• The same page lists "De-identify or redact sensitive tokens from text strings synchronously before passing content to third-party APIs or large language models (LLMs)." as a use of content methods generally {{D:concepts-method-types}} **[Documented]**
• Tokenising a prompt before the model and re-identifying the reply afterwards is one way to apply this to an LLM flow; the docs read for this column describe no LLM round trip, and it needs the model to return the tokens unchanged **[Inferred]**
• Cryptographic hashing is the one-way contrast: "Unlike other types of crypto-based transformations, this type of transformation isn't reversible." {{D:transformations-reference}}; its row belongs to the SD3 column **[Documented]**
• The Python client at v3.40.0 exposes `reidentify_content` and `deidentify_content` ({{L:C|def reidentify_content(}} and {{L:C|def deidentify_content(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R2
Summary: **Keeps raw values away from downstream systems.** Tokens replace detected personal or secret values, repeat consistently for the same key, and can be reversed only with that key. Which values are tokenised depends on the detectors in the request. **[Documented]**
Detail:
• "Enable secure reversibility for authorized workflows: Use two-way encryption (such as AES-SIV or FPE) with keys stored in Cloud Key Management Service so that only authenticated and privileged backend services can de-tokenize the original values when legally required." {{D:pseudonymization}} **[Documented]**
• "Preserve referential integrity across analytical datasets: Replace customer IDs and primary keys with consistent cryptographic tokens so teams can join and aggregate tables in BigQuery without exposing sensitive identifiers." {{D:pseudonymization}} **[Documented]**
• Referential integrity is defined as "Given the same crypto key and context tweak, a table of data will be replaced with the same obfuscated form each time it is transformed" {{D:pseudonymization}} **[Documented]**
• "Transient cryptographic keys only keep integrity per API request." {{D:pseudonymization}} **[Documented]**
• Repeated values leak equality, and the docs say so: "In situations where repetitive data or data patterns might occur, the risk of re-identification increases." {{D:pseudonymization}} **[Documented]**
• For FPE the docs add: "In situations where the number of possible character strings is small, either increase the radix of the alphabet or use a context tweak." {{D:pseudonymization}} **[Documented]**
• Values are chosen by detection: "The most common way to do this is to use a built-in or custom infoType detector to match on the desired sensitive data values." {{D:pseudonymization}} **[Documented]**
• Structured data can also be tokenised by whole column: "you can also perform tokenization on entire columns of data using record transformations" {{D:pseudonymization}} **[Documented]**
• Detection coverage (PII, government IDs including Singapore NRIC and passport, credentials) is the subject of the SD1 and SD2 columns; a value the detectors miss is not tokenised, which follows from transformations being applied to findings **[Inferred]**
• An infoType transformation names the infoTypes it applies to, so tokenising a Singapore NRIC means listing its infoType in the transformation; the docs examples use PHONE_NUMBER and EMAIL_ADDRESS, not a Singapore type {{D:transformations-reference}} **[Inferred]**
• "Country-specific infoTypes support the English language and the respective country's languages. Most global infoTypes work with multiple languages." This covers the detection step that feeds tokenisation {{D:concepts-infotypes}} **[Documented]**
• FPE exists for fixed formats: "This allows the output to be used in systems that have format validation on length. This is useful for legacy systems where string length must be maintained." {{D:transformations-reference}} **[Documented]**
• Scope statement: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• Prompt injection, jailbreaks, toxicity and topic control are not described as functions of tokenisation or of the service (checked the overview, method-types, pseudonymization, transformation-reference and quickstart pages; none mentions them) **[Not disclosed]**
### R3
Summary: **One text or table item per call, with no input or output flag.** Prompts, responses, retrieved text and tool results all go through the same two calls. Content methods are stateless and results are not stored in Google Cloud. **[Inferred]**
Detail:
• For `content.deidentify` the REST reference says "The item to de-identify. Will be treated as text." and "This value must be of type Table if your deidentifyConfig is a RecordTransformations object." {{D:REST projects.content.deidentify}} **[Documented]**
• For `content.reidentify`: "The item to re-identify. Will be treated as text." {{D:REST projects.content.reidentify}} **[Documented]**
• The `content.deidentify` request body has the fields `deidentifyConfig`, `inspectConfig`, `item`, `inspectTemplateName`, `deidentifyTemplateName` and `locationId` {{D:REST projects.content.deidentify}} **[Documented]**
• The `content.reidentify` request body has the fields `reidentifyConfig`, `inspectConfig`, `item`, `inspectTemplateName`, `reidentifyTemplateName` and `locationId` {{D:REST projects.content.reidentify}} **[Documented]**
• Neither request has a field for direction, message role or prompt type, so the caller decides what string to send; the column therefore applies to prompts, responses, retrieved text, tool inputs and tool outputs alike **[Inferred]**
• The client request class at the tag matches the REST body: {{L:T|class ReidentifyContentRequest(proto.Message):}} **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "Content methods are synchronous, stateless methods." {{D:concepts-method-types}} **[Documented]**
• "Request data is encrypted in transit and is not stored." {{D:concepts-method-types}} **[Documented]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• Reversal needs the whole token and the key, not a lookup table: "To re-identify the de-identified content, you pass the entire token in the re-identify request." {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• "Reversible: Can be re-identified using the cryptographic key, surrogate annotation, and any context tweak." {{D:pseudonymization}} **[Documented]**
• "A surrogate annotation is required for re-identification of unstructured data." {{D:pseudonymization}} **[Documented]**
• For tables the annotation is optional: "Sensitive Data Protection can perform both de-identification and re-identification on an entire column using a RecordTransformation without a surrogate annotation." {{D:pseudonymization}} **[Documented]**
• Context tweaks apply to structured data only: the step is titled "Step 5 (Format preserving and deterministic encryption with AES-SIV of structured data only)" {{D:pseudonymization}} **[Documented]**
• For plain strings with no record, the client docstring says the context is ignored: "plaintext would be used as is for encryption." ({{L:T|plaintext would be used as is for encryption.}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Nothing in the request carries a system prompt or conversation roles, so no prompt context is needed to tokenise or restore a string **[Inferred]**
### R4
Summary: **Standard keyed encryption, not a model.** AES-SIV gives base64 tokens of any length; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. Detectors that pick the values are separate. **[Documented]**
Detail:
• "Sensitive Data Protection supports three pseudonymization techniques, all of which use cryptographic keys." {{D:pseudonymization}} **[Documented]**
• AES-SIV: the value is "encrypted using the AES-SIV encryption algorithm with a cryptographic key, encoded using base64, and then prepended with a surrogate annotation, if specified" {{D:pseudonymization}} **[Documented]**
• The client docstring for `CryptoDeterministicConfig`: "representation of the encrypted output. Uses AES-SIV based on" the RFC 5297 link on the next line ({{L:T|representation of the encrypted output. Uses AES-SIV based on}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Key handling for AES-SIV: "provided key is internally expanded to 64 bytes" ({{L:T|provided key is internally expanded to 64 bytes}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• FPE: "By design, FPE-FFX preserves the length and character set of the input text." {{D:pseudonymization}} **[Documented]**
• "This means that it lacks authentication and an initialization vector, which would cause a length expansion in the output token." {{D:pseudonymization}} **[Documented]**
• "FPE provides fewer security guarantees compared to other deterministic encryption methods such as deterministic encryption with AES-SIV." {{D:pseudonymization}} **[Documented]**
• "Other methods like deterministic encryption using AES-SIV provide these stronger security guarantees and are recommended for tokenization use cases unless length and character set preservation are strict requirements" {{D:pseudonymization}} **[Documented]**
• "Important: Don't use the CryptoReplaceFfxFpeConfig method, except when preserving the input alphabet space and size is a requirement." {{D:transformations-reference}} **[Documented]**
• "The CryptoReplaceFfxFpeConfig method can run very slowly, and it has limitations on the size of the alphabet and number of tokens" {{D:transformations-reference}} **[Documented]**
• "The CryptoDeterministicConfig method has no limitations on the input and is much faster." {{D:transformations-reference}} **[Documented]**
• The client docstring agrees: "plus warrant referential integrity. FPE incurs significant latency" ({{L:T|plus warrant referential integrity. FPE incurs significant latency}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• FPE security limits recommended by NIST, quoted from the page: "radix^max_size <= 2^128." and "radix^min_len >= 100" {{D:transformations-reference}} **[Documented]**
• FPE alphabet choices: "Use one of four enumerated values that represent the four most common character sets/alphabets." Other choices are a radix from 2 to 95 or an explicit character list {{D:pseudonymization}} **[Documented]**
• Three key types exist: Cloud KMS wrapped, transient and unwrapped; the page calls the wrapped key "the most secure type of cryptographic key available to use with the Sensitive Data Protection de-identification methods" {{D:pseudonymization}} **[Documented]**
• "A Cloud KMS wrapped key consists of a 128-, 192-, or 256-bit cryptographic key that has been encrypted using another key." {{D:pseudonymization}} **[Documented]**
• A transient key "is generated by Sensitive Data Protection at the time of de-identification, and then discarded" so it cannot support later reversal {{D:pseudonymization}} **[Documented]**
• Raw keys: "Because of the risk of accidentally leaking the key, these types of keys are not recommended." {{D:pseudonymization}} **[Documented]**
• The client defines `CryptoKey` with a one-of of transient, unwrapped and kms_wrapped sources ({{L:T|kms_wrapped: "KmsWrappedCryptoKey" = proto.Field(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The client docstring names the permission needed for a KMS-wrapped key: {{L:T|    dlp.kms.encrypt}} lists "dlp.kms.encrypt" **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The IAM page lists `dlp.kms.encrypt` in DLP User (`roles/dlp.user`) {{D:roles and permissions}} **[Documented]**
• Reversal finds tokens with a custom infoType: "Message for detecting output from deidentification transformations that support reversing." {{D:REST InspectConfig}} **[Documented]**
• The quickstart re-identify request pairs a `customInfoTypes` entry holding `surrogateType` with the same `cryptoDeterministicConfig` and `surrogateInfoType` used to tokenise {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• Pick a surrogate name that cannot occur in data: "info type must not occur naturally anywhere in your data;" ({{L:T|info type must not occur naturally anywhere in your data;}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Failure modes named by the same docstring: inspection may "reverse a surrogate that does not correspond to an actual" identifier, or be unable to parse the surrogate and return an error ({{L:T|- reverse a surrogate that does not correspond to an actual}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cloud KMS key placement: "When you create a Cloud KMS key, you must store it in either global or in the same region that you will use for your Sensitive Data Protection requests. Otherwise, the Sensitive Data Protection requests will fail." {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• Access is by the DLP API over REST (global endpoint `dlp.googleapis.com`, regional endpoint `dlp.REGION.rep.googleapis.com`), through `projects.content.reidentify` or `projects.locations.content.reidentify` {{D:REST projects.locations.content.reidentify}} **[Documented]**
• In the REST bodies the `locationId` field is described as "Deprecated. This field has no effect." and the location is carried by `parent` {{D:REST projects.content.reidentify}} **[Documented]**
• "There is no guarantee that the data in transit remains in the processing region that you specified." applies to the global endpoint with a location; regional endpoints "guarantee data residency" for data at rest, in use and in transit {{D:api-endpoints}} **[Documented]**
• Python client: package `google-cloud-dlp` version 3.40.0 ({{L:G|__version__ = "3.40.0"}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Tokenisation itself uses a cryptographic algorithm and no machine-learning model; what is tokenised depends on infoType detectors, whose backing models are covered in SD1 **[Inferred]**
• Conflict on AES-SIV output length, statement 1: the transformation table row says CryptoDeterministicConfig "Replaces an input value with a token, or surrogate value, of the same length using AES in Synthetic Initialization Vector mode (AES-SIV)." {{D:transformations-reference}} **[Documented]**
• Conflict on AES-SIV output length, statement 2: the same page's deterministic-encryption section says the token "Does not preserve the character set ("alphabet") or length of the input value post-encryption." {{D:transformations-reference}} **[Documented]**
• Conflict on AES-SIV output length, statement 3: "This method produces a hashed value, so it does not preserve the character set or the length of the input value." {{D:pseudonymization}} **[Documented]**
• The client docstring supports statements 2 and 3 on format (base64 output) but says nothing on length: {{L:T|encryption for the given input. Outputs a base64 encoded}}; behaviour needs a test **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R5
Summary: **Transformed text plus a summary, no verdict.** The response returns the item with tokens or restored values and an overview listing each transformation with success or error counts. A token is a surrogate name, a length and the encrypted value. **[Documented]**
Detail:
• `content.deidentify` returns `item` (the de-identified item) and `overview` ({{L:T|class DeidentifyContentResponse(proto.Message):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• `content.reidentify` returns `item` (the re-identified item) and `overview` ({{L:T|class ReidentifyContentResponse(proto.Message):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Token form: "SURROGATE_INFOTYPE(SURROGATE_VALUE_LENGTH):SURROGATE_VALUE" {{D:pseudonymization}} **[Documented]**
• Documented example token for an email address: "EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q." {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• Without an annotation: "If you do not specify a surrogate annotation, the resulting token is equal to the transformed value" {{D:pseudonymization}} **[Documented]**
• The quickstart response overview holds `transformedBytes` and `transformationSummaries[]`, each with `infoType`, `transformation`, `results[]` (`count`, `code`) and `transformedBytes` {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• In that example the summary echoes the transformation configuration, including `kmsWrapped.wrappedKey` (the wrapped, encrypted key) and `cryptoKeyName` {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• The re-identify response in the quickstart returns the restored sentence in `item.value` and an `overview` of the same shape {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• Each summary result carries a code and a free-text field: `details` is "A place for warnings or errors to show up if" a transformation did not work as expected ({{L:T|A place for warnings or errors to show up if}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Result codes are `SUCCESS` and `ERROR` ({{L:T|Transformation completed without an error.}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Documented FPE error text for values outside the alphabet: "CryptoReplaceFfxFpeConfig's 'alphabet' does not include all the characters in the value being transformed" {{D:release-notes}} (change of 2018-12-12) **[Documented]**
• Too many findings: "Too many findings to de-identify. Retry with a smaller request." {{D:deidentify-sensitive-data}} **[Documented]**
• The call returns no score, likelihood or allow or block verdict for the transformation; the caller decides what to do with the output, which follows from the two response fields above **[Inferred]**
• Which values are transformed is filtered by minimum likelihood: "If you don't set a minimum likelihood in your request, or if you set it to LIKELIHOOD_UNSPECIFIED, Sensitive Data Protection returns only the findings with a likelihood of POSSIBLE and higher." {{D:likelihood}} **[Documented]**
• The likelihood page describes the trade-off at each level (for example VERY_LIKELY gives "the highest precision at the expense of recall") but names no recommended value for tokenisation {{D:likelihood}} **[Not disclosed]**
• No published measure of round-trip correctness, token collision rate or throughput (checked the pseudonymization, transformation-reference, quickstart, pricing, limits, SLA and release-note pages) **[Not disclosed]**
### R6
Summary: **Needs a key, a surrogate name and a supported input.** Requests need a Cloud KMS wrapped key in a matching region, a surrogate annotation for free text, and values within AES-SIV or FPE limits. API keys cannot be used with wrapped keys. **[Documented]**
Detail:
• Parent resource: `projects/{projectId}` or `projects/{projectId}/locations/{locationId}`; "Authorization requires the following IAM permission on the specified resource parent: serviceusage.services.use" {{D:REST projects.content.reidentify}} **[Documented]**
• DLP User (`roles/dlp.user`) is described as "Inspect, Redact, and De-identify Content" and holds `dlp.kms.encrypt` and `serviceusage.services.use` {{D:roles and permissions}} **[Documented]**
• The quickstart asks for Cloud KMS Admin, Cloud KMS CryptoKey Encrypter and DLP User on the project to wrap a key, de-identify and re-identify {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• Setup commands: verify billing is enabled and run `gcloud services enable dlp.googleapis.com cloudkms.googleapis.com` {{D:quickstart De-identify and re-identify sensitive data}} **[Documented]**
• "Note: When a Cloud Key Management Service wrapped key is used on deidentify or reidentify requests, API keys can't be used for authentication." {{D:auth}} **[Documented]**
• Key material: a 128-, 192- or 256-bit AES key, wrapped by a Cloud KMS key, passed as `kmsWrapped` with `cryptoKeyName` and `wrappedKey`; the wrapped key is base64 by default and clients must decode it to bytes {{D:transformations-reference}} **[Documented]**
• Key location: the Cloud KMS key must be in global or in the same region as the Sensitive Data Protection request {{D:create-wrapped-key}} **[Documented]**
• "When you use Cloud KMS for cryptographic operations, charges apply." {{D:pseudonymization}} **[Documented]**
• Free-text reversal needs the surrogate name: "To re-identify unstructured data, this entire token is required, including the surrogate annotation." {{D:pseudonymization}} **[Documented]**
• Context must match: "If a context tweak is used to create the token, then this context tweak is also required for the de-identification transformations to be reversed." {{D:pseudonymization}} **[Documented]**
• AES-SIV input rule: the summary table gives "At least 1 char long; no character set limitations." {{D:pseudonymization}} **[Documented]**
• FPE input rule: "At least 2 chars long; must be encoded as ASCII." and the alphabet "must be made up of at least 2 characters and contain no more than 95" {{D:pseudonymization}} and {{D:transformations-reference}} **[Documented]**
• "For input that varies in length or has length greater than 32 bytes, use CryptoDeterministicConfig." {{D:transformations-reference}} **[Documented]**
• Content request limits: 0.5 MB per request, 3,000 findings, 100 transformations and 50,000 table values per request {{D:limits}} **[Documented]**
• The limits table is headed as covering "inspecting and de-identifying content sent directly to the DLP API" and does not name re-identification; the same limits probably also apply to `content.reidentify` **[Inferred]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint {{D:limits}} **[Documented]**
• "Note: Quotas and limits specified in this document are subject to change." {{D:limits}} **[Documented]**
• Billing: the pricing page marks `projects.content.reidentify` and `projects.content.deidentify` as billed for both content inspection and content transformation {{O:Sensitive Data Protection pricing page}} **[Documented]**
• The first 1 gibibyte per month per account of content inspected and of content transformed is $0.00 (Free); a minimum of 1 KB is billed per content inspect or transform request {{O:Sensitive Data Protection pricing page}} **[Documented]**
• SLA: "Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests {{O:Sensitive Data Protection SLA page}} **[Documented]**
• Because the SLA names only inspect and deidentify requests, `content.reidentify` has no published uptime objective **[Inferred]**
• Client install: `pip install google-cloud-dlp` ({{L:R|pip install google-cloud-dlp}}) and Python 3.10 or later ({{L:S|python_requires=">=3.10",}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
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
• Effect of rotating or destroying a Cloud KMS key version on tokens already issued; the quickstart cleanup warns that destroying a key version stops decryption, and no rotation guidance was found (checked the quickstart, create-wrapped-key and pseudonymization pages)
• Which identity needs which Cloud KMS permission at request time: the quickstart grants the caller KMS Admin, CryptoKey Encrypter and DLP User, and the client names `dlp.kms.encrypt`, but the page does not say whether the DLP service agent or the caller unwraps the key (checked the quickstart, create-wrapped-key, roles and auth pages)
• Whether request bodies, tokens or wrapped keys appear in Cloud Audit Logs (the audit-logging page was not read)
• Whether tokenised output and the key reach any Google training or product-improvement use: the customer data terms were not read
• SLO, latency and quota values for `content.reidentify` in particular (the SLA covers only inspect and deidentify; the limits page lists no per-method quota)
• Whether a Singapore-region KMS key can be used with the `asia-southeast1` regional endpoint: both are named only generally in the docs read
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
## Column SD5: Sensitive Data Protection: Sensitive-data detection and redaction in images
### R1
Summary: **Finds and blanks sensitive text and objects in images.** The service reads text in an image with OCR and also detects objects such as passports, photo ID cards, faces and licence plates. It returns bounding boxes, or the image with opaque rectangles over the matches. **[Documented]**
Detail:
• "Using infoType detectors, Sensitive Data Protection inspects a base64-encoded image and detects sensitive data within the image." {{D:concepts-image-redaction}} **[Documented]**
• "Inspection and redaction are two distinct operations:" and the page defines both, so one image can be inspected without being changed {{D:concepts-image-redaction}} **[Documented]**
• Inspection "returns the detected InfoTypes, along with one or more set of pixel coordinates and dimensions." {{D:concepts-image-redaction}} **[Documented]**
• Redaction "returns the redacted base64-encoded image in the same image format as the original image." {{D:concepts-image-redaction}} **[Documented]**
• "In the returned image, the detected sensitive data elements are obscured by an opaque rectangle." {{D:redacting-sensitive-data-images}} **[Documented]**
• "By default, Sensitive Data Protection uses black rectangles to obscure the redacted content, but you can specify a color for each infoType in your image redaction configuration." {{D:redacting-sensitive-data-images}} **[Documented]**
• "Sensitive Data Protection uses optical character recognition (OCR) to detect text within images." {{D:concepts-image-redaction}} **[Documented]**
• "Sensitive Data Protection can classify and redact objects in images." {{D:concepts-image-redaction}} **[Documented]**
• An option redacts every piece of text found: "Sensitive Data Protection also contains an option to redact all detected text in an image." {{D:redacting-sensitive-data-images}} **[Documented]**
• The release notes of 2025-07-04 add object redaction: "Sensitive Data Protection can detect and redact the following object infoTypes in images:" barcode, licence plate, person and whiteboard {{D:release-notes}} **[Documented]**
• Later object detectors: passport and photo ID card (2025-11-03), face in Preview (2025-12-15) and signature (2026-06-08) {{D:release-notes}} **[Documented]**
• The Python client at v3.40.0 exposes `redact_image` and `inspect_content` ({{L:C|def redact_image(}} and {{L:C|def inspect_content(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Image safety classification uses the same two methods and is covered by the SD6 column **[Inferred]**
### R2
Summary: **Sensitive text and ID-type objects in pictures.** Text infoTypes run on text read from the image, and object detectors cover faces, passports, photo ID cards, signatures, licence plates, barcodes and whiteboards. **[Documented]**
Detail:
• "To detect text in images, specify any text-based infoType, such as PERSON_NAME and CREDIT_CARD_NUMBER in your inspection or redaction configuration." {{D:concepts-image-redaction}} **[Documented]**
• "all other infoType detectors are text-based; when analyzing images, they first extract text from images and then analyze the text." {{D:infotypes-reference}} **[Documented]**
• The reference lists eight object infoTypes that "analyze image pixels and features directly" and describes them {{D:infotypes-reference}} **[Documented]**
  – `OBJECT_TYPE/PERSON/PASSPORT`: "Image of a person's passport card or passport booklet, which is often used for identification and travel purposes. Note that images of the inner visa-stamped pages might not be identified."
  – `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`: "Image of a person's photo ID card, which can be government-issued (for example, driver's license) or non-government-issued (for example, school ID or employee ID)."
  – `OBJECT_TYPE/PERSON/SIGNATURE`: "Image of a signature which is done by a human on some document for their identity verification."
  – `OBJECT_TYPE/PERSON/FACE`: "Image of a person's face." and `OBJECT_TYPE/PERSON`: "Image of a human-like figure, which can include a full body, a face, or other body parts."
  – `OBJECT_TYPE/LICENSE_PLATE`: "Image of a license plate, which is a government-issued vehicle identifier."
  – `OBJECT_TYPE/BARCODE`: "Image of a 1D or 2D barcode, which is a machine-readable image that represents a piece of data." and `OBJECT_TYPE/WHITEBOARD`: "Image of a whiteboard."
• The face detector is not generally available: "This infoType detector is in Preview." {{D:infotypes-reference}} **[Documented]**
• "Default infoTypes don't include objects in images." so object detectors must be requested by name {{D:redacting-sensitive-data-images}} **[Documented]**
• Documented use case: "Sanitize customer support uploads: Automatically redact account numbers and personal contact details in user-submitted screenshots before tickets are routed to support agents." {{D:concepts-image-redaction}} **[Documented]**
• Documented use case: "Obfuscate sensitive data in scanned documents: Mask driver's licenses, national identity cards, and credit card numbers from uploaded PDF or image attachments before processing in downstream workflows." {{D:concepts-image-redaction}} **[Documented]**
• The redaction walkthrough uses an image with a handwritten Social Security number and notes "Sensitive Data Protection also redacted the year." (a match the author did not ask for) {{D:redacting-sensitive-data-images}} **[Documented]**
• Default sensitivity scores of the object infoTypes {{D:infotypes-reference}} **[Documented]**
  – SENSITIVITY_HIGH: `OBJECT_TYPE/PERSON/FACE`, `OBJECT_TYPE/PERSON/PASSPORT`, `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`, `OBJECT_TYPE/PERSON/SIGNATURE`
  – SENSITIVITY_MODERATE: `OBJECT_TYPE/PERSON`, `OBJECT_TYPE/LICENSE_PLATE`
  – SENSITIVITY_LOW: `OBJECT_TYPE/BARCODE`, `OBJECT_TYPE/WHITEBOARD`
• Singapore: the text infoTypes `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` and `SINGAPORE_PASSPORT` are available in all locations {{D:infotypes-reference}} **[Documented]**
• A Singapore NRIC printed in an image is therefore reachable by OCR followed by the text detector; this needs a test because no Singapore image example is given **[Inferred]**
• The object detectors for passports and photo ID cards are global; the docs do not say whether they recognise Singapore passports or NRIC cards (checked the infoType reference, release notes and image pages) **[Not disclosed]**
• OCR language and script coverage, handwriting accuracy and rotated or low-resolution text: not stated (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages) **[Not disclosed]**
• "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• Prompt injection or jailbreak text inside an image is not described as something the service looks for (checked the same image pages); OCR text is matched only against the infoTypes requested **[Not disclosed]**
### R3
Summary: **Image bytes only, with no input or output flag.** One image goes in per call, whether from a prompt, a response, a retrieved file or a tool result. Results are not stored in Google Cloud, and only the first frame of a multiframe image is used. **[Inferred]**
Detail:
• "To inspect an image for sensitive data, you submit a base64-encoded image to the content.inspect method." {{D:inspecting-images}} **[Documented]**
• "To redact sensitive data from an image, submit the image to the DLP API's image.redact method." {{D:redacting-sensitive-data-images}} **[Documented]**
• The client type is described as "Container for bytes to inspect or redact." and `ContentItem` carries it as `byte_item` beside `value` and `table` ({{L:T|Container for bytes to inspect or redact.}} and {{L:T|byte_item (google.cloud.dlp_v2.types.ByteContentItem):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The `projects.image.redact` request body has `locationId`, `inspectConfig`, `imageRedactionConfigs[]`, `includeFindings`, `byteItem`, `inspectTemplate` and `deidentifyTemplate` {{D:REST projects.image.redact}} **[Documented]**
• None of these fields marks direction, role or prompt type, so the same call is used for images from prompts, responses, retrieved files and tool inputs or outputs, with the caller supplying the bytes **[Inferred]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." {{D:REST projects.image.redact}} **[Documented]**
• For inspection the client enum says "Only the first frame of each multiframe image is inspected. Metadata" ({{L:T|Only the first frame of each multiframe image is inspected. Metadata}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• "Content methods are synchronous, stateless methods." and "Request data is encrypted in transit and is not stored." {{D:concepts-method-types}} **[Documented]**
• Documents with embedded images are a different route: the inspect guide says other formats such as PDF, DOCX, XLSX and PPTX "may generate mixed findings" and the redact guide says "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." {{D:inspecting-images}} and {{D:redacting-sensitive-data-images}} **[Documented]**
• Image scanning runs only in listed locations (see R6); in other regions images and documents with images are scanned as binary files {{D:locations}} **[Documented]**
• No system prompt or conversation context is read; the service sees the image and the configuration only **[Inferred]**
### R4
Summary: **OCR for text, direct pixel analysis for objects.** Text infoTypes run on text extracted from the image; object detectors look at pixels and return a box. Both go through the DLP API over REST or client libraries, on a global or regional endpoint. **[Documented]**
Detail:
• "In regions that support image scanning, Sensitive Data Protection uses OCR to find text-based infoTypes in images." {{D:supported-file-types}} **[Documented]**
• Object scanning: "This scanning mode focuses on locating a specific item within the image and produces a bounding box around it." {{D:supported-file-types}} **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any object infoTypes that are specified in the inspection or redaction configuration." {{D:supported-file-types}} **[Documented]**
• Names, versions, architecture and training data of the OCR and object-detection models (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages and the release notes) **[Not disclosed]**
• "Image redaction is similar to image inspection, with one additional step." {{D:concepts-image-redaction}} **[Documented]**
• Redaction targets are set per entry in `imageRedactionConfigs[]`: an `infoType`, or `redactAllText`, plus an optional `redactionColor` ({{L:T|redact_all_text: bool = proto.Field(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• With no infoType listed and redact-all-text false, the docstring says the API "will redact all text that it matches against all info_types" found ({{L:T|will redact all text that it matches against all info_types}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "Note: If you include infoTypes in the imageRedactionConfigs object, Sensitive Data Protection ignores them." when `redactAllText` is set {{D:redacting-sensitive-data-images}} **[Documented]**
• Colours are RGB values from 0 to 1: "Each value is between 0 and 1, inclusive." {{D:redacting-sensitive-data-images}} **[Documented]**
• Templates can drive redaction: `deidentifyTemplate` "The request fails if the type of the template's deidentifyConfig is not imageTransformations." {{D:REST projects.image.redact}} **[Documented]**
• An image transformation holds a colour and one of selected infoTypes, all infoTypes or all text: `selectedInfoTypes`, `allInfoTypes`, `allText` {{D:REST organizations.deidentifyTemplates}} **[Documented]**
• Image-based rules refine results by position: "Image-based exclusion rules, which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings." (general availability 2026-02-23) {{D:release-notes}} **[Documented]**
• Such a rule "is silently ignored if the content being inspected is not an image" (docstring) ({{L:T|This rule is silently ignored if the content being inspected is}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and the location form `{parent=projects/*/locations/*}/image:redact`; regional endpoint form `dlp.REGION.rep.googleapis.com` {{D:REST projects.locations.image.redact}} and {{D:api-endpoints}} **[Documented]**
• Regional endpoint support for `asia-southeast1` (Singapore) is listed as Yes {{D:locations}} **[Documented]**
• API keys are accepted: "The image.redact method also supports API keys." {{D:redacting-sensitive-data-images}} **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 ({{L:G|__version__ = "3.40.0"}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Model Armor docs, not SDP docs: Model Armor image screening (see the Model Armor column `Model Armor: Image screening with OCR and visual scanning`) says "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." {{O:Model Armor overview page}} **[Documented]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column {{O:Gemini Enterprise protect-sensitive-data page}} **[Documented]**
### R5
Summary: **Bounding boxes or a redacted image, with a likelihood.** Inspection returns each detected infoType with a likelihood bucket and pixel boxes. Redaction returns the image with rectangles drawn and, if asked, the findings. There is no allow or block verdict. **[Documented]**
Detail:
• "The output of an inspection operation includes the detected infoTypes, the likelihood of the match, and pixel coordinates and length values that indicate the areas within which Sensitive Data Protection found the sensitive data." {{D:inspecting-images}} **[Documented]**
• A finding in the guide's sample holds `infoType` (with `sensitivityScore`), `likelihood`, `location.contentLocations[].imageLocation.boundingBoxes[]` (`top`, `left`, `width`, `height`), `createTime` and `findingId` {{D:inspecting-images}} **[Documented]**
• "Be aware that Sensitive Data Protection often uses multiple boxes to indicate where a single instance of sensitive data is in the image." {{D:inspecting-images}} **[Documented]**
• For object infoTypes "the inspection result doesn't include a quote for the detected object." {{D:inspecting-images}} **[Documented]**
• Bounding-box origin, statement 1 (REST reference and client): "Top coordinate of the bounding box. (0,0) is upper left." {{D:REST InspectResult}} **[Documented]**
• Bounding-box origin, statement 2: "The coordinates at the bottom left corner of an image are (0,0)." {{D:inspecting-images}} **[Documented]**
• Bounding-box origin, statement 3: boxes are described by "the bottom-left corner and the dimensions of bounding boxes, respectively." {{D:concepts-image-redaction}} **[Documented]**
• The client agrees with statement 1: {{L:T|Top coordinate of the bounding box. (0,0) is}} **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No match, inspection: "it returns an empty, successful HTTP 200 response." {{D:concepts-image-redaction}} **[Documented]**
• No match, redaction: "it returns the base64-encoded image unchanged." {{D:concepts-image-redaction}} **[Documented]**
• Redaction response `redactedImage`: "The redacted image. The type will be the same as the original image." {{D:REST RedactImageResponse}} **[Documented]**
• Redaction response `extractedText`: "If an image was being inspected and the InspectConfig's includeQuote was set to true, then this field will include all text, if any, that was found in the image." {{D:REST RedactImageResponse}} **[Documented]**
• Redaction response `inspectResult`: "The findings. Populated when includeFindings in the request is true." {{D:REST RedactImageResponse}} **[Documented]**
• Setting `includeQuote` returns all recognised text to the caller, so the response itself holds the sensitive text that redaction was meant to hide **[Inferred]**
• Threshold: findings below `minLikelihood` are dropped and "returns only the findings with a likelihood of POSSIBLE and higher" when it is unset; five levels from VERY_UNLIKELY to VERY_LIKELY, no numeric score {{D:likelihood}} **[Documented]**
• The likelihood page describes each level (for example "Useful if you want a balance of precision and recall." for POSSIBLE) but gives no recommended level for images {{D:likelihood}} **[Not disclosed]**
• The redaction guide shows a request with `minLikelihood` set to LIKELY inside `inspectConfig` ("Code example with likelihood setting") {{D:redacting-sensitive-data-images}} **[Documented]**
• Redaction responses carry no allow or block field, only the image, optional text and optional findings ({{L:T|class RedactImageResponse(proto.Message):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Published precision, recall, false-positive rate, OCR error rate or per-object detection accuracy (checked the image concepts, inspect, redact, likelihood and infoType reference pages and the release notes; the likelihood page only defines the terms) **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location, up to 4 MB; formats disagree.** The docs name PNG, JPEG and BMP most often, while SVG, GIF and TIFF appear on only some pages. Redaction requests are capped at 4 MB and other content requests at 0.5 MB. **[Documented]**
Detail:
• Format conflict, statement 1 (REST reference for `byteItem`): "The content must be PNG, JPEG, SVG or BMP." {{D:REST projects.image.redact}} **[Documented]**
• Format conflict, statement 2 (redaction guide): "Sensitive Data Protection can redact sensitive data from many image types, including JPEG, BMP, and PNG." and "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." {{D:redacting-sensitive-data-images}} **[Documented]**
• Format conflict, statement 3 (supported file types, inspection and de-identification table, image row): extensions "bmp, gif, jpe, jpeg, jpg, png", scanning modes OCR, image content detection and image content classification, transformation support Redaction {{D:supported-file-types}} **[Documented]**
• Format conflict, statement 4 (inspect guide): "Sensitive Data Protection can inspect many image types for sensitive data, including JPEG, BMP, PNG, and SVG." {{D:inspecting-images}} **[Documented]**
• Format conflict, statement 5 (method-types page): "Redact sensitive data from uploaded images: Obfuscate sensitive text in image formats (such as JPEG, PNG, or TIFF)" {{D:concepts-method-types}} **[Documented]**
• Format conflict, statement 6 (client enum, surface only): `IMAGE` ("Any image type."), `IMAGE_JPEG`, `IMAGE_BMP`, `IMAGE_PNG` and `IMAGE_SVG`, and no GIF value ({{L:T|IMAGE_SVG = 4}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The supported-file-types page also has a discovery table whose Images cluster lists "bmp, gif, heic, ico, jpe, jpeg, jpg, pm, png, svg, tiff, webp" and says "Supported images (bmp, gif, jpe, jpeg, jpg, and png) smaller than 4 MiB are scanned using OCR"; this table is for discovery, not content methods {{D:supported-file-types}} **[Documented]**
• PNG, JPEG and BMP are the formats named by the REST reference, the redaction guide, the inspect guide and the client enum; SVG, GIF and TIFF are disputed, so tests should use PNG, JPEG and BMP first **[Inferred]**
• Size: "Maximum size of each projects.image.redact request | 4 MB" and "Maximum size of each request, except projects.image.redact | 0.5 MB" {{D:limits}} **[Documented]**
• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`, so larger images need `image.redact` or a storage inspection job **[Inferred]**
• "If you need to inspect files that are larger than these limits, store those files on Cloud Storage and run an inspection job." {{D:limits}} **[Documented]**
• Locations: "Image inspection and redaction are supported only in the following locations:" global, asia, asia-southeast1, europe, europe-north1, us, us-central1, us-east4, us-west1 {{D:locations}} **[Documented]**
• "If you attempt to inspect images or documents that contain images in a region that doesn't support image scanning, Sensitive Data Protection scans those files as binary files." {{D:locations}} **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22 {{D:release-notes}} **[Documented]**
• "When you redact data from images, you can't include limits in your inspection configuration." and "If you set the limits field in your request, Sensitive Data Protection generates an error." {{D:redacting-sensitive-data-images}} **[Documented]**
• Default detectors, statement 1: "Unless you specify specific information types (infoTypes) to search for, Sensitive Data Protection searches for the most common infoTypes." {{D:redacting-sensitive-data-images}} **[Documented]**
• Default detectors, statement 2: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated." {{D:REST projects.image.redact}} **[Documented]**
• Advice from the infoType concepts page: "Always specify infoType detectors explicitly. Don't use an empty infoTypes list." {{D:concepts-infotypes}} **[Documented]**
• Encoding and parameters: REST callers base64-encode the image; client libraries take bytes; optional `includeFindings`, `inspectConfig`, `imageRedactionConfigs`, `inspectTemplate` and `deidentifyTemplate` {{D:redacting-sensitive-data-images}} **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User (`roles/dlp.user`); an API key also works for `image.redact` {{D:redacting-sensitive-data-images}} **[Documented]**
• "You can use a Google Cloud console API key to authenticate to the DLP API for some methods, including all projects.content.* and projects.image.* methods." {{D:auth}} **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint; values "are subject to change" {{D:limits}} **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection and not for content transformation; the first 1 gibibyte per month is free, minimum 1 KB per request {{O:Sensitive Data Protection pricing page}} **[Documented]**
• The SLA covers only content.inspect and content.deidentify requests, so `image.redact` has no published uptime objective {{O:Sensitive Data Protection SLA page}} **[Inferred]**
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
• Launch stage of image redaction by object infoType: only the face detector is marked Preview (checked the infoType reference and release notes)
• Whether the redacted image strips metadata such as EXIF; the REST text says metadata is omitted for multiframe images only (needs testing)
• How a content policy or Model Armor image screening differs in practice from calling `image.redact` directly (cross-reference only; content policies are inventory-only)
• Customer data terms for images sent to the API (not read)
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
## Column SD6: Sensitive Data Protection: Image safety classification (sexual and violent content)
### R1
Summary: **Whole-image safety labels for sexual and violent content.** Three image context detectors judge the overall subject of an image rather than objects inside it. Inspection reports a finding for the image, and redaction based on them blanks the entire image. **[Documented]**
Detail:
• "Sensitive Data Protection can classify and redact images based on their thematic content. This feature helps you identify images that contain sensitive or harmful subject matter according to predefined safety categories." {{D:concepts-image-redaction}} **[Documented]**
• "Sensitive Data Protection analyzes an image's overall context and meaning to determine if it belongs to categories such as sexually explicit or violent content." {{D:concepts-image-redaction}} **[Documented]**
• "You can use this feature to support content moderation and enforce acceptable use policies." {{D:concepts-image-redaction}} **[Documented]**
• The reference lists three image context infoTypes: `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`, `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE` and `IMAGE_TYPE/CONTEXT/VIOLENCE`, introduced as detectors that "analyze an entire image for sensitive or harmful subject matter" {{D:infotypes-reference}} **[Documented]**
• "Unlike object detection, which identifies specific items within an image, this feature assesses the image's subject matter as a whole." {{D:concepts-image-redaction}} **[Documented]**
• "If you configure redaction based on image safety, this feature redacts the entire image." {{D:concepts-image-redaction}} **[Documented]**
• Release notes of 2026-01-16: "The following infoType detectors are available in global and the asia, europe, and us multi-regions:" the three image context detectors {{D:release-notes}} **[Documented]**
• Release notes of 2026-06-23: "Image safety classification infoTypes are now supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." {{D:release-notes}} **[Documented]**
• The calls are the image inspection and redaction methods of the SD5 column (`inspect_content` and `redact_image` in the Python client) ({{L:C|def redact_image(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R2
Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a one-sentence definition, and the docs describe the use as content moderation. Other harm categories are not listed. **[Documented]**
Detail:
• `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`: "A finding of this type indicates that an image contains adult content of a sexual nature." {{D:infotypes-reference}} **[Documented]**
• Same entry: "Adult content might include elements such as nudity, specific contours or shapes of reproductive body parts, sexual activities, or pornographic images including photo-realistic or cartoon in nature." {{D:infotypes-reference}} **[Documented]**
• `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE`: "A finding of this type indicates that an image contains racy or sexually suggestive content. Racy content might include elements like revealing clothing, lewd or provocative poses or themes, or other sexually suggestive material." {{D:infotypes-reference}} **[Documented]**
• `IMAGE_TYPE/CONTEXT/VIOLENCE`: "A finding of this type indicates that an image contains violent or gory content either real or fictionalized." {{D:infotypes-reference}} **[Documented]**
• Same entry: "Violent content might include imagery related to death, serious injury, or harm to an individual or group of individuals or animals." {{D:infotypes-reference}} **[Documented]**
• All three carry the default sensitivity score SENSITIVITY_HIGH and the category CONTEXTUAL_INFORMATION in the reference tables {{D:infotypes-reference}} **[Documented]**
• The reference lists only these three image context detectors; categories such as hate symbols, self-harm, weapons or child safety are not named (checked the infoType reference, image concepts page and release notes) **[Not disclosed]**
• Generated images are a stated weak point: "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." {{D:concepts-image-redaction}} **[Documented]**
• "their effectiveness in detecting all types of policy-violating content in AI-generated images can vary" {{D:concepts-image-redaction}} **[Documented]**
• On AI-generated images the page says these might not be detected: nuanced or subtle content; context-dependent scenarios such as private settings; non-graphic depictions of sensitive themes {{D:concepts-image-redaction}} **[Documented]**
• "Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications." {{D:concepts-image-redaction}} **[Documented]**
• "We recommend that you conduct thorough testing for your specific generative AI use cases to ensure that the results meet your safety requirements." {{D:concepts-image-redaction}} **[Documented]**
• The text-side analogues are document-category infoTypes of the SD1 column, for example `DOCUMENT_TYPE/CONTEXT/SEXUAL` ("Content contains sex-related topics."), `DOCUMENT_TYPE/CONTEXT/OFFENSIVE` ("Content contains offensive topics.") and `DOCUMENT_TYPE/CONTEXT/OBSCENE` ("Content contains obscene topics."); they classify text, not pixels {{D:infotypes-reference}} **[Documented]**
• The reference introduces document classification as "To help with document risk assessment and policy enforcement, Sensitive Data Protection can classify documents into enterprise, sensitive, and regulated content categories." {{D:infotypes-reference}} **[Documented]**
• Prompt injection, jailbreaks, toxicity in text and topic control are not part of this feature (checked the image concepts, inspect, redact and infoType reference pages; none mentions them) **[Not disclosed]**
• Languages: the classifier works on pixels, not on extracted text: "can analyze image pixels and features directly, rather than text extracted from images." {{D:supported-file-types}} **[Documented]**
### R3
Summary: **Whole images as bytes, with no input or output flag.** The same call can score a user upload or an image a model generated. The whole image is judged, multiframe images use the first frame only, and results are not stored in Google Cloud. **[Inferred]**
Detail:
• "When performing image safety classification, Sensitive Data Protection analyzes the entire image." {{D:concepts-image-redaction}} **[Documented]**
• The input is image bytes in the same `ByteContentItem` used by the SD5 column: "Container for bytes to inspect or redact." ({{L:T|Container for bytes to inspect or redact.}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The image methods have no direction, role or prompt-type field ({{D:REST projects.image.redact}}), so uploads, model-generated images, retrieved images and tool outputs go through the same call **[Inferred]**
• The docs name AI-generated images as an expected input, which is the response-side case: "If you use image context infoTypes on AI-generated images, the following might not be detected:" {{D:concepts-image-redaction}} **[Documented]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." {{D:REST projects.image.redact}} **[Documented]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• The classification mode "can analyze image pixels and features directly, rather than text extracted from images." {{D:supported-file-types}} **[Documented]**
• No system prompt or conversation context is read; the image and the configuration are the only inputs **[Inferred]**
### R4
Summary: **A classifier over the whole image, with unnamed models.** Image context detectors run an image content classification mode that assigns one theme or category. The models are described only as trained mainly on real-world images. Rules can use the findings from June 2026. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." {{D:supported-file-types}} **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any image context infoType detectors that are specified in the inspection or redaction configuration." {{D:supported-file-types}} **[Documented]**
• "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." {{D:concepts-image-redaction}} **[Documented]**
• Model names, architecture, training data and evaluation sets for the image safety classifiers (checked the image concepts, supported-file-types, infoType reference and release-note pages) **[Not disclosed]**
• Image safety findings can act as context in rules: the 2026-06-23 release note says they are "supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." {{D:release-notes}} **[Documented]**
• "Sensitive Data Protection excludes a target infoType finding if the bounding box of a context infoType has the specified relationship with the target infoType finding." and "you must set the matchingType field to MATCHING_TYPE_RULE_SPECIFIC." {{D:creating-custom-infotypes-rules}} **[Documented]**
• The rules page shows no example that uses an image context infoType (checked the page for IMAGE_TYPE) **[Not disclosed]**
• Such a rule "is silently ignored if the content being inspected is not an image" ({{L:T|This rule is silently ignored if the content being inspected is}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access is the DLP API over REST (`POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and `content:inspect`), global or regional endpoint, or the client libraries {{D:REST projects.image.redact}} and {{D:api-endpoints}} **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 ({{L:G|__version__ = "3.40.0"}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column {{O:Gemini Enterprise protect-sensitive-data page}} **[Documented]**
### R5
Summary: **A rated finding for the image, or a fully blanked image.** The docs say classification produces a label, and give a likelihood bucket per finding rather than a number. They show no worked example of an image safety response. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." {{D:supported-file-types}} **[Documented]**
• The scanning-modes table lists ImageLocation as the additional location detail for image content classification, as it does for OCR and object detection; what box a whole-image finding carries is not shown {{D:supported-file-types}} **[Documented]**
• A finding carries `infoType`, `likelihood`, `location` and, when requested, `quote` {{D:REST InspectResult}} **[Documented]**
• Each category is its own infoType, so one image can in principle produce one finding per category **[Inferred]**
• Redaction by image safety replaces the whole image: "this feature redacts the entire image." and the response holds `redactedImage` of the same type as the original {{D:concepts-image-redaction}} and {{D:REST RedactImageResponse}} **[Documented]**
• With `includeFindings` set, the redact response also holds `inspectResult`: "The findings. Populated when includeFindings in the request is true." {{D:REST RedactImageResponse}} **[Documented]**
• No allow or block field exists in the redact response ({{L:T|class RedactImageResponse(proto.Message):}}), so the caller maps findings to a decision **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Threshold: findings below `minLikelihood` are dropped, with POSSIBLE as the default; five levels, no numeric score {{D:likelihood}} **[Documented]**
• A recommended minimum likelihood for image safety, or a calibrated threshold per category (checked the likelihood, image concepts and infoType reference pages) **[Not disclosed]**
• Worked request or response samples for `IMAGE_TYPE/CONTEXT/*` (checked the inspect guide, redact guide, image concepts page, supported-file-types page and REST references; the infoType names appear only in the reference and release notes) **[Not disclosed]**
• Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location; categories must be named.** Image context detectors have to be requested in the configuration, and image scanning runs only in listed locations, including Singapore. Format and size rules are those of other image calls, whose format statements conflict. **[Inferred]**
Detail:
• "To perform image safety classification, specify image context infoTypes in your inspection or redaction configuration." {{D:concepts-image-redaction}} **[Documented]**
• Whether a request with no infoTypes also runs image context detectors: the redaction guide says only that "Default infoTypes don't include objects in images." and is silent on image context infoTypes (checked the redact, inspect and REST pages) **[Not disclosed]**
• Availability: "Availability indicates the regions or multi-regions where the infoType is supported." {{D:infotypes-reference}} **[Documented]**
• For the three image context infoTypes the availability column lists asia, asia-southeast1, europe, europe-north1, global, us, us-central1, us-east4 and us-west1 {{D:infotypes-reference}} **[Documented]**
• "Image inspection and redaction are supported only in the following locations:" the same nine locations {{D:locations}} **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22, and the locations page lists a regional endpoint for it {{D:release-notes}} and {{D:locations}} **[Documented]**
• Input handling uses the same methods and body as the SD5 column (image bytes, 4 MB for `image.redact`, 0.5 MB for other content requests, format statements that conflict), so those rules and that conflict carry over **[Inferred]**
• "When you redact data from images, you can't include limits in your inspection configuration." {{D:redacting-sensitive-data-images}} **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User; API keys are accepted for `projects.image.*` methods {{D:redacting-sensitive-data-images}} and {{D:auth}} **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection only; the pricing page lists no separate price for image safety classification {{O:Sensitive Data Protection pricing page}} **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint {{D:limits}} **[Documented]**
• Launch stage of the three detectors (general availability or Preview) is not stated beyond the release note that says they are "available" (checked the infoType reference and release notes) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, the Python client, and an image-scanning location such as Singapore. Build a lawful, approved image set labelled by category, real and AI-generated, send each image asking for the three detectors, and compare findings with human labels at several thresholds. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; calls to `inspect_content` with the three `IMAGE_TYPE/CONTEXT/*` infoTypes in `asia-southeast1` or global **[Inferred]**
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
• How the image format conflict recorded in the SD5 column applies here (needs testing)
• Whether findings on very small, very large or multi-subject images are reliable, including minimum image size (not stated)
• How content-policy rules over image safety, documented only in Gemini Enterprise docs, differ from calling the image methods directly (cross-reference; content policies are inventory-only)
• Customer data terms for images sent to the API (not read)
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
