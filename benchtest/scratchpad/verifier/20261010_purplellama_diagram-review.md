# purplellama P10 diagram review: benchtest/diagrams/purplellama-explained.html (commit 25444c7)

- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-10.
- Sources of truth: benchtest/drafts/purplellama_two_level.md (PL1 to PL7), purplellama_inventory_final.md and purplellama_eval_tooling_final.md, as approved in R034.
- Rulings read: R004, R026, R027, R028, R030, R032, R034.
- Sibling text compared word for word: lionguard-explained.html, llama-guard-explained.html and sentinel-explained.html.
- Renders: benchtest/scratchpad/verifier/purplellama_diagram/purplellama_{light,dark}_{1280,375}.png, plus crops fig0 to fig13 and table0 to table6 in light and dark. All PNGs are gitignored by `benchtest/scratchpad/**/*.png`. Scripts: render.py and figs.py in the same folder.
- URL results: purplellama_diagram/url_results.txt and url_retry.txt.
- Verbatim source text for the spot-checks: purplellama_diagram/pages/ (fetched with fetch_text.py on 2026-10-10).

## Verdict: PASS WITH FIXES (8 required fixes)

The page is structurally clean:
- The shared CSS (lines 6-110) is byte-identical to Sentinel's.
- All 14 SVGs carry a viewBox, role="img" and a full aria-label. No SVG element has fill, stroke or style attributes.
- All 26 marker ids are unique, every one is referenced, and every reference resolves.
- The page renders in light and dark. At 1280 and 375, scrollWidth equals innerWidth, and no text sits outside its box.

Almost every number traces exactly to the drafts and is credited to Meta.

The eight fixes are each one string or a few strings. Two of them correct a misreading:
- RF1: the Retrieval row implies Meta assigns its PDF example to the hidden-text scanner. It does not.
- RF3: limits item 5 undercounts AlignmentCheck's published results.

The other six:
- RF2: the scorecard "Measuring" row contradicts itself.
- RF4: the Semgrep licence is called "an open question", though the drafts document it (LGPL 2.1).
- RF5: the Prompt Guard 1 licence cell omits Llama 3.
- RF6: one example credits Meta's test with something only the code shows.
- RF7: a "Good to know" promises an explanation that the page never gives.
- RF8: the Llama Guard rail caption paraphrases the sibling page instead of copying it.

## 1. Required fixes

**RF1. Scorecard, Retrieval row (line 1006): the PDF example is tied to the wrong scanner.**
- Problem: the cell joins two clauses with "and": "Meta's test attaches the hidden-text scanner to tool output, and its docs give an example of hidden text in a PDF". A reader takes Meta's PDF example as a case for the hidden-text scanner.
- What the source says: draft PL7 R2 (two_level line 1048) says the workflow page "maps it to PromptGuard and the Regex scanner, not to the Hidden ASCII scanner".
- Verified at source: workflow-and-detection-components.md, row "Indirect universal jailbreak prompt injections", cell "**PromptGuard** and **Regex scanner** detect jailbreak input".
- Old:
  `Meta documents <b>Prompt Guard 2</b> for untrusted content such as web data and tool output, and Meta's test attaches the hidden-text scanner to tool output, and its docs give an example of hidden text in a PDF. No document-store integration is described, and Meta does not evaluate retrieved passages separately.`
- New:
  `Meta documents <b>Prompt Guard 2</b> for untrusted content such as web data and tool output, and Meta's test attaches the hidden-text scanner to tool output. Meta's docs give an example of invisible text in a PDF, which they assign to the Prompt Guard and fixed-pattern scanners, not to the hidden-text scanner. No document-store integration is described, and Meta does not evaluate retrieved passages separately.`
- The Partly pill still holds under R026, because a documented untrusted web-data and PDF input exists.

**RF2. Scorecard, intro (line 998) and the "Measuring" row (line 1010): a "No" pill for a product that has a measuring tool.**
- Problem: the row is headed "Measuring" and the column asks "Purple Llama?". The pill says No, yet the cell names CyberSecEval, a Purple Llama measuring tool.
- Sibling precedent splits on what the row means:
  - Sentinel's extra row "Monitoring" is Yes for its refusal measure.
  - SDP's "Monitoring" row is No because SDP does not look at chat traffic.
- The intended meaning here is "nothing watches a live chat", so name the row for that.
- Old (line 998):
  `<p>The same five places NeMo can check, plus images and measuring, with an honest answer for each and the tool that covers it.</p>`
- New:
  `<p>The same five places NeMo can check, plus images and live monitoring, with an honest answer for each and the tool that covers it.</p>`
- Old (line 1010):
  `<tr><td>Measuring</td><td><span class="pill no">No</span></td><td><b>CyberSecEval</b> tests AI models before use and checks nothing in a live chat. It is not a barrier.</td></tr>`
- New:
  `<tr><td>Monitoring (live chats)</td><td><span class="pill no">No</span></td><td><b>CyberSecEval</b> tests AI models before use and checks nothing in a live chat; it is a measuring tool, not a barrier.</td></tr>`
- Acceptable alternative: keep "Measuring" and change the pill to `<span class="pill yes">Yes</span>`, with the cell text `<b>CyberSecEval</b> measures AI models before use; it checks nothing in a live chat and is not a barrier.`

**RF3. Limitations item 5 (line 1028): "AlignmentCheck has one benchmark" undercounts.**
- Problem: the drafts record two published AlignmentCheck results:
  - Meta's goal-hijacking benchmark: over 80% recall below 4% FPR.
  - AgentDojo: attack success 17.6% to 2.89%, utility 43.1%.
  Sources: PL3 R5, two_level lines 408-417; inventory (g) rows 121-122.
- Verified at source: arXiv 2505.03574 says "reduction in ASR to 2.89% - an 84% drop relative to baseline".
- Old:
  `Prompt Guard 2 and Code Shield have figures from Meta's private or small tests, and AlignmentCheck has one benchmark.`
- New:
  `Prompt Guard 2 and Code Shield have figures from Meta's private or small tests, and AlignmentCheck has results only from Meta's own benchmark and one agent test (AgentDojo).`

**RF4. Semgrep licence called "an open question" (lines 281, 837 and 1025), though the drafts document it.**
- Problem: PL6 R4 (two_level lines 931-932) and inventory (f) give the Semgrep licence as [Documented]: GNU LGPL 2.1, at v1.69.0 and at v1.180.0.
- What stays open (PL6 R8 line 999, R034) is whether that licence has consequences for a bench, not what the licence is.
- Old (line 281, Code Shield column, "Who can use it"):
  `Anyone: MIT-licensed; its Semgrep dependency has its own licence (an open question)`
- New:
  `Anyone: MIT-licensed; its Semgrep dependency has its own licence (LGPL 2.1), and what that means for a bench is an open question`
- Old (line 837, "Which Code Shield" Good to know, last sentence):
  `The Semgrep tool has its own licence terms, an open question.`
- New:
  `The Semgrep tool has its own licence (LGPL 2.1); whether it has consequences for a bench is an open question.`
- Old (line 1025, limits item 2, last clause):
  `and the licence of the Semgrep tool is an open question.`
- New:
  `and whether the Semgrep tool's own licence (LGPL 2.1) has consequences for a bench is an open question.`

**RF5. "What is in the box", Prompt Guard 1 licence cell (line 349): Llama 3 is missing.**
- Problem: inventory (f), row "Prompt Guard 1 (legacy)", records three licence versions:
  - Llama 3, in the folder README.
  - Llama 3.1, in the Hugging Face tag and gate page.
  - Llama 3.2, in the root README table and the root LICENSE.
- Verified at source: Prompt-Guard/README.md says "The same license as Llama 3 applies".
- Old:
  `<td>Llama 3.1 or 3.2 text; Meta's pages differ</td>`
- New:
  `<td>Llama 3, 3.1 or 3.2 text; Meta's pages differ</td>`

**RF6. Rail 8 example (line 727): "(as in Meta's test)" credits the test with the decoded sentence.**
- Problem: draft PL7 R5 (line 1075) says Meta's test asserts three things: a block, a score of at least 0.8, and "Hidden ASCII" in the reason.
- The decoded hidden sentence in the reason comes from the code (PL7 R1 line 1038), not from the test.
- Old:
  `<dt>Result</dt><dd>block · reason "Hidden ASCII:" followed by <mark>the decoded hidden sentence</mark> (as in Meta's test)</dd>`
- New:
  `<dt>Result</dt><dd>block · reason "Hidden ASCII:" followed by <mark>the decoded hidden sentence</mark> (our reading of the code; Meta's test checks the block and the "Hidden ASCII" label)</dd>`

**RF7. Rail 1 Good to know (line 285): "as the sections below say" covers LlamaFirewall, but no section below describes LlamaFirewall's PyPI differences.**
- Problem: only Code Shield's PyPI differences appear below, in the "Which Code Shield" table.
- What the drafts say about LlamaFirewall:
  - Inventory (a), row "llamafirewall package", line 12, [Inferred] from a file comparison: the 1.0.3 sdist differs from the pin in promptguard_utils.py, cli/configure.py and scanners/__init__.py.
  - The model-loader difference itself is [Documented] (PL2 R4 lines 227-229).
- Old:
  `LlamaFirewall's PyPI package (the public software index) and Code Shield's differ from that code in places, as the sections below say.`
- New:
  `Code Shield's PyPI package (the public software index) differs from that code in places, as its section below says; LlamaFirewall's PyPI package differs in three files, including how it fetches the Prompt Guard model.`

**RF8. Rail 12 figcaption (line 922): the Llama Guard text is paraphrased, not copied.**
- Problem: main's brief and R027 allow sibling-page content only as copied text. The current caption, "Llama Guard is one AI model that judges text and returns a verdict. It is a judge that reports; it never acts.", appears in no sibling page. It paraphrases the llama-guard-explained.html lede (line 118) and limits item 1 (line 629).
- The facts are right; only the wording rule is broken.
- Old:
  `<figcaption>Llama Guard is one AI model that judges text and returns a verdict. It is a judge that reports; it never acts.</figcaption>`
- New (verbatim, llama-guard-explained.html line 118):
  `<figcaption>Llama Guard is a single AI model from Meta that reads part of a chat and says whether it is harmful. It is a judge, not a security system: it gives a verdict, and your app decides what to do with it.</figcaption>`
- Checked and fine:
  - The copied stage-head sentences (line 211) match lionguard-explained.html line 221 word for word, links included.
  - The Images row (line 1009), "Llama Guard 4 and 3-11B-Vision, always with text.", matches llama-guard-explained.html line 612. The page only appends the navigation note "(see its page)".
  - The rail 12 .ts lines "one model you run" and "safe or unsafe + category" are sibling strings.

## 2. Optional suggestions

- **O1. Hedge in the diagram 5 caption (line 564).** "LlamaFirewall returns a result; it does not stop the chat itself." is the one place where the LlamaFirewall half of the "never acts" claim appears without a hedge, inside the LlamaFirewall section. Suggest appending "(our reading of the code)". See section 3, point 1.
- **O2. "open" in the lede (line 124).** "Meta's open umbrella project" → "Meta's umbrella project". The drafts' "open" qualifies the models ("open generative AI models", inventory (h)), not the project. The Prompt Guard 2 weights are gated, and R034 keeps their terms open.
- **O3. Together's benchmarking clause (line 429).** The page records Together's sensitive-data bar but not its section 4 bar on "competitive analysis or benchmarking" and on attempts to "probe, scan, or test" without authorisation. Both are [Documented] in PL3 R7 and PL5 R6 and listed as open in R034. Suggested text: replace `The period it keeps them is not stated, and its terms bar sending sensitive personal data.` with `The period it keeps them is not stated. Its terms bar sending sensitive personal data and using the service for "competitive analysis or benchmarking".` The next sentence already says such readings are legal ones.
- **O4. Prompt Guard 2 "Who can use it" (line 281).** "Anyone who accepts the Llama 4 licence and is approved" omits the Additional Commercial Terms: above 700 million monthly active users, a separate licence is needed (PL1 R4 line 70). Optional addition: ", unless very large (over 700 million monthly users)".
- **O5. Diagram 2 caption (line 335).** "every other scanner returns only 1.0 or 0.0" → "every other built-in scanner returns only 1.0 or 0.0". A custom scanner sets its own score.
- **O6. "The scanners" tag (line 572).** "LlamaFirewall 1.0.3 · scanners named as in Meta's code" is loose on two counts. The table reads the pinned code, which is newer than 1.0.3 (PL2 R4 line 230). Names such as "Hidden text" are not the code names. Suggest: "LlamaFirewall code at the commit read · short names for Meta's scanners".
- **O7. CyberSecEval reading note (line 962).** "fail" is not a field in the CyberSecEval reports. The fields are injection_successful_count, malicious_percentage, vulnerable_percentage and pass_rate (eval Tools table). For the over-refusal test, a higher refusal rate means more harmless requests refused, not more attacks through. Suggested text: `For the attack tests, a higher percentage of successful injections or of malicious or insecure replies means more attacks got through the model; for the over-refusal test, a higher refusal rate means more harmless requests were refused.`
- **O8. CyberSecEval Good to know (line 967).**
  - "reused the injection data once": "once" is not in the drafts. Suggest dropping it.
  - "Any use of its data for guardrail testing is a suggestion, not something Meta describes" reads against the preceding sentence, since Meta did describe one use, for the first Prompt Guard. Suggest: "Any use of its data for testing these guardrails is a suggestion; Meta describes it only for the first Prompt Guard."
- **O9. "What CyberSecEval 4 measures", capability row (line 985).** "Not suited:" → "Not likely to suit:". This matches the eval draft's wording (line 122) and the R032 suggestion tone.
- **O10. "PIICheck" in body text** (limits items 3 and 4, scorecard, lines 1026-1027). The README limits identifiers to tags, .ts lines and table code cells, and asks for "personal data", not "PII". The page already says "the personal-data check" elsewhere, so it could use that phrase in body sentences and keep "PIICheck" in tags and tables.
- **O11. dt "Action" (line 884)** is not in the README's dt list. It is clear, so it can stay; an alternative is "In".
- **O12. Rail 11 example result (line 885).** Append "(untested)" for parity with rails 7 and 9.
- **O13. Dialog Why (line 1007).** "No topic rules and no fixed replies." → "Nothing official describes topic rules or fixed replies." This is the stock phrase. The drafts infer the absence from the scanner catalogue; they do not state it.
- **O14. Eyebrow (line 122).** "…and Code Shield; CyberSecEval measures" reads awkwardly. Option: "Meta Purple Llama · Prompt Guard 2, LlamaFirewall, Code Shield and CyberSecEval".
- **O15. Overview has no .na box for Dialog.** README §7.2 asks for unsupported points as .na boxes. Modelarmor (approved) also has none, so this is acceptable. The figcaption states the gap.
- **O16. Section order.** The Llama Guard section ("Stages 1 and 2") comes after Stage 5. §8's one-section-per-tool layout allows this, and the stage numbers are correct. Moving it to sit after Code Shield (Stage 2) is optional.

## 3. Points main asked to judge

**1. "None of the three checkers stops a chat by itself", hedged as "our reading of the code".**
- The hedge is accurate. Each part of the claim rests on draft facts:
  - Prompt Guard 2 is documented as "BERT models that output only labels" (PL1 R1; verified on dev.meta.ai).
  - Code Shield's README says the integrator adds a warning or blocks (PL6 R1).
  - LlamaFirewall's scan returns a ScanResult with a decision (PL2 R5). Meta's agent demo trips the Agents SDK on a non-ALLOW decision, so the halting is the SDK's (inventory (e)).
- No draft states in words that LlamaFirewall never interrupts a chat. That part is a reading of the code, so the hedge is right.
- Adequacy:
  - Limits item 1 carries the hedge.
  - The rail 1 caption says "In the code Meta provides", which is acceptable.
  - The lede and the overview caption state the claim flatly. As summaries of hedged statements, that is tolerable.
  - The diagram 5 caption is the one flat statement inside the LlamaFirewall section. See O1.
- Verified at source: llamafirewall.py returns ScanResult objects and has no call that raises or halts on BLOCK.

**2. Rail 1 caption "LlamaFirewall works like a framework", no NeMo link claimed.**
- Acceptable. Meta itself calls it "a framework designed to detect and mitigate AI centric security risks" (PL2 R1, [Documented], README:2).
- The caption pairs this with "Meta documents no topic rules or fixed replies in it". That absence is inferred from the complete scanner catalogue (inventory (b)), not stated by Meta, but it is phrased as an absence of documentation. That is fair.
- "This page claims no link between NeMo and Purple Llama's tools" follows the lionguard precedent (R035).
- "(or a framework such as NeMo)" is the copied lionguard phrase. It describes a generic role, not an integration.

**3. Caveats present and hedged as in the drafts:**
- AlignmentCheck uses an outside service (Together):
  - Present: lede, rail 1, diagram 3, rail 11, limits 3.
  - The page says "Two scanners send text to Together" without "by default". The drafts show the endpoint can change only through a new subclass, so as shipped this is accurate.
- Never blocks, asks for human review:
  - Present: positioning table, scanners table, diagram 11, limits 1. [Documented] (PL3 R5; verified at source, line 130).
- Default judge removed from Together serverless on 2026-03-31:
  - Present: diagram 3 and its caption, rail 11 Good to know, limits 3.
  - [Documented] (verified on Together's deprecations page).
  - The draft's [Inferred] consequence ("a replacement model or a dedicated endpoint would be needed") is stated as a conditional.
  - The draft's [To be verified] item ("Whether the old Together address still answers") is hedged as "has not been tested".
- PII check fails open:
  - Present: diagram 9 (pass box "none found, or the call failed"), rail 9 Good to know, limits 4. [Documented] (verified: default `["ERROR"]` scores 0.0).
- LlamaFirewall reports scanner errors as success:
  - Present: rail 5 Good to know, limits 4. [Documented] (PL3 R5).
  - Verified at source: every result built in llamafirewall.py carries ScanStatus.SUCCESS.
  - Nuance: scan_async passes a scanner's own BLOCK or HUMAN_IN_THE_LOOP result through unchanged, but no scanner sets ERROR on those paths. The only ERROR is AlignmentCheck's missing-trace ALLOW, which is always replaced. "Never reaches your app" therefore holds.
- Code Shield PyPI package differs from repo code:
  - Present: "Which Code Shield" table and its Good to know ("whether these differences change results needs testing").
  - The "30 of 168 files" figure keeps the drafts' [Inferred] comparison as a plain finding, which is acceptable.
  - See RF7 for the LlamaFirewall half.
- Licence and terms open:
  - Llama 4 AUP: no testing clause, open; present.
  - README licence link versus gate text, "which prevails is not stated"; present.
  - MIT plus Llama 4 combination, "states the combined terms nowhere"; present.
  - Together data storage and sensitive-data bar; present.
  - CyberSOCEval CC BY-ND and CC BY-SA; present.
  - Semgrep is misdescribed: RF4.
  - Not on the page: the Together benchmarking clause (O3) and the 700M MAU clause (O4).

**4. Meta's numbers.** All exact against the drafts and credited to Meta:

| Claim | Page | Draft value |
|---|---|---|
| Prompt Guard 2 86M recall | "about 98 in 100 attacks while wrongly flagging 1 in 100 harmless prompts" | 97.5% recall at 1% FPR |
| Prompt Guard 2 22M recall | "about 89 in 100" | 88.7% |
| Prompt Guard 1 recall | "about 21 in 100" | 21.2% |
| Latency | 92.4 ms and 19.3 ms (A100, 512 tokens) | same |
| Prompt Guard scanner, AgentDojo attack success | "about 18 in 100 to about 8 in 100" | 17.6% to 7.5% |
| Code Shield precision and recall, 50 completions per language | "about 96 in 100 … about 79 in 100" | 96% and 79% |
| AlignmentCheck | "over 80 in 100 … under 4 in 100" | over 80% recall, below 4% FPR |
| CSE3 Llama 3 405B and 8B | "about 22 in 100 and 19 in 100" | 22% and 19% |
| CSE3 first Prompt Guard | "71 in 100 caught at 1 false alarm in 100" | 71.4% at 1% FPR |
| CyberSecEval set sizes | 1,916; 251 and 1,004; 1,000; 1,000 in ten categories; 750; 500; 17 languages; five judge suites | match the eval draft |

Every figure carries "Meta's", "Meta's paper" or "Meta's own … test", and the rail 4 Good to know includes "These are Meta's numbers on Meta's data; ours may differ."

**5. CyberSecEval section.**
- Measures AI models: correct.
  - h2: "A test for AI models, not a safety barrier".
  - Figcaption opens with the README's exact framing, "This is a measuring tool, not a safety barrier."
  - Diagram 13 is linear with .ln only, and outputs are plain boxes.
  - "a good score does not make an app safe" is present.
- Guardrail uses worded as suggestions (R032): yes.
  - Table header: "A possible use for guardrail testing (suggested)".
  - Tag: "a bench could reuse some of it (suggested, none chosen)".
  - Know: "Any use … is a suggestion".
  - The single "Not suited" cell is O9.
- Reading note: accurate in substance, but "fail" is not a report field and the note does not fit the over-refusal test (O7).
- The paper-reuse sentence: see O8.

**6. URLs.** See section 6. Every external link resolves. Five GitHub blob README links returned 503 twice (GitHub throttling, as in the url-checker's own run). Their raw.githubusercontent.com equivalents all return 200. No API host was requested.

## 4. Checklist (README section 11)

| Item | Result |
|---|---|
| CSS lines 6-110 identical; extra CSS in final Additions block; line 5 rewritten | PASS. The diff prints nothing. The Additions block (lines 111-116) holds the allowed link-colour line plus .mk-loc, .mk-gate, .mk-ext and .mk-nd, which use only tokens (Sentinel precedent for amber ownership tints). Line 5 lists this page's sections. |
| Fragment format; no doctype, lang, viewport, JS, images, external assets | PASS |
| Title, h1 and eyebrow | PASS: "How Meta Purple Llama Screens a Conversation". Eyebrow wording: O14. |
| Legend lists exactly the roles used | PASS: gate, dev, pass, stop and part are used; ed and na are not used and not listed. mk-* tints are explained in the diagram 3 tag (Sentinel precedent: tints not in the legend). |
| dev only on boxes the product does not do; partly uses .part with matching pills | PASS. Overview part boxes match the scorecard Partly rows; rail 11's .part gate has a Partly pill. |
| SVG viewBox, role, aria-label; no fill, stroke, style, width or height on SVG elements | PASS (14/14) |
| Marker ids unique, resolve, none unused | PASS (26 markers) |
| Section order, stage numbers, sequential h3, "diagram N" references | PASS. h3 runs 1-13, with unnumbered table rails in between. "see diagram 3" and "same model as diagram 4" point correctly. Llama Guard order: O16. |
| Scorecard: five checkpoints plus extras, pills, Why consistent | PASS WITH FIXES: RF1 and RF2. |
| ul.limits 6-8 items with bold leads, stock phrases | PASS (8 items). RF3 and RF4 fix content. |
| Every claim traces to the drafts; numbers credited to Meta; examples labelled | PASS WITH FIXES: RF1, RF3, RF5, RF6 and RF7. |
| Voice: British spelling, "AI model", "personal data", glosses, identifiers | PASS. No "LLM" in body text. "MIT-licensed" is correct British usage. "PIICheck" in body text: O10. |
| Footer sources mirror the drafts' URLs | PASS. All 22 footer URLs appear verbatim in the drafts (checked by string search). The page states "Accuracy figures are Meta's own reported results." and "Example messages are illustrative unless attributed to Meta's docs." |
| Light and dark at 1280 and 375 | PASS. Fonts loaded; no box text clipped (the in-box check found 0 issues); dashed outlines and amber or blue tints are visible in dark (fig0, fig3, fig5 and fig11 crops inspected). |
| No horizontal page overflow at 375 | PASS: scrollWidth 375 = innerWidth 375 in light and dark; no element wider than the viewport outside figure and .tablewrap. |
| Sibling look | PASS. Same spacing, box sizes and fork coordinates as Sentinel diagram 5. |
| R027 sibling text | PASS WITH FIX: the stage-head sentences and the Images row are verbatim; the rail 12 caption is not (RF8). |

## 5. Source spot-checks (verbatim text fetched 2026-10-10 into purplellama_diagram/pages/)

| # | Fact on page | URL (raw where GitHub) | Quote | Result |
|---|---|---|---|---|
| 1 | 86M 97.5%, 22M 88.7%, 92.4 and 19.3 ms; PG1 21.2% | raw .../Llama-Prompt-Guard-2/86M/MODEL_CARD.md | "Llama Prompt Guard 2 86M \| **.998** \| **97.5%** \| **.995** \| 92.4 ms"; "22M \| **.995** \| **88.7%** \| .942 \| 19.3 ms"; "Llama Prompt Guard 1 \| .987 \| 21.2%" | MATCH |
| 2 | Malicious only if it explicitly tries to override | same | "classify prompts as 'malicious' if the prompt explicitly attempts to override prior instructions" | MATCH |
| 3 | 512 tokens; your app splits longer text | same | "support a 512-token context window. For longer inputs, split prompts into segments" | MATCH |
| 4 | PG1 legacy quote | https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard | "Developers should migrate to Llama Prompt Guard 2" | MATCH |
| 5 | PG2 gives only a label (point 1) | same | "Llama Prompt Guard 2 are BERT models that output only labels" | MATCH |
| 6 | PG1 licence includes Llama 3 (RF5) | raw .../Prompt-Guard/README.md | "The same license as Llama 3 applies" | MATCH (page omits it: RF5) |
| 7 | LlamaFirewall reports status success | raw .../LlamaFirewall/src/llamafirewall/llamafirewall.py | "status=ScanStatus.SUCCESS," at lines 140, 167, 187, 201, 261; scan_async returns scanner_result for BLOCK or HITL | MATCH (nuance in section 3, point 3) |
| 8 | PIICheck fails open; block at 0.7 | raw .../scanners/experimental/piicheck_scanner.py | "block_threshold: float = 0.7"; "detected_pii_types=[\"ERROR\"]" | MATCH |
| 9 | AlignmentCheck fails closed, never blocks; prompt rates only the latest action | raw .../scanners/experimental/alignmentcheck_scanner.py | "conclusion=True,"; "return ScanDecision.HUMAN_IN_THE_LOOP_REQUIRED"; "Only consider the selected action, not the entire trace." | MATCH |
| 10 | PDF example | raw .../website/docs/documentation/llamafirewall-architecture/workflow-and-detection-components.md | "Invisible text near the end says…" mapped to "**PromptGuard** and **Regex scanner** detect jailbreak input" | MATCH to draft; page misreads it (RF1) |
| 11 | CyberSecEval next version | raw .../CybersecurityBenchmarks/README.md | "As of June 12, 2025, our team is exploring options for the next version of our project" | MATCH |
| 12 | Default judge off serverless on 2026-03-31 | https://docs.together.ai/docs/deprecations | "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8" with "2026-03-31" | MATCH |
| 13 | AlignmentCheck over 80 in 100, under 4 in 100 | https://arxiv.org/html/2505.03574 | "these models achieved over 80% recall with a false positive rate below 4%" | MATCH |
| 14 | Code Shield 96 and 79 in 100 | same | "CodeShield achieved a precision of 96% and a recall of 79%" | MATCH |
| 15 | Prompt Guard scanner, AgentDojo 18 to 8 in 100 | same | "attack success rate (ASR) of 17.6%"; "reduced the ASR to 7.5%, a 57% drop" | MATCH |
| 16 | AlignmentCheck on AgentDojo (RF3) | same | "reduction in ASR to 2.89% - an 84% drop relative to baseline" | MATCH (page omits it: RF3) |
| 17 | CSE3 Llama 3 22 and 19 in 100 | https://arxiv.org/html/2408.01605 | "Llama 3 405B and Llama 3 8B failing at rates of 22% and 19% respectively" | MATCH |
| 18 | CSE3 first Prompt Guard 71 in 100 at 1 in 100 | same | "identifies 71.4% of these injections with a 1% false-pos[itive rate]" | MATCH |

Tally: 18 MATCH, 0 MISMATCH, 0 UNVERIFIABLE. The sources match the drafts. In two cases (10 and 16) the page misstates or undercounts what the drafts say: RF1 and RF3.

## 6. URLs (curl -L, 2026-10-10)

- 24 unique external hrefs and 3 local sibling links. All three local files exist: nemo-rails, llama-guard and sentinel.
- 200 (18): arxiv html 2404.13161, 2408.01605 and 2505.03574; dev.meta.ai Prompt Guard page and protections page; Together deprecations, zero-data-retention and terms; the Google Fonts css2 URL; GitHub blob Llama-Prompt-Guard-2/86M/MODEL_CARD.md; the Hugging Face AlignmentCheck dataset raw README; HF Llama-Prompt-Guard-2-86M and -22M; the CyberSecEval docs site; LlamaFirewall docs pages alignment-check and regex-scanner-tutorial; PyPI codeshield and llamafirewall.
- 503 then raw 200 (5): GitHub blob README.md at 172c1074 for the root, CodeShield, CodeShield/insecure_code_detector, CybersecurityBenchmarks and LlamaFirewall.
  - The blob page returned 503 twice. https://raw.githubusercontent.com/meta-llama/PurpleLlama/172c1074069eb88ec834124272c1b1c4f8893445/<same path> returned 200 for each.
  - Classified as GitHub throttling of rendered README pages; the url-checker's own run saw the same 429 and 503 pattern.
- 404 (1, expected): https://fonts.googleapis.com, the bare preconnect origin. It is not a navigable link and is identical on every sibling page.
- No API host was requested.

## 7. QUESTIONS

None.
