## Column CK1: Cloak: Free-text PII detection and anonymisation
### R1
Summary: **Finds personal data in text and rewrites it.** Cloak's free-text tool detects entities such as names, NRICs and addresses in pasted text or uploaded files, then replaces, redacts, masks, aliases, hashes or encrypts them. The result is rewritten text or a file. **[Documented]**
Detail:
• Cloak is GovTech's whole-of-government anonymisation service: "Cloak offers tabular and free-text anonymisation to enable agencies to anonymise data safely before data sharing and utilisation." (Cloak Guide, home page, read 2026-10-10) **[Documented]**
• Free-text anonymisation (FTA) "automatically detects and redacts/transforms sensitive information within unstructured text" (Cloak Guide, intro to FTA) **[Documented]**
• By default "Cloak scans your text for all available Entity Types and Replaces them with their data type", and the user can toggle each entity type and choose a technique per type (Cloak Guide, usage guide) **[Documented]**
• Techniques named in the guide: Replace, Replace (Unique), Redact, Mask, Alias, Pseudonymise and Encrypt (Cloak Guide, anonymisation techniques pages) **[Documented]**
• The vendor names a use on AI traffic: "Anonymise before sending to LLMs | Strip PII in real-time via API before data reaches external LLMs or other WOG products" (Cloak Guide, home page) **[Documented]**
• Portal use case: "Agencies integrate Cloak via API into chatbot services and WOG AI platforms to strip PII from user prompts in real-time before they reach external LLMs." (Developer Portal, use cases, last updated 21 Aug 2026) **[Documented]**
• FAQ: anonymising before sending data to GenAI "is a common use pattern, provided anonymisation happens before the data leaves the approved environment and the output is validated" (Cloak Guide, key FAQs) **[Documented]**
• The documented output is transformed text or files (text, .csv, .docx formats in the FAQ file-format table); no safe or unsafe verdict, risk label or content classification is described (checked the FTA guide pages, FAQs, home page and portal pages; not stated) **[Not disclosed]**
• Custom entities (CK2 mechanisms) are a separate function: the FTA caption says Cloak also handles "custom entities defined via pattern matching, inclusion lists, or privately-hosted LLMs" (Cloak Guide, intro to FTA) **[Documented]**
• Cloak also has a tabular anonymisation tool and a Secrets Manager; they are separate tools from free-text anonymisation (Cloak Guide, home page) **[Documented]**
### R2
Summary: **Personal data in free text, tuned for Singapore.** Seventeen entity groups cover names, NRICs, phone numbers, emails, addresses, banking, dates and more. Scanned documents and images are not processed, and detection is probabilistic. **[Documented]**
Detail:
• The Entity Types page lists 17 groups: Name, NRIC (SG), Email Address, Phone Number, Nationality/Race/Religion, Address (SG), Location, Passport (SG), Currency, Credit Card, Bank Account Number (SG), Bank Account Number (IBAN), IP Address, URL, Date & Time, UEN (SG), Organization, plus Exceptions and Custom (Cloak Guide, entity types intro) **[Documented]**
• The Address page says "Cloak provides 4 address-related recognisers for Singapore addresses": SG_ADDRESS, SG_ADDRESS_POSTAL_CODE and SG_ADDRESS_UNIT_NUMBER are on by default and SG_ADDRESS_STREET is "OFF (advanced)" (Cloak Guide, Address page) **[Documented]**
• Counting one tag per group plus the 4 address tags gives 20 baseline tags (PERSON, SG_NRIC_FIN, EMAIL_ADDRESS, PHONE_NUMBER, NRP, 4 address tags, LOCATION, SG_PASSPORT, CURRENCY, CREDIT_CARD, SG_BANK_ACCOUNT_NUMBER, IBAN_CODE, IP_ADDRESS, URL, DATE_TIME, SG_UEN, ORGANIZATION); the count is a tally of the entity pages, not a vendor figure **[Inferred]**
• Vendor count, version one: "Cloak detects and transforms 20+ baseline entity types" (Cloak Guide, intro to FTA; Developer Portal, features page, "Auto-detection of 20+ entity types") **[Documented]**
• Vendor count, version two: "Cloak detects 17+ entity types out of the box" (Developer Portal, FAQs, last updated 21 Aug 2026); the two counts conflict in wording, and the entity pages give 17 groups and 20 tags **[Documented]**
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
• The API Guide and OpenAPI pages redirect to the docs login page: https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ and https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/ both end at "auth/otp-login" with redirect_reason=not_logged_in (HTTP 200 after redirect, observed 2026-10-10) **[Documented]**
• The tool works on whatever string or file reaches it, so it would apply to prompts, responses, retrieved text and tool output; premise: text and files in, the vendor's LLM use case, and no direction flag found **[Inferred]**
• No system prompt, user prompt or conversation history is a documented input; the usage guide shows only text or files plus anonymisation settings (checked the usage guide and FTA pages; API schema not readable) **[Inferred]**
• Playbook, PII protection page, "Where PII can appear": "User prompts.", "Model outputs.", "Retrieved documents.", "Tool arguments and tool results." (a bulleted list); the page lists Cloak under "Detection tools" **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• 2023 GovTech deck, GenAI workflow slide: the original prompt goes through "Detect PII" and "Anonymise PII" before the GenAI product, so the anonymise step acts on the prompt side (USENIX PEPR 2023 deck, slide 22; dated September 2023) **[Documented]**
• The same deck slide shows an "Anonymised Response" returning through a "Transformer Module" (restore side of reversible anonymisation, a CK3 mechanism) (USENIX PEPR 2023 deck, slide 22) **[Documented]**
### R4
Summary: **Named techniques, model not named.** Entities are found by an AI model (spaCy given as an example) plus regex, rule-based matching and checksums, hosted on GovTech's cloud. Reached by web UI or API. **[Documented]**
Detail:
• "Entity types are identified either by the underlying AI Model (e.g. spaCy), and a combination of: Regex Patterning … Rule-based Matching … Validation using checksums (if applicable)" (Cloak Guide, entity types intro) **[Documented]**
• The same page links its spaCy example to spaCy's en_core_web_sm model page (Cloak Guide, entity types intro) **[Documented]**
• Which model Cloak runs, its version, any fine-tuning, and which entity uses the model versus rules (checked the entity pages, FAQs, credits, release notes, portal pages and the 2023 deck; not stated) **[Not disclosed]**
• Address entities list their method: SG_ADDRESS "Pattern matching", SG_ADDRESS_POSTAL_CODE "Regex", SG_ADDRESS_UNIT_NUMBER "Regex", SG_ADDRESS_STREET "Pattern matching" (Cloak Guide, Address page) **[Documented]**
• Scoring: Confidence Level "denotes the level of certainty / probability that a particular entity type is accurately detected by the algorithm" (Cloak Guide, confidence level page) **[Documented]**
• Hosting: "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment"; the portal tech stack lists "AWS GCC 2.0" (Cloak Guide, key FAQs; Developer Portal, features page) **[Documented]**
• Routes: Web UI, and API at L2 (Analytics.gov), L3 (GCC) and L4 (internet); a Python package exists but is "Tabular only; provided as-is with no active maintenance" (Cloak Guide, home page) **[Documented]**
• No self-hosting route for free-text anonymisation is documented: no repository, Hugging Face entry or free-text package turned up (checked the Cloak Guide, cloak.gov.sg, the portal, and GitHub searches of GovTechSG, govtech-responsibleai and opengovsg on 2026-10-10) **[Not disclosed]**
• LLM-enabled custom entity (CK2 mechanism, Beta): "Cloak privately hosts a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS. No data is sent to external parties" (Cloak Guide, unstructured custom entities intro) **[Documented]**
• Encrypt technique (CK3 mechanism): "The encryption uses AES cypher in CBC mode"; "we have restricted encryption to only AES-256 CBC Mode Encryption" (Cloak Guide, Encrypt page) **[Documented]**
• Release notes: the newest entry is v2.2.2 (4 August 2024); v2.1.0 added the ORGANIZATION entity and FTA templates, and v2.0.1 added Word support (Cloak Guide, release notes) **[Documented]**
• The deployed version, and when later documented features shipped (Replace (Unique), the SG_ADDRESS recognisers, LLM entities; none is in the release notes) (checked release notes, home page, portal pages; not stated) **[Not disclosed]**
• The Encrypt page says "Microsoft Presidio has a built-in encryption functionality" and the entity types page links Presidio's supported-entities page (Cloak Guide, Encrypt page and entity types intro) **[Documented]**
• No GovTech page says Cloak is built on Presidio (checked the Cloak Guide, credits page, portal and cloak.gov.sg; the credits list neither Presidio nor spaCy) **[Not disclosed]**
• Cloak shares tag names such as PERSON, EMAIL_ADDRESS, PHONE_NUMBER, CREDIT_CARD, IBAN_CODE, IP_ADDRESS, URL, DATE_TIME, LOCATION, NRP and SG_UEN with Presidio's catalogue, which could mean reuse of Presidio recognisers; see Presidio: PII detection in text (Analyzer) and Presidio: PII anonymisation and masking in text (Anonymizer); no Presidio fact is restated here **[Inferred]**
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
• Whether the confidence setting is global or per entity: the Developer Portal Features page says "Adjust detection sensitivity per entity type", while the guide shows one "Adjust Confidence level" slider (Developer Portal, features page; Cloak Guide, confidence level page) **[Documented]**
• Accuracy claim: ">97% recall for key PIIs like Name, NRIC and Email" (Cloak Guide, home page; Developer Portal, overview page); a vendor claim with no method, dataset or precision figure **[Documented]**
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
• Inclusion list on an existing entity: words or a CSV of "up to 500 entries"; "Word-sensitive", "Not case-sensitive", "Only the first 500 words in a CSV upload will be used" (Cloak Guide, inclusion feature page) **[Documented]**
• Mask defaults: 3 characters, type Suffix, character "-"; Alias applies to the PERSON entity only, with Context and Offset options both On (Cloak Guide, masking and Alias pages) **[Documented]**
• Pseudonymise uses "irreversible hashing (SHA-256) or (SHA-512) with a random salt" (Cloak Guide, Pseudonymisation page) **[Documented]**
• Replace (Unique) limits: available "On the Cloak Web App; For single CSV uploads; and For Cloak's baseline entities", not for PDF, DOCX, multi-file uploads or custom entities, and "up to two entity types per anonymisation job" (Cloak Guide, Replace (Unique) page) **[Documented]**
• Whether Replace (Unique) works on pasted text (the page lists CSV only as available and does not name pasted text in either list) **[Not disclosed]**
• Encrypt needs a secret key (an AES-256 key); the page shows an example key beside the transformed value (CK3 mechanism, Encrypt with a shared secret) (Cloak Guide, Encrypt page) **[Documented]**
• Templates: a free-text template stores "Entity types, anonymisation techniques, parameters, and score threshold"; free-text templates are personal and cannot be shared (Cloak Guide, templates page) **[Documented]**
• The FAQ names three tuning controls: Enhanced Detection for names, checksum validation for NRIC and UEN, and global detection for phone numbers; the pages read do not show where these are switched on (Cloak Guide, key FAQs) **[Documented]**
• API: security levels L2 (personalised token), L3 (system token), L4 (signature-based); an API key per level; "complete our Cloak (API) Onboarding Form" and a key follows "within 1-2 business days" (Cloak Guide, API guide and key FAQs) **[Documented]**
• API parameters: the release notes name an "allow_list" parameter (v2.0.5); the API guide names custom recognisers, "fine-grained confidence score tuning" and the allow list; request fields, headers and limits (checked the API guide, FAQs, release notes, portal pages; schema behind a login) **[Not disclosed]**
• Regex custom entity, API only (CK2 mechanism): "Define custom context words that must appear near a regex match" and "Set different confidence scores for each regex pattern" (Cloak Guide, structured custom entities page) **[Documented]**
• Web UI access: WOG users sign in with WOG-AD; other approved users register (vendors complete TechPass onboarding after Cloak Ops approval); non-government entities need pre-approval of purpose (Cloak Guide, key FAQs and registration guide) **[Documented]**
• Data ceiling: "You shall not upload any information, data and material that are classified above the following classifications: Confidential (Cloud-Eligible) \ Sensitive (High)" (Terms of Use, Schedule clause 4.6, dated 24 July 2024, read with pypdf) **[Documented]**
• Retention: "Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request." (Cloak Guide, key FAQs) **[Documented]**
• cloak.gov.sg banner: "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period." (cloak.gov.sg home page, observed 2026-10-10) **[Documented]**
• Cost: "Cloak is currently free for all approved users"; "For FY26, there is no charge." (Cloak Guide, home page) **[Documented]**
### R7
Summary: **Minimum setup:** Cloak has no public code or package, so a bench would need approved Web UI or API access. A bench could send short synthetic Singapore-style prompts with planted names, NRICs, addresses and phone numbers, and compare each output with the expected tags. Terms clause 3.4.7 mentions benchmarking, an open licensing question. **[Inferred]**
Detail:
• **Minimum setup:** the public pages are documentation only, so a bench could not run Cloak without an approved account or API key; a first trial would be the Web UI with a short synthetic text, or an API key after the onboarding form (access routes as in R6) **[Inferred]**
• Access conditions: a Web UI account needs WOG-AD or TechPass registration; non-public-sector use is "restricted solely for such purpose that GovTech has consented to in writing (including via email)" (Terms of Use, clause 3.3) **[Documented]**
• Terms of Use, clause 3.4 and 3.4.7: "You shall not, and shall not authorise or permit any third party to … perform any benchmarking tests or analyses of the Service" **[Documented]**
• Terms of Use, Schedule clause 2.2: "You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency." **[Documented]**
• Terms of Use, clauses 3.4.9 and 3.4.11: no transfer or sharing of "license keys" and no "third party access to the Service" (read with pypdf, dated 24 July 2024) **[Documented]**
• Possible test inputs for a bench: short synthetic prompts with known planted entities, namely names of Malay, Indian and Chinese structure, NRIC-shaped numbers, Singapore addresses with postal codes and unit numbers, phone numbers, emails and UENs **[Inferred]**
• A bench could add near-miss strings, such as NRIC-shaped numbers that fail the checksum, 9-digit numbers that are not phone numbers, and street names that are also common words, to see what the default detection does with them **[Inferred]**
• A bench could check the 20,000-character limit, compare the default Confidence Level of 0.30 with higher and lower settings, and compare Replace with Replace (Unique) on a single CSV **[Inferred]**
• Possible comparator: Presidio with Singapore recognisers as a clearly labelled stand-in, never reported as Cloak (see Presidio: PII detection in text (Analyzer)) **[Inferred]**
• No access was requested and nothing was run or called during this research; data used in any test is limited by the Terms to Confidential (Cloud-Eligible) and Sensitive (High) classifications, and the choice of test data is left to bench design **[Inferred]**
### R8
Summary: **Key open questions.** Whether Terms clause 3.4.7 allows benchmarking, the API schema and any direction flag, the model and version, accuracy beyond the recall claim, language coverage, short-prompt latency, and the Sentinel integration.
Detail:
• Does Terms clause 3.4.7 ("perform any benchmarking tests or analyses of the Service") bar a bench comparison, and would GovTech's written consent under clause 3.3 cover it? (clauses read as written; needs GovTech's answer before any bench run)
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

## Reviewer notes
1. **Scope and headers.** Only CK1 is in this file (half A). Header text is the brief's CK1 header with no change; main's rulings changed CK2 and CK3 headers only. Inventory covered-by for Inclusion lists is CK2 in the brief block (c) but CK1's "what it covers" text includes per-entity Inclusion lists; the Inclusion bullet in R6 is kept here, and the merger may move it if CK2 also carries it.
2. **CK2 and CK3 facts kept as own bullets** (mechanism named in the bullet): R1 custom entities caption; R3 deck "Anonymised Response" restore side; R4 LLM-enabled custom entity hosting and Encrypt AES-256 CBC; R6 Encrypt secret key and regex custom entity API-only settings. If CP1 chooses option (b), these fold in unchanged; if (c), the column is not merged.
3. **Conflicts.** C1: "20+" (FTA intro, Features page) versus "17+" (portal FAQs) given as two bullets; entity pages give 17 groups, 20 tags (drafter tally, Inferred). C2: dates of birth and vehicle plate numbers on portal pages only. C3: the playbook says "GovTech's dedicated internal service" while the docs say open to select non-government entities; not drafted in CK1 because it is an access fact (inventory block (b) and R6 carry the access route). C4 (salt text) belongs to CK3. C5 (MDG) is inventory only. C6: release notes list v2.2.2 (4 August 2024) above v2.2.1 (28 August 2024); R4 cites v2.2.2 as the newest by version number. C7: older CSV limits (v2.0.3) not used; the current usage guide is authoritative. C8: the Encrypt page links a Presidio tutorial URL that the brief says returned 404 on 2026-10-10; not re-requested here, and the entity types page link is the one cited. C9: the FAQ links https://www.cloak.gov.sg/terms (HTTP 404 per the brief); the live Terms are the go.gov.sg PDF, cited here.
4. **Confidence level.** The 0 to 1 range and the 0.30 default rest on image captions, not body text; flagged in the R5 bullet. The portal "per entity type" wording versus a single slider is kept as one [Documented] bullet with both sides named plus an R8 item, because both are quoted as written.
5. **Count of 20 tags** is the drafter's own tally and appears only in an Inferred Detail bullet; the R2 Summary uses the Documented 17 groups.
6. **R3 Summary label is Inferred** because the Summary draws on the Inferred direction and context bullets.
7. **Pages not reachable:** API Guide (cloak-api-guide), OpenAPI spec (cloak-api-specifications-openapi) redirect to the login page (HTTP 200 after redirect to auth/otp-login, observed 2026-10-10); also the "Replace (Unique) via API" page under cloak-api-guide, linked from the Replace (Unique) page, redirects the same way. The package guide was not requested again. The Developer Portal getting-started page returned HTTP 502 on the first fetch and 200 on a retry; it was not needed for CK1 and is not cited.
8. **Sources read as text:** Cloak Guide Markdown by curl (raw `.md`), portal and cloak.gov.sg by fetch_text.py (verbatim text), the Terms PDF and the 2023 deck by pypdf (page text; slide 22 wording is from the text layer, with the layout order of labels not guaranteed), the playbook page via the raw GitHub URL at the full SHA 45908b48c0a8b6d3855a154c0e41a12958a99205 (cited as the blob URL). No fact came from a summarising fetch.
9. **Not used:** the Privacy Statement (dated 1 December 2022), Terms clauses 6.1 and 4.2 (data licence and routine deletion), which are service-wide facts for the inventory; Terms clauses 3.4.6 and 3.4.10 and 3.7, which the brief lists for inventory block (e).
10. **Brief corrections checked at source:** Terms 3.4.7 and Schedule 4.6 and 2.2 matched; Replace (Unique) limits matched; the API pages are named only by the release notes ("Reconstruct endpoint", CK3) and the Replace (Unique) page ("/analyze", not cited because it is a code identifier and API-only).
