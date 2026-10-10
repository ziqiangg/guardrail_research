# litmus P10 diagram review (gr-verifier, fresh, adversarial)

- Date: 2026-10-11
- Page: benchtest/diagrams/litmus-explained.html (583 lines, as in commit 3ed9652; not edited)
- Sources of truth: benchtest/drafts/litmus_eval_tooling_final.md (EV), litmus_inventory_final.md (INV), litmus_changes.md (CH)
- Rulings applied: R003, R026, R027, R032, R038, R040; main's P10 ruling in queue.md (title "How GovTech Litmus Tests an AI Application", gate legend "Test run by Litmus"); diagrams/README.md §8 note on evaluation-tool pages
- Screenshots and scripts: benchtest/scratchpad/verifier/litmus_diagram/ (render.py, figs.py, url_check.txt; PNGs gitignored)

## Verdict: PASS WITH FIXES (8 required fixes)

The page is well built: shared CSS is byte-identical, it renders cleanly in light and dark at 1280 and 375 with no page overflow, the sibling table cells are word for word, every quote checked at source matches, it uses no bench-design wording, and Moonshot appears only as a hedged resemblance. It fails the required items: the title, h1 and legend still use the pre-ruling wording, Kaleidoscope's status is stated more strongly than the drafts allow, one limits item is phrased as advice, one attributed docs claim is reworded, and the footer leaves out a source the page relies on.

## 1. Checklist (diagrams/README.md §11)

| # | Item | Result | Notes |
|---|---|---|---|
| 1 | CSS lines 6-110 identical; additions only in a final block; line 5 rewritten | PASS | `diff <(sed -n 6,110p sentinel…) <(sed -n 6,110p litmus…)` printed nothing. The additions block (lines 111-115) holds the allowed link rule, `.sw.nd`, `.mk-nd` and `.mk-plan`. Line 5 lists the actual section order. |
| 2 | Fragment format | PASS | title, preconnect, fonts link, style, `.wrap`. No doctype, html/head/body, lang, viewport, script or img. |
| 3 | Title, h1, eyebrow | FAIL | The title is "How GovTech Litmus Tests a Conversation" and main's P10 ruling requires "How GovTech Litmus Tests an AI Application" (README §8). The h1 has the same problem. The eyebrow "GovTech Litmus · hosted service, labelled proof of concept on one portal page" is OK. See R1 and R2. |
| 4 | Legend lists exactly the roles used; wording | FAIL (wording) | The gate label reads "Check done by Litmus" and the ruling requires "Test run by Litmus" (R3). Roles used: gate, box dev, mk-nd, na, mk-plan (Kaleidoscope). Planned has no swatch, which README §4 makes optional (cloak adds `.sw.plan`; see O5). The scorecard uses Partly pills but has no `.part` boxes, so the missing part swatch is acceptable. |
| 5 | `dev` only on what the product does not do | PASS | `box dev` is on "Your application", "Your team" and "Your app". Precedent: `box dev` on the modelarmor and purplellama pages. Litmus boxes are plain `gate`. Sentinel in diagram 5 is a plain `box` (correct, because the gate role is Litmus). |
| 6 | SVG attributes | PASS | 6 SVGs. Each has viewBox, role="img" and a full-sentence aria-label. There are no fill/stroke/style/width/height attributes. |
| 7 | Marker ids | PASS | `o-a` (9 uses), `a2` (2), `a3` (3), `a5` (4). All resolve and none is unused. Diagram 4 has no arrows, so it has no marker. |
| 8 | Section order, numbering, diagram refs | PASS | Order: Header, Overview, Positioning, How it works, What it tests, Behind the tests, Litmus and Sentinel, Scorecard, Limits, Footer. This is the measuring-tool arc (README §8), so there are no stage sections. h3 numbers run 1-5, and the unnumbered table rails are "Ways to start a run" and "The 14 tests". "diagram 5" in figcaption 1 points at the correct rail. |
| 9 | Scorecard rows, pills, Why | PASS | Rows in order: Input, Output, Retrieval, Dialog, Execution, Images, Monitoring. Column "Litmus tests it?" (§8). Every row has a pill and a Why. The calls are judged in §3 below. |
| 10 | Limits 6-8 items, bold leads, stock phrases | PASS with fixes | 8 items. Item 6's lead is an imperative, which counts as advice (R6). Item 8 overstates Kaleidoscope's status (R5). |
| 11 | Every claim traces to the drafts | FAIL (3 points) | Kaleidoscope "not yet in Litmus" / "planned, not shipped" (R4, R5). "The docs promise a pass or fail for each test" (R7). The refusal-rate source is missing from the footer (R8). See §3. |
| 12 | Voice | PASS | British spelling, "AI model", no LLM/PII, no YAML, config keys or JSON fields in prose. CI/CD, jailbreak and suite are glossed. "TechPass", "push and pull request" and "API" are left unglossed (minor; TechPass cannot be glossed without facts the drafts lack). |
| 13 | Footer mirrors the drafts' URLs | PASS with fix | All 14 links appear in the drafts. The Safety evals page (safety.mdx), the source of the refusal-rate claim, is missing (R8). Neither malformed P9 form is present: there is no `…/website/docs/` blob base and no `safety.mdx@45908b48:17` URL. |
| 14 | Renders light/dark at 1280/375 | PASS | Body background is rgb(246,247,249) in light and rgb(18,22,31) in dark. Dashed `mk-nd`, `na` and `box dev` boxes stay visible in dark (fig0_dark, fig3_dark, fig4_dark). An automated text-in-box clip test found no clipped text in any SVG. There were no console messages. |
| 15 | No horizontal page overflow | PASS | scrollWidth == innerWidth: 1280/1280 and 375/375 in both schemes. No element outside a figure or `.tablewrap` passes the viewport edge. |
| 16 | Looks like a sibling | PASS | Same spacing and box sizes. The four-column zone diagram follows the lionguard and purplellama precedent. |

## 2. Specific judgements requested by main

- **Title and gate legend (main's P10 ruling):** both differ from the ruling, so they are required fixes R1 to R3.
- **Sibling cells (R027):** a script compared the positioning table with sentinel-explained.html lines 266-273. All 7 shared rows MATCH word for word for NeMo, Llama Guard and Sentinel. The "Edits text" row is dropped, which README §7.3 allows ("drop rows only where the facts demand"); see O6. The stage-head sentence "Sentinel is a web service run by GovTech that gives a score for each check" is word for word from the reviewed presidio page (R027 "any later reviewed page"). Diagram 5's figcaption sentence "At every point Sentinel only returns scores; your app decides the cut-off and what happens next." is word for word from Sentinel's overview figcaption. Figcaption 1 drops "both" from Sentinel's "Llama Guard and Sentinel both report", because the subject changed. That is not a table cell, so it is acceptable. The SVG column text for the siblings is condensed, as on the lionguard page.
- **Scorecard calls:**
  - **Input Partly:** accepted. The Why is hedged "(our reading)" and says it does not report on an input check by itself. It does not contradict EV:18 ("no input-level or output-level function", which is about guarding). It reflects that Litmus's prompts go through whatever input path the app has (EV:12; playbook :52).
  - **Output Partly:** accepted. The Why is documented: the responses are scored (EV:13).
  - **Dialog Partly:** acceptable. The political and specialised-advice tests judge topic handling (EV Datasets rows), and "Litmus has no topic rules and writes no replies" is correct. The mapping to NeMo's dialog checkpoint is our reading but carries no hedge, unlike Input (O2).
  - **Retrieval, Execution, Images No:** consistent with R026 and EV:169 [Not disclosed]. **Monitoring No:** consistent with playbook :46.
- **Refusal-based vs substantive-answer conflict:** shown as a conflict in limits item 5 ("The playbook calls the tests refusal-based, while the test page describes other pass conditions"). The rail 3 "Good to know" gives both sides, with the inference marked "(our reading)", matching EV:96 [Inferred]. PASS. Optionally note that the refusal sentence is only on the staging playbook (EV:3; O10).
- **Kaleidoscope, one mention:** PARTLY. It appears in diagram 4 (one box plus aria-label plus figcaption), again in limits item 8 (repeating the figcaption), and in the footer. The fixes below delete limits item 8 (R5), which leaves one body placement (rail 4) plus the footer. The content also overstates the status: "not yet in Litmus" and "planned, not shipped" contradict the playbook's "Kaleidoscope is a contextual, functional evaluation module within Litmus" (kaleidoscope.md:9) and "which is the contextual evaluation module within Litmus" (litmus.md:17). They also contradict the page's own figcaption ("whether Litmus users can use it today is not disclosed") and INV:28, which records tenant access today as [Not disclosed]. The module itself is shipped as open source ("Try the open-sourced Kaleidoscope module today", kaleidoscope.md:39).
- **Moonshot only as [Inferred] resemblance:** PASS. Rail 4's know says "so Litmus may be modelled on it. No GovTech page says so, and the hosted service may differ." Limits item 3 says "that is our reading, and no GovTech page confirms it". The footer cites it "only for the resemblance note". O8 is a wording polish: the field match is a fact, and only the "modelled on" is our reading.
- **Bench-design wording (R032):** PASS. The page body never says "bench", and it makes no decided bench plans.

## 3. Claim tracing (page → drafts)

Every sentence was traced. Only exceptions and notable points are listed. All other claims trace to EV or INV with the same strength.

| Location | Page text | Draft | Finding |
|---|---|---|---|
| Diagram 4, Kaleidoscope row label (line 474) | "not yet in Litmus" | INV:28 "Whether Litmus tenants can use it today is [Not disclosed]"; playbook calls it a module within Litmus | Overclaim: states as fact something the drafts mark not disclosed and that two GovTech pages contradict (R4). |
| Limits item 8 (line 573) | "Kaleidoscope is planned, not shipped." | EV:27-29, EV:58 (open-sourced module exists; Litmus integration "upcoming months") | Overclaim, and a repeat of the figcaption (R5). |
| Figcaption 4 (line 479) | "GovTech's docs say Litmus is being extended … whether Litmus users can use it today is not disclosed." | EV:27-29, INV:28 | Correct but one-sided. The drafts record the playbook/docs conflict. R5 folds the conflict in here. |
| Limits item 5 (line 570) | "The docs promise a pass or fail for each test" | EV:94 "Results will show pass/fail status for each test case" (verified at source) | Attributed claim reworded: "test case" (unit not defined) became "test" (one of the 14). R7. Elsewhere the page says "per test" in its own voice (O1). |
| Limits item 6 (line 571) | "<b>Test the system your users meet.</b>" | EV:124 (playbook quote); README §1 "does not recommend" | Advice in the page's own voice (R6). |
| Positioning cell, limits item 5, rail 3 | "playbook example prints a refusal rate per category" | EV:57, EV:97, source safety.mdx@45908b48:429-440 | Traces, but the source is not in the footer (R8). |
| Rail 3 figcaption (line 357) | "A pass means the replies met that test's pass condition" | EV:162 "What is the pass or fail rule per test … [Not disclosed]" | Mild: asserts a rule the drafts leave open (O3). |
| Rail 3 know (line 364) | "The tests are a fixed set of curated prompts" | EV:105-107 ("curated"; DAN "variations"); EV:108 | "fixed" is documented for no test except DAN's dataset (O4). |
| Ways-to-start, Custom scenarios (line 376) | "there is no authoring guide" | EV:56 "no authoring guide found" | Absence stated more strongly than checked (O7). |
| Scorecard Dialog (line 549) | mapping of political and advice tests to dialog | EV Datasets rows | Inference without a hedge (O2). |
| Lede, overview, diagram 5 | "before launch" | EV:26 one-pager "automated pre-deployment … testing" | OK. |
| 14-test table | categories, membership of the 6-test suite, pass texts | EV:71-86 | All 14 rows MATCH the draft (Baseline = DAN, Medical, Hateful, Insults, Domestic Affairs, Social Policies). Undesirable-content rows are reordered against the docs order; not a factual issue. |
| Diagram 2 | three registration details, three returns | EV:117, EV:94, EV:14 | MATCH. |
| Ways to start | web app, API, Action, custom | INV:13-16, EV:53-56 | MATCH, including archive date 8 Sep 2026, "not found", staging link "to be verified". |
| Diagram 5 and know | pairing quotes, one interest form, access difference | EV:24-26, EV:124, EV:128; sibling Sentinel cells | MATCH. |
| Limits 1-4, 7 | | EV:15, EV:22-23, EV:34-41, EV:108, EV:169 | MATCH. |

## 4. Spot-checks at source (verbatim, 2026-10-11)

| # | Fact on page | URL | Quote at source | Result |
|---|---|---|---|---|
| 1 | Does not judge usefulness | https://raw.githubusercontent.com/govtech-responsibleai/playbook/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/litmus.md (:17) | "It does not evaluate whether your system does its job well." | MATCH |
| 2 | Not a runtime defence | same (:46) | "Litmus tests a system; it does not defend one at runtime." | MATCH |
| 3 | Designed to be used with Sentinel | same (:46) | "The two are designed to be used together: Litmus identifies which risks your system actually exhibits, and Sentinel mitigates them in production." | MATCH |
| 4 | Endpoint caution | same (:52) | "If guardrails sit in front of your production endpoint but not the tested one, the scores describe a system nobody uses." | MATCH |
| 5 | Refusal-based | same (:53) | "A system that refuses every request may score well on refusal-based safety tests" | MATCH |
| 6 | Trigger modes | same (:25) | "manually from the web application, on a schedule, or from a CI/CD job on each commit or deployment" | MATCH |
| 7 | Public sector, TechPass | same (:57) | "Litmus is available to public sector teams through AI Guardian … signs in with TechPass" | MATCH |
| 8 | Result format | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Getting-Started | "Results will show pass/fail status for each test case" / "Corrective measures and guardrails will be recommended for failing tests" | MATCH (page limits item 5 says "each test": R7) |
| 9 | Web app run, Actions tab, custom testing | same | "choose from compiled Baseline tests in the WebApp and hit "Run Tests""; "results visible under the Actions tab in your repository"; "Custom model testing can be requested at aiguardian@tech.gov.sg" | MATCH |
| 10 | API key from onboarding; three details | same | "API key provided by the AIGuardian team during onboarding"; "URL endpoint for your AI application" | MATCH |
| 11 | Active subscription | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Troubleshooting | "Ensure your account setup is complete and subscription is active" | MATCH |
| 12 | Two suites, 6 and 14, copy text | https://www.aiguardian.gov.sg/docs/wiki/Test-Information-Documentation | "two test suite options … Baseline Tests and Baseline+"; "Baseline Tests consists of 6 key tests"; "Baseline Tests consists of all 14 tests across these four categories" | MATCH |
| 13 | Domestic Affairs refusal wording | same | "to assess whether the model refuses to answer due to potential misinterpretation and misrepresentation" | MATCH |
| 14 | Hundreds of prompts; internal evaluation; multi-tenant | https://www.aiguardian.gov.sg/docs/wiki/Litmus-Overview | "Litmus sends hundreds of curated prompts to the tenant's application"; "automated internal evaluation"; "multi-tenant SaaS service" | MATCH |
| 15 | Proof of concept on one portal page | https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/overview | "PROOF OF CONCEPT" … "Last updated 19 May 2025" | MATCH |
| 16 | Kaleidoscope "upcoming months" | https://govtech-responsibleai.github.io/kaleidoscope/ | "We are extending Litmus to support Kaleidoscope's structured evaluation workflow in the upcoming months." | MATCH |
| 17 | Kaleidoscope status in the playbook | https://raw.githubusercontent.com/govtech-responsibleai/playbook/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/kaleidoscope.md (:9, :39) | "Kaleidoscope is a contextual, functional evaluation module within Litmus." / "Try the open-sourced Kaleidoscope module today, or stay tuned for more updates to access it via Litmus." | MATCH with the drafts; contradicts the page's "not yet in Litmus" (R4) |
| 18 | Sample Action route and fields | https://raw.githubusercontent.com/dsaidgovsg/aiguardian-test-action/190600937062c100d0c10181e3edf71702230244/action.yml (:28, :31-44) | "url: https://litmus.dev.aiguardian.gov.sg/api/v1/benchmarks"; body run_name … runner_processing_module | MATCH |
| 19 | Moonshot DTO same eight fields | https://raw.githubusercontent.com/aiverify-foundation/moonshot/ab4dbbad9177ff8590838071de82079b6d47ad51/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py (:4-13) | run_name, description, endpoints, inputs, num_of_prompts, random_seed, system_prompt, runner_processing_module | MATCH |
| 20 | Playbook refusal-rate example | https://raw.githubusercontent.com/govtech-responsibleai/playbook/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/evaluating-ai-systems/safety.mdx (:429-440) | "returns category-level refusal scores" … "print(category, score.refusal_rate)" | MATCH |

Tally: 20 checked. 20 MATCH (one shows the source supports the drafts and contradicts a page label, see R4), 0 MISMATCH, 0 UNVERIFIABLE. The one-pager PDF quotes were not re-read; P7 checked them.

## 5. URLs (all 16 absolute hrefs in the page, plus 3 relative links)

Each URL was requested twice, plain and with a browser User-Agent (url_check.txt). Not requested: form.gov.sg, litmus.*.aiguardian.gov.sg and /api/ paths (none is linked in the page).

| Status | URL | Classification |
|---|---|---|
| 200 | fonts css2 link; 4 aiguardian docs pages; 4 portal pages; govtech-responsibleai.github.io/kaleidoscope/ | OK |
| 404 | https://fonts.googleapis.com (preconnect href) | Expected. A preconnect origin, not a page; identical on every sibling page. |
| 403 plain / 200 browser UA | one-pager PDF (isomer-user-content…) | Expected per CH 5b |
| 503 (plain, browser UA, fetch_text, 3 retries; one 429) | github.com blob: playbook litmus.md, playbook kaleidoscope.md, aiguardian-test-action action.yml, moonshot benchmark_runner_dto.py | GitHub web serving 503 to this session, the same as P9 (gh_retry.txt). Not broken: the raw.githubusercontent.com equivalents at the same refs return 200, and the content was verified (spot-checks 1-7, 17-19). github.com/govtech-responsibleai/playbook and its tree URL return 200, and the safety.mdx blob returned 200 on retry. |
| exists | nemo-rails-explained.html, llama-guard-explained.html, sentinel-explained.html | OK (relative) |

URL failures: none real. Malformed P9 forms: not present.

## 6. Required fixes

**R1. `<title>` (line 1)**
- Problem: main's P10 ruling and README §8.
- Old: `<title>How GovTech Litmus Tests a Conversation</title>`
- New: `<title>How GovTech Litmus Tests an AI Application</title>`

**R2. h1 (line 122)**
- Problem: the h1 must match the title in sentence case.
- Old: `<h1>How GovTech Litmus tests a conversation</h1>`
- New: `<h1>How GovTech Litmus tests an AI application</h1>`

**R3. Legend, gate role (line 125)**
- Problem: main's P10 ruling.
- Old: `<span><i class="sw gate"></i>Check done by Litmus</span>`
- New: `<span><i class="sw gate"></i>Test run by Litmus</span>`

**R4. Diagram 4, Planned row label (line 474)**
- Problem: "not yet in Litmus" asserts something the drafts mark [Not disclosed] (INV:28). The playbook calls Kaleidoscope "a … module within Litmus".
- Old: `<text class="ts" x="10" y="342">not yet in Litmus</text>`
- New: `<text class="ts" x="10" y="342">Litmus support planned</text>`

**R5. Figcaption 4 (line 479) and limits item 8 (line 573)**
- Problem: show the documented conflict once, and keep Kaleidoscope to one body placement.
- In figcaption 4, old: `GovTech's docs say Litmus is being extended to support it in the upcoming months; whether Litmus users can use it today is not disclosed.`
- New: `GovTech's pages disagree on its status: the playbook calls it a module within Litmus, while the Kaleidoscope docs say Litmus is being extended to support it in the upcoming months. Whether Litmus users can use it today is not disclosed.`
- Delete limits item 8 entirely: `      <li><b>Kaleidoscope is planned, not shipped.</b> It checks whether an application does its job well, not whether it is safe, and GovTech's docs say Litmus will support it in the upcoming months.</li>`
- This leaves 7 items, within README 6-8. If main reads "one mention" as allowing a limits item, keep an item instead, with this text: `<li><b>Kaleidoscope's place in Litmus is unclear.</b> GovTech's playbook calls it a module within Litmus, while the Kaleidoscope docs say Litmus support comes in the upcoming months; whether Litmus users can use it today is not disclosed.</li>`

**R6. Limits item 6 (line 571)**
- Problem: the bold lead is advice in the page's own voice (README §1).
- Old: `<li><b>Test the system your users meet.</b> Results describe whatever address you registered. Whether a guardrail-protected endpoint, such as one behind Sentinel, can be tested is not stated.</li>`
- New: `<li><b>Results describe only the address you registered.</b> GovTech's playbook warns that testing an endpoint other than the production one describes "a system nobody uses". Whether a guardrail-protected endpoint, such as one behind Sentinel, can be tested is not stated.</li>`

**R7. Limits item 5 (line 570)**
- Problem: an attributed docs claim must keep the docs' unit (EV:94).
- Old: `The docs promise a pass or fail for each test, while`
- New: `The docs promise a pass or fail for each test case, while`

**R8. Footer (lines 579-580)**
- Problem: the refusal-rate example (positioning table, rail 3, limits item 5) has no listed source. EV:57 and EV:97 give it.
- In `<p>Sources…`, old: `(the Litmus and Kaleidoscope pages, at one commit)`
- New: `(the Litmus, Kaleidoscope and Safety evals pages, at one commit)`
- In the link list, after `<a href="https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/kaleidoscope.md">Playbook: Kaleidoscope</a>`, insert: ` · <a href="https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/evaluating-ai-systems/safety.mdx">Playbook: Safety evals</a>`

## 7. Optional suggestions

- **O1.** The page says "pass or fail per test" in its own voice (lede, overview box, aria-label and caption, diagram 1, positioning cell, diagram 3 box and caption). The docs say "each test case", and the unit is undefined. Consider "for each test case", or "per test case", in the lede, the positioning cell and diagram 2/3 text. The box text fits: "pass or fail per test case" is about 24 characters at 13px.
- **O2.** Scorecard Dialog Why: append " (our reading)" after "referring users to professionals". This matches the Input row's hedge.
- **O3.** Rail 3 figcaption. Replace "A pass means the replies met that test's pass condition, for example that the application refused; the docs give no score, threshold or sample report." with "The test page describes in words what a pass looks like, for example that the application refused; how a pass is decided, and any score, threshold or sample report, is not published." (EV:96, EV:162)
- **O4.** Rail 3 know. "The tests are a fixed set of curated prompts" → "The tests use curated prompts".
- **O5.** Add a Planned swatch, as the cloak page does. In Additions: `.sw.plan { background: var(--bg); border-color: var(--line); border-style: dashed; }`. In the legend: `<span><i class="sw plan"></i>Planned</span>`.
- **O6.** Keep the sibling "Edits text" row with a Litmus cell "No", so the positioning table stays comparable with the Sentinel page (cells copied word for word).
- **O7.** Ways to start, Custom scenarios. "A request; there is no authoring guide" → "A request; no authoring guide is published".
- **O8.** Limits item 3. "A sample Action resembles Moonshot's web API, but that is our reading, and no GovTech page confirms it." → "A sample Action's request matches Moonshot's web API; that Litmus is built on Moonshot is our reading, and no GovTech page confirms it."
- **O9.** The legend's dev swatch is drawn blue-dashed (`.sw.dev`), while the dev boxes are grey-dashed `box dev`. The same mismatch exists on the modelarmor and purplellama pages. Leave as is unless all pages change together.
- **O10.** Limits item 5: optionally add "(on the playbook's staging pages)" after "refusal-based". EV:3 records that the production page words it differently.

## QUESTIONS

- **Q1 (main).** Does "Kaleidoscope one mention" mean one body placement (rail 4 box and caption) and allow a footer source line? R5 assumes yes and deletes limits item 8. If a limits item is wanted, R5 gives replacement text.
- **Q2 (main).** O1 (test vs test case) is optional because the per-test "Outcome" texts imply a per-test pass condition. Main may want to raise it to required for consistency with R7.
