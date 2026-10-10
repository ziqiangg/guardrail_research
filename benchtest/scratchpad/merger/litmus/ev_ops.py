import re
from lib import Doc

B = "benchtest/drafts/"
ev = Doc(B + "litmus_eval_tooling.md", "EV")
PBL = "**[Documented: repo govtech-responsibleai/playbook@45908b48]**"
D = "**[Documented]**"
ND = "**[Not disclosed]**"
INF = "**[Inferred]**"
TBV = "**[To be verified]**"

# ---------------------------------------------------------------- title / Version scope (unparsed)
ev.replace(1, "## Topic: GovTech Litmus evaluation tooling (reuse assessment for the test bench)",
           "Title (EV:1)", "style", "'draft,' removed from the title; finals are not drafts (T62)")

ev.sub(3, "AI Guardian docs pages (Docusaurus site, source repository not located)",
       "AI Guardian docs pages (Docusaurus v3.10.0 per the page's generator tag, deployed 2026-10-08 08:42 UTC per the Last-Modified header, the same for every page; no edit link or source repository found in the pages or in a GitHub repository search of the dsaidgovsg and govtech-responsibleai organisations)",
       "Version scope (EV:3)", "edit", "T8: docs pages stay unpinned; evidence for the absence of a source repository stated")
ev.sub(3, "(full SHA 45908b48c0a8b6d3855a154c0e41a12958a99205, committed 2026-09-14; the pinned `website/docs/tools/litmus.md` matches the live page text, which carries \"Last updated on Sep 14, 2026\").",
       "(full SHA 45908b48c0a8b6d3855a154c0e41a12958a99205, committed 2026-09-14). The repository README lists two deployments, staging (govtech-responsibleai.github.io/playbook, built from staging) and production (playbooks.aip.gov.sg/responsibleai, built from main); the pinned Litmus, Kaleidoscope, Safety evals and WOG safety testing pages match the staging site, and the production pages carry the same statements cited here except the refusal sentence in tools/litmus.md line 53.",
       "Version scope (EV:3)", "edit", "A1 (CORRECTION): the pinned branch is the staging deployment; production-versus-staging note per main P5 ruling")
ev.sub(3, "nothing was signed in to, submitted or called (R019).", "nothing was signed in to, submitted or called.",
       "Version scope (EV:3)", "style", "T59: ruling id removed from the text")

# ---------------------------------------------------------------- Overview
ev.replace(6, "Summary: **Litmus is a hosted testing service for AI applications, not a runtime defence.** It scores an application's responses to curated prompts, from a web app or CI/CD. It is available to public sector teams; a May 2025 portal page labels it proof of concept. **[Documented]**",
           "Overview Summary (EV:6)", "summary",
           "T20 + T4 + T21 (main P5 ruling): resolver's RECOMMENDED text with eligibility and proof-of-concept qualifiers; 'not a guardrail' and 'before launch' dropped (44 words excluding the label)")

ev.replace(15, [
    "• Litmus tests a system and is not a runtime defence: \"Litmus tests a system; it does not defend one at runtime.\" (PB tools/litmus.md@45908b48:46) " + PBL,
    "• The playbook adds that Litmus \"does not evaluate whether your system does its job well\" (PB tools/litmus.md@45908b48:17) " + PBL],
    "Overview, bullet 'Litmus tests a system' (EV:15)", "replace",
    "T20: split into two one-fact bullets; second quote is on line 17; locators in file@ref:line form (T11)")
ev.after(15, "• Runs can be triggered \"manually from the web application, on a schedule, or from a CI/CD job on each commit or deployment\" (PB tools/litmus.md@45908b48:25) " + PBL,
         "Overview, after EV:15", "T20: backs 'from a web app or CI/CD' in the Summary and removes the 'before launch' reading")

ev.replace(16, "• Direction: Litmus is not an inline guardrail. It sends prompts to a tenant endpoint and judges the application's responses, so it has no input-level or output-level function " + INF + " (premise: Overview steps 2 and 3 describe prompts going out and responses being scored; the playbook sentence \"Litmus tests a system; it does not defend one at runtime\")",
           "Overview, direction bullet (EV:16)", "replace", "T20 + T59: ruling id (R002) and 'in this draft' removed")

ev.after(17, "• The Kaleidoscope documentation calls Litmus \"AI Guardian’s testing and evaluation platform for Whole-of-Government AI products\" (https://govtech-responsibleai.github.io/kaleidoscope/, read 2026-10-10) " + D,
         "Overview, after EV:17", "T4: audience statement from the Kaleidoscope docs")

ev.sub(18, "the form was not opened, R019)", "the form was not opened)", "Overview, interest-form bullet (EV:18)", "style",
       "T59: ruling id removed")

ev.replace(20, "• Status, source two (conflict C4, not resolved): the docs Overview, Getting Started and Troubleshooting pages, the docs home page, the AI Guardian home page, the one-pager and the playbook Litmus page give no maturity label for Litmus (checked all of them) " + ND,
           "Overview, status source two (EV:20)", "replace", "T21 + T22: checked list widened; Sentinel clause dropped (one fact per bullet)")

ev.sub(23, "(a \"Global Overview Document\", dated by its file name 20250916)",
       "(titled \"AI Guardian: Litmus & Sentinel Global Overview Document\"; created 2025-09-16 per the PDF metadata, the same date as the file name)",
       "Overview, one-pager bullet (EV:23)", "edit", "T10: provenance from the PDF itself")
ev.sub(23, "text read with pdftotext)", "text read with pdftotext and checked with a second extractor)",
       "Overview, one-pager bullet (EV:23)", "edit", "T10: second extraction (pypdf) found all nine phrases")

ev.replace(24, [
    "• Kaleidoscope, playbook Litmus page: \"Kaleidoscope, which is the contextual evaluation module within Litmus\" (PB tools/litmus.md@45908b48:17) " + PBL,
    "• Kaleidoscope, conflict C12, playbook Kaleidoscope page: \"Try the open-sourced Kaleidoscope module today, or stay tuned for more updates to access it via Litmus.\" (PB tools/kaleidoscope.md@45908b48:39) " + PBL],
    "Overview, Kaleidoscope playbook-side bullet (EV:24)", "replace",
    "T32: split into the two playbook statements that differ; the 'stay tuned' quote added")

ev.replace(26, [
    "• Alignment, conflict C9 first side: the docs Overview says \"aligned with public sector AI ethics, policies, and National AI Group (NAIG) guidelines\" (DOCS Litmus-Overview) " + D,
    "• Alignment, conflict C9 second side: the docs home page and the AI Guardian home page say \"aligned with public sector AI ethics, policies, and guidelines\", without NAIG (https://www.aiguardian.gov.sg/docs/ and https://www.aiguardian.gov.sg/) " + D],
    "Overview, alignment bullet (EV:26)", "replace", "T23: one fact per bullet; AI Guardian home page added as a second source of the shorter wording")

ev.after(27, "• No licence or reuse statement was found for the quoted GovTech material: the playbook repository at 45908b48 has no LICENSE file and its README and CONTRIBUTING name none, and the sample Action repository holds only action.yml (checked the docs, portal and one-pager footers, the playbook and the Action repository) " + ND,
         "Overview, after EV:27 (owner)", "T5: licence of the quoted material (class c; absence)")

ev.replace(28, [
    "• Evaluator or judge and backing model: not published; the Overview says only \"automated internal evaluation\" (checked DOCS Overview, Getting Started, Troubleshooting and Test Information Documentation, the five PORTAL pages, the one-pager, the playbook Litmus page, ACT, and a GitHub search of the two GovTech organisations) " + ND,
    "• Test dataset size, provenance and licence: not published (checked the same pages; the Overview says only \"hundreds of curated prompts\") " + ND,
    "• The developer portal Terms of Use say \"The featured products and services are subject to separate terms of use.\" (https://www.developer.tech.gov.sg/terms-of-use, read 2026-10-10) " + D,
    "• No separate Litmus terms, pricing, quota or service-level statement is published (checked the PORTAL Terms of Use and Privacy Statement, the DOCS pages and footers, the AI Guardian home page, the one-pager and the playbook Litmus page) " + ND,
    "• Data handling and retention: not published beyond \"Tenants can access the report directly from Litmus to analyse trends and make comparisons\" (checked the same pages, the PORTAL Terms of Use and Privacy Statement) " + ND],
    "Overview, 'No model, judge ...' bullet (EV:28)", "replace",
    "T22 + T3: one bullet with six absences split into separate bullets, each with its own checked list; the Terms clause is its own [Documented] bullet (one label per fact)")

ev.replace(29, [
    "• No public repository for the Action name the docs give: `git ls-remote https://github.com/dsaidgovsg/aiguardian-litmus-test` returns \"Repository not found\" and the github.com page returns HTTP 404 (both observed 2026-10-10; a private repository would answer the same way) " + D,
    "• No open-source Litmus server or client was found: a GitHub repository search (name, description and README) of the `dsaidgovsg` organisation for \"litmus\" returns only the archived sample Action, and the `govtech-responsibleai` organisation (11 repositories) has none (checked 2026-10-10) " + ND],
    "Overview, 'No open-source Litmus' bullet (EV:29)", "replace",
    "T17 + T18 + T22: the HTTP facts become a [Documented] bullet; the repository search is a separate [Not disclosed] bullet naming the method")

ev.after(30, [
    "• Two Litmus addresses return HTTP 403 AccessDenied (Server AmazonS3, X-Cache \"Error from cloudfront\"): https://www.aiguardian.gov.sg/litmus and https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide (observed 2026-10-10); the PORTAL Getting Started and Resources pages link the second one " + D,
    "• A made-up path under /docs/wiki/ returns the same 403, while /docs/wiki/Litmus-Overview returns 200 (observed 2026-10-10) " + D,
    "• Those two addresses are most likely not published at those paths " + INF + " (premise: the made-up path returns the identical 403, and the docs sidebar lists only four Litmus pages)",
    "• No archived copy of either address: the Internet Archive availability API returned no snapshot and its CDX index no rows (checked 2026-10-10; control: one capture of Litmus-Getting-Started on 2026-05-13) " + D],
    "Overview, after EV:30 (four new bullets)", "T14 + T13: HTTP facts moved from Open questions to Detail as [Documented]; the conclusion stays [Inferred] with its premise; Wayback scope narrowed; Sentinel wiki path dropped")

# ---------------------------------------------------------------- Tools
ev.sub(34, "Litmus has no Table 3 column (R003).", "Litmus has no Table 3 column.", "Tools note (EV:34)", "style", "T59: ruling id removed")
ev.sub(34, "DOCS, PORTAL, PB, ACT and MS are defined in the Version scope line.",
       "DOCS = the AI Guardian docs at https://www.aiguardian.gov.sg/docs/wiki/; PORTAL = https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/; PB = playbook files at 45908b48 under https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/; ACT = the sample Action action.yml at v0.0.1; MS = AI Verify Foundation, not a GovTech source.",
       "Tools note (EV:34)", "edit", "T60: legend in a parsed note so it reaches the sheet")
ev.sub(34, "its repository was not researched.",
       "its repository was not researched. Table 3 headers named: GovTech Sentinel: Prompt-attack detection; GovTech Sentinel: Localised harmful-content classification (LionGuard 2); LionGuard: Localised harmful-content classification.",
       "Tools note (EV:34)", "add", "T30: the exact headers named in the Evaluates cell of row 1 are listed in the note")

ev.sub(38, "A possible reuse: the test themes could serve as a reference list when planning tests for GovTech Sentinel: Prompt-attack detection (the DoAnythingNow jailbreak test) and GovTech Sentinel: Localised harmful-content classification (LionGuard 2) (the hateful, insults, sexual, physical violence, self-harm and all other misconduct tests) [Inferred] (premise: the test names equal the threat themes and harm category names of those columns).",
       "A possible reuse: the six Undesirable Content test names (Hateful, Insults, Sexual, Physical Violence, Self-Harm, All Other Misconduct) equal the harm categories of the two harmful-content columns named in the note, and the DoAnythingNow jailbreak test could line up with the prompt-attack column [Inferred] (premise: the test names equal the threat themes and harm category names of those columns).",
       "Tools row 1 (Litmus web app), Evaluates cell (EV:38)", "replace",
       "T30: prose with two Sentinel headers inside replaced; headers listed in the note; LionGuard column named")

# row 2 Litmus API
ev.sub(39, "(not called) [Documented]. The route /api/v1/benchmarks and a request body appear only in the sample Action (ACT line 28 and lines 31 to 45)",
       "(link target read from the page HTML with curl and the Python standard-library parser, 2026-10-10; not called) [Documented]. The route /api/v1/benchmarks and a request body appear only in the sample Action (ACT:28 and ACT:31-44)",
       "Tools row 2 (Litmus API), Inputs cell (EV:39)", "edit", "T9 (triage location EV:39) + T11: link-target method named; locators in file@ref:line form")
ev.sub(39, "| Not disclosed [Not disclosed]. | [Not disclosed]; the sample Action",
       "| [Not disclosed] (see Engine coverage). | [Not disclosed]; the sample Action",
       "Tools row 2, Judge cell (EV:39)", "style", "T61: repeated absence points to Engine coverage")

# row 3 CI/CD
ev.sub(40, "That repository returns \"Repository not found\" (observed 2026-10-10) [Documented].",
       "That repository returns \"Repository not found\" and HTTP 404 on github.com (observed 2026-10-10) [Documented].",
       "Tools row 3 (CI/CD), Inputs cell (EV:40)", "edit", "T18: both methods for one fact stated alike in all places")
ev.sub(40, "(conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1].",
       "(conflict C2) [Documented: repo dsaidgovsg/aiguardian-test-action@v0.0.1]. The step is headed \"Push Changes to GitHub/Gitlab\" while the text and the example are GitHub only (conflict C18) [Documented].",
       "Tools row 3, Inputs cell (EV:40)", "add", "T26: platform wording conflict recorded in the eval sheet (the inventory already carried it)")
ev.sub(40, "| Not disclosed [Not disclosed]. | [Not disclosed]. | DOCS",
       "| [Not disclosed] (see Engine coverage). | [Not disclosed] (see Engine coverage). | DOCS",
       "Tools row 3, Judge and Engine cells (EV:40)", "style", "T61")
ev.sub(41, "| Not disclosed [Not disclosed]. | [Not disclosed]. | DOCS",
       "| [Not disclosed] (see Engine coverage). | [Not disclosed] (see Engine coverage). | DOCS",
       "Tools row 4 (custom scenarios), Judge and Engine cells (EV:41)", "style", "T61")

# row 5 LitmusClient
ev.sub(42, "Playbook LitmusClient Python example (illustrative)", "Playbook LitmusClient Python example (Code example tab)",
       "Tools row 5, Tool cell (EV:42)", "edit", "T28: 'illustrative' was the drafter's word; the page labels the tab 'Litmus' under 'Code example'")
ev.sub(42, "The code comment says it \"returns category-level refusal scores\" (conflict C8 with the docs' pass/fail per test case)",
       "The code comment (safety.mdx@45908b48:429-430) says it \"returns category-level refusal scores\" (conflict C8 with the docs' pass/fail per test case)",
       "Tools row 5, Evaluates cell (EV:42)", "edit", "T11: comment lines located")
ev.sub(42, "(safety.mdx lines 432 to 437)", "(safety.mdx@45908b48:432-438)", "Tools row 5, Inputs cell (EV:42)", "edit", "T11: locator corrected to file@ref:line")
ev.sub(42, "(safety.mdx line 440)", "(safety.mdx@45908b48:440)", "Tools row 5, Outputs cell (EV:42)", "edit", "T11: locator form")
ev.sub(42, "| Not disclosed. | [Not disclosed]. | https://github.com",
       "| [Not disclosed] (see Engine coverage). | [Not disclosed] (see Engine coverage). | https://github.com",
       "Tools row 5, Judge and Engine cells (EV:42)", "style", "T61")

# row 6 Kaleidoscope
ev.sub(43, "Yes: LLM judges, kept only when reliable [Documented: repo govtech-responsibleai/playbook@45908b48]",
       "Yes: LLM judges \"calibrated against human annotations\"; \"Only reliable judges are kept for wider scoring\" [Documented: repo govtech-responsibleai/playbook@45908b48]",
       "Tools row 6 (Kaleidoscope), Judge cell (EV:43)", "replace", "T31: paraphrase replaced by the page's own words")
ev.sub(43, "no tags; not researched here)", "no tags; its licence and code were not read, GovTech pages only)",
       "Tools row 6, Engine cell (EV:43)", "edit", "T6 (R038): licence of the Kaleidoscope repository not researched, stated as such")
ev.after(43, ["", "Judge needed and Engine cells: the evaluator and the scoring engine are not published for any Litmus row (see Engine coverage)."],
         "Tools, note after the table", "T61: one note replaces the repeated 'Not disclosed [Not disclosed]' cells")

# ---------------------------------------------------------------- Datasets
ev.sub(47, "Typo (conflict C5): the Baseline+ introduction says \"Baseline Tests consists of all 14 tests\"; the heading and the table show Baseline+ with 14 tests [Documented].",
       "Wording (conflict C5): under the Baseline+ heading the page says \"Baseline Tests consists of all 14 tests across these four categories\"; the heading and the 14-row table show Baseline+ [Documented]. That this is a copy error is [Inferred] (premise: the Baseline Tests table has 6 rows).",
       "Datasets note (EV:47)", "replace", "T42: 'typo' was an inference; page text stated plainly, reading labelled [Inferred]")
ev.after(47, [
    "• Taxonomy, docs test page (primary, most detailed): four categories Security, Specialised Advice, Undesirable Content and Political Content, with 14 tests (DOCS Test-Information-Documentation) " + D,
    "• Taxonomy, conflict C1, developer portal: \"Litmus uses four main categories of tests\", headed Security Tests, Undesirability Tests, Specialised Advice Tests and Political Tests (PORTAL how-it-works, last updated 13 May 2025) " + D,
    "• Taxonomy, conflict C1, one-pager: test suites \"across safety domains (toxicity, bias, misinformation, robustness)\" (one-pager section 3) " + D],
    "Datasets, three standalone bullets after the note", "T41: the three taxonomies written side by side in the eval sheet (they were an Open question only)")

ev.sub(51, "Baseline Tests (suite; suite id aiguardian-baseline-tests)", "Baseline Tests (suite)", "Datasets row 1 (Baseline Tests), Dataset cell (EV:51)", "edit",
       "T35: the id-to-suite mapping is not stated by any page, so it leaves the name cell")
ev.sub(51, "The Getting Started table says \"Use aiguardian-baseline-tests for our baseline tests\".",
       "The Getting Started table says \"Use aiguardian-baseline-tests for our baseline tests\" [Documented]; that this id selects this 6-test suite is [Inferred] (premise: the id and the suite name both say baseline; no page links them).",
       "Datasets row 1, Contents cell (EV:51)", "edit", "T35: same label as the inventory (id mapping [Inferred])")
ev.sub(51, "| [Documented]; size, licence, origin [Not disclosed] |", "| [Documented]; id-to-suite mapping [Inferred]; size, licence, origin [Not disclosed] |",
       "Datasets row 1, Label cell (EV:51)", "edit", "T35")

# 14 test rows: look-alike brackets
n_t43 = 0
for n in range(53, 67):
    ev.rsub(n, r"\| \[(Security|Specialised Advice|Undesirable Content|Political Content)\] ", r"| Category: \1. ",
            "Datasets row (EV:%d), Contents cell" % n, "hygiene", "T43: look-alike bracket prefix replaced by 'Category: X.'")
    n_t43 += 1
ev.sub(64, "The description says the test checks whether the model \"refuses to answer\", while the Outcome column says success is a model that \"maintains a neutral stance\"; both are on the page.",
       "Description, conflict C13: the test assesses \"whether the model refuses to answer due to potential misinterpretation and misrepresentation\" [Documented]. Outcome: success is a model that \"maintains a neutral stance, presents information factually, and avoids partisan bias or inflammatory rhetoric\" [Documented].",
       "Datasets row 12 (Domestic Affairs), Contents cell (EV:64)", "replace", "T39: both sides quoted in full, each labelled")

# ---------------------------------------------------------------- Published results
ev.sub(75, "(dated by file name, 2025-09-16)", "(created 2025-09-16 per the PDF metadata)", "Published results row 2 (one-pager), Conditions cell (EV:75)", "edit", "T10")
ev.sub(76, "playbook page). | Test Information Documentation, \"Outcome\" column",
       "playbook page). Conflict C14: the playbook warns that \"A system that refuses every request may score well on refusal-based safety tests\" (PB tools/litmus.md@45908b48:53) [Documented: repo govtech-responsibleai/playbook@45908b48]; its production page says \"A system that refuses everything scores well on safety suites while being unusable\" (playbooks.aip.gov.sg, read 2026-10-10) [Documented]; the test page requires substantive answers for Medical, Financial, Legal, Geopolitics and Social Policies [Documented]; a blanket refusal would not meet those pass conditions [Inferred] (premise: the Outcome texts name information the application must give). | Test Information Documentation, \"Outcome\" column",
       "Published results row 3 (per-test pass condition), Numbers cell (EV:76)", "add", "T40: the playbook's refusal-based wording set beside the test-page pass conditions, both playbook deployments quoted")
ev.sub(77, "| [To be verified] (premise for doubt: no Litmus page shows this output; the example is a code sample) |",
       "| Code and comment [Documented: repo govtech-responsibleai/playbook@45908b48]; that Litmus returns this output [To be verified] (premise for doubt: no Litmus page shows it; see Tools row 5) |",
       "Published results row 4 (category-level refusal scores), Label cell (EV:77)", "replace", "T46: one label per thing")
ev.sub(77, "Illustrative code in the playbook Safety evals page, tab Litmus", "Code example in the playbook Safety evals page, tab Litmus",
       "Published results row 4, Conditions cell (EV:77)", "edit", "T28: 'illustrative' was the drafter's word, the page gives no such label")
ev.sub(78, "the playbook calls Litmus tests \"refusal-based\"", "the playbook calls safety tests \"refusal-based\" on its staging page",
       "Published results row 5 (ASR), Label cell (EV:78)", "edit", "T40: the 'refusal-based' sentence is on the staging page only")

# ---------------------------------------------------------------- Red-teaming
ev.replace(89, [
    "• \"Custom scenarios\" and \"user simulation\" exist as feature names: \"Custom workflow and user simulation | Design tailored test cases that simulate real user interactions and end-to-end workflows\" (PORTAL features-roadmap, last updated 06 May 2025) " + D,
    "• How custom scenarios and user simulation work is not described (checked the Litmus Overview, Getting Started, Troubleshooting, the five PORTAL pages, the one-pager and the playbook Litmus page) " + ND],
    "Red-teaming, custom scenarios bullet (EV:89)", "replace", "T48: quote [Documented] and absence [Not disclosed] split")

# ---------------------------------------------------------------- Engine coverage
ev.replace(94, "Summary: **Litmus tests an application endpoint over HTTP; its scoring engine is not disclosed.** Setup needs an endpoint, an API key and a parameter specification. No list of supported models or guardrails, no judge model, and no support statement for guardrailed endpoints is published. **[Not disclosed]**",
           "Engine coverage Summary (EV:94)", "summary",
           "T51 + T50 (main P5 ruling: resolver's new text): 'over HTTP' now backed by a Detail bullet; 'no statement on guardrailed endpoints' narrowed to 'no support statement' because the playbook speaks to guardrails in front of the tested endpoint (43 words excluding the label)")
ev.replace(97, "• The Getting Started example is a `curl` request with a `Content-Type: application/json` header, an `x-api-key` header and a JSON body with the fields `question`, `topic` (empty list) and `history` (empty list) (DOCS Litmus-Getting-Started, step 2) " + D,
           "Engine coverage, example request bullet (EV:97)", "replace", "T51: the bullet now carries the HTTP fact")
ev.after(97, [
    "• The Getting Started page names an API key twice: step 2 lists \"API key for authentication\" among the tenant's application details (the `x-api-key` header of the example), and the parameter table describes `api_key` as \"API key provided by the AIGuardian team during onboarding\" (conflict C20) " + D,
    "• The two keys are different keys, the application's and Litmus's " + INF + " (premise: one is supplied by the tenant, the other issued by the AIGuardian team)"],
    "Engine coverage, after EV:97 (two bullets)", "T49: two API keys under one name written side by side; the reading is [Inferred]")
ev.after(102, [
    "• Playbook on Sentinel and testing: \"A guardrail in front of a system does not tell you what the system does without it. Test the system as well as defending it.\" (PB tools/sentinel.md@45908b48:95) " + PBL,
    "• A guardrail-fronted production endpoint is the intended test target " + INF + " (premise: the playbook warns against testing an endpoint without the production guardrails, PB tools/litmus.md@45908b48:52)"],
    "Engine coverage, after EV:102 (two bullets)", "T50: the two adjacent documented statements and the reading drawn from them")
ev.replace(103, "• An explicit statement that a guardrailed (for example Sentinel-protected) endpoint can be registered and tested, and how its blocks are scored, is not published (checked the Sentinel Overview and getting-started docs pages, the playbook Sentinel and Litmus pages and the Sentinel sheet text) " + ND,
           "Engine coverage, guardrailed-endpoint bullet (EV:103)", "replace", "T50: checked list widened")
ev.sub(105, "(action.yml line 28)", "(action.yml@190600937062:28)", "Engine coverage, sample Action bullet (EV:105)", "edit", "T11: locator form")
ev.sub(105, "(lines 31 to 45; code read, not run)", "(action.yml@190600937062:31-44, headers at 45; code read, not run)",
       "Engine coverage, sample Action bullet (EV:105)", "edit", "T11: the JSON body is lines 31-44, headers line 45")
ev.replace(106, [
    "• Moonshot fact, MS at tag 0.4.11 (2024-10-25, the last tag before the sample Action commit of 2024-10-29; AI Verify Foundation repo, not a GovTech source): `BenchmarkRunnerDTO` has the same eight fields `run_name`, `description`, `endpoints`, `inputs`, `num_of_prompts`, `random_seed`, `system_prompt`, `runner_processing_module` (benchmark_runner_dto.py@0.4.11:4-13) and the route file declares `@router.post(\"/api/v1/benchmarks\")` (routes/benchmark.py@0.4.11:14) (code read, not run) **[Documented: repo aiverify-foundation/moonshot@0.4.11]** https://github.com/aiverify-foundation/moonshot/blob/ab4dbbad9177ff8590838071de82079b6d47ad51/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py",
    "• Moonshot fact, MS at tag 0.5.0 (2024-12-10): the same DTO file text as 0.4.11 and 0.4.0 (code read, not run) **[Documented: repo aiverify-foundation/moonshot@0.5.0]** https://github.com/aiverify-foundation/moonshot/blob/f1b816c0bdb26051bea8890d5ff73b460b3efe33/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py",
    "• Moonshot fact, MS at tag 0.7.6 (latest tag, 2026-02-05): the route takes a required `type` of `BenchmarkCollectionType` with values \"cookbook\" and \"recipe\" (types/types.py@0.7.6:74-76), and the DTO replaces `num_of_prompts` with `prompt_selection_percentage` (benchmark_runner_dto.py@0.7.6:10) (code read, not run) **[Documented: repo aiverify-foundation/moonshot@0.7.6]** https://github.com/aiverify-foundation/moonshot/blob/03e9344dc9fc949ae05b1f38580611fce36528ab/moonshot/integrations/web_api/types/types.py"],
    "Engine coverage, Moonshot tag bullets (EV:106-108)", "replace",
    "T12 + T11: tag 0.4.11 (the tag in force at the sample Action commit) replaces 0.4.0; 0.5.0 shortened; 0.7.6 locator corrected (line 10, not 11); file@ref:line locators")
ev.delete(107, "Engine coverage, Moonshot tag 0.4.0 bullet (EV:107)", "T12: replaced by the 0.4.11 bullet above (DTO file byte-identical at 0.4.0, 0.4.11 and 0.5.0)")
ev.delete(108, "Engine coverage, Moonshot tag 0.7.6 bullet (EV:108)", "T12: merged into the three-bullet replacement at EV:106")
ev.after(108, "• Licence of the cited code: Apache License 2.0 (LICENSE.md at 0.7.6; the same text at 0.5.0 and 0.4.11; AI Verify Foundation repo, not a GovTech source) **[Documented: repo aiverify-foundation/moonshot@0.7.6]** https://github.com/aiverify-foundation/moonshot/blob/03e9344dc9fc949ae05b1f38580611fce36528ab/LICENSE.md",
         "Engine coverage, after the Moonshot tag bullets", "T7: licence of the cited third-party repository (R019)")
ev.sub(109, "(premise: the matches in the three bullets above;", "(premise: the matches in the sample Action bullet and the Moonshot tag bullets above;",
       "Engine coverage, possible-link bullet (EV:109)", "style", "reference to 'the three bullets above' kept true after the new licence bullet was inserted between")
ev.after(109, "• Name resemblance only: moonshot-data@0.7.6 has the recipe `jailbreak-dan` (\"assesses whether the system will be jailbroken using the common jailbreak methods\") and a cookbook named \"Undesirable Content\" (AI Verify Foundation repo, not a GovTech source) **[Documented: repo aiverify-foundation/moonshot-data@0.7.6]** https://github.com/aiverify-foundation/moonshot-data/blob/30fac12375476ac1eb9f47e5872ea5d379c1aa4c/cookbooks/undesirable-content.json",
         "Engine coverage, after EV:109", "T53: name resemblances with AI Verify data, no GovTech statement links them")
ev.sub(110, "(checked the docs, portal, playbook, one-pager, sample Action and the two GovTech GitHub organisations)",
       "(checked the docs, portal, playbook, one-pager, sample Action, a GitHub repository search of the two GovTech organisations on 2026-10-10, and the Moonshot and AI Verify Foundation pages)",
       "Engine coverage, engine bullet (EV:110)", "edit", "T17 + T52: method of the organisation check named; Moonshot and AI Verify pages added")
ev.sub(111, "(PORTAL overview, read 2026-10-10; the staging host; not visited)",
       "(PORTAL overview, read 2026-10-10; link target read from the page HTML with curl and the Python standard-library parser; the staging host; not visited)",
       "Engine coverage, host bullet portal (EV:111)", "edit", "T9: method for link-target facts")
ev.sub(113, "(href in the page HTML; the visible text", "(href in the page HTML read with curl and the Python standard-library parser, 2026-10-10; the visible text",
       "Engine coverage, host bullet Getting Started (EV:113)", "edit", "T9: method for link-target facts")
ev.sub(114, "(action.yml line 28; the development host; not called)", "(action.yml@190600937062:28; the development host; not called)",
       "Engine coverage, host bullet sample Action (EV:114)", "edit", "T11: locator form")
ev.after(114, "• Host conflict C6, AI Guardian home page: the \"Try Litmus Now\" button links `https://litmus.aiguardian.gov.sg/login` (https://www.aiguardian.gov.sg/, link target read from the page HTML, 2026-10-10; not visited) " + D,
         "Engine coverage, after EV:114", "T9 + T54 + T55 (CORRECTION: three hosts in five sources): fifth source of the production host")

# ---------------------------------------------------------------- Reuse
ev.sub(120, "(for example Graphic Content, Race and Religion)", "(by name: Graphic Content and Race & Religion; compared by name only)",
       "Reuse, WOG taxonomy bullet (EV:120)", "edit", "T44: names as the playbook writes them; comparison by name only")
ev.sub(122, "may score well on refusal-based safety tests\".", "may score well on refusal-based safety tests\" (PB tools/litmus.md@45908b48:53).",
       "Reuse, design-cautions bullet (EV:122)", "edit", "T40: the staging quote keeps its locator")
ev.replace(124, "• Litmus is offered to public sector teams through onboarding, so a bench could treat it as a reference and not as a tool it can run " + INF + " (premise: the playbook sentence and Getting Started step 1)",
           "Reuse, onboarding bullet (EV:124)", "replace", "T58 (R032): proposal wording with its premise; 'any run would be a user decision' dropped")

# ---------------------------------------------------------------- Open questions
ev.replace(130, "• Is Litmus built on or compatible with Moonshot (route and body fields match in the sample Action; no GovTech page, and no Moonshot or AI Verify Foundation page checked, says so; the only \"litmus\" in the Moonshot repositories is the English phrase \"litmus test\")? " + ND,
           "Open questions, Moonshot (EV:130)", "replace", "T52: no public source can answer it, so [Not disclosed] replaces [To be verified]")
ev.replace(131, "• Do any of the 14 tests reuse AI Verify cookbooks or datasets (name resemblances only, see Engine coverage; no GovTech page says so)? " + ND,
           "Open questions, AI Verify reuse (EV:131)", "replace", "T53: relabelled; text points to the Engine coverage name-resemblance bullet")
ev.sub(135, "production hosts in the playbook and Getting Started,", "production hosts in the playbook, the Getting Started link and the AI Guardian home page,",
       "Open questions, host (EV:135)", "edit", "T54: the AI Guardian home page also links the production host")
ev.replace(137, "• Does the `LitmusClient` Python example in the playbook exist as a package or API (conflict C7 on the suite name `wog-baseline-v1` against `aiguardian-baseline-tests`)? No GovTech package was found on PyPI under litmus-client, litmusclient, aiguardian or govtech-litmus; a different project named `litmus` (a pytest skeleton generator by another author) holds that name. " + TBV,
           "Open questions, LitmusClient (EV:137)", "replace", "T28: PyPI check recorded; still open")
ev.sub(138, "(checked Getting Started, Overview, Troubleshooting, playbook page)", "(checked Getting Started, Overview, Troubleshooting, the Sentinel docs pages and both playbook pages)",
       "Open questions, guardrailed endpoint (EV:138)", "edit", "T50")
ev.replace(139, "• Who else may use Litmus: the playbook says \"available to public sector teams\", the Kaleidoscope docs say \"for Whole-of-Government AI products\" and the one-pager invites collaboration; no explicit eligibility rule or exclusion is stated (checked the docs, AI Guardian home page, portal pages and Terms of Use, one-pager, playbook)? " + ND,
           "Open questions, eligibility (EV:139)", "replace", "T4")
ev.sub(140, "(checked the docs, portal, one-pager, playbook)", "(checked the docs, portal, the developer portal Terms of Use and Privacy Statement, one-pager, playbook)",
       "Open questions, maturity and terms (EV:140)", "edit", "T3: Terms of Use and Privacy Statement added to the checked list")
ev.sub(143, "**[To be verified]**", ND, "Open questions, Domestic Affairs (EV:143)", "edit", "T39: no source can answer it; [Not disclosed]")
ev.replace(144, "• Can Litmus tenants use Kaleidoscope today, and when will it reach Litmus (the playbook Litmus page calls it a module within Litmus, the Kaleidoscope page says \"stay tuned\", the docs say \"upcoming months\")? " + ND,
           "Open questions, Kaleidoscope (EV:144)", "replace", "T32: one question aligned with the inventory caveat")
ev.delete(145, "Open questions, taxonomy (EV:145)", "T41: the three taxonomies are now Datasets bullets")
ev.delete(146, "Open questions, three 403 pages (EV:146)", "T14: the HTTP facts moved to Overview Detail; Open questions carry only [To be verified] or [Not disclosed]")
ev.replace(147, "• Is the Getting Started page the \"Litmus Onboarding Guide\" that the portal links to? The portal says \"To begin, refer to this onboarding guide.\" and links the unreachable Onboarding Guide address; the live Getting Started page carries the onboarding steps and the playbook says AI Guardian \"carries the current onboarding guide\" (no capture of the guide found)? " + TBV,
           "Open questions, onboarding guide (EV:147)", "replace", "T15: [Inferred] is not an Open-question label (README section 6); relabelled [To be verified]")
ev.after(147, "• Licence of the open-source Kaleidoscope repository and terms of the arXiv paper (not stated on the playbook Kaleidoscope page or the Kaleidoscope docs home; the repository was not read)? " + ND,
         "Open questions, last (new)", "T6: licence of the Kaleidoscope repository (class c, not researched per R038)")

# ---------------------------------------------------------------- Reviewer notes
ev.silent_delete(range(148, 160))
ev._log("Reviewer notes (EV:149-158), 9 notes", "delete", "## Reviewer notes (9 notes)", "(moved to the change log, section 7a)", "T62: README section 7 item 2; finals carry no Reviewer notes")

# ---------------------------------------------------------------- brief conflict ids (process ids) -> plain wording
GEN = [
    ("(conflict C4, not resolved)", "(the sources conflict; not resolved)"),
    ("(conflict C9, minor)", "(a minor difference)"),  # kept for safety; replaced earlier
]
