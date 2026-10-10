# -*- coding: utf-8 -*-
from gen_a import *

ON = "On [Inferred] (premise P-ON)"


def block_c():
    h = "| Entity tag | Group | Default state | Method as documented | Notes and limits | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|---|---|"]

    def base(tag, grp, default, method, notes, cov, keys):
        out.append(row([tag, grp, default, method, notes, cov], keys))

    NOM = "Method not named on the entity page [Not disclosed] (checked the {p} page; the ENTI page gives only the general statement quoted in the block note)"
    base("PERSON", "Personal (Name)",
         "REPLACE with <PERSON> [Documented] (NAME: \"REPLACE names with <PERSON> tag\"). " + ON,
         NOM.format(p="NAME"),
         "\"Name refers to a person's Name (First, Last or Full Name), including ethnic names in roman characters.\" [Documented] (NAME). Names in non-roman scripts and other languages [Not disclosed] (checked NAME and ENTI). Alias technique is available for this tag only [Documented] (ALIAS)",
         CK1, "NAME ENTI ALIAS")
    base("SG_NRIC_FIN", "Personal (NRIC (SG))",
         "REPLACE with <SG_NRIC_FIN> [Documented] (NRIC: \"REPLACE NRIC with <SG_NRIC_FIN> tag\"). " + ON,
         "\"Validation disabled: Both real and fake NRIC numbers following the format @xxxxxxx# — where @ is \"S\", \"T\", \"F\", \"G\" or \"M\" (depending on the status of the holder) are detected.\" [Documented] (NRIC)",
         "Covers S and T (citizens and permanent residents) and F, G and M (long-term pass holders) [Documented] (NRIC). The FAQ lists \"checksum\" among the parameters to tune \"for NRIC/UEN\" and says to enable checksum validation to reject matches that fail mathematical validation [Documented] (FAQ); the control that enables it [Not disclosed] (checked NRIC, USE, CONF)",
         CK1, "NRIC FAQ")
    base("EMAIL_ADDRESS", "Personal (Email Address)",
         "REPLACE with <EMAIL_ADDRESS> [Documented] (EMAIL: \"REPLACE email addresses with <EMAIL_ADDRESS> tag\"). " + ON,
         NOM.format(p="EMAIL"),
         "Two examples only, no format limits stated [Documented] (EMAIL). Email is one of the key PIIs in the vendor's \">97% recall\" claim, with no method published [Documented] (HOME)",
         CK1, "EMAIL HOME")
    base("PHONE_NUMBER", "Personal (Phone Number)",
         "REPLACE with <PHONE_NUMBER> [Documented] (PHONE: \"REPLACE all phone numbers with <PHONE_NUMBER> tag\"). " + ON,
         "\"Global coverage disabled: Only Singapore numbers are detected by default.\" [Documented] (PHONE). \"Validation check is not included. Both real and fake phone numbers may be detected.\" [Documented] (PHONE)",
         "The same page's example replaces a non-Singapore number, \"+91 7513200000\" [Documented] (PHONE). The control for global coverage [Not disclosed] (the FAQ names \"global detection (for phone numbers)\" as a parameter; checked PHONE and USE for where it is set). \"Phone numbers (especially non-Singapore numbers) may sometimes be falsely detected as bank account numbers, or other numeric-type data fields.\" [Documented] (PHONE)",
         CK1, "PHONE FAQ")
    base("NRP", "Personal (Nationality/Race/Religion)",
         "REPLACE with <NRP> [Documented] (NRPG: \"REPLACE all NRP values with <NRP> tag\"). " + ON,
         NOM.format(p="NRPG"),
         "\"NRP detects values that correspond to a Nationality (e.g. Singaporean), Race (e.g. Chinese), Religion (e.g. Christian) and political groups.\" [Documented] (NRPG).",
         CK1, "NRPG")
    base("SG_ADDRESS", "Personal (Address (SG))",
         "On [Documented] (ADDR table: Default ON). REPLACE with <SG_ADDRESS> [Documented] (ADDR)",
         "Pattern matching [Documented] (ADDR table, column Method)",
         "\"Full Singapore addresses (street + postal code + unit number together)\" [Documented] (ADDR). \"Cloak provides 4 address-related recognisers for Singapore addresses\" [Documented] (ADDR)",
         CK1, "ADDR")
    base("SG_ADDRESS_POSTAL_CODE", "Personal (Address (SG))",
         "On [Documented] (ADDR table: Default ON). REPLACE with <SG_ADDRESS_POSTAL_CODE> [Documented] (ADDR)",
         "Regex [Documented] (ADDR table, column Method)",
         "\"6-digit Singapore postal codes (e.g. 520123)\" [Documented] (ADDR). \"Overridden if Full Address detection is enabled.\" [Documented] (ADDR). \"We are improving our algorithm to improve accuracy for this field.\" [Documented] (ADDR)",
         CK1, "ADDR")
    base("SG_ADDRESS_UNIT_NUMBER", "Personal (Address (SG))",
         "On [Documented] (ADDR table: Default ON). REPLACE with <SG_ADDRESS_UNIT_NUMBER> [Documented] (ADDR)",
         "Regex [Documented] (ADDR table, column Method)",
         "\"Unit/floor numbers (e.g. #05-123, Blk 123)\" [Documented] (ADDR). \"Overridden if Full Address detection is enabled.\" [Documented] (ADDR)",
         CK1, "ADDR")
    base("SG_ADDRESS_STREET", "Personal (Address (SG))",
         "Off [Documented] (ADDR table: \"OFF (advanced)\"; \"Enable in Anonymisation Settings under advanced entities\"). REPLACE with <SG_ADDRESS_STREET> when enabled [Documented] (ADDR)",
         "Pattern matching [Documented] (ADDR table, column Method)",
         "\"Street names alone (e.g. \"Bukit Timah Road\")\" [Documented] (ADDR). Off by default because street names \"have higher false-positive rates\" [Documented] (ADDR)",
         CK1, "ADDR")
    base("LOCATION", "Personal (Location)",
         "REPLACE with <LOCATION> [Documented] (LOCN: \"REPLACE location names with <LOCATION> tag\"). " + ON,
         NOM.format(p="LOCN"),
         "\"Countries, cities, states, and other named geographical locations (mountains, bodies of water, regions).\" [Documented] (LOCN). Inclusion lists can add terms such as \"BMTC School\" to this entity [Documented] (INCL)",
         CK1, "LOCN INCL")
    base("SG_PASSPORT", "Personal (Passport (SG))",
         "REPLACE with <SG_PASSPORT> [Documented] (PASS: \"REPLACE all Singapore passport numbers with the <SG_PASSPORT> tag\"). " + ON,
         NOM.format(p="PASS"),
         "\"Detects Singapore passport numbers.\" [Documented] (PASS). Non-Singapore passport numbers [Not disclosed] (checked PASS and ENTI; no international passport entity in the group list)",
         CK1, "PASS ENTI")
    base("CURRENCY", "Financial (Currency)",
         "REPLACE with <CURRENCY> [Documented] (CURR). " + ON,
         "Rule on symbols: \"REPLACE values with a symbol or a 3-char symbol before or after the digits with <CURRENCY> tag.\" [Documented] (CURR)",
         "Examples \"$5000 USD\" and \"¥500,000\" [Documented] (CURR)",
         CK1, "CURR")
    base("CREDIT_CARD", "Financial (Credit Card)",
         "REPLACE with <CREDIT_CARD> [Documented] (CARD: \"REPLACE credit card numbers with a <CREDIT_CARD> tag\"). " + ON,
         NOM.format(p="CARD"),
         "Examples with dashes and without [Documented] (CARD). Checksum validation [Not disclosed] (checked CARD and ENTI; ENTI says \"Validation using checksums (if applicable)\" in general)",
         CK1, "CARD ENTI")
    base("SG_BANK_ACCOUNT_NUMBER", "Financial (Bank Account Number (SG))",
         "REPLACE with <SG_BANK_ACCOUNT_NUMBER> [Documented] (SGBK). " + ON,
         "\"Detects Singapore bank account numbers based on common formats and patterns\" [Documented] (SGBK)",
         "\"Phone numbers (especially non-SG numbers) may sometimes be falsely detected as bank account numbers, or other numeric-type data fields.\" [Documented] (SGBK). The STRC page uses a 10-digit hospital case number detected as a bank account number as its worked example [Documented] (STRC)",
         CK1, "SGBK STRC")
    base("IBAN_CODE", "Financial (Bank Account Number (IBAN))",
         "REPLACE with <IBAN_CODE> [Documented] (IBAN). " + ON,
         "\"Detects international bank account numbers based on the official IBAN calculator\" [Documented] (IBAN)",
         "Examples: one GB IBAN [Documented] (IBAN)",
         CK1, "IBAN")
    base("IP_ADDRESS", "Technical Security (IP Address)",
         "REPLACE with <IP_ADDRESS> [Documented] (IPAD: \"REPLACE IPv4 or IPv6 IP addresses with a <IP_ADDRESS> tag\"). " + ON,
         NOM.format(p="IPAD"),
         "\"Currently, the FTA tool does not support CIDR Block notation.\" [Documented] (IPAD). Covers IPv4 and IPv6 [Documented] (IPAD)",
         CK1, "IPAD")
    base("URL", "Technical Security (URL)",
         "REPLACE with <URL> [Documented] (URLE: \"REPLACE URLs and web addresses with a <URL> tag\"). " + ON,
         NOM.format(p="URLE"),
         "Examples include a bare domain, \"jasoncjw.me\", and a full https URL [Documented] (URLE)",
         CK1, "URLE")
    base("DATE_TIME", "Others (Date & Time)",
         "REPLACE with <DATE_TIME> [Documented] (DATE: \"REPLACE dates and times with a <DATE_TIME> tag\"). " + ON,
         NOM.format(p="DATE"),
         "Examples \"1800 GMT+8\" and \"22 January 1997, 10:25AM\" [Documented] (DATE). A sample LLM entity named DATE_TIME_SPECIFIC exists for narrower date expressions: \"User wants to anonymise specific date and/or time expressions, but not other temporal references.\" [Documented] (SAMPD)",
         CK1, "DATE SAMPD")
    base("SG_UEN", "Others (UEN (SG))",
         "REPLACE with <SG_UEN> [Documented] (UENP: \"REPLACE UENs with the <SG_UEN> tag\"). " + ON,
         "\"Validation disabled: Both real and fake UEN numbers following the formats below are detected.\" [Documented] (UENP)",
         "Three formats: 8 digits then a letter, 9 digits then a letter, and a T, S or R prefix pattern [Documented] (UENP). Checksum control [Not disclosed] (checked UENP, USE, CONF; the FAQ mentions checksum validation for NRIC and UEN)",
         CK1, "UENP FAQ")
    base("ORGANIZATION", "Others (Organization)",
         "REPLACE with <ORGANIZATION> [Documented] (ORGN: \"REPLACE all organisation names with the <ORGANIZATION> tag\"). " + ON,
         NOM.format(p="ORGN"),
         "\"Detects names of companies, government bodies, and public organisations.\" [Documented] (ORGN). Added in v2.1.0: \"[FTA] Added the ORGANIZATION entity type\" [Documented] (REL)",
         CK1, "ORGN REL")
    base("Exceptions (allow list)", "Others (Exceptions)",
         "Off until words are added [Inferred] (premise: the EXCP page describes keying in words to ignore)",
         "Manual exclusion list: \"Exceptions are used to manually exclude words from being detected and anonymised.\" [Documented] (EXCP)",
         "Set at the bottom of the Transform drawer [Documented] (EXCP). The API parameter is allow_list: \"allows a list of text to be excluded from detection\" [Documented] (REL, v2.0.5). Matching rules (case, exactness, size limit) [Not disclosed] (checked EXCP, FAQ, REL)",
         CK1, "EXCP REL FAQ")
    base("Inclusion list on an existing entity", "Advanced feature",
         "Off until words are added [Inferred] (premise: the INCL page describes an optional \"Inclusion (optional)\" section)",
         "Fixed word matching: \"specify additional words or phrases that should be detected and anonymised under an existing entity type\" [Documented] (INCL)",
         "\"Word-sensitive\" (exact spelling and punctuation) and \"Not case-sensitive\" [Documented] (INCL). \"Only the first 500 words in a CSV upload will be used.\" [Documented] (INCL)",
         CK2, "INCL USE")
    base("Custom entity by fixed list", "Custom",
         "Not present until the user adds it [Inferred] (premise: created in the Custom entities tab)",
         "Created with the \"Pattern-matching based\" approach, then words are uploaded through the Inclusion feature [Documented] (FIXD). Match is exact: \"exact-match detection for specific words or phrases\" [Documented] (FIXD)",
         "\"The CSV to be uploaded should contain a maximum of 500 words listed in the first column.\" [Documented] (FIXD). Word-sensitive, not case-sensitive, \"Only the first 500 words in the CSV will be used.\" [Documented] (FIXD)",
         CK2, "FIXD INCL")
    base("Custom entity by regex", "Custom",
         "Not present until the user adds it [Inferred] (premise: created in the Custom entities tab)",
         "\"These entities utilise regular expressions to recognise and anonymise data based on the patterns you configure.\" [Documented] (STRC)",
         "Release v2.1.5: \"[FTA] Regex custom entities\" [Documented] (REL). API-only settings: context words that \"must appear near a regex match\" and \"different confidence scores for each regex pattern\" [Documented] (STRC; the API guide is behind a login). Regex engine and flavour [Not disclosed] (checked STRC, CUST)",
         CK2, "STRC CUST REL")
    base("Custom entity by LLM (Beta)", "Custom",
         "Not present until the user adds it [Inferred] (premise: created in the Custom entities tab)",
         "\"few-shot prompting, which allows the LLM to detect new entities without fine-tuning\" with \"a small set of 3-5 examples\" [Documented] (LLMI)",
         "[Beta Feature]: 1 entity per dataset, up to 5,000 documents, processing \"up to 8 hours\" [Documented] (LLMI). The FAQ says the Web UI \"normally allows one LLM-enabled custom entity per project\" [Documented] (FAQ). Sample entities DISEASE, DATE_TIME_SPECIFIC and PERSON_NAME [Documented] (SIDE, PRMP)",
         CK2, "LLMI ADDE PRMP FAQ SIDE")
    base("Dates of birth; vehicle plate numbers (no tag named)", "Named on Developer Portal pages only",
         "Not stated [Not disclosed] (checked ENTI, the entity pages in the sidebar, USE)",
         "Not stated [Not disclosed] (checked the same pages)",
         "PF: \"Auto-detection of 20+ entity types including names, NRICs, phone numbers, addresses, emails, dates of birth, bank accounts, and more\" [Documented]. PFAQ: \"Cloak detects 17+ entity types out of the box, including: names, NRICs/FINs, phone numbers, emails, addresses (Singapore-specific), dates of birth, bank account numbers, credit card numbers, UENs, vehicle plate numbers, passport numbers, and more\" [Documented]. The DATE_TIME_SPECIFIC LLM sample caption mentions \"how a date of birth is identified within an address block\" [Documented] (SAMPD). No entity page for either in the Cloak Guide [Not disclosed] (checked the sidebar). Whether DATE_TIME covers dates of birth and whether any recogniser covers vehicle plates [To be verified]",
         CK1, "PF PFAQ ENTI SIDE SAMPD")
    return "\n".join(out)


def block_d():
    h = "| Technique | Behaviour | Reversible | Parameters and limits | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|---|"]

    def base(*cells, keys):
        out.append(row(list(cells), keys))

    base("Replace",
         "\"Replace identified token with a word or tag of your choice\" [Documented] (REPL). \"By default, it would be <ENTITY_NAME>\" [Documented] (REPL). It is the default technique for every entity [Documented] (USE: \"Replaces them with their data type as the default anonymisation technique\")",
         "No [Inferred] (premise: the REPL page describes replacement by a tag or word and mentions no key, mapping or restore step)",
         "The replacement value is user-entered; default <ENTITY_NAME> [Documented] (REPL). All instances of an entity type share one placeholder [Documented] (RUNQ: standard Replace \"uses the same placeholder for all entities of a given type\")",
         CK1, keys="REPL USE RUNQ")
    base("Replace (Unique)",
         "\"assigns a distinct numbered placeholder to each unique entity value\", for example <PERSON_1> and <PERSON_2> [Documented] (RUNQ). Matching is on the detected value: \"Jane Huang\" and \"Jane\" get different placeholders [Documented] (RUNQ)",
         "Not stated [Not disclosed] (checked RUNQ: it describes consistent numbered placeholders, and the API route mentions a mapping table you maintain, with no restore step described)",
         "Web App only, single CSV uploads only, baseline entities only, not PDF, DOCX, multi-file or custom entities; \"up to two entity types per anonymisation job\" [Documented] (RUNQ). Pasted text [Not disclosed] (not listed as available or unavailable on RUNQ). Slower than standard Replace [Documented] (RUNQ). API route: \"Cloak's /analyze endpoint and a mapping table you maintain\" [Documented] (RUNQ)",
         CK1, keys="RUNQ")
    base("Redact",
         "\"Remove all words associated with the entity type completely. Detected entities will be replaced with a blank.\" [Documented] (REDA)",
         "No [Inferred] (premise: the REDA page says the words are removed and gives no key or mapping)",
         "No parameters listed [Not disclosed] (checked the REDA page)",
         CK1, keys="REDA")
    base("Mask",
         "\"Masking hides characters of a data value, e.g. by using a constant symbol (e.g. * or x)\" [Documented] (MASK)",
         "No [Inferred] (premise: the MASK page describes hiding characters and gives no key or mapping)",
         "Defaults: Number of Characters 3, Masking Type Suffix, Masking Character - [Documented] (MASK). Definition: \"Suffix: masks the starting characters\" and \"Prefix: masks the ending characters\" [Documented] (MASK). The same page's example that keeps the first three digits of 120414 and masks the rest is labelled \"Transforms into a suffix masked value\", which reads the other way [Documented] (MASK; wording conflict inside one page)",
         CK1, keys="MASK")
    base("NRIC masking",
         "A special masking for the NRIC entity only: \"FTA currently supports general Masking and special NRIC Masking (for NRIC entity types only)\" [Documented] (MASK). The page says \"agencies are no longer allowed to used masked / partial NRICs\" under SNG (PMO) Circular Minute No. 4/2024 [Documented] (NRMK)",
         "Not stated [Not disclosed] (checked NRMK, which gives no mechanics)",
         "No parameters listed [Not disclosed] (checked NRMK). Recommends \"Encryption / Pseudoanonymisation instead\" [Documented] (NRMK)",
         CK1, keys="NRMK MASK NRIC")
    base("Alias (PERSON only)",
         "Swaps a name for another while keeping its cultural context: \"maintaining the integrity of its cultural/ethnic context\" and useful for \"LLM prompts\" that need \"Context and Consistency of names in free text\" [Documented] (ALIAS)",
         "Not stated [Not disclosed] (checked ALIAS: no key or mapping described)",
         "\"Alias is only available for the PERSON entity type.\" [Documented] (ALIAS). Options Context (default On; when disabled \"the altered name will return a western name\") and Offset (default On; when disabled the name \"will consistently return a constant value\") [Documented] (ALIAS). Examples cover Malay, Indian and Chinese names [Documented] (ALIAS)",
         CK1, keys="ALIAS")
    base("Pseudonymise (SHA-256 or SHA-512 with a salt)",
         "\"replacing them with cryptographically generated values (pseudonyms)\" by \"irreversible hashing (SHA-256) or (SHA-512) with a random salt\" [Documented] (PSEU)",
         "No: \"irreversible\" [Documented] (PSEU)",
         "Persistent only with the same salt: \"conditioned on using the same salt value for the datasets\" [Documented] (PSEU). The page advises storing the salt in the Secrets Manager and sharing it [Documented] (PSEU). Page text \"Custom salt values will be included in the future\" [Documented] (PSEU). Release v2.1.0 \"Added salt parameter for Pseudonymisation transformation\" and v2.1.4 \"Support for custom salts and user managed salts\" [Documented] (REL); the two official sources conflict on whether custom salts exist; the page wording is probably stale [Inferred] (premise: both statements sit on official pages and cannot both describe the current release). Example output is a 64-character hexadecimal string [Documented] (PSEU)",
         CK1 + " ; " + CK3, keys="PSEU REL SECR")
    base("Encrypt (AES-256 CBC)",
         "Encrypts the detected value with a user-supplied key: \"The encryption uses AES cypher in CBC mode and requires a cryptographic key as an input for both encryption and decryption.\" [Documented] (ENCR). \"The output would be in base64.\" [Documented] (ENCR)",
         "Yes, with the key: the same page says the key is needed \"for both encryption and decryption\" [Documented] (ENCR)",
         "\"we have restricted encryption to only AES-256 CBC Mode Encryption\" [Documented] (ENCR). Keys and salts can be managed and shared through the Secrets Manager, and \"user managed secret keys\" arrived in v2.1.4 [Documented] (SECR, REL). The ENCR page names Presidio's built-in encryption and links its tutorial, which returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC)",
         CK1 + " ; " + CK3, keys="ENCR SECR REL PRESENC")
    base("Decrypt (free text, Web UI one value at a time; API)",
         "Reverses Encrypt: input the encrypted value, select the secret, obtain the decrypted value [Documented] (FTDC). Use is audited as the activity \"Decrypt Free Text\" [Documented] (SECR)",
         "Applies to values from Encrypt only [Inferred] (premise: FTDC says to \"Select your secret\", and the Pseudonymise page calls hashing irreversible)",
         "\"The Web UI currently supports decrypting one value at a time\"; the API route loops through CSV rows [Documented] (FTDC). The secret holder can share it with \"up to 10 other users per operation, and with a maximum of 50 users per secret\" [Documented] (SECR). API request format for decryption [Not disclosed] (the helper script page is behind a login)",
         CK1 + " ; " + CK3, keys="FTDC SECR")
    return "\n".join(out)
