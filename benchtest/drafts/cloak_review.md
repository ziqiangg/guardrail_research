# Cloak workbook: fresh verifier review

Date of checks: 2026-10-10. Reviewer: gr-verifier (did not draft, triage, resolve or merge).

Inputs read:
- CLAUDE.md and drafts/README.md.
- Rulings R037, R032, R019, R020, R015 and R011 in full; R002, R007, R009 and R021 as applied in the files.
- queue.md rows starting "cloak".
- cloak_two_level.md (CK1 to CK3) and cloak_inventory_final.md (85 rows), read in full.
- cloak_changes.md and the Summary, label and Report sections of cloak_resolutions_1.md, read in full.
- cloak_summaries_preview.md, compared mechanically with the final.
- The originals cloak_cols_a.md, cloak_cols_b.md and cloak_inventory.md were diffed with difflib, not re-read.

Sources re-read today:
- 37 Cloak Guide Markdown pages fetched raw with curl from https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/<path>.md, plus _sidebar.md (80 .md paths).
- With `python benchtest/tools/fetch_text.py`: www.cloak.gov.sg, the five Developer Portal Cloak pages, mirage.gov.sg, aiguardian.gov.sg /docs and /docs/wiki/Sentinel-Guardrails, the deployed playbook page, the Presidio project-transition page, the PyPI pycrypto page, the spaCy and PyCryptodome LICENSE files at their pins, and the playbook mdx raw at 45908b48c0a8b6d3855a154c0e41a12958a99205.
- The Terms PDF (go.gov.sg/cloak-terms, 302 to file.go.gov.sg/cloak-terms.pdf, 103170 bytes, 15 pages), the Privacy Statement PDF (4 pages) and the USENIX PEPR 2023 deck (32 slides) were downloaded and their text extracted with pypdf.
- Slide 22 of the deck was rendered with the Ghostscript already installed on this machine, to check the layout claim (T57) independently of the resolver's image.

No sign-in, no form, no call to any Cloak API, no install. Scripts and page copies are in benchtest/scratchpad/verifier/cloak/. No file other than this one and that folder was modified.

## Verdict: PASS WITH FIXES

The merge follows the triage, the resolutions, R037 and main's queue rows. Every substantive difference between the originals and the finals is in cloak_changes.md. Both finals pass the checker with 0 errors and 0 warnings. The inventory has 10/8/26/9/28/4 = 85 rows.

Covered-by is valid:
- Decrypt is CK3 only; Pseudonymise is CK1 and CK3; Inclusion is CK1 and CK2.
- The planned Sentinel row carries "— (planned, not in Table 3)".
- 7 cells are inventory only and 1 is legacy.
- 76 cells name headers, with 138 header mentions in total.

The known-wrong strings are gone: "GovTech's cloud", "learns from", "Transformer Module", "clause 4.2" for routine deletion, the old CK2 and CK3 header wording, "salts" in the CK3 header, "newest", "pypdf", "read-only rule", "not interpreted here", ruling ids, CK ids outside headings. Two leftovers of resolved items remain:
- the custom-entity Findings-table claim in CK2 R1 (T60);
- a "built on Presidio" inference in inventory (f) that is stronger than the columns and contradicts the block (c) intro (T30).

Spot-checks: I checked 46 facts at source, with 43 MATCH, 3 MISMATCH and 0 UNVERIFIABLE. One mismatch is the inline-reply wording in CK2 R3, one is the v2.1.0 salts wording in CK3 R4, and one is a portal attribution in CK1 R5.

URLs: of 84 distinct URLs, 78 return 200. The other 6 are the expected gated or short-link redirects listed in cloak_changes.md section 5b.

The main defect class is Summary entailment. Seven Summaries draw on facts that sit only in other rows of the same column. There are 14 required fixes. Two Summaries change by one word each; no headline number changes.

## Required fixes

1. **CK1 R1 Summary (line 3) is not entailed by its own Detail (lines 5 to 14).**
   - Problem:
     - The Summary says the tool detects "names, NRICs and addresses" in "pasted text or uploaded files" and that it "hashes" entities.
     - R1 Detail names no entity type: line 7 says only "all available Entity Types".
     - R1 Detail does not quote the pasted-text and file input; that quote is in R3 line 39.
     - R1 Detail lists Pseudonymise, not hashing (line 8).
   - Fix:
     - After line 6, add:
       - `• Inputs: "The tool supports pasted text input as well as file uploads (.csv, .pdf, .docx)." (Cloak Guide, intro to FTA) **[Documented]**`
       - `• Baseline entities: "Cloak detects and transforms 20+ baseline entity types (names, NRICs, addresses, dates, phone numbers, etc.)" (Cloak Guide, intro to FTA, image caption) **[Documented]**`
     - In the Summary, replace "aliases, hashes or encrypts them" with "aliases, pseudonymises or encrypts them". The Summary stays at 42 words.
   - Both quotes were re-read today in intro-to-fta.md.

2. **CK1 R2 line 22: an inferred tally inside a Documented bullet.**
   - Problem: the bullet ends "and the entity pages give 17 groups and 20 tags **[Documented]**". The 20-tag figure is the drafter's own tally; line 20 and inventory (c) both label it `[Inferred]` (README section 3 rule 5).
   - Replace line 22 with: `• Vendor count, version two: "Cloak detects 17+ entity types out of the box" (Developer Portal, FAQs, last updated 21 Aug 2026); the wording differs from the "20+" of version one **[Documented]**`

3. **CK2 R1 Summary (line 205) is not entailed: "in Beta, an LLM given a definition and examples".**
   - Problem: R1 Detail says "few-shot prompting" (line 211) but never says Beta, definition or examples. Those facts sit in R4 (line 261) and R6 (lines 296 and 297).
   - Fix: after line 211, add:
     - `• LLM route inputs: for the LLM-based approach the Custom page lists "Define your custom entity" and "Give some examples" (Cloak Guide, entity types, Custom) **[Documented]**`
     - `• LLM route status: the unstructured intro marks the feature "[Beta Feature]" (Cloak Guide, unstructured intro) **[Documented]**`
   - Both texts were re-read today (others/custom.md; custom-entities-unstructured/intro.md).

4. **CK2 R1 line 217: a leftover of T60 (custom matches in the Findings table).**
   - Problem: the bullet says that for a custom entity "the documented result is transformed text and a Findings table".
     - T60 established that the Findings table caption is about detected entities in general.
     - CK2 R5 line 280 says whether custom entities appear in it is `[Not disclosed]`.
     - The bullet is also an absence claim labelled `[Inferred]` (R020 ruling 1).
   - Replace line 217 with: `• A safe or unsafe verdict, or a score, for a custom entity (checked the custom entity pages and the FTA usage guide: they show only transformed output, and whether custom matches appear in the Findings table is not stated) **[Not disclosed]**`

5. **CK2 R2 Summary (line 219): "hospital names" is not in R2 Detail.**
   - Problem: R2 has the "10-digit hospital case number" (line 223). Hospital names occur only in R1 (line 209).
   - Fix: replace "hospital names" with "hospital case numbers" (33 words).

6. **CK2 R3 line 240: an inference under a Documented label, contradicted by the source.**
   - Problem: "The Web UI returns a download, not an inline reply". The usage guide shows the anonymised result inline: "Your Original Data is displayed on the left, and your Anonymised Data is displayed on the right", with preview limits. "not an inline reply" is the drafter's reading.
   - Replace line 240 with: `• Output delivery: "Once you are done with your transformations, click on Download to proceed with the download request." (usage guide) **[Documented]**`
   - The R3 Summary does not depend on the removed clause.

7. **CK2 R4 Summary (line 250) is not entailed: "few-shot LLM" and "prompted with 3 to 5 examples".**
   - Problem: R4 Detail (lines 252 to 271) has no few-shot or example-count bullet. T59 said "Detail unchanged (B:13, B:62, B:99 carry the quotes)", but B:13 is in R1 and B:99 is in R6.
   - Fix: after line 260, add: `• LLM method: "Cloak allows you to add such custom entities through few-shot prompting, which allows the LLM to detect new entities without fine-tuning. This approach only needs a small set of 3-5 examples (labelled data)" (unstructured intro) **[Documented]**`
   - The quote is 33 words and was re-read today in custom-entities-unstructured/intro.md.

8. **CK3 R1 Summary (line 374) is not entailed: "replaces each detected value with AES-256 CBC ciphertext".**
   - Problem: R1 Detail says "AES cypher in CBC mode" (line 376) but not AES-256 (only R4 line 418 does), and it says nothing about Encrypt being applied per detected entity.
   - Fix: after line 376, add:
     - `• Anonymise side, mode: "Due to security reasons, we have restricted encryption to only AES-256 CBC Mode Encryption." (Cloak Guide, Encrypt page) **[Documented]**`
     - `• Anonymise side, scope: the settings drawer sets "the corresponding anonymisation technique to be applied for each entity type" (Cloak Guide, usage guide) **[Documented]**`

9. **CK3 R2 Summary (line 386) is not entailed: "Encrypt is reversible".**
   - Problem: R2 Detail gives only the one-way side (line 392) and the shared-key aims.
   - Fix: after line 392, add: `• Encrypt is the reversible side: the cipher "requires a cryptographic key as an input for both encryption and decryption" (Cloak Guide, Encrypt page) **[Documented]**`

10. **CK3 R3 Summary (line 399) is not entailed: "or rows through the API".**
    - Problem: R3 Detail has only the Web UI single-value restore (lines 404 and 405). The API looping route is in R1 line 379.
    - Fix: after line 405, add: `• Restore side, bulk: for "multiple values or a file of encrypted data" the page points to the Free-Text Decryption API, "which supports looping through rows in a CSV" (free-text decryption page; the API page is behind a login) **[Documented]**`

11. **CK3 R4 line 427: v2.1.0 does not list custom salts.**
    - Problem: the line reads "the release notes list custom salts in v2.1.0 and v2.1.4". The release notes list "[FTA] Added salt parameter for Pseudonymisation transformation" in v2.1.0 and "[FTA] Support for custom salts and user managed salts" in v2.1.4. Line 428, R8 line 493 and inventory (d) already state this correctly.
    - Replace "the release notes list custom salts in v2.1.0 and v2.1.4" with "the release notes list a salt parameter in v2.1.0 and custom salts in v2.1.4".

12. **CK3 R7 line 474: Terms clauses paraphrased with interpretive verbs.**
    - This conflicts with main's queue row "Terms clauses verbatim with no interpretation" and with R037.
    - Problem: "Terms clause 3.4.7 bars ..., and 3.4.9 and 3.4.11 bar sharing licence keys or access with third parties". The CK2 R7 twin was reworded under T70 ("lists ... among the things the user shall not do"), but this one was not. "licence keys" also departs from the Terms' "license keys", and 3.4.11 is "provide third party access to the Service", not "sharing access".
    - Replace line 474 with: `• Terms clause 3.4 lists "perform any benchmarking tests or analyses of the Service" (3.4.7), "transfer assign or permit the sharing of license keys to or with a third party" (3.4.9) and "provide third party access to the Service" (3.4.11) among the things the user shall not do, so a bench could first seek GovTech's written view **[Inferred]**`

13. **Inventory (f), Presidio row, "Where a Cloak page names it" cell: an over-strong inference that contradicts block (c) and the columns.**
    - Problem: the cell ends "That Cloak is built on Presidio [Inferred] (premise: ...)". The positions elsewhere are weaker:
      - The block (c) intro says the tag-name match is "a cross-reference to sheet 3f only [Inferred] (premise: tag-name match, not a statement about Cloak's engine)".
      - CK1 R4 says only "could mean reuse of Presidio recognisers" and "No GovTech page says Cloak is built on Presidio [Not disclosed]".
      - CK3 R4 says "not stated by any GovTech page".
    - Replace "That Cloak is built on Presidio [Inferred] (premise: the tag names such as SG_NRIC_FIN and PERSON follow Presidio's style, the ENCR text, and the ENTI link; no GovTech page says it)" with: `Whether Cloak is built on Presidio is not stated by any GovTech page [Not disclosed] (checked ENTI, ENCR, CRED, HOME and the portal pages). The shared tag names such as SG_NRIC_FIN and PERSON, the ENCR text and the ENTI link could point to reuse of Presidio components [Inferred] (premise: name and wording match only)`
    - The text contains no `|`, `**` or backtick.

14. **Inventory scope paragraph (line 3) and block (a) FTA row "What it is": "does not return a score".**
    - Problem: the usage guide documents "the Findings table listing each detected entity with its type, transformation applied, original text, anonymised text, and confidence score", and CK1 R5 carries it. Two places say otherwise:
      - The scope paragraph says "it does not return a score or a verdict". The paragraph is not built, but the diagrammer reads it.
      - The FTA row says "does not return a verdict or a risk score [Inferred]". That is an absence claim labelled `[Inferred]`, while CK1 R1 line 12 labels the same absence `[Not disclosed]` (R020 ruling 1, T50 precedent).
    - Fix:
      - Scope paragraph: replace "it does not return a score or a verdict." with "it returns transformed text or files, the Web UI findings table lists a confidence score per detected entity, and no safe or unsafe verdict is described."
      - FTA row, "What it is": replace "It returns the transformed text or file and does not return a verdict or a risk score [Inferred] (premise: the FTAI and USE pages describe only an anonymised output and a findings table, no verdict field)" with `It returns the transformed text or file, and the Web UI findings table lists a confidence score per detected entity [Documented] (USE). A safe or unsafe verdict or a risk label [Not disclosed] (checked FTAI, USE, FAQ and HOME; no verdict field is described)`

For every fix:
- Log it in cloak_changes.md (section 2 or 3).
- Update the bullet counts in section 8b and in cloak_summaries_preview.md:
  - CK1 R1 goes from 10 to 12 bullets.
  - CK2 R1 goes from 11 to 13.
  - CK2 R4 goes from 20 to 21.
  - CK3 R1 goes from 9 to 11.
  - CK3 R2 goes from 10 to 11.
  - CK3 R3 goes from 13 to 14.
- Update the two changed Summaries (CK1 R1 at 42 words, CK2 R2 at 33 words).
- Re-run both checker commands.

## Optional suggestions

- **CK1 R5 line 86.** The quote ">97% recall for key PIIs like Name, NRIC and Email" is verbatim on the Cloak Guide home page only. The portal overview says "optimised for Singaporean PIIs with >97% recall like Names, NRICs, and Emails". Cite the home page alone, or quote both wordings.
- **CK1 R1 line 12.** The `[Not disclosed]` bullet begins with a positive fact ("The documented output is transformed text or files ..."). Split the positive fact into its own `[Documented]` bullet (R020 ruling 1).
- **CK3 R4 Summary (line 415).** "shares keys and salts without showing key material": the R4 bullet (line 421) speaks of the "secret key and IV value". To cover salts, add the Secrets Manager line "Keys and salts are stored securely and never exposed to shared users" as an R4 bullet.
- **CK2 R5 Summary (line 273).** "replaced, redacted, masked or otherwise transformed": R5 Detail names no Redact or Mask for custom entities. "replaced or otherwise transformed" would stay within the Detail. This is borderline, which is why it is not a required fix.
- **Inventory (f), Presidio row, licence cell.** "Cross-reference: see the Presidio inventory sheet 3f for components and licences; not re-read here": "not re-read here" is process wording in a built cell (README section 4). Drop it.
- **Inventory (d), Mask row.** "neither is chosen here" could read "neither is stated as correct".
- **Inventory (d), Covered-by cells of the Pseudonymise and Encrypt rows.** They use " ; " while every other cell uses "; ". The checker and COUNTIF accept both; harmonise for consistency.
- **Inventory (c), LLM row, Notes cell.** The cell starts with "[Beta Feature]:" outside quotation marks, which looks like a label form. Quote it: `"[Beta Feature]": 1 entity per dataset ...`.
- **CK1 R4 line 62.** The GitHub search names three orgs (GovTechSG, govtech-responsibleai, opengovsg), while CK2 R4 line 269 and CK3 R4 line 437 name four (plus datagovsg). Align the lists.
- **CK1 R3 line 45.** The column gives "(HTTP 200 after redirect ...)", while the inventory gives "HTTP 302 then a 200 login page". Use the inventory wording in both.
- **Inventory (b), Sentinel integration (planned), "Applies to" cell.** The sheet-3 column AF reference is a workbook cross-reference, not an inference from the playbook. Consider "PII detection and masking on Sentinel traffic [Inferred] (premise: ...). Cross-reference: GovTech Sentinel: PII detection and masking (AWS Bedrock), sheet 3 column AF". I confirmed that SN6 is the sixth Sentinel column, which is AF in the AA to AG range, and that the header text matches sentinel_two_level.md exactly.
- **cloak_brief.md.** The brief still carries the old CK2 and CK3 header wording. Main ruled that the brief is a historical P1 file (queue cloak P6 Q1), so no action is needed for the build.

## 1. Unlogged differences

Method:
- `benchtest/scratchpad/verifier/cloak/diff_cols.py` parses CK1 from cols_a.md, CK2 and CK3 from cols_b.md, and the final, into per-row line lists, then runs difflib SequenceMatcher per row.
- Each added or removed line is searched in cloak_changes.md by normalised 60, 40 and 25-character prefixes.
- `diff_words.py` gives a word-level diff for each modified line.
- `diff_inv.py` aligns the inventories by row key and diffs each cell word by word.

Results:
- **Headers.** They are identical between drafts and final for all three columns, and equal to R037.
- **Columns.** 63 lines were added and 44 removed. All 44 removals and 55 additions prefix-match a log entry. The other 8 additions are later parts of multi-bullet entries that the log joins with " // " and truncates. I matched each one by hand:
  - CK1 R3 "The deck draws no step ..." is in the T57 entry (row 36).
  - CK1 R4 "v2.0.1 ... Word document support" is in row 40.
  - CK1 R6 has five: Inclusion matching (row 44), the Mask example (row 45), Alias PERSON only and Alias options (row 45), and the NGE pre-approval and Cloak Guide access wording (row 49).
  - All 8 are verbatim in cloak_resolutions_1.md.
- **Word-level.** Every modified line maps to a logged reason: T33, T34, T39, T41, T42, T57, T59, T60, T70, T71, T72, T73, or hygiene.
- **Inventory.**
  - The new rows (b) Sentinel integration and (e) Terms Schedule 4.1 and 4.2, Terms clause 6.1 and Privacy Statement paragraphs 4 and 5.1.5 are logged.
  - Every changed cell maps to a section 3 entry: T4, T5, T7, T8, T9 to T15, T18 to T20, T41, T43, T48, T50, T52, T64, T67, T69, T70 and T74.
  - The 35 spans that did not prefix-match are again truncation of long "after" cells: MDG, the non-WOG row, Mask, Pseudonymise, Encrypt, CSV size, LLM limits, Confidence, retention, ceiling, clause 3.3, 3.4.9, Schedule 2.2, clause 15, the dates row, Presidio and PyCrypto. Each was matched by hand.
  - No row was removed.
- **Summaries.** The 4 changed Summaries (CK1 R4, CK2 R4, CK2 R5, CK2 R6) are exactly those in the log. cloak_summaries_preview.md equals the final for all 27 Summaries and bullet counts (script compare).
- Result: no substantive unlogged change.

## 2. Sourcing and label strength

- **Changed Documented facts.** They trace to resolution quotes: T8, T9, T10, T11, T13, T14, T15, T16, T18, T19, T20, T33, T35, T41, T42, T43, T48, T57, T60, T64, T67, T69 and T73.
- **Merger-made text.** It consists of the per-fact splits logged as T73, with each half's quote present in the resolutions.
- **Inferences or readings under a Documented label:**
  - CK1 R2 line 22, "20 tags" (fix 2).
  - CK2 R3 line 240, "not an inline reply" (fix 6).
  - CK3 R4 line 427, "custom salts in v2.1.0" (fix 11; a misreading rather than an inference).
  - I also scanned the Documented bullets for "so", "which", "because" and "therefore". The remaining hits are inside quotes or name a conflict, as README section 3 rule 4 allows: CK1 R6 line 107 "which reads the other way" and CK1 R6 line 122 "the playbook words it differently".
- **Absence labels.**
  - CK2 R1 line 217 (fix 4) and inventory (a) FTA row (fix 14) are absences labelled `[Inferred]`.
  - Every other `[Not disclosed]` bullet or cell names what was checked.
  - Scope or purpose conclusions (CK1 R2 line 34, CK2 R2 line 233) are `[Inferred]` with a premise, per R015.
- **Leftovers that contradict a resolution:**
  - CK2 R1 line 217 against T60 (fix 4).
  - Inventory (f) "built on Presidio" against the T30 wording in the columns and the (c) intro (fix 13).
  - Inventory scope paragraph "does not return a score" against the documented confidence score (fix 14).
  - No other hit for the strings named in the brief for this review:
    - "GovTech's cloud": 0.
    - "learns from": 0.
    - "Transformer Module": 0.
    - "clause 4.2": 0. Only "Schedule 4.2" occurs.
    - "(regex and LLM)" without "lists": 0.
    - "secrets and salts": 0.
    - The deck "restore" claim: CK1 R3 and CK3 R3 now say that the response returns with the placeholder and that no restore step is drawn. This matches the slide, which I rendered today.
- **Terms clauses.**
  - They are quoted verbatim in CK1 R6 and R7, CK2 R8, CK3 R8 and inventory (e). Typographic quotes are normalised to ASCII, as the scope paragraph says.
  - The definition of Public Sector Entities, the undefined "Agency" and "license keys", Schedule 4.6 with the printed backslash, clauses 6.1 and 9.1, Schedule 4.1 and 4.2, and the clause 15 numbering all match the PDF.
  - Permitted use is never concluded; it stays an R8 question "decided before any bench run".
  - The one interpretive paraphrase left is CK3 R7 (fix 12).
- **R032 wording.**
  - R7 rows use "a bench could", "possible", "suggested first step" and "would need".
  - The sweep for "bench will", "we use", "bench rule" and "this is the plan" gives 0 hits.
  - CK1 R7 line 141 frames sensitive test data as a bench-design question.
- **Process wording.** "not re-read here" (inventory (f)) and "neither is chosen here" (inventory (d)) remain; both are optional fixes. There is no "pypdf", "read-only", "this draft" or "I checked".

## 3. Summary entailment and style

- **Checker.** `python benchtest/tools/check_drafts.py columns benchtest/drafts/cloak_two_level.md --final --expect 3` gives the three headers and "RESULT: 0 errors, 0 warnings".
- **Word counts** (re-counted, label excluded; limit minus 1 is 44, and 59 for R7):

| Column | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 |
|---|---|---|---|---|---|---|---|---|---|
| CK1 | 42 | 33 | 44 | 35 | 43 | 38 | 53 | 33 | 26 |
| CK2 | 38 | 32 | 42 | 35 | 40 | 43 | 48 | 39 | 24 |
| CK3 | 42 | 33 | 44 | 39 | 34 | 38 | 45 | 37 | 26 |

  None is over the limit. After fixes 1 and 5, CK1 R1 stays at 42 and CK2 R2 becomes 33.
- **Format.** R8 rows start with "**Key open questions.**" and carry no label. R9 rows are plain. Each R7 starts with "**Minimum setup:**".
- **Entailment, row by row:**

| Column | Entailed | Not entailed |
|---|---|---|
| CK1 | R2 to R8 | R1 (fix 1) |
| CK2 | R3, R5 (borderline, optional), R6, R7, R8 | R1 (fix 3), R2 (fix 5), R4 (fix 7) |
| CK3 | R4 (salts wording optional), R5, R6, R7, R8 | R1 (fix 8), R2 (fix 9), R3 (fix 10) |

- **Pins.** The playbook label @45908b48 (CK1 R3, R4, R6; CK2 R1) has its blob URL in CK1 R9 and CK2 R9. CK3 carries no repo label.

## 4. Spot-checks at source

All reads were made on 2026-10-10. Cloak Guide pages are the raw .md files (base https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/). PDFs were read through pypdf text. Slide 22 was also rendered.

| # | Claim | Location | Source URL | Verbatim quote or value seen | Match |
|---|---|---|---|---|---|
| 1 | Cloak offers tabular and free-text anonymisation; open to select NGEs | CK1 R1, R6; INV (b) | .../home.md | "Cloak offers tabular and free-text anonymisation to enable agencies to anonymise data safely before data sharing and utilisation."; "is open to select non-government entities (e.g. public healthcare)" | MATCH |
| 2 | Use case on LLM traffic | CK1 R1, R3; CK2 R3; CK3 R3 | .../home.md | "Anonymise before sending to LLMs \| Strip PII in real-time via API before data reaches external LLMs or other WOG products" | MATCH |
| 3 | Portal use case on chatbot prompts, dated | CK1 R1 | https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/use-cases | "Agencies integrate Cloak via API into chatbot services and WOG AI platforms to strip PII from user prompts in real-time before they reach external LLMs."; "Last updated 21 Aug 2026" | MATCH |
| 4 | FAQ on GenAI use | CK1 R1 | .../faqs.md | "Yes, this is a common use pattern, provided anonymisation happens before the data leaves the approved environment and the output is validated." | MATCH |
| 5 | 17 entity groups; method statement; spaCy and Presidio links | CK1 R2, R4; INV (c), (f) | .../fta/entity-types/intro.md | 8 + 4 + 2 + 3 groups plus Exceptions and Custom; "Entity types are identified either by the underlying AI Model (e.g. spaCy), and a combination of:"; link spacy.io/models/en#en_core_web_sm; "for general information on the PII entities supported by Presidio" | MATCH |
| 6 | Address recognisers, methods, defaults | CK1 R2, R4; INV (c) | .../fta/entity-types/personal/full-address.md | "Cloak provides 4 address-related recognisers for Singapore addresses"; SG_ADDRESS ON Pattern matching; POSTAL_CODE ON Regex; UNIT_NUMBER ON Regex; STREET "OFF (advanced)" Pattern matching | MATCH |
| 7 | Vendor counts 20+ and 17+ | CK1 R2; INV (c) | .../fta/intro-to-fta.md ; portal features-roadmap ; portal faqs | "Cloak detects and transforms 20+ baseline entity types"; "Auto-detection of 20+ entity types including names, NRICs, phone numbers, addresses, emails, dates of birth, bank accounts, and more"; "Cloak detects 17+ entity types out of the box" ... "vehicle plate numbers" | MATCH |
| 8 | NRIC validation disabled; phone global coverage | CK1 R2; INV (c) | .../personal/nric.md ; .../personal/phone-number.md | "Both real and fake NRIC numbers following the format @xxxxxxx# ... are detected."; "Only Singapore numbers are detected by default."; "+91 7513200000" | MATCH |
| 9 | Probabilistic detection; content not processed | CK1 R2; CK2 R2; INV (e) | .../faqs.md | "Free-text detection is probabilistic, so 100% recall should not be assumed."; "Cloak does not process scanned PDFs, screenshots, images or engineering drawings." | MATCH |
| 10 | Input limits | CK1 R3, R6; CK2 R3, R6; CK3 R3, R6; INV (e) | .../fta/usage-guide.md | "Maximum 20,000 characters (approx. 3,000 words) per submission."; CSV "Maximum 500 MB per file"; PDF and DOCX "Maximum 200 MB per file"; "Up to 100 files per project, with a total upload limit of 2 GB." | MATCH |
| 11 | Slide 22 layout: response returns from Gen AI with placeholder; Mapping Table on the agency side; no restore step drawn | CK1 R3; CK3 R3 | https://www.usenix.org/system/files/pepr23_slides-tang.pdf | Rendered slide: arrow from "<<Gen AI Magic!>>" to "Anonymised Response: Dear <hash value 1>, we regret to inform.." in the Agency Product column; Mapping Table box in that column; no arrow back through the Transformer Module | MATCH |
| 12 | Deck text and date | CK1 R5; CK3 R1, R2, R5 | same deck | slide 21 "Potential privacy leakages from usage of LLM products in the public sector."; slide 22 "Outgoing prompt does not leak PII to overseas servers or ChatGPT", "API: Takes in unstructured text, returns mapping table and anonymized result."; slide 1 "Sep 11, 2023" | MATCH |
| 13 | GCC hosting and tech stack | CK1 R4; CK2 R4; CK3 R4 | .../faqs.md ; portal features-roadmap | "users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment"; "AWS GCC 2.0"; "Last updated 21 Aug 2026" | MATCH |
| 14 | Release notes order and entries | CK1 R4; CK2 R4; CK3 R4; INV (a), (b) | .../release-notes.md | v2.2.2 "Released on 4 August 2024" listed above v2.2.1 "Released on 28 August 2024"; v2.1.0 "[FTA] Added the ORGANIZATION entity type", "[FTA] Create and reuse project settings as templates"; v2.0.1 "[FTA] Added Word document support", "[API] Reconstruct endpoint for FTA API"; v2.1.5 "[FTA] Regex custom entities"; v1.2.0 "[FTA] Free Text Anonymisation feature availability" | MATCH |
| 15 | Confidence threshold and default | CK1 R5; CK2 R5; INV (e) | .../fta/advanced-features/confidence-level.md ; .../fta/usage-guide.md | "Entities below the specified threshold will not be anonymised"; "set to the default value of 0.30"; "adjustment of the detection threshold from 0 to 1" | MATCH |
| 16 | ">97% recall for key PIIs like Name, NRIC and Email" (home and portal overview) | CK1 R5 | .../home.md ; portal overview | Home: verbatim. Overview: "optimised for Singaporean PIIs with >97% recall like Names, NRICs, and Emails" | MISMATCH (overview wording differs; optional) |
| 17 | PROOF OF VALUE badge; >5 million PIIs per month | CK1 R5; INV (a) | https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/overview | "PROOF OF VALUE"; "Currently processing >5 million PIIs removed per month across WOG."; "Last updated 26 Aug 2026" | MATCH |
| 18 | Terms 9.1 and 9.1.1 | CK1 R5; INV (e) | https://go.gov.sg/cloak-terms | "9.1. The Service is provided on an 'as is' and 'as available' basis without warranties of any kind."; "9.1.1. as to the accuracy, completeness, correctness" | MATCH |
| 19 | Inclusion page: entries against words; matching | CK1 R6; CK2 R6; INV (c), (e) | .../fta/advanced-features/inclusion-feature.md | "You can add words individually or upload a CSV file containing up to 500 entries."; "Only the first 500 words in a CSV upload will be used."; "Word-sensitive"; "Not case-sensitive" | MATCH |
| 20 | Mask defaults and the conflict inside the page | CK1 R6; INV (d) | .../fta/anonymisation-techniques/masking/intro.md | "`Suffix`: masks the starting characters"; "`Prefix`: masks the ending characters"; default 3, Suffix, "-"; example "120414 \| 120*** \| Transforms into a suffix masked value" | MATCH |
| 21 | Replace (Unique) limits; /analyze | CK1 R6; CK3 R1; INV (b), (d), (e) | .../fta/anonymisation-techniques/replace-unique.md | "On the Cloak Web App; For single CSV uploads; and For Cloak's baseline entities"; "Custom entities (including custom regex and dictionary entities)"; "up to two entity types per anonymisation job"; "Cloak's /analyze endpoint and a mapping table you maintain" | MATCH |
| 22 | Retention; encryption in transit and at rest on cloak.gov.sg | CK1 R6; CK3 R4; INV (e) | .../faqs.md ; https://www.cloak.gov.sg | "Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request."; site FAQ "All data is encrypted in transit and at rest." | MATCH |
| 23 | Maintenance banner | CK1 R6; CK2 R6; CK3 R6; INV (b), (e) | https://www.cloak.gov.sg | "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period." | MATCH |
| 24 | Terms 3.3, the definition, 3.4 and 3.4.7, 3.4.9, 3.4.11, Schedule 2.2, Schedule 4.6 | CK1 R6, R7; CK2 R8; CK3 R8; INV (e) | https://go.gov.sg/cloak-terms (302 to file.go.gov.sg/cloak-terms.pdf) | "restricted solely for such purpose that GovTech has consented to in writing (including via email)"; "'Public Sector Entities' means the Government (including its ministries, departments and organs of state) and public authorities (such as statutory boards)"; "3.4.7. perform any benchmarking tests or analyses of the Service;"; "3.4.9. transfer assign or permit the sharing of license keys to or with a third party;"; "3.4.11. provide third party access to the Service"; Schedule "2.2. You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency."; "4.6. ... Confidential (Cloud-Eligible) \ Sensitive (High)" | MATCH |
| 25 | Terms 6.1, Schedule 4.1 and 4.2, clause 15 numbering, date, Schedule 3 | INV (e), (f) | same PDF | "non-exclusive, worldwide, perpetual and royalty- free right to collect, use, disclose ..."; Schedule "4.2. You acknowledge and agree that GovTech may routinely delete any or all of Your Data ..."; "15.2. Subject to clause 14.3"; "15.3. ... referred to in clause 14.2 above"; "14. Severability"; "These Terms of Use are dated 24 July 2024."; "a list of open source components used in the Service" | MATCH |
| 26 | Privacy Statement date, paragraphs 4 and 5.1.5, Annex | INV (e) | https://go.gov.sg/cloak-privacy | "This version of the Privacy Statement is dated 1 December 2022."; "Your data may be stored in our servers, systems or devices, in the servers, systems or devices of our third party service providers or collaborators"; "5.1.5. for the purposes of storing or creating backups of your data ..."; "2.2. Dataset uploaded by user for purposes of data anonymisation/transformation." | MATCH |
| 27 | Custom entity routes on the home page | CK2 R1; INV (a) | .../home.md | "Customisable - add any custom entity using inclusion lists, pattern-matching (regex), or privately-hosted LLMs" | MATCH |
| 28 | Structured page samples and hospital case number | CK2 R2, R4 | .../fta/custom-entities/custom-entities-structured.md | "Car license number", "Unusual date format", "Username"; "Suppose a 10-digit hospital case number (e.g. 1234567890) is consistently detected as a Bank Account Number"; "Define custom context words that must appear near a regex match"; "Set different confidence scores for each regex pattern" | MATCH |
| 29 | "The Web UI returns a download, not an inline reply" | CK2 R3 | .../fta/usage-guide.md | Download quote present; but "Your Original Data is displayed on the left, and your Anonymised Data is displayed on the right" (inline preview) | MISMATCH (fix 6) |
| 30 | Fixed-list behaviour | CK2 R4; INV (c), (e) | .../fta/custom-entities/custom-entities-fixed-list.md | "if "Changi General Hospital" is listed, "Changi-General-Hospital" will not be detected"; "if "CGH" is listed, "cgh" will also be detected"; "The CSV to be uploaded should contain a maximum of 500 words listed in the first column." | MATCH |
| 31 | LLM entity: hosting, Beta, limits, few-shot, 3 to 5 examples | CK2 R4, R6; INV (a), (c), (e) | .../fta/custom-entities/custom-entities-unstructured/intro.md | "[Beta Feature]"; "only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)"; "up to 8 hours"; "few-shot prompting ... a small set of 3-5 examples (labelled data)"; "Cloak privately hosts a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS." | MATCH |
| 32 | FAQ LLM entity per project; choice table | CK2 R2, R4; INV (c), (e) | .../faqs.md | "The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time."; "Inclusion list \| The exact values are known (e.g. a staff list, building names)" | MATCH |
| 33 | Write-prompts tips and iteration | CK2 R3, R6 | .../custom-entities-unstructured/write-prompts.md | "Include 3-5 examples that captures the diversity present in your dataset."; "PERSON_NAME, BUILDING_NAME" against "NAME"; "(e.g., <100 documents, which should take <20min)" | MATCH |
| 34 | Portal roadmap lines | CK2 R4; CK3 R8 | portal features-roadmap | "Improve performance of free-text anonymisation through novel LLM-based approaches"; "Incorporation of other privacy technologies, e.g., Homomorphic Encryption and Searchable Symmetric Encryption" | MATCH |
| 35 | Encrypt page: cipher, key, restriction, base64, example | CK1 R4, R6; CK3 R1, R4, R5; INV (d) | .../fta/anonymisation-techniques/encrypt.md | "The encryption uses AES cypher in CBC mode and requires a cryptographic key as an input for both encryption and decryption."; "AES-256 Encryption is recommended. The output would be in base64."; "we have restricted encryption to only AES-256 CBC Mode Encryption"; "Jason \| pX09dIQ4X3gU1FC3r8pZXA==" | MATCH |
| 36 | Free-text decryption | CK3 R1, R3, R5, R6; INV (a), (d) | .../decryption/free-text-decryption.md | "The Web UI currently supports decrypting one value at a time (paste into the text field)."; "which supports looping through rows in a CSV"; "after selecting your secret, you can then obtain the decrypted value." | MATCH |
| 37 | Secret sharing intro and Secrets Manager | CK3 R1, R2, R4, R5, R6; INV (a) | .../decryption/intro-to-decryption.md ; .../decryption/secrets-manager.md | "Consistent anonymisation across datasets - Use the same keys or salts ..."; "Members of shared secrets will not be able to view or access the secret key and IV value"; "up to 10 other users per operation, and with a maximum of 50 users per secret"; "Decrypt Free Text: Users decrypts a singular encrypted value" | MATCH |
| 38 | "the release notes list custom salts in v2.1.0 and v2.1.4" | CK3 R4 line 427 | .../release-notes.md | v2.1.0 "[FTA] Added salt parameter for Pseudonymisation transformation"; v2.1.4 "[FTA] Support for custom salts and user managed salts" | MISMATCH (fix 11) |
| 39 | Pseudonymisation page | CK1 R6; CK3 R1, R2, R4, R6; INV (d) | .../fta/anonymisation-techniques/pseudonymisation.md | "irreversible hashing (SHA-256) or (SHA-512) with a random salt"; "Custom salt values will be included in the future."; "conditioned on using the same salt value for the datasets"; 64-character hex example | MATCH |
| 40 | HTTP facts | CK3 R4; INV (b), (d), (e), (f) | the listed URLs | cloak.gov.sg/terms 404; microsoft.github.io/presidio/tutorial/12_encryption/ 404; presidio.dataprivacystack.org/tutorial/12_encryption/ 200; .../decryption-secret-sharing/intro-to-decryption.md 404; go.gov.sg/cloak-open-source 302 to .../sections/credits; API guide, OpenAPI, package guide and helper-script pages 302 to auth/otp-login with redirect_reason=not_logged_in | MATCH |
| 41 | Playbook text and Sentinel stub @45908b48; deployed page | CK1 R3, R4, R6; CK2 R1; INV (b) | https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx ; https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/ | "GovTech's dedicated internal service for comprehensive and localised PII detection"; "Direct integration with the Sentinel API is coming soon."; "# Coming soon — Sentinel + Cloak integration is on the roadmap."; "User prompts.", "Model outputs.", "Retrieved documents.", "Tool arguments and tool results."; the deployed page carries the same two lines | MATCH |
| 42 | Sentinel docs do not mention Cloak | CK1 R4; INV (b) | https://www.aiguardian.gov.sg/docs ; https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails | 0 case-insensitive hits for "cloak" in 44 and 617 lines of page text | MATCH |
| 43 | MDG placement and Mirage | INV (a) | portal features-roadmap ; https://mirage.gov.sg ; https://www.cloak.gov.sg | "Generate mock data that mimics the structure and format of real datasets."; "Field categories: Person, location, business, healthcare, and custom"; "Mock Data Generation is available via API through Cloak (https://cloak.gov.sg)."; "Mock data generation does not require any input data"; "Mirage is our sister product for Synthetic Data Generation" | MATCH |
| 44 | Getting started; registration | INV (b); CK1 R6 | portal getting-started ; .../registration-guide.md | "For WOG users: Log in immediately at cloak.gov.sg using WOG-AD. No onboarding required for the Web UI."; "Access is approved on a case by case basis for entities in service for public sector outcomes."; "it will submit the request to Cloak's Ops Team" | MATCH |
| 45 | Package page; templates; Alias; NRIC masking | INV (a), (b), (d); CK1 R4, R6 | .../packages-anonymiser.md ; .../templates/templates.md ; .../alias.md ; .../masking/nric-masking.md | "offline access to Cloak's tabular anonymisation features (without k-anonymity)"; "no longer actively maintained and is provided as-is"; "Entity types, anonymisation techniques, parameters, and score threshold"; "Not shareable"; "Alias is only available for the PERSON entity type."; Context and Offset default On; "agencies are no longer allowed to used masked / partial NRICs" | MATCH |
| 46 | Block (f) owners | INV (f) | .../credits.md ; https://pypi.org/project/pycrypto/ ; LICENSE files at pins ; https://presidio.dataprivacystack.org/project_transition/ | Credits has 32 level-2 entries, including crypto (pypi pycrypto) and cryptodome (Legrandin/pycryptodome), and no spaCy or Presidio entry; PyPI "Dwayne C. Litzenberger", "amk", "dlitz", "Public Domain", Oct 17, 2013, Jun 20, 2014; PyCryptodome "partially in the public domain and partially released under the BSD 2-Clause license"; spaCy "Copyright (C) 2016-2024 ExplosionAI GmbH ..."; Presidio "in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project" | MATCH |

I also checked the following without giving each its own table row; all match:
- the NRP, Name, Exceptions, Custom, Replace, add-entities and video-guides pages, including the "ContextGuard Demo (Spoken - 9min)" title and the Secure Internet API video;
- the API guide security-level table and its "same anonymisation capabilities as the Web UI" sentence;
- the Sentinel column SN6 header "GovTech Sentinel: PII detection and masking (AWS Bedrock)", the sixth of the seven Sentinel columns, which is AF in AA to AG.

Tally: 46 checked, 43 MATCH, 3 MISMATCH (rows 16, 29, 38), 0 UNVERIFIABLE.

## 5. Inventory consistency

- **Checker.** `python benchtest/tools/check_drafts.py inventory benchtest/drafts/cloak_inventory_final.md --headers benchtest/drafts/cloak_two_level.md` gives:

| Block | Rows | Columns |
|---|---|---|
| (a) | 10 | 7 |
| (b) | 8 | 8 |
| (c) | 26 | 7 |
| (d) | 9 | 6 |
| (e) | 28 | 5 |
| (f) | 4 | 6 |

  The result is "RESULT: 0 errors, 0 warnings", which is 85 rows as logged for P8 (section 5b).
- **Covered-by (independent count):**
  - 76 header cells with 138 mentions: CK1 67, CK2 38, CK3 33.
  - "— (inventory only, not in Table 3)" in 7 cells: Tabular data anonymisation, Tabular decryption, MDG, Anonymiser package, Mirage, Python package path and Tabular file limits.
  - "— (legacy, not in Table 3)" in 1 cell (enCRYPT).
  - "— (planned, not in Table 3)" in 1 cell (Sentinel integration).
  - No Sentinel or Presidio header appears in any Covered-by cell.
  - Main's rows are applied: Decrypt is CK3 only; Pseudonymise and Encrypt are CK1 and CK3; Inclusion (c) and Inclusion and fixed-list size (e) are CK1 and CK2; Templates is CK1 and CK2.
  - Two cells use " ; " (optional fix).
- **Cell format.**
  - No `**`, no backtick, and no stray `|` (every row has its header's cell count).
  - Bracketed tokens outside the allowed labels are vendor text: "[FTA]", "[Decryption]" and "[Beta Feature]". All are inside quotes except the (c) LLM row (optional fix).
  - Repo labels use the 8-character sha or the release tag.
- **Column and inventory agreement.**
  - Limits, terms, techniques, entity tags, release dates, the confidence default, the LLM limits and the access routes agree with the columns.
  - Exceptions: inventory (f) "built on Presidio" (fix 13), and the scope paragraph and (a) FTA row "no score" (fix 14).
- **Block intros.** They carry no ruling ids, triage ids or session references.

## 6. URLs

Scope: the R9 bullets of CK1 to CK3 and the inventory "Source URL" cells, deduplicated, give 84 distinct URLs (`benchtest/scratchpad/verifier/cloak/urls.tsv`). Each was requested once without following redirects and once with `curl -L` (`url_check.tsv`).

Results:
- 78 return 200 directly.
- 3 return 302 to https://docs.developer.tech.gov.sg/auth/otp-login (redirect_reason=not_logged_in), then 200: the API Guide, the OpenAPI page and the Anonymiser package guide. These are expected gated pages, cited as HTTP facts with `[Not disclosed]` content (R007).
- 2 return 302 to file.go.gov.sg PDFs, then 200: go.gov.sg/cloak-terms and go.gov.sg/cloak-privacy. These are expected short links.
- 1 returns 307 to https://www.cloak.gov.sg/sign-in, then 200: www.cloak.gov.sg/packages. This is expected (gated application page).

URLs that appear only as HTTP facts in cell text were also checked. They match the text:
- www.cloak.gov.sg/terms gives 404.
- microsoft.github.io/presidio/tutorial/12_encryption/ gives 404.
- The old home-page decryption link .../decryption-secret-sharing/intro-to-decryption.md gives 404.
- go.gov.sg/cloak-open-source gives 302 to the Credits page.
- The free-text decryption helper script gives 302 to the login page.

The 404 URLs are not used as Source URLs.

No URL failures beyond the expected set in cloak_changes.md section 5b.

### Appendix: URL table

| URL | Status | Used in |
|---|---|---|
| https://docs.developer.tech.gov.sg/docs/cloak-anonymiser-package-guide/?product=Cloak | 302 to docs login page (redirect_reason=not_logged_in), then 200; expected (gated) | INV (a) |
| https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ | 302 to docs login page (redirect_reason=not_logged_in), then 200; expected (gated) | CK1 R9, CK2 R9, CK3 R9, INV (b) |
| https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/ | 302 to docs login page (redirect_reason=not_logged_in), then 200; expected (gated) | CK1 R9, INV (b) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/_sidebar.md | 200 | INV (a), INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/credits.md | 200 | CK1 R9, INV (f) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/free-text-decryption.md | 200 | CK3 R9, INV (a), INV (b), INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/intro-to-decryption.md | 200 | CK3 R9, INV (a) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/secrets-manager.md | 200 | CK3 R9, INV (a), INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/decryption/tabular-decryption.md | 200 | CK3 R9, INV (a), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/developer-api-guide.md | 200 | CK1 R9, CK2 R9, INV (a), INV (b) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/faqs.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (b), INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/confidence-level.md | 200 | CK1 R9, CK2 R9, INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/advanced-features/inclusion-feature.md | 200 | CK1 R9, CK2 R9, INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/alias.md | 200 | CK1 R9, INV (c), INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/encrypt.md | 200 | CK1 R9, CK3 R9, INV (d), INV (f) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/masking/intro.md | 200 | CK1 R9, INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/masking/nric-masking.md | 200 | INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/pseudonymisation.md | 200 | CK1 R9, CK3 R9, INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/redact.md | 200 | INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace-unique.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (b), INV (d), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/anonymisation-techniques/replace.md | 200 | CK1 R9, CK2 R9, INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-fixed-list.md | 200 | CK2 R9, INV (a), INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-structured.md | 200 | CK1 R9, CK2 R9, INV (a), INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/add-entities.md | 200 | CK2 R9, INV (a), INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/intro.md | 200 | CK1 R9, CK2 R9, INV (a), INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/datetime-specific.md | 200 | CK2 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/disease.md | 200 | CK2 R9 |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/samples/person-name.md | 200 | CK2 R9 |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/custom-entities/custom-entities-unstructured/write-prompts.md | 200 | CK2 R9, INV (a), INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/financial/credit-card.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/financial/currency.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/financial/intl-bank-account.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/financial/sg-bank-account.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/intro.md | 200 | CK1 R9, INV (c), INV (f) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/custom.md | 200 | CK2 R9, INV (a), INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/datetime.md | 200 | CK1 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/exceptions.md | 200 | CK1 R9, CK2 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/organization.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/others/uen.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/country.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/email-address.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/full-address.md | 200 | CK1 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/name.md | 200 | CK1 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/nric.md | 200 | CK1 R9, INV (c), INV (d) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/nrp.md | 200 | CK1 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/passport.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/personal/phone-number.md | 200 | CK1 R9, INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/technical-security/ip-address.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/entity-types/technical-security/url.md | 200 | INV (c) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/intro-to-fta.md | 200 | CK1 R9, CK2 R9, INV (a) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/fta/usage-guide.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (b), INV (c), INV (d), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/home.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (b), INV (c), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/packages-anonymiser.md | 200 | CK2 R9, CK3 R9, INV (a), INV (b) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/registration-guide.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (b) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/release-notes.md | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (b), INV (c), INV (d), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/tabular/intro-to-tabular.md | 200 | INV (a) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/tabular/usage-guide.md | 200 | INV (a), INV (e) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/templates/templates.md | 200 | CK1 R9, CK2 R9, INV (a) |
| https://docs.developer.tech.gov.sg/docs/cloak-guide/sections/video-guides.md | 200 | CK1 R9, INV (a), INV (b) |
| https://file.go.gov.sg/cloak-terms.pdf | 200 | CK1 R9, CK2 R9, CK3 R9 |
| https://github.com/Legrandin/pycryptodome/blob/v3.24.0/LICENSE.rst | 200 | INV (f) |
| https://github.com/data-privacy-stack/presidio/blob/2.2.364/LICENSE | 200 | INV (f) |
| https://github.com/explosion/spaCy/blob/release-v3.8.16/LICENSE | 200 | INV (f) |
| https://github.com/explosion/spacy-models/blob/ca6f473afda3c4943d3919d3e39406c1b3f48b85/meta/en_core_web_sm-3.8.0.json | 200 | INV (f) |
| https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx | 200 | CK1 R9, CK2 R9, INV (b) |
| https://go.gov.sg/cloak-privacy | 302 to https://file.go.gov.sg/cloak-privacy.pdf, then 200; expected (short link) | INV (e) |
| https://go.gov.sg/cloak-terms | 302 to https://file.go.gov.sg/cloak-terms.pdf, then 200; expected (short link) | INV (b), INV (e) |
| https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/ | 200 | INV (b) |
| https://microsoft.github.io/presidio/supported_entities/ | 200 | INV (f) |
| https://mirage.gov.sg | 200 | INV (a) |
| https://presidio.dataprivacystack.org/project_transition/ | 200 | INV (f) |
| https://presidio.dataprivacystack.org/tutorial/12_encryption/ | 200 | INV (d), INV (f) |
| https://pypi.org/project/pycrypto/ | 200 | INV (f) |
| https://www.aiguardian.gov.sg/docs | 200 | CK1 R9, CK2 R9, INV (b) |
| https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Guardrails | 200 | CK1 R9, CK2 R9, INV (b) |
| https://www.cloak.gov.sg | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (b), INV (e) |
| https://www.cloak.gov.sg/packages | 307 to www.cloak.gov.sg/sign-in, then 200; expected (gated) | INV (a), INV (b) |
| https://www.cloak.gov.sg/register | 200 | INV (b) |
| https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/faqs | 200 | CK1 R9, INV (c), INV (e) |
| https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/features-roadmap | 200 | CK1 R9, CK2 R9, CK3 R9, INV (a), INV (c), INV (e) |
| https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/getting-started | 200 | INV (b) |
| https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/overview | 200 | CK1 R9, INV (a) |
| https://www.developer.tech.gov.sg/products/categories/data-and-apis/cloak/use-cases | 200 | CK1 R9, CK3 R9 |
| https://www.usenix.org/system/files/pepr23_slides-tang.pdf | 200 | CK1 R9, CK3 R9 |
