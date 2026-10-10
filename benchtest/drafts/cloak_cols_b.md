# Cloak column drafts, half B (CK2 and CK3), P2, 2026-10-10

Headers follow main's tweaks (queue.md, 2026-10-10): CK2 and CK3 as below. Cloak Guide pages were read as docsify Markdown (curl, HTTP 200) on 2026-10-10; portal, cloak.gov.sg and playbook pages with `fetch_text.py`; Terms PDF and the USENIX deck with pypdf.

## Column CK2: Cloak: Custom entity detection in free text (lists, regex and LLM)
### R1
Summary: **Adds your own entity types to free-text anonymisation.** A custom entity can be a fixed word list, a regex pattern or, in Beta, an LLM given a definition and examples. Matches are then transformed like the built-in entities. **[Documented]**
Detail:
• Home page: "Customisable - add any custom entity using inclusion lists, pattern-matching (regex), or privately-hosted LLMs" (Cloak Guide, home page, read 2026-10-10) **[Documented]**
• Custom entity page: "If no entity type matches the data you are trying to anonymise, you may add a Custom Entity. This function is similar to the "Find and Replace" feature offered on some text editors" (Cloak Guide, entity types, Custom) **[Documented]**
• Fixed list route: "If you have a known, finite list of words or phrases to detect (e.g. hospital names, school names, or organisation acronyms), you can use the Inclusion Feature together with a Custom Entity to anonymise them." (Cloak Guide, fixed-list page) **[Documented]**
• Regex route: "Custom Entities are used to define entities with structured data patterns specific to your needs." (Cloak Guide, structured page) **[Documented]**
• LLM route: "Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning." (Cloak Guide, unstructured intro) **[Documented]**
• Inclusion list on a built-in entity is a related control, not a new entity: "specify additional words or phrases that should be detected and anonymised under an existing entity type" (Cloak Guide, Inclusion Feature page) **[Documented]**
• The result is transformed text: "Click Start anonymisation. Your text is now transformed with the new custom entity applied." (fixed-list page) **[Documented]**
• Cloak's home page describes the LLM entity as: "Define custom sensitive entities using LLM-powered detection — add organisation-specific terms or domain-specific identifiers without re-training a model" (www.cloak.gov.sg home page) **[Documented]**
• GovTech's playbook says: "Cloak also offers LLM-enabled custom entity detection to protect custom, domain-specific or localised entities unique to your use case." (Responsible AI playbook, privacy improvements page) **[Documented: repo govtech-responsibleai/playbook@45908b48]**
• Exceptions is the opposite control, "used to manually exclude words from being detected and anonymised"; it is covered in the column Cloak: Free-text PII detection and anonymisation (Cloak Guide, Exceptions page) **[Documented]**
• No page describes a safe or unsafe verdict or score for a custom entity; the documented result is transformed text and a Findings table (premise: the custom entity pages and the FTA usage guide show only transformed output) **[Inferred]**
### R2
Summary: **Domain terms the built-in entities miss.** Documented examples are hospital names, car licence numbers, unusual date formats, usernames and disease names. Free-text detection is probabilistic, so full recall should not be assumed. **[Documented]**
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
• The Web UI returns a download, not an inline reply: "click on Download to proceed with the download request" (usage guide) **[Documented]**
• Vendor use on AI traffic: "Strip PII in real-time via API before data reaches external LLMs or other WOG products" (Cloak Guide, home page, use cases table) **[Documented]**
• Prompts, responses, retrieved text and tool output can all be sent as a string or file, so a custom entity applies to each (premise: string or file input and the vendor's LLM use case above) **[Inferred]**
• Direction (R002): no input or output flag, role or setting appears on the custom entity pages, the FTA usage guide, the public API guide page or the portal pages (searched for direction, inbound, outbound, input type, response); the API schema is behind login **[Not disclosed]**
• Real-time path: whether an LLM-enabled entity runs on the real-time API path is not stated; the public API guide names only "custom recognisers (regex patterns, context words)" (checked the API guide page, FAQs and portal pages) **[Not disclosed]**
• LLM entity timing: "Including an LLM-enabled custom entity may increase processing times to up to 8 hours." (unstructured intro) **[Documented]**
• Quick iteration: "Test your definition and examples using Cloak's transformation preview or run a job on a smaller dataset (e.g., <100 documents, which should take <20min)." (write-prompts page) **[Documented]**
• Preview limits: "CSV preview shows first cell only", "PDF preview shows first page only", "Word preview shows first 200 words only" (usage guide) **[Documented]**
• Context needed: the documented inputs are the entity name, a list, pattern or definition with examples, and the text; no page describes use of a system prompt or conversation history (premise: the custom entity pages list no such input) **[Inferred]**
### R4
Summary: **Three mechanisms: list, regex and few-shot LLM.** Lists match exact words, regex matches patterns, and the Beta LLM entity learns from 3 to 5 examples on a privately hosted model on Government Commercial Cloud. **[Documented]**
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
• LLM status and limit: "[Beta Feature] Currently, only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)." (unstructured intro) **[Documented]**
• LLM roadmap wording: "We're working to expand support to larger datasets, multiple entities, and shorter processing times." (unstructured intro) **[Documented]**
• Web UI limit per project: "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time." (Cloak Guide, FAQs) **[Documented]**
• Language model name, size, version and prompt template (checked the unstructured intro, add-entities, write-prompts and three sample pages, FAQs, home page, portal pages, release notes, credits page, the 2023 GovTech deck and the playbook) **[Not disclosed]**
• Release history: the newest release note is v2.2.2 (4 August 2024) and none names the LLM entity, so the deployed version and the LLM entity's release date are not given (checked the release notes page in full) **[Not disclosed]**
• API route: the API offers "custom recognisers (regex patterns, context words), fine-grained confidence score tuning, or the allow list feature via code" (Cloak Guide, API guide) **[Documented]**
• Portal roadmap lists "Improve performance of free-text anonymisation through novel LLM-based approaches" as a roadmap item, not a current feature (developer portal, Features and Roadmap, last updated 21 Aug 2026) **[Documented]**
• Techstack: "AWS GCC 2.0" (developer portal, Features and Roadmap) **[Documented]**
• Closed hosted service: no public repo or model was found (GitHub repository search for "cloak" in the GovTechSG, opengovsg, govtech-responsibleai and datagovsg orgs returned 0 results on 2026-10-10; checked the Cloak Guide and portal pages) **[Not disclosed]**
• The offline package covers only "Cloak's tabular anonymisation features", so free-text custom entities have no offline route (premise: package page text) **[Inferred]**
• Cross-reference: Presidio also has regex and word-list custom recognisers, see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); no GovTech page says Cloak's custom entities are Presidio recognisers (premise for any link: the shared terms "custom recognisers" and "context words") **[Inferred]**
### R5
Summary: **Transformed text, not a verdict.** Each custom match is replaced, redacted, masked or otherwise transformed with the technique chosen for that entity, and the Findings table lists type, transformation, original, anonymised text and score. **[Documented]**
Detail:
• Technique per custom entity: "Select your anonymisation technique of choice." (Custom page) **[Documented]**
• Default replacement text: "By default, it would be <ENTITY_NAME>." (Cloak Guide, Replace page) **[Documented]**
• Fixed list result caption: "The anonymisation result with hospital names and acronyms replaced by HOSPITAL tags." (fixed-list page) **[Documented]**
• LLM result caption: "The project page showing the anonymised output with disease names replaced by the DISEASE tag" (add-entities page) **[Documented]**
• Findings table: "The Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score." (usage guide caption) **[Documented]**
• Whether custom entities of each kind appear in the Findings table with a score (checked the usage guide and custom entity pages) **[Not disclosed]**
• Threshold: "Entities below the specified threshold will not be anonymised" and a slider "set to the default value of 0.30" (Cloak Guide, confidence level page, caption) **[Documented]**
• Whether the 0.30 threshold applies to regex, list or LLM entities (checked the confidence level page and custom entity pages) **[Not disclosed]**
• API regex scores: the API lets users "Set different confidence scores for each regex pattern" (structured page, "sign-in required" for the API guide) **[Documented]**
• Vendor example without figures: the base DATE_TIME entity "over-detects by also replacing relative temporal references such as "42-year-old" and "2 hours"" while DATE_TIME_SPECIFIC does not (date-time sample page, image caption) **[Documented]**
• LLM entity completion: the user is notified by email when the job completes (unstructured intro) **[Documented]**
• Download: "An email containing the password required to unzip the folder will be sent to you." (usage guide) **[Documented]**
• Vendor claim ">97% recall for key PIIs like Name, NRIC and Email" covers built-in entities, with no method, data set or precision stated (Cloak Guide, home page) **[Documented]**
• Precision, recall or F1 for list, regex or LLM custom entities (checked the home, overview and FAQ pages, the custom entity pages, the samples and the 2023 deck) **[Not disclosed]**
• API response format for custom entities (the API guide and OpenAPI pages redirect to a login page, HTTP 200 at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in, observed 2026-10-10) **[Not disclosed]**
### R6
Summary: **A list, a regex or examples.** A list takes up to 500 words from a CSV, a regex takes a pattern, and the LLM entity takes a definition with 3 to 5 labelled examples. Context words and per-pattern scores are API only. **[Documented]**
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
• Terms clause 3.4.7 bars "perform any benchmarking tests or analyses of the Service", so a bench could first seek GovTech's written view (a licensing item, not interpreted here) **[Inferred]**
• Possible test text: short synthetic notes with planted terms (made-up hospital names and acronyms, a made-up car licence format, unusual date formats, usernames, disease names with misspellings), using no real personal data (sensitive test data is decided at bench design) **[Inferred]**
• Possible list checks: exact-match behaviour, the hyphen variant that the page says will not match, the case-insensitive variant, and the 500-word cut-off **[Inferred]**
• Possible regex checks: sample patterns from the structured page, then a value that also looks like a built-in entity (such as a 10-digit case number against Bank Account Number) to see which entity wins **[Inferred]**
• Possible LLM checks: 3 to 5 examples, under 100 documents (the page says under 20 minutes), then a wider run, with the Wednesday maintenance window avoided **[Inferred]**
• Possible comparison source: Presidio with custom recognisers as a clearly labelled stand-in, never reported as Cloak (see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers)) **[Inferred]**
• Nothing was run or requested during research; the Web UI, API and API guide were not opened (research is read-only) **[Inferred]**
### R8
Summary: **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, which language model backs the LLM entity, accuracy and languages for custom entities, API support for the LLM entity, and how custom and built-in entities rank when they overlap.
Detail:
• Terms clause 3.4 says "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 reads "perform any benchmarking tests or analyses of the Service;" (Terms of Use dated 24 July 2024, text from the PDF via pypdf). Whether a comparison bench falls under it is a licensing question; not interpreted here and needs GovTech's written position
• Terms clause 3.3 limits non-public-sector use to "such purpose that GovTech has consented to in writing (including via email)"; whether a bench could obtain that consent (agency onboarding is the other route)
• Which language model, size and version serve the LLM entity, and whether the Beta label is still current (checked the Cloak Guide, portal pages, release notes and the 2023 deck; the newest release note is v2.2.2 of August 2024)
• Accuracy for list, regex and LLM entities: no figure is published (checked the custom entity pages, samples, home, overview, FAQs and the 2023 deck); needs testing
• Languages and scripts supported by the LLM entity and by regex matching (not stated)
• Whether the API accepts an LLM-enabled entity and what its request schema is (the API guide and OpenAPI pages are behind login)
• Whether the 0.30 confidence threshold applies to custom entities, and whether custom entities show a score in the Findings table
• Which entity wins when a custom entity and a built-in entity match the same span (the structured page only advises disabling or tuning the built-in entity)
• What a "document" is in "up to 5,000 documents", and the latency of an LLM entity on one short prompt (documented times are for datasets: under 20 minutes for under 100 documents, up to 8 hours)
• Regex dialect, flags and timeouts (the page names regex101.com and pair.gov.sg only)
• Whether the 500 limit counts words or entries (the fixed-list page says words, the Inclusion page says entries)
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
• Anonymise side, one-way contrast: Pseudonymisation values "are generated by irreversible hashing (SHA-256) or (SHA-512) with a random salt applied to prevent brute-force attacks" (Cloak Guide, Pseudonymisation page) **[Documented]**
• Restore side: "The Web UI currently supports decrypting one value at a time (paste into the text field)." (Cloak Guide, free-text decryption page) **[Documented]**
• Restore side, bulk: for "multiple values or a file of encrypted data" the page points to the Free-Text Decryption API, "which supports looping through rows in a CSV" (free-text decryption page; the API page is behind login) **[Documented]**
• Key management: "Cloak provides a secure way to store, manage, and share the encryption keys and salts used in your anonymisation jobs." (Cloak Guide, Secret Sharing and Decryption page) **[Documented]**
• Home page features: "Encrypt identifiers consistently across datasets using shared secrets" and "Decrypt data when needed through the Web UI or API" (Cloak Guide, home page) **[Documented]**
• Mapping-table route in the API: "You can achieve Replace (Unique) behaviour programmatically using Cloak's `/analyze` endpoint and a mapping table you maintain." (Cloak Guide, Replace (Unique) page) **[Documented]**
• Restoring placeholders from a mapping table the caller keeps is a possible way to reverse Replace (Unique) output (premise: the page says the mapping table is maintained by the caller; no page describes restoring from it) **[Inferred]**
• GovTech 2023 deck workflow: "Detect PII", "Anonymise PII", "Mapping Table" and "Anonymised Response", with "API: Takes in unstructured text, returns mapping table and anonymized result." (USENIX PEPR 2023 slides, slide 22, 11 Sep 2023; may have changed) **[Documented]**
### R2
Summary: **Keeps values linkable or restorable without exposing them.** Documented aims are consistent identifiers across datasets, safer key sharing, and keeping personal data out of external LLM prompts. Encrypt is reversible; Pseudonymise is one-way. **[Documented]**
Detail:
• "Consistent anonymisation across datasets - Use the same keys or salts to encrypt or pseudonymise entities consistently, enabling dataset linkage on primary keys without exposing the originals." (Cloak Guide, Secret Sharing and Decryption page) **[Documented]**
• "Secure sharing and continuity - Share secrets with colleagues without exposing the underlying key material, and ensure access persists across role changes and departures." (same page) **[Documented]**
• The page says this "replaces insecure practices like storing keys in spreadsheets or emailing them between colleagues" (same page) **[Documented]**
• Home use case: "Multiple data owners anonymise independently using the same secret, producing data that can still be linked on a common encrypted identifier" (Cloak Guide, home page) **[Documented]**
• Pseudonyms persist but cannot be undone: "irreversible and persistent pseudonyms" that are the same "within and across different datasets, conditioned on using the same salt value" (Pseudonymisation page) **[Documented]**
• LLM leakage framing: "Potential privacy leakages from usage of LLM products in the public sector." and "Outgoing prompt does not leak PII to overseas servers or ChatGPT" (USENIX PEPR 2023 slides, slides 21 and 22, 11 Sep 2023) **[Documented]**
• Whether Replace, Redact, Mask or Alias output can be reversed (checked the Replace, Redact, Masking and Alias pages, which describe the transformation only) **[Not disclosed]**
• Residual risk: "the data owner must assess the final output for remaining direct identifiers, quasi-identifier combinations, missed free-text entities and linkage risk." (Cloak Guide, FAQs) **[Documented]**
• An entity the detector misses stays in clear text, because Encrypt acts only on detected entities (premise: FAQ "Free-text detection is probabilistic, so 100% recall should not be assumed.") **[Inferred]**
• Compare Presidio's reversible route in Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt); this column covers only what Cloak's pages state **[Inferred]**
### R3
Summary: **Encrypt on the way out, decrypt on the way back.** Encrypt runs inside a free-text job on a prompt string or file; decrypt takes one pasted ciphertext in the Web UI, or rows through the API. No direction flag or prompt context is documented. **[Inferred]**
Detail:
• Anonymise side: Encrypt is chosen per entity type: "toggle the detection of Entity Types and the corresponding anonymisation technique to be applied for each entity type" (Cloak Guide, usage guide) **[Documented]**
• Anonymise side input: pasted text up to "20,000 characters (approx. 3,000 words)" or .csv, .pdf and .docx files (usage guide) **[Documented]**
• Anonymise side vendor use: "Strip PII in real-time via API before data reaches external LLMs or other WOG products" (home page use cases) **[Documented]**
• Restore side Web UI: "Input your encrypted value into the left text field." and the secret is selected in step 2 (free-text decryption page) **[Documented]**
• Restore side scope: the guide's own link text is "Free-text Decryption Guide - Decrypt individual encrypted values" (Secret Sharing and Decryption page) **[Documented]**
• Restore side, whole text: whether one call can restore a full reply that holds several ciphertext tokens (checked the free-text decryption page, the decryption intro and the home page) **[Not disclosed]**
• Restore side in the deck: the "Anonymised Response" comes back through the Cloak "Transformer Module" in the Government Commercial Cloud environment, with placeholders shown as "<hash value 1>" (USENIX PEPR 2023 slides, slide 22) **[Documented]**
• Release note v2.0.1, 4 December 2023, lists "[API] Reconstruct endpoint for FTA API"; what it does is not described (checked the release notes, the public API guide page and the Replace (Unique) page) **[Not disclosed]**
• Direction (R002): no input or output flag was found on the encrypt, decryption or API guide pages or the portal pages (searched for direction, inbound, outbound, input type, response); the API schema is behind login **[Not disclosed]**
• Anonymise side acts on the text going to a model and restore side on text coming back; both take a string (premise: the deck workflow and the vendor's LLM use case) **[Inferred]**
• A model reply must keep a base64 token intact for restore to work, since the Web UI decrypts one pasted value exactly (premise: Encrypt output is base64 and decrypt takes the whole value) **[Inferred]**
• No system or user prompt is needed as context (premise: the documented inputs are the text, the entity settings and the secret) **[Inferred]**
### R4
Summary: **AES-256 CBC encryption under a managed secret.** Encrypt output is base64. The Secrets Manager shares keys and salts without showing key material, and logs their use. Pseudonymise uses SHA-256 or SHA-512 with a salt. Hosting is Government Commercial Cloud. **[Documented]**
Detail:
• Cipher: "The encryption uses AES cypher in CBC mode"; "AES-256 Encryption is recommended. The output would be in base64." (Encrypt page) **[Documented]**
• Mode restriction: "Due to security reasons, we have restricted encryption to only AES-256 CBC Mode Encryption." (Encrypt page) **[Documented]**
• Example row on the page: original "Jason" becomes "pX09dIQ4X3gU1FC3r8pZXA==" (Encrypt page) **[Documented]**
• That example decodes to 16 bytes, one AES block, so the token seems to carry no separate initialisation vector, which the Secrets Manager holds with the key (premise: base64 arithmetic and the Secrets Manager text "secret key and IV value"); Presidio's token layout differs, see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt) **[Inferred]**
• Key sharing: "Members of shared secrets will not be able to view or access the secret key and IV value, but will be able to use it to decrypt data." (Cloak Guide, Secrets Manager page) **[Documented]**
• Sharing limits: "up to 10 other users per operation, and with a maximum of 50 users per secret" (Secrets Manager page) **[Documented]**
• Audit: the audit view shows "the member's email, time of usage and activity type"; one activity is "Decrypt Free Text: Users decrypts a singular encrypted value" (Secrets Manager page) **[Documented]**
• Storage: "Salts and Secret Keys within Cloak are stored in encrypted format, and usage of salts/secret keys are audited." (Cloak Guide, FAQs) **[Documented]**
• Transport and rest: "All data is encrypted in transit and at rest." (www.cloak.gov.sg FAQ, read 2026-10-10) **[Documented]**
• Pseudonymise: SHA-256 or SHA-512 "with a random salt"; the same salt gives the same pseudonym (Pseudonymisation page) **[Documented]**
• Salts, page text: "Custom salt values will be included in the future." (Pseudonymisation page); see the conflict with the release notes below **[Documented]**
• Salts, release notes: v2.1.0, 19 March 2024, "[FTA] Added salt parameter for Pseudonymisation transformation" and v2.1.4, 4 June 2024, "[FTA] Support for custom salts and user managed salts" (Cloak Guide, release notes) **[Documented]**
• Decryption release: v2.1.0, 19 March 2024: "[Decryption] Decrypt encrypted free-text or tabular data using secret keys." (release notes) **[Documented]**
• Techstack: "AWS GCC 2.0" (developer portal, Features and Roadmap, last updated 21 Aug 2026) **[Documented]**
• Presidio link: "Microsoft Presidio has a built-in encryption functionality, to encrypt and decrypt identified entities." (Encrypt page); its link to microsoft.github.io/presidio/tutorial/12_encryption/ returned HTTP 404 on 2026-10-10 **[Documented]**
• Whether Cloak's Encrypt is Presidio's encrypt operator: the wording and AES-CBC match point that way, while the example token length differs from Presidio's layout; no GovTech page says it (see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) **[Inferred]**
• Deployed version: the newest release note is v2.2.2 (4 August 2024) (release notes page) **[Not disclosed]**
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
• API response format for encrypt and decrypt (the API guide and OpenAPI pages redirect to login, HTTP 200 at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in, observed 2026-10-10) **[Not disclosed]**
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
• Terms clause 3.4.7 bars "perform any benchmarking tests or analyses of the Service", and 3.4.9 and 3.4.11 bar sharing licence keys or access with third parties; a bench could first seek GovTech's written view (licensing items, not interpreted here) **[Inferred]**
• Possible round trip: made-up names and IDs, encrypt, decrypt, and compare with the originals across lengths and non-ASCII names **[Inferred]**
• Possible checks: the same value twice in one text and across two jobs under the same secret, and under a different secret **[Inferred]**
• Possible failure cases: a changed or truncated token, a wrong secret, a secret not shared with the user, and a mock model reply that edits or drops the token **[Inferred]**
• Possible LLM step: use a harmless local model reply to see whether base64 tokens survive, and note token cost; no real model call is needed for the first pass **[Inferred]**
• Possible comparison source: Presidio's encrypt and decrypt as a clearly labelled stand-in, never reported as Cloak (see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) **[Inferred]**
• Nothing was run or requested during research; the Web UI, API and API guide were not opened (research is read-only) **[Inferred]**
### R8
Summary: **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, how a whole model reply with several tokens is restored, what the Reconstruct endpoint does, key length and IV handling, and failure behaviour for a wrong secret.
Detail:
• Terms clause 3.4 says "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 reads "perform any benchmarking tests or analyses of the Service;" (Terms of Use dated 24 July 2024, text from the PDF via pypdf). Whether a comparison bench falls under it is a licensing question; not interpreted here and needs GovTech's written position
• Terms 3.4.9 reads "transfer assign or permit the sharing of license keys to or with a third party;" and 3.4.11 reads "provide third party access to the Service"; whether secret sharing between test accounts is affected (the Cloak guide describes sharing secrets among Cloak users)
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

## Reviewer notes
1. **Scope and drafting split.** This file holds CK2 and CK3 only (half B); CK1 is drafted by another drafter. Cross-references name CK1 and Presidio columns by exact header text only. Headers use main's tweaks from queue.md (CK2 "(lists, regex and LLM)", CK3 "(encrypt and restore)"), not the brief's original wording.
2. **CK3 direction (R002).** No public input or output flag was found, so CK3 stays one column. The anonymise side and the restore side are separate bullets in R1, R3, R4, R5 and R6 (and the restore-only facts are marked "Restore side"), so a later split needs only a copy.
3. **Not-yet-resolved facts.** The Reconstruct endpoint's function, the API's schema and any direction flag, the LLM's identity, key and IV handling, failure behaviour, and Terms 3.4.7 are open and listed in each R8.
4. **Terms text.** Clause 3.3, 3.4 (lead-in), 3.4.7, 3.4.9, 3.4.11, Schedule 2.2 and Schedule 4.6 were read from `https://file.go.gov.sg/cloak-terms.pdf` (go.gov.sg/cloak-terms redirects there, HTTP 302 observed 2026-10-10) with pypdf; the PDF printed pypdf warnings about malformed objects but the clause text is intact. The PDF text is quoted exactly; whitespace normalised.
5. **Conflicts.** C3 (playbook "internal service" versus docs "open to select non-government entities") appears in CK2 R8. C4 (salts: Pseudonymisation page "will be included in the future" versus release notes v2.1.0 and v2.1.4) is two bullets in CK3 R4 and one line in R8. C8 (Encrypt page link to Presidio's tutorial returns HTTP 404; the supported-entities link returns 200) is a bullet in CK3 R4. C9 (FAQ links www.cloak.gov.sg/terms, HTTP 404) is not used; the Terms are cited at file.go.gov.sg.
6. **Small page inconsistencies, not conflicts.** (a) LLM entity limit is worded "per dataset" on the intro page and "per project" in the FAQs (the FAQ says "normally"); both are quoted. (b) Inclusion page says "up to 500 entries", fixed-list page says "500 words". (c) The Custom page's link for LLM entities points at `custom-entities-structured/intro.md`, which does not exist in the sidebar; the real page is `custom-entities-unstructured/intro.md`.
7. **Derived facts.** The 16-byte arithmetic in CK3 R4 is my base64 decoding of the example string on the Encrypt page (Python base64, 24 characters ending "==" gives 16 bytes); it is labelled `[Inferred]`. The claim "the same value gives the same ciphertext under one secret" in R5 is also `[Inferred]`.
8. **Image captions.** Several facts rest on Markdown image captions in the Cloak Guide (confidence default 0.30, the Findings table columns, custom-entity result captions, the DATE_TIME_SPECIFIC comparison). They are text on the official page, labelled `[Documented]`, and each bullet names the source as a caption.
9. **Pages not reachable.** The API Guide, OpenAPI specification and package guide redirect to `docs.developer.tech.gov.sg/auth/otp-login` (HTTP 200 after redirect, reason not_logged_in, observed 2026-10-10); not opened further. The free-text decryption helper script page (linked from the free-text decryption page) redirects the same way.
10. **Summarising fetches.** None used. Cloak Guide pages by curl; portal pages, cloak.gov.sg and the aiguardian.gov.sg pages with `fetch_text.py` (verbatim); the playbook mdx by curl of raw.githubusercontent.com at the full pin SHA `45908b48c0a8b6d3855a154c0e41a12958a99205` (also identical at HEAD `97338569`); PDFs by pypdf.
11. **Absence checks.** GitHub repository search ("cloak" in GovTechSG, opengovsg, govtech-responsibleai, datagovsg) returned 0 results through the GitHub search API on 2026-10-10 (no rate-limit message); aiguardian.gov.sg `/docs` and `/docs/wiki/Sentinel-Guardrails` text has no "cloak" hit.
12. **Bench wording (R032).** R7 states suggestions only ("a bench could", "possible", "suggested") and records that nothing was run. Sensitive test data and any approach to GovTech are not decided here.
13. **Counts.** Two columns, R1 to R9 each. Summary word counts are at most limit minus 1 excluding the label (lessons 18).
