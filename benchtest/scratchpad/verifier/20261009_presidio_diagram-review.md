# Presidio explainer: diagram review (P10)

- Page: `benchtest/diagrams/presidio-explained.html` (commit 5de6bfb, 803 lines)
- Sources of truth: `benchtest/drafts/presidio_two_level.md`, `benchtest/drafts/presidio_inventory_final.md`; rulings R016, R022
- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-09
- Scripts and screenshots: `benchtest/scratchpad/verifier/presidio_diagram/` (`mech.py`, `render.py`, `figs.py`, `url_check.txt`; PNGs are gitignored)

## Verdict: PASS WITH FIXES

The page is structurally sound, renders cleanly in light and dark at 1280 and 375, has no clipped SVG text, and every vendor number matches the drafts. There are 8 required fixes:

- One is structural: the positioning table compares Presidio with no other tool.
- Three are example labels and a gloss.
- Four are over-claims or wrong wording in the limits list and the footer.

## Main's specific points

### 1. The `min-width: 0` addition

- `diff <(sed -n 6,109p sentinel-explained.html) <(sed -n 6,109p presidio-explained.html)` prints nothing. The same is true against `llama-guard-explained.html`, so base lines 6-109 are byte-identical.
- The only extra CSS is the final block (lines 110-112), headed `/* Additions for this page: tick marks on the score scale; let grid children shrink so only figures and tables scroll sideways on phones */`:
  - `.tick` is copied from Sentinel's additions and uses `var(--ink)`.
  - `.wrap > *, .stage > *, .grid2 > * { min-width: 0; }` is the overflow fix.
- **Harmless: yes.** Measured in Playwright with the line present and with it removed:
  - At 1280, light and dark: 0 of 759 element boxes inside `.wrap` change, so desktop layout is unaffected.
  - At 375: scrollWidth is 628 without the line and 375 with it. Only figures and tables scroll sideways.
- Reference pages at 375 (fragment, light) all have scrollWidth 628: sentinel, llama-guard, nemo-rails and sdp. In each, the overflow starts at `header`, `.eyebrow` and `h1`.
- It adds no colour or look change. Whether to apply it to every page is left as a user question, as instructed.
- The page passes the checklist line "No horizontal page overflow" only because of this addition.

### 2. Glosses and the NRIC illustration

| Item | Judgement |
|---|---|
| "UEN type (a business registration number)" | Acceptable. UEN (Unique Entity Number) is Singapore's registration number for businesses and other registered entities. The gloss is accurate for a lay reader. Optional refinement in O7. |
| "NRIC and FIN pattern (Singapore's national ID numbers)" | **Not accurate enough: fix required (R4).** The NRIC is the national identity card number. The FIN (Foreign Identification Number) is issued to foreigners, so calling both "national ID numbers" is wrong for FIN. Readers in the Singapore public sector will notice. Expanding the two acronyms is enough, and is general knowledge of the same kind as the UK expansion. |
| "UK_NINO = national insurance number" (UK row: "national insurance number ... are off") | Acceptable. This is the plain expansion of NINO, and the drafts list "NINO" as disabled (PD1 R2; inventory UK row). |
| Rail 4 masked example: "My NRIC is S1234567D, email `<EMAIL_ADDRESS>`. (expected in a default setup; not tested)" | **Acceptable as a hedged illustration.** It follows directly from draft facts: `SgFinRecognizer` is `enabled: false` (YAML at the tag; 74 entries, 24 enabled, re-parsed), and `EmailRecognizer` is enabled. It is labelled as untested.<br><br>I also checked at source that no default-enabled US pattern would catch `S1234567D`:<br>- The US driver-licence alphanumeric regex at 2.2.364 has no alternative of the form letter + 7 digits + letter, and `\b` prevents partial matches.<br>- US passport needs `\b[A-Z][0-9]{8}\b` or 9 digits.<br>- US bank number and SSN are digit-only.<br><br>So the expectation is plausible. spaCy NER behaviour cannot be ruled out without a run, which the "not tested" wording covers. Optional wording alignment in O8. |

### 3. Positioning compares with NeMo only

**Not acceptable as it stands. Fix required (R1).**

- README section 1, question 4, and section 9 ("compare ... against Sentinel and Llama Guard in the positioning table") require the comparison.
- The rationale "the drafts hold no such facts" does not hold. The NeMo, Llama Guard and Sentinel cells are not new Presidio facts. They are cross-references reused verbatim from the already verified sibling pages, and `sentinel-explained.html` and `sdp-explained.html` (same batch) do exactly this.
- The current second table is a one-column "comparison" (`<th></th><th>Presidio</th>`) that compares nothing. It also drops the README rows "Your own rules and fixed replies" and "Singapore languages", although the drafts support Presidio cells for both.
- Keeping the two-zone SVG (Presidio and NeMo) is fine, because NeMo actually calls Presidio. Only the table and the stage-head need to change.

### 4. Vendor numbers

All match the drafts exactly. Source checks are in the next section.

| Page | Draft | Status |
|---|---|---|
| "about 7 in 10 of the things it flagged were real" | precision 0.733 (PD1 R5, notebook 4, cell 19) | MATCH (rounded) |
| "found about 6 in 10 of the personal data present" | recall 0.646 | MATCH (rounded to the nearest whole number per README section 9) |
| "1,500 made-up text samples, default detectors, cut-off 0.4" | 1500 synthetic samples, default recognizers, threshold 0.4 | MATCH |
| "not recommended for production" | notebook 4, markdown cell 9 | MATCH |
| 0.85 fixed NER score | `ner_strength: float = 0.85` | MATCH |
| 80 distinct types (our count) | 80 on the live page (PD1 R2, Inferred) | MATCH, hedged as "our count" |
| 24 of 74 entries on | 74 entries, 24 enabled | MATCH |
| eight phone regions (US, GB, DE, FR, IL, IN, CA, BR) | inventory, phone row | MATCH |
| default cut-off 0; examples 0.4 and 0.7 | PD1 R5 | MATCH |
| 60-second regex timeout | PD6 R4 | MATCH |
| 44-character token | PD3 R5 (Inferred: 1 to 15 bytes gives 44 base64 characters) | MATCH, labelled illustrative |
| docs last published 2026-07-04; release 2.2.364 | PD1 R4 | MATCH |
| four DICOM sample files | PD4 R5 | MATCH |

### 5. URLs

There are 17 hrefs, excluding the fonts link; no `*.googleapis.com` URL was requested.

- **17/17 return HTTP 200**, with no redirects.
- The three github.com blob links (notebooks 4 and 5, `default_recognizers.yaml`) return 200 directly. Their raw.githubusercontent.com equivalents also return 200.
- Every footer URL appears in the drafts, either in an R9 list or an inventory Source URL.
- Details are in `presidio_diagram/url_check.txt`.

## Spot-checks at source (fetch_text.py / raw files)

| # | Claim on page | Source | Quote / value | Result |
|---|---|---|---|---|
| 1 | precision about 7 in 10, recall about 6 in 10 | raw notebook 4 @0.3.2, cell 19 output | `{'F2': 0.661, 'Precision': 0.733, 'Recall': 0.646}` | MATCH |
| 2 | "not recommended for production" | notebook 4, cell 9 | "Using Presidio with default parameters (not recommended for production)." | MATCH |
| 3 | 24 of 74 entries on; Singapore pattern off | raw `default_recognizers.yaml` @2.2.364, parsed | 74 entries, 24 enabled; `SgFinRecognizer` enabled False; no Sg UEN entry | MATCH |
| 4 | eight phone regions | raw `phone_recognizer.py` @2.2.364:29 | `DEFAULT_SUPPORTED_REGIONS = ("US", "GB", "DE", "FR", "IL", "IN", "CA", "BR")` | MATCH |
| 5 | fixed name score 0.85 | raw `spacy_recognizer.py` @2.2.364:41 | `ner_strength: float = 0.85,` | MATCH |
| 6 | Image Redactor "not production ready" | /image-redactor/ | "Please notice, this package is still in beta and not production ready." | MATCH |
| 7 | "a library or SDK rather than a service" | /faq/ | "Presidio is a library or SDK rather than a service." | MATCH |
| 8 | "not an official product of any company and comes with no warranty or SLA" | /faq/ | identical sentence | MATCH |
| 9 | endpoints have no authentication by design | /faq/ | "Presidio API endpoints do not include built-in authentication by design." | MATCH |
| 10 | "in the process of transitioning"; Microsoft supports; MIT stays | /project_transition/ | "...is in the process of transitioning from a Microsoft-owned project to an independent, community-governed open source project..."; "Microsoft supports this transition..."; "Presidio will continue to be open source under the MIT license." | MATCH |
| 11 | random salt by default; no session | /anonymizer/ | "Starting from version 2.2.361, the hash operator uses random salt by default for security."; "Presidio does not store or maintain stateful sessions." | MATCH |
| 12 | Word list TITLE: Mr., Mrs., Miss (Presidio's docs); In "Mr. Schmidt" | /analyzer/adding_recognizers/ | `PatternRecognizer(supported_entity="TITLE", deny_list=["Mr.","Mrs.","Miss"])`; `titles_recognizer.analyze(text="Mr. Schmidt", entities="TITLE")` | MATCH for Rule and In. **The page shows no output**, so the Result row is not from the docs (R3). |
| 13 | NRIC not masked by any default US pattern (rail 4 illustration) | raw `us_driver_license_recognizer.py`, `us_passport_recognizer.py`, `us_itin_recognizer.py` @2.2.364 | no alternative matches letter + 7 digits + letter under `\b` boundaries | MATCH (supports the hedged expectation) |
| 14 | NeMo diagrams 4 and 5 are Presidio masking on output and retrieval | `nemo-rails-explained.html` h3 | "4. Personal-data masking on output", "5. Personal-data masking on retrieved passages" | MATCH |

Tally: 14 checked, 14 MATCH, 0 MISMATCH, 0 UNVERIFIABLE. Item 12 supports required fix R3.

## Checklist (README section 11)

| Item | Result |
|---|---|
| Lines 6-109 identical to Sentinel; extra CSS only in a final Additions block; line 5 rewritten | PASS. The line 5 comment lists this page's section order. |
| Fragment format (title, preconnect, fonts link, style, `.wrap`); no doctype, lang, viewport, JS, images | PASS |
| Title "How Presidio Masks a Conversation"; h1 in sentence case; eyebrow "<Vendor> <Product> · <status>" | PASS. The eyebrow is "Data Privacy Stack Presidio · release 2.2.364, created at Microsoft", consistent with R016. |
| Legend lists exactly the roles used | PASS: gate, dev, pass (diagram 3), edit, part, na. No stop box is used and none is listed. |
| `dev` only where the product does not act | PASS: Your app decides / keeps the key / holds the key / Your pattern. |
| Every SVG has viewBox, role, full-sentence aria-label; no fill, stroke, style, width or height attributes | PASS (12 SVGs) |
| Marker ids unique; all `url(#)` resolve; none unused | PASS: o-a, a2, a3/a3o, a4/a4e … a10/a10e |
| Section order; NeMo stage numbers; sequential h3; "diagram N" references | PASS. Stages 1, 2, 2b, 3 and 5 appear; Dialog is skipped because it is not served. h3 1-10 are sequential and the unnumbered table rails are allowed. The references to diagrams 3, 4 and 5 and NeMo diagrams 4 and 5 are correct. |
| Scorecard: five checkpoints in NeMo order plus extras, pill and Why matching stages | PASS. See O1 on the output versus retrieval rationale. |
| `ul.limits` 6-8 items with bold leads, stock gap phrases | PASS on form (8 items). Wording fixes are R5, R6 and R7. |
| Every claim traces to the drafts; numbers attributed as plain ratios; examples labelled | **FAIL until R1-R3 are fixed**: positioning lacks the comparison; two examples are unlabelled. |
| Voice: British spelling, "AI model", "personal data", glosses, identifiers placement | PASS. "LLM" appears only inside the product name "LiteLLM"; no "PII" in text. "Regex" in the scorecard is glossed earlier in rail 8 ("regular expression"). |
| Footer sources mirror the drafts' official URLs | PASS for URLs; R8 for wording. |
| Renders light and dark at 1280 and 375; no clipped box text | PASS. 4 renders, plus 24 per-figure crops. Fragment and doctype-wrapped modes are both checked. No console errors. Body backgrounds are rgb(246,247,249) in light and rgb(18,22,31) in dark. The automated bbox check finds 0 tight or clipped texts. Dashes and amber tints are visible in dark. |
| No horizontal page overflow at 375 | PASS (375 = 375) because of the local addition. |
| Sibling look to Sentinel | PASS. Fork coordinates in diagram 3 follow the reference fork; the red branch is deliberately grey because Presidio never stops anything. |

## Required fixes

**R1. Positioning section: compare with NeMo, Llama Guard and Sentinel (lines 211-213 and 264-277).**

Problem: README section 9 requires the comparison against Sentinel and Llama Guard in the positioning table. The current table has a single Presidio column.

1. Line 211: replace `<div class="eyebrow">Presidio and NeMo</div>` with:
   `<div class="eyebrow">Presidio, NeMo, Llama Guard and Sentinel</div>`
2. Line 213: replace the `<p>` with:
   `<p>The four tools sit at different levels. NeMo is a framework you run that decides where checks go. Llama Guard is one model you run that gives a verdict. Sentinel is a web service run by GovTech that gives a score for each check. Presidio is a toolkit you run that finds personal data and, if asked, edits it; it never decides whether a message is safe. NeMo Guardrails calls Presidio for its personal-data checks.</p>`
3. Lines 264-277: replace the second `tablewrap` table with the one below. The NeMo, Llama Guard and Sentinel cells are verbatim from `sentinel-explained.html` lines 263-273. The Presidio cells reuse the current page wording plus PD6 and the languages facts.

```html
    <div class="tablewrap">
      <table class="cats">
        <thead><tr><th></th><th>NeMo Guardrails</th><th>Llama Guard</th><th>GovTech Sentinel</th><th>Presidio</th></tr></thead>
        <tbody>
          <tr><td>What it is</td><td>A framework around your chatbot</td><td>One AI model</td><td>A web service with a menu of checks</td><td>An open-source toolkit of four parts that find and edit personal data</td></tr>
          <tr><td>Who runs it</td><td>You</td><td>You</td><td>GovTech (hosted); some models can be self-hosted</td><td>You. The FAQ says it "is not an official product of any company and comes with no warranty or SLA" (a promised service level).</td></tr>
          <tr><td>What it hands back</td><td>Allow or block</td><td>Safe or unsafe, plus a category</td><td>A score from 0 to 1 per check</td><td>Findings with scores, or edited text, images and tables. Never a pass or fail.</td></tr>
          <tr><td>Decides where checks run</td><td>Yes</td><td>No</td><td>No, your app chooses what text to send</td><td>No. Your app chooses which text, image or table to send.</td></tr>
          <tr><td>Your own rules and fixed replies</td><td>Yes</td><td>No</td><td>No</td><td>Your own patterns and word lists for what to find; no fixed replies</td></tr>
          <tr><td>Edits text</td><td>Masks personal data</td><td>No</td><td>Returns a masked copy (personal data, via AWS)</td><td>Yes, through the Anonymizer: swap, remove, mask, hash, encrypt and more</td></tr>
          <tr><td>Singapore languages</td><td>Depends on the model it calls</td><td>Listed languages do not include Chinese, Malay or Tamil</td><td>LionGuard: Singlish, Chinese, Malay, partial Tamil</td><td>English by default. Other languages need changes to the language model and the detectors (called recognisers); no accuracy is published for any non-English one.</td></tr>
          <tr><td>Who can use it</td><td>Anyone (open source)</td><td>Anyone who accepts Meta's licence</td><td>Singapore Government public officers, closed beta</td><td>Anyone: open source under the MIT licence (a common open-source licence), which the project says will stay</td></tr>
        </tbody>
      </table>
    </div>
```

The current "Who made it" row is dropped because the sibling tables have no such row. The ownership facts stay in the lede and in limits item 7. The current page's FAQ and MIT wording moves into the Presidio column.

**R2. Rail 5 example is unlabelled (line 520).**

Problem: an invented output is shown with no "(illustrative)" mark. Rail 3 and rail 4 mark theirs, so the page is inconsistent with README section 5.

Replace `<dt>Shown</dt><dd>You can reach <mark>&lt;PERSON&gt;</mark> at <mark>&lt;EMAIL_ADDRESS&gt;</mark>.</dd>` with:
`<dt>Shown</dt><dd>You can reach <mark>&lt;PERSON&gt;</mark> at <mark>&lt;EMAIL_ADDRESS&gt;</mark>. (illustrative)</dd>`

**R3. Rail 8 Result row reads as quoted from docs, but the docs show no output (line 670).**

Problem: the Rule row is marked "(Presidio's docs)". The adding-recognizers page shows the call `titles_recognizer.analyze(text="Mr. Schmidt", entities="TITLE")` but no result (checked at source). The result is an inference from `deny_list_score=1.0` (PD6 R4).

Replace `<dt>Result</dt><dd>TITLE found at "Mr.", score 1.0 (the word-list default)</dd>` with:
`<dt>Result</dt><dd>TITLE found at "Mr.", score 1.0, the word-list default (illustrative: the docs show the call, not its output)</dd>`

**R4. NRIC/FIN gloss is inaccurate for FIN (line 364).**

Problem: FIN (Foreign Identification Number) is issued to foreigners, so it is not a national ID number.

Replace `The NRIC and FIN pattern (Singapore's national ID numbers) is switched off in the default file.` with:
`The NRIC and FIN pattern (Singapore's identity card numbers and foreign identification numbers) is switched off in the default file.`

**R5. Limits item 4 says no speed figures are published; the drafts record one (line 789).**

Problem: notebook 4 prints "Wall time: 5.84 s" for 1500 samples, with hardware and version not stated (PD1 R5, PD1 R8: "one unlabelled notebook timing only"). Also, "no recommended cut-off" should be scoped to the default setup, because the German recipe advises 0.4-0.5 (PD1 R5).

Replace `No per-type accuracy, no non-English accuracy, no recommended cut-off and no speed figures are published.` with:
`No per-type accuracy, no non-English accuracy and no recommended cut-off for the default setup are published, and the only speed figure is one notebook timing with the hardware not stated.`

**R6. Limits item 5 bold lead over-claims (line 790).**

Problem: the drafts document no built-in authentication (FAQ). TLS, rate limits and request size are [Not disclosed], not documented as absent, so "no built-in security" goes beyond the source.

Replace `<b>The web services have no built-in security.</b>` with:
`<b>The web services have no built-in login.</b>`

**R7. Limits item 7: a causal claim that the drafts do not support (line 792).**

Problem: "so the docs and the code differ" makes the 2026-07-04 publication the cause. The drafts mark that only as "a likely reason" [Inferred]. The example given, the web API file omitting options, is also true of `docs/api-docs/api-docs.yml` at the 2.2.364 tag itself (PD1 R6, PD6 R6), so it is not caused by the publication lag.

Replace `The live docs were last published on 2026-07-04, before release 2.2.364, so the docs and the code differ in places (for example, the web API file omits options the code accepts), and the older Microsoft container images are no longer updated.` with:
`The live docs were last published on 2026-07-04, before release 2.2.364, and the docs and the code differ in places (for example, the web API description omits options the code accepts, and one docs example names an edit differently from the code). The older Microsoft container images are no longer updated.`

(The second example is the AHDS "surrogate" versus "surrogate_ahds" naming, PD2 R2.)

**R8. Footer says NVIDIA's page is used "for the NeMo link only" (line 799).**

Problem: the page also states an NVIDIA-sourced fact in rail 9 and in the scorecard ("NVIDIA's NeMo docs do run Presidio on retrieved chunks"), and the positioning SVG's three NeMo boxes come from the same source.

Replace `and NVIDIA's NeMo Guardrails page on Presidio (for the NeMo link only).` with:
`and NVIDIA's NeMo Guardrails page on Presidio (for how NeMo uses Presidio).`

## Optional suggestions

- **O1.** Scorecard and overview: Output is "Yes" while Retrieval is "Partly", yet both Why cells give the same reason ("no Presidio page shows it" / "Presidio's pages show no example"). A careful reader will see the inconsistency. Either give retrieval a distinct reason, or state the pill logic once. For example, the retrieval Why could add: "Presidio has nothing that handles fetched documents; your app must send each passage." The pill choice itself is a judgement for main.
- **O2.** Limits item 4, "The only figures are the vendor's demo notebooks on made-up data": the DICOM demo in rail 7 uses four sample files, not made-up text. Consider "The only text-detection figures are ...".
- **O3.** Rail 9 Good to know, "That is our reading of the code for Presidio itself; we have not tested it yet.": the referent is unclear. Suggest: "That Presidio's own steps work on passages is our reading of the code; we have not tested it yet."
- **O4.** Rail 9 figcaption, "The AI model cannot repeat personal data it was never shown.": add "... and anything the Analyzer misses still reaches it."
- **O5.** Rail 6: a useful caveat from PD3 R2 and R5 is missing. Encrypting the same name twice gives two different tokens (random starting value), so the AI model cannot tell that two tokens are the same person. This fits in the Good to know.
- **O6.** Positioning "Languages" cell, "the name model": the NLP engine does tokens, lemmas and named entities. "the language model" or "the language-processing model" is closer.
- **O7.** UEN gloss: "(a registration number for Singapore businesses and other organisations)" is slightly more exact. The current gloss is acceptable.
- **O8.** Rail 4 Masked label: for consistency with README section 5, consider "(illustrative: what we expect from a default setup; not tested)".
- **O9.** "Azure Health Data Services" appears in the Anonymizer table without a gloss. Consider "(a Microsoft cloud service)".

## QUESTIONS

1. (User, already flagged by main.) The `min-width: 0` overflow fix is local to this page. Sentinel, Llama Guard, NeMo and SDP all overflow to 628 px at 375. Should it go into the shared base for all pages at once (README section 2 and section 3 forbid per-page base edits)?
2. (Main.) For R1, may the positioning tables of new pages reuse the verified sibling pages' NeMo, Llama Guard and Sentinel cells verbatim, as SDP and Sentinel do? If yes, a one-line note in README section 10 would stop future diagrammers reading section 10 as forbidding it.
