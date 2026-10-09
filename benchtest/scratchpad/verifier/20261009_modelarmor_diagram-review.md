# modelarmor P10 diagram review: benchtest/diagrams/modelarmor-explained.html (commit fbd6460)

- Reviewer: gr-verifier (fresh, adversarial). Date: 2026-10-09.
- Sources of truth: benchtest/drafts/modelarmor_two_level.md and benchtest/drafts/modelarmor_inventory_final.md. Rulings read: R002, R012, R017, R024, R025, R026.
- The working-tree page is identical to fbd6460 (`git diff fbd6460` is empty).
- Renders are in benchtest/scratchpad/verifier/modelarmor_diagram/ (PNGs are gitignored):
  - full pages: modelarmor_{light,dark}_{1280,375}.png
  - per figure: fig_{light,dark}_NN.png
  - per table: tab_{light,dark}_NN.png
  - phone_top_dark.png
  - scripts: render.py, figs.py and mech.py
- URL results: modelarmor_diagram/url_check.txt. The verbatim source texts fetched for this review are in the same folder: ov.txt, int.txt, quotas.txt and the other .txt files.

## Verdict: PASS WITH FIXES (10 required fixes)

The structure is clean:
- The shared CSS block is byte-identical to Sentinel's.
- There are 15 SVGs and 31 markers, all unique and resolved.
- The legend matches the roles used.
- Sections, stage numbers and diagram references are correct.
- All 34 URLs return 200.
- No box text is clipped in either theme.

Most claims trace to the drafts. The 10 fixes are all one-line text edits. They fall into four groups:
- Three claims contradict the drafts or the source: the LangChain flag (RF4), image answers (RF5) and the footer latency link (RF3).
- Three claims are not in the drafts: topic rules "on some Google routes" (RF2), "there is no check" (RF8) and "swapped for labels" (RF9).
- One title is internally inconsistent (RF1).
- Three are README voice rules: "set it yourself" (RF7), and missing glosses on first use (RF6, RF10).

## 1. Required fixes

**RF1. Rail 1 h3 (line 217): "Four different kinds of tool", but the diagram shows three and two of the four are the same kind.**
- The rail's diagram and its aria-label ("Three columns.") show NeMo, Llama Guard and Model Armor.
- Sentinel appears only in the table, where it is "A web service with a menu of checks". Model Armor is "A managed Google Cloud service with a menu of checks", which is the same kind.
- The SDP page uses "Four" because its diagram has four columns. The Sentinel page uses "Three different kinds of tool" with Sentinel in the table only, and that precedent fits here.
- Replace: `<h3>1. Four different kinds of tool</h3>`
- With: `<h3>1. Three different kinds of tool</h3>`

**RF2. Overview aria-label (line 133) and figcaption (line 203): "topic rules … only on some Google routes" is not in the drafts.**
- The drafts tie topic rules to no route. MA1 R2 has the overview scenario [Documented] and says no setting exists [Not disclosed].
- Only fetched text and tool calls are route-bound: INT routes for grounding data; MCP servers and Agent Gateway for tool calls.
- Replace in the aria-label: `Text fetched for the AI model, topic rules and tool calls are only partly covered, on some Google routes.`
- With: `Text fetched for the AI model and tool calls are only partly covered, on some Google routes, and topic rules appear only as a scenario in Google's docs.`
- Replace in the figcaption: `Fetched text, topic rules and tool calls are only partly covered, and only on some Google routes.`
- With: `Fetched text and tool calls are only partly covered, and only on some Google routes; topic rules appear only as a scenario in Google's docs.`

**RF3. Footer (line 952): the "Service Extensions guide" link points to a page without the quoted latency.**
- Rail 3 quotes Google's guide: Model Armor has a latency of "approximately 250 milliseconds".
- The quote is on configure-extensions-to-google-services (SEGS). The inventory, row "Service Extensions…", cites it as SEGS.
- The P7 cached copy of SEGS reads: "Consider that Model Armor has a latency of approximately 250 milliseconds."
- The linked configure-traffic-extensions page has 0 mentions of "Model Armor" in the cached copy.
- The SEGS URL is in the drafts (MA1/MA3/MA4/MA8 R9 and the inventory) and returns 200.
- Replace: `<a href="https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions">Service Extensions guide</a>`
- With: `<a href="https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services">Service Extensions guide</a>`
- Keeping the traffic-extensions link as a second link is optional. It is in the drafts, but nothing on the page relies on it.

**RF4. Rail 3 "Good to know" (line 443): the LangChain flag does not "do the same".**
- The Agent Platform behaviour is a skip on failure. VTX: "skips the Model Armor sanitization step and continues processing the request" when Model Armor is unavailable, unreachable or errors.
- LangChain's flag is a different thing. LC: "True: logs a warning but lets content pass even if risks are detected."
- MA4 R4 records only the LangChain wording, so the page's "does the same" is not supported. Result: MISMATCH.
- Replace: `LangChain's fail-open flag does the same if you set it to true.`
- With: `LangChain's fail-open flag, if set to true, lets content through with only a warning, even when risks are found.`

**RF5. Image answers: rail 10 "Good to know" (line 769) and the menu-table Images row (line 355) contradict the drafts and the rail's own figcaption.**
- MA10 R3 marks it [Documented] that the overview and release note 2026-06-25 say images are screened "in the prompts and responses". The missing piece is an example (MA10 R3 [Not disclosed]).
- Rail 10's figcaption already says this correctly.
- Line 769: replace `Which checks run on the text read from a picture, the languages it reads, and whether answers can carry images are not stated.`
- With: `Which checks run on the text read from a picture and the languages it reads are not stated, and no answer-side example is shown.`
- Line 355, last cell: replace `<td>Input; the us and eu regions only</td>`
- With: `<td>Input; answers too per Google's docs, with no example; the us and eu regions only</td>`

**RF6. Glosses on first use (README section 9). Main asked about MCP; data residency and grounding data have the same problem.**
- MCP:
  - Its first use is the route table, line 435 ("calls to MCP servers"). The gloss comes only at line 899.
  - The gloss's word "common" is not in the drafts. The drafts never characterise MCP, they only describe "MCP tool calls and tool responses".
  - Line 435: replace `and calls to MCP servers, other agents` with `and calls to MCP servers (MCP is a way for an AI agent to call tools), other agents`.
  - Line 899: replace `MCP is a common way for an AI agent to call tools. On Google's MCP servers` with `On Google's MCP servers`.
- Data residency:
  - Its first use is the menu table, line 350 ("when data residency is enforced"). It is used again at lines 494 and 587, but glossed only in limits item 4 (line 941).
  - Line 350: replace `Singapore included, when data residency is enforced</td>`
  - With: `Singapore included, when data residency is enforced (a template setting, on by default, that keeps processing inside the region's jurisdiction)</td>`
  - The gloss text is the page's own limits wording. It traces to inventory (c) dataResidencyCompliant: "True for new templates", "True disables features not hosted in the template's jurisdiction".
- Grounding data:
  - It is first used in the h3 and figcaption of rail 11 (line 813), with no gloss.
  - Line 813: replace `in-between steps such as grounding data and web search results.`
  - With: `in-between steps such as grounding data (reference text fetched to support the answer) and web search results.`
  - This traces to INT, which calls it "the retrieved grounding data". The source text is in int.txt.

**RF7. "so set it yourself" (lines 335 and 494) is a setup instruction, and the drafts keep this point as needing testing.**
- README section 1 says the page "does not recommend … or give setup steps".
- MA1 R5 and R8 mark the effective default as [To be verified] (needs testing).
- Line 335: replace `Its docs state three different defaults when you leave the level out, so set it yourself.`
- With: `Its docs state three different defaults when you leave the level out, and which one applies needs testing.`
- Line 494: replace `Its docs give three different defaults for a missing level, so set it yourself.`
- With: `Its docs give three different defaults for a missing level, and which one applies needs testing.`

**RF8. Rail 13 aria-label (line 874) and "Good to know" (line 901): a flat absence claim that the drafts do not make.**
- No draft bullet states that an action-validity check is absent. A grep for "sensible", "action itself" and "business" finds nothing relevant.
- The scorecard row (line 921) already uses the stock phrase "Nothing official describes a check for whether an action is sensible", so the page should say the same in all three places.
- Line 874: replace `Whether the action itself is sensible is not checked.`
- With: `Nothing official describes a check on whether the action itself is sensible.`
- Line 901: replace `There is no check for whether an action is sensible, so a business limit`
- With: `Nothing official describes a check for whether an action is sensible, so a business limit`

**RF9. Rail 8 aria-label (line 642) and figcaption (line 661): "replaced by a label" generalises from the one example.**
- The de-identified form is whatever the customer's de-identify template does.
- The drafts cover more than labels. MA5 R1: SDP inside Model Armor can "transform, tokenize, and redact sensitive elements". MA5 R1 also leaves the transformation types to the SDP columns.
- The only example uses the label [IP_ADDRESS].
- Line 642: replace `it also returns a copy with each match replaced by a label.`
- With: `it also returns a copy with each match changed as that template says, for example replaced by a label.`
- Line 661: replace `Model Armor also returns a copy with the items swapped for labels.`
- With: `Model Armor also returns a copy with the items changed as that template says, for example swapped for a label such as [IP_ADDRESS].`

**RF10. Rail 6 tag (line 553): "mainly output" is the drafts' reading, stated as fact.**
- MA7 R1 says: "the filter is not output-only; 'mainly output' is a reading [Inferred]".
- README section 10 says hedged material stays hedged. A tag has no room for a hedge, so drop the phrase. The figcaption already explains the output emphasis.
- Replace: `Malicious URL detection · input and output, mainly output ·`
- With: `Malicious URL detection · input and output ·`

## 2. Optional suggestions

- **O1. Rail 3 route table, Gemini Enterprise.**
  - "Gemini Enterprise" is never glossed. The drafts call it "the Gemini Enterprise assistant" (MA9 R3).
  - Suggest at line 401 or line 434: "Gemini Enterprise, Google's AI assistant product".
  - "Custom agents (ADK, A2A, Dialogflow)" are unglossed acronyms in a body cell. Suggest "Custom agents, such as ones built with Google's Agent Development Kit or Dialogflow, are not screened."
- **O2. Rail 11 Agent Runtime gloss (line 813).**
  - "Agent Runtime is where agents built with Google's Agent Development Kit run" reads as exclusive.
  - AGW says non-ADK payloads (LangChain) reach the gateway but are not sent to Model Armor, which implies other agents run there too.
  - Suggest "Agent Runtime is a Google service that runs AI agents, such as ones built with Google's Agent Development Kit".
  - The current wording is defensible from inventory row 33, so this is optional.
- **O3. "Preview" is never glossed.**
  - It appears in the eyebrow, line 117. The drafts give a [Documented] line in MA10 R4: "Preview offerings are intended for use in test environments only".
  - Suggest at the first body use (line 303 area, or limits item 7): "Preview (Google's pre-release stage, meant for test environments)".
- **O4. Limits item 7 and the rail 10 "Good to know".**
  - "Plan tests with made-up data" and "so tests need made-up data" read as advice.
  - Attributing them to the bench rule (R025) is cleaner: "The project's rule is to test Preview features with made-up data only."
- **O5. Rail 8 figcaption (line 661).**
  - "LIKELY" is an identifier in a figcaption. README section 9 allows identifiers only in tags, `.ts`, `td.code`, `mark` and `dd`.
  - Suggest `a likelihood word such as "likely"`.
- **O6. Limits item 3 (line 940).**
  - The bold lead ends in a colon ("Its docs disagree in places:"), not a sentence. This is the same as SDP O6.
- **O7. Limits item 4.**
  - "Switching it off enables the other checks" could add "except image screening, which stays in the us and eu regions".
  - This is per TPL: "enables all Model Armor features except for image modality". It already appears elsewhere on the page.
- **O8. Rail 3 route table, MCP servers row.**
  - "Tool calls that match are blocked" holds only in Inspect and block mode. The MCP floor setting has an enforcement type of INSPECT_ONLY or INSPECT_AND_BLOCK (inventory c).
  - Suggest "Tool calls that match can be blocked".
- **O9. Rail 10 tag "Image screening (Preview) · input" and rail 9 tag "Document screening · input".**
  - These are fine as simplifications once RF5 is applied.
  - For images, "input and output (no answer example)" would be more exact.

## 3. Points main asked to judge

**1. Scorecard "Monitoring = Partly": CONFIRM.**
- README section 7 names Monitoring as an extra row but does not define it. The house definition comes from the siblings:
  - Sentinel = Yes: "The refusal check measures how often, and how, the bot says no."
  - SDP = No: its scans and profiles look at stored data, "not at chat traffic".
- Model Armor sits between the two:
  - It has a Cloud Monitoring dashboard of live chat-traffic detections: request_count, pi_jb_request_count, rai_request_count, sdp_request_count, malicious_uri_request_count and used_token_count, with Input and Output counts. This is in inventory (b) [Documented] (MON), and the dashboard has been GA since 2025-12-04.
  - Sanitize operations are logged to Cloud Logging [Documented] (LOG).
  - It has no refusal measurement. MA1 R2 [Not disclosed] says: "A model's refusal is separate from a Model Armor block". This is verified at source (ov.txt line 490).
- Partly is therefore the consistent call, and the Why text is accurate.

**2. Hedged "our reading, untested" claims**
- **Singapore NRIC (rail 8 example, line 667): SUPPORTED, keep.**
  - MA5 R7 (l. 987) and MA6 R7 (l. 1153) say [Inferred]: "A Singapore NRIC test therefore needs an advanced template whose inspect template lists that built-in infoType".
  - The built-in infoType is [Documented]. Verified at source: SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER, "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card." (sdpinfo.txt l. 406-407). MATCH.
  - "Basic mode lists no Singapore identifier" traces to MA5 R2 [Not disclosed].
- **Topic rules are probably custom SDP detectors (rail 12 figcaption, line 859): SUPPORTED, keep.**
  - MA1 R2 (l. 39) is [Inferred], with its premise "including topicality" [Documented] (l. 38).
  - Verified at source: "sensitive data protection (including topicality)." (ov.txt l. 215). MATCH.
  - The page uses the stock phrase "That is our reading; we have not tested it yet."
- **Own-document passages could be sent as text (rail 11 figcaption, line 813): ACCEPTABLE, keep.**
  - No draft bullet states this capability in so many words. It is a trivial consequence of [Documented] facts: the text API (MA1 and MA3 R3) and "intermediate steps … grounding data" on INT routes.
  - The drafts' bench plans already assume it [Inferred]:
    - MA3 R7 l. 570: test data "instructions hidden in retrieved text".
    - MA4 R7 l. 788: "a retrieved web page or tool result carrying hidden instructions" posted to the response method.
  - "Nothing official describes this" matches MA3 R2 l. 450 [Not disclosed]: "Coverage of indirect injection through retrieved text … no evaluation or statement found".
  - The sentence is hedged ("our reading and it is untested").
  - Under R026, Retrieval = Partly rests on the documented INT grounding-data routes and file inputs, not on this hedge.

**3. Plain-English glosses**
- **Apigee** ("a Google service that sits between apps and the web APIs they call"): ACCURATE.
  - Inventory (b) Apigee row: "Apigee API proxies", "Inline in the Apigee request flow and response flow".
  - GA date verified: the Apigee release notes of September 04, 2025 say "SanitizeUserPrompt / SanitizeModelResponse … are now GA". MATCH.
- **MCP**: the gloss comes late, and its word "common" is unsupported (RF6).
- **Agent Runtime**: acceptable. It traces to inventory row 33, "agents built with the Agent Development Kit (ADK) on Agent Runtime". O2 suggests a less exclusive wording.
- **Agent Gateway** ("a Google gateway that intercepts an AI agent's traffic and calls Model Armor"): ACCURATE. AGW (inventory row 33): "Agent Gateway intercepts the request and the response and invokes Model Armor".
- **Floor settings** ("a minimum set of checks that applies across a project, folder or organisation"): ACCURATE. Inventory (c): template conformance plus the organisation, folder and project levels.
- **Agent Platform** ("Google's name for the Vertex AI route"): ACCURATE (inventory scope paragraph, naming).
- **Not glossed: data residency and grounding data** (RF6); Gemini Enterprise and Preview (O1, O3).

**4. Internal link to sdp-explained.html (line 633): FINE.**
- benchtest/diagrams/sdp-explained.html exists (commit 3930aea, with fixes in a3962a3).
- The sentence matches R012: Model Armor keeps its own column and cross-references the wrapped engine. "Model Armor does not find sensitive data itself. It calls … Sensitive Data Protection … covered on its own page."
- The SDP page links back to modelarmor-explained.html at lines 280 and 512.
- The one-line CSS addition, `.stage-head a, .know a { color: var(--accent); }`, is identical to the reviewed SDP page's block. README section 9 says "link with plain text, not new CSS", so see Q2.

**5. Phone width: known shared issue, not counted as a fix.**
- At 375 px the scrollWidth is 628 in both themes.
- The elements overflowing are header, eyebrow, h1, lede, legend, sections and h2, all from the base CSS. This matches the SDP and Sentinel pages.
- At 1280 px there is no overflow.
- The automated check found 0 SVG text-overflow issues at either width.

**6. URLs: 34 of 34 return 200, with 0 redirects.**
- The page has no github.com links. fonts.googleapis.com was not requested, and no *.googleapis.com URL was requested.
- The RF3 replacement URL (configure-extensions-to-google-services) also returns 200.
- All 34 URLs appear in the drafts.

## 4. Checklist (README section 11)

| Item | Result |
|---|---|
| CSS lines 6-109 identical to Sentinel; line 5 rewritten; extra CSS only in a final "Additions for this page" block | PASS. The diff is empty. The one added block is for links, as on the SDP page (Q2) |
| Fragment format: title, preconnect, fonts link, style, .wrap; no doctype, lang, viewport, JS, images or other assets | PASS |
| Title in title case; h1 in sentence case; eyebrow "Google Cloud Model Armor · managed service, some features in Preview" | PASS |
| Legend lists exactly the roles used (gate, dev, pass, stop, edit, part); no .na is used, so no na swatch | PASS |
| dev only on boxes the app owns; Google-service blocks are plain .no (rails 11 and 13); .part boxes match Partly pills (rails 7, 11, 12, 13) | PASS |
| Every SVG has viewBox, role and an aria-label narrating both branches; no fill, stroke, style, width or height attributes; no title element | PASS (15 SVGs; RF2, RF8 and RF9 fix wording only) |
| Marker ids unique; every url(#) resolves; none unused | PASS (31 markers) |
| Section order (header, overview, positioning, how it works, routes, stage 1, stage 2, sensitive data, files and images, stage 3, stages 4 and 5, scorecard, limits, footer); h3 numbers 1-13 run in order; "diagram N" references are correct, including NeMo's diagram 8 | PASS |
| Scorecard: five checkpoints in NeMo order plus Files, Images and Monitoring, each with a pill and a Why that matches its stage | PASS |
| ul.limits: 8 items, each with a bold lead; stock gap phrases used | PASS (O6) |
| Every claim traces to the drafts; vendor numbers attributed; examples labelled | FAIL until RF2-RF5 and RF8-RF10 are applied |
| Voice: British spelling; "AI model"; no LLM or PII outside quotes; terms glossed; identifiers only where allowed | FAIL until RF6 and RF7 are applied (O1, O3 and O5 are optional) |
| Footer sources mirror the drafts' official URLs | PASS for presence; RF3 corrects the target of one link |
| Renders in light and dark at 1280 and 375; text legible; no clipped box text; dashes and tints visible in dark | PASS |
| No horizontal page overflow | Known shared base-CSS issue at 375 (628 px); not counted |
| Looks like a sibling of Sentinel | PASS. The positioning-table cells for NeMo, Llama Guard and Sentinel match sentinel-explained.html word for word. The new "Singapore region" row's Sentinel cell traces to sentinel_two_level.md l. 135 [Not disclosed] |

## 5. Source spot-checks (fetched live 2026-10-09 with fetch_text.py unless marked "cached")

| # | Claim on page | Source and verbatim | Result |
|---|---|---|---|
| 1 | Three routes screen grounding data and search results (rail 11) | integrations: "The Model Armor integrations with Gemini Enterprise, Agent Runtime, and Apigee sanitize the initial user prompt, the final agent or model response, and intermediate steps, such as grounding data and responses returned by web search tools." | MATCH. The drafts' inventory (b) intro says "Gemini Enterprise Agent Platform, Agent Runtime and Apigee", which is a draft-side error (Q1) |
| 2 | REST use "functions only as a detector" (rail 2 "Good to know") | integrations: "Model Armor functions only as a detector using templates." | MATCH |
| 3 | Only Gemini Enterprise accepts files among Google's routes | integrations: "only the Gemini Enterprise integration supports documents. All other integrations scan and sanitize only text." | MATCH |
| 4 | Harassment definition (rail 4) | overview: "Threatening, intimidating, bullying, or abusive comments targeting another individual." | MATCH |
| 5 | "configured using custom rules to not discuss competitors" (rail 12) | overview: "A company's support bot is configured using custom rules to not discuss competitors." | MATCH |
| 6 | Phishing link in an answer: whole answer blocked (rail 6 example) | overview: "Model Armor blocks the entire LLM response" | MATCH |
| 7 | Refusal is separate from a block (scorecard, Monitoring row) | overview: "A model's refusal is separate from a Model Armor block." | MATCH |
| 8 | Confidence advice; Low and above "not recommended" for general categories | overview: "Production environments that prioritize uninterrupted user interactions" / "Standard enterprise applications" / "Not recommended for general responsible AI content categories" | MATCH |
| 9 | Nine tested languages, Mandarin included; quality "might vary" | overview: Chinese (Mandarin), English, French, German, Italian, Japanese, Korean, Portuguese, Spanish; "might vary" | MATCH |
| 10 | Fewer than three words returns no match | overview: "if the word count is fewer than three words, Model Armor returns NO_MATCH_FOUND because such inputs lack enough information to constitute an attack." | MATCH |
| 11 | 1,200 a minute; 65,536 tokens (about 262,144 characters); 130,000; 4 MB; first 256 links | quotas: "1200 queries per minute (QPM) per project"; "65,536 tokens (approximately 262,144 characters)"; 130,000; 4 MB; "scans only the first 256 URLs" | MATCH |
| 12 | Free to 2 million tokens a month, then $0.10 per million; no extra charge for SDP | pricing: "no cost for using Model Armor up to 2 million tokens per month … billed at a rate of $0.10 per million tokens"; "there are no additional charges to use it." | MATCH |
| 13 | "combines rules-based controls, ML models, and powerful AI reasoning models"; "embedded threats like indirect prompt injection" | product page, same words | MATCH |
| 14 | AUP clause (limits item 8) | aup: "to test or reverse-engineer the Services in order to find limitations or vulnerabilities, or to evade filtering capabilities, except as expressly permitted in the Agreement" | MATCH |
| 15 | Cross-jurisdictional routing "can impact your data residency compliance" (limits item 4) | manage-templates: "Caution: Cross-jurisdictional routing of your data can impact your data residency compliance." | MATCH |
| 16 | Agent Platform skips on failure (rail 3) | vertex integration: "skips the Model Armor sanitization step and continues processing the request" when Model Armor is unavailable, temporarily unreachable or errors | MATCH |
| 17 | LangChain's fail-open flag "does the same" (rail 3 "Good to know") | langchain: "True: logs a warning but lets content pass even if risks are detected." | MISMATCH (RF4) |
| 18 | GA dates: Agent Platform 2025-12-03, Gemini Enterprise 2025-09-16, Agent Gateway 2026-06-24, streaming 2026-07-10, MCP 2026-04-22, GKE 2025-09-15 | release notes: all six entries state General Availability on those dates | MATCH |
| 19 | Apigee GA since 2025-09-04 | Apigee release notes, September 04, 2025: "Four new Apigee policies … are now GA: … SanitizeUserPrompt, SanitizeModelResponse" (cached P7 copy) | MATCH |
| 20 | Built-in Singapore NRIC detector | SDP infotypes reference: SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER, "A unique set of nine alpha-numeric characters on the Singapore National Registration Identity Card." | MATCH |
| 21 | Agent Gateway docs disagree on masking | agent gateway: "block and redact content that violates policies" vs "either allows or blocks it based on the verdict" | MATCH |
| 22 | Latency "approximately 250 milliseconds", and the footer link that should support it | configure-extensions-to-google-services (cached P7 copy; today's live fetch returned an empty body): "Consider that Model Armor has a latency of approximately 250 milliseconds." The linked configure-traffic-extensions page has no "Model Armor" text (cached) | MATCH for the quote, MISMATCH for the footer link (RF3) |
| 23 | "topicality" placed inside the sensitive-data filter | overview: "sensitive data protection (including topicality)." | MATCH |

Tally: 21 MATCH, 2 MISMATCH (17 and the footer-link half of 22), 0 UNVERIFIABLE.

## 6. QUESTIONS

- **Q1 (route to gr-merger; draft-side and outside this page).**
  - modelarmor_inventory_final.md line 24, block (b) intro, says "INT also says the Gemini Enterprise Agent Platform, Agent Runtime and Apigee integrations sanitize … intermediate steps".
  - The live integrations page says "Gemini Enterprise, Agent Runtime, and Apigee", which is what the two_level drafts say (MA1 R3 l. 49 and others).
  - Suggested fix: delete "Agent Platform" in that sentence.
  - This needs a check of whether P8 has already written it to the workbook (R024 approved the finals as they stood).
- **Q2 (main; consistency).**
  - README section 9 says to cross-link "with plain text, not new CSS".
  - Both sdp-explained.html and modelarmor-explained.html add the same one-line block, `.stage-head a, .know a { color: var(--accent); }`. Without it, in-body links would render in the browser's default blue, which has poor contrast in dark mode.
  - Either record a ruling or README note that allows this block on all pages, or drop it from both pages. This review does not count it as a fix, because the reviewed SDP page set the precedent.
