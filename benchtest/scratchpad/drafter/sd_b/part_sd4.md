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
• For plain strings with no record, the client docstring says the context is ignored: "plaintext would be used as is for encryption." ({{L:T|plaintext would be used as is for encryption.|2}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
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
Summary: **Needs a key, a surrogate name and a supported input.** Requests need a wrapped key in a matching region (or a transient or raw key), a surrogate annotation for free text, and values within AES-SIV or FPE limits. API keys cannot be used with wrapped keys. **[Documented]**
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
