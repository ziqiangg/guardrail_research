"""P7 verifier fixes for cloak (cloak_review.md): 14 required fixes plus the optional suggestions accepted by main."""
DOC = "**[Documented]**"
INF = "**[Inferred]**"
ND = "**[Not disclosed]**"


def apply(K, V):
    # ================================================================ required fixes
    K.summary_text("CK1", 1, "aliases, hashes or encrypts them", "aliases, pseudonymises or encrypts them",
                   "P7 fix 1: R1 Detail lists Pseudonymise, not hashing (42 words)")
    K.ins_after("CK1", 1, 'Free-text anonymisation (FTA) "automatically detects', [
        '• Inputs: "The tool supports pasted text input as well as file uploads (.csv, .pdf, .docx)." (Cloak Guide, intro to FTA) ' + DOC,
        '• Baseline entities: "Cloak detects and transforms 20+ baseline entity types (names, NRICs, addresses, dates, phone numbers, etc.)" (Cloak Guide, intro to FTA, image caption) ' + DOC],
        "P7 fix 1: the R1 Summary draws on entity types and the pasted-text and file input, which sat only in R3 and R2; now quoted in R1")
    K.repl("CK1", 2, "Vendor count, version two", [
        '• Vendor count, version two: "Cloak detects 17+ entity types out of the box" (Developer Portal, FAQs, last updated 21 Aug 2026); the wording differs from the "20+" of version one ' + DOC],
        "P7 fix 2: the drafter's 20-tag tally is Inferred (line 20), so it cannot sit in a Documented bullet (README section 3 rule 5)")
    K.ins_after("CK2", 1, 'LLM route: "Cloak allows you to add such custom entities', [
        '• LLM route inputs: for the LLM-based approach the Custom page lists "Define your custom entity" and "Give some examples" (Cloak Guide, entity types, Custom) ' + DOC,
        '• LLM route status: the unstructured intro marks the feature "[Beta Feature]" (Cloak Guide, unstructured intro) ' + DOC],
        "P7 fix 3: the R1 Summary says Beta, definition and examples, which sat only in R4 and R6")
    K.repl("CK2", 1, "No page describes a safe or unsafe verdict or score for a custom entity", [
        "• A safe or unsafe verdict, or a score, for a custom entity (checked the custom entity pages and the FTA usage guide: they show only transformed output, and whether custom matches appear in the Findings table is not stated) " + ND],
        "P7 fix 4: leftover of T60 (the Findings table caption is about detected entities in general); an absence claim is Not disclosed (R020 ruling 1)")
    K.summary_text("CK2", 2, "hospital names", "hospital case numbers",
                   "P7 fix 5: R2 Detail has the hospital case number example, not hospital names (33 words)")
    K.repl("CK2", 3, "The Web UI returns a download", [
        '• Output delivery: "Once you are done with your transformations, click on Download to proceed with the download request." (usage guide) ' + DOC],
        'P7 fix 6: "not an inline reply" was the drafter\'s reading; the usage guide also shows the anonymised result inline')
    K.ins_after("CK2", 4, "LLM hosting: ",
        '• LLM method: "Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning. This approach only needs a small set of 3-5 examples (labelled data)" (unstructured intro) ' + DOC,
        "P7 fix 7: the R4 Summary says few-shot and 3 to 5 examples; T59 pointed to lines in R1 and R6, not R4")
    K.ins_after("CK3", 1, 'Anonymise side: "The encryption uses AES cypher', [
        '• Anonymise side, mode: "Due to security reasons, we have restricted encryption to only AES-256 CBC Mode Encryption." (Cloak Guide, Encrypt page) ' + DOC,
        '• Anonymise side, scope: the settings drawer sets "the corresponding anonymisation technique to be applied for each entity type" (Cloak Guide, usage guide) ' + DOC],
        "P7 fix 8: the R1 Summary says AES-256 CBC applied to each detected value; AES-256 and the per-entity scope sat only in R4 and R3")
    K.ins_after("CK3", 2, "Pseudonyms persist but cannot be undone",
        '• Encrypt is the reversible side: the cipher "requires a cryptographic key as an input for both encryption and decryption" (Cloak Guide, Encrypt page) ' + DOC,
        "P7 fix 9: the R2 Summary says Encrypt is reversible; R2 Detail gave only the one-way side")
    K.ins_after("CK3", 3, "Restore side scope: the guide's own link text",
        '• Restore side, bulk: for "multiple values or a file of encrypted data" the page points to the Free-Text Decryption API, "which supports looping through rows in a CSV" (free-text decryption page; the API page is behind a login) ' + DOC,
        "P7 fix 10: the R3 Summary says 'or rows through the API'; the bulk route sat only in R1")
    K.sub("CK3", 4, "Salts, page text",
          "the release notes list custom salts in v2.1.0 and v2.1.4",
          "the release notes list a salt parameter in v2.1.0 and custom salts in v2.1.4",
          "P7 fix 11: v2.1.0 lists 'Added salt parameter for Pseudonymisation transformation'; custom salts are v2.1.4")
    K.repl("CK3", 7, "Terms clause 3.4.7 bars", [
        "• Terms clause 3.4 lists \"perform any benchmarking tests or analyses of the Service\" (3.4.7), \"transfer assign or permit the sharing of license keys to or with a third party\" (3.4.9) and \"provide third party access to the Service\" (3.4.11) among the things the user shall not do, so a bench could first seek GovTech's written view " + INF],
        "P7 fix 12: Terms clauses verbatim with no interpretation (main queue row, R037), as in CK2 R7")
    V.sub("f", "Presidio", "Where",
          "That Cloak is built on Presidio [Inferred] (premise: the tag names such as SG_NRIC_FIN and PERSON follow Presidio's style, the ENCR text, and the ENTI link; no GovTech page says it)",
          "Whether Cloak is built on Presidio is not stated by any GovTech page [Not disclosed] (checked ENTI, ENCR, CRED, HOME and the portal pages). The shared tag names such as SG_NRIC_FIN and PERSON, the ENCR text and the ENTI link could point to reuse of Presidio components [Inferred] (premise: name and wording match only)",
          "P7 fix 13: aligned with the block (c) intro and the columns (T30)", kind="label")
    V.para_sub("it does not return a score or a verdict.",
               "it returns transformed text or files, the Web UI findings table lists a confidence score per detected entity, and no safe or unsafe verdict is described.",
               "P7 fix 14: the usage guide documents a confidence score per entity in the findings table")
    V.sub("a", "Free-text anonymisation (FTA)", "What it is",
          "It returns the transformed text or file and does not return a verdict or a risk score [Inferred] (premise: the FTAI and USE pages describe only an anonymised output and a findings table, no verdict field)",
          "It returns the transformed text or file, and the Web UI findings table lists a confidence score per detected entity [Documented] (USE). A safe or unsafe verdict or a risk label [Not disclosed] (checked FTAI, USE, FAQ and HOME; no verdict field is described)",
          "P7 fix 14 (R020 ruling 1): the absence is Not disclosed, as in CK1 R1; the score fact is Documented", kind="label")

    # ================================================================ optional suggestions accepted by main
    K.sub("CK1", 5, 'Accuracy claim: ">97% recall',
          "(Cloak Guide, home page; Developer Portal, overview page)", "(Cloak Guide, home page)",
          "P7 optional: the quote is verbatim on the home page only; the portal overview words it differently")
    K.repl("CK1", 1, "The documented output is transformed text or files", [
        "• The documented output is transformed text or files (text, .csv, .docx formats in the FAQ file-format table) " + DOC,
        "• No safe or unsafe verdict, risk label or content classification is described (checked the FTA guide pages, FAQs, home page and portal pages; not stated) " + ND],
        "P7 optional (R020 ruling 1): a positive fact split from the absence")
    K.ins_after("CK3", 4, "Key sharing:",
        '• Key and salt protection: "Keys and salts are stored securely and never exposed to shared users" (Cloak Guide, Secrets Manager page) ' + DOC,
        "P7 optional: covers the 'salts' in the R4 Summary")
    K.summary_text("CK2", 5, "replaced, redacted, masked or otherwise transformed", "replaced or otherwise transformed",
                   "P7 optional: R5 Detail names no Redact or Mask for custom entities (38 words)")
    V.sub("f", "Presidio", "Licence", "; not re-read here", "", "P7 optional: process wording removed from a built cell")
    V.sub("d", "=Mask", "Parameters", "; neither is chosen here", "", "P7 optional: 'neither is chosen here' removed (main)")
    for key in ["Pseudonymise", "Encrypt"]:
        V.sub("d", key, "Covered by", " ; ", "; ", "P7 optional: separator spacing harmonised", kind="covered-by")
    V.sub("c", "Custom entity by LLM", "Notes", "[Beta Feature]: 1 entity", '"[Beta Feature]": 1 entity',
          "P7 optional: quoted so it does not read as a label form")
    K.sub("CK1", 4, "No self-hosting route",
          "GitHub searches of GovTechSG, govtech-responsibleai and opengovsg on 2026-10-10",
          "GitHub searches of GovTechSG, opengovsg, govtech-responsibleai and datagovsg on 2026-10-10",
          "P7 optional: the four organisations searched, as in CK2 R4 and CK3 R4")
    K.sub("CK1", 3, "The API Guide and OpenAPI pages redirect to the docs login page",
          "(HTTP 200 after redirect, observed 2026-10-10)", "(HTTP 302 then a 200 login page, observed 2026-10-10)",
          "P7 optional: HTTP wording aligned with the inventory")
    K.sub("CK2", 5, "API response format for custom entities",
          "HTTP 200 at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in",
          "HTTP 302 then a 200 login page at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in",
          "P7 optional: HTTP wording aligned with the inventory")
    K.sub("CK3", 5, "API response format for encrypt and decrypt",
          "HTTP 200 at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in",
          "HTTP 302 then a 200 login page at docs.developer.tech.gov.sg/auth/otp-login with reason not_logged_in",
          "P7 optional: HTTP wording aligned with the inventory")
    V.sub("b", "Sentinel integration (planned)", "Applies to",
          "PII detection and masking on Sentinel traffic; the Sentinel sheet column is GovTech Sentinel: PII detection and masking (AWS Bedrock) (sheet 3, column AF) [Inferred] (premise: the playbook lists Cloak under \"Detection tools\" for PII and shows the planned integration under the Sentinel tab)",
          "PII detection and masking on Sentinel traffic [Inferred] (premise: the playbook lists Cloak under \"Detection tools\" for PII and shows the planned integration under the Sentinel tab). Cross-reference: GovTech Sentinel: PII detection and masking (AWS Bedrock), sheet 3 column AF",
          "P7 optional: the workbook cross-reference separated from the Inferred fact")
