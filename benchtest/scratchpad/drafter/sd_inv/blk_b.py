from gen_common import *
import json
cat = {r["name"]: r for r in json.load(open("cat.json"))}
G = json.load(open("groups.json"))
HB = ["Group","Examples","Count or scope","Region availability","Image or text","Covered by Table 3 column","Source URL"]
def n(g): return len(G[g])
def avail(g):
    vs = collections = None
    import collections as c
    cnt = c.Counter(cat[x]["av"] for x in G[g])
    if list(cnt) == ["ANY_LOCATION"]:
        return f"ANY_LOCATION for all {n(g)} [Documented] (DOCS infotypes-reference, Availability column)"
    parts = [f"{v} infoTypes: {k}" for k, v in cnt.items()]
    return "; ".join(parts) + " [Documented] (DOCS infotypes-reference, Availability column)"
COUNT = " [Inferred] (my count of rows in the infoType categories table, grouped by my own rule)"
TXT = "Text; text infoTypes also run on images after text extraction [Documented] (DOCS infotypes-reference, Image-based infoTypes)"
LANG = "Country-specific infoTypes support English and the respective country's languages [Documented] (DOCS concepts-infotypes)"
def row(g, grp, ex, scope, imgtxt, covered, extra_urls=()):
    return [grp, ex + " [Documented] (DOCS infotypes-reference)", scope, avail(g), imgtxt, covered, urls("infotypes", *extra_urls)]
ROWS_B = []
ROWS_B.append(row("persons","Global person identifiers","PERSON_NAME, FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE_NUMBER, USER_NAME, DATE_OF_BIRTH",
 f"{n('persons')} infoTypes{COUNT}. PHONE_NUMBER is described only as a telephone number, with no country statement, so +65 numbers are [To be verified] (needs testing). PERSON_NAME, FIRST_NAME, LAST_NAME, FEMALE_NAME, MALE_NAME and DATE_OF_BIRTH each carry the note Not recommended for use during latency sensitive operations [Documented] (DOCS infotypes-reference). The concepts page lists the same infoTypes as ones that can make requests run much more slowly [Documented] (DOCS concepts-infotypes). The PERSON_NAME detector uses various technologies, including natural language understanding [Documented] (DOCS concepts-infotypes)",
 TXT, cov("SD1"), ("cinfo","relnotes")))
ROWS_B.append(row("places","Global places and organisations","STREET_ADDRESS, LOCATION, LOCATION_COORDINATES, GEOGRAPHIC_DATA, ORGANIZATION_NAME",
 f"{n('places')} infoTypes{COUNT}. STREET_ADDRESS, LOCATION and ORGANIZATION_NAME carry the note Not recommended for use during latency sensitive operations [Documented] (DOCS infotypes-reference). A Singapore-specific address infoType [Not disclosed] (checked the whole table; no such name)",
 TXT, cov("SD1")))
ROWS_B.append(row("net","Network, device and web identifiers","IP_ADDRESS, MAC_ADDRESS, IMEI_HARDWARE_ID, IMSI_ID, ICCID_NUMBER, ADVERTISING_ID, URL, DOMAIN_NAME, HTTP_USER_AGENT",
 f"{n('net')} infoTypes{COUNT}. 8 of the 12 rows show TELECOMMUNICATIONS in the Industry column [Inferred] (my count of the Industry column)",
 TXT, cov("SD1")))
ROWS_B.append(row("dates","Dates and times","DATE, TIME",
 f"{n('dates')} infoTypes{COUNT}. Dates of birth sit in the person identifier group above; DateShiftConfig and TimePartConfig work on date and time values [Documented] (DOCS transformations-reference)",
 TXT, cov("SD1"), ("transf",)))
ROWS_B.append(row("demo","Demographic and sensitive-attribute terms","AGE, GENDER, MARITAL_STATUS, ETHNIC_GROUP, SEXUAL_ORIENTATION, RELIGIOUS_TERM, POLITICAL_TERM, TRADE_UNION, CRIME_STATUS, IMMIGRATION_STATUS",
 f"{n('demo')} infoTypes{COUNT}. Term and attribute detectors rather than identifiers [Inferred] (premise: the descriptions refer to terms and statuses)",
 TXT, cov("SD1")))
ROWS_B.append(row("generic","Generic and global government IDs","PASSPORT, GOVERNMENT_ID, GENERIC_ID, DRIVERS_LICENSE_NUMBER, VAT_NUMBER, VEHICLE_IDENTIFICATION_NUMBER",
 f"{n('generic')} infoTypes{COUNT}. PASSPORT matches passport numbers for a list of countries that includes Singapore [Documented] (DOCS infotypes-reference). GENERIC_ID at a minimum likelihood below POSSIBLE might flag most numeric and alphanumeric entities [Documented] (DOCS concepts-infotypes)",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("fin","Financial (global)","CREDIT_CARD_NUMBER, CVV_NUMBER, FINANCIAL_ACCOUNT_NUMBER, IBAN_CODE, SWIFT_CODE, FINANCIAL_ID",
 f"{n('fin')} infoTypes{COUNT}",
 TXT, cov("SD1")))
ROWS_B.append(row("health","Health (global)","ICD10_CODE, ICD9_CODE, MEDICAL_RECORD_NUMBER, MEDICAL_ID, MEDICAL_TERM, BLOOD_TYPE",
 f"{n('health')} infoTypes{COUNT}. A MEDICAL_ID behaviour change took effect for InfoType.version latest, with the old behaviour on stable [Documented] (DOCS release-notes)",
 TXT, cov("SD1"), ("relnotes",)))
ROWS_B.append(row("cred","Credentials and secrets (global)","ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY, GCP_API_KEY, AWS_CREDENTIALS, AUTH_TOKEN, JSON_WEB_TOKEN, PASSWORD, ENCRYPTION_KEY",
 f"{n('cred')} infoTypes{COUNT}. ANTHROPIC_API_KEY is described as an API key used to authenticate requests to Anthropic APIs; OPENAI_API_KEY and GEMINI_API_KEY are listed alongside [Documented] (DOCS infotypes-reference). The three LLM-provider key detectors were made available in all regions on 2026-08-13 [Documented] (DOCS release-notes)",
 TXT, cov("SD1"), ("relnotes",)))
ROWS_B.append(row("Singapore","Singapore","SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER, SINGAPORE_PASSPORT",
 f"{n('Singapore')} infoTypes with location SINGAPORE{COUNT}. The NRIC description is A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card [Documented] (DOCS infotypes-reference). Coverage of the FIN format [To be verified] (needs testing). Singapore FIN, UEN, +65 phone and address infoTypes [Not disclosed] (checked every name in the table). {LANG}. Which languages count as Singapore's [Not disclosed] (checked the concepts page)",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("United States","United States","US_SOCIAL_SECURITY_NUMBER, US_DRIVERS_LICENSE_NUMBER, US_INDIVIDUAL_TAXPAYER_IDENTIFICATION_NUMBER, US_EMPLOYER_IDENTIFICATION_NUMBER, US_HEALTHCARE_NPI, US_BANK_ROUTING_MICR",
 f"{n('United States')} infoTypes with location UNITED_STATES{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("Canada","Canada","CANADA_SOCIAL_INSURANCE_NUMBER, CANADA_PASSPORT, CANADA_DRIVERS_LICENSE_NUMBER, CANADA_OHIP, CANADA_BC_PHN, CANADA_QUEBEC_HIN, CANADA_BANK_ACCOUNT",
 f"{n('Canada')} infoTypes with location CANADA{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("United Kingdom and Ireland","United Kingdom and Ireland","UK_NATIONAL_INSURANCE_NUMBER, UK_NATIONAL_HEALTH_SERVICE_NUMBER, UK_DRIVERS_LICENSE_NUMBER, IRELAND_PPSN, IRELAND_EIRCODE, SCOTLAND_COMMUNITY_HEALTH_INDEX_NUMBER",
 f"{n('United Kingdom and Ireland')} infoTypes with location UNITED_KINGDOM or IRELAND{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("Western and Southern Europe","Western and Southern Europe","FRANCE_NIR, FRANCE_PASSPORT, GERMANY_IDENTITY_CARD_NUMBER, SPAIN_NIF_NUMBER, ITALY_FISCAL_CODE, PORTUGAL_CDC_NUMBER, BELGIUM_NATIONAL_ID_CARD_NUMBER, AUSTRIA_SOCIAL_SECURITY_NUMBER",
 f"{n('Western and Southern Europe')} infoTypes with locations SPAIN, FRANCE, GERMANY, ITALY, PORTUGAL, AUSTRIA, BELGIUM, SWITZERLAND and THE_NETHERLANDS{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("Northern Europe","Northern Europe","DENMARK_CPR_NUMBER, FINLAND_NATIONAL_ID_NUMBER, NORWAY_NI_NUMBER, SWEDEN_NATIONAL_ID_NUMBER, SWEDEN_PASSPORT",
 f"{n('Northern Europe')} infoTypes with locations SWEDEN, FINLAND, NORWAY and DENMARK{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("Eastern Europe, Central Asia, Middle East and Africa","Eastern Europe, Central Asia, Middle East and Africa","POLAND_NATIONAL_ID_NUMBER, CZECHIA_PERSONAL_ID_NUMBER, ISRAEL_IDENTITY_CARD_NUMBER, KAZAKHSTAN_PASSPORT, SOUTH_AFRICA_ID_NUMBER, TURKEY_ID_NUMBER",
 f"{n('Eastern Europe, Central Asia, Middle East and Africa')} infoTypes with locations POLAND, CZECHIA, CROATIA, RUSSIA, UKRAINE, BELARUS, KAZAKHSTAN, ARMENIA, AZERBAIJAN, UZBEKISTAN, TURKEY, ISRAEL and SOUTH_AFRICA{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("East Asia","East Asia","KOREA_ARN, JAPAN_INDIVIDUAL_NUMBER, CHINA_RESIDENT_ID_NUMBER, TAIWAN_ID_NUMBER, HONG_KONG_ID_NUMBER, JAPAN_PASSPORT",
 f"{n('East Asia')} infoTypes with locations KOREA, JAPAN, CHINA, TAIWAN and HONG_KONG{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("South and Southeast Asia and Oceania (excluding Singapore)","South and Southeast Asia and Oceania (excluding Singapore)","INDIA_AADHAAR_INDIVIDUAL, INDIA_PAN_INDIVIDUAL, INDONESIA_NIK_NUMBER, THAILAND_NATIONAL_ID_NUMBER, AUSTRALIA_TAX_FILE_NUMBER, NEW_ZEALAND_NHI_NUMBER",
 f"{n('South and Southeast Asia and Oceania (excluding Singapore)')} infoTypes with locations INDIA, INDONESIA, THAILAND, AUSTRALIA and NEW_ZEALAND{COUNT}. No Malaysia infoType in the table [Not disclosed] (checked the Location column)",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("Latin America","Latin America","BRAZIL_CPF_NUMBER, MEXICO_CURP_NUMBER, ARGENTINA_DNI_NUMBER, CHILE_CDI_NUMBER, COLOMBIA_CDC_NUMBER, PARAGUAY_TAX_NUMBER",
 f"{n('Latin America')} infoTypes with locations MEXICO, BRAZIL, ARGENTINA, CHILE, COLOMBIA, PARAGUAY, PERU, URUGUAY and VENEZUELA{COUNT}. {LANG}",
 TXT, cov("SD1"), ("cinfo",)))
ROWS_B.append(row("doc context","Document context categories","DOCUMENT_TYPE/CONTEXT/FINANCE, DOCUMENT_TYPE/CONTEXT/HEALTH, DOCUMENT_TYPE/CONTEXT/LEGAL, DOCUMENT_TYPE/CONTEXT/OBSCENE, DOCUMENT_TYPE/CONTEXT/OFFENSIVE, DOCUMENT_TYPE/CONTEXT/POLITICS, DOCUMENT_TYPE/CONTEXT/RELIGION, DOCUMENT_TYPE/CONTEXT/SEXUAL",
 f"{n('doc context')} infoTypes{COUNT}. The docs say Sensitive Data Protection can classify documents into enterprise, sensitive and regulated content categories [Documented] (DOCS infotypes-reference, Documents). They are listed as limited-availability infoTypes that can cause scanning issues in unsupported regions [Documented] (DOCS infotypes-reference). Accuracy [Not disclosed] (checked the reference and likelihood pages)",
 TXT, cov("SD1"), ("likelihood",)))
ROWS_B.append(row("doc kinds","Document types by kind (legal, finance, HR, medical, R&D)","DOCUMENT_TYPE/LEGAL/BRIEF, DOCUMENT_TYPE/LEGAL/COURT_ORDER, DOCUMENT_TYPE/FINANCE/INVOICE, DOCUMENT_TYPE/FINANCE/SEC_FILING, DOCUMENT_TYPE/HR/RESUME, DOCUMENT_TYPE/MEDICAL/RECORD, DOCUMENT_TYPE/R&D/PATENT, DOCUMENT_TYPE/R&D/SYSTEM_LOG",
 f"{n('doc kinds')} infoTypes (5 legal, 3 finance, 1 HR, 1 medical, 3 R&D other than source code){COUNT}. DOCUMENT_TYPE/FINANCE/INVOICE and DOCUMENT_TYPE/MEDICAL/RECORD are limited-availability infoTypes [Documented] (DOCS infotypes-reference)",
 TXT, cov("SD1")))
ROWS_B.append(row("source code","Source code document types","DOCUMENT_TYPE/R&D/SOURCE_CODE, DOCUMENT_TYPE/R&D/SOURCE_CODE/PYTHON, DOCUMENT_TYPE/R&D/SOURCE_CODE/JAVASCRIPT, DOCUMENT_TYPE/R&D/SOURCE_CODE/SQL, DOCUMENT_TYPE/R&D/SOURCE_CODE/SHELL",
 f"{n('source code')} infoTypes (one general plus 15 language-specific){COUNT}. Relevant to code in prompts and tool output [Inferred] (premise: code appears in LLM traffic)",
 TXT, cov("SD1")))
ROWS_B.append(row("image object","Image object detectors","OBJECT_TYPE/PERSON/FACE, OBJECT_TYPE/PERSON/PASSPORT, OBJECT_TYPE/PERSON/PHOTO_ID_CARD, OBJECT_TYPE/PERSON/SIGNATURE, OBJECT_TYPE/LICENSE_PLATE, OBJECT_TYPE/BARCODE, OBJECT_TYPE/WHITEBOARD, OBJECT_TYPE/PERSON",
 f"{n('image object')} infoTypes{COUNT}. OBJECT_TYPE/PERSON/FACE is marked as in Preview [Documented] (DOCS infotypes-reference). These detectors analyse image pixels and features directly [Documented] (DOCS infotypes-reference, Image-based infoTypes)",
 "Image (pixels and features) [Documented] (DOCS infotypes-reference, Image-based infoTypes)", cov("SD5"), ("cimg",)))
ROWS_B.append(row("image context","Image context (safety) detectors","IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT, IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE, IMAGE_TYPE/CONTEXT/VIOLENCE",
 f"{n('image context')} infoTypes{COUNT}. The reference says they analyse an entire image for sensitive or harmful subject matter [Documented] (DOCS infotypes-reference). Accuracy and the model behind them [Not disclosed] (checked the reference, concepts-image-redaction and release-notes pages)",
 "Image, whole-image classification [Documented] (DOCS infotypes-reference, DOCS concepts-image-redaction)", cov("SD6"), ("cimg","relnotes")))
assert len(ROWS_B)==24, len(ROWS_B)
assert sum(len(v) for v in G.values())==261
