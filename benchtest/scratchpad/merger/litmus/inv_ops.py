import re
from lib import Doc

B = "benchtest/drafts/"
inv = Doc(B + "litmus_inventory.md", "INV")
PB45 = "[Documented: repo govtech-responsibleai/playbook@45908b48]"
METH = "link target read from the page HTML with curl and the Python standard-library parser, 2026-10-10"

inv.replace(1, "# Litmus inventory (final, sheet 3x)", "Title (INV:1)", "style", "'draft' removed from the title (T62)")

inv.sub(3, "so it has no Table 3 columns (R003) and every Covered by cell carries the inventory-only marker (R011).",
        "so it has no Table 3 columns and every Covered by cell carries the inventory-only marker.",
        "Scope paragraph (INV:3)", "style", "T59: ruling ids removed")
inv.sub(3, "Nothing was signed in to, submitted or called (R019): the web app,", "Nothing was signed in to, submitted or called: the web app,",
        "Scope paragraph (INV:3)", "style", "T59: ruling id removed")

# short-name legend (INV:5)
inv.sub(5, "(the AI Guardian Docusaurus site, no source repository found, unpinned)",
        "(the AI Guardian Docusaurus site, v3.10.0 per the page's generator tag, deployed 2026-10-08 per the Last-Modified header; no edit link or source repository found in the pages or in a GitHub repository search of the dsaidgovsg and govtech-responsibleai organisations; unpinned)",
        "Short-name legend, AIG/DOCS (INV:5)", "edit", "T8: evidence for the absence of a source repository and for the missing pin")
inv.sub(5, "the staging branch commit that matches the deployed page text \"Last updated on Sep 14, 2026\", as for Sentinel R007 item 7)",
        "the staging branch commit, committed 2026-09-14; the README lists two deployments, staging at govtech-responsibleai.github.io/playbook, built from staging, and production at playbooks.aip.gov.sg/responsibleai, built from main; the pinned pages match the staging site, and the production pages carry the same statements cited here except the refusal sentence in tools/litmus.md line 53)",
        "Short-name legend, PB (INV:5)", "edit", "A1 (CORRECTION) + main P5 ruling: staging pin with a production-versus-staging note; T59: 'R007 item 7' removed")
inv.sub(5, "Host names appear in four forms across pages (see the Litmus web app and Litmus API rows); none was visited.",
        "Three hosts (production, staging, development) appear across five sources (see the Litmus web app and Litmus API rows); none was visited.",
        "Short-name legend, hosts (INV:5)", "edit", "T55 (CORRECTION): three hosts in five sources, not 'four forms'")

# (a) intro
inv.sub(9, "because access is by onboarding (a proposal, R032).",
        "because access is by onboarding [Inferred]. Short names in the cells: DOCS = the AI Guardian docs at https://www.aiguardian.gov.sg/docs/wiki/; PORTAL = https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus/; PB = playbook files at 45908b48 under https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/; ACT = the sample Action action.yml at v0.0.1.",
        "Block (a) intro (INV:9)", "edit", "T58 (R032): proposal wording with its label, ruling id removed; T60: legend in the parsed intro so it reaches the sheet")

# ---- (a) row 1 web app
inv.sub(13, "The DEV pages carry a \"Login to Litmus\" link to https://litmus.stg.aiguardian.gov.sg/login [Documented] (link target read from the page, 2026-10-10). Not visited",
        "The DEV pages carry a \"Login to Litmus\" link to https://litmus.stg.aiguardian.gov.sg/login [Documented] (" + METH + "). The AI Guardian home page links \"Try Litmus Now\" to https://litmus.aiguardian.gov.sg/login [Documented] (https://www.aiguardian.gov.sg/, link target read the same way). Not visited",
        "(a) Litmus web app / Host or address (INV:13)", "edit", "T9: method for link-target facts; home-page host added (same fact as the Engine coverage bullet)")
inv.sub(13, "The AIG pages, the one-pager and the playbook describe an onboarding service and give no maturity label [Not disclosed] (checked AIG Overview, Getting Started, Troubleshooting and the playbook page)",
        "The AIG pages, the AI Guardian home page, the one-pager and the playbook describe an onboarding service and give no maturity label [Not disclosed] (checked AIG Overview, Getting Started, Troubleshooting, the docs home page, the AI Guardian home page, the one-pager and the playbook page)",
        "(a) Litmus web app / Status (INV:13)", "edit", "T21: checked list matches the eval sheet (all pages checked, no date or withdrawal of the portal label)")
inv.sub(13, "is [To be verified]: the playbook names litmus.aiguardian.gov.sg and the portal link names litmus.stg.aiguardian.gov.sg. Pricing, quota, terms of use, data handling and retention are [Not disclosed] (checked the AIG pages, the DEV pages and the playbook page)",
        "is [To be verified]: the playbook names litmus.aiguardian.gov.sg, the AI Guardian home page links the same production host, and the portal link names litmus.stg.aiguardian.gov.sg. Pricing, quota, terms of use, data handling and retention are [Not disclosed] (checked the AIG pages, the DEV pages and their Terms of Use and Privacy Statement, and the playbook page)",
        "(a) Litmus web app / Caveats (INV:13)", "edit", "T3 (checked list) + T54 (home page also links the production host)")
inv.replace(13, inv.cur[13].rstrip(" |") + " ; https://www.aiguardian.gov.sg/ |", "(a) Litmus web app / Source URL (INV:13)", "url",
            "T9: the AI Guardian home page is cited for the home-page login link")

# ---- (a) row 2 API
inv.sub(14, "(link target read from the page, 2026-10-10). The sample Action posts", "(" + METH + "). The sample Action posts",
        "(a) Litmus API / Host or address (INV:14)", "edit", "T9: method for link-target facts")

# ---- (a) row 3 CI/CD
inv.sub(15, "returns HTTP 404 on github.com (checked 2026-10-10) [Documented]",
        "returns HTTP 404 on github.com and \"Repository not found\" on git ls-remote (observed 2026-10-10; a private repository would answer the same way) [Documented]",
        "(a) CI/CD integration / Host or address (INV:15)", "edit", "T18: both methods for one fact, worded as in the eval sheet")
inv.sub(15, " ; https://github.com/dsaidgovsg/aiguardian-test-action ; https://github.com/dsaidgovsg/aiguardian-test-action/blob",
        " ; https://github.com/dsaidgovsg/aiguardian-test-action/blob",
        "(a) CI/CD integration / Source URL (INV:15)", "url", "T63: unpinned URL dropped; the pinned action.yml URL stays")

# ---- (a) row 4 onboarding
inv.sub(16, "A public sector team, per the playbook sentence above [Documented: repo govtech-responsibleai/playbook@45908b48]. An explicit eligibility rule for other organisations is [Not disclosed] (checked AIG Overview and Getting Started, DEV Overview and the playbook page).",
        "The playbook states availability for public sector teams, not as a requirement: \"Litmus is available to public sector teams through AI Guardian\" " + PB45 + ". An explicit eligibility rule for other organisations is [Not disclosed] (checked DOCS Overview, Getting Started and home page, PORTAL pages and Terms of Use, the one-pager and the playbook page).",
        "(a) Onboarding and access request / Needs (INV:16)", "replace", "T4 (C15): removes the label mismatch with the eval sheet's eligibility question")
inv.sub(16, "[Documented] (link target read from the page); the DEV Resources page links the same target [Documented]",
        "[Documented] (" + METH + "; not visited); the DEV Resources page links the same target [Documented]",
        "(a) Onboarding and access request / Host or address (INV:16)", "edit", "T9: method for link-target facts")
inv.sub(16, "The three addresses https://www.aiguardian.gov.sg/litmus, https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide and https://www.aiguardian.gov.sg/docs/wiki/Sentinel-Getting-Started return HTTP 403",
        "The two addresses https://www.aiguardian.gov.sg/litmus and https://www.aiguardian.gov.sg/docs/wiki/Litmus-Onboarding-Guide return HTTP 403",
        "(a) Onboarding and access request / Status (INV:16)", "edit", "T14: the Sentinel wiki path is not a Litmus page and is dropped (the real Sentinel page is in the eval sheet)")
inv.sub(16, "The Wayback availability API returned no snapshot for the three addresses (archived_snapshots empty, 2026-10-10) [Documented]",
        "The Wayback availability API returned no snapshot for the two addresses (archived_snapshots empty, 2026-10-10) and its CDX index returned no rows for each (checked 2026-10-10; control: one capture of Litmus-Getting-Started on 2026-05-13) [Documented]",
        "(a) Onboarding and access request / Status (INV:16)", "edit", "T13: CDX result added; scope narrowed to the two addresses")
inv.sub(16, "The three 403 pages most likely do not exist", "The two 403 pages most likely do not exist",
        "(a) Onboarding and access request / Caveats (INV:16)", "edit", "T14")
inv.sub(16, "(checked the AIG pages, the DEV pages, the playbook page and the one-pager)",
        "(checked the AIG pages, the DEV pages and their Terms of Use and Privacy Statement, the playbook page and the one-pager)",
        "(a) Onboarding and access request / Caveats (INV:16)", "edit", "T3: checked list")

# ---- (b)
inv.sub(25, "under the Baseline+ heading, which looks like a copy error [Documented]. That the six Baseline Tests are all among the 14 is read from the two tables and not stated in prose [Inferred] (premise: each of the six test names also appears in the 14-row table)",
        "under the Baseline+ heading [Documented]. A copy error is the likely reading [Inferred] (premise: the Baseline Tests table has 6 rows). Each of the six Baseline Tests names also appears in the 14-row Baseline+ table [Documented] (AIG Test Information Documentation, both tables read 2026-10-10)",
        "(b) Baseline+ / Caveats (INV:25)", "replace", "T42 (copy error is a reading, labelled [Inferred]) + T35 (main P5 ruling: Baseline subset of Baseline+ is [Documented] in both files)")
inv.sub(26, "(website/docs/evaluating-ai-systems/safety.mdx, lines 427 to 440)", "(safety.mdx@45908b48:429-440)",
        "(b) wog-baseline-v1 / Where published (INV:26)", "edit", "T11: locator in file@ref:line form; lines corrected to 429-440")
inv.sub(26, "Illustrative code. No package, client library or API page confirms that LitmusClient or this suite name exists [To be verified].",
        "The page presents it as a code example. No package, client library or API page confirms that LitmusClient or this suite name exists [To be verified] (a PyPI check on 2026-10-10 found no GovTech package under litmus-client, litmusclient, aiguardian or govtech-litmus; a different project named litmus is a pytest skeleton generator by another author).",
        "(b) wog-baseline-v1 / Caveats (INV:26)", "replace", "T28: 'illustrative' was the drafter's word; PyPI check recorded")
inv.sub(26, " ; https://govtech-responsibleai.github.io/playbook/evaluating-ai-systems/safety/ |", " |",
        "(b) wog-baseline-v1 / Source URL (INV:26)", "url", "T63: unpinned duplicate of the pinned safety.mdx URL dropped")
inv.sub(28, "\"Kaleidoscope is a contextual, functional evaluation module within Litmus\" [Documented] (playbook Kaleidoscope page, read 2026-10-10, last updated 25 Jul 2026)",
        "\"Kaleidoscope is a contextual, functional evaluation module within Litmus\" " + PB45 + " (playbook Kaleidoscope page, last updated 25 Jul 2026)",
        "(b) Kaleidoscope / Tests included (INV:28)", "edit", "T63: playbook Kaleidoscope page pinned to 45908b48 (passages matched), repo label")
inv.sub(28, "stay tuned for more updates to access it via Litmus\" [Documented].", "stay tuned for more updates to access it via Litmus\" " + PB45 + ".",
        "(b) Kaleidoscope / Tests included (INV:28)", "edit", "T63: repo label")
inv.sub(28, "the repository was not researched here) [Documented]", "the repository's licence and code were not read, GovTech pages only) [Documented]",
        "(b) Kaleidoscope / Identifier (INV:28)", "edit", "T6 (R038): consistent with the eval sheet")
inv.sub(28, "Whether it is already available to Litmus tenants is [To be verified]:", "Whether Litmus tenants can use it today is [Not disclosed]:",
        "(b) Kaleidoscope / Caveats (INV:28)", "edit", "T32: one question, one label across both files (no source can answer it)")
inv.sub(28, "https://govtech-responsibleai.github.io/playbook/tools/kaleidoscope/ ;",
        "https://github.com/govtech-responsibleai/playbook/blob/45908b48c0a8b6d3855a154c0e41a12958a99205/website/docs/tools/kaleidoscope.md ;",
        "(b) Kaleidoscope / Source URL (INV:28)", "url", "T63: pinned URL replaces the live staging URL")

# ---- (c)
inv.sub(36, "(link target read from the page, 2026-10-10)", "(" + METH + ")", "(c) base_url / Description (INV:36)", "edit", "T9: method for link-target facts")

# ---- global short-name rename AIG->DOCS, DEV->PORTAL
for n in [5, 13, 14, 15, 16, 24, 25, 26, 27, 28, 36, 37, 38, 39, 40, 41]:
    line = inv.cur[n]
    a = len(re.findall(r"\bAIG\b", line))
    d = len(re.findall(r"\bDEV\b", line))
    if a or d:
        line = re.sub(r"\bAIG\b", "DOCS", line)
        line = re.sub(r"\bDEV\b", "PORTAL", line)
        inv.cur[n] = line
        inv._log("INV line %d: short names" % n, "hygiene", "AIG x%d, DEV x%d" % (a, d), "DOCS x%d, PORTAL x%d" % (a, d),
                 "T60: one name set (DOCS, PORTAL, PB, ACT) in both files")

# ---- Reviewer notes
inv.silent_delete(range(42, 52))
inv._log("Reviewer notes (INV:43-50), 6 notes", "delete", "## Reviewer notes (6 notes)", "(moved to the change log, section 7b)", "T62")
