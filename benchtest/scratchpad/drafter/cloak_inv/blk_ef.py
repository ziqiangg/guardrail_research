# -*- coding: utf-8 -*-
from gen_a import *

T = "Terms of Use (TERMS)"


def block_e():
    h = "| Item | Value | Applies to | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|"]

    def base(item, value, applies, cov, keys):
        out.append(row([item, value, applies, cov], keys))

    base("Pasted text length",
         "\"Maximum 20,000 characters (approx. 3,000 words) per submission.\" [Documented] (USE)",
         "FTA text input in the Web UI [Documented] (USE). Limit for text sent through the API [Not disclosed] (checked USE, APIG, FAQ; the API guide is behind a login)",
         CK1, "USE")
    base("CSV file size",
         "\"Maximum 500 MB per file.\" [Documented] (USE). \"CSV files can only be uploaded together with other CSV files (not combined with PDF or DOCX).\" [Documented] (USE)",
         "FTA file upload. Users on COMET/GSIB devices \"may be blocked by SIS/Menlo for uploads exceeding 500 MB\" [Documented] (USE). Earlier release limit v2.0.3: \"Maximum 10 columns\" and \"up to 100k rows * 10 columns per CSV file\" [Documented] (REL); the current usage guide is the later statement and gives no column limit for FTA CSV [Inferred] (premise: the usage guide and FAQ state the current limits, the release note is dated 15 January 2024)",
         CK1, "USE REL FAQ")
    base("PDF and DOCX file size",
         "\"Maximum 200 MB per file.\" [Documented] (USE). \"PDF and DOCX files can be combined in the same upload.\" [Documented] (USE)",
         "FTA file upload [Documented] (USE, FAQ)",
         CK1, "USE FAQ")
    base("Files per project and total upload",
         "\"Up to 100 files per project, with a total upload limit of 2 GB.\" [Documented] (USE)",
         "FTA file upload [Documented] (USE, FAQ)",
         CK1, "USE FAQ")
    base("Content not processed",
         "\"Cloak does not process scanned PDFs, screenshots, images or engineering drawings. Such content requires an approved OCR or text-extraction step before anonymisation.\" [Documented] (FAQ). For .docx: \"Texts within images will not be detected as text.\" [Documented] (USE)",
         "FTA [Documented] (FAQ, USE)",
         CK1, "FAQ USE")
    base("PDF input types and output",
         "Native PDF gives .docx, searchable PDF gives .csv, scanned PDF gives \"Failed Upload\" [Documented] (USE). The FAQ table lists scanned PDF as \"Not supported\" [Documented] (FAQ)",
         "FTA file upload [Documented] (USE, FAQ)",
         CK1, "USE FAQ")
    base("Preview limits and processing time",
         "\"CSV preview shows first cell only.\" \"PDF preview shows first page only.\" \"Word preview shows first 200 words only.\" [Documented] (USE). CSV estimates: 20 rows by 1 column \"1 minute\", 5000 rows by 1 column \"4 hours\" [Documented] (USE). \"Text and PDF projects typically have a fast processing time\" [Documented] (USE)",
         "FTA Web UI. A processing time for a short prompt through the API [Not disclosed] (checked USE, APIG, PF, FAQ)",
         CK1, "USE")
    base("LLM-enabled custom entity limits",
         "\"only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)\" and \"may increase processing times to up to 8 hours\" [Documented] (LLMI). The vendor suggests iterating on \"<100 documents, which should take <20min\" [Documented] (PRMP)",
         "LLM custom entities, Beta [Documented] (LLMI)",
         CK2, "LLMI PRMP")
    base("Inclusion and fixed-list size",
         "\"Only the first 500 words in a CSV upload will be used.\" [Documented] (INCL). \"The CSV to be uploaded should contain a maximum of 500 words listed in the first column.\" [Documented] (FIXD)",
         "Inclusion lists and fixed-list custom entities [Documented] (INCL, FIXD)",
         CK2, "INCL FIXD")
    base("Confidence level",
         "Slider \"set to the default value of 0.30\" [Documented] (CONF, image caption). The usage guide caption: \"adjustment of the detection threshold from 0 to 1\" [Documented] (USE). \"Entities below the specified threshold will not be anonymised\" [Documented] (CONF)",
         "FTA Web UI. The default rests on an image caption, not on body text [Documented] (CONF). Per-entity or global scope of the threshold [Not disclosed] (the PF page says \"per entity type\", the CONF page describes one slider; checked both)",
         CK1, "CONF USE PF")
    base("Replace (Unique) limits",
         "Web App only, single CSV uploads only, baseline entities only; not PDF, DOCX, multi-file or custom entities; \"up to two entity types\" per job [Documented] (RUNQ). Pasted text [Not disclosed] (RUNQ lists neither available nor unavailable)",
         "Replace (Unique) technique, see block (d) [Documented] (RUNQ)",
         CK1, "RUNQ")
    base("Data retention",
         "\"Cloak does not retain data. Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request.\" [Documented] (FAQ). Portal wording: \"anonymised data is kept for up to 24 hours or removed upon user request\" [Documented] (PFAQ)",
         "Whole service, as described for jobs [Documented] (FAQ). Decrypted tabular downloads are \"available for up to 24 hours from the job creation time\" [Documented] (TABD). Retention of API calls [Not disclosed] (checked FAQ, PFAQ, PRIV; the API guide is behind a login)",
         ALL3, "FAQ PFAQ TABD PRIV")
    base("Data-classification ceiling",
         "FAQ: \"up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)\" [Documented] (FAQ). Terms Schedule 4.6: \"You shall not upload any information, data and material that are classified above the following classifications: Confidential (Cloud-Eligible) \\ Sensitive (High)\" [Documented] (TERMS, 15 pages read with pypdf)",
         "Whole service [Documented] (FAQ, TERMS). The tabular usage guide gives the same wording [Documented] (TABU)",
         ALL3, "FAQ TERMS TABU")
    base("Pricing",
         "\"Cloak is currently free for all approved users. Pricing for cost recovery may be introduced in future financial years, in line with standard GovTech product policy. For FY26, there is no charge.\" [Documented] (HOME)",
         "Whole service [Documented] (HOME, FAQ, PFAQ)",
         ALL3, "HOME FAQ PFAQ")
    base("Scheduled maintenance",
         "\"Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period.\" [Documented] (SITE, banner observed 2026-10-10)",
         "Web UI jobs. Effect on the API [Not disclosed] (checked SITE, APIG, FAQ)",
         ALL3, "SITE")
    base("Terms clause 1.1 (scope of the Service)",
         "\"These Terms of Use govern your access to and use of our services including the application ... its contents (including APIs, if any)\" [Documented] (TERMS, clause 1.1)",
         "Whole service, Web UI and APIs [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms clause 3.3 (non-public-sector use)",
         "\"In relation to entities that are not Public Sector Entities, your use and access of the Service is restricted solely for such purpose that GovTech has consented to in writing (including via email) ('Purpose').\" [Documented] (TERMS, clause 3.3). \"Any change in the Purpose shall be subject to the GovTech's prior written consent (including via email).\" [Documented] (TERMS, clause 3.3)",
         "Users that are not Public Sector Entities [Documented] (TERMS). The FAQ restates it for NGE users: \"they must have agreed with the Cloak team on the purpose of use prior to access\" [Documented] (FAQ)",
         ALL3, "TERMS FAQ")
    base("Terms clause 3.4.7 (benchmarking)",
         "\"3.4. You shall not, and shall not authorise or permit any third party to: ... 3.4.7. perform any benchmarking tests or analyses of the Service;\" [Documented] (TERMS, clause 3.4)",
         "Whole service [Documented] (TERMS). Whether a comparison run by an approved user is within this clause [Not disclosed] (the Terms define no benchmarking term; checked the full 15 pages)",
         ALL3, "TERMS")
    base("Terms clauses 3.4.9 and 3.4.11 (keys and third-party access)",
         "\"3.4.9. transfer assign or permit the sharing of license keys to or with a third party;\" and \"3.4.11. provide third party access to the Service;\" [Documented] (TERMS, clause 3.4)",
         "Whole service [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms clauses 3.4.6, 3.4.10 and 3.7 (other use limits)",
         "\"3.4.6. make the Service available in or through a network, file-sharing service, service bureau or any similar timesharing arrangement or as a managed service provider;\" [Documented] (TERMS). \"3.4.10. use the Service to process or permit to be processed any code of a third party;\" [Documented] (TERMS). \"3.7. You will not interfere or attempt to interfere with the proper working of the Service or otherwise do anything that imposes an unreasonable or disproportionately large load on GovTech's servers.\" [Documented] (TERMS)",
         "Whole service [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms Schedule 2.2 (use on behalf of an Agency)",
         "\"You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency.\" [Documented] (TERMS, Schedule 2.2). \"Notwithstanding this, the Terms of Use bind you individually and you will be personally responsible for use of this Service.\" [Documented] (TERMS, Schedule 2.2)",
         "Whole service [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms clause 9.1 (as is)",
         "\"The Service is provided on an 'as is' and 'as available' basis without warranties of any kind.\" [Documented] (TERMS, clause 9.1)",
         "Whole service. Clause 9.1.1 disclaims warranties \"as to the accuracy, completeness, correctness\" of the Service [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms clause 15 (governing law and disputes)",
         "\"These Terms of Use shall be governed by and construed in accordance with laws of Singapore.\" [Documented] (TERMS, clause 15.1). \"GovTech may, at its sole discretion, refer any dispute referred to in clause 14.2 above to arbitration administered by the Singapore International Arbitration Centre ('SIAC') in Singapore\" [Documented] (TERMS, clause 15.3). Courts: \"the exclusive jurisdiction of the Courts of the Republic of Singapore\" [Documented] (TERMS, clause 15.2)",
         "Whole service. The clause cross-references say clause 14.2 and 14.3, while the numbering in the PDF is 15.2 and 15.3 [Documented] (TERMS)",
         ALL3, "TERMS")
    base("Terms and Privacy Statement dates and links",
         "\"These Terms of Use are dated 24 July 2024.\" [Documented] (TERMS). \"This version of the Privacy Statement is dated 1 December 2022.\" [Documented] (PRIV, 4 pages read with pypdf). Privacy Annex: \"Dataset uploaded by user for purposes of data anonymisation/transformation.\" [Documented] (PRIV)",
         "Whole service. The FAQ links the Terms at https://www.cloak.gov.sg/terms, HTTP 404 observed 2026-10-10; go.gov.sg/cloak-terms redirects (HTTP 302) to file.go.gov.sg/cloak-terms.pdf [Documented] (FAQ, TERMS)",
         ALL3, "TERMS PRIV FAQ")
    base("Tabular file limits",
         "\"up to 100 data fields (i.e. columns) in CSV or XLSX format, up to 2 GB per file\" [Documented] (TABU). The FAQ gives the same figures with \"no limit on rows\" [Documented] (FAQ)",
         "Tabular anonymisation only. Release v2.0.0 gave \"max at 100\" columns on selection [Documented] (REL)",
         INV, "TABU FAQ REL")
    return "\n".join(out)


def block_f():
    h = "| Component | Owner | Where a Cloak page names it | Licence or ownership page (owner's, not GovTech docs) | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|---|"]

    def base(*cells, keys):
        out.append(row(list(cells), keys))

    base("spaCy",
         "Explosion (ExplosionAI GmbH) [Documented] (spaCy LICENSE: \"Copyright (C) 2016-2024 ExplosionAI GmbH, 2016 spaCy GmbH, 2015 Matthew Honnibal\", owner's page, not GovTech docs)",
         "ENTI: \"Entity types are identified either by the underlying AI Model (e.g. spaCy), and a combination of:\" followed by Regex Patterning, Rule-based Matching and \"Validation using checksums (if applicable)\" [Documented]; it links the en_core_web_sm model page and the spaCy rule-based matching page [Documented] (ENTI). The Credits page has no spaCy entry [Not disclosed] (checked CRED, 32 entries). Which model and version Cloak runs [Not disclosed] (checked the entity pages, FAQ, CRED, REL, portal pages)",
         "spaCy library licence MIT [Documented: repo explosion/spaCy@release-v3.8.16] (LICENSE:1, owner's page, not GovTech docs). en_core_web_sm 3.8.0 licence MIT, with a listed source OntoNotes 5 under \"commercial (licensed by Explosion)\" [Documented: repo explosion/spacy-models@ca6f473a] (meta/en_core_web_sm-3.8.0.json, owner's page, not GovTech docs). Their licence is not evidence for what Cloak runs [Inferred] (premise: Cloak names spaCy only as an example)",
         CK1, keys="ENTI CRED SPYLIC SPYMODEL")
    base("Presidio",
         "Created at Microsoft and moving to the independent data-privacy-stack organisation, per the Presidio docs; both owners are recorded in sheet 3f [Documented] (PRESTR, owner's page, not GovTech docs)",
         "ENTI: \"Click here for general information on the PII entities supported by Presidio.\" with a link to the Presidio supported-entities page (HTTP 200 observed 2026-10-10) [Documented] (ENTI, PRESENT). ENCR: \"Microsoft Presidio has a built-in encryption functionality, to encrypt and decrypt identified entities.\" with a tutorial link that returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC). The Credits page has no Presidio entry [Not disclosed] (checked CRED). That Cloak is built on Presidio [Inferred] (premise: the tag names such as SG_NRIC_FIN and PERSON follow Presidio's style, the ENCR text, and the ENTI link; no GovTech page says it)",
         "Presidio licence MIT [Documented: repo data-privacy-stack/presidio@2.2.364] (LICENSE:1, owner's page, not GovTech docs). Cross-reference: see the Presidio inventory sheet 3f for components and licences; not re-read here",
         CK1, keys="ENTI ENCR CRED PRESENT PRESENC PRESTR PRESLIC")
    base("PyCryptodome (cryptodome)",
         "Legrandin (GitHub account of the PyCryptodome project) [Documented: repo Legrandin/pycryptodome@v3.24.0] (LICENSE.rst, owner's page, not GovTech docs)",
         "CRED lists \"cryptodome\" with the source link https://github.com/Legrandin/pycryptodome [Documented]. What Cloak uses it for [Not disclosed] (CRED gives a name and a link only). That it backs the Encrypt technique [Inferred] (premise: the name and the AES-256 CBC encryption feature; no page says it)",
         "\"The source code in PyCryptodome is partially in the public domain and partially released under the BSD 2-Clause license.\" [Documented: repo Legrandin/pycryptodome@v3.24.0] (LICENSE.rst:1-2, owner's page, not GovTech docs)",
         CK3, keys="CRED PCDLIC")
    base("PyCrypto (crypto)",
         "PyPI project page pycrypto 2.6.1, \"Python Cryptography Toolkit (pycrypto)\" [Documented] (PyPI project page, owner not named in the text read, not GovTech docs)",
         "CRED lists \"crypto\" with the source link https://pypi.org/project/pycrypto/ [Documented]. What Cloak uses it for [Not disclosed] (CRED gives a name and a link only)",
         "PyPI metadata: \"Public Domain\" [Documented] (PyPI pycrypto page, not GovTech docs). The page says \"PyCrypto is written and tested using Python version 2.1 through 3.3\" [Documented] (PyPI pycrypto page, not GovTech docs). Current maintenance status [Not disclosed] (checked the project page text read)",
         CK3, keys="CRED PCRYPTO")
    return "\n".join(out)
