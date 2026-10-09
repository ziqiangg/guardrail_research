# lionguard P10 diagram review: benchtest/diagrams/lionguard-explained.html (commit 32f872d)

- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-10.
- Sources of truth: benchtest/drafts/lionguard_two_level.md (LN1) and benchtest/drafts/lionguard_inventory_final.md. Change log read for the "open" wording (lionguard_changes.md line 36, T49/T6).
- Rulings read: R005, R026, R027, R028, R031, R032, R033.
- Renders: benchtest/scratchpad/verifier/lionguard_diagram/lionguard_{light,dark}_{1280,375}.png, plus per-figure and per-table crops fig0-6 and table0-4 in light and dark (all PNGs gitignored by `benchtest/scratchpad/**/*.png`). Scripts: render.py, figs.py in the same folder.
- URL results: benchtest/scratchpad/verifier/lionguard_diagram/url_check.txt.
- Source spot-checks used the cached official page text in benchtest/scratchpad/verifier/lionguard/pages/ (read 2026-10-09 by the P7 verifier with fetch_text.py).

## Verdict: PASS WITH FIXES (6 required fixes)

The page is structurally clean. The shared CSS is byte-identical, the sibling cells are word for word, the SVGs and markers are clean, it renders in both themes, and there is no overflow at 375. Almost every claim traces to the drafts.

Six fixes remain. Each is one string or a few strings:
- RF1: "open" survives in the eyebrow and in diagram 3, although the merge removed it.
- RF2: the lede states an [Inferred] data flow flatly and runs to five sentences.
- RF3: F1 is not glossed at its first use.
- RF4: limits item 4 misdescribes the 2.1 evaluation.
- RF5: the "not directly comparable" claim is the drafts' [Inferred], stated flatly, and the blog's own wording undercuts it.
- RF6: diagram 3 says "first for Sentinel users", which misreads the 21 Aug 2026 blog.

## 1. Required fixes

**RF1. Eyebrow (line 126) and diagram 3 (lines 424, 431): "open" survives although the merge removed it.**
- Problem: lionguard_changes.md line 36 records that the R1 Summary dropped "open Hugging Face weights" because "'open' depends on the unresolved licence reading T6". R033 keeps the licence relation as an open R8 question.
- The eyebrow states "open models" in the page's own voice, without attribution. Diagram 3 says "Open data" for the dataset box, which has the same LICENSE (inventory (d): license_name govtech-singapore, same md5).
- Precedent: the Llama Guard eyebrow lists models only.
- Replace (line 126):
  `GovTech LionGuard · open models: LionGuard 2, 2.1 and 2 Lite`
- With:
  `GovTech LionGuard · LionGuard 2, 2.1 and 2 Lite on Hugging Face`
- Replace (line 431):
  `<text class="tb" x="612" y="44" text-anchor="middle">Open data</text>`
- With:
  `<text class="tb" x="612" y="44" text-anchor="middle">Public data</text>`
- Replace (line 424, inside the aria-label):
  `and open data, meaning a training-data subset and a public test set`
- With:
  `and public data, meaning a training-data subset and a public test set`
- "Public" is documented: the inventory (d) rows say "Not gated".
- Limits item 8, "Updates and code are not fully open", is about code availability rather than the licence. It can stay.

**RF2. Lede (line 128): the [Inferred] data flow is stated flatly, and the lede has 5 sentences (README section 2 allows 2 to 4).**
- Problem: the drafts label "each text to be classified is sent to OpenAI / to Google to be embedded" as [Inferred]: R7 lines 189-190, and inventory (a) "Embedder hosting and access".
- The page hedges this claim correctly in the "Which LionGuard" table ("our reading of the code") and in the rail 3 Good to know ("That is our reading of GovTech's code; we have not tested it yet"). The lede does not hedge it.
- The lede also keeps "and you run it yourself", the phrase that T49 removed from R1 because 2 and 2.1 embed through a hosted service.
- Replace the whole lede text:
  `LionGuard is a small scoring model from Singapore's GovTech that looks for harmful content in English, Singlish, Chinese, Malay and Tamil. GovTech publishes it on Hugging Face, a public site for sharing AI models, and you run it yourself. Only the small classifier is GovTech's: LionGuard 2 and 2.1 send each text to OpenAI or Google Gemini to be turned into numbers first, and only Lite does that step on your own machine. For each text your app gets back a probability from 0 to 1 for every harm category, with no verdict and no cut-off supplied. This page shows how that works, where it fits in a chat, and what it leaves to your app.`
- With:
  `LionGuard is a small scoring model from Singapore's GovTech that looks for harmful content in English, Singlish, Chinese, Malay and Tamil. GovTech publishes it on Hugging Face, a public site for sharing AI models, for you to run, but only the small classifier is GovTech's: by our reading of GovTech's code, LionGuard 2 and 2.1 send each text to OpenAI or Google Gemini to be turned into numbers first, and only Lite does that step on your own machine. For each text your app gets back a probability from 0 to 1 for every harm category, with no verdict and no cut-off supplied. This page shows how that works, where it fits in a chat, and what it leaves to your app.`

**RF3. "Which LionGuard" table (line 400): first use of F1 is not glossed.**
- Problem: README section 9 says "gloss every term on first use".
- The first F1 on the page is in this cell. The gloss "F1, a 0 to 100 accuracy measure" appears only later, at line 525 and in the line 590 tag.
- Replace:
  `<td>Paper: F1 of 77 on GovTech's own test set</td>`
- With:
  `<td>Paper: F1 (a 0 to 100 accuracy measure) of 77 on GovTech's own test set</td>`
- The later gloss at line 525 can then stay or be shortened to "scored 77 (F1)". Either is fine.

**RF4. Limits item 4 (line 640): the 2.1 evaluation is misdescribed, and the missing-speed claim is too narrow.**
- Problem 1: the page says 2.1 "has one blog table on a private test split".
- The drafts (R5 line 142) quote the blog: it evaluated "on a held-out private LionGuard test split and RabakBench".
- The page's own languages table shows the four 2.1 RabakBench figures from that blog. Source check, B3: "a held-out private LionGuard test split and RabakBench". Result: MISMATCH for the page.
- Problem 2: R6 line 173 lists latency as [Not disclosed] for both 2.1 and Lite, not only Lite.
- Replace:
  `LionGuard 2 has a paper; 2.1 has one blog table on a private test split; Lite has no figure. No operating threshold, maximum text length or Lite speed is stated.`
- With:
  `LionGuard 2 has a paper; 2.1 has one blog table, on a private test split and RabakBench; Lite has no figure. No operating threshold, maximum text length, or speed for 2.1 or Lite is stated.`

**RF5. Languages table (line 596): "so not directly comparable with 77" states an [Inferred] claim that the source appears to undercut.**
- Problem: the claim comes from R5 line 143, which is [Inferred]. Its premise is that the blog's split is private and that the paper does not say its internal test set is released.
- That premise is equally consistent with the two being the same set. The blog (B3) says it used "the same benchmarks used in our earlier LionGuard experiments: a held-out private LionGuard test split". It labels the row "Original test" and later calls it "our private LionGuard 2 Test dataset" and "the original LionGuard 2 Test set".
- The page should not assert either reading. It should quote the blog and stay neutral. See QUESTION Q1 for the draft bullet.
- Replace:
  `<td>73 (a private split, so not directly comparable with 77)</td>`
- With:
  `<td>73 (on what the blog calls a held-out private test split)</td>`
- The "Which LionGuard" cell, "Blog: F1 of 73 on a private GovTech test split", is already neutral and can stay.

**RF6. Diagram 3, Planned row (lines 424, 468): "first for Sentinel users" misreads the blog.**
- Problem: B2 says "we'll be rolling out the first retrained LionGuard 2 model". Here "first" means the first of the retrained models. B2 also says access to retrained models is "currently only available to Sentinel users within the Singapore Government" (R4 line 104).
- "First for Sentinel users" reads as "Sentinel users first, everyone later", which the drafts mark [Not disclosed] (R4 line 107). Source check, B2 lines 85 and 88: MISMATCH for the page wording.
- Replace (line 468):
  `<text class="ts" x="327" y="343" text-anchor="middle">first for Sentinel users</text>`
- With:
  `<text class="ts" x="327" y="343" text-anchor="middle">for Sentinel users only</text>`
- Replace (line 424, inside the aria-label):
  `Planned: a retrained LionGuard 2 for Sentinel users first, with no statement`
- With:
  `Planned: a retrained LionGuard 2 for Sentinel users only, with no statement`
- Limits item 8, "announced for Sentinel users with no word on a public release", is already correct.

## 2. Optional suggestions

- **O1. Diagram 2, LionGuard box (line 330): "a file of about 3 MB" is true for 2 and 2.1 only.**
  - Lite's classifier is 1,039,200 bytes (R4 line 67), and the "Which LionGuard" Good to know says so.
  - Suggest `a file of 1 to 3 MB`.
- **O2. Rail 4 figcaption (line 518): "The scoring is the same for every language it covers" can be read as "equally accurate".**
  - The page later says Tamil is the weakest.
  - Suggest `One model scores every language it covers: English, Singlish, Chinese, Malay and Tamil, though less well in Tamil.`
- **O3. Overview figcaption (line 212): the first use of "embedding step" is not glossed.**
  - The gloss "a kind of fingerprint of its meaning" comes at line 297. The lede explains the idea ("turned into numbers") but never names it.
  - Suggest `after an embedding step (turning the text into numbers) that another company runs`.
- **O4. Positioning table, LionGuard "Who can use it" (line 284): the paper's research-only wording is missing.**
  - The cell is neutral ("under a GovTech licence text"), and limits item 3 covers the point.
  - Optional addition: `; the paper says the weights are for research and public interest purposes only`.
- **O5. "Which LionGuard" Lite row (line 402): "no API key" is jargon (README section 9). Elsewhere the page says "your own key".**
  - Suggest `no key needed`. The vendor quote "no external API calls" can stay as a quote.
- **O6. Score scale (lines 346, 364): the demo bands apply to the overall (binary) score only (R5 line 123), and the page does not say so.**
  - Suggest adding "on the overall flag" to the aria-label and the figcaption: "These bands, applied to the overall flag, come from ...".
- **O7. Languages Good to know (line 604) has 4 sentences. README section 5 says a maximum of about 3.**
  - The RabakBench gloss could move into the tag line.
- **O8. Languages table, "Singlish (RabakBench)" row: the 2.1 blog row is "RabakBench English/Singlish".**
  - Optional row label: `Singlish (RabakBench; the blog says English/Singlish)`.
- **O9. Rail 2 know (line 366): "8,192 tokens" adds a unit.**
  - The OpenAI table reads only "Max input | 8192", and the drafts write "max input of 8192".
  - The unit is plausible: the same page prices "per input token", and Google states "2048 tokens" explicitly. Leave as is, or write "8,192 (OpenAI) and 2,048 tokens (Google)".
- **O10. Rail 2 figcaption (line 343): "The first step is the only part that differs between versions" is GovTech's playbook claim ("differ only in the embedding model").**
  - The classifier weights and sizes also differ.
  - Suggest attributing it: `GovTech says the versions differ only in the first step, which is not GovTech's work (diagram 3).`

## 3. Points main asked to judge

**1. Eyebrow "open models": yes, "open" should go (RF1).**
- The merge removed "open" from R1 for exactly this reason (T49, T6).
- The drafts keep "open-sourced" only as attributed quotes: the playbook at R1 line 8 and R4 line 89, and B1 at R1 line 16.
- The eyebrow is the page's own voice, and README section 2 asks for a version or status there.
- Proposed text: `GovTech LionGuard · LionGuard 2, 2.1 and 2 Lite on Hugging Face`. This mirrors the Llama Guard eyebrow, which lists the models.
- Alternative if main prefers a status word: `GovTech LionGuard · published models: LionGuard 2, 2.1 and 2 Lite`.
- Apply the same reasoning to "Open data" in diagram 3, which becomes "Public data".

**2. Required statements: all present. One hedge is missing (RF2).**

| Statement | Where on the page | Hedge as in the drafts? |
|---|---|---|
| 2 and 2.1 send text to OpenAI or Gemini for embedding | lede; positioning row "Who runs it"; "Which LionGuard" table; diagram 3 and its Good to know; limits item 2 | Table and diagram 3 Good to know say "our reading of the code" (matches [Inferred]). The lede is unhedged (RF2). "Who runs it" and limits item 2 say only that OpenAI or Google run, or are depended on for, the embedding step, which is [Documented] (README "users to input their own ... API key"). |
| Lite embeds locally; Hugging Face login and Gemma terms | lede; positioning "Who can use it"; "Which LionGuard"; diagram 3 Google row; limits item 2 | Yes. "runs fully locally, with no external API calls" is quoted from the card. The login and gate follow R7 lines 182-184 [Documented, owner's page]. |
| Probabilities only, no shipped threshold | lede; diagram 2 ("no cut-off built in"); score scale caption; diagram 3 "Cut-off: none ships with it"; limits item 1 ("no official cut-off") | Yes (R5 line 120 [Documented]; R5 line 121 [Not disclosed]). The demo bands are called demo behaviour (R5 line 127). |
| Licence texts' relation not stated | limits item 3; positioning "under a GovTech licence text" | Yes. The bold lead is "how they relate is not stated" (R4 line 103 [Not disclosed]). The MIT, Singapore-law, arbitration and marks wording matches the LICENSE (source check MATCH). The paper quote is verbatim. |
| Embedder terms for test text | diagram 3 Good to know; limits item 2 ("still to be verified") | Yes (R8 line 222 open question; R031 and R033). |

**3. F1 numbers and language order: exact after rounding. One flat inference (RF5).**
- LionGuard 2 (paper Table 1, column order SS, ZH, MS, TA): 77.0, 88.1, 87.8, 78.4, 66.6. The page shows 77, 88, 88, 78, 67. MATCH, verified at source: P2 line 173 ff.
- LionGuard 2.1 (B3): 0.7318, 0.8618 (English/Singlish), 0.8420 (Malay), 0.7267 (Tamil), 0.8688 (Chinese). The page shows 73, 86, 84, 73, 87, and the rows map correctly (Malay 84, Chinese 87). MATCH, verified at source.
- Table 1 vs Table 3 handling:
  - The page says "The paper prints Chinese and Malay in a different order in two tables; this page follows the order that matches GovTech's blog."
  - This matches R5 lines 128-130: Table 1 order, which B1's "Chinese (88%) and Malay (78%)" matches.
  - The page does not assert which table is wrong, so it does not overstate the drafts' [Inferred] line 132. Correct.
- Rail 4 comparators: OpenAI Moderation 54.7 → 55 and LlamaGuard 4 12B 26.5 → 27 (half-up). Both MATCH at P2 Table 3.
- All are attributed: "GovTech's own results, not ours".
- RF5 neutralises the comparability claim.

**4. Scorecard: confirmed.**
- Input Yes, Output Yes: R3 [Documented]: paper section 3 "input filter ... output filter", and B1 heading.
- Retrieval No: per R026. Retrieval is "Partly" only if a document, file or retrieval input is documented. The drafts give retrieved text only as [Inferred] (R3 line 51), so "No" is correct. The Why wording mirrors Sentinel's.
- Dialog No and Execution No: no topic, reply or tool features in any draft. The Why for Execution uses the stock phrase "Nothing official describes".
- Rows are in NeMo order. Each pill matches its stage section, and no Retrieval, Dialog or Execution sections are drawn.

**5. URLs: 18 of 18 return 200, with no redirects.**
- All 18 footer URLs appear verbatim in the drafts (R9 or inventory Source URL cells).
- Not requested: fonts.googleapis.com, and every API host. No API host appears on the page.
- The internal links nemo-rails-explained.html, llama-guard-explained.html and sentinel-explained.html exist in benchtest/diagrams/.

## 4. Checklist (README section 11)

| Item | Result |
|---|---|
| `diff` of lines 6-110 against sentinel-explained.html prints nothing; extra CSS only in a final "Additions for this page" block; line 5 rewritten | PASS. The diff is empty. Lines 111-120 hold one Additions block: the allowed link-colour line `.stage-head a, .know a { color: var(--accent); }` plus `.mk-gov/.mk-emb/.mk-nd/.mk-plan/.bar-*/.tick`, all `var(--token)` only. Line 5 lists this page's order. |
| Fragment format | PASS. title, preconnect, fonts link, style, `.wrap`; no doctype, html, head, body, meta, script or img. |
| Title, h1, eyebrow | Title and h1 PASS. Eyebrow: see RF1. |
| Legend lists exactly the roles used | PASS. gate, dev, pass, stop and na are all used. No edit or part role is used: the amber "warn" band is a scale band, as on Sentinel. The `.mk-*` boxes are explained in the rail 3 tag ("dashed boxes mean not disclosed or not yet available"), as on Sentinel line 359. |
| `dev` only on app-owned boxes | PASS. 2× `gate dev` (Your app, overview) and 2× `no dev` (refusal, discard). |
| SVG viewBox, role and aria-label; no fill, stroke, style, width or height attributes | PASS. 7 SVGs; 0 offending attributes; each fork's aria-label names both branches. |
| Marker ids | PASS. o-a, a2, a4, a4o, a4n, a5, a5o, a5n: unique, all resolve, none unused. |
| Section order, stage numbers, h3 numbering, "diagram N" references | PASS. Header, overview, positioning, how it works, behind the model, Stage 1, Stage 2, then the extra "Input and output · Languages and accuracy", scorecard, limits, footer. h3 runs 1-5 plus unnumbered table rails. "diagram 3" points to parts and makers; "diagram 5" points to output. |
| Scorecard | PASS (see point 4). |
| Limits: 6-8 items with bold leads | PASS. 8 items; stock phrases used ("is not stated", "still to be verified"). Content fix in RF4. |
| Every claim traces to the drafts; vendor numbers attributed; examples labelled | FAIL until RF2, RF4, RF5 and RF6 are applied. The examples are marked "(illustrative)" and "no real values shown". |
| Voice | Mostly PASS. British spelling (0 American forms found by scan); "AI model" and "personal data" used. F1 gloss: RF3. "API key": O5. |
| Footer | PASS. Sources paragraph and link list; every URL is in the drafts; "Accuracy figures are GovTech's own reported results"; examples illustrative. |
| Renders light and dark at 1280 and 375 | PASS. Fonts loaded. Automated check: 0 box-text overflows and 0 text outside the viewBox. Visual check of all 7 figures and 5 tables in light and dark: dashes, tints and the score bars are visible in dark. |
| No horizontal page overflow (R028) | PASS. scrollWidth equals innerWidth at 375 (375 = 375) and at 1280 in both themes; no element extends past the viewport outside figure or .tablewrap. |
| Sibling look; sibling cells (R027) | PASS. All 8 positioning rows: the NeMo, Llama Guard and Sentinel cells are identical to sentinel-explained.html lines 266-273 (script compare). Diagram 1's first three columns are byte-identical to sdp-explained.html's reviewed four-column zone diagram; only the LionGuard column differs. The figcaption's "Only NeMo acts on a result" is Sentinel's own wording. |
| R032 (bench content as proposals) | PASS. The only bench wording is "a bench could pin a revision" (limits item 8). |
| R005 (no Sentinel-service duplication) | PASS. Sentinel appears only as a cross-reference: same three versions served; one spelling conflict from R4 line 109. No hosted ids, token limits or endpoints. |

## 5. Source spot-checks (cached official pages, read 2026-10-09)

| # | Claim on page | Source (URL) and quote | Result |
|---|---|---|---|
| 1 | LionGuard 2 F1: 77, 88, 88, 78, 67 | arxiv.org/html/2507.15339 Table 1: "Test, RabakBench SS, ZH, MS, TA ... text-embedding-3-large ... 77.0, 88.1, 87.8, 78.4, 66.6" | MATCH |
| 2 | LionGuard 2.1 F1: 73, 86, 87, 84, 73 | blog.ai.gov.sg/decision-models-...: "Original test 0.7318; RabakBench English/Singlish 0.8618; Malay 0.8420; Tamil 0.7267; Chinese 0.8688" | MATCH |
| 3 | Limits item 4: "2.1 has one blog table on a private test split" | same blog: "a held-out private LionGuard test split and RabakBench" | MISMATCH (RF4) |
| 4 | "a private split, so not directly comparable with 77" | same blog: "the same benchmarks used in our earlier LionGuard experiments"; "our private LionGuard 2 Test dataset" | UNVERIFIABLE; the source leans the other way (RF5, Q1) |
| 5 | 55 for OpenAI's moderation tool, 27 for Llama Guard 4 | P2 Table 3: "54.7" and "26.5" | MATCH (rounded) |
| 6 | Retrained model "first for Sentinel users" | blog guardrails-in-the-wild: "we'll be rolling out the first retrained LionGuard 2 model"; "currently only available to Sentinel users within the Singapore Government" | MISMATCH in meaning (RF6) |
| 7 | Playbook: "differ only in ... embedding"; 2.1 "for best performance"; Lite "for local deployment" | govtech-responsibleai.github.io/playbook/tools/lionguard/: "differ only in the embedding model they use ... For best performance, we recommend LionGuard 2.1. For local deployment, we recommend LionGuard 2 Lite." | MATCH |
| 8 | Level 2 implies Level 1 | playbook: "If a Level 2 instance is detected, Level 1 is also flagged by design." | MATCH |
| 9 | Lite "runs fully locally, with no external API calls" | huggingface.co/govtech/lionguard-2-lite README: "LionGuard 2 Lite runs fully locally, with no external API calls." | MATCH |
| 10 | Paper: a "bidirectional filter" | P2 Figure 2: "LionGuard 2 working as a bidirectional filter around an LLM Chatbot" | MATCH |
| 11 | Weights "exclusively for research and public interest purposes only" | P2 Ethical Considerations: identical wording | MATCH |
| 12 | About 4 in 100 examples show the flag and the categories disagreeing | P2 section 7.2: "About 4% of examples ... show disagreement between the binary head and category heads" | MATCH |
| 13 | Little to no Chinese, Malay or Tamil-only training data | P2: "our training data contained little to no Chinese/Malay/Tamil-only examples" | MATCH |
| 14 | The paper calls Tamil "moderate"; human oversight in high-stakes settings | P2: "its Tamil performance remains moderate"; "we recommend combining LionGuard 2 with human oversight in high-stakes settings" | MATCH |
| 15 | Training texts 20,333 of 26,207; 2,098 synthetic | P2 section 4.1.4: "26,207 unique texts: 20,333 online comments, 2,098 synthetically augmented comments" | MATCH |
| 16 | Category descriptions (9 cells) | lionguard-2 README taxonomy, for example "Derogatory or generalized negative statements targeting a protected group."; "Descriptions of ongoing or imminent self-harm behavior." | MATCH (faithful paraphrase, British spelling) |
| 17 | Demo bands 0.40 and 0.70 | lionguard-demo services.py: "if binary_score < 0.4: ... elif 0.4 <= binary_score < 0.7:" | MATCH |
| 18 | LICENSE: MIT subject to conditions, Singapore law, arbitration, marks excluded | lionguard-2 LICENSE: "provided under the MIT License SUBJECT FURTHER TO THE FOLLOWING"; "governed by the laws of Singapore"; "arbitration administered by the Singapore International Arbitration Centre" | MATCH |
| 19 | 8,192 tokens (OpenAI) and 2,048 (Google) | developers.openai.com embeddings: "Max input ... text-embedding-3-large ... 8192"; EmbeddingGemma: "Maximum input context length of 2048 tokens"; gemini-embedding-001 page: "2,048" | MATCH (the OpenAI unit is implicit, O9) |
| 20 | About 300 tokens a second on one CPU | P2 section 3: "giving an end-to-end throughput of ≈300 tokens/s" | MATCH |

Tally: 16 MATCH, 3 MISMATCH (RF4, RF6, and RF5's direction), 1 UNVERIFIABLE (#4, raised as Q1).

## 6. QUESTIONS

- **Q1 (route to gr-merger or gr-resolver; draft content, not the page):**
  - The issue: LN1 R5 line 143 says, as [Inferred], that the 2.1 figure "cannot be compared directly with the paper's 77.0". Its premise is that the blog's split is private and that the paper does not say its internal set is released.
  - Why it may be wrong: the 28 Sep 2026 blog says it used "the same benchmarks used in our earlier LionGuard experiments: a held-out private LionGuard test split", and calls it "Original test" and "the original LionGuard 2 Test set". That suggests it may be the paper's own test set.
  - Request: should the bullet be reworded neutrally, for example "Whether the blog's private split is the paper's test set is not stated; if it is, LionGuard 2.1 scores below LionGuard 2's 77.0 on it [Not disclosed / Inferred]"?
  - RF5 makes the page neutral either way.
- **Q2 (main, eyebrow wording only):** RF1 proposes `LionGuard 2, 2.1 and 2 Lite on Hugging Face`. If main prefers a status word, the alternative is `published models: LionGuard 2, 2.1 and 2 Lite`. Neither uses "open".
