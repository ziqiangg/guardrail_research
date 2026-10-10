## Column CK1: Cloak: Free-text PII detection and anonymisation
### R1
Summary: **Finds personal data in text and rewrites it.** Cloak's free-text tool detects entities such as names, NRICs and addresses in pasted text or uploaded files, then replaces, redacts, masks, aliases, pseudonymises or encrypts them. The result is rewritten text or a file. **[Documented]**
Detail:
• Cloak is GovTech's whole-of-government anonymisation service: "Cloak offers tabular and free-text anonymisation to enable agencies to anonymise data safely before data sharing and utilisation." (Cloak Guide, home page, read 2026-10-10) **[Documented]**
• Free-text anonymisation (FTA) "automatically detects and redacts/transforms sensitive information within unstructured text" (Cloak Guide, intro to FTA) **[Documented]**
• Inputs: "The tool supports pasted text input as well as file uploads (.csv, .pdf, .docx)." (Cloak Guide, intro to FTA) **[Documented]**
• Baseline entities: "Cloak detects and transforms 20+ baseline entity types (names, NRICs, addresses, dates, phone numbers, etc.)" (Cloak Guide, intro to FTA, image caption) **[Documented]**
• By default "Cloak scans your text for all available Entity Types and Replaces them with their data type", and the user can toggle each entity type and choose a technique per type (Cloak Guide, usage guide) **[Documented]**
• Techniques named in the guide: Replace, Replace (Unique), Redact, Mask, Alias, Pseudonymise and Encrypt (Cloak Guide, anonymisation techniques pages) **[Documented]**
• The vendor names a use on AI traffic: "Anonymise before sending to LLMs | Strip PII in real-time via API before data reaches external LLMs or other WOG products" (Cloak Guide, home page) **[Documented]**
• Portal use case: "Agencies integrate Cloak via API into chatbot services and WOG AI platforms to strip PII from user prompts in real-time before they reach external LLMs." (Developer Portal, use cases, last updated 21 Aug 2026) **[Documented]**
• FAQ: anonymising before sending data to GenAI "is a common use pattern, provided anonymisation happens before the data leaves the approved environment and the output is validated" (Cloak Guide, key FAQs) **[Documented]**
• The documented output is transformed text or files (text, .csv, .docx formats in the FAQ file-format table) **[Documented]**
• No safe or unsafe verdict, risk label or content classification is described (checked the FTA guide pages, FAQs, home page and portal pages; not stated) **[Not disclosed]**
• Custom entities are a separate function, covered in the column Cloak: Custom entity detection in free text (lists, regex and LLM): the FTA caption says Cloak also handles "custom entities defined via pattern matching, inclusion lists, or privately-hosted LLMs" (Cloak Guide, intro to FTA) **[Documented]**
• Cloak also has a tabular anonymisation tool and a Secrets Manager; they are separate tools from free-text anonymisation (Cloak Guide, home page) **[Documented]**
### R2
Summary: **Personal data in free text, tuned for Singapore.** Seventeen entity groups cover names, NRICs, phone numbers, emails, addresses, banking, dates and more. Scanned documents and images are not processed, and detection is probabilistic. **[Documented]**
Detail:
• The Entity Types page lists 17 groups: Name, NRIC (SG), Email Address, Phone Number, Nationality/Race/Religion, Address (SG), Location, Passport (SG), Currency, Credit Card, Bank Account Number (SG), Bank Account Number (IBAN), IP Address, URL, Date & Time, UEN (SG), Organization, plus Exceptions and Custom (Cloak Guide, entity types intro) **[Documented]**
• The Address page says "Cloak provides 4 address-related recognisers for Singapore addresses": SG_ADDRESS, SG_ADDRESS_POSTAL_CODE and SG_ADDRESS_UNIT_NUMBER are on by default and SG_ADDRESS_STREET is "OFF (advanced)" (Cloak Guide, Address page) **[Documented]**
• Counting one tag for each of the 16 groups other than Address, plus the 4 address tags, gives 20 baseline tags (PERSON, SG_NRIC_FIN, EMAIL_ADDRESS, PHONE_NUMBER, NRP, 4 address tags, LOCATION, SG_PASSPORT, CURRENCY, CREDIT_CARD, SG_BANK_ACCOUNT_NUMBER, IBAN_CODE, IP_ADDRESS, URL, DATE_TIME, SG_UEN, ORGANIZATION); the count is a tally of the entity pages, not a vendor figure **[Inferred]**
• Vendor count, version one: "Cloak detects and transforms 20+ baseline entity types" (Cloak Guide, intro to FTA; Developer Portal, features page, "Auto-detection of 20+ entity types") **[Documented]**
• Vendor count, version two: "Cloak detects 17+ entity types out of the box" (Developer Portal, FAQs, last updated 21 Aug 2026); the wording differs from the "20+" of version one **[Documented]**
• Singapore optimisation: "Singapore-optimised detection … (NRICs, local phone numbers, UENs, addresses, postal codes)" (cloak.gov.sg home page, read 2026-10-10) **[Documented]**
• NRIC page: covers "S", "T" (citizens, permanent residents) and "F", "G", "M" (long-term pass holders), with "Validation disabled: Both real and fake NRIC numbers following the format … are detected" (Cloak Guide, NRIC page) **[Documented]**
• Phone page: "Global coverage disabled: Only Singapore numbers are detected by default."; "Validation check is not included. Both real and fake phone numbers may be detected." (Cloak Guide, phone number page) **[Documented]**
• Name page: "Name refers to a person's Name (First, Last or Full Name), including ethnic names in roman characters." (Cloak Guide, Name page) **[Documented]**
• Language coverage beyond roman-script names, and the languages the detector supports (checked the entity pages, FAQs, home page and portal pages; not stated) **[Not disclosed]**
• Sensitive-attribute tag: NRP "detects values that correspond to a Nationality (e.g. Singaporean), Race (e.g. Chinese), Religion (e.g. Christian) and political groups" (Cloak Guide, NRP page) **[Documented]**
• The Developer Portal FAQs name "dates of birth" and "vehicle plate numbers" as detected types, and the Features page names "dates of birth" (Developer Portal, FAQs and features page) **[Documented]**
• No Cloak Guide entity page covers dates of birth or vehicle plate numbers; the Date & Time page lists only a generic DATE_TIME tag (checked all entity pages and the entity types intro) **[Not disclosed]**
• Whether the generic DATE_TIME tag catches a date of birth, and whether a vehicle plate type exists **[To be verified]**
• Probabilistic detection: "Free-text detection is probabilistic, so 100% recall should not be assumed." Results can be weaker for uncommon formats, all-caps names, formatting artefacts and contextual ambiguity (Cloak Guide, key FAQs) **[Documented]**
• Out of scope: "Cloak does not process scanned PDFs, screenshots, images or engineering drawings."; text inside images in a .docx "will not be detected as text" (Cloak Guide, key FAQs; usage guide) **[Documented]**
• Cloak's pages describe PII anonymisation only; no harmful-content, jailbreak or prompt-injection category appears on any page read, so those threats look outside its stated purpose (checked the FTA pages, FAQs, home page, portal pages) **[Inferred]**
• The data owner stays responsible: the user must check output for "remaining direct identifiers, quasi-identifier combinations, missed free-text entities and linkage risk" (Cloak Guide, key FAQs) **[Documented]**
### R3
Summary: **Any text or file passed in; no direction setting found.** The tool takes pasted text, CSV, PDF or DOCX and needs no conversation context. No page shows an input or output flag, so prompts, replies and retrieved text would all be handled as strings. **[Inferred]**
Detail:
• Inputs: "The tool supports pasted text input as well as file uploads (.csv, .pdf, .docx)." (Cloak Guide, intro to FTA) **[Documented]**
• Pasted text is capped at 20,000 characters; CSV, PDF (native or searchable) and DOCX files are accepted; scanned PDFs fail upload (Cloak Guide, usage guide) **[Documented]**
• "The anonymisation techniques selected will be implemented across all cells in CSV files and on all pages for both PDF and Word files." (Cloak Guide, usage guide) **[Documented]**
• The Web UI takes a job, shows an Original and an Anonymised preview, then prepares a download request; text and PDF projects "typically have a fast processing time" (Cloak Guide, usage guide) **[Documented]**
• "Real-time" use is documented for the API: "Strip PII in real-time via API before data reaches external LLMs" (Cloak Guide, home page); the API "gives you the same anonymisation capabilities as the Web UI" (Cloak Guide, API guide) **[Documented]**
• No input-or-output or prompt-or-response flag appears on any public page (checked all Cloak Guide pages, the Developer Portal pages and cloak.gov.sg for direction, inbound, outbound and response settings); the API schema is behind a login, so an API flag is not ruled out **[Not disclosed]**
• The API Guide and OpenAPI pages redirect to the docs login page: https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ and https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/ both end at "auth/otp-login" with redirect_reason=not_logged_in (HTTP 302 then a 200 login page, observed 2026-10-10) **[Documented]**
• The tool works on whatever string or file reaches it, so it would apply to prompts, responses, retrieved text and tool output; premise: text and files in, the vendor's LLM use case, and no direction flag found **[Inferred]**
• No system prompt, user prompt or conversation history is a documented input; the usage guide shows only text or files plus anonymisation settings (checked the usage guide and FTA pages; API schema not readable) **[Inferred]**
• Playbook, PII protection page, "Where PII can appear": "User prompts.", "Model outputs.", "Retrieved documents.", "Tool arguments and tool results." (a bulleted list); the page lists Cloak under "Detection tools" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• 2023 GovTech deck, GenAI workflow slide: the original prompt goes through "Detect PII" and "Anonymise PII" before the GenAI product, so the anonymise step acts on the prompt side (USENIX PEPR 2023 deck, slide 22; dated September 2023) **[Documented]**
• The same deck slide shows the "Anonymised Response" returning from the "Gen AI Magic!" box to the agency product with the placeholder "<hash value 1>" still in it (USENIX PEPR 2023 deck, slide 22, layout read from the rendered slide) **[Documented]**
• The deck draws no step that turns the placeholders back into the original values (checked slide 22 and the text of all 32 slides; the Mapping Table box sits on the agency product side) **[Not disclosed]**
### R4
Summary: **Named techniques, model not named.** Entities are found by an AI model (spaCy given as an example) plus regex, rule-based matching and checksums, hosted on the Government Commercial Cloud. Reached by web UI or API. **[Documented]**
Detail:
• "Entity types are identified either by the underlying AI Model (e.g. spaCy), and a combination of: Regex Patterning … Rule-based Matching … Validation using checksums (if applicable)" (Cloak Guide, entity types intro) **[Documented]**
• The same page links its spaCy example to spaCy's en_core_web_sm model page (Cloak Guide, entity types intro) **[Documented]**
• Which model Cloak runs, its version, any fine-tuning, and which entity uses the model versus rules (checked the entity pages, FAQs, credits, release notes, portal pages and the 2023 deck; not stated) **[Not disclosed]**
• Address entities list their method: SG_ADDRESS "Pattern matching", SG_ADDRESS_POSTAL_CODE "Regex", SG_ADDRESS_UNIT_NUMBER "Regex", SG_ADDRESS_STREET "Pattern matching" (Cloak Guide, Address page) **[Documented]**
• Scoring: Confidence Level "denotes the level of certainty / probability that a particular entity type is accurately detected by the algorithm" (Cloak Guide, confidence level page) **[Documented]**
• Hosting: "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment"; the portal tech stack lists "AWS GCC 2.0" (Cloak Guide, key FAQs; Developer Portal, features page) **[Documented]**
• Routes: Web UI, and API at L2 (Analytics.gov), L3 (GCC) and L4 (internet); a Python package exists but is "Tabular only; provided as-is with no active maintenance" (Cloak Guide, home page) **[Documented]**
• No self-hosting route for free-text anonymisation is documented: no repository, Hugging Face entry or free-text package turned up (checked the Cloak Guide, cloak.gov.sg, the portal, and GitHub searches of GovTechSG, opengovsg, govtech-responsibleai and datagovsg on 2026-10-10) **[Not disclosed]**
• LLM-enabled custom entity (Beta; see Cloak: Custom entity detection in free text (lists, regex and LLM)): "Cloak privately hosts a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS. No data is sent to external parties" (Cloak Guide, unstructured custom entities intro) **[Documented]**
• Encrypt technique (see Cloak: Reversible anonymisation and decryption (encrypt and restore)): "The encryption uses AES cypher in CBC mode"; "we have restricted encryption to only AES-256 CBC Mode Encryption" (Cloak Guide, Encrypt page) **[Documented]**
• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) **[Documented]**
• Release notes: v2.1.0 (19 March 2024) lists the ORGANIZATION entity type and FTA templates (Cloak Guide, release notes) **[Documented]**
• Release notes: v2.0.1 (4 December 2023) lists "[FTA] Added Word document support" (Cloak Guide, release notes) **[Documented]**
• The deployed version, and when later documented features shipped (Replace (Unique), the SG_ADDRESS recognisers, LLM entities; none is in the release notes) (checked release notes, home page, portal pages; not stated) **[Not disclosed]**
• The Encrypt page says "Microsoft Presidio has a built-in encryption functionality" and the entity types page links Presidio's supported-entities page (Cloak Guide, Encrypt page and entity types intro) **[Documented]**
• No GovTech page says Cloak is built on Presidio (checked the Cloak Guide, credits page, portal and cloak.gov.sg; the credits list neither Presidio nor spaCy) **[Not disclosed]**
• Cloak shares tag names such as PERSON, EMAIL_ADDRESS, PHONE_NUMBER and IBAN_CODE with Presidio's catalogue, which could mean reuse of Presidio recognisers; see Presidio: PII detection in text (Analyzer) **[Inferred]**
• Playbook: "Direct integration with the Sentinel API is coming soon." and a code stub "# Coming soon — Sentinel + Cloak integration is on the roadmap." (see GovTech Sentinel: PII detection and masking (AWS Bedrock) for Sentinel's own PII check) **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Sentinel's own pages do not mention Cloak (checked the Sentinel docs home and Sentinel-Guardrails wiki page for "cloak" on 2026-10-10; no hit) **[Not disclosed]**
### R5
Summary: **Rewritten text plus a findings table.** Output is transformed text or a file; the web UI adds a per-entity table with type and score. A confidence slider (default 0.30) sets the cut-off. The only accuracy claim is over 97 percent recall, no method. **[Documented]**
Detail:
• Output formats: direct text gives text, .csv gives .csv, native .pdf gives .docx, searchable .pdf gives .csv, .docx gives .docx; scanned .pdf is "Not supported" (Cloak Guide, key FAQs, supported file formats) **[Documented]**
• Default technique: Replace, "By default, it would be <ENTITY_NAME>", so a name becomes a tag such as PERSON in angle brackets (Cloak Guide, Replace page) **[Documented]**
• Web UI: Original Data on the left, Anonymised Data on the right; previews show the first cell of a CSV, the first page of a PDF and the first 200 words of a Word file (Cloak Guide, usage guide) **[Documented]**
• Review findings table: "listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score" (Cloak Guide, usage guide, image caption) **[Documented]**
• Files are delivered by a download request; an email gives the password "required to unzip the folder" (Cloak Guide, usage guide) **[Documented]**
• Confidence Level: "Entities below the specified threshold will not be anonymised"; raise it for false positives, lower it for missed PII (Cloak Guide, confidence level page) **[Documented]**
• The slider range and default come from image captions: "adjustment of the detection threshold from 0 to 1" (usage guide) and "set to the default value of 0.30" (confidence level page) **[Documented]**
• Developer Portal Features page: "Adjust detection sensitivity per entity type to balance recall and precision for your dataset" (Developer Portal, features page) **[Documented]**
• Cloak Guide: the Anonymisation Settings drawer has one "Adjust Confidence level" dropdown with a slider "set to the default value of 0.30" (Cloak Guide, confidence level page, captions) **[Documented]**
• Accuracy claim: ">97% recall for key PIIs like Name, NRIC and Email" (Cloak Guide, home page); a vendor claim with no method, dataset or precision figure **[Documented]**
• Terms clause 9.1 says the Service is provided "on an 'as is' and 'as available' basis without warranties of any kind", and 9.1.1 lists accuracy, completeness and correctness among the warranties disclaimed (Terms of Use dated 24 July 2024) **[Documented]**
• Method, test data, precision, F-score, per-entity or per-language figures for any recall number (checked the home page, FAQs, portal pages, release notes and the 2023 deck; none stated) **[Not disclosed]**
• Usage figures are not accuracy: "Currently processing >5 million PIIs removed per month across WOG" (Developer Portal, overview page, last updated 26 Aug 2026; vendor statistic) **[Documented]**
• Output is not automatically safe: "Cloak applies the transformations selected by the user, but the data owner must assess the final output" (Cloak Guide, key FAQs) **[Documented]**
• API response fields and error behaviour (the API Guide and OpenAPI pages are behind a login; not readable) **[Not disclosed]**
• 2023 deck: "API: Takes in unstructured text, returns mapping table and anonymized result." (USENIX PEPR 2023 deck, slide 22; may have changed since) **[Documented]**
### R6
Summary: **Text or files within size limits, plus settings.** Pasted text is capped at 20,000 characters, files at 500 MB (CSV) or 200 MB (PDF, DOCX). Settings choose entities, techniques, threshold and word lists. Access needs an approved account. **[Documented]**
Detail:
• Pasted text: "Maximum 20,000 characters (approx. 3,000 words) per submission." (Cloak Guide, usage guide) **[Documented]**
• File limits: CSV "Maximum 500 MB per file"; PDF and DOCX "Maximum 200 MB per file"; "Up to 100 files per project, with a total upload limit of 2 GB." (Cloak Guide, usage guide) **[Documented]**
• CSV files can only be uploaded with other CSV files; PDF and DOCX can be mixed; a CSV needs proper headers and .xlsx must be converted to .csv first (Cloak Guide, usage guide) **[Documented]**
• CSV processing time table: 20 rows by 1 column "1 minute", 100 by 1 "5 minutes", 100 by 2 "10 minutes", 5000 by 1 "4 hours" (Cloak Guide, usage guide) **[Documented]**
• Per-entity settings: toggle each entity type, choose its technique, set the Confidence Level and the Inclusion lists (Cloak Guide, usage guide) **[Documented]**
• Exceptions: "used to manually exclude words from being detected and anonymised" (Cloak Guide, Exceptions page) **[Documented]**
• Inclusion list on an existing entity: "You can add words individually or upload a CSV file containing up to 500 entries." (Cloak Guide, inclusion feature page) **[Documented]**
• Inclusion list limit as worded in the Important Notes table: "Only the first 500 words in a CSV upload will be used." (Cloak Guide, inclusion feature page; the same page gives the limit in entries and in words) **[Documented]**
• Inclusion list matching is "Word-sensitive" (exact spelling and punctuation must match) and "Not case-sensitive" (Cloak Guide, inclusion feature page) **[Documented]**
• Mask defaults: Number of Characters 3, Masking Type Suffix, Masking Character "-" (Cloak Guide, masking page, Usage Guide table) **[Documented]**
• Masking Type table: "Suffix: masks the starting characters" and "Prefix: masks the ending characters" (Cloak Guide, masking page) **[Documented]**
• Masking page example: 120414 becomes 120 followed by three asterisks and is described as "Transforms into a suffix masked value", which reads the other way from the Masking Type table (Cloak Guide, masking page, Example table) **[Documented]**
• Alias is "only available for the PERSON entity type" (Cloak Guide, Alias page) **[Documented]**
• Alias options Context and Offset both default to On (Cloak Guide, Alias page) **[Documented]**
• Pseudonymise uses "irreversible hashing (SHA-256) or (SHA-512) with a random salt" (Cloak Guide, Pseudonymisation page) **[Documented]**
• Replace (Unique) limits: available "On the Cloak Web App; For single CSV uploads; and For Cloak's baseline entities", not for PDF, DOCX, multi-file uploads or custom entities, and "up to two entity types per anonymisation job" (Cloak Guide, Replace (Unique) page) **[Documented]**
• Whether Replace (Unique) works on pasted text (the page lists CSV only as available and does not name pasted text in either list) **[Not disclosed]**
• Encrypt needs a secret key (an AES-256 key); the page shows an example key beside the transformed value (see Cloak: Reversible anonymisation and decryption (encrypt and restore)) (Cloak Guide, Encrypt page) **[Documented]**
• Templates: a free-text template stores "Entity types, anonymisation techniques, parameters, and score threshold"; free-text templates are personal and cannot be shared (Cloak Guide, templates page) **[Documented]**
• The FAQ names three tuning controls: Enhanced Detection for names, checksum validation for NRIC and UEN, and global detection for phone numbers; the pages read do not show where these are switched on (Cloak Guide, key FAQs) **[Documented]**
• API security levels: L2 (personalised token), L3 (system token), L4 (signature-based) (Cloak Guide, API guide) **[Documented]**
• API onboarding: an API key per security level; "complete our Cloak (API) Onboarding Form", and a key follows "within 1-2 business days" (Cloak Guide, API guide and key FAQs) **[Documented]**
• API parameters: the release notes name an "allow_list" parameter (v2.0.5); the API guide names custom recognisers, "fine-grained confidence score tuning" and the allow list; request fields, headers and limits (checked the API guide, FAQs, release notes, portal pages; schema behind a login) **[Not disclosed]**
• Regex custom entity, API only (see Cloak: Custom entity detection in free text (lists, regex and LLM)): "Define custom context words that must appear near a regex match" and "Set different confidence scores for each regex pattern" (Cloak Guide, structured custom entities page) **[Documented]**
• Web UI access: WOG users sign in with WOG-AD; other approved users register, and vendors complete TechPass onboarding after Cloak Ops approval (Cloak Guide, key FAQs and registration guide) **[Documented]**
• Non-government entities "Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step." (Cloak Guide, key FAQs) **[Documented]**
• Who may use it, Cloak Guide: Cloak "is open to select non-government entities (e.g. public healthcare)" (Cloak Guide, home page); the playbook words it differently **[Documented]**
• Who may use it, playbook: "GovTech's dedicated internal service for comprehensive and localised PII detection" (Responsible AI playbook, privacy improvements page) **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Data ceiling: "You shall not upload any information, data and material that are classified above the following classifications: Confidential (Cloud-Eligible) \ Sensitive (High)" (Terms of Use, Schedule clause 4.6, dated 24 July 2024) **[Documented]**
• Retention: "Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request." (Cloak Guide, key FAQs) **[Documented]**
• cloak.gov.sg banner: "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period." (cloak.gov.sg home page, observed 2026-10-10) **[Documented]**
• Cost: "Cloak is currently free for all approved users"; "For FY26, there is no charge." (Cloak Guide, home page) **[Documented]**
### R7
Summary: **Minimum setup:** Cloak has no public code or package, so a bench would need approved Web UI or API access. A bench could send short synthetic Singapore-style prompts with planted names, NRICs, addresses and phone numbers, and compare each output with the expected tags. Terms clause 3.4.7 mentions benchmarking, an open licensing question. **[Inferred]**
Detail:
• **Minimum setup:** the public pages are documentation only, so a bench could not run Cloak without an approved account or API key; a first trial would be the Web UI with a short synthetic text, or an API key after the onboarding form (access routes as in R6) **[Inferred]**
• Access conditions: a Web UI account needs WOG-AD or TechPass registration; non-public-sector use is "restricted solely for such purpose that GovTech has consented to in writing (including via email)" (Terms of Use, clause 3.3) **[Documented]**
• Terms of Use, clause 3.3 defines the term: "'Public Sector Entities' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)" **[Documented]**
• Terms of Use, clause 3.4 and 3.4.7: "You shall not, and shall not authorise or permit any third party to … perform any benchmarking tests or analyses of the Service" **[Documented]**
• Terms of Use, Schedule clause 2.2: "You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency." **[Documented]**
• Terms of Use, clauses 3.4.9 and 3.4.11: no transfer or sharing of "license keys" and no "third party access to the Service" (Terms of Use dated 24 July 2024) **[Documented]**
• Possible test inputs for a bench: short synthetic prompts with known planted entities, namely names of Malay, Indian and Chinese structure, NRIC-shaped numbers, Singapore addresses with postal codes and unit numbers, phone numbers, emails and UENs **[Inferred]**
• A bench could add near-miss strings, such as NRIC-shaped numbers that fail the checksum, 9-digit numbers that are not phone numbers, and street names that are also common words, to see what the default detection does with them **[Inferred]**
• A bench could check the 20,000-character limit, compare the default Confidence Level of 0.30 with higher and lower settings, and compare Replace with Replace (Unique) on a single CSV **[Inferred]**
• Possible comparator: Presidio with Singapore recognisers as a clearly labelled stand-in, never reported as Cloak (see Presidio: PII detection in text (Analyzer)) **[Inferred]**
• Sensitive test data (real personal data) is a bench-design question; a bench could start with made-up values, and Terms Schedule 4.6 sets a data ceiling for anything uploaded (see R6) **[Inferred]**
### R8
Summary: **Key open questions.** Whether Terms clause 3.4.7 allows benchmarking, the API schema and any direction flag, the model and version, accuracy beyond the recall claim, language coverage, short-prompt latency, and the Sentinel integration.
Detail:
• Does Terms clause 3.4.7 ("perform any benchmarking tests or analyses of the Service") bar a bench comparison, and would GovTech's written consent under clause 3.3 cover it? (the Terms define no benchmarking term and state no exception; checked all 15 pages; decided before any bench run)
• API request and response schemas, auth header, limits, latency and whether a direction flag exists (checked the API guide, FAQs, release notes, portal pages; the API Guide and OpenAPI pages need a login)
• Which NER model backs the baseline entities, its version and tuning, and whether any recogniser comes from Presidio (checked the entity pages, credits, release notes, portal pages and the 2023 deck; not stated)
• What the ">97% recall" claim measures (data set, entity types, language mix, precision) (checked the home page, FAQs, portal pages and the 2023 deck; not stated)
• Language coverage beyond roman-script names, for example Chinese-character, Tamil or Malay text (checked the entity pages and FAQs; not stated)
• Processing time for a short prompt through the API, given the "real-time" wording (only the CSV time table and "fast processing time" for text are given)
• Deployed version and the ship dates of Replace (Unique), the SG_ADDRESS recognisers and LLM entities (release notes stop at v2.2.2)
• Whether the Web UI and the API give identical results, and which features are API only (context words, per-pattern scores, allow list)
• Whether the confidence threshold is global or per entity type (portal says per entity type; the guide shows one slider)
• Where checksum validation for NRIC and UEN, global phone detection and Enhanced Detection for names are enabled (named in the FAQ; controls not shown on the entity pages)
• Whether dates of birth and vehicle plate numbers are detected, and under which tag (portal pages name them; no entity page)
• Whether Replace (Unique) works on pasted text (the page lists CSV only)
• Sentinel integration: status and date (the playbook says "coming soon"; checked the Sentinel docs pages, no mention); see GovTech Sentinel: PII detection and masking (AWS Bedrock)
• The "ContextGuard Demo" on the Video Guides page: its relation to Cloak (the page gives only a title and section labels, "Feature A demo" and "Feature B demo")
### R9
Summary: Cloak Guide Markdown pages, the Cloak product site, GovTech Developer Portal pages, the Terms PDF, a 2023 GovTech deck and the GovTech playbook, all read 2026-10-10.
Detail:
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/intro-to-fta.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/intro.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/name.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/nric.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/phone-number.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/nrp.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/full-address.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/datetime.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/exceptions.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/confidence-level.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/inclusion-feature.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace-unique.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/masking/intro.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/alias.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/pseudonymisation.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/encrypt.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-structured.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/intro.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/templates/templates.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/developer-api-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/registration-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/credits.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/video-guides.md
• https://docs.developer.tech.gov.sg/docs/cloak-api-guide/
• https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/
• https://www.cloak.gov.sg
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/overview
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/use-cases
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/faqs
• https://file.go.gov.sg/cloak-terms.pdf
• https://www.usenix.org/system/files/pepr23_slides-tang.pdf
• https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx
• https://www.aiguardian.gov.sg/docs
• https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails

## Column CK2: Cloak: Custom entity detection in free text (lists, regex and LLM)
### R1
Summary: **Adds your own entity types to free-text anonymisation.** A custom entity can be a fixed word list, a regex pattern or, in Beta, an LLM given a definition and examples. Matches are then transformed like the built-in entities. **[Documented]**
Detail:
• Home page: "Customisable - add any custom entity using inclusion lists, pattern-matching (regex), or privately-hosted LLMs" (Cloak Guide, home page, read 2026-10-10) **[Documented]**
• Custom entity page: "If no entity type matches the data you are trying to anonymise, you may add a Custom Entity. This function is similar to the "Find and Replace" feature offered on some text editors" (Cloak Guide, entity types, Custom) **[Documented]**
• Fixed list route: "If you have a known, finite list of words or phrases to detect (e.g. hospital names, school names, or organisation acronyms), you can use the Inclusion Feature together with a Custom Entity to anonymise them." (Cloak Guide, fixed-list page) **[Documented]**
• Regex route: "Custom Entities are used to define entities with structured data patterns specific to your needs." (Cloak Guide, structured page) **[Documented]**
• LLM route: "Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning." (Cloak Guide, unstructured intro) **[Documented]**
• LLM route inputs: for the LLM-based approach the Custom page lists "Define your custom entity" and "Give some examples" (Cloak Guide, entity types, Custom) **[Documented]**
• LLM route status: the unstructured intro marks the feature "[Beta Feature]" (Cloak Guide, unstructured intro) **[Documented]**
• Inclusion list on a built-in entity is a related control, not a new entity: "specify additional words or phrases that should be detected and anonymised under an existing entity type" (Cloak Guide, Inclusion Feature page) **[Documented]**
• The result is transformed text: "Click Start anonymisation. Your text is now transformed with the new custom entity applied." (fixed-list page) **[Documented]**
• Cloak's home page describes the LLM entity as: "Define custom sensitive entities using LLM-powered detection — add organisation-specific terms or domain-specific identifiers without re-training a model" (www.cloak.gov.sg home page) **[Documented]**
• GovTech's playbook says: "Cloak also offers LLM-enabled custom entity detection to protect custom, domain-specific or localised entities unique to your use case." (Responsible AI playbook, privacy improvements page) **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Exceptions is the opposite control, "used to manually exclude words from being detected and anonymised"; it is covered in the column Cloak: Free-text PII detection and anonymisation (Cloak Guide, Exceptions page) **[Documented]**
• A safe or unsafe verdict, or a score, for a custom entity (checked the custom entity pages and the FTA usage guide: they show only transformed output, and whether custom matches appear in the Findings table is not stated) **[Not disclosed]**
### R2
Summary: **Domain terms the built-in entities miss.** Documented examples are hospital case numbers, car licence numbers, unusual date formats, usernames and disease names. Free-text detection is probabilistic, so full recall should not be assumed. **[Documented]**
Detail:
• Fixed list fits when "You have a predefined list of terms that Cloak's analyser does not recognise by default" and "The terms do not follow a predictable pattern; regular expressions are not suitable" (fixed-list page) **[Documented]**
• Regex sample use cases named on the structured page: "Car license number", "Unusual date format" and "Username", each with a sample regular expression (Cloak Guide, structured page) **[Documented]**
• Regex versus built-in conflict: "Suppose a 10-digit hospital case number (e.g. 1234567890) is consistently detected as a Bank Account Number because both values follow a similar numeric format." (structured page) **[Documented]**
• LLM entity targets values "without predictable, fixed patterns", with "School names", "Medical conditions" and "Free-text descriptions" as examples (unstructured intro) **[Documented]**
• LLM entity is recommended when "Your entity is not detected accurately due to the unique context of your documents (e.g., formatting)." (unstructured intro) **[Documented]**
• Sample DISEASE: "User wants to anonymise names of medical conditions, which are not pre-existing entities in Cloak or other common NLP models." (disease sample page) **[Documented]**
• Sample DATE_TIME_SPECIFIC: the built-in DATE_TIME entity exists "but the user requires more control over what to and not to detect" (date-time sample page) **[Documented]**
• Sample PERSON_NAME: "detection is affected when names are present in sections of their document that include XML tags" (person-name sample page) **[Documented]**
• FAQ choice table: "Inclusion list | The exact values are known (e.g. a staff list, building names)"; "Pattern matching (regex) | The identifier follows stable rules (length, prefix, suffix, separators)"; "LLM-enabled custom entity | The target is contextual or domain-specific and cannot be expressed as exact values or deterministic rules" (Cloak Guide, FAQs) **[Documented]**
• Limits on all detection: "Free-text detection is probabilistic, so 100% recall should not be assumed." and results "can be weaker" for formatting issues such as "HTML tags, markdown, encoding artefacts, entities split across lines" (Cloak Guide, FAQs) **[Documented]**
• Out of scope per FAQs: "Cloak does not process scanned PDFs, screenshots, images or engineering drawings."; the usage guide adds "Texts within images will not be detected as text." for .docx files **[Documented]**
• Languages for custom entities: the guidance examples are English (Chinese and Malay name examples such as "Tan Mei Ling" and "Mohammad Bin Ali" in English text); no page states supported languages (checked the custom entity pages, write-prompts page, samples, FAQs and home page) **[Not disclosed]**
• Prompt-injection, jailbreak or harmful-content detection is not a stated purpose of custom entities (premise: the FTA intro says the tool "automatically detects and redacts/transforms sensitive information within unstructured text" and lists no such function) **[Inferred]**
### R3
Summary: **A setting applied to free text in a project.** A custom entity runs on pasted text or csv, pdf and docx uploads. No direction flag was found, so it applies to prompts, responses or retrieved text sent as a string or file. **[Inferred]**
Detail:
• Where it is defined: the Anonymisation Settings button, then the Custom entities tab, then "+ Add a custom entity" (fixed-list page, steps 1 and 2; Cloak Guide) **[Documented]**
• Input forms: pasted text, "Maximum 20,000 characters (approx. 3,000 words) per submission", or files (.csv, .pdf, .docx) (Cloak Guide, usage guide) **[Documented]**
• Scope of a setting: "The anonymisation techniques selected will be implemented across all cells in CSV files and on all pages for both PDF and Word files." (usage guide) **[Documented]**
• Output delivery: "Once you are done with your transformations, click on Download to proceed with the download request." (usage guide) **[Documented]**
• Vendor use on AI traffic: "Strip PII in real-time via API before data reaches external LLMs or other WOG products" (Cloak Guide, home page, use cases table) **[Documented]**
• Prompts, responses, retrieved text and tool output can all be sent as a string or file, so a custom entity applies to each (premise: string or file input and the vendor's LLM use case above) **[Inferred]**
• Direction: no input or output flag, role or setting appears on the custom entity pages, the FTA usage guide, the public API guide page or the portal pages (searched for direction, inbound, outbound, input type, response); the API schema is behind login **[Not disclosed]**
• Real-time path: whether an LLM-enabled entity runs on the real-time API path is not stated; the public API guide names only "custom recognisers (regex patterns, context words)" (checked the API guide page, FAQs and portal pages) **[Not disclosed]**
• LLM entity timing: "Including an LLM-enabled custom entity may increase processing times to up to 8 hours." (unstructured intro) **[Documented]**
• Quick iteration: "Test your definition and examples using Cloak's transformation preview or run a job on a smaller dataset (e.g., <100 documents, which should take <20min)." (write-prompts page) **[Documented]**
• Preview limits: "CSV preview shows first cell only", "PDF preview shows first page only", "Word preview shows first 200 words only" (usage guide) **[Documented]**
• Context needed: the documented inputs are the entity name, a list, pattern or definition with examples, and the text; no page describes use of a system prompt or conversation history (premise: the custom entity pages list no such input) **[Inferred]**
### R4
Summary: **Three mechanisms: list, regex and few-shot LLM.** Lists match exact words, regex matches patterns, and the Beta LLM entity is prompted with 3 to 5 examples on a privately hosted model on Government Commercial Cloud. **[Documented]**
Detail:
• List: "You want exact-match detection for specific words or phrases" (fixed-list page) **[Documented]**
• List is "word-sensitive: exact spelling and punctuation must match", so listed "Changi General Hospital" does not match "Changi-General-Hospital" (fixed-list page) **[Documented]**
• List is "not case-sensitive": listed "CGH" also matches "cgh" (fixed-list page) **[Documented]**
• Regex: "These entities utilise regular expressions to recognise and anonymise data based on the patterns you configure." (structured page) **[Documented]**
• Regex release: v2.1.5, 3 July 2024, lists "[FTA] Regex custom entities" (Cloak Guide, release notes) **[Documented]**
• Regex dialect, flags and match timeouts are not stated; the page points to regex101.com and pair.gov.sg for help (checked the structured page, Custom page and public API guide page) **[Not disclosed]**
• Pattern-matching entity fields: "Fill in the regular expression representing your custom entity", "Select your anonymisation technique of choice" and "Fill in the word(s) or phase(s) which you wish to detect" (Custom page, spelling as printed) **[Documented]**
• Inclusion bulk upload: v2.1.4, 4 June 2024, "[FTA] Allow bulk upload of inclusion/ exclusion list (e.g. txt or csv file)" (release notes) **[Documented]**
• LLM hosting: "Cloak privately hosts a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS. No data is sent to external parties" (unstructured intro) **[Documented]**
• LLM method: "Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning. This approach only needs a small set of 3-5 examples (labelled data)" (unstructured intro) **[Documented]**
• LLM status and limit: "[Beta Feature] Currently, only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)." (unstructured intro) **[Documented]**
• LLM roadmap wording: "We're working to expand support to larger datasets, multiple entities, and shorter processing times." (unstructured intro) **[Documented]**
• Web UI limit per project: "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time." (Cloak Guide, FAQs) **[Documented]**
• Language model name, size, version and prompt template (checked the unstructured intro, add-entities, write-prompts and three sample pages, FAQs, home page, portal pages, release notes, credits page, the 2023 GovTech deck and the playbook) **[Not disclosed]**
• Release history: the release notes name no LLM entity, so the deployed version and the LLM entity's release date are not given (checked the release notes page in full; highest version v2.2.2 of 4 August 2024, latest dated entry v2.2.1 of 28 August 2024) **[Not disclosed]**
• API route: the API offers "custom recognisers (regex patterns, context words), fine-grained confidence score tuning, or the allow list feature via code" (Cloak Guide, API guide) **[Documented]**
• Portal roadmap lists "Improve performance of free-text anonymisation through novel LLM-based approaches" as a roadmap item, not a current feature (developer portal, Features and Roadmap, last updated 21 Aug 2026) **[Documented]**
• Techstack: "AWS GCC 2.0" (developer portal, Features and Roadmap) **[Documented]**
• Closed hosted service: no public repo or model was found (GitHub repository search for "cloak" in the GovTechSG, opengovsg, govtech-responsibleai and datagovsg orgs returned 0 results on 2026-10-10; checked the Cloak Guide and portal pages) **[Not disclosed]**
• The offline package covers only "Cloak's tabular anonymisation features", so free-text custom entities have no offline route (premise: package page text) **[Inferred]**
• Cross-reference: see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); no GovTech page says Cloak's custom entities are Presidio recognisers (premise for any link: the shared terms "custom recognisers" and "context words") **[Inferred]**
### R5
Summary: **Transformed text for each custom match.** Each match is replaced or otherwise transformed with the technique chosen for that entity. The result is anonymised text or a file, and an email says when an LLM entity job completes. **[Documented]**
Detail:
• Technique per custom entity: "Select your anonymisation technique of choice." (Custom page) **[Documented]**
• Default replacement text: "By default, it would be <ENTITY_NAME>." (Cloak Guide, Replace page) **[Documented]**
• Fixed list result caption: "The anonymisation result with hospital names and acronyms replaced by HOSPITAL tags." (fixed-list page) **[Documented]**
• LLM result caption: "The project page showing the anonymised output with disease names replaced by the DISEASE tag" (add-entities page) **[Documented]**
• Findings table for detected entities in general: "The Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score." (usage guide caption) **[Documented]**
• Whether custom entities of each kind appear in the Findings table with a score (checked the usage guide and custom entity pages) **[Not disclosed]**
• Threshold: "Entities below the specified threshold will not be anonymised" and a slider "set to the default value of 0.30" (Cloak Guide, confidence level page, caption) **[Documented]**
• Whether the 0.30 threshold applies to regex, list or LLM entities (checked the confidence level page and custom entity pages) **[Not disclosed]**
• API regex scores: the API lets users "Set different confidence scores for each regex pattern" (structured page, "sign-in required" for the API guide) **[Documented]**
• Vendor example without figures: the base DATE_TIME entity "over-detects by also replacing relative temporal references such as "42-year-old" and "2 hours"" while DATE_TIME_SPECIFIC does not (date-time sample page, image caption) **[Documented]**
• LLM entity completion: the user is notified by email when the job completes (unstructured intro) **[Documented]**
• Download: "An email containing the password required to unzip the folder will be sent to you." (usage guide) **[Documented]**
• Vendor claim ">97% recall for key PIIs like Name, NRIC and Email" covers built-in entities, with no method, data set or precision stated (Cloak Guide, home page) **[Documented]**
• Precision, recall or F1 for list, regex or LLM custom entities (checked the home, overview and FAQ pages, the custom entity pages, the samples and the 2023 deck) **[Not disclosed]**
• API response format for custom entities (the API guide and OpenAPI pages redirect to a login page, HTTP 302 then a 200 login page at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in, observed 2026-10-10) **[Not disclosed]**
### R6
Summary: **A list, a regex or examples.** A list takes up to 500 (words or entries; the docs differ), a regex takes a pattern, and the LLM entity takes a definition and 3 to 5 examples. Context words and per-pattern scores are API only. **[Documented]**
Detail:
• List input: "The CSV to be uploaded should contain a maximum of 500 words listed in the first column." and "Only the first 500 words in the CSV will be used." (fixed-list page) **[Documented]**
• Inclusion page unit: "You can add words individually or upload a CSV file containing up to 500 entries." (Inclusion Feature page) **[Documented]**
• Regex input: a regular expression, a transformation type and optional words (Custom page, "Fill in the regular expression representing your custom entity") **[Documented]**
• LLM input: "Input your Definition and Examples", then label each example by typing the output in the "Output for Example 1" field (add-entities page, steps 5 and 6) **[Documented]**
• Example count: "Include 3-5 examples that captures the diversity present in your dataset." (write-prompts page) **[Documented]**
• Name tip: "PERSON_NAME" and "BUILDING_NAME" are positive examples and "NAME" a negative one under "Reduce ambiguity" (write-prompts page) **[Documented]**
• Definition tip: "Name of a person residing in Singapore..." is a positive example and "Name of a person" a negative one under "Provide context and common attributes" (write-prompts page) **[Documented]**
• LLM limits: 1 entity per dataset (up to 5,000 documents) and up to 8 hours of processing (unstructured intro) **[Documented]**
• Save and reuse: "To reuse this custom entity configuration in other projects, save your settings as a Template" (fixed-list page); free-text templates "Not shareable" (Cloak Guide, templates page) **[Documented]**
• Replace (Unique) is "not currently available for" "Custom entities (including custom regex and dictionary entities)" (Cloak Guide, Replace (Unique) page) **[Documented]**
• API-only settings: context words that "must appear near a regex match", per-pattern scores and the allow list; full details need sign-in (structured page, API guide page) **[Documented]**
• API parameters and request schema for custom entities (checked the public API guide and release notes; the API guide and OpenAPI pages redirect to login) **[Not disclosed]**
• Access: the Web UI is open to WOG users via WOG-AD and to approved non-WOG users who register; API access needs the Onboarding Form and gives a key "within 1-2 business days" (Cloak Guide, FAQs, API guide) **[Documented]**
• Data ceiling: LLM entity use is "safe for data classified up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)" (unstructured intro); the Terms Schedule 4.6 sets the same ceiling (Terms of Use dated 24 July 2024) **[Documented]**
• File limits: CSV 500 MB per file, PDF and DOCX 200 MB per file, 100 files and 2 GB per project (usage guide) **[Documented]**
• Maintenance: "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period." (www.cloak.gov.sg banner, read 2026-10-10) **[Documented]**
### R7
Summary: **Minimum setup:** documentation only today; a Web UI trial needs an approved Cloak account and the API needs an onboarding key. A bench could, once permitted, run synthetic text through one list, one regex and one LLM entity on under 100 documents, then compare with a baseline-only run. **[Inferred]**
Detail:
• **Minimum setup:** the public pages are documentation only; a suggested first step is a Web UI project with synthetic text, one list entity, one regex entity and one LLM entity, compared with a run on built-in entities alone **[Inferred]**
• Access to try it: Web UI needs WOG-AD or a TechPass account approved by Cloak Ops; API needs the Onboarding Form and a key; non-public-sector use needs GovTech's written consent to a stated purpose (Terms clause 3.3) (Cloak Guide, registration guide and FAQs; Terms PDF) **[Documented]**
• Terms clause 3.4.7 lists "perform any benchmarking tests or analyses of the Service" among the things the user shall not do, so a bench could first seek GovTech's written view **[Inferred]**
• Possible test text: short synthetic notes with planted terms (made-up hospital names and acronyms, a made-up car licence format, unusual date formats, usernames, disease names with misspellings), using no real personal data (sensitive test data is decided at bench design) **[Inferred]**
• Possible list checks: exact-match behaviour, the hyphen variant that the page says will not match, the case-insensitive variant, and the 500-word cut-off **[Inferred]**
• Possible regex checks: sample patterns from the structured page, then a value that also looks like a built-in entity (such as a 10-digit case number against Bank Account Number) to see which entity wins **[Inferred]**
• Possible LLM checks: 3 to 5 examples, under 100 documents (the page says under 20 minutes), then a wider run, with the Wednesday maintenance window avoided **[Inferred]**
• Possible comparison source: Presidio with custom recognisers as a clearly labelled stand-in, never reported as Cloak (see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)) **[Inferred]**
### R8
Summary: **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, which language model backs the LLM entity, accuracy and languages for custom entities, API support for the LLM entity, and how custom and built-in entities rank when they overlap.
Detail:
• Terms clause 3.4 says "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 reads "perform any benchmarking tests or analyses of the Service;" (Terms of Use dated 24 July 2024). Whether a comparison bench falls under it is not stated (the Terms define no benchmarking term; checked all 15 pages); decided before any bench run
• Terms clause 3.3 limits non-public-sector use to "such purpose that GovTech has consented to in writing (including via email)"; whether a bench could obtain that consent (agency onboarding is the other route)
• Which language model, size and version serve the LLM entity, and whether the Beta label is still current (checked the Cloak Guide, portal pages, release notes and the 2023 deck; the release notes end at v2.2.2 and v2.2.1 of August 2024)
• Accuracy for list, regex and LLM entities: no figure is published (checked the custom entity pages, samples, home, overview, FAQs and the 2023 deck); needs testing
• Languages and scripts supported by the LLM entity and by regex matching (not stated)
• Whether the API accepts an LLM-enabled entity and what its request schema is (the API guide and OpenAPI pages are behind login)
• Whether the 0.30 confidence threshold applies to custom entities, and whether custom entities show a score in the Findings table
• Which entity wins when a custom entity and a built-in entity match the same span (the structured page only advises disabling or tuning the built-in entity)
• What a "document" is in "up to 5,000 documents", and the latency of an LLM entity on one short prompt (documented times are for datasets: under 20 minutes for under 100 documents, up to 8 hours)
• Regex dialect, flags and timeouts (the page names regex101.com and pair.gov.sg only)
• Whether the 500 limit counts words or entries (the fixed-list page says words, the Inclusion page says entries)
• Whether the LLM-enabled custom entity limit is per dataset or per project (the unstructured intro says "only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)" and the FAQs say "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time"; needs testing)
• Whether Web UI and API give the same custom-entity results (the API guide says it gives "the same anonymisation capabilities as the Web UI" and also offers extra parameters)
• Playbook says Cloak is "GovTech's dedicated internal service" while the Cloak Guide says it is open to select non-government entities; and Sentinel integration is "coming soon" per the playbook (checked the Sentinel docs pages /docs and /docs/wiki/Sentinel-Guardrails: no mention of Cloak)
• The Video Guides page lists a "ContextGuard Demo" with no description of how it relates to Cloak (checked the Cloak Guide and portal pages)
### R9
Summary: Cloak Guide pages (docsify Markdown), the www.cloak.gov.sg home page, GovTech developer portal pages, the Cloak Terms of Use PDF, and GovTech's Responsible AI playbook.
Detail:
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/intro-to-fta.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/custom.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/exceptions.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-fixed-list.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-structured.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/intro.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/add-entities.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/write-prompts.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/disease.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/datetime-specific.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/person-name.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/inclusion-feature.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/confidence-level.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace-unique.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/templates/templates.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/developer-api-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/packages-anonymiser.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/registration-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-api-guide/
• https://www.cloak.gov.sg
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap
• https://file.go.gov.sg/cloak-terms.pdf
• https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx
• https://www.aiguardian.gov.sg/docs
• https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails

## Column CK3: Cloak: Reversible anonymisation and decryption (encrypt and restore)
### R1
Summary: **Encrypts chosen entities and decrypts them later.** The Encrypt technique replaces each detected value with AES-256 CBC ciphertext under a key kept in the Secrets Manager, and free-text decryption restores one value at a time in the Web UI. Pseudonymise is one-way. **[Documented]**
Detail:
• Anonymise side: "The encryption uses AES cypher in CBC mode and requires a cryptographic key as an input for both encryption and decryption." (Cloak Guide, Encrypt page, read 2026-10-10) **[Documented]**
• Anonymise side, mode: "Due to security reasons, we have restricted encryption to only AES-256 CBC Mode Encryption." (Cloak Guide, Encrypt page) **[Documented]**
• Anonymise side, scope: the settings drawer sets "the corresponding anonymisation technique to be applied for each entity type" (Cloak Guide, usage guide) **[Documented]**
• Anonymise side, one-way contrast: Pseudonymisation values "are generated by irreversible hashing (SHA-256) or (SHA-512) with a random salt applied to prevent brute-force attacks" (Cloak Guide, Pseudonymisation page) **[Documented]**
• Restore side: "The Web UI currently supports decrypting one value at a time (paste into the text field)." (Cloak Guide, free-text decryption page) **[Documented]**
• Restore side, bulk: for "multiple values or a file of encrypted data" the page points to the Free-Text Decryption API, "which supports looping through rows in a CSV" (free-text decryption page; the API page is behind login) **[Documented]**
• Key management: "Cloak provides a secure way to store, manage, and share the encryption keys and salts used in your anonymisation jobs." (Cloak Guide, Secret Sharing and Decryption page) **[Documented]**
• Home page features: "Encrypt identifiers consistently across datasets using shared secrets" and "Decrypt data when needed through the Web UI or API" (Cloak Guide, home page) **[Documented]**
• Mapping-table route in the API: "You can achieve Replace (Unique) behaviour programmatically using Cloak's `/analyze` endpoint and a mapping table you maintain." (Cloak Guide, Replace (Unique) page) **[Documented]**
• Restoring placeholders from a mapping table the caller keeps is a possible way to reverse Replace (Unique) output (premise: the page says the mapping table is maintained by the caller; no page describes restoring from it) **[Inferred]**
• GovTech 2023 deck slide labels: "Detect PII", "Anonymise PII", "Mapping Table" and "Anonymised Response", with "API: Takes in unstructured text, returns mapping table and anonymized result." (USENIX PEPR 2023 slides, slide 22, 11 Sep 2023; may have changed) **[Documented]**
### R2
Summary: **Keeps values linkable or restorable without exposing them.** Documented aims are consistent identifiers across datasets, safer key sharing, and keeping personal data out of external LLM prompts. Encrypt is reversible; Pseudonymise is one-way. **[Documented]**
Detail:
• "Consistent anonymisation across datasets - Use the same keys or salts to encrypt or pseudonymise entities consistently, enabling dataset linkage on primary keys without exposing the originals." (Cloak Guide, Secret Sharing and Decryption page) **[Documented]**
• "Secure sharing and continuity - Share secrets with colleagues without exposing the underlying key material, and ensure access persists across role changes and departures." (same page) **[Documented]**
• The page says this "replaces insecure practices like storing keys in spreadsheets or emailing them between colleagues" (same page) **[Documented]**
• Home use case: "Multiple data owners anonymise independently using the same secret, producing data that can still be linked on a common encrypted identifier" (Cloak Guide, home page) **[Documented]**
• Pseudonyms persist but cannot be undone: "irreversible and persistent pseudonyms" that are the same "within and across different datasets, conditioned on using the same salt value" (Pseudonymisation page) **[Documented]**
• Encrypt is the reversible side: the cipher "requires a cryptographic key as an input for both encryption and decryption" (Cloak Guide, Encrypt page) **[Documented]**
• LLM leakage framing: "Potential privacy leakages from usage of LLM products in the public sector." and "Outgoing prompt does not leak PII to overseas servers or ChatGPT" (USENIX PEPR 2023 slides, slides 21 and 22, 11 Sep 2023) **[Documented]**
• Whether Replace, Redact, Mask or Alias output can be reversed (checked the Replace, Redact, Masking and Alias pages, which describe the transformation only) **[Not disclosed]**
• Residual risk: "the data owner must assess the final output for remaining direct identifiers, quasi-identifier combinations, missed free-text entities and linkage risk." (Cloak Guide, FAQs) **[Documented]**
• An entity the detector misses stays in clear text, because Encrypt acts only on detected entities (premise: FAQ "Free-text detection is probabilistic, so 100% recall should not be assumed.") **[Inferred]**
• Presidio's reversible route is covered in the column Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt) (premise: both products offer an encrypt and a decrypt step) **[Inferred]**
### R3
Summary: **Encrypt on the way out, decrypt on the way back.** Encrypt runs inside a free-text job on a prompt string or file; decrypt takes one pasted ciphertext in the Web UI, or rows through the API. No direction flag or prompt context is documented. **[Inferred]**
Detail:
• Anonymise side: Encrypt is chosen per entity type: "toggle the detection of Entity Types and the corresponding anonymisation technique to be applied for each entity type" (Cloak Guide, usage guide) **[Documented]**
• Anonymise side input: pasted text up to "20,000 characters (approx. 3,000 words)" or .csv, .pdf and .docx files (usage guide) **[Documented]**
• Anonymise side vendor use: "Strip PII in real-time via API before data reaches external LLMs or other WOG products" (home page use cases) **[Documented]**
• Restore side Web UI: "Input your encrypted value into the left text field." and the secret is selected in step 2 (free-text decryption page) **[Documented]**
• Restore side scope: the guide's own link text is "Free-text Decryption Guide - Decrypt individual encrypted values" (Secret Sharing and Decryption page) **[Documented]**
• Restore side, bulk: for "multiple values or a file of encrypted data" the page points to the Free-Text Decryption API, "which supports looping through rows in a CSV" (free-text decryption page; the API page is behind a login) **[Documented]**
• Restore side, whole text: whether one call can restore a full reply that holds several ciphertext tokens (checked the free-text decryption page, the decryption intro and the home page) **[Not disclosed]**
• Restore side in the deck: the "Anonymised Response" returns from the "Gen AI Magic!" box to the agency product with the placeholder "<hash value 1>" still in it (USENIX PEPR 2023 slides, slide 22, layout read from the rendered slide) **[Documented]**
• Restore side in the deck: the slide does not say where or how placeholders are restored from the mapping table (checked slide 22 and the text of all 32 slides) **[Not disclosed]**
• Release note v2.0.1, 4 December 2023, lists "[API] Reconstruct endpoint for FTA API"; what it does is not described (checked the release notes, the public API guide page and the Replace (Unique) page) **[Not disclosed]**
• Direction: no input or output flag was found on the encrypt, decryption or API guide pages or the portal pages (searched for direction, inbound, outbound, input type, response); the API schema is behind login **[Not disclosed]**
• Anonymise side acts on the text going to a model and restore side on text coming back; both take a string (premise: the Encrypt page says the key is needed "for both encryption and decryption", and the deck slide shows the response returning with placeholders) **[Inferred]**
• A model reply must keep a base64 token intact for restore to work, since the Web UI decrypts one pasted value exactly (premise: Encrypt output is base64 and decrypt takes the whole value) **[Inferred]**
• No system or user prompt is needed as context (premise: the documented inputs are the text, the entity settings and the secret) **[Inferred]**
### R4
Summary: **AES-256 CBC encryption under a managed secret.** Encrypt output is base64. The Secrets Manager shares keys and salts without showing key material, and logs their use. Pseudonymise uses SHA-256 or SHA-512 with a salt. Hosting is Government Commercial Cloud. **[Documented]**
Detail:
• Cipher: "The encryption uses AES cypher in CBC mode"; "AES-256 Encryption is recommended. The output would be in base64." (Encrypt page) **[Documented]**
• Mode restriction: "Due to security reasons, we have restricted encryption to only AES-256 CBC Mode Encryption." (Encrypt page) **[Documented]**
• Example row on the page: original "Jason" becomes "pX09dIQ4X3gU1FC3r8pZXA==" (Encrypt page) **[Documented]**
• That example decodes to 16 bytes, one AES block, so the token seems to carry no separate initialisation vector, which the Secrets Manager holds with the key (premise: base64 arithmetic and the Secrets Manager text "secret key and IV value") **[Inferred]**
• Key sharing: "Members of shared secrets will not be able to view or access the secret key and IV value, but will be able to use it to decrypt data." (Cloak Guide, Secrets Manager page) **[Documented]**
• Key and salt protection: "Keys and salts are stored securely and never exposed to shared users" (Cloak Guide, Secrets Manager page) **[Documented]**
• Sharing limits: "up to 10 other users per operation, and with a maximum of 50 users per secret" (Secrets Manager page) **[Documented]**
• Audit: the audit view shows "the member's email, time of usage and activity type"; one activity is "Decrypt Free Text: Users decrypts a singular encrypted value" (Secrets Manager page) **[Documented]**
• Storage: "Salts and Secret Keys within Cloak are stored in encrypted format, and usage of salts/secret keys are audited." (Cloak Guide, FAQs) **[Documented]**
• Transport and rest: "All data is encrypted in transit and at rest." (www.cloak.gov.sg FAQ, read 2026-10-10) **[Documented]**
• Pseudonymise: SHA-256 or SHA-512 "with a random salt"; the same salt gives the same pseudonym (Pseudonymisation page) **[Documented]**
• Salts, page text: "Custom salt values will be included in the future." (Pseudonymisation page); the release notes list a salt parameter in v2.1.0 and custom salts in v2.1.4 **[Documented]**
• Salts, release notes: v2.1.0, 19 March 2024, "[FTA] Added salt parameter for Pseudonymisation transformation" and v2.1.4, 4 June 2024, "[FTA] Support for custom salts and user managed salts" (Cloak Guide, release notes) **[Documented]**
• Decryption release: v2.1.0, 19 March 2024: "[Decryption] Decrypt encrypted free-text or tabular data using secret keys." (release notes) **[Documented]**
• Techstack: "AWS GCC 2.0" (developer portal, Features and Roadmap, last updated 21 Aug 2026) **[Documented]**
• Hosting: "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment" (Cloak Guide, key FAQs) **[Documented]**
• Encrypt page: "Microsoft Presidio has a built-in encryption functionality, to encrypt and decrypt identified entities." (Cloak Guide, Encrypt page) **[Documented]**
• The Encrypt page's link to microsoft.github.io/presidio/tutorial/12_encryption/ returned HTTP 404 on 2026-10-10 **[Documented]**
• Whether Cloak's Encrypt is Presidio's encrypt operator is not stated by any GovTech page; the Encrypt page's wording and AES-CBC point that way (premise: the Encrypt page text above; see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) **[Inferred]**
• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) **[Documented]**
• The deployed version (checked the release notes page in full, the home page and the portal pages; not stated) **[Not disclosed]**
• Closed hosted service: no public repo, model or package was found (GitHub repository search for "cloak" in the GovTechSG, opengovsg, govtech-responsibleai and datagovsg orgs returned 0 results on 2026-10-10) **[Not disclosed]**
• The offline package covers only tabular features, so free-text encrypt and decrypt have no offline route (premise: package page text) **[Inferred]**
### R5
Summary: **Ciphertext out, original value back.** Encrypt replaces each entity with a base64 string, and the Web UI shows the decrypted value for a pasted token. The 2023 deck's API also returned a mapping table. **[Documented]**
Detail:
• Anonymise side output: the Encrypt page example shows "Jason" as "pX09dIQ4X3gU1FC3r8pZXA==" under a secret key (Encrypt page) **[Documented]**
• Anonymise side review: the Findings table lists "each detected entity with its type, transformation applied, original text, anonymised text, and confidence score" (usage guide caption) **[Documented]**
• Anonymise side delivery: "An email containing the password required to unzip the folder will be sent to you." (usage guide) **[Documented]**
• Restore side output: "after selecting your secret, you can then obtain the decrypted value." (free-text decryption page) **[Documented]**
• Restore side audit: the Secrets Manager logs "Decrypt Free Text" for each singular decrypted value (Secrets Manager page) **[Documented]**
• 2023 deck: "API: Takes in unstructured text, returns mapping table and anonymized result." (USENIX PEPR 2023 slides, slide 22, 11 Sep 2023) **[Documented]**
• Repeatability: the vendor says owners using one shared secret produce data "that can still be linked on a common encrypted identifier" (portal Use Cases page), which needs the same value to give the same ciphertext under one secret (premise: linkage on the encrypted value) **[Inferred]**
• Free-text failure output for a wrong secret or damaged token (checked the free-text decryption page and Secrets Manager page) **[Not disclosed]**
• Tabular decryption, for contrast: "a separate csv file named "failed_cells.csv" will be provided" for values that failed to decrypt (Cloak Guide, tabular decryption page; tabular is outside this column) **[Documented]**
• Round-trip accuracy or failure rate (checked the home, overview and FAQ pages, the Encrypt and decryption pages and the 2023 deck) **[Not disclosed]**
• API response format for encrypt and decrypt (the API guide and OpenAPI pages redirect to login, HTTP 302 then a 200 login page at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in, observed 2026-10-10) **[Not disclosed]**
### R6
Summary: **A secret, plus a ciphertext to restore.** Encrypting needs a key made or chosen in the Secrets Manager; Pseudonymise needs a salt. Decrypting needs the encrypted value and access to the same secret, as owner or shared member. **[Documented]**
Detail:
• Anonymise side key: the Encrypt page example lists a "Secret Key" beside each value, and the text says a "cryptographic key" is required (Encrypt page) **[Documented]**
• Anonymise side secret: "creating your first secret to encrypt data with, you are also able to simultaneously share the created secret with other valid (active and verified) Cloak users." (Secrets Manager page) **[Documented]**
• Anonymise side release: v2.1.4, 4 June 2024, "[FTA] Allow for user managed secret keys" (release notes) **[Documented]**
• Key rules: whether the user types the key or Cloak generates it, key length rules and rotation (checked the Secrets Manager page, whose figures are captions only, and the release notes) **[Not disclosed]**
• Anonymise side salt: "Store your salt in the Secrets Manager and share it with colleagues. Using the same salt across jobs ensures the same input always produces the same pseudonym" (Pseudonymisation page) **[Documented]**
• Restore side inputs: the encrypted value, then "choose which secret to use when decrypting" (free-text decryption page, steps 1 and 2) **[Documented]**
• Restore side API: a helper script for "looping through rows in a CSV"; its parameters are not public (the page is behind login) **[Not disclosed]**
• Who can restore: secret owners and members with whom the secret is shared; sharing is up to 10 users per operation and 50 per secret (Secrets Manager page) **[Documented]**
• Sharing a secret needs another "valid (active and verified) Cloak user", so a sharing test needs a second approved account (premise: Secrets Manager page) **[Inferred]**
• Pasted text up to 20,000 characters; CSV 500 MB, PDF and DOCX 200 MB per file; 100 files and 2 GB per project (usage guide) **[Documented]**
• Data ceiling: "up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)" (Cloak Guide, FAQs); Terms Schedule 4.6 gives the same ceiling (Terms of Use dated 24 July 2024) **[Documented]**
• Access: Web UI for WOG users via WOG-AD and approved non-WOG users; API key "within 1-2 business days" after the onboarding request (FAQs) **[Documented]**
• Maintenance: "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period." (www.cloak.gov.sg banner, read 2026-10-10) **[Documented]**
### R7
Summary: **Minimum setup:** documentation only today; a trial needs an approved Cloak account, and a sharing test needs a second user. A bench could encrypt made-up values, decrypt them with the same secret, then try a changed token, a wrong secret and a mock model reply. **[Inferred]**
Detail:
• **Minimum setup:** the public pages are documentation only; a suggested first step is a Web UI project that encrypts synthetic entities under one new secret, then decrypts each ciphertext one at a time with that secret **[Inferred]**
• Access to try it: Web UI needs WOG-AD or a TechPass account approved by Cloak Ops; the API needs the Onboarding Form and a key; non-public-sector use needs GovTech's written consent to a stated purpose (Terms clause 3.3) (Cloak Guide, registration guide and FAQs; Terms PDF) **[Documented]**
• Terms clause 3.4 lists "perform any benchmarking tests or analyses of the Service" (3.4.7), "transfer assign or permit the sharing of license keys to or with a third party" (3.4.9) and "provide third party access to the Service" (3.4.11) among the things the user shall not do, so a bench could first seek GovTech's written view **[Inferred]**
• Possible round trip: made-up names and IDs, encrypt, decrypt, and compare with the originals across lengths and non-ASCII names **[Inferred]**
• Possible checks: the same value twice in one text and across two jobs under the same secret, and under a different secret **[Inferred]**
• Possible failure cases: a changed or truncated token, a wrong secret, a secret not shared with the user, and a mock model reply that edits or drops the token **[Inferred]**
• Possible LLM step: use a harmless local model reply to see whether base64 tokens survive, and note token cost; no real model call is needed for the first pass **[Inferred]**
• Possible comparison source: Presidio's encrypt and decrypt as a clearly labelled stand-in, never reported as Cloak (see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) **[Inferred]**
### R8
Summary: **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, how a whole model reply with several tokens is restored, what the Reconstruct endpoint does, key length and IV handling, and failure behaviour for a wrong secret.
Detail:
• Terms clause 3.4 says "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 reads "perform any benchmarking tests or analyses of the Service;" (Terms of Use dated 24 July 2024). Whether a comparison bench falls under it is not stated (the Terms define no benchmarking term; checked all 15 pages); decided before any bench run
• Terms 3.4.9 reads "transfer assign or permit the sharing of license keys to or with a third party;" and 3.4.11 reads "provide third party access to the Service"; whether secret sharing between test accounts is affected is not stated (the Terms do not define "license keys"; the Cloak guide describes sharing secrets among Cloak users)
• Terms 3.3 limits non-public-sector use to "such purpose that GovTech has consented to in writing (including via email)"; Schedule 2.2 reads "You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency."
• Whether one API call or Web UI action can restore a full text that holds several tokens (the Web UI decrypts one value at a time)
• What the "Reconstruct endpoint for FTA API" (v2.0.1) does and whether it restores text from a mapping table as in the 2023 deck (checked the release notes, public API guide page and Replace (Unique) page)
• Whether the 2023 deck's mapping-table design is still how the free-text API works (the deck is dated 11 Sep 2023)
• Key length and format, whether Cloak generates keys, how the IV is stored and used, and whether the same value always gives the same ciphertext (checked the Encrypt and Secrets Manager pages)
• Behaviour for a wrong secret, a damaged token or a secret the user cannot access in free-text decryption (the pages show no error handling)
• Whether Replace, Redact, Mask or Alias can be reversed with any Cloak feature (the technique pages are silent)
• Whether Cloak's Encrypt is the Presidio encrypt operator (the Encrypt page links Presidio, and the link is HTTP 404)
• Salt conflict: the Pseudonymisation page still says custom salts are future, while the release notes list custom salts in v2.1.4; which is current needs the live Web UI
• Whether a real model keeps base64 tokens intact, and what they cost in model tokens (needs testing)
• Latency for a short encrypt or decrypt call and any API rate limits (not stated)
• Roadmap line "Incorporation of other privacy technologies, e.g., Homomorphic Encryption and Searchable Symmetric Encryption" is planned, not available (developer portal, Features and Roadmap)
### R9
Summary: Cloak Guide pages (docsify Markdown), the www.cloak.gov.sg home page, GovTech developer portal pages, the Cloak Terms of Use PDF, and the GovTech USENIX PEPR 2023 slides.
Detail:
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/encrypt.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/pseudonymisation.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace-unique.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/intro-to-decryption.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/free-text-decryption.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/secrets-manager.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/tabular-decryption.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/registration-guide.md
• https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/packages-anonymiser.md
• https://docs.developer.tech.gov.sg/docs/cloak-api-guide/
• https://www.cloak.gov.sg
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap
• https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/use-cases
• https://file.go.gov.sg/cloak-terms.pdf
• https://www.usenix.org/system/files/pepr23_slides-tang.pdf
