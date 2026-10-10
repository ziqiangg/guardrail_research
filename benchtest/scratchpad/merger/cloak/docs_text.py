INTRO = (
    "Inputs merged: cloak_brief.md, cloak_cols_a.md (CK1), cloak_cols_b.md (CK2 and CK3), cloak_inventory.md, cloak_triage.md (75 items), "
    "cloak_resolutions_1.md (39 items: 27 class a, 12 class c; 36 RESOLVED, 2 PARTLY RESOLVED, 1 CORRECTION), the rulings R002, R007, R009, R011, R015, R019, R020, R021, R032 and R037 (cloak CP1: three columns, CK3 one column), "
    "and main's rows in scratchpad/main/queue.md (headers; Decrypt row CK3 only; Pseudonymise row stays CK1 and CK3; Inclusion row CK1 and CK2; planned Sentinel integration row with the planned marker, cross-referencing the Sentinel PII column in sheet 3 column AF; "
    "accept the three new block (e) Terms and Privacy rows, giving blocks 10/8/26/9/28/4 = 85; presidio.dataprivacystack.org URLs official; T66 default-on rows stay [Inferred]; list-limit Summary wording 'words or entries; the docs differ'; "
    "Terms clauses verbatim with no interpretation). "
    "Outputs: cloak_two_level.md, cloak_inventory_final.md, cloak_changes.md (this file), cloak_summaries_preview.md. Cloak has no evaluation-tooling sheet. "
    "No source file was modified and no new web or repository research was done; every added fact is in the resolutions file, a ruling or main's queue. "
    "Merged 2026-10-10 by gr-merger with the scripts in benchtest/scratchpad/merger/cloak/.\n\n"
    "In this file bold markers are dropped from quoted text and long text is shortened. Reason codes: Tn = triage id (resolution in cloak_resolutions_1.md), 'style n' = triage Style issues in columns, 'hygiene' = triage Label hygiene or a merger-found hygiene fix, 'main' = main's queue rows, 'Rnnn' = ruling. "
    "Kinds: summary, replace, edit, add, delete, correction (a CORRECTION verdict), label (a label changed), covered-by, url (R9 or Source URL cell), style. Entries have the form location (kind) | before | after | reason."
)

GLOBAL = [
    ("Reviewer notes sections (two column drafts, inventory draft, inventory self-check)", "present", "removed from cloak_two_level.md and cloak_inventory_final.md; kept verbatim in section 7", "README section 4"),
    ("Column set", "three columns drafted by default, open at CP1 (T1)", "three columns in the order CK1, CK2, CK3. Tabular anonymisation, mock data generation, the offline Anonymiser package and Mirage stay inventory only; enCRYPT is legacy", "T1, R037"),
    ("CK3 direction", "one column, anonymise-side and restore-side bullets, open (T2)", "one column; the two sides stay separate bullets in R1, R3, R5 and R6; revisit only if the gated API later shows a direction setting", "T2, R037, R002"),
    ("Header wording and prefix", "brief: CK2 '(regex and LLM)', CK3 '(secrets and salts)'; drafts and inventory already use main's wording", "CK2 'Cloak: Custom entity detection in free text (lists, regex and LLM)', CK3 'Cloak: Reversible anonymisation and decryption (encrypt and restore)'; prefix 'Cloak:' (R009), fixed at CP1, frozen after CP2. The brief's lines 24, 25, 34, 180 and 183 still carry the old wording: cloak_brief.md is outside the merger's write scope, so the edit proposed in T3 is not applied (see section 6c)", "T3; main queue (cloak P1 Q4); R037"),
    ("Inventory row counts", "10 / 7 / 26 / 9 / 25 / 4 = 81", "10 / 8 / 26 / 9 / 28 / 4 = 85: block (b) gains the planned Sentinel integration row; block (e) gains three rows (Terms Schedule 4.1 and 4.2, Terms clause 6.1, Privacy Statement paragraphs 4 and 5.1.5)", "T6, T7, T14, T15; main queue (cloak P5 Q1)"),
    ("Covered-by cells", "Decrypt 'CK1; CK3'; Templates, Inclusion list, limits and the Presidio row mapped inconsistently with the column Detail", "13 cells edited (see section 3). Decrypt row CK3 only; Pseudonymise stays 'CK1; CK3'; Templates, Inclusion list, Replace (Unique) limits, Preview limits, Content not processed, Confidence level, Inclusion and fixed-list size 'CK1; CK2'; Pasted text length and the three file-limit rows all three headers; the Presidio row 'CK1; CK3'", "T4, T5; main queue"),
    ("Planned marker", "no row used it", "one row (block (b) Sentinel integration) carries '— (planned, not in Table 3)'; legacy and inventory-only markers unchanged", "T7, R011"),
    ("Terms and Privacy clauses", "quoted in block (e), partly with process wording", "quoted verbatim, no interpretation; permitted use under clause 3.4.7 and consent under clause 3.3 stay open R8 questions, 'decided before any bench run' (R025 pattern, R032 wording); definition of Public Sector Entities and the undefined 'Agency' and 'license keys' recorded", "T9 to T15, T18, T19; main queue; R019"),
    ("Process language and internal ids in deliverable text", "'read with pypdf', 'research is read-only', 'not interpreted here', '(CK2 mechanism)', 'CK1 to CK3', 'open at CP1' and similar, about 25 occurrences", "product-neutral statements; internal ids replaced by the exact header text; two ruling ids ('Direction (R002)') removed from CK2 R3 and CK3 R3", "T70, T71; README section 4"),
    ("Cross-references to Presidio", "CK3 R4 had three Presidio bullets and restated Presidio facts", "one pointer per row, no restated Presidio facts", "T72"),
    ("Labels", "reversibility of Replace, Redact and Mask 'No [Inferred]' in block (d), [Not disclosed] in CK3", "[Not disclosed] with what was checked (R020 ruling 1); Mask-page conflict as two labelled facts; salts: no conclusion; positive facts split from absences (release notes, hosting)", "T33, T48, T50, T52, T73"),
    ("T66 (16 default-on rows 'On [Inferred]')", "resolver proposed upgrading to [Documented]", "NOT applied: main ruled the rows stay [Inferred] because the page shows SG_ADDRESS_STREET off, so 'all available' is loose; the scope paragraph P-ON text is unchanged", "main queue (cloak P5 Q1 to Q5, T66)"),
    ("Presidio tutorial URL", "https://microsoft.github.io/presidio/tutorial/12_encryption/ (HTTP 404) as a Source URL in blocks (d) and (f)", "https://presidio.dataprivacystack.org/tutorial/12_encryption/ (HTTP 200); the Cloak page's own 404 link stays recorded as an HTTP fact in the cell text", "T69; main queue; R016"),
    ("Bench content", "R7 bullets that reported what was or was not run; a 'bench could' plan", "bench content stays suggestion wording ('a bench could', 'possible', 'suggested'); the two session-report bullets in CK2 R7 and CK3 R7 deleted; sweep for 'bench will', 'we use', 'bench rule', 'this is the plan': 0 hits (section 8e)", "R032, T70"),
]

CONFLICTS = [
    "**Entity count (C1, T39).** Sources: FTA intro and portal Features page '20+' [Documented]; portal FAQs '17+' [Documented]; the entity pages give 17 groups [Documented] and 20 tags (drafter tally) [Inferred]. Chosen text: CK1 R2 keeps the two vendor counts as two bullets and the R2 Summary keeps the documented 17 groups (main). The tally bullet now reads 'one tag for each of the 16 groups other than Address, plus the 4 address tags' because the 17 groups already include Address.",
    "**Dates of birth and vehicle plates (C2).** Portal Features and FAQs name them [Documented]; no Cloak Guide entity page covers them [Not disclosed]. Both written in CK1 R2 and block (c); the single [To be verified] (does DATE_TIME catch a date of birth) stays.",
    "**Access wording (C3, T8).** Playbook: 'GovTech's dedicated internal service for comprehensive and localised PII detection' [Documented: repo govtech-responsibleai/playbook@45908b48]. Cloak Guide home page: 'open to select non-government entities (e.g. public healthcare)' [Documented]. Chosen text: two attributed bullets in CK1 R6 and two attributed facts in the block (b) non-WOG row; neither side chosen; CK2 R8 keeps the question.",
    "**Salts (C4, T52).** Pseudonymisation page: 'Custom salt values will be included in the future' [Documented]; release notes v2.1.0 and v2.1.4 list salt parameters and custom salts [Documented]. Chosen text: two bullets in CK3 R4 with no conclusion; block (d) aligned ('which of the two statements is current is [Not disclosed]'); the earlier 'probably stale [Inferred]' removed.",
    "**Mock Data Generation placement (C5, T64).** Portal Features lists MDG under Cloak [Documented]; the Mirage site lists it under Mirage and says it 'is available via API through Cloak' [Documented]; the Cloak Guide has no MDG page [Not disclosed]. Chosen text: all three quoted, and 'how the two placements relate is [Not disclosed]'; the phrase 'not reconciled here' removed.",
    "**Release-note order (C6, T33).** v2.2.2 (4 August 2024) is listed above v2.2.1 (28 August 2024). Chosen text: 'the highest version is v2.2.2 and the latest dated entry is v2.2.1'; 'newest' removed in CK1 R4, CK2 R4 and R8, CK3 R4; in CK3 R4 the positive fact is a [Documented] bullet and the deployed version a separate [Not disclosed] bullet.",
    "**File-limit history (C7, T67).** Release note v2.0.3 (15 January 2024) 'Maximum 10 columns' and 100k rows against the current usage guide (500 MB per file) [Documented]. Chosen text: the facts, the absence of a current column limit [Not disclosed] and 'the guide supersedes it' as [Inferred] with its premise.",
    "**Broken links (C8, C9, T69, T19).** The Cloak home page decryption link and the FAQ link to www.cloak.gov.sg/terms return 404; the Encrypt page's Presidio tutorial link returns 404. Recorded as HTTP facts [Documented] with the observation date; the working locations (go.gov.sg/cloak-terms, the dataprivacystack tutorial) are named.",
    "**Inside the Mask page (T48).** Usage Guide table: 'Suffix: masks the starting characters', 'Prefix: masks the ending characters' [Documented]; the example 120414 to '120' plus asterisks is 'Transforms into a suffix masked value' [Documented]. Chosen text: CK1 R6 and block (d) carry the two parts as separate labelled facts; neither chosen. The example is written as '120 followed by three asterisks' because asterisks would break the bold markup.",
    "**Terms numbering (T18).** The PDF numbers the disputes clause 15, while 15.2 and 15.3 refer to 'clause 14.3' and 'clause 14.2 above', and clause 14 is Severability [Documented]. Chosen text: numbers as printed; that the references mean 15.2 and 15.3 is [Inferred] with its premise.",
    "**LLM entity limit unit (T43).** Unstructured intro: 'per dataset (up to 5,000 documents)'; FAQ: 'normally one ... per project' [Documented both]. Chosen text: both quoted in CK2 R4 and block (c) (as drafted), now also in block (e) and as a CK2 R8 question (needs testing).",
    "**List limit unit (T42).** Fixed-list page: 'a maximum of 500 words'; Inclusion page: 'up to 500 entries' and 'first 500 words' [Documented all]. Chosen text (main): CK2 R6 Summary 'up to 500 (words or entries; the docs differ)'; CK1 R6 carries three bullets (entries, words, matching); the R8 question stays.",
    "**Confidence scope (T41).** Portal Features: 'Adjust detection sensitivity per entity type' [Documented]; Cloak Guide: one 'Adjust Confidence level' slider, default 0.30 from image captions [Documented]. Chosen text: CK1 R5 two bullets, one label each; block (e) keeps the [Not disclosed] fact on scope and gains both quotes; R8 keeps the question.",
    "**Slide 22 of the 2023 deck (T57, CORRECTION).** The text-layer reading ('Anonymised Response returns through the Transformer Module') is wrong: the rendered slide shows the response coming back from the 'Gen AI Magic!' box with the placeholder still in it and draws no restore step. Chosen text: layout [Documented], absence of a restore step [Not disclosed], in CK1 R3 and CK3 R3; CK3 R3's Inferred premise and CK3 R1's 'workflow' wording adjusted.",
    "**Terms clause 4.2 against Schedule 4.2 (T15, CORRECTION).** The triage and CK1 reviewer note 9 call routine deletion 'clause 4.2'; the PDF has it in Schedule 4.2, and main-body clause 4.2 is identity verification. Chosen text: the new block (e) row is titled 'Terms Schedule 4.1 and 4.2'.",
    "**PyCrypto owner (T20, PARTLY).** The draft said 'owner not named'; the PyPI page names an author and maintainers [Documented, PyPI page, not GovTech docs]. Maintenance status stays [Not disclosed].",
    "**Inclusion list placement (T5).** Brief put it in CK1's coverage text and in block (c) under CK2 only. Chosen: Covered-by 'CK1; CK2' for the Inclusion row; CK1 R6 carries the three Inclusion bullets, CK2 R1 and R6 keep the fuller pair of limit quotes.",
    "**Decrypt and Pseudonymise Covered-by (T4, main).** Decrypt acts on stored ciphertext, so the row is CK3 only; Pseudonymise stays 'CK1; CK3' because the salt bullets sit in CK3 R1, R4 and R6.",
]

HANDLED = (
    "- Resolution items applied: 39 (T3 to T20, T33 to T36, T39, T48, T50, T57, T59 to T61, T66 to T75; T66 not applied per main, T61, T68 and T17 need no text change, T3 is logged but the brief is not edited). "
    "Class b items with a drafting edit from the resolver's closing notes: T41, T42, T43, T52, T64; T1 and T2 closed by R037; T40, T62, T65 and the other class b items unchanged. "
    "CORRECTIONS applied: T57 (slide 22), T15 note (Schedule 4.2), T20 (PyCrypto owner)."
)

# T, item, class, where it stays, checked
OPEN = [
    ("T1, T2", "Column set and CK3 direction", "b (closed)", "R037: three columns, CK3 one column; revisit only if the gated API shows a direction setting", "-"),
    ("T21", "API direction flag (input or output) unknown; all three R3 Summaries say none was found", "b (honest gap)", "CK1, CK2, CK3 R3 and R8; inventory (b) API onboarding row", "all Cloak Guide pages, portal pages, home page; API Guide and OpenAPI redirect to the docs login (HTTP 302 then 200, observed 2026-10-10)"),
    ("T22", "API request and response schemas, limits, latency, API retention, prompt context", "b (honest gap)", "R5, R6, R8 in all columns; inventory (b), (e)", "login-gated; closed government service, not public"),
    ("T23", "API against Web UI: identical results, API-only features", "b", "CK1 R6 and R8, CK2 R6 and R8", "needs approved access"),
    ("T24", "LLM entity on the API or real-time path", "b (honest gap)", "CK2 R3 and R8", "public API guide page, FAQs, portal pages"),
    ("T25", "Reconstruct endpoint (v2.0.1) and the /analyze mapping-table route", "b (honest gap)", "CK3 R1, R3, R8; inventory (b)", "release notes, public API guide page, Replace (Unique) page"),
    ("T26", "Free-text decryption helper script and bulk restore API", "b (honest gap)", "CK3 R1, R6; inventory (a), (b), (d)", "login redirect observed 2026-10-10"),
    ("T27", "Latency of one short prompt; 'real-time' wording", "b", "CK1 R3 and R8, CK2 R8, CK3 R8; inventory (b), (e)", "only the CSV time table is given"),
    ("T28", "Model behind the baseline entities, version, tuning", "b (honest gap)", "CK1 R4 and R8; inventory (c) intro and 10 'Method not named' rows; (f) spaCy row", "entity pages, FAQ, Credits, release notes, portal, 2023 deck"),
    ("T29", "Per-entity detail gaps (method, credit-card checksum, non-SG passports, Exceptions matching, regex dialect)", "b (honest gap)", "inventory (c); CK2 R4 and R8", "entity pages per cell"),
    ("T30", "'Built on Presidio' stays [Inferred]", "b (honest gap)", "CK1 R4 and R8, CK2 R4, CK3 R4 and R8; inventory (f)", "no GovTech page says it"),
    ("T31", "Language model behind the LLM entity; whether Beta is current", "b (honest gap)", "CK2 R4 and R8; inventory (a)", "intro, add-entities, write-prompts, samples, FAQ, home, portal, release notes, Credits, deck, playbook"),
    ("T32", "Deployed version; ship dates of features absent from the release notes", "b (honest gap)", "CK1 R4 and R8, CK2 R4, CK3 R4", "release notes in full"),
    ("T37, T38", "Accuracy: the '>97% recall' claim has no method; no figures for custom entities or round trips", "b (honest gap)", "CK1 R5 and R8, CK2 R5 and R8, CK3 R5", "home, overview, FAQs, features page, deck"),
    ("T40", "Confidence default 0.30 and 0 to 1 range rest on image captions", "b", "CK1 R5, CK2 R5; inventory (e); caption named in the bullets", "caption re-read raw 2026-10-10"),
    ("T41", "Whether the confidence threshold is global or per entity type, and whether it applies to custom entities", "b", "CK1 R8, CK2 R8; inventory (e) [Not disclosed]", "portal Features and confidence page"),
    ("T42", "Whether the 500 limit counts words or entries", "b", "CK2 R8 and R6 Summary wording; CK1 R6", "fixed-list and Inclusion pages (both quoted)"),
    ("T43, T44", "LLM entity limit per dataset or per project; unit of '5,000 documents'", "b", "CK2 R8", "unstructured intro and FAQ (both quoted)"),
    ("T45", "Language coverage beyond roman-script names", "b (honest gap)", "CK1 R2 and R8, CK2 R2 and R8", "entity pages, FAQs, home, portal, custom pages"),
    ("T46", "Dates of birth and vehicle plate numbers; whether DATE_TIME catches a date of birth", "b", "CK1 R2 ([To be verified] bullet) and R8; inventory (c)", "two official sources differ"),
    ("T47", "Where checksum validation, global phone detection and Enhanced Detection are switched on", "b", "CK1 R6 and R8; inventory (c)", "NRIC, usage guide and confidence pages"),
    ("T49", "Which end the Mask default masks", "b", "CK1 R6 (conflict stated); inventory (d)", "masking page (two readings)"),
    ("T51", "Replace (Unique) on pasted text; Alias algorithm; NRIC masking mechanics; Exceptions matching", "b (honest gap)", "CK1 R6 and R8; inventory (c), (d), (e)", "pages list neither available nor unavailable"),
    ("T52", "Which salts statement is current", "b", "CK3 R4 and R8; inventory (d)", "Pseudonymisation page, release notes, Secrets Manager page"),
    ("T53", "Encrypt key length and format, key generation, IV storage, same value same ciphertext", "b (honest gap)", "CK3 R4, R5, R6, R8; inventory (d)", "Encrypt and Secrets Manager pages (captions only)"),
    ("T54", "Free-text failure behaviour (wrong secret, damaged token)", "b", "CK3 R5 and R8", "decryption and Secrets Manager pages"),
    ("T55", "Whole-reply restore; whether a model keeps base64 tokens intact", "b", "CK3 R3 and R8; inventory (a)", "free-text decryption page, intro, home"),
    ("T56", "Currency of the 2023 deck (dated 11 September 2023)", "b (honest gap)", "CK1 R3 and R5, CK3 R1, R3, R5, R8", "later docs are silent on a mapping table"),
    ("T58", "Custom versus built-in entity overlap; custom matches in the Findings table; threshold on custom entities", "b", "CK2 R5 and R8", "structured page"),
    ("T62", "Sentinel integration status and date", "b (honest gap)", "CK1 R8; CK2 R8; inventory (b) planned row", "playbook text identical at staging 45908b48 and main 97338569; aiguardian.gov.sg /docs and /docs/wiki/Sentinel-Guardrails have no 'cloak' hit"),
    ("T63", "'ContextGuard Demo' on the Video Guides page", "b (honest gap)", "CK1 R8, CK2 R8", "Cloak Guide, portal, home"),
    ("T64", "MDG placement (Cloak portal against Mirage)", "b (honest gap)", "inventory (a) MDG row: relation [Not disclosed]", "Cloak Guide sidebar, portal, both home pages"),
    ("T65", "Meaning of the PROOF OF VALUE badge; 'Available [Inferred]' status basis", "b (honest gap)", "inventory (a) FTA and Tabular rows", "portal overview and home page"),
]

# T, residual, class, label, checked
RES = [
    ("T9", "Whether a comparison bench falls under clause 3.4.7 (benchmarking) and whether clause 3.3 consent would cover it; no exception for evaluation is stated", "c", "[Not disclosed]", "all 15 pages of the Terms, the FAQ, the Privacy Statement, the home page; permitted use decided before any bench run (R025 pattern, R032 wording)"),
    ("T10", "Whether a bench could obtain written consent under clause 3.3; the meaning of 'Agency' (Schedule 2.2)", "c", "[Not disclosed]", "15 pages; FAQ"),
    ("T11", "Whether sharing secrets under the Secrets Manager is 'sharing of license keys' (clause 3.4.9)", "c", "[Not disclosed]", "'license keys' is not defined in the 15 pages"),
    ("T13", "The meaning of 'above' in Schedule 4.6 (the backslash is printed in the PDF)", "c", "[Documented] (text only)", "page 15 rendered and read"),
    ("T14, T15", "A retention period in the Terms (Schedule 4.2 says 'a reasonable period') and in the Privacy Statement; whether the Privacy Statement paragraphs and the FAQ describe the same data", "c", "[Not disclosed]", "15 Terms pages, 4 Privacy pages, FAQ"),
    ("T18", "That the Terms cross-references 'clause 14.3' and 'clause 14.2 above' mean 15.2 and 15.3", "c", "[Inferred]", "clauses 14 and 15 read in the PDF"),
    ("T19", "A Terms version later than 24 July 2024", "c", "[Not disclosed]", "cloak.gov.sg home and register pages, FAQ, docs home, the PDF"),
    ("T20", "Current maintenance status of PyCrypto", "c", "[Not disclosed]", "PyPI page gives release dates only"),
    ("T33", "The deployed Cloak version", "a", "[Not disclosed]", "release notes in full, home, portal"),
    ("T39", "What the deployed Web UI actually shows against the entity pages (17 groups, 20 tags)", "a (UI check, stays with the bench)", "[Inferred] for the 20-tag tally", "entity pages recounted at source"),
    ("T57", "Where and how placeholders are restored from the mapping table in the deck", "a", "[Not disclosed]", "slide 22 rendered; text of all 32 slides"),
    ("T66", "Whether 'On [Inferred] (premise P-ON)' in the 16 default-on rows should be [Documented]", "a (main: stay Inferred)", "[Inferred]", "usage guide says 'all available Entity Types' but SG_ADDRESS_STREET is off by default"),
    ("T67", "Whether the usage guide supersedes the v2.0.3 limits (the guide pages are undated)", "a", "[Inferred]", "usage guide, FAQ, release notes through v2.2.2"),
]

FYI = [
    "**Brief not edited (T3).** The brief still has the old CK2 and CK3 header wording at lines 24, 25, 34, 180 and 183. The resolver proposed replacing lines 24 and 25 and adding one line under the heading 'Table 3 headers (exact)': 'CK2 and CK3 wording as ruled by main (queue.md, cloak P1 Q4) and R037; the older wording in the Why-the-header-wording paragraph and in Q01 and Q04 is superseded.' The merger may write only the P6 outputs and its scratchpad, so main (or the drafter role) can apply it. Not a build input.",
    "**Optional Source URL not added (T20).** https://go.gov.sg/cloak-open-source (HTTP 302 to the Credits page) is named in the block (f) intro only; it is not added to the Presidio or spaCy Source cells, because the Credits URL is already there.",
    "**Deck date (T56).** CK1 A:49 and the 'may have changed' bullets already carry the deck date; no other bullet was changed.",
    "**No text change by design:** T16 (the Terms 9.1 bullet was added; the block (e) row already quoted both), T17 (block (e) row matches the PDF), T61 (counts re-run: no Summary above limit minus 1), T68 (pins confirmed as the latest tags), T40, T62, T65.",
    "**Not interpreted:** Terms clauses are recorded as printed. No licensing or permitted-use conclusion is drawn anywhere in the finals (main; R019; R032).",
]

NOTES_STATUS = (
    "- CK1 note 8 (slide 22 layout order not guaranteed): closed by T57 (the slide was rendered and its drawn arrows listed); CK1 R3 and CK3 R3 corrected.\n"
    "- CK1 note 9 ('Terms clauses 6.1 and 4.2 (data licence and routine deletion)') is corrected to 'Terms clause 6.1 (data licence) and Schedule 4.2 (routine deletion)'; both are now block (e) rows (T15).\n"
    "- CK1 note 1 (Inclusion list in CK1 or CK2): resolved by T5 (Covered-by 'CK1; CK2'). CK1 note 3 C3 (access wording): now in CK1 R6 and block (b) (T8). CK1 note 3 C6: handled by T33.\n"
    "- CK2/CK3 note 2 should read: 'The anonymise side and the restore side are separate bullets in R1, R3, R5 and R6 (13 bullets start Anonymise side, 10 start Restore side); R2, R4 and R7 are not split by side, so a later split of CK3 would need a side added there (R037: one column; revisit only if the gated API shows a direction setting).' (T75; the draft note listed R4 wrongly.)\n"
    "- CK2/CK3 note 6a (LLM limit per dataset against per project) is now an R8 bullet in CK2 and a block (e) fact (T43). Note 6b (500 words against entries): see conflict 12.\n"
    "- Inventory note 1 (Decrypt under both CK1 and CK3): Decrypt is now CK3 only (main). Note 2 (row counts): now 10, 8, 26, 9, 28, 4 = 85. Note 4 (C3 not in the inventory): C3 is now in block (b). Note 5 ('a planned Sentinel row would need the planned marker'): the row and the marker are in (b).\n"
    "- Inventory self-check line ('tables 10, 7, 26, 9, 25 and 4 rows (81 rows)') is superseded by section 8f of this file."
)
