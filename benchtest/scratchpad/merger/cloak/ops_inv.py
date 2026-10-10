"""Inventory edits for cloak (sheet 3x). Imported by merge_cloak.py."""

H1 = "Cloak: Free-text PII detection and anonymisation"
H2 = "Cloak: Custom entity detection in free text (lists, regex and LLM)"
H3 = "Cloak: Reversible anonymisation and decryption (encrypt and restore)"
ALL3 = "; ".join([H1, H2, H3])
H12 = H1 + "; " + H2
PBREF = "[Documented: repo govtech-responsibleai/playbook@45908b48]"
PBURL = "https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx"
OLD_TUT = "https://microsoft.github.io/presidio/tutorial/12_encryption/"
NEW_TUT = "https://presidio.dataprivacystack.org/tutorial/12_encryption/"
PSE = '"\'Public Sector Entities\' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)"'


def cov(V, blk, key, old, new, reason):
    V.sub(blk, key, "Covered by", old, new, reason, kind="covered-by")


def apply(V):
    # ------------------------------------------------------------------ scope paragraph
    V.para_sub("redirect to a login page and are not read (read-only rule).",
               "return a login redirect (HTTP 302 then a 200 login page, observed 2026-10-10), so their content is [Not disclosed].",
               "T70: process wording ('read-only rule') replaced by the HTTP fact and the label (the span includes the words 'redirect to a login page and' to avoid a duplicated clause)")
    V.para_sub("15 pages, text read with pypdf);", "15 pages);", "T70: extraction-tool wording removed")
    V.para_sub("Covered-by headers are the three Table 3 headers CK1 to CK3 (default column split, open at CP1); a cell with several headers separates them with a semicolon.",
               "A Covered by cell carries one or more of the three Table 3 headers of this product, separated by a semicolon, or one marker.",
               "T70, T71: internal ids and 'open at CP1' removed")
    V.para_sub("APIGUIDE and APISPEC = the login-gated API Guide and OpenAPI pages.",
               "APIGUIDE and APISPEC = the login-gated API Guide and OpenAPI pages; TECHI = fta/anonymisation-techniques/intro.md; SAMPD = fta/custom-entities/custom-entities-unstructured/samples/datetime-specific.md; PRESTR = https://presidio.dataprivacystack.org/project_transition/ (the Presidio project transition page); PRESENT = https://microsoft.github.io/presidio/supported_entities/ (the Presidio supported-entities page); PRESENC = https://microsoft.github.io/presidio/tutorial/12_encryption/ (HTTP 404; the tutorial is served at https://presidio.dataprivacystack.org/tutorial/12_encryption/, HTTP 200, observed 2026-10-10).",
               "T74: five short names used in cells but not defined")

    # ------------------------------------------------------------------ (a)
    cov(V, "a", "Templates", H1, H12, "T4: CK2 R6 says a custom entity configuration is saved as a template")
    V.sub("a", "Mock Data Generation", "Status",
          "Two official pages place MDG under different products and are not reconciled here: the portal lists it under Cloak [Documented] (PF) and the Mirage site lists it under Mirage [Documented] (MIR).",
          'Two official pages place MDG under different products, and the Mirage page adds that MDG "is available via API through Cloak" [Documented] (MIR): the portal lists it under Cloak [Documented] (PF) and the Mirage site lists it under Mirage [Documented] (MIR); how the two placements relate is [Not disclosed] (checked the Cloak Guide sidebar, the portal pages and both home pages).',
          "T64 (class b, drafting edit): quote, do not decide; 'not reconciled here' was stronger than the quotes")
    V.sub("a", "Mirage (sister product)", "Data",
          ". Mirage is not mined further in this inventory [Inferred] (premise: scope decision for Cloak research, not a Mirage fact)",
          "",
          "T70: scope-decision sentence removed (not a Mirage fact)")

    # ------------------------------------------------------------------ (b)
    V.para_sub("free-text decryption helper script return a login redirect (HTTP 302, then a 200 login page, observed 2026-10-10).",
               "free-text decryption helper script return a login redirect (HTTP 302, then a 200 login page, observed 2026-10-10). The last row records a planned integration with Sentinel, not a current path.",
               "T7: block intro names the planned row")
    V.append("b", "Web UI for non-WOG users", "Audience",
             'The playbook calls Cloak "GovTech\'s dedicated internal service for comprehensive and localised PII detection" ' + PBREF + '; the Cloak Guide home page says it "is open to select non-government entities (e.g. public healthcare)" [Documented] (HOME)',
             "T8: conflict C3 as two attributed facts (README section 3 rule 4)")
    V.url_add("b", "Web UI for non-WOG users", [PBURL], "T8: playbook source for the added fact")
    V.sub("b", "API onboarding and gated documentation", "Audience",
          "The form link was not opened (read-only rule)",
          "The onboarding form itself is not public documentation and is not described here [Not disclosed]",
          "T70: process wording removed")
    V.row_insert("b", "Python package (application",
        "| Sentinel integration (planned) | Sentinel API users: \"Direct integration with the Sentinel API is coming soon.\" " + PBREF + " (playbook privacy improvements page) | Not stated [Not disclosed] (checked the playbook page, aiguardian.gov.sg /docs and /docs/wiki/Sentinel-Guardrails for \"cloak\"; no hit, observed 2026-10-10) | Not stated [Not disclosed] (same checks) | PII detection and masking on Sentinel traffic; the Sentinel sheet column is GovTech Sentinel: PII detection and masking (AWS Bedrock) (sheet 3, column AF) [Inferred] (premise: the playbook lists Cloak under \"Detection tools\" for PII and shows the planned integration under the Sentinel tab) | Planned, no date given. Code stub: \"# Coming soon — Sentinel + Cloak integration is on the roadmap.\" " + PBREF + " (playbook, tab Sentinel (Cloak)). The deployed playbook page states the same [Documented] (observed 2026-10-10). Whether a Sentinel guardrail for Cloak exists today [Not disclosed] (checked the Sentinel docs pages above) | — (planned, not in Table 3) | " + PBURL + " ; https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/ ; https://www.aiguardian.gov.sg/docs ; https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails |",
        "T7 (main): planned Sentinel integration row, marker 'planned', cross-reference to the Sentinel PII column (sheet 3 column AF)")

    # ------------------------------------------------------------------ (c)
    cov(V, "c", "Inclusion list on an existing entity", H2, H12, "T5: the Inclusion Feature page is about an existing built-in entity (CK1) and about fixed-list custom entities (CK2)")

    # ------------------------------------------------------------------ (d)
    V.sub("d", "=Replace", "Reversible",
          "No [Inferred] (premise: the REPL page describes replacement by a tag or word and mentions no key, mapping or restore step)",
          "Not stated [Not disclosed] (checked REPL, USE and RUNQ: they describe replacement by a tag or word and mention no key, mapping or restore step)",
          "T50 (R020, R015): an absence conclusion is Not disclosed; aligned with CK3 R2 and R8", kind="label")
    V.sub("d", "=Redact", "Reversible",
          "No [Inferred] (premise: the REDA page says the words are removed and gives no key or mapping)",
          'Not stated [Not disclosed] (checked REDA: it says detected entities "will be replaced with a blank" [Documented] and mentions no key, mapping or restore step)',
          "T50 (R020, R015): an absence conclusion is Not disclosed; aligned with CK3 R2 and R8", kind="label")
    V.sub("d", "=Mask", "Reversible",
          "No [Inferred] (premise: the MASK page describes hiding characters and gives no key or mapping)",
          "Not stated [Not disclosed] (checked MASK: it describes hiding characters and mentions no key or mapping)",
          "T50 (R020, R015): an absence conclusion is Not disclosed; aligned with CK3 R2 and R8", kind="label")
    cell = V.cell_get("d", "=Mask", "Parameters")
    i = cell.index(' Definition: "Suffix')
    V.sub("d", "=Mask", "Parameters", cell[i:],
          ' Masking Type table: "Suffix: masks the starting characters" and "Prefix: masks the ending characters" [Documented] (MASK, Usage Guide table). Example table: 120414 becomes 120 followed by three asterisks and is described as "Transforms into a suffix masked value" [Documented] (MASK, Example table). The two parts of the page read opposite ways on which end Suffix masks; neither is chosen here',
          "T48: two labelled facts, one per part of the page (README section 3 rule 4)")
    V.sub("d", "Pseudonymise", "Parameters",
          "the page wording is probably stale [Inferred] (premise: both statements sit on official pages and cannot both describe the current release)",
          "which of the two statements is current is [Not disclosed] (both sit on official pages; checked PSEU, REL and SECR)",
          "T52 (class b, drafting edit): aligned with CK3, no conclusion", kind="label")
    V.sub("d", "Encrypt", "Parameters",
          "returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC)",
          "returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC). The tutorial is served at presidio.dataprivacystack.org/tutorial/12_encryption/ (HTTP 200, observed 2026-10-10) [Documented] (PRESENC)",
          "T69: working location of the tutorial (successor org is official per R016); the 404 stays recorded as an HTTP fact")
    V.sub("d", "Encrypt", "Source URL", OLD_TUT, NEW_TUT,
          "T69: the 404 URL replaced by the working presidio.dataprivacystack.org URL", kind="url")
    cov(V, "d", "Decrypt", H1 + " ; " + H3, H3, "T4 (main): Decrypt acts on stored ciphertext, restore side only")

    # ------------------------------------------------------------------ (e)
    V.para_sub("Terms rows quote clauses as written and carry no interpretation.",
               "Terms rows quote clauses as printed.",
               "T70: process wording removed")
    ALL = ALL3
    for key in ["Pasted text length", "CSV file size", "PDF and DOCX file size", "Files per project"]:
        cov(V, "e", key, H1, ALL, "T4: the limit is repeated in CK2 R3 and R6 and CK3 R6")
    for key in ["Content not processed", "Preview limits", "Confidence level", "Replace (Unique) limits"]:
        cov(V, "e", key, H1, H12, "T4: the same fact is carried in CK2 Detail")
    cov(V, "e", "Inclusion and fixed-list size", H2, H12, "T4, T5: the Inclusion page covers an existing entity (CK1) and fixed-list entities (CK2)")
    V.sub("e", "CSV file size", "Applies to",
          "the current usage guide is the later statement and gives no column limit for FTA CSV [Inferred] (premise: the usage guide and FAQ state the current limits, the release note is dated 15 January 2024)",
          "The usage guide and the FAQ give no column limit for FTA CSV files [Not disclosed] (checked USE, FAQ and the release notes through v2.2.2). The release note is dated 15 January 2024 and the guide pages are undated, so that the guide supersedes it is [Inferred] (premise: the Cloak Guide is the live documentation)",
          "T67: the verbatim facts and the absence separated from the inference")
    V.append("e", "Confidence level", "Applies to",
             'The portal Features page says "Adjust detection sensitivity per entity type to balance recall and precision for your dataset" [Documented] (PF). The Anonymisation Settings drawer has one "Adjust Confidence level" dropdown with a slider "set to the default value of 0.30" [Documented] (CONF)',
             "T41 (class b, hygiene): the two sides of the question as documented facts; the Not disclosed fact on scope stays")
    V.append("e", "LLM-enabled custom entity limits", "Value",
             'The FAQ says "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time." [Documented] (FAQ); the unit differs from the LLMI wording (dataset against project) [Documented]',
             "T43 (class b, drafting edit): both units now in the inventory as in block (c) and CK2 R4")
    V.append("e", "Data retention", "Applies to",
             "The Privacy Statement gives no retention period [Not disclosed] (checked its 4 pages); see the Privacy Statement row",
             "T14: retention in the Privacy Statement")
    V.sub("e", "Data-classification ceiling", "Value",
          "(TERMS, 15 pages read with pypdf)", "(TERMS, Schedule 4.6; the backslash is printed in the PDF)",
          "T13, T70: the backslash is in the PDF (page rendered and read); extraction wording removed")
    V.sub("e", "Data-classification ceiling", "Applies to",
          "The tabular usage guide gives the same wording [Documented] (TABU)",
          'The tabular usage guide says "Cloak supports datasets classified up to Confidential (Cloud-Eligible) and/or Sensitive (High)" [Documented] (TABU)',
          "T13: the three official wordings are written as separate facts")
    V.append("e", "Terms clause 3.3", "Value",
             "The same clause defines the term: " + PSE + " [Documented] (TERMS, clause 3.3)",
             "T10: definition of Public Sector Entities, verbatim")
    V.append("e", "Terms clause 3.3", "Applies to",
             'The FAQ defines Non-Government Entities as "entities not covered under the Public Sector Governance Act" [Documented] (FAQ)',
             "T10: FAQ definition")
    V.sub("e", "Terms clause 3.4.7", "Applies to",
          "checked the full 15 pages)",
          "checked the full 15 pages); the Terms state no exception for evaluation or comparison [Not disclosed] (same checks)",
          "T9: absence of an exception recorded")
    V.append("e", "Terms clauses 3.4.9", "Applies to",
             '"License keys" is not defined in the Terms [Not disclosed] (checked the 15 pages); the Secrets Manager shares secrets with "up to 10 other users per operation" [Documented] (SECR)',
             "T11: no definition of license keys")
    V.append("e", "Terms Schedule 2.2", "Applies to",
             'The Terms do not define "Agency" [Not disclosed] (checked the 15 pages). The FAQ says "Users do not sign a separate agreement or contract. All users are legally bound by Cloak\'s Terms of Use." [Documented] (FAQ). Clause 1.5 says a user acting for another entity warrants "the necessary authority to bind such entity to these Terms of Use" [Documented] (TERMS, clause 1.5)',
             "T10, T12: Agency is undefined; FAQ and clause 1.5 quotes")
    V.sub("e", "Terms clause 15", "Applies to",
          "The clause cross-references say clause 14.2 and 14.3, while the numbering in the PDF is 15.2 and 15.3 [Documented] (TERMS)",
          'Clause numbers are as printed: 15.2 begins "Subject to clause 14.3" and 15.3 refers to "clause 14.2 above", while clause 14 is Severability with no sub-clauses [Documented] (TERMS). That the references mean 15.2 and 15.3 is [Inferred] (premise: 15.2 is the courts clause and 15.3 refers to "any dispute referred to" there)',
          "T18: numbers as printed; the meaning of the cross-references kept as an inference")
    V.sub("e", "Terms and Privacy Statement dates", "Value",
          "(PRIV, 4 pages read with pypdf)", "(PRIV)", "T70: extraction wording removed")
    V.append("e", "Terms and Privacy Statement dates", "Applies to",
             "The cloak.gov.sg home and register pages link the Terms and the Privacy Statement through go.gov.sg/cloak-terms and go.gov.sg/cloak-privacy [Documented] (SITE, REGP, observed 2026-10-10); a later Terms version [Not disclosed] (checked SITE, REGP, FAQ and the PDF)",
             "T19: link currency and later version")
    V.row_insert("e", "Terms and Privacy Statement dates",
        "| Terms Schedule 4.1 and 4.2 (routine deletion of Your Data) | \"4.2. You acknowledge and agree that GovTech may routinely delete any or all of Your Data from its systems after a reasonable period as from time to time determined by GovTech.\" [Documented] (TERMS, Schedule 4.2). Schedule 4.1 defines Your Data as \"all information, data and materials (including their derivatives) which GovTech may access or receive from you, in the course of providing the Service\" [Documented] (TERMS, Schedule 4.1) | Whole service. A retention period in the Terms [Not disclosed] (Schedule 4.2 says \"a reasonable period\"; checked the 15 pages). The FAQ gives \"purged within 24 hours\" for anonymised data [Documented] (FAQ) | " + ALL3 + " | https://go.gov.sg/cloak-terms |",
        "T15 (main P5 Q1): new row; CORRECTION: routine deletion is Schedule 4.2, not main-body clause 4.2 (clause 4.2 is identity verification)")
    V.row_insert("e", "Terms Schedule 4.1 and 4.2",
        "| Terms clause 6.1 (licence to GovTech over submitted data) | \"You hereby grant to GovTech a non-exclusive, worldwide, perpetual and royalty-free right to collect, use, disclose, process, modify, adapt, create derivative works of, reproduce, and sublicense any and all information or data submitted, uploaded or shared by you\" [Documented] (TERMS, clause 6.1, quoted to this point) | Whole service. The clause continues \"to the extent necessary to provide the Service or for any other purpose expressly or impliedly provided in these Terms of Use, or as permitted by law\" [Documented] (TERMS, clause 6.1) | " + ALL3 + " | https://go.gov.sg/cloak-terms |",
        "T15 (main P5 Q1): new row")
    V.row_insert("e", "Terms clause 6.1",
        "| Privacy Statement paragraphs 4 and 5.1.5 (storage and backups) | Paragraph 4: \"Your data may be stored in our servers, systems or devices, in the servers, systems or devices of our third party service providers or collaborators\" [Documented] (PRIV). Paragraph 5.1.5: \"for the purposes of storing or creating backups of your data (whether for contingency or business continuity purposes or otherwise), whether within or outside Singapore\" [Documented] (PRIV) | Whole service, version dated 1 December 2022 [Documented] (PRIV). A retention period [Not disclosed] (checked the 4 pages). The FAQ says \"Cloak does not retain data\" [Documented] (FAQ); neither source relates the two [Not disclosed] (checked both) | " + ALL3 + " | https://go.gov.sg/cloak-privacy ; https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md |",
        "T15, T14 (main P5 Q1): new row")

    # ------------------------------------------------------------------ (f)
    V.para_sub("Owners' pages are cited for licences and are not GovTech docs.",
               "Owners' pages are cited for licences and are not GovTech docs. Terms Schedule 3 refers to \"a list of open source components used in the Service\" [Documented] (TERMS); the link go.gov.sg/cloak-open-source redirects to the Credits page [Documented] (HTTP 302 observed 2026-10-10).",
               "T20: the vendor's own pointer to its open-source list")
    cov(V, "f", "Presidio", H1, H1 + "; " + H3, "T4: the Encrypt-page evidence in this row supports CK3")
    V.sub("f", "Presidio", "Where",
          "tutorial link that returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC)",
          "tutorial link that returned HTTP 404 on 2026-10-10 [Documented] (ENCR, PRESENC). The tutorial is served at presidio.dataprivacystack.org/tutorial/12_encryption/ (HTTP 200, observed 2026-10-10) [Documented] (PRESENC)",
          "T69: working location of the tutorial")
    V.sub("f", "Presidio", "Source URL", OLD_TUT, NEW_TUT,
          "T69: the 404 URL replaced by the working presidio.dataprivacystack.org URL", kind="url")
    V.sub("f", "=PyCrypto (crypto)", "Owner",
          'PyPI project page pycrypto 2.6.1, "Python Cryptography Toolkit (pycrypto)" [Documented] (PyPI project page, owner not named in the text read, not GovTech docs)',
          "PyPI project page pycrypto 2.6.1, author Dwayne C. Litzenberger, maintainers amk and dlitz [Documented] (PyPI project page, linked from CRED, not GovTech docs)",
          "T20 (PARTLY): the PyPI page names an author and maintainers; 'owner not named' was wrong", kind="correction")
    V.sub("f", "=PyCrypto (crypto)", "Licence",
          "Current maintenance status [Not disclosed] (checked the project page text read)",
          "Released Oct 17, 2013; last file added Jun 20, 2014 [Documented] (PyPI pycrypto page, not GovTech docs). Current maintenance status [Not disclosed] (the PyPI page gives release dates and no maintenance statement)",
          "T20: release dates added; process wording removed")
