"""Column edits for cloak (CK1, CK2, CK3). Imported by merge_cloak.py."""

DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"
PB = "**[Documented: repo govtech-responsibleai/playbook@45908b48]**"
H1 = "Cloak: Free-text PII detection and anonymisation"
H2 = "Cloak: Custom entity detection in free text (lists, regex and LLM)"
H3 = "Cloak: Reversible anonymisation and decryption (encrypt and restore)"


def apply(K):
    # =================================================================== CK1
    C = "CK1"
    # ---- R1
    K.sub(C, 1, "Custom entities (CK2 mechanisms)",
          "Custom entities (CK2 mechanisms) are a separate function:",
          "Custom entities are a separate function, covered in the column " + H2 + ":",
          "T71: internal id replaced by the exact header text")
    # ---- R2
    K.sub(C, 2, "Counting one tag per group plus the 4 address tags",
          "Counting one tag per group plus the 4 address tags gives 20 baseline tags",
          "Counting one tag for each of the 16 groups other than Address, plus the 4 address tags, gives 20 baseline tags",
          "T39: the 17 groups include Address, so 'one tag per group plus 4' counted it twice; label stays Inferred")
    # ---- R3
    K.repl(C, 3, 'shows an "Anonymised Response" returning through a "Transformer Module"', [
        '• The same deck slide shows the "Anonymised Response" returning from the "Gen AI Magic!" box to the agency product with the placeholder "<hash value 1>" still in it (USENIX PEPR 2023 deck, slide 22, layout read from the rendered slide) ' + DOC,
        '• The deck draws no step that turns the placeholders back into the original values (checked slide 22 and the text of all 32 slides; the Mapping Table box sits on the agency product side) ' + ND],
        "T57 CORRECTION: the rendered slide does not show the response returning through the Transformer Module; two bullets (layout Documented, absence of a restore step Not disclosed); the 'a CK3 mechanism' wording goes (T71)",
        kind="correction")
    # ---- R4
    K.summary(C, 4,
        "Summary: **Named techniques, model not named.** Entities are found by an AI model (spaCy given as an example) plus regex, rule-based matching and checksums, hosted on the Government Commercial Cloud. Reached by web UI or API. " + DOC,
        "T34: 'GovTech's cloud' is not in the Detail; the FAQ and portal say Government Commercial Cloud (35 words)")
    K.sub(C, 4, "LLM-enabled custom entity (CK2 mechanism, Beta)",
          "LLM-enabled custom entity (CK2 mechanism, Beta):",
          "LLM-enabled custom entity (Beta; see " + H2 + "):",
          "T71: internal id replaced by the exact header text")
    K.sub(C, 4, "Encrypt technique (CK3 mechanism)",
          "Encrypt technique (CK3 mechanism):",
          "Encrypt technique (see " + H3 + "):",
          "T71: internal id replaced by the exact header text")
    K.repl(C, 4, "Release notes: the newest entry is v2.2.2", [
        "• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) " + DOC,
        "• Release notes: v2.1.0 (19 March 2024) lists the ORGANIZATION entity type and FTA templates (Cloak Guide, release notes) " + DOC,
        '• Release notes: v2.0.1 (4 December 2023) lists "[FTA] Added Word document support" (Cloak Guide, release notes) ' + DOC],
        "T33, T36, T73: 'newest' reworded (v2.2.2 is listed above v2.2.1); three release facts split, one label each")
    K.repl(C, 4, "Cloak shares tag names such as PERSON", [
        "• Cloak shares tag names such as PERSON, EMAIL_ADDRESS, PHONE_NUMBER and IBAN_CODE with Presidio's catalogue, which could mean reuse of Presidio recognisers; see Presidio: PII detection in text (Analyzer) " + INF],
        "T72: one Presidio pointer, shortened from 383 characters; no Presidio fact restated")
    # ---- R5
    K.repl(C, 5, "Whether the confidence setting is global or per entity", [
        '• Developer Portal Features page: "Adjust detection sensitivity per entity type to balance recall and precision for your dataset" (Developer Portal, features page) ' + DOC,
        '• Cloak Guide: the Anonymisation Settings drawer has one "Adjust Confidence level" dropdown with a slider "set to the default value of 0.30" (Cloak Guide, confidence level page, captions) ' + DOC],
        "T41: two sides of a conflict as two bullets, one label each (README section 3 rule 4); the open question stays in R8")
    K.ins_after(C, 5, 'Accuracy claim: ">97% recall',
        "• Terms clause 9.1 says the Service is provided \"on an 'as is' and 'as available' basis without warranties of any kind\", and 9.1.1 lists accuracy, completeness and correctness among the warranties disclaimed (Terms of Use dated 24 July 2024) " + DOC,
        "T16: Terms 9.1 and 9.1.1 beside the recall claim, no comment")
    # ---- R6
    K.repl(C, 6, "Inclusion list on an existing entity: words or a CSV", [
        '• Inclusion list on an existing entity: "You can add words individually or upload a CSV file containing up to 500 entries." (Cloak Guide, inclusion feature page) ' + DOC,
        '• Inclusion list limit as worded in the Important Notes table: "Only the first 500 words in a CSV upload will be used." (Cloak Guide, inclusion feature page; the same page gives the limit in entries and in words) ' + DOC,
        '• Inclusion list matching is "Word-sensitive" (exact spelling and punctuation must match) and "Not case-sensitive" (Cloak Guide, inclusion feature page) ' + DOC],
        "T5, T42: one bullet mixing entries and words split in three (entries, words, matching); main: unit difference stays an R8 question")
    K.repl(C, 6, "Mask defaults: 3 characters", [
        '• Mask defaults: Number of Characters 3, Masking Type Suffix, Masking Character "-" (Cloak Guide, masking page, Usage Guide table) ' + DOC,
        '• Masking Type table: "Suffix: masks the starting characters" and "Prefix: masks the ending characters" (Cloak Guide, masking page) ' + DOC,
        '• Masking page example: 120414 becomes 120 followed by three asterisks and is described as "Transforms into a suffix masked value", which reads the other way from the Masking Type table (Cloak Guide, masking page, Example table) ' + DOC,
        '• Alias is "only available for the PERSON entity type" (Cloak Guide, Alias page) ' + DOC,
        '• Alias options Context and Offset both default to On (Cloak Guide, Alias page) ' + DOC],
        "T48, T73: the within-page Mask conflict stated as two attributed facts; Alias split from the Mask defaults")
    K.sub(C, 6, "Encrypt needs a secret key",
          "(CK3 mechanism, Encrypt with a shared secret)",
          "(see " + H3 + ")",
          "T71: internal id replaced by the exact header text")
    K.repl(C, 6, "API: security levels L2", [
        "• API security levels: L2 (personalised token), L3 (system token), L4 (signature-based) (Cloak Guide, API guide) " + DOC,
        '• API onboarding: an API key per security level; "complete our Cloak (API) Onboarding Form", and a key follows "within 1-2 business days" (Cloak Guide, API guide and key FAQs) ' + DOC],
        "T73: levels and onboarding are two facts, one label each")
    K.sub(C, 6, "Regex custom entity, API only (CK2 mechanism)",
          "Regex custom entity, API only (CK2 mechanism):",
          "Regex custom entity, API only (see " + H2 + "):",
          "T71: internal id replaced by the exact header text")
    K.repl(C, 6, "Web UI access: WOG users sign in", [
        "• Web UI access: WOG users sign in with WOG-AD; other approved users register, and vendors complete TechPass onboarding after Cloak Ops approval (Cloak Guide, key FAQs and registration guide) " + DOC,
        '• Non-government entities "Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step." (Cloak Guide, key FAQs) ' + DOC,
        '• Who may use it, Cloak Guide: Cloak "is open to select non-government entities (e.g. public healthcare)" (Cloak Guide, home page); the playbook words it differently ' + DOC,
        '• Who may use it, playbook: "GovTech\'s dedicated internal service for comprehensive and localised PII detection" (Responsible AI playbook, privacy improvements page) ' + PB],
        "T73, T8: access route and pre-approval split; the playbook and Cloak Guide access wordings as two attributed bullets (conflict C3 logged in the change log); 'see the next bullet' dropped")
    K.sub(C, 6, 'Data ceiling: "You shall not upload',
          ", read with pypdf)", ")",
          "T70: process wording removed")
    # ---- R7
    K.ins_after(C, 7, "Access conditions: a Web UI account needs WOG-AD",
        '• Terms of Use, clause 3.3 defines the term: "\'Public Sector Entities\' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)" ' + DOC,
        "T10: definition of Public Sector Entities, verbatim, no interpretation")
    K.sub(C, 7, "Terms of Use, clauses 3.4.9 and 3.4.11",
          "(read with pypdf, dated 24 July 2024)", "(Terms of Use dated 24 July 2024)",
          "T70, T11: process wording removed")
    K.repl(C, 7, "No access was requested and nothing was run", [
        "• Sensitive test data (real personal data) is a bench-design question; a bench could start with made-up values, and Terms Schedule 4.6 sets a data ceiling for anything uploaded (see R6) " + INF],
        "T70, R032: session wording ('no access was requested', 'research') removed; bench content stays a suggestion")
    # ---- R8
    K.repl(C, 8, "Does Terms clause 3.4.7", [
        "• Does Terms clause 3.4.7 (\"perform any benchmarking tests or analyses of the Service\") bar a bench comparison, and would GovTech's written consent under clause 3.3 cover it? (the Terms define no benchmarking term and state no exception; checked all 15 pages; decided before any bench run)"],
        "T9: clause quoted; permitted use stays open (R025 pattern, R032); process wording removed", kind="replace")

    # =================================================================== CK2
    C = "CK2"
    K.summary(C, 4,
        "Summary: **Three mechanisms: list, regex and few-shot LLM.** Lists match exact words, regex matches patterns, and the Beta LLM entity is prompted with 3 to 5 examples on a privately hosted model on Government Commercial Cloud. " + DOC,
        "T59: 'learns from' contradicts 'without fine-tuning'; few-shot prompting (35 words)")
    K.repl(C, 4, "Release history: the newest release note", [
        "• Release history: the release notes name no LLM entity, so the deployed version and the LLM entity's release date are not given (checked the release notes page in full; highest version v2.2.2 of 4 August 2024, latest dated entry v2.2.1 of 28 August 2024) " + ND],
        "T33: 'newest' reworded")
    K.repl(C, 4, "Cross-reference: Presidio also has regex", [
        "• Cross-reference: see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); no GovTech page says Cloak's custom entities are Presidio recognisers (premise for any link: the shared terms \"custom recognisers\" and \"context words\") " + INF],
        "T72: the restated Presidio fact (regex and word-list recognisers) dropped; one pointer")
    K.summary(C, 5,
        "Summary: **Transformed text for each custom match.** Each match is replaced, redacted, masked or otherwise transformed with the technique chosen for that entity. The result is anonymised text or a file, and an email says when an LLM entity job completes. " + DOC,
        "T60: the Findings table is described for detected entities in general, not for custom matches (custom-entity rows in it are Not disclosed in B R5); Summary reworded (40 words)")
    K.sub(C, 5, "Findings table: \"The Findings table listing",
          "• Findings table: ", "• Findings table for detected entities in general: ",
          "T60: prefix so the caption does not read as a custom-entity fact; the Not disclosed bullet that follows stays")
    K.summary(C, 6,
        "Summary: **A list, a regex or examples.** A list takes up to 500 (words or entries; the docs differ), a regex takes a pattern, and the LLM entity takes a definition and 3 to 5 examples. Context words and per-pattern scores are API only. " + DOC,
        "T42 (main): list-limit wording 'words or entries; the docs differ', R8 question stays (43 words)")
    K.sub(C, 3, "Direction (R002): no input or output flag, role",
          "Direction (R002): ", "Direction: ",
          "hygiene: ruling id removed from the cell text", kind="style")
    K.repl(C, 7, "Terms clause 3.4.7 bars", [
        "• Terms clause 3.4.7 lists \"perform any benchmarking tests or analyses of the Service\" among the things the user shall not do, so a bench could first seek GovTech's written view " + INF],
        "T70: 'a licensing item, not interpreted here' removed")
    K.delete(C, 7, "Nothing was run or requested during research",
             "T70: the bullet only reported that nothing was run; R7 keeps its Minimum setup bullet and the others")
    K.repl(C, 8, "Terms clause 3.4 says", [
        "• Terms clause 3.4 says \"You shall not, and shall not authorise or permit any third party to:\" and 3.4.7 reads \"perform any benchmarking tests or analyses of the Service;\" (Terms of Use dated 24 July 2024). Whether a comparison bench falls under it is not stated (the Terms define no benchmarking term; checked all 15 pages); decided before any bench run"],
        "T9, T70: clause quoted verbatim, no interpretation; process wording removed")
    K.sub(C, 8, "Which language model, size and version serve the LLM entity",
          "the newest release note is v2.2.2 of August 2024", "the release notes end at v2.2.2 and v2.2.1 of August 2024",
          "T33: 'newest' reworded")
    K.ins_after(C, 8, "Whether the 500 limit counts words or entries",
        "• Whether the LLM-enabled custom entity limit is per dataset or per project (the unstructured intro says \"only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)\" and the FAQs say \"The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time\"; needs testing)",
        "T43: R8 bullet for the per-dataset against per-project wording (both quoted in R4)")

    # =================================================================== CK3
    C = "CK3"
    K.sub(C, 1, "GovTech 2023 deck workflow",
          "GovTech 2023 deck workflow:", "GovTech 2023 deck slide labels:",
          "T57: the labels and the API callout are what the slide shows; 'workflow' implied a flow the slide does not draw")
    K.repl(C, 2, "Compare Presidio's reversible route", [
        "• Presidio's reversible route is covered in the column Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt) (premise: both products offer an encrypt and a decrypt step) " + INF],
        "T70: instruction to the reader ('this column covers only ...') removed")
    K.repl(C, 3, "Restore side in the deck", [
        '• Restore side in the deck: the "Anonymised Response" returns from the "Gen AI Magic!" box to the agency product with the placeholder "<hash value 1>" still in it (USENIX PEPR 2023 slides, slide 22, layout read from the rendered slide) ' + DOC,
        "• Restore side in the deck: the slide does not say where or how placeholders are restored from the mapping table (checked slide 22 and the text of all 32 slides) " + ND],
        "T57 CORRECTION: the response does not return through the Transformer Module on the rendered slide; restore step Not disclosed",
        kind="correction")
    K.sub(C, 3, "Direction (R002): no input or output flag was found",
          "Direction (R002): ", "Direction: ",
          "hygiene: ruling id removed from the cell text", kind="style")
    K.sub(C, 3, "Anonymise side acts on the text going to a model",
          "(premise: the deck workflow and the vendor's LLM use case)",
          "(premise: the Encrypt page says the key is needed \"for both encryption and decryption\", and the deck slide shows the response returning with placeholders)",
          "T57: premise no longer rests on a Transformer Module flow")
    K.repl(C, 4, "That example decodes to 16 bytes", [
        "• That example decodes to 16 bytes, one AES block, so the token seems to carry no separate initialisation vector, which the Secrets Manager holds with the key (premise: base64 arithmetic and the Secrets Manager text \"secret key and IV value\") " + INF],
        "T72: the Presidio token-layout clause dropped (no Presidio source or label here)")
    K.repl(C, 4, "Salts, page text", [
        "• Salts, page text: \"Custom salt values will be included in the future.\" (Pseudonymisation page); the release notes list custom salts in v2.1.0 and v2.1.4 " + DOC],
        "T70: 'see the conflict with the release notes below' (instruction to the reader) replaced by a statement; the release-note bullet follows (conflict C4 logged)")
    K.ins_after(C, 4, 'Techstack: "AWS GCC 2.0"',
        "• Hosting: \"users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment\" (Cloak Guide, key FAQs) " + DOC,
        "T35: the R4 Summary says Government Commercial Cloud; the expansion is now in this column's Detail")
    K.repl(C, 4, "Presidio link", [
        "• Encrypt page: \"Microsoft Presidio has a built-in encryption functionality, to encrypt and decrypt identified entities.\" (Cloak Guide, Encrypt page) " + DOC,
        "• The Encrypt page's link to microsoft.github.io/presidio/tutorial/12_encryption/ returned HTTP 404 on 2026-10-10 " + DOC],
        "T72, T73: quote and HTTP fact split, one label each")
    K.repl(C, 4, "Whether Cloak's Encrypt is Presidio's encrypt operator", [
        "• Whether Cloak's Encrypt is Presidio's encrypt operator is not stated by any GovTech page; the Encrypt page's wording and AES-CBC point that way (premise: the Encrypt page text above; see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) " + INF],
        "T72: the three Presidio bullets reduced to one cross-reference; the token-length contrast dropped")
    K.repl(C, 4, "Deployed version: the newest release note", [
        "• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) " + DOC,
        "• The deployed version (checked the release notes page in full, the home page and the portal pages; not stated) " + ND],
        "T33: a positive fact split from the absence; 'newest' reworded")
    K.sub(C, 7, "Terms clause 3.4.7 bars",
          "(licensing items, not interpreted here)", "(the clauses are quoted in R8)",
          "T70: process wording removed")
    K.delete(C, 7, "Nothing was run or requested during research",
             "T70: the bullet only reported that nothing was run; R7 keeps its Minimum setup bullet and the others")
    K.repl(C, 8, "Terms clause 3.4 says", [
        "• Terms clause 3.4 says \"You shall not, and shall not authorise or permit any third party to:\" and 3.4.7 reads \"perform any benchmarking tests or analyses of the Service;\" (Terms of Use dated 24 July 2024). Whether a comparison bench falls under it is not stated (the Terms define no benchmarking term; checked all 15 pages); decided before any bench run"],
        "T9, T70: clause quoted verbatim, no interpretation; process wording removed")
    K.sub(C, 8, "Terms 3.4.9 reads",
          "whether secret sharing between test accounts is affected (the Cloak guide describes sharing secrets among Cloak users)",
          "whether secret sharing between test accounts is affected is not stated (the Terms do not define \"license keys\"; the Cloak guide describes sharing secrets among Cloak users)",
          "T11: 'license keys' is undefined in the Terms (checked the 15 pages)")
