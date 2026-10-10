# cloak P10 diagram review: benchtest/diagrams/cloak-explained.html (last changed in 027f2fc; clean at HEAD 4172873)

- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-11.
- Sources of truth: benchtest/drafts/cloak_two_level.md (CK1 to CK3), cloak_inventory_final.md (blocks a to f) and cloak_changes.md, as approved in R039.
- Rulings read: R026, R027, R028, R032, R037, R039. Also main's P10 ruling in queue.md ("cloak P10 Q1–Q4"): the legend swatch must read "Not disclosed"; Output Partly and Reversible Partly stand; the planned Sentinel box stays in the access diagram only.
- Sibling cells compared word for word against presidio-explained.html and sentinel-explained.html (plus sdp, modelarmor, lionguard and litmus as cross-checks).
- Renders: benchtest/scratchpad/verifier/cloak_diagram/cloak_{light,dark}_{1280,375}.png, crops fig0 to fig9 and header in light and dark, and phone_top.png. All PNGs are gitignored by `benchtest/scratchpad/**/*.png` (checked with git check-ignore). Scripts: check.py, sib.py, render.py and figs.py in the same folder.
- URL results: cloak_diagram/url_results.txt.

## Verdict: PASS WITH FIXES (7 required fixes)

The page is structurally clean:
- The shared CSS (lines 6-110) is byte-identical to Sentinel's.
- Extra CSS sits only in one final "Additions for this page" block, and the line 5 comment is rewritten.
- The file is a fragment: no doctype, html, head, body, script, img or viewport.
- All 10 SVGs carry a viewBox, role="img" and a full-sentence aria-label. No SVG element has fill, stroke or style attributes, and no svg has width or height.
- All 12 marker ids (o-a, a2, a4/a4e to a8/a8e) are unique, used, and resolve.
- The page renders in light and dark. At 1280 and 375, scrollWidth equals innerWidth, and no SVG text runs outside its box or the viewBox.
- All 32 sibling cells in the positioning table (NeMo, Llama Guard, Sentinel and Presidio, 8 rows) match the reviewed pages exactly (R027).

The specific points main asked about:
- "Built on Presidio" is hedged exactly as the drafts are: tag names and the Encrypt page "could mean shared parts", and "No GovTech page says Cloak is built on Presidio".
- Terms clauses 3.4.7 and Schedule 2.2 are quoted verbatim (checked against the live PDF) and shown as "recorded, not decided".
- ">97% recall" is credited to GovTech with "no data set, method or precision".
- All eight scorecard pills match the drafts and main's ruling.
- The "Tag (our tally)" column is labelled as ours, and the rail's Good to know repeats it.
- The deck correction is respected: no restore step is credited to the 2023 slides.

The seven fixes:
- RF1: the legend swatch reads "Not public", not "Not disclosed". Main's ruling makes this required.
- RF2: "add up to 8 hours" misreads the source, which says processing time rises "to up to 8 hours". It appears twice.
- RF3: the encrypt, AI model and decrypt round trip is drawn as fact. The drafts mark it [Inferred].
- RF4: the access map widens "MOHH entities" to "public healthcare bodies".
- RF5: WOG-AD is not glossed.
- RF6: access routes are drawn as `gate` boxes, which mean "Check done by Cloak".
- RF7: "built-in types miss ... case numbers" contradicts the vendor example, where a case number is detected, but as the wrong type.

## 1. Required fixes

**RF1. Header legend (line 133): swatch label.**
- Problem: main's P10 ruling (queue.md, cloak P10 Q1–Q4; diagrams README §8) requires the `.sw.nd` swatch to read "Not disclosed". The Litmus page uses that wording.
- Old: `    <span><i class="sw nd"></i>Not public</span>`
- New: `    <span><i class="sw nd"></i>Not disclosed</span>`
- Keep the matching wording in diagram 3. Old (line 432): `<text class="tb" x="10" y="254">Not public</text>`. New: `<text class="tb" x="10" y="254">Not disclosed</text>`. The `.ts` line under it ("behind a login") stays, so the reason is still given. Without this second change, the swatch and the only boxes it describes carry different names.

**RF2. "Up to 8 hours" is misread (line 469 and line 669).**
- Source (draft CK2 R3; inventory e, LLM row; verified verbatim at custom-entities-unstructured/intro.md line 9): "Including an LLM-enabled custom entity may increase processing times to **up to 8 hours**." This gives a total ceiling. It does not say 8 hours are added.
- Old (line 469, Speed row): `An AI-model custom type can add up to 8 hours.`
- New: `Adding an AI-model custom type can raise processing time to up to 8 hours.`
- Old (line 669): `no accuracy is published for any custom type, and the AI-model type can add up to 8 hours of processing.`
- New: `no accuracy is published for any custom type, and the AI-model type can raise processing time to up to 8 hours.`

**RF3. Diagram 6 (lines 566-621): the chat round trip is drawn as documented.**
- Problem: the drafts label the round trip [Inferred]:
  - CK3 R3 Summary: "Encrypt on the way out, decrypt on the way back … **[Inferred]**".
  - CK3 R3 Detail: "Anonymise side acts on the text going to a model and restore side on text coming back … [Inferred]".
- What GovTech documents is Encrypt, the Secrets Manager and one-value-at-a-time decryption. No Cloak page shows a model answer being decrypted.
- The page states the flow flatly ("The AI model never sees the real name, yet the user does."). Its only hedge covers token survival. README §10 says anything uncertain in the drafts must stay hedged.
- Old (figcaption, line 614): `<figcaption>The AI model never sees the real name, yet the user does. In the web UI the restore step takes one pasted value at a time;`
- New: `<figcaption>No Cloak page shows this round trip with an AI model; it is our reading of the Encrypt and decryption pages. In it the AI model never sees the real name, yet the user does. In the web UI the restore step takes one pasted value at a time;`
- The rest of the figcaption is unchanged.
- Optional for the same reason: begin the aria-label (line 578) with `A possible round trip, our reading of Cloak's pages: the user's message contains a name.` in place of `The user's message contains a name.`

**RF4. Diagram 3 (lines 398 and 417-418): MOHH is widened to all public healthcare.**
- Source (CK1 R6; inventory b, non-WOG row): "Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step."
- The drafts never equate MOHH with all public healthcare bodies. "public healthcare" appears separately, only as an example of the select non-government entities.
- Old (aria-label fragment, line 398): `public healthcare bodies skip the pre-approval step.`
- New: `the FAQ exempts MOHH entities from the pre-approval step.`
- Old (line 417): `<text class="tb" x="660" y="114" text-anchor="middle">Public healthcare</text>`
- New: `<text class="tb" x="660" y="114" text-anchor="middle">MOHH entities</text>`
- Old (line 418): `<text class="ts" x="660" y="133" text-anchor="middle">MOHH: no pre-approval</text>`
- New: `<text class="ts" x="660" y="133" text-anchor="middle">no pre-approval step</text>`

**RF5. Diagram 3 figcaption (line 450): WOG-AD is not glossed.**
- Problem: "WOG-AD" first appears in a `.ts` line (line 403). No sentence ties it to its meaning. README §9 says to gloss every term on first use, and §11 has the same checklist item.
- Old: `<figcaption>Government users sign in with their government account and need no onboarding for the web UI.`
- New: `<figcaption>Government users sign in with their government account (WOG-AD, the whole-of-government sign-in) and need no onboarding for the web UI.`

**RF6. Diagram 3 (lines 401, 404, 422, 425 and 428): access routes are drawn as checks.**
- Problem: `gate` (blue) means "Check done by Cloak" (README §4, legend). The Web UI, the API and the three API levels are ways in, not checks.
- Litmus's sibling access map draws its routes as plain `box`.
- Fix: in these five rects, change `class="gate"` to `class="box"`. Coordinates and text do not change. The Not disclosed (`mk-nd`) and Planned (`mk-plan`) rows keep their classes.
- Old: `<rect class="gate" x="190" y="20" width="275" height="56" rx="8"/>` New: `<rect class="box" x="190" y="20" width="275" height="56" rx="8"/>`
- Make the same change at x="475" y="20", x="190" y="160", x="380" y="160" and x="570" y="160".

**RF7. Custom-entities stage head (line 630): "miss ... case numbers" contradicts the vendor example.**
- Source:
  - CK2 R2: "Suppose a 10-digit hospital case number (e.g. 1234567890) is consistently detected as a Bank Account Number". Verified verbatim at custom-entities-structured.md line 79. The case number is found, but under the wrong type.
  - CK2 R2: "Car license number" is a regex sample use case.
- Old: `The built-in types miss things such as hospital names or case numbers.`
- New: `The built-in types do not cover things such as hospital names or car licence numbers, and can label others wrongly: GovTech's example is a hospital case number detected as a bank account number.`

## 2. Optional suggestions

1. **Line 340 (tag of "What Cloak can find").** "by default it scans for all of them" sits above a row saying the street part is "OFF (advanced)" by default. Main ruled at P5 that "all available" is loose. Suggest: `Seventeen groups on the entity types page; by default it scans for all of them except the street-name part of addresses`.
2. **Line 126 (lede).** "a few approved outside bodies": the source says "select", which does not mean few. Suggest "selected approved outside bodies" or "some approved outside bodies".
3. **Line 560 (Output Good to know).** The slide check holds: the response returns from "Gen AI Magic!" with "<hash value 1>" still in it, and no Cloak box sits on the way back. To tie it to the correction in cloak_changes.md (T57), suggest replacing ", not rewritten again." with `; the slide draws no step that puts the real value back.`
4. **Overview (lines 205-209).** The "encrypted values" arrow starts at the Output anonymising box and ends at Restore (decrypt). It reads as if decryption follows re-anonymising the answer. Suggest starting the arrow from the AI-model-to-output line (for example `M523,200 V306` with the box moved under it), or adding `.ts` "if Encrypt was used". Either is a layout choice, not a fact error.
5. **Line 270 (positioning Good to know).** Tag names (PERSON, EMAIL_ADDRESS, PHONE_NUMBER, IBAN_CODE) appear in body prose. README §9 limits identifiers to tags, `.ts`, `td.code` and `mark`. Suggest: "some tag names, such as those for names, emails, phone numbers and IBANs, match Presidio's".
6. **Lines 344 and 367 (tables).** The "Group" column has 8 rows directly under "Seventeen groups". Suggest the header "Kind of data (grouped here)". Technique names in `td.code` (Replace (Unique), NRIC masking) are names, not fixed codes. Plain `td` would follow README §5.
7. **Line 662 (diagram 7 figcaption).** `such as "five digits in a row"` is in quotation marks and could be read as a vendor quote. Drop the quotation marks.
8. **Line 687 (diagram 8 aria-label).** "Every cell or page is rewritten" overstates the source, "implemented across all cells … and on all pages". Suggest "The chosen techniques apply across every cell or page".
9. **Line 621 (rail 6 Good to know).** Add after "the Terms do not define the term": `, and whether sharing a secret counts is not stated.` This matches CK3 R8. Clause 3.4.11 ("provide third party access to the Service", R037) is not on the page. It could be added to limits item 3 if wanted.
10. **Footer (line 761).** The page cites the Privacy Statement (limits table, retention row), but the footer neither names it nor links it. Its URL is in the drafts (inventory e: https://go.gov.sg/cloak-privacy). Suggest adding "the Privacy Statement (dated 1 December 2022)" to the sources and a "Privacy Statement" link.
11. **Line 610 (diagram 6).** The Secrets Manager is drawn as `gate` (a check). It stores keys and is not a check, so a `box` fits it better. This is low priority.
12. **First uses of UEN (line 265) and MOHH.** UEN is glossed only later, in the entity table. Consider moving the gloss to its first use.

## 3. Checklist (diagrams README §11)

| Item | Result |
|---|---|
| CSS 6-110 identical; additions block; line 5 rewritten | PASS (diff empty) |
| Fragment format | PASS |
| Title, h1, eyebrow | PASS: "How GovTech Cloak Anonymises a Conversation"; "GovTech Cloak · hosted service, approved users only" |
| Legend lists exactly the roles used, with house wording | FAIL until RF1 (label). Every swatch is used and no used role is missing (gate, dev, ed, part, na, mk-nd, mk-plan; no ok or no boxes) |
| dev only where the product does not act; part/na with matching pills | PASS after RF6 (gate misuse on access routes) |
| SVG attributes, aria-labels | PASS |
| Markers unique, resolve, none unused | PASS |
| Section order, stage numbers, sequential h3, diagram refs | PASS. Input 1, Output 2, then extras for input and output (reversible, own types), then Retrieval 3. h3 1 to 8 are sequential, plus unnumbered table rails. "diagram 4/5/6/7/8" references are correct |
| Scorecard: five checkpoints in NeMo order plus extras, pills match stages | PASS: Input Yes, Output Partly, Retrieval Partly (R026: file inputs documented), Dialog No, Execution No, Images No, Reversible Partly, Own entity types Yes |
| Limits 6-8 with bold leads and stock phrases | PASS (8 items) |
| Every claim traces to the drafts; vendor numbers attributed | FAIL until RF2, RF3, RF4 and RF7 |
| Voice, glossing, identifiers | FAIL until RF5. Optional 5 and 12 are minor |
| Footer mirrors the drafts' URLs | PASS. Every footer URL is in the drafts. Optional 10 adds the Privacy Statement |
| Light and dark, 1280 and 375 | PASS. Dashes and tints are visible in dark. The `mk-plan` dashes are faint but visible, as on Litmus |
| No horizontal overflow | PASS: scrollWidth equals innerWidth (1280 and 375, light and dark) |
| Looks like a sibling | PASS |

## 4. Traceability notes (claims checked, no fix needed)

- Lede, positioning cells and Who-runs-it: CK1 R1 and R4, inventory a and b.
- Score scale: the 0.30 default, the raise or lower advice and the per-kind conflict match CK1 R5 and inventory e.
- Entity table: all 20 tags, NRIC "Validation disabled", phone SG-only with no validation, "OFF (advanced)", the DOB and vehicle-plate open question, and the 20+ versus 17+ counts match CK1 R2 and inventory c.
- Techniques table: matches inventory d, including the "no longer allowed to used masked / partial NRICs" typo kept verbatim, "irreversible", and AES-256 reversible with the key.
- Access map: L2/L3/L4, the 1-2 business day key, the Ops team, the purpose in writing (Terms 3.3), the PROOF OF VALUE badge and the package "provided as-is with no active maintenance" match inventory b and CK1 R4/R6.
- Limits table: every quote matches CK1 R6 and inventory e.
- Input: GovTech's own use, the illustrative Jane Tan example and recall attributed to GovTech match CK1 R1 and R5.
- Output: Partly with "our reading", and the playbook list, match CK1 R3 and main's P10 ruling.
- Reversible: the Jason token example (Encrypt page), the 10/50 sharing limits and clause 3.4.9 with "license keys" undefined match CK3 R4, R6 and R8.
- Custom: CGH and cgh, 3 to 5 examples, one per dataset, model not disclosed and overlap not stated match CK2 R4, R6 and R8.
- Retrieval: Partly per R026, "our reading", and native PDF to .docx match CK1 R3/R5 and inventory e.
- Limits list: every item traces, including salts, the Mask contradiction, the 404 Presidio tutorial and release notes ending in August 2024.

## 5. Spot-checks at source (verbatim, fetch_text.py, 2026-10-11)

| # | URL | Quote checked | Result |
|---|---|---|---|
| 1 | .../fta/entity-types/personal/name.md | "including ethnic names in roman characters" | MATCH |
| 2 | .../fta/entity-types/personal/nric.md | "Both real and fake NRIC numbers following the format" | MATCH |
| 3 | .../fta/entity-types/personal/full-address.md | SG_ADDRESS_STREET "OFF (advanced)" | MATCH |
| 4 | .../faqs.md | "Free-text detection is probabilistic, so 100% recall should not be assumed." | MATCH |
| 5 | .../masking/nric-masking.md | "agencies are no longer allowed to used masked / partial NRICs" | MATCH |
| 6 | .../fta/usage-guide.md | "Maximum 20,000 characters (approx. 3,000 words) per submission." | MATCH |
| 7 | .../faqs.md | "Cloak does not process scanned PDFs, screenshots, images or engineering drawings." | MATCH |
| 8 | .../faqs.md | "Confidential Cloud-Eligible (CCE), Sensitive-High (SH)" | MATCH |
| 9 | .../faqs.md | "Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request." | MATCH |
| 10 | .../fta/usage-guide.md | "Text and PDF projects typically have a fast processing time" | MATCH |
| 11 | .../home.md | "Cloak is currently free for all approved users" ("free" is bold in the source); "For FY26, there is no charge." | MATCH |
| 12 | .../home.md | ">97% recall for key PIIs like Name, NRIC and Email" | MATCH |
| 13 | .../home.md | "provided as-is with no active maintenance" | MATCH |
| 14 | .../custom-entities-unstructured/intro.md | "may increase processing times to up to 8 hours" | MATCH with the drafts; the page MISMATCHES it ("add up to 8 hours", RF2) |
| 15 | .../anonymisation-techniques/encrypt.md | "pX09dIQ4X3gU1FC3r8pZXA==" for "Jason" | MATCH |
| 16 | .../release-notes.md | "[API] Reconstruct endpoint for FTA API" | MATCH |
| 17 | developer.tech.gov.sg .../cloak/faqs | "Cloak detects 17+ entity types out of the box" | MATCH |
| 18 | .../fta/intro-to-fta.md | "Cloak detects and transforms 20+ baseline entity types" | MATCH |
| 19 | .../decryption/secrets-manager.md | "up to 10 other users per operation", "maximum of 50 users per secret" | MATCH |
| 20 | .../custom-entities-structured.md | "a 10-digit hospital case number … detected as a Bank Account Number" | MATCH (basis of RF7) |
| 21 | https://www.cloak.gov.sg | "Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM." | MATCH |
| 22 | developer.tech.gov.sg .../cloak/overview | "PROOF OF VALUE" | MATCH |
| 23 | raw.githubusercontent.com playbook@45908b48 privacy-improvements.mdx | "GovTech's dedicated internal service"; "Direct integration with the Sentinel API is coming soon."; "Model outputs." "Retrieved documents." "Tool arguments and tool results." | MATCH |
| 24 | https://file.go.gov.sg/cloak-terms.pdf (15 pages) | "perform any benchmarking tests or analyses of the Service"; "You are not permitted to use this Service if you are not using the Service for and on behalf of your Agency."; "sharing of license keys to or with a third party"; 'as is'; "dated 24 July 2024"; "consented to in writing (including via email)" | MATCH |
| 25 | usenix.org pepr23_slides-tang.pdf, slide 22 (rendered PNG from P7) | The Anonymised Response returns from "Gen AI Magic!" to the Agency Product with "<hash value 1>" and no restore step drawn | MATCH |

Tally: 25 checked, 25 match at source. One page wording misreads its source (RF2).

## 6. URLs (curl, 2026-10-11; 32 hrefs: 26 http(s) content links, 2 font hosts and 4 local sibling links)

- 200: 24 content URLs (the Cloak Guide pages, portal pages, cloak.gov.sg, the Terms PDF, the USENIX PDF and the aiguardian Sentinel-Guardrails page).
- 302 then 200 at the login page: https://docs.developer.tech.gov.sg/docs/cloak-api-guide/ goes to /auth/otp-login?…redirect_reason=not_logged_in. This is expected: it is labelled "API guide (login required)" and was not signed in.
- 503 (3 of 3 tries): https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/improving-ai-systems/privacy-improvements.mdx.
  - The file exists at the pinned SHA. The same path with `?plain=1` returns 200, the raw.githubusercontent.com copy returns 200, and the tree and commit pages return 200.
  - Only the rendered .mdx view fails from this network.
  - P9 classed it the same way (scratchpad/url-checker/cloak: "blocked-by-proxy").
  - Class: a network or rendering block, not a dead link. See QUESTIONS Q1.
- 404: https://fonts.googleapis.com/ (preconnect origin, not a page). Expected; same as every sibling page. The fonts stylesheet itself returns 200.
- Local: llama-guard-, nemo-rails-, presidio- and sentinel-explained.html all exist.

## QUESTIONS

- Q1 (main): the playbook GitHub blob link returns 503 from here, while `?plain=1` and raw return 200. Should it stay as P9 classified it, or should the footer use the deployed playbook page? That page is https://govtech-responsibleai.github.io/playbook/improving-ai-systems/privacy-improvements/: HTTP 200, already in the drafts (inventory b, Sentinel integration row) and observed with the same text. A one-link footer change would fix this; it is not required.
- Q2 (main): RF6 (access routes as `box`, not `gate`) follows the Litmus precedent and README §4. If main reads blue as "Cloak-owned" rather than "a check", RF6 can be downgraded to optional.
