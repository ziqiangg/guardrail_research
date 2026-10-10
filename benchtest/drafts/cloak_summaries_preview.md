# Cloak: Summary preview (Checkpoint 2)

Generated from cloak_two_level.md on 2026-10-10. Format: `Rn` (words excluding the trailing label, top-level Detail bullets): Summary text. Limits: 45 words, R7 60 (the merge keeps every Summary at most limit minus 1, lessons 18).

## CK1: Cloak: Free-text PII detection and anonymisation

- **R1** (42w, 13 bullets): **Finds personal data in text and rewrites it.** Cloak's free-text tool detects entities such as names, NRICs and addresses in pasted text or uploaded files, then replaces, redacts, masks, aliases, pseudonymises or encrypts them. The result is rewritten text or a file. **[Documented]**
- **R2** (33w, 18 bullets): **Personal data in free text, tuned for Singapore.** Seventeen entity groups cover names, NRICs, phone numbers, emails, addresses, banking, dates and more. Scanned documents and images are not processed, and detection is probabilistic. **[Documented]**
- **R3** (44w, 13 bullets): **Any text or file passed in; no direction setting found.** The tool takes pasted text, CSV, PDF or DOCX and needs no conversation context. No page shows an input or output flag, so prompts, replies and retrieved text would all be handled as strings. **[Inferred]**
- **R4** (35w, 19 bullets): **Named techniques, model not named.** Entities are found by an AI model (spaCy given as an example) plus regex, rule-based matching and checksums, hosted on the Government Commercial Cloud. Reached by web UI or API. **[Documented]**
- **R5** (43w, 16 bullets): **Rewritten text plus a findings table.** Output is transformed text or a file; the web UI adds a per-entity table with type and score. A confidence slider (default 0.30) sets the cut-off. The only accuracy claim is over 97 percent recall, no method. **[Documented]**
- **R6** (38w, 32 bullets): **Text or files within size limits, plus settings.** Pasted text is capped at 20,000 characters, files at 500 MB (CSV) or 200 MB (PDF, DOCX). Settings choose entities, techniques, threshold and word lists. Access needs an approved account. **[Documented]**
- **R7** (53w, 11 bullets): **Minimum setup:** Cloak has no public code or package, so a bench would need approved Web UI or API access. A bench could send short synthetic Singapore-style prompts with planted names, NRICs, addresses and phone numbers, and compare each output with the expected tags. Terms clause 3.4.7 mentions benchmarking, an open licensing question. **[Inferred]**
- **R8** (33w, 14 bullets): **Key open questions.** Whether Terms clause 3.4.7 allows benchmarking, the API schema and any direction flag, the model and version, accuracy beyond the recall claim, language coverage, short-prompt latency, and the Sentinel integration.
- **R9** (26w, 40 bullets): Cloak Guide Markdown pages, the Cloak product site, GovTech Developer Portal pages, the Terms PDF, a 2023 GovTech deck and the GovTech playbook, all read 2026-10-10.

## CK2: Cloak: Custom entity detection in free text (lists, regex and LLM)

- **R1** (38w, 13 bullets): **Adds your own entity types to free-text anonymisation.** A custom entity can be a fixed word list, a regex pattern or, in Beta, an LLM given a definition and examples. Matches are then transformed like the built-in entities. **[Documented]**
- **R2** (33w, 13 bullets): **Domain terms the built-in entities miss.** Documented examples are hospital case numbers, car licence numbers, unusual date formats, usernames and disease names. Free-text detection is probabilistic, so full recall should not be assumed. **[Documented]**
- **R3** (42w, 12 bullets): **A setting applied to free text in a project.** A custom entity runs on pasted text or csv, pdf and docx uploads. No direction flag was found, so it applies to prompts, responses or retrieved text sent as a string or file. **[Inferred]**
- **R4** (35w, 21 bullets): **Three mechanisms: list, regex and few-shot LLM.** Lists match exact words, regex matches patterns, and the Beta LLM entity is prompted with 3 to 5 examples on a privately hosted model on Government Commercial Cloud. **[Documented]**
- **R5** (38w, 15 bullets): **Transformed text for each custom match.** Each match is replaced or otherwise transformed with the technique chosen for that entity. The result is anonymised text or a file, and an email says when an LLM entity job completes. **[Documented]**
- **R6** (43w, 16 bullets): **A list, a regex or examples.** A list takes up to 500 (words or entries; the docs differ), a regex takes a pattern, and the LLM entity takes a definition and 3 to 5 examples. Context words and per-pattern scores are API only. **[Documented]**
- **R7** (48w, 8 bullets): **Minimum setup:** documentation only today; a Web UI trial needs an approved Cloak account and the API needs an onboarding key. A bench could, once permitted, run synthetic text through one list, one regex and one LLM entity on under 100 documents, then compare with a baseline-only run. **[Inferred]**
- **R8** (39w, 15 bullets): **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, which language model backs the LLM entity, accuracy and languages for custom entities, API support for the LLM entity, and how custom and built-in entities rank when they overlap.
- **R9** (24w, 30 bullets): Cloak Guide pages (docsify Markdown), the www.cloak.gov.sg home page, GovTech developer portal pages, the Cloak Terms of Use PDF, and GovTech's Responsible AI playbook.

## CK3: Cloak: Reversible anonymisation and decryption (encrypt and restore)

- **R1** (42w, 11 bullets): **Encrypts chosen entities and decrypts them later.** The Encrypt technique replaces each detected value with AES-256 CBC ciphertext under a key kept in the Secrets Manager, and free-text decryption restores one value at a time in the Web UI. Pseudonymise is one-way. **[Documented]**
- **R2** (33w, 11 bullets): **Keeps values linkable or restorable without exposing them.** Documented aims are consistent identifiers across datasets, safer key sharing, and keeping personal data out of external LLM prompts. Encrypt is reversible; Pseudonymise is one-way. **[Documented]**
- **R3** (44w, 14 bullets): **Encrypt on the way out, decrypt on the way back.** Encrypt runs inside a free-text job on a prompt string or file; decrypt takes one pasted ciphertext in the Web UI, or rows through the API. No direction flag or prompt context is documented. **[Inferred]**
- **R4** (39w, 23 bullets): **AES-256 CBC encryption under a managed secret.** Encrypt output is base64. The Secrets Manager shares keys and salts without showing key material, and logs their use. Pseudonymise uses SHA-256 or SHA-512 with a salt. Hosting is Government Commercial Cloud. **[Documented]**
- **R5** (34w, 11 bullets): **Ciphertext out, original value back.** Encrypt replaces each entity with a base64 string, and the Web UI shows the decrypted value for a pasted token. The 2023 deck's API also returned a mapping table. **[Documented]**
- **R6** (38w, 13 bullets): **A secret, plus a ciphertext to restore.** Encrypting needs a key made or chosen in the Secrets Manager; Pseudonymise needs a salt. Decrypting needs the encrypted value and access to the same secret, as owner or shared member. **[Documented]**
- **R7** (45w, 8 bullets): **Minimum setup:** documentation only today; a trial needs an approved Cloak account, and a sharing test needs a second user. A bench could encrypt made-up values, decrypt them with the same secret, then try a changed token, a wrong secret and a mock model reply. **[Inferred]**
- **R8** (37w, 14 bullets): **Key open questions.** Whether benchmarking is allowed under Terms 3.4.7, how a whole model reply with several tokens is restored, what the Reconstruct endpoint does, key length and IV handling, and failure behaviour for a wrong secret.
- **R9** (26w, 19 bullets): Cloak Guide pages (docsify Markdown), the www.cloak.gov.sg home page, GovTech developer portal pages, the Cloak Terms of Use PDF, and the GovTech USENIX PEPR 2023 slides.

## Summaries changed in the merge

| Location | Words before | Words after | Reason |
|---|---|---|---|
| CK1 R1 | 42 | 42 | P7 fix 1: R1 Detail lists Pseudonymise, not hashing (42 words) |
| CK1 R4 | 33 | 35 | T34: 'GovTech's cloud' is not in the Detail; the FAQ and portal say Government Commercial Cloud (35 words) |
| CK2 R2 | 32 | 33 | P7 fix 5: R2 Detail has the hospital case number example, not hospital names (33 words) |
| CK2 R4 | 34 | 35 | T59: 'learns from' contradicts 'without fine-tuning'; few-shot prompting (35 words) |
| CK2 R5 | 34 | 38 | T60: the Findings table is described for detected entities in general, not for custom matches (custom-entity rows in it are Not disclosed in B R5); Summary reworded (40 words); P7 optional: R5 Detail names no Redact or Mask for custom entities (38 words) |
| CK2 R6 | 42 | 43 | T42 (main): list-limit wording 'words or entries; the docs differ', R8 question stays (43 words) |
