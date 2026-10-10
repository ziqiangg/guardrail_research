# Cloak resolutions 1 (P5, gr-resolver, 2026-10-10)

Items handled: all 27 class (a) items (T3, T4, T5, T6, T7, T8, T33, T34, T35, T36, T39, T48, T50, T57, T59, T60, T61, T66, T67, T68, T69, T70, T71, T72, T73, T74, T75) and all 12 class (c) items (T9 to T20). H items first (T34, T39, T59, T60, T9, T10), then M, then L. A closing note for the class (b) items that a ruling or a drafting edit touches (T1, T2, T21 to T26, T40 to T43, T52, T62, T64, T65) is in "Class (b) items" before the Report. Rulings applied: R037 (three columns, CK3 one column), R002, R007, R009, R011, R013, R015, R019 (Terms and Privacy PDFs read), R020, R021, R032 (bench wording stays a proposal), and main's cloak rows in `scratchpad/main/queue.md` (headers, Decrypt to CK3 only, Pseudonymise stays CK1 and CK3, Inclusion row, planned Sentinel row, list-limit Summary wording, Terms clauses verbatim with no interpretation, login-gated pages are `[Not disclosed]` plus the HTTP fact).

Line numbers are file lines of the drafts as at 2026-10-10 (`A:52` = `cloak_cols_a.md` line 52, `B:67` = `cloak_cols_b.md`, `INV(e) line 108` = `cloak_inventory.md` line 108, `BR:24` = `cloak_brief.md`); they move once the merger edits. Where a Summary changes, the new text is given in full with its word count (checker method: label excluded; lessons 18 limit is 44 for rows other than R7).

## Method and access notes

- All web reads were read-only GETs. Cloak Guide Markdown pages were fetched again today with `curl` from `https://docs.developer.tech.gov.sg/docs/cloak-guide/<path>.md` (HTTP 200, 31 pages plus `_sidebar.md`) and are copied in `benchtest/scratchpad/resolver/cloak1/docs/`. Portal, cloak.gov.sg, mirage.gov.sg, aiguardian.gov.sg and playbook site text came from `python benchtest/tools/fetch_text.py`. The playbook page was read raw at both `45908b48c0a8b6d3855a154c0e41a12958a99205` (staging) and `97338569d8711ae4c7a6615a34deb92a720beba8` (main); the two files are byte-identical.
- The Terms PDF (`https://go.gov.sg/cloak-terms`, HTTP 302 to `https://file.go.gov.sg/cloak-terms.pdf`, 103170 bytes, 15 pages) and the Privacy Statement PDF (`https://go.gov.sg/cloak-privacy`, 302 to `https://file.go.gov.sg/cloak-privacy.pdf`, 52311 bytes, 4 pages) were downloaded again; the Terms file is byte-identical to the drafter's copy (`cmp`). Text was extracted with pypdf and, for layout, with PyMuPDF (installed with `pip install --target` into `benchtest/scratchpad/resolver/cloak1/_pylib`, a third-party tool, not a vendor package; the folder is deleted at the end of this task). PyMuPDF was used for two things the text layer cannot show: page 15 of the Terms was rendered to an image (T13) and slide 22 of the USENIX deck was rendered and its drawn arrows listed (T57).
- The 2023 USENIX deck (`https://www.usenix.org/system/files/pepr23_slides-tang.pdf`, 32 slides) was read from the drafter's copy (`benchtest/scratchpad/drafter/cloak_cols_b/usenix.pdf`) to avoid saving a second 6.8 MB file; all 32 slides were searched for restore, reconstruct, decrypt and mapping.
- Git reads: `git ls-remote --tags` for explosion/spaCy, explosion/spacy-models, data-privacy-stack/presidio and Legrandin/pycryptodome, and `git ls-remote` for the playbook (T68). Raw licence files read with `fetch_text.py` at the pins (R020).
- Not read: the API Guide, OpenAPI pages, package guide and free-text decryption helper script (login redirect re-observed today, T69); the onboarding form and support links (never opened, R019). No sign-in, no form, no vendor API call. The two `go.gov.sg` support links were requested without following the redirect, only to record the status (HTTP 302); nothing behind them was opened.
- A scratch quote check (`benchtest/scratchpad/resolver/cloak1/quotecheck.py`) compares every verbatim quote below with the fresh copies after whitespace, quote and backtick normalisation; its result is in the Report.

## Resolutions

### T34 — CK1 R4 Summary "hosted on GovTech's cloud" (class a, H)
- Verdict: RESOLVED (drafting fix; the Detail never calls it GovTech's cloud).
- Evidence: Cloak Guide, key FAQs (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md): "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment". Portal Features and Roadmap (https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap) names the tech stack "AWS GCC 2.0". No page says "GovTech's cloud".
- Label to use: `[Documented]`.
- Draft impact: CK1 R4 Summary (A:52), replace with (35 words):
  - `Summary: **Named techniques, model not named.** Entities are found by an AI model (spaCy given as an example) plus regex, rule-based matching and checksums, hosted on the Government Commercial Cloud. Reached by web UI or API. **[Documented]**`
  - Detail unchanged (A:59 already carries the FAQ quote). Summary change: yes (CK1 R4).

### T39 — Entity count: 17 groups, 20 tags, vendor "20+" and "17+" (class a, H)
- Verdict: RESOLVED. Recount at source gives 17 groups (plus Exceptions and Custom) and 20 baseline tags; both vendor counts are verbatim. The R2 Summary "Seventeen entity groups" stays. What the deployed Web UI shows is a UI check and stays with the bench (class b).
- Evidence:
  - Entity Types page (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/intro.md): "The following entity groups are currently available:" followed by Personal (Name, NRIC (SG), Email Address, Phone Number, Nationality/Race/Religion, Address (SG), Location, Passport (SG)), Financial (Currency, Credit Card, Bank Account Number (SG), Bank Account Number (IBAN)), Technical Security (IP Address, URL), Others (Date & Time, UEN (SG), Organization, Exceptions, Custom). That is 8 + 4 + 2 + 3 = 17 groups plus Exceptions and Custom.
  - Tags (each entity page, "REPLACE ... with <TAG>"): PERSON, SG_NRIC_FIN, EMAIL_ADDRESS, PHONE_NUMBER, NRP, LOCATION, SG_PASSPORT, CURRENCY, CREDIT_CARD, SG_BANK_ACCOUNT_NUMBER, IBAN_CODE, IP_ADDRESS, URL, DATE_TIME, SG_UEN, ORGANIZATION = 16 single-tag groups; the Address page gives "4 address-related recognisers" (SG_ADDRESS, SG_ADDRESS_POSTAL_CODE, SG_ADDRESS_UNIT_NUMBER, SG_ADDRESS_STREET). 16 + 4 = 20.
  - FTA intro caption (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/intro-to-fta.md): "Cloak detects and transforms 20+ baseline entity types". Portal Features (https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap): "Auto-detection of 20+ entity types including names, NRICs, phone numbers, addresses, emails, dates of birth, bank accounts, and more". Portal FAQs (https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/faqs): "Cloak detects 17+ entity types out of the box".
- Label to use: 17 groups `[Documented]`; the tally of 20 tags stays `[Inferred]` (premise: one tag per entity page plus the four Address tags; a drafter's count, not a vendor figure); the two vendor counts `[Documented]`.
- Draft impact:
  - CK1 R2 Summary (A:16): no change.
  - CK1 R2 A:20, replace the first clause "Counting one tag per group plus the 4 address tags gives 20 baseline tags" with "Counting one tag for each of the 16 groups other than Address, plus the 4 address tags, gives 20 baseline tags" (the 17 groups include Address, so "one tag per group plus 4" would count it twice). Label stays `**[Inferred]**`.
  - INV(c) intro (line 38): same wording fix in "(premise: 16 single-tag groups plus the 4 address tags)" is already correct; no change there.
  - Summary change: none.

### T59 — CK2 R4 Summary "learns from 3 to 5 examples" (class a, H)
- Verdict: RESOLVED (drafting fix).
- Evidence: Unstructured intro (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/intro.md): "few-shot prompting, which allows the LLM to detect new entities without fine-tuning. This approach only needs a small set of 3-5 examples (labelled data)". Write-prompts page: "Include 3-5 examples that captures the diversity present in your dataset."
- Label to use: `[Documented]`.
- Draft impact: CK2 R4 Summary (B:52), replace with (35 words):
  - `Summary: **Three mechanisms: list, regex and few-shot LLM.** Lists match exact words, regex matches patterns, and the Beta LLM entity is prompted with 3 to 5 examples on a privately hosted model on Government Commercial Cloud. **[Documented]**`
  - Detail unchanged (B:13, B:62, B:99 carry the quotes). Summary change: yes (CK2 R4).

### T60 — CK2 R5 Summary says custom matches appear in the Findings table (class a, H)
- Verdict: RESOLVED (drafting fix). The usage guide caption describes the Findings table for detected entities in general; no page says custom entities of any kind appear in it with a score (Detail B:82 is `[Not disclosed]`).
- Evidence: Usage guide (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md), caption: "The Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score." Unstructured intro: "We'll notify you via email when your job is complete." (the page prints "We’ll" with a typographic apostrophe). Fixed-list page: "Your text is now transformed with the new custom entity applied."
- Label to use: `[Documented]` for the new Summary (it draws only on documented bullets B:77, B:79, B:80, B:87, B:88).
- Draft impact:
  - CK2 R5 Summary (B:75), replace with (40 words):
    - `Summary: **Transformed text for each custom match.** Each match is replaced, redacted, masked or otherwise transformed with the technique chosen for that entity. The result is anonymised text or a file, and an email says when an LLM entity job completes. **[Documented]**`
  - CK2 R5 B:81, prefix the bullet so it does not read as a custom-entity fact: `• Findings table for detected entities in general: "The Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score." (usage guide caption) **[Documented]**` (B:82, the `[Not disclosed]` bullet that follows, stays).
  - CK3 R5 B:241 carries the same caption as "Anonymise side review"; no change needed (it says detected entity, not custom).
  - Summary change: yes (CK2 R5).

### T9 — Terms clause 3.4.7 (benchmarking) (class c, H)
- Verdict: RESOLVED as a verbatim record; permitted use stays open (checked the Terms for a definition of "benchmarking" or an exception for evaluation: the word occurs once in 15 pages and nothing defines it or excepts any use; not stated). No interpretation is given.
- Evidence (https://go.gov.sg/cloak-terms, 302 to https://file.go.gov.sg/cloak-terms.pdf, dated 24 July 2024, page 2 to 3): clause 3.4 "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 "perform any benchmarking tests or analyses of the Service;". Clause 3.2: "a non-exclusive, revocable, and non-transferable right to access and use the Service for personal or internal purposes only, and only for such use permitted by the functions of the Service and intended by GovTech."
- Label to use: the clause text `[Documented]`; whether a comparison bench falls under it `[Not disclosed]` (checked all 15 pages of the Terms and the FAQ, the Privacy Statement and the home page; no definition or exception).
- Draft impact (wording per R025 pattern and R032; process words removed, see T70):
  - CK1 R8 A:129, replace with: `• Does Terms clause 3.4.7 ("perform any benchmarking tests or analyses of the Service") bar a bench comparison, and would GovTech's written consent under clause 3.3 cover it? (the Terms define no benchmarking term and state no exception; checked all 15 pages; decided before any bench run)`
  - CK2 R8 B:126 and CK3 R8 B:282, replace with: `• Terms clause 3.4 says "You shall not, and shall not authorise or permit any third party to:" and 3.4.7 reads "perform any benchmarking tests or analyses of the Service;" (Terms of Use dated 24 July 2024). Whether a comparison bench falls under it is not stated (the Terms define no benchmarking term; checked all 15 pages); decided before any bench run`
  - CK1 R7 A:118: unchanged (already a verbatim quote, `[Documented]`). CK2 R7 B:116 and CK3 R7 B:272: reworded under T70.
  - INV(e) line 108 (Terms clause 3.4.7 row): value cell unchanged; Applies-to cell wording `(the Terms define no benchmarking term; checked the full 15 pages)` stays; add after it `; the Terms state no exception for evaluation or comparison [Not disclosed] (same checks)`.
  - R7 and R8 Summaries (A:114, A:127, B:112, B:124, B:268, B:280): no change (they name the clause and the open question).
  - Summary change: none.

### T10 — Terms clause 3.3 (non-public-sector use) and the definition of Public Sector Entities (class c, H)
- Verdict: RESOLVED as a verbatim record, with the definition clause (not in any draft) added. Whether a bench could obtain written consent is not stated and is not interpreted.
- Evidence (Terms PDF, page 2): clause 3.3 "In relation to entities that are not Public Sector Entities, your use and access of the Service is restricted solely for such purpose that GovTech has consented to in writing (including via email) (‘Purpose’)." and "‘Public Sector Entities’ means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)." The definition sits inside clause 3.3; the Privacy Statement paragraph 11 repeats it for that document.
  - FAQ (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md): "NGE users are additionally required to fulfil Clause 3.3: they must have agreed with the Cloak team on the purpose of use prior to access, and any change in purpose requires written consent (including via email)." Also "Non-Government Entities (NGEs) are entities not covered under the Public Sector Governance Act and therefore not subject to IM8 Data."
  - Terms Schedule 2.2 uses "your Agency" without a definition: the capitalised word "Agency" has no definition in the 15 pages (the only "agency" in lower case is "Government Technology Agency" in clause 1.2).
- Label to use: clause and definition text `[Documented]`; the meaning of "Agency" `[Not disclosed]` (checked the 15 pages).
- Draft impact:
  - INV(e) line 107 (clause 3.3 row), value cell: append `. The same clause defines the term: "'Public Sector Entities' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)" [Documented] (TERMS, clause 3.3)`. Applies-to cell: append `. The FAQ defines Non-Government Entities as "entities not covered under the Public Sector Governance Act" [Documented] (FAQ)`.
  - INV(e) line 111 (Schedule 2.2 row), Applies-to cell: append `. The Terms do not define "Agency" [Not disclosed] (checked the 15 pages)`.
  - CK1 R7: insert after A:117 `• Terms of Use, clause 3.3 defines the term: "'Public Sector Entities' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)" **[Documented]**`.
  - CK2 R8 B:127 and CK3 R8 B:284: no change.
  - Summary change: none.

### T57 — Slide 22 of the 2023 deck: restore step read from the pypdf text layer (class a, M)
- Verdict: CORRECTION. Rendered at 170 dpi and with the drawn arrows listed, slide 22 does not show the "Anonymised Response" returning through the "Transformer Module". The Transformer Module box (labels "Detect PII" and "Anonymise PII") receives the Original Prompt and sends back the Mapping Table and the Anonymised Prompt; the Anonymised Prompt goes to the "Gen AI Magic!" box, and the "Anonymised Response" (with "<hash value 1>" still in it) comes back from that box to the agency product side. No arrow or label draws a step that restores the original values. The draft's reading (A:50 and B:209) came from the text-layer order and is wrong. A:49 (prompt goes through Detect PII and Anonymise PII before the GenAI product) is correct.
- Evidence (https://www.usenix.org/system/files/pepr23_slides-tang.pdf, slide 22, "What We Did: Designed API workflow to mitigate potential privacy leakages for Generative AI use cases"): labels "Original Prompt:", "Detect PII", "Anonymise PII", "Transformer Module", "Mapping Table", "Anonymised Prompt:", "<<Gen AI Magic!>>", "Anonymised Response" ("Dear <hash value 1>, we regret to inform.."), callout "API: Takes in unstructured text, returns mapping table and anonymized result." Layout (rendered slide and PyMuPDF drawn lines): one arrow runs from the Original Prompt box into the Transformer Module; two short arrows run from the Transformer Module and the API callout back to the Mapping Table and the Anonymised Prompt boxes; a long arrow runs from the Anonymised Prompt box to the "Gen AI Magic!" box, and a long arrow runs from the "Gen AI Magic!" box back to the Anonymised Response box. Nothing else is drawn between the Gen AI box and the Transformer Module. Search of all 32 slides for restore, de-anonymise, reconstruct, decrypt: no hit.
- Label to use: the layout description `[Documented]` (read from the rendered slide); the absence of a restore step `[Not disclosed]` (checked slide 22 and the text of all 32 slides).
- Draft impact:
  - CK1 R3 A:50, replace with two bullets:
    - `• The same deck slide shows the "Anonymised Response" returning from the "Gen AI Magic!" box to the agency product with the placeholder "<hash value 1>" still in it (USENIX PEPR 2023 deck, slide 22, layout read from the rendered slide) **[Documented]**`
    - `• The deck draws no step that turns the placeholders back into the original values (checked slide 22 and the text of all 32 slides; the Mapping Table box sits on the agency product side) **[Not disclosed]**`
  - CK3 R3 B:209, replace with the same two bullets, each starting `Restore side in the deck:` (first bullet `**[Documented]**`, second `**[Not disclosed]**`; the second can replace the wording "draws no step" with "does not say where or how placeholders are restored from the mapping table").
  - CK3 R3 B:212: replace the premise `(premise: the deck workflow and the vendor's LLM use case)` with `(premise: the Encrypt page says the key is needed "for both encryption and decryption", and the deck slide shows the response returning with placeholders)`; label stays `**[Inferred]**`.
  - CK3 R1 B:186: change "GovTech 2023 deck workflow:" to "GovTech 2023 deck slide labels:" (the labels and the API callout quote are correct); label stays `**[Documented]**`.
  - CK3 R5 B:245 and Summary B:238 ("The 2023 deck's API also returned a mapping table"): unchanged, supported by the callout.
  - CK1 R3 Summary and CK3 R3 Summary do not use the deck; no Summary change.
  - Brief and reviewer notes: A RN-8 ("layout order not guaranteed") is closed by this read.

### T3 — Header text drift in the brief (class a, M)
- Verdict: RESOLVED.
- Evidence: `scratchpad/main/queue.md`, row "cloak P1 Q4 header tweaks": "accepted for accuracy: CK2 `Cloak: Custom entity detection in free text (lists, regex and LLM)`; CK3 `Cloak: Reversible anonymisation and decryption (encrypt and restore)`". R037 repeats both headers. The brief still has the old text at `BR:24` (`... (regex and LLM)`), `BR:25` (`... (secrets and salts)`), `BR:34`, `BR:180`, `BR:183`. All three drafts and the inventory Covered-by cells use the new text (the checker passes).
- Label to use: not a fact label (process item).
- Draft impact:
  - `cloak_brief.md` `BR:24` and `BR:25`: replace with `Cloak: Custom entity detection in free text (lists, regex and LLM)` and `Cloak: Reversible anonymisation and decryption (encrypt and restore)`; add under the heading line "Table 3 headers (exact)" one line: `CK2 and CK3 wording as ruled by main (queue.md, cloak P1 Q4) and R037; the older wording in the Why-the-header-wording paragraph and in Q01 and Q04 is superseded.`
  - `cloak_changes.md` Section 1: `Header wording | brief: CK2 "(regex and LLM)", CK3 "(secrets and salts)" | CK2 "(lists, regex and LLM)", CK3 "(encrypt and restore)" | main's tweak, queue.md cloak P1 Q4; R037 | prefix "Cloak:" fixed at CP1 per R009, frozen after CP2`.
  - No change to Summaries.

### T4 — Covered-by mappings to reconcile (class a, M)
- Verdict: RESOLVED. Rule used: a row lists every column whose Detail carries a bullet on that same fact; markers unchanged. Evidence is the column Detail itself (no outside source). Main's rulings: Decrypt CK3 only; Pseudonymise stays `CK1; CK3` (salt bullets are in CK3 R1, R4, R6).
- Evidence: CK2 R3 B:40 (20,000 characters) and B:49 (preview limits), CK2 R5 B:83 (0.30), CK2 R6 B:103 (template), B:104 (Replace (Unique)), B:109 (file limits); CK3 R3 B:204, CK3 R6 B:263; CK1 R2 A:33 and CK2 R2 B:33 (content not processed); CK3 R4 B:232 (Presidio Encrypt link).
- Label to use: not a fact label.
- Draft impact: replace the Covered-by cell as follows (H1 = `Cloak: Free-text PII detection and anonymisation`, H2 = `Cloak: Custom entity detection in free text (lists, regex and LLM)`, H3 = `Cloak: Reversible anonymisation and decryption (encrypt and restore)`; a cell with two or three headers separates them with `; `):

| Location | Row | Now | New |
|---|---|---|---|
| INV(d) line 83 | Decrypt | H1; H3 | H3 |
| INV(d) line 81 | Pseudonymise | H1; H3 | no change (main) |
| INV(a) line 16 | Templates | H1 | H1; H2 |
| INV(f) line 124 | Presidio | H1 | H1; H3 |
| INV(e) line 91 | Pasted text length | H1 | H1; H2; H3 |
| INV(e) lines 92, 93, 94 | CSV size; PDF and DOCX size; files per project | H1 | H1; H2; H3 |
| INV(e) line 95 | Content not processed | H1 | H1; H2 |
| INV(e) line 97 | Preview limits and processing time | H1 | H1; H2 |
| INV(e) line 99 | Inclusion and fixed-list size | H2 | H1; H2 |
| INV(e) line 100 | Confidence level | H1 | H1; H2 |
| INV(e) line 101 | Replace (Unique) limits | H1 | H1; H2 |
| INV(c) line 63 | Inclusion list on an existing entity | H2 | H1; H2 (see T5) |

  - Unchanged: INV(e) line 96 (PDF input types, CK1 R5 only), lines 98, 102 to 115 (already two or three headers or whole-service), and every other (c) row.
  - Effect on counts: none (cells only). The Covered-by panel counts a row once per header named.

### T5 — Inclusion-list placement (class a, M)
- Verdict: RESOLVED (proposal as suggested in the triage, with the limit bullet split per T42).
- Evidence: Inclusion Feature page (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/inclusion-feature.md): "The Inclusion Feature allows you to specify additional words or phrases that should be detected and anonymised under an existing entity type." The page is about an existing built-in entity (CK1) and, in its "See Also", about new fixed-list entities (CK2): "The Inclusion Feature can also be used to create entirely new custom entities with a fixed list of words to detect."
- Label to use: `[Documented]` for both quotes.
- Draft impact:
  - INV(c) line 63 Covered-by: `Cloak: Free-text PII detection and anonymisation; Cloak: Custom entity detection in free text (lists, regex and LLM)`.
  - CK1 R6 A:97: replace by the three bullets in T42 (entries, words, matching).
  - CK2 R1 B:14 and R6 B:95 to B:96: keep (the fuller pair of limit quotes lives there).
  - Summary change: none.

### T6 — Inventory row counts and build config (class a, M)
- Verdict: RESOLVED (counts re-run: tables 10, 7, 26, 9, 25, 4 = 81 rows today, as in the triage).
- Evidence: parse of `cloak_inventory.md` (rows between each table separator and the next heading) gives (a) 10, (b) 7, (c) 26, (d) 9, (e) 25, (f) 4. `check_drafts.py columns cloak_cols_a.md`: 0 errors, 0 warnings.
- Label to use: not a fact label.
- Draft impact: counts after this resolution file: (a) 10, (b) 8 (T7 adds the planned Sentinel row), (c) 26, (d) 9, (e) 28 (T15 adds three rows: Schedule 4.2, clause 6.1, Privacy Statement paragraphs 4 and 5.1.5), (f) 4: 85 rows. If main or the merger declines the three T15 rows, (e) stays 25 and the total is 82. `gr-xlsx-writer` BLOCKS for the new sheet: `(a)` 10, `(b)` 8, `(c)` 26, `(d)` 9, `(e)` 28 (or 25), `(f)` 4; `covered` header `Covered by Table 3 column`; markers tuple `— (legacy, not in Table 3)`, `— (planned, not in Table 3)`, `— (inventory only, not in Table 3)`. No other change.

### T7 — Planned "Sentinel integration" row for INV(b) (class a, M)
- Verdict: RESOLVED (row text below; no date or status beyond "coming soon" is published).
- Evidence:
  - Playbook, privacy improvements page at `45908b48` (https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx), line 27: "Direct integration with the Sentinel API is coming soon." Lines 80 to 84, tab "Sentinel (Cloak)": "# Coming soon — Sentinel + Cloak integration is on the roadmap." The raw file at `97338569` (main) is identical. The deployed page (https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/, HTTP 200, observed 2026-10-10) carries the same two statements.
  - Absence: `https://www.aiguardian.gov.sg/docs` and `https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails` (HTTP 200 each, observed 2026-10-10): the text has no "cloak" hit; `https://govtech-responsibleai.github.io/playbook/tools/sentinel/` also has no hit.
  - Sentinel's own PII check is column SN6 (`sentinel_two_level.md` line 650), header `GovTech Sentinel: PII detection and masking (AWS Bedrock)` (sheet 3 column AF).
- Label to use: statements `[Documented: repo govtech-responsibleai/playbook@45908b48]`; absence in Sentinel docs `[Not disclosed]`.
- Draft impact: insert as row 8 of INV(b), after line 34 (the block has 8 columns: Path | Audience | Security level or sign-in | Data classification ceiling | Applies to | Caveats and status | Covered by Table 3 column | Source URL):
  - `| Sentinel integration (planned) | Sentinel API users: "Direct integration with the Sentinel API is coming soon." [Documented: repo govtech-responsibleai/playbook@45908b48] (playbook privacy improvements page) | Not stated [Not disclosed] (checked the playbook page, aiguardian.gov.sg /docs and /docs/wiki/Sentinel-Guardrails for "cloak"; no hit, observed 2026-10-10) | Not stated [Not disclosed] (same checks) | PII detection and masking on Sentinel traffic; the Sentinel sheet column is GovTech Sentinel: PII detection and masking (AWS Bedrock) (sheet 3, column AF) [Inferred] (premise: the playbook lists Cloak under "Detection tools" for PII and shows the planned integration under the Sentinel tab) | Planned, no date given. Code stub: "# Coming soon — Sentinel + Cloak integration is on the roadmap." [Documented: repo govtech-responsibleai/playbook@45908b48] (playbook, tab Sentinel (Cloak)). The deployed playbook page states the same [Documented] (observed 2026-10-10). Whether a Sentinel guardrail for Cloak exists today [Not disclosed] (checked the Sentinel docs pages above) | — (planned, not in Table 3) | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx ; https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/ ; https://www.aiguardian.gov.sg/docs ; https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails |`
  - INV(b) intro paragraph (line 24): append `The last row records a planned integration with Sentinel, not a current path.`
  - INV(b) row count 7 to 8; config marker `— (planned, not in Table 3)` (R011); the planned marker cell makes it count in the planned counter only.
  - CK1 R4 A:69 and A:70: no change (already correct, label `[Documented: repo govtech-responsibleai/playbook@45908b48]`; its R9 blob URL at A:183 matches the ref).
  - Summary change: none.

### T8 — C3 access wording: "dedicated internal service" against "select non-government entities" (class a, M)
- Verdict: RESOLVED (two attributed bullets, each with its own label, plus a note naming the conflict).
- Evidence:
  - Playbook at `45908b48`, line 27: "Cloak — GovTech's dedicated internal service for comprehensive and localised PII detection (names, addresses, etc.)." (`[Documented: repo govtech-responsibleai/playbook@45908b48]`).
  - Cloak Guide home (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md): "is open to select non-government entities (e.g. public healthcare)." FAQ (faqs.md): "Cloak is also available to select non-WOG users, including public healthcare institutions and data contributors to agency projects."
- Label to use: playbook sentence `[Documented: repo govtech-responsibleai/playbook@45908b48]`; docs sentences `[Documented]`.
- Draft impact:
  - CK1 R6: after A:108 (as split in T73) add two bullets:
    - `• Who may use it, Cloak Guide: Cloak "is open to select non-government entities (e.g. public healthcare)" (Cloak Guide, home page); the playbook words it differently, see the next bullet **[Documented]**`
    - `• Who may use it, playbook: "GovTech's dedicated internal service for comprehensive and localised PII detection" (Responsible AI playbook, privacy improvements page) **[Documented: repo govtech-responsibleai/playbook@45908b48]**`
    - (the playbook blob URL is already in CK1 R9 at A:183; "see the next bullet" can be dropped by the merger if it prefers; the note naming the conflict goes in `cloak_changes.md`).
  - INV(b) non-WOG row (line 29), Audience cell: append `. The playbook calls Cloak "GovTech's dedicated internal service for comprehensive and localised PII detection" [Documented: repo govtech-responsibleai/playbook@45908b48]; the Cloak Guide home page says it "is open to select non-government entities (e.g. public healthcare)" [Documented] (HOME)`; Source URL cell: append ` ; https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx`.
  - CK2 R8 B:138: keep as is (the question stays; add nothing).
  - Summary change: none.

### T33 — "Newest release note" wording (class a, M)
- Verdict: RESOLVED. The release notes list v2.2.2 (4 August 2024) above v2.2.1 (28 August 2024); v2.2.0 and v2.1.9 are both 07 August 2024.
- Evidence (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md): "## `v2.2.2` (Released on 4 August 2024)", "## `v2.2.1` (Released on 28 August 2024)", "## `v2.2.0` (Released on 07 August 2024)", "## `v2.1.9` (Released on 07 August 2024)".
- Label to use: the version and date facts `[Documented]`; the deployed version `[Not disclosed]`.
- Draft impact:
  - CK1 R4 A:64: replace by the three bullets in T36 (the first states highest version and latest dated entry).
  - CK2 R4 B:67, replace with: `• Release history: the release notes name no LLM entity, so the deployed version and the LLM entity's release date are not given (checked the release notes page in full; highest version v2.2.2 of 4 August 2024, latest dated entry v2.2.1 of 28 August 2024) **[Not disclosed]**`
  - CK2 R8 B:128: replace "the newest release note is v2.2.2 of August 2024" with "the release notes end at v2.2.2 and v2.2.1 of August 2024".
  - CK3 R4 B:234, replace with two bullets: `• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) **[Documented]**` and `• The deployed version (checked the release notes page in full, the home page and the portal pages; not stated) **[Not disclosed]**`.
  - Summary change: none.

### T35 — CK3 R4 Summary "Hosting is Government Commercial Cloud" without the expansion in CK3 Detail (class a, M)
- Verdict: RESOLVED (add a bullet; the Summary stays).
- Evidence: FAQ (faqs.md): "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment". Portal Features and Roadmap: "AWS GCC 2.0".
- Label to use: `[Documented]`.
- Draft impact: CK3 R4, after B:231 add `• Hosting: "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment" (Cloak Guide, key FAQs) **[Documented]**`. Summary B:216 unchanged (39 words). Summary change: none.

### T48 — Mask page conflict inside one page (class a, M)
- Verdict: RESOLVED (two labelled facts, one per part of the page; neither side chosen).
- Evidence (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/masking/intro.md): Usage Guide table "Suffix: masks the starting characters" and "Prefix: masks the ending characters"; defaults "Number of Characters" 3, "Masking Type" Suffix, "Masking Character" -. Example table: "120414 | 120*** | Transforms into a suffix masked value" and "120414 | ***414 | Transforms into a prefix masked value".
- Label to use: each `[Documented]` (same page, different parts).
- Draft impact:
  - INV(d) Mask row (line 78), Parameters cell: replace the last two sentences with `Masking Type table: "Suffix: masks the starting characters" and "Prefix: masks the ending characters" [Documented] (MASK, Usage Guide table). Example table: 120414 becomes 120*** and is described as "Transforms into a suffix masked value" [Documented] (MASK, Example table). The two parts of the page read opposite ways on which end Suffix masks; neither is chosen here`.
  - CK1 R6 A:98, replace with five bullets: `• Mask defaults: Number of Characters 3, Masking Type Suffix, Masking Character "-" (Cloak Guide, masking page, Usage Guide table) **[Documented]**`; `• Masking Type table: "Suffix: masks the starting characters" and "Prefix: masks the ending characters" (Cloak Guide, masking page) **[Documented]**`; `• Masking page example: 120414 becomes 120*** and is described as "Transforms into a suffix masked value", which reads the other way from the Masking Type table (Cloak Guide, masking page, Example table) **[Documented]**`; `• Alias is "only available for the PERSON entity type" (Cloak Guide, Alias page) **[Documented]**`; `• Alias options Context and Offset both default to On (Cloak Guide, Alias page) **[Documented]**`.
  - Summary change: none.

### T50 — Reversibility labelled two ways (class a, M)
- Verdict: RESOLVED (one convention). R020 ruling 1: a statement that something is not published is `[Not disclosed]` with what was checked; `[Inferred]` is for scope or purpose conclusions drawn from a feature list (R015). "Replace, Redact and Mask cannot be reversed" is an absence conclusion, so it becomes `[Not disclosed]`, matching CK3 R2 B:196 and R8 B:290. Documented definitions beside it keep their own label.
- Evidence: Replace page (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace.md): "Replaces the identified original value with the replaced value that you entered." Redact page: "Detected entities will be replaced with a blank." Masking page: "Masking hides characters of a data value". None of the three pages mentions a key, mapping or restore step (read in full today). Pseudonymisation page: "irreversible hashing" (stays `[Documented]`). Encrypt page: "requires a cryptographic key as an input for both encryption and decryption" (stays `[Documented]`).
- Label to use: `[Not disclosed]` for Replace, Redact and Mask; unchanged for Replace (Unique), NRIC masking, Alias (already `[Not disclosed]`), Pseudonymise and Encrypt (`[Documented]`), Decrypt (`[Inferred]`, a scope reading from the FTDC and PSEU pages).
- Draft impact: INV(d), Reversible cell:
  - Replace (line 75): `Not stated [Not disclosed] (checked REPL, USE and RUNQ: they describe replacement by a tag or word and mention no key, mapping or restore step)`.
  - Redact (line 77): `Not stated [Not disclosed] (checked REDA: it says detected entities "will be replaced with a blank" [Documented] and mentions no key, mapping or restore step)`.
  - Mask (line 78): `Not stated [Not disclosed] (checked MASK: it describes hiding characters and mentions no key or mapping)`.
  - CK3 R2 B:196 and R8 B:290: no change.
  - Summary change: none.

### T69 — URLs and HTTP facts for P9 (class a, M)
- Verdict: RESOLVED (statuses observed today; replacement for the 404 Presidio tutorial URL found).
- Evidence (GET without credentials, 2026-10-10; "final" = after redirects):

| URL | Status | Used in |
|---|---|---|
| https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ | 302 to .../auth/otp-login#/?originalPath=/docs/cloak-api-guide/&redirect_reason=not_logged_in, final 200 | CK1 R9 A:174, CK2 R9 B:166, CK3 R9 B:312, INV(b) |
| https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/ | 302 to the same login page (originalPath openapi), final 200 | CK1 R9 A:175, INV(b) |
| https://docs.developer.tech.gov.sg/docs/cloak-anonymiser-package-guide/?product=Cloak | 302 to login, final 200 | INV(a) line 18 |
| https://docs.developer.tech.gov.sg/docs/cloak-api-guide/sections/helper-scripts/secure-internet-api-decryption-freetext | 302 to login, final 200 | linked from the decryption page; INV(b), INV(a) |
| https://www.cloak.gov.sg/packages | 307 to https://www.cloak.gov.sg/sign-in, final 200 | INV(a) line 18, INV(b) line 34 |
| https://go.gov.sg/cloak-terms | 302 to https://file.go.gov.sg/cloak-terms.pdf, final 200 | INV(b), INV(e), CK R9 uses the file URL |
| https://go.gov.sg/cloak-privacy | 302 to https://file.go.gov.sg/cloak-privacy.pdf, final 200 | INV(e) line 114 |
| https://go.gov.sg/cloak-open-source | 302 to https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/credits, final 200 | new (T20) |
| https://www.cloak.gov.sg/terms | 404 | FAQ link (HTTP fact, INV(b), INV(e)) |
| https://microsoft.github.io/presidio/tutorial/12_encryption/ | 404 | ENCR link (HTTP fact), INV(d) line 82, INV(f) line 124 |
| https://presidio.dataprivacystack.org/tutorial/12_encryption/ | 200 ("Example 12: Encryption and decryption") | replacement for the Source cells |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption-secret-sharing/intro-to-decryption.md | 404 (home page link; the working path is .../sections/decryption/intro-to-decryption.md, 200) | HTTP fact (C8) |
| https://www.cloak.gov.sg, /register, https://mirage.gov.sg, microsoft.github.io/presidio/supported_entities/, presidio.dataprivacystack.org/project_transition/, portal overview and getting-started pages | 200 | as listed |

- Label to use: `[Documented]` with the plain text "(HTTP 302 to … observed 2026-10-10)" for each redirect or 404 (README section 3 rule 7).
- Draft impact:
  - INV(d) Encrypt row (line 82) Source URL cell and INV(f) Presidio row (line 124) Source URL cell: replace `https://microsoft.github.io/presidio/tutorial/12_encryption/` by `https://presidio.dataprivacystack.org/tutorial/12_encryption/` (the successor org is official per R016; the Cloak page's own link stays recorded as the 404 HTTP fact in the cell text). Keep the sentence "the tutorial link returned HTTP 404 on 2026-10-10"; append `; the tutorial is served at presidio.dataprivacystack.org/tutorial/12_encryption/ (HTTP 200, observed 2026-10-10)`.
  - Exceptions list for `cloak_url_check.txt` (expected non-200 or redirects, not defects): the four docs login redirects, www.cloak.gov.sg/packages (307), the go.gov.sg short links (302), www.cloak.gov.sg/terms (404, a vendor-side broken link), the Cloak home-page decryption link (404), and the old Presidio tutorial URL (404, only as a recorded HTTP fact, no longer a Source URL).
  - R9 lists: no change (the file.go.gov.sg PDF URL returns 200).
  - Summary change: none.

### T70 — Process and session language in deliverable text (class a, M)
- Verdict: RESOLVED (replacement text per occurrence). README section 4: finals contain no process language and no instructions to the reader.
- Evidence: README section 4 ("Final files contain no `## Reviewer notes`, no process language ... and no instructions to the reader") and mechanical grep today (the occurrence list below).
- Label to use: labels unchanged unless stated.
- Draft impact:
  - CK1 R6 A:109: delete ", read with pypdf" so it ends `(Terms of Use, Schedule clause 4.6, dated 24 July 2024)`. A:120: replace `(read with pypdf, dated 24 July 2024)` with `(Terms of Use dated 24 July 2024)`.
  - CK1 R7 A:125, replace with `• Sensitive test data (real personal data) is a bench-design question; a bench could start with made-up values, and Terms Schedule 4.6 sets a data ceiling for anything uploaded (see R6) **[Inferred]**`.
  - CK1 R8 A:129: see T9.
  - CK2 R7 B:116, replace with `• Terms clause 3.4.7 lists "perform any benchmarking tests or analyses of the Service" among the things the user shall not do, so a bench could first seek GovTech's written view **[Inferred]**`.
  - CK2 R7 B:122 and CK3 R7 B:278: delete the bullet (it only reports that nothing was run); each R7 keeps its `**Minimum setup:**` bullet and the others.
  - CK3 R7 B:272: replace the tail `(licensing items, not interpreted here)` with `(the clauses are quoted in R8)`.
  - CK2 R8 B:126 and CK3 R8 B:282: see T9.
  - CK3 R2 B:199, replace with `• Presidio's reversible route is covered in the column Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt) (premise: both products offer an encrypt and a decrypt step) **[Inferred]**`.
  - CK3 R4 B:228, replace with `• Salts, page text: "Custom salt values will be included in the future." (Pseudonymisation page); the release notes list custom salts in v2.1.0 and v2.1.4 **[Documented]**`.
  - INV scope paragraph (line 3): replace "are not read (read-only rule)" with "return a login redirect (HTTP 302 then a 200 login page, observed 2026-10-10), so their content is [Not disclosed]"; delete "text read with pypdf" after TERMS and "(default column split, open at CP1)"; replace "Covered-by headers are the three Table 3 headers CK1 to CK3 (...); a cell with several headers separates them with a semicolon." with "A Covered by cell carries one or more of the three Table 3 headers of this product, separated by a semicolon, or one marker."
  - INV(a) MDG row (line 17), Status cell: see T64 for the replacement of "are not reconciled here". INV(a) Mirage row (line 19), Data cell: delete the sentence "Mirage is not mined further in this inventory [Inferred] (premise: scope decision for Cloak research, not a Mirage fact)".
  - INV(b) API onboarding row (line 33), Audience cell: replace "The form link was not opened (read-only rule)" with "The onboarding form itself is not public documentation and is not described here [Not disclosed]" (the form is an external form page that was never opened; the fact that it was not opened is not an evidence label).
  - INV(e) intro (line 87): replace "Terms rows quote clauses as written and carry no interpretation." with "Terms rows quote clauses as printed."
  - INV(e) line 103: replace "(TERMS, 15 pages read with pypdf)" with "(TERMS, Schedule 4.6)" (see T13). INV(e) line 114: replace "(PRIV, 4 pages read with pypdf)" with "(PRIV)".
  - Reviewer-note sections and the Self-check are removed at merge (README section 2).
  - Summary change: none.

### T71 — Internal ids in column text (class a, M)
- Verdict: RESOLVED (replace each id with the exact header text, README "Headers and IDs").
- Evidence: README section 4, "Headers and IDs": a header is identical in every file; ids are internal.
- Label to use: unchanged.
- Draft impact:
  - CK1 R1 A:13: `Custom entities (CK2 mechanisms) are a separate function:` becomes `Custom entities are a separate function, covered in the column Cloak: Custom entity detection in free text (lists, regex and LLM):`.
  - CK1 R3 A:50: replaced under T57 (the "a CK3 mechanism" wording goes).
  - CK1 R4 A:62: `LLM-enabled custom entity (CK2 mechanism, Beta):` becomes `LLM-enabled custom entity (Beta; see Cloak: Custom entity detection in free text (lists, regex and LLM)):`. A:63: `Encrypt technique (CK3 mechanism):` becomes `Encrypt technique (see Cloak: Reversible anonymisation and decryption (encrypt and restore)):`.
  - CK1 R6 A:102: `(CK3 mechanism, Encrypt with a shared secret)` becomes `(see Cloak: Reversible anonymisation and decryption (encrypt and restore))`. A:107: `Regex custom entity, API only (CK2 mechanism):` becomes `Regex custom entity, API only (see Cloak: Custom entity detection in free text (lists, regex and LLM)):`.
  - INV scope (line 3): covered by T70 ("CK1 to CK3" goes).
  - Summary change: none.

### T72 — Cross-reference limit: one Presidio pointer per row, no restated Presidio facts (class a, M)
- Verdict: RESOLVED.
- Evidence: brief section "Cross-reference, do not duplicate" (`cloak_brief.md`); CK3 R4 has three Presidio-related bullets (B:221, B:232, B:233) and states a Presidio token-layout fact without a Presidio source; CK2 R4 B:73 states a fact about Presidio's recognisers.
- Label to use: Cloak-side facts keep their labels; Presidio-side claims are dropped.
- Draft impact:
  - CK3 R4 B:221, replace with `• That example decodes to 16 bytes, one AES block, so the token seems to carry no separate initialisation vector, which the Secrets Manager holds with the key (premise: base64 arithmetic and the Secrets Manager text "secret key and IV value") **[Inferred]**` (the Presidio clause goes).
  - CK3 R4 B:232 (split, T73): `• Encrypt page: "Microsoft Presidio has a built-in encryption functionality, to encrypt and decrypt identified entities." (Cloak Guide, Encrypt page) **[Documented]**` and `• The Encrypt page's link to microsoft.github.io/presidio/tutorial/12_encryption/ returned HTTP 404 on 2026-10-10 **[Documented]**`.
  - CK3 R4 B:233, replace with the single cross-reference: `• Whether Cloak's Encrypt is Presidio's encrypt operator is not stated by any GovTech page; the Encrypt page's wording and AES-CBC point that way (premise: the Encrypt page text above; see Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)) **[Inferred]**`.
  - CK2 R4 B:73, replace with `• Cross-reference: see Presidio: Custom-recognizer detection (regex patterns, deny lists, ad-hoc recognizers); no GovTech page says Cloak's custom entities are Presidio recognisers (premise for any link: the shared terms "custom recognisers" and "context words") **[Inferred]**`.
  - CK1 R4 A:68 (383 characters), shorten to `• Cloak shares tag names such as PERSON, EMAIL_ADDRESS, PHONE_NUMBER and IBAN_CODE with Presidio's catalogue, which could mean reuse of Presidio recognisers; see Presidio: PII detection in text (Analyzer) **[Inferred]**`.
  - R2 B:199 and R7 B:277 (one pointer each) stay.
  - Summary change: none.

### T11 — Terms clauses 3.4.9 and 3.4.11 against Secrets Manager sharing (class c, M)
- Verdict: RESOLVED as a verbatim record, no interpretation. "License keys" is not defined in the Terms (the phrase occurs once, in 3.4.9).
- Evidence: Terms PDF page 3: "3.4.9. transfer assign or permit the sharing of license keys to or with a third party;" and "3.4.11. provide third party access to the Service; or". Secrets Manager page (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/secrets-manager.md): "You can share with up to 10 other users per operation, and with a maximum of 50 users per secret." and "Members of shared secrets will not be able to view or access the secret key and IV value, but will be able to use it to decrypt data." Terms 3.4 lead-in as in T9.
- Label to use: all `[Documented]`; whether secret sharing falls under 3.4.9 `[Not disclosed]` (the Terms do not say what a "license key" is; checked 15 pages and the Secrets Manager page).
- Draft impact:
  - CK3 R8 B:283 and CK1 R7 A:120: wording as in T70 (no "read with pypdf"); R8 B:283 ends `; whether secret sharing between test accounts is affected is not stated (the Terms do not define "license keys"; the Cloak guide describes sharing secrets among Cloak users)`.
  - INV(e) line 109: Applies-to cell append `. "License keys" is not defined in the Terms [Not disclosed] (checked the 15 pages); the Secrets Manager shares secrets with "up to 10 other users per operation" [Documented] (SECR)`.
  - Summary change: none (R7 CK3 Summary B:268 names the clause set; unchanged).

### T12 — Schedule 2.2 and the FAQ "no separate agreement" (class c, M)
- Verdict: RESOLVED (FAQ quote added; "Agency" is undefined).
- Evidence: Terms PDF page 14, Schedule 2.2: "You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency." and, in the same clause, "the Terms of Use bind you individually and you will be personally responsible for use of this Service." Clause 1.5: "If you are accessing or using the Service for and on behalf of another entity (such as your employer), you warrant and represent that you have the necessary authority to bind such entity to these Terms of Use." FAQ (faqs.md): "Users do not sign a separate agreement or contract. All users are legally bound by Cloak's Terms of Use."
- Label to use: `[Documented]` for all three; "Agency" undefined `[Not disclosed]` (see T10).
- Draft impact:
  - INV(e) line 111 (Schedule 2.2 row), Applies-to cell: append `. The FAQ says "Users do not sign a separate agreement or contract. All users are legally bound by Cloak's Terms of Use." [Documented] (FAQ). Clause 1.5 says a user acting for another entity warrants "the necessary authority to bind such entity to these Terms of Use" [Documented] (TERMS, clause 1.5)`.
  - CK1 R7 A:119 and CK3 R8 B:284: no change.
  - Summary change: none.

### T13 — Schedule 4.6 data ceiling and the FAQ wording (class c, M)
- Verdict: RESOLVED. The backslash is printed in the PDF (page 15 rendered to an image and read; PyMuPDF text also gives `\`), so it is not an extraction artefact. The meaning of "above" is not interpreted.
- Evidence: Terms PDF page 15, Schedule 4.6: "You shall not upload any information, data and material that are classified above the following classifications: Confidential (Cloud-Eligible) \ Sensitive (High)". FAQ (faqs.md): "for use of Government data classified up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)". Tabular usage guide (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/tabular/usage-guide.md): "Cloak supports datasets classified up to Confidential (Cloud-Eligible) and/or Sensitive (High)." Unstructured intro: "safe for data classified up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)".
- Label to use: `[Documented]` for each wording (three official statements worded differently; written as separate facts).
- Draft impact:
  - INV(e) line 103 (Data-classification ceiling): value cell, replace "(TERMS, 15 pages read with pypdf)" with "(TERMS, Schedule 4.6; the backslash is printed in the PDF)". Applies-to cell: "The tabular usage guide gives the same wording [Documented] (TABU)" becomes `The tabular usage guide says "Cloak supports datasets classified up to Confidential (Cloud-Eligible) and/or Sensitive (High)" [Documented] (TABU)`.
  - CK1 R6 A:109, CK2 R6 B:108, CK3 R6 B:264: no further change (CK2 and CK3 already give both wordings; T70 handles A:109).
  - Sensitive test data stays a bench-design question (R019).
  - Summary change: none.

### T14 — Privacy Statement against the FAQ retention (class c, M)
- Verdict: RESOLVED (both sources quoted; the Privacy Statement states no retention period).
- Evidence (https://go.gov.sg/cloak-privacy, 302 to https://file.go.gov.sg/cloak-privacy.pdf, dated 1 December 2022, 4 pages): paragraph 4 "Your data may be stored in our servers, systems or devices, in the servers, systems or devices of our third party service providers or collaborators"; paragraph 5.1.5 "for the purposes of storing or creating backups of your data (whether for contingency or business continuity purposes or otherwise), whether within or outside Singapore"; Annex 2.2 "Dataset uploaded by user for purposes of data anonymisation/transformation." FAQ (faqs.md): "Cloak does not retain data. Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request." Portal FAQs (https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/faqs, read today): "Raw data is deleted after anonymisation, and anonymised data is kept for up to 24 hours or removed upon user request." Terms Schedule 4.2 as in T15.
- Label to use: all quotes `[Documented]`; a retention period in the Privacy Statement `[Not disclosed]` (checked all 4 pages); whether the Privacy Statement paragraphs and the FAQ describe the same data `[Not disclosed]` (neither source relates them).
- Draft impact: INV(e) new row (see T15, row 3) and line 102 (Data retention), Applies-to cell: append `. The Privacy Statement gives no retention period [Not disclosed] (checked its 4 pages); see the Privacy Statement row`.
  - Summary change: none.

### T15 — Terms clauses 4.2 and 6.1, the definitions clause, and the Privacy Statement (class c, M)
- Verdict: RESOLVED, with one CORRECTION to the triage and to A RN-9: "routine deletion" is Schedule 4.2, not clause 4.2. Main-body clause 4.2 is about verifying identity. The definition of Public Sector Entities is inside clause 3.3 (T10); the Terms have no separate definitions clause; "Your Data" is defined in Schedule 4.1.
- Evidence (Terms PDF):
  - Schedule 4.1 (page 14): "all information, data and materials (including their derivatives) which GovTech may access or receive from you, in the course of providing the Service (“Your Data”)". Schedule 4.2: "GovTech may routinely delete any or all of Your Data from its systems after a reasonable period as from time to time determined by GovTech."
  - Clause 6.1 (page 6): "You hereby grant to GovTech a non-exclusive, worldwide, perpetual and royalty-free right to collect, use, disclose, process, modify, adapt, create derivative works of, reproduce, and sublicense any and all information or data submitted, uploaded or shared by you" and the clause continues "to the extent necessary to provide the Service or for any other purpose expressly or impliedly provided in these Terms of Use, or as permitted by law".
  - Clause 4.2 (page 4): "GovTech shall be entitled, but not obliged, to verify the identity of the person using the Service." Clause 11: "The Privacy Statement will form part of these Terms of Use."
  - Privacy Statement: see T14.
- Label to use: `[Documented]` for each quote; a retention figure in the Terms `[Not disclosed]` (Schedule 4.2 gives "a reasonable period" and no number; checked the 15 pages).
- Draft impact: add three rows to INV(e), after line 114 (columns Item | Value | Applies to | Covered by | Source URL; Covered by = all three headers; Source URL `https://go.gov.sg/cloak-terms` or `https://go.gov.sg/cloak-privacy`):
  - `| Terms Schedule 4.1 and 4.2 (routine deletion of Your Data) | "4.2. You acknowledge and agree that GovTech may routinely delete any or all of Your Data from its systems after a reasonable period as from time to time determined by GovTech." [Documented] (TERMS, Schedule 4.2). Schedule 4.1 defines Your Data as "all information, data and materials (including their derivatives) which GovTech may access or receive from you, in the course of providing the Service" [Documented] (TERMS, Schedule 4.1) | Whole service. A retention period in the Terms [Not disclosed] (Schedule 4.2 says "a reasonable period"; checked the 15 pages). The FAQ gives "purged within 24 hours" for anonymised data [Documented] (FAQ) | H1; H2; H3 | https://go.gov.sg/cloak-terms |`
  - `| Terms clause 6.1 (licence to GovTech over submitted data) | "You hereby grant to GovTech a non-exclusive, worldwide, perpetual and royalty-free right to collect, use, disclose, process, modify, adapt, create derivative works of, reproduce, and sublicense any and all information or data submitted, uploaded or shared by you" [Documented] (TERMS, clause 6.1, quoted to this point) | Whole service. The clause continues "to the extent necessary to provide the Service or for any other purpose expressly or impliedly provided in these Terms of Use, or as permitted by law" [Documented] (TERMS, clause 6.1) | H1; H2; H3 | https://go.gov.sg/cloak-terms |`
  - `| Privacy Statement paragraphs 4 and 5.1.5 (storage and backups) | Paragraph 4: "Your data may be stored in our servers, systems or devices, in the servers, systems or devices of our third party service providers or collaborators" [Documented] (PRIV). Paragraph 5.1.5: "for the purposes of storing or creating backups of your data (whether for contingency or business continuity purposes or otherwise), whether within or outside Singapore" [Documented] (PRIV) | Whole service, version dated 1 December 2022 [Documented] (PRIV). A retention period [Not disclosed] (checked the 4 pages). The FAQ says "Cloak does not retain data" [Documented] (FAQ); neither source relates the two [Not disclosed] (checked both) | H1; H2; H3 | https://go.gov.sg/cloak-privacy ; https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md |`
  - Replace each `H1`, `H2`, `H3` by the full header text. Each quote is under 40 words (the clause 6.1 value is cut with the note "quoted to this point").
  - Correct A RN-9 in `cloak_changes.md`: "Terms clauses 6.1 and 4.2 (data licence and routine deletion)" becomes "Terms clause 6.1 (data licence) and Schedule 4.2 (routine deletion)".
  - Row count (e): 25 to 28 (T6). Summary change: none.

### T36 — Release-note cross-check: v2.0.1 "added Word support" (class a, L)
- Verdict: RESOLVED. Both statements are true: v2.0.1 lists "[FTA] Added Word document support" and "[API] Reconstruct endpoint for FTA API"; v2.1.0 lists "[FTA] Added the ORGANIZATION entity type" under Improvements and "[FTA] Create and reuse project settings as templates" under Features.
- Evidence (release notes): "## `v2.0.1` (Released on 4 December 2023)" with "[FTA] Added Word document support" and "[API] Reconstruct endpoint for FTA API"; "## `v2.1.0` (Released on 19 Mar 2024)" with "[FTA] Create and reuse project settings as templates" and "[FTA] Added the ORGANIZATION entity type".
- Label to use: `[Documented]`.
- Draft impact: CK1 R4 A:64 becomes three bullets:
  - `• Release notes: the highest version is v2.2.2 (4 August 2024) and the latest dated entry is v2.2.1 (28 August 2024) (Cloak Guide, release notes) **[Documented]**`
  - `• Release notes: v2.1.0 (19 March 2024) lists the ORGANIZATION entity type and FTA templates (Cloak Guide, release notes) **[Documented]**`
  - `• Release notes: v2.0.1 (4 December 2023) lists "[FTA] Added Word document support" (Cloak Guide, release notes) **[Documented]**`
  - CK3 R3 B:210 stays. Summary change: none.

### T61 — Summaries near the cap (class a, L)
- Verdict: RESOLVED. Counts re-run with the checker's method (label excluded): no Summary exceeds limit minus 1 before or after the edits. CK1 R3 and CK3 R3 are at 44 (the allowed maximum) and are not edited.
- Evidence: counts today: CK1 R1 42, R2 33, R3 44, R4 33, R5 43, R6 38, R7 53, R8 33, R9 26; CK2 38, 32, 42, 34, 34, 42, 48, 39, 24; CK3 42, 33, 44, 39, 34, 38, 45, 37, 26. After the edits: CK1 R4 35, CK2 R4 35, CK2 R5 40, CK2 R6 43 (T42).
- Label to use: not a fact label.
- Draft impact: none beyond the Summary rewrites in T34, T59, T60 and T42; the merger re-runs `check_drafts.py columns ... --final --expect 3` and the Summary counts. Summary change: no further.

### T66 — "On [Inferred]" for 16 baseline rows (class a, L)
- Verdict: RESOLVED (upgrade for 16 rows with the quote below; the remaining rows keep their labels).
- Evidence: Usage guide (https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md), Step 2: "By default, Cloak scans your text for all available Entity Types and Replaces them with their data type as the default anonymisation technique."
- Label to use: `[Documented]` for the 16 rows PERSON, SG_NRIC_FIN, EMAIL_ADDRESS, PHONE_NUMBER, NRP, LOCATION, SG_PASSPORT, CURRENCY, CREDIT_CARD, SG_BANK_ACCOUNT_NUMBER, IBAN_CODE, IP_ADDRESS, URL, DATE_TIME, SG_UEN, ORGANIZATION. The three Address rows with "Default ON" stay `[Documented]` (ADDR table); SG_ADDRESS_STREET stays Off (ADDR "OFF (advanced)"); Exceptions, Inclusion list and the three custom-entity rows keep `[Inferred]` (their premise is a different page).
- Draft impact: INV(c) lines 42, 43, 44, 45, 46, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, Default state cell: replace `On [Inferred] (premise P-ON)` with `On [Documented] (USE, quoted in the scope paragraph as P-ON)`; INV scope paragraph: replace "P-ON = the premise that an entity is scanned by default: USE says" with "P-ON = the USE sentence on default scanning:". Summary change: none.

### T67 — C7 file-limit history (class a, L)
- Verdict: PARTLY RESOLVED. The v2.0.3 entries and the current limits are verbatim; which is current is not dated by any page (the usage guide and FAQ carry no date), so "the current usage guide is the later statement" stays an inference.
- Evidence: release notes "## `v2.0.3` (Released on 15 Jan 2024)": "[FTA] Support select columns from CSV files (Maximum 10 columns)" and "now can support up to 100k rows * 10 columns per CSV file." Usage guide: "Maximum 500 MB per file." FAQ: "CSV files up to 500 MB per file; PDF/DOCX files up to 200 MB per file." Tabular FAQ line: "Up to 100 selected columns, no limit on rows."
- Label to use: release-note and current limits `[Documented]`; "no FTA CSV column limit is stated on the usage guide or FAQ" `[Not disclosed]` (checked USE, FAQ and release notes through v2.2.2); which statement is current `[Inferred]`.
- Draft impact: INV(e) line 92 (CSV file size), Applies-to cell: replace the last sentence "the current usage guide is the later statement and gives no column limit for FTA CSV [Inferred] (premise: ...)" with `The usage guide and the FAQ give no column limit for FTA CSV files [Not disclosed] (checked USE, FAQ and the release notes through v2.2.2). The release note is dated 15 January 2024 and the guide pages are undated, so that the guide supersedes it is [Inferred] (premise: the Cloak Guide is the live documentation)`. Summary change: none.

### T68 — Pins (class a, L)
- Verdict: RESOLVED. All four component pins are the latest release tags today; the playbook staging pin still matches main.
- Evidence (`git ls-remote`, 2026-10-10): explosion/spaCy latest `release-v3.8.16` (26b4d1dc); data-privacy-stack/presidio latest `2.2.364` (779dbd28); Legrandin/pycryptodome latest `v3.24.0` (a0ed9b62); explosion/spacy-models `master` is `ca6f473afda3c4943d3919d3e39406c1b3f48b85` and the latest model tag is `en_core_web_sm-3.8.0` (374ece89), which has no `meta/` folder (HTTP 404 for the JSON at the tag), so the SHA pin stays. Raw reads at the pins: spaCy LICENSE "The MIT License (MIT) ... Copyright (C) 2016-2024 ExplosionAI GmbH, 2016 spaCy GmbH, 2015 Matthew Honnibal"; pycryptodome LICENSE.rst "The source code in PyCryptodome is partially in the public domain and partially released under the BSD 2-Clause license."; presidio LICENSE "The MIT License (MIT)"; `meta/en_core_web_sm-3.8.0.json` at `ca6f473a`: "license": "MIT" and the OntoNotes 5 source "license": "commercial (licensed by Explosion)". Playbook: `staging` 45908b48, `main` 97338569, files identical.
- Label to use: unchanged (`[Documented: repo explosion/spaCy@release-v3.8.16]` and the three others as drafted).
- Draft impact: none. INV(f) pins and the blob URLs stand; the playbook pin `45908b48` stays (R007 item 7; identical text at main). Summary change: none.

### T73 — Bullets with more than one fact under one label (class a, L)
- Verdict: RESOLVED (splits; A:64, A:98 and B:232 are given under T36, T48 and T72).
- Evidence: README section 3 rule 5.
- Label to use: each new bullet keeps the label of its fact.
- Draft impact:
  - CK1 R6 A:105: replace with `• API security levels: L2 (personalised token), L3 (system token), L4 (signature-based) (Cloak Guide, API guide) **[Documented]**` and `• API onboarding: an API key per security level; "complete our Cloak (API) Onboarding Form", and a key follows "within 1-2 business days" (Cloak Guide, API guide and key FAQs) **[Documented]**`. The FAQ wording is "you should be provisioned a key within 1-2 business days"; keep the quoted part exact.
  - CK1 R6 A:108 (access route plus pre-approval): replace with `• Web UI access: WOG users sign in with WOG-AD; other approved users register, and vendors complete TechPass onboarding after Cloak Ops approval (Cloak Guide, key FAQs and registration guide) **[Documented]**` and `• Non-government entities "Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step." (Cloak Guide, key FAQs) **[Documented]**`.
  - Summary change: none.

### T74 — INV short names used but not defined (class a, L)
- Verdict: RESOLVED. Checked every name inside a source hint against the scope paragraph: exactly TECHI, SAMPD, PRESTR, PRESENT, PRESENC are missing (APIGUIDE and APISPEC are defined).
- Evidence: scope paragraph (line 3) against the cells that use them: INV(d) intro (TECHI), INV(c) DATE_TIME row (SAMPD), INV(c) last row (SAMPD), INV(d) Encrypt row (PRESENC), INV(f) Presidio row (PRESTR, PRESENT, PRESENC).
- Label to use: not a fact label.
- Draft impact: INV scope paragraph, add to the short-name list: `TECHI = fta/anonymisation-techniques/intro.md; SAMPD = fta/custom-entities/custom-entities-unstructured/samples/datetime-specific.md; PRESTR = https://presidio.dataprivacystack.org/project_transition/ (the Presidio project transition page); PRESENT = https://microsoft.github.io/presidio/supported_entities/ (the Presidio supported-entities page); PRESENC = https://microsoft.github.io/presidio/tutorial/12_encryption/ (HTTP 404; the tutorial is served at https://presidio.dataprivacystack.org/tutorial/12_encryption/, HTTP 200, observed 2026-10-10)`. Summary change: none.

### T75 — Reviewer-note accuracy: side labels in CK3 R4 (class a, L)
- Verdict: RESOLVED. Count today of CK3 bullets in R1 to R7 (83): 13 start "Anonymise side" and 10 start "Restore side"; R1 2 and 2, R3 4 and 4, R5 3 and 2, R6 4 and 2; R2, R4 and R7 have none.
- Evidence: grep of `cloak_cols_b.md` lines 174 to 318 by row.
- Label to use: not a fact label.
- Draft impact: `cloak_changes.md` (the moved Reviewer note B RN-2) should read: "The anonymise side and the restore side are separate bullets in R1, R3, R5 and R6 (13 bullets start `Anonymise side`, 10 start `Restore side`); R2, R4 and R7 are not split by side, so a later split of CK3 would need a side added there (R037: one column; revisit only if the gated API shows a direction setting)." Summary change: none.

### T16 — Terms clause 9.1 and 9.1.1 beside the ">97% recall" claim (class c, L)
- Verdict: RESOLVED (quotes verified; both are shown side by side without comment).
- Evidence: Terms PDF page 8: "The Service is provided on an ‘as is’ and ‘as available’ basis without warranties of any kind." and 9.1.1 "as to the accuracy, completeness, correctness, currency, timeliness, reliability, availability, interoperability, security, non-infringement, title, merchantability, quality or fitness for any particular purpose of the Service". Cloak Guide home: ">97% recall for key PIIs like Name, NRIC and Email". FAQ: "Free-text detection is probabilistic, so 100% recall should not be assumed."
- Label to use: `[Documented]`.
- Draft impact: CK1 R5, after A:82 add `• Terms clause 9.1 says the Service is provided "on an 'as is' and 'as available' basis without warranties of any kind", and 9.1.1 lists accuracy, completeness and correctness among the warranties disclaimed (Terms of Use dated 24 July 2024) **[Documented]**`. INV(e) line 112 already quotes both. Summary change: none (CK1 R5 Summary has 43 words and is not touched).

### T17 — Terms clauses 3.4.6, 3.4.10 and 3.7 (class c, L)
- Verdict: RESOLVED (quotes verified verbatim; their relevance to a bench is not stated in the Terms).
- Evidence: Terms PDF page 3: "3.4.6. make the Service available in or through a network, file-sharing service, service bureau or any similar timesharing arrangement or as a managed service provider;", "3.4.10. use the Service to process or permit to be processed any code of a third party;", "3.7. You will not interfere or attempt to interfere with the proper working of the Service or otherwise do anything that imposes an unreasonable or disproportionately large load on GovTech’s servers."
- Label to use: `[Documented]`.
- Draft impact: none (INV(e) line 110 matches the PDF text; the straight apostrophe in "GovTech's" is the normalisation already stated in the scope paragraph). Summary change: none.

### T18 — Terms numbering 14 against 15 (class c, L)
- Verdict: RESOLVED. The PDF numbers the disputes clause 15 (15.1 to 15.3) and its cross-references read "clause 14.3" and "clause 14.2 above"; clause 14 is Severability and is one paragraph with no sub-clauses. Also, after 8.3.2 the PDF prints "4." where 8.4 is expected (a numbering slip in the source, not used).
- Evidence: Terms PDF pages 12 to 13: "15.2. Subject to clause 14.3, any dispute arising out of or in connection with these Terms of Use ..."; "15.3. GovTech may, at its sole discretion, refer any dispute referred to in clause 14.2 above to arbitration administered by the Singapore International Arbitration Centre"; "14. Severability".
- Label to use: the printed text `[Documented]`; which clauses the cross-references mean `[Inferred]` (premise: clause 15.2 is the courts clause and 15.3 refers to "any dispute referred to" there).
- Draft impact: INV(e) line 113 (Terms clause 15 row), Applies-to cell: replace the last sentence with `Clause numbers are as printed: 15.2 begins "Subject to clause 14.3" and 15.3 refers to "clause 14.2 above", while clause 14 is Severability with no sub-clauses [Documented] (TERMS). That the references mean 15.2 and 15.3 is [Inferred] (premise: 15.2 is the courts clause and 15.3 refers to "any dispute referred to" there)`. Summary change: none.

### T19 — Terms version and link currency (class c, L)
- Verdict: RESOLVED for the links; a later Terms version is `[Not disclosed]`.
- Evidence: the Cloak home page (https://www.cloak.gov.sg, HTTP 200) and its register page (https://www.cloak.gov.sg/register, HTTP 200) link "Terms of Use" to https://go.gov.sg/cloak-terms and "Privacy Statement" to https://go.gov.sg/cloak-privacy (page source, observed 2026-10-10); https://www.cloak.gov.sg/terms and /privacy return HTTP 404; go.gov.sg/cloak-terms returns HTTP 302 to https://file.go.gov.sg/cloak-terms.pdf (200); the PDF text reads "These Terms of Use are dated 24 July 2024." No page states a later version (checked the cloak.gov.sg home and register pages, the FAQ, the docs home page and the PDF).
- Label to use: link and date facts `[Documented]`; a later version `[Not disclosed]`.
- Draft impact: INV(e) line 114, Applies-to cell: append `. The cloak.gov.sg home and register pages link the Terms and the Privacy Statement through go.gov.sg/cloak-terms and go.gov.sg/cloak-privacy [Documented] (SITE, REGP, observed 2026-10-10); a later Terms version [Not disclosed] (checked SITE, REGP, FAQ and the PDF)`. Summary change: none.

### T20 — Component licences and the PyPI label (class c, L)
- Verdict: PARTLY RESOLVED. Licence texts at the pins are confirmed (T68). The PyPI row's "owner not named" is wrong: the PyPI page names an author and maintainers. The Terms also point to the Credits page as the vendor's own list of open-source components.
- Evidence:
  - Terms PDF page 14, Schedule 3: "Please see this link for a list of open source components used in the Service."; the link is https://go.gov.sg/cloak-open-source, HTTP 302 to https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/credits (200, 32 entries, no spaCy and no Presidio entry).
  - PyPI (https://pypi.org/project/pycrypto/, linked from the Credits page as the "crypto" source): "Author: Dwayne C. Litzenberger"; maintainers listed "amk" and "dlitz"; "Released: Oct 17, 2013"; "Last file added: Jun 20, 2014"; "License Public Domain (Public domain)"; "PyCrypto is written and tested using Python version 2.1 through 3.3."
  - Licence texts at the pins: see T68.
- Label to use: owner licence files `[Documented: repo <repo>@<ref>]` as drafted; PyPI facts `[Documented]` (PyPI page, linked from the Credits page, not GovTech docs); maintenance status `[Not disclosed]` (the PyPI page gives dates only).
- Draft impact:
  - INV(f) PyCrypto row (line 126): Owner cell becomes `PyPI project page pycrypto 2.6.1, author Dwayne C. Litzenberger, maintainers amk and dlitz [Documented] (PyPI project page, linked from CRED, not GovTech docs)`. Licence cell: append `. Released Oct 17, 2013; last file added Jun 20, 2014 [Documented] (PyPI pycrypto page, not GovTech docs). Current maintenance status [Not disclosed] (the PyPI page gives release dates and no maintenance statement)`; delete "(checked the project page text read)".
  - INV(f) intro paragraph (line 119): append `Terms Schedule 3 refers to "a list of open source components used in the Service" [Documented] (TERMS); the link go.gov.sg/cloak-open-source redirects to the Credits page [Documented] (HTTP 302 observed 2026-10-10).` Add `https://go.gov.sg/cloak-open-source` to the Source URL cells of the Presidio and spaCy rows only if the merger wants the absence evidence there; the Credits URL is already present.
  - "Built on Presidio" stays `[Inferred]` (T30). Summary change: none.

## Class (b) items: closing notes (no source answers them; listed where a ruling or a drafting edit applies)

- **T1, T2:** closed by R037 (three columns; CK3 one column, anonymise and restore bullets kept separate, revisit only if the gated API shows a direction setting). No further draft impact.
- **T21 to T26 (login-gated pages):** re-observed today, HTTP 302 to `docs.developer.tech.gov.sg/auth/otp-login` then 200 for the API Guide, OpenAPI page, package guide and free-text decryption helper script (T69 table). Still `[Not disclosed]` with the HTTP fact, as drafted. No change.
- **T40 (0.30 default on a caption):** re-read: confidence-level page caption "The expanded confidence level slider, set to the default value of 0.30." Stays `[Documented]` with the "image caption" source type named. No change.
- **T41 (confidence scope):** hygiene edit, no new fact. Replace CK1 R5 A:81 with two bullets: `• Developer Portal Features page: "Adjust detection sensitivity per entity type to balance recall and precision for your dataset" (Developer Portal, features page) **[Documented]**` and `• Cloak Guide: the Anonymisation Settings drawer has one "Adjust Confidence level" dropdown with a slider "set to the default value of 0.30" (Cloak Guide, confidence level page, captions) **[Documented]**`. INV(e) line 100, Applies-to cell: the `[Not disclosed]` fact stays and gains the two quotes as `[Documented]` facts (PF, CONF). R8 bullets keep the open question (global or per entity type).
- **T42 (limit unit, H):** main's ruling: Summary reads "500 (words or entries; the docs differ)" and the R8 question stays. Evidence (verbatim): fixed-list page "The CSV to be uploaded should contain a maximum of 500 words listed in the first column." and "Only the first 500 words in the CSV will be used."; Inclusion page "You can add words individually or upload a CSV file containing up to 500 entries." and "Only the first 500 words in a CSV upload will be used." Label `[Documented]` for each quote (the conflict is between official pages; both written). Edits: CK2 R6 Summary (B:93), replace with (43 words): `Summary: **A list, a regex or examples.** A list takes up to 500 (words or entries; the docs differ), a regex takes a pattern, and the LLM entity takes a definition and 3 to 5 examples. Context words and per-pattern scores are API only. **[Documented]**`. CK1 R6 A:97, replace with three bullets: `• Inclusion list on an existing entity: "You can add words individually or upload a CSV file containing up to 500 entries." (Cloak Guide, inclusion feature page) **[Documented]**`; `• Inclusion list limit as worded in the Important Notes table: "Only the first 500 words in a CSV upload will be used." (Cloak Guide, inclusion feature page; the same page gives the limit in entries and in words) **[Documented]**`; `• Inclusion list matching is "Word-sensitive" (exact spelling and punctuation must match) and "Not case-sensitive" (Cloak Guide, inclusion feature page) **[Documented]**`. INV(c) lines 63 to 64 and INV(e) line 99 already give both quotes. B:136 (R8) stays. Summary change: yes (CK2 R6).
- **T43 (LLM entity limit, per dataset against per project):** add the R8 bullet and the FAQ quote. CK2 R8 (after B:136): `• Whether the LLM-enabled custom entity limit is per dataset or per project (the unstructured intro says "only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)" and the FAQs say "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time"; needs testing)`. INV(e) line 98 (LLM limits), value cell: append `. The FAQ says "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time." [Documented] (FAQ); the unit differs from the LLMI wording (dataset against project) [Documented]`. Summary change: none (R8 CK2 Summary B:124 may add "the LLM entity limit unit"; it has 39 words and room for 4).
- **T52 (salts):** align INV(d) line 81 to CK3 (no conclusion): replace "the page wording is probably stale [Inferred] (premise: both statements sit on official pages and cannot both describe the current release)" with "which of the two statements is current is [Not disclosed] (both sit on official pages; checked PSEU, REL and SECR)". CK3 R4 B:228 to B:229 and R8 B:292 stay as drafted (T70 edits B:228).
- **T62 (Sentinel integration status):** re-checked: playbook text identical at staging and main; aiguardian.gov.sg /docs and /docs/wiki/Sentinel-Guardrails have no "cloak" hit; no date anywhere. Stays `[Not disclosed]` for a date or availability (T7 row records it as planned).
- **T64 (MDG):** the Mirage FAQ line is verbatim: "Mock Data Generation is available via API through Cloak (https://cloak.gov.sg)." (https://mirage.gov.sg); the Cloak portal Features page: "Generate mock data that mimics the structure and format of real datasets." INV(a) MDG row (line 17), Status cell: replace "Two official pages place MDG under different products and are not reconciled here:" with "Two official pages place MDG under different products, and the Mirage page adds that MDG "is available via API through Cloak" [Documented] (MIR);" and end the sentence with "how the two placements relate is [Not disclosed] (checked the Cloak Guide sidebar, the portal pages and both home pages)". Still no Cloak Guide MDG page.
- **T65 (status badge):** the portal overview prints "PROOF OF VALUE" next to "Cloak" and the same page describes a product in use (">5 million PIIs removed per month across WOG"); no page defines the badge. Stays `[Not disclosed]`; INV(a) rows 11 and 14 keep "Available [Inferred]" with the premise as drafted.
- **T27, T28 to T32, T37, T38, T44 to T47, T49, T51, T53 to T56, T58, T63:** no documentation answers them; unchanged and kept as R8 questions. T56 note: the deck's slide 23 says "Cloak’s Free Text Anon API is currently used to support >20 LLM products and use cases; >1m API calls made to date." (deck dated 11 September 2023, so the numbers are dated); the bullets that rely on the deck should carry the date (A:49 and B:245 already do or can add "dated September 2023").

## Report

- Counts: 39 items assigned (27 class a, 12 class c). RESOLVED 36, PARTLY RESOLVED 2 (T20, T67), CORRECTION 1 (T57), STILL OPEN 0. The CORRECTION item also has replacement text; it is counted once, as CORRECTION. T15 carries a second, smaller correction (clause 4.2 against Schedule 4.2) inside a RESOLVED verdict.
- CORRECTIONs: T57 (slide 22 does not show the response returning through the Transformer Module; CK1 R3 A:50 and CK3 R3 B:209 are wrong); T15 note (the "routine deletion" clause is Schedule 4.2; main-body clause 4.2 is identity verification; A RN-9 and the triage name it wrongly).
- Summaries that must change (new text above): CK1 R4 (T34), CK2 R4 (T59), CK2 R5 (T60), CK2 R6 (T42). No other Summary changes. New word counts 35, 35, 40, 43 (limit minus 1 is 44).
- New or changed inventory rows: block (b) +1 planned Sentinel row (T7); block (e) +3 rows (T15) if accepted; counts 10, 8, 26, 9, 28, 4 = 85 (or 82 without T15). Covered-by edits per T4 (INV(a) Templates, INV(c) Inclusion, INV(d) Decrypt, INV(e) 11 rows, INV(f) Presidio).
- Quote check (`benchtest/scratchpad/resolver/cloak1/quotecheck.py`): 271 quoted segments compared with the fresh copies after whitespace, typographic-quote, markdown-link and PDF line-break-hyphen normalisation. Every segment that quotes a source matches; the segments that do not match are proposed draft wording, field labels or paired fragments between two quotes, not source quotes. Two quotes that exceeded 40 words were split (T12) or trimmed (T15). No verbatim source quote in the Evidence lines exceeds 40 words.

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T3 | RESOLVED | process item | no |
| T4 | RESOLVED | process item | no |
| T5 | RESOLVED | [Documented] | no |
| T6 | RESOLVED | process item | no |
| T7 | RESOLVED | [Documented: repo govtech-responsibleai/playbook@45908b48]; [Not disclosed] | no |
| T8 | RESOLVED | [Documented] and [Documented: repo govtech-responsibleai/playbook@45908b48] | no |
| T9 | RESOLVED | [Documented]; permitted use [Not disclosed] | no |
| T10 | RESOLVED | [Documented]; "Agency" undefined [Not disclosed] | no |
| T11 | RESOLVED | [Documented]; scope of "license keys" [Not disclosed] | no |
| T12 | RESOLVED | [Documented]; "Agency" [Not disclosed] | no |
| T13 | RESOLVED | [Documented] | no |
| T14 | RESOLVED | [Documented]; retention period [Not disclosed] | no |
| T15 | RESOLVED (note: clause 4.2 is Schedule 4.2) | [Documented]; period [Not disclosed] | no |
| T16 | RESOLVED | [Documented] | no |
| T17 | RESOLVED | [Documented] | no |
| T18 | RESOLVED | [Documented]; cross-reference meaning [Inferred] | no |
| T19 | RESOLVED | [Documented]; later version [Not disclosed] | no |
| T20 | PARTLY RESOLVED | [Documented: repo <repo>@<ref>]; PyPI [Documented]; maintenance [Not disclosed] | no |
| T33 | RESOLVED | [Documented]; deployed version [Not disclosed] | no |
| T34 | RESOLVED | [Documented] | yes (CK1 R4) |
| T35 | RESOLVED | [Documented] | no |
| T36 | RESOLVED | [Documented] | no |
| T39 | RESOLVED | 17 groups [Documented]; 20 tags [Inferred] | no |
| T48 | RESOLVED | [Documented] | no |
| T50 | RESOLVED | [Not disclosed] (Replace, Redact, Mask) | no |
| T57 | CORRECTION | [Documented]; no restore step [Not disclosed] | no |
| T59 | RESOLVED | [Documented] | yes (CK2 R4) |
| T60 | RESOLVED | [Documented] | yes (CK2 R5) |
| T61 | RESOLVED | process item | no |
| T66 | RESOLVED | [Documented] (16 rows) | no |
| T67 | PARTLY RESOLVED | [Documented]; [Not disclosed]; [Inferred] | no |
| T68 | RESOLVED | [Documented: repo <repo>@<ref>] unchanged | no |
| T69 | RESOLVED | [Documented] (HTTP facts) | no |
| T70 | RESOLVED | labels unchanged | no |
| T71 | RESOLVED | labels unchanged | no |
| T72 | RESOLVED | [Inferred] and [Documented] as listed | no |
| T73 | RESOLVED | labels unchanged | no |
| T74 | RESOLVED | process item | no |
| T75 | RESOLVED | process item | no |
| T42 (class b, H) | stays open; Summary text per main | [Documented] (both quotes) | yes (CK2 R6) |
