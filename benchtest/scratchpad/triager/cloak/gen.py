import re, collections, sys
sys.path.insert(0, "benchtest/scratchpad/triager/cloak")
from items import GROUPS, TERMS, LOGIN

# assign ids
items = []
for gname, lst in GROUPS:
    for d in lst:
        items.append(dict(d, group=gname))
for n, d in enumerate(items, 1):
    d["id"] = n
key2id = {d["k"]: "T%d" % d["id"] for d in items}
assert len(key2id) == len(items), "duplicate keys"


def sub(s):
    s = s.replace("{TERMS}", TERMS).replace("{LOGIN}", LOGIN)
    def r(m):
        k = m.group(1)
        if k not in key2id:
            raise KeyError(k)
        return key2id[k]
    return re.sub(r"\{([a-z0-9_]+)\}", r, s)


# group ranges
ranges = []
for gname, lst in GROUPS:
    ids = [d["id"] for d in items if d["group"] == gname]
    ranges.append("%s T%d to T%d" % (gname, min(ids), max(ids)))

cls = collections.Counter(d["c"] for d in items)
pri = collections.Counter(d["p"] for d in items)
cp = collections.Counter((d["c"], d["p"]) for d in items)
files = collections.Counter()
for d in items:
    for f in d["f"].split():
        files[f] += 1
cp1 = [key2id[d["k"]] for d in items if d["fl"] == "CP1"]
gap = [key2id[d["k"]] for d in items if d["fl"] == "GAP"]
licc = [key2id[d["k"]] for d in items if d["c"] == "c"]
H = [d for d in items if d["p"] == "H"]
T = lambda k: key2id[k]

out = []
w = out.append
w("# Cloak triage of open evidence items (DRAFT)\n")
w("Sources triaged: `cloak_cols_a.md` (column CK1; 9 rows, 103 Detail bullets in R1 to R7, 14 R8 bullets, 10 Reviewer notes), `cloak_cols_b.md` (columns CK2 and CK3; 96 and 83 Detail bullets in R1 to R7, 14 R8 bullets each, 13 Reviewer notes), `cloak_inventory.md` (sheet 3x draft, 81 rows: (a) 10, (b) 7, (c) 26, (d) 9, (e) 25, (f) 4; 8 Reviewer-note items and a self-check), the brief `cloak_brief.md` (scope, Q01 to Q04, facts to re-verify, conflicts C1 to C9, gaps), rulings R002, R007, R009, R011, R013, R015, R019, R020, R021, R032 (R025 as the terms precedent), and main's cloak rows in `scratchpad/main/queue.md` (header tweaks, Decrypt to CK3 only, planned Sentinel integration row, Inclusion-list placement to reconcile, limit wording stays R8, Terms clauses to class c). No research done; source suggestions only. Nothing here is verified. Written 2026-10-10 by gr-triager. Mechanical checks re-run at the start of this triage: `check_drafts.py columns cloak_cols_a.md` gives 0 errors and 0 warnings (header CK1); `columns cloak_cols_b.md` gives 0 errors and 0 warnings (CK2 and CK3 with main's tweaked headers); `inventory cloak_inventory.md --headers` (a scratch file holding the three tweaked headers) gives 0 errors and 0 warnings (tables 10, 7, 26, 9, 25 and 4 rows).\n")
w("## Legend\n")
w("- File short names: A = cloak_cols_a.md (CK1), B = cloak_cols_b.md (CK2 lines 5-172, CK3 lines 174-318), INV = cloak_inventory.md, BR = cloak_brief.md, queue = `scratchpad/main/queue.md`. Line numbers are as at 2026-10-10 and move when the merger edits (`A:97` = line 97 of cols_a; `INV(e) line 108` = file line 108). Where the file letter is given with a column, `CK2 R6 B:96` means column CK2, row R6, file line 96.")
w("- Location notation: `CKn Rk` = column n, row k (Summary, or Detail bullet by line); `INV(a)` to `INV(f)` = inventory blocks (a) lines 11-20, (b) 28-34, (c) 42-67, (d) 75-83, (e) 91-115, (f) 123-126; `A RN-n` = Reviewer note n of cols_a (10 notes); `B RN-n` = Reviewer note n of cols_b (13 notes); `INV-RN n` = item n of the inventory Reviewer notes (8 items, lines 130-137).")
w("- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; R8 = unlabelled R8 bullet.")
w("- Class: a = answerable from an official page, a pinned repo file, a PDF or a local file, or a drafting fix that needs no research; b = needs testing (stays open) or a CP1 decision item (closes when chosen, NeMo b22 and Presidio precedent); `GAP` = honest gap: closed or undisclosed vendor internals, login-gated pages, plans, or third-party services where no public document is expected to answer; c = licensing, terms or ownership (Terms of Use, Schedules, Privacy Statement, component licences).")
w("- Priority: H = changes an R1 to R7 Summary line, a Summary label, or a headline number that appears in a Summary (here: 17 groups, 0.30, 500 words, \">97% recall\", \"model not named\", the R3 direction statement), or is a CP1 decision that rewrites Summaries; M = Detail level, or only an R8 Summary line (R8 Summaries list questions and are not counted as H, as in the Presidio, Sentinel and LionGuard triage); L = cosmetic or low impact.")
w("- Short source names: GUIDE = Cloak Guide docsify Markdown pages (docs.developer.tech.gov.sg/docs/cloak-guide/sections/*.md), PORTAL = Developer Portal Cloak pages, SITE = www.cloak.gov.sg, TERMS = Terms PDF (24 July 2024), PRIV = Privacy Statement PDF (1 December 2022), DECK = USENIX PEPR 2023 slides (GovTech), PB = playbook page `govtech-responsibleai/playbook` privacy-improvements.mdx at 45908b48, LOGIN = the login redirect for the API Guide, OpenAPI and package guide (HTTP fact, observed 2026-10-10).\n")
w("## Counts\n")
w("Total %d deduplicated items (T1 to T%d), drawn from the 42 R8 bullets (14 per column), the explicit open labels (column bullets R1 to R7: ND 13 in CK1, 12 in CK2, 11 in CK3, TBV 1, INF 11, 14 and 19; raw bracket text including Summaries and Reviewer notes: Documented 215 plus 3 repo-pinned, INF 52, TBV 1, ND 36; inventory: ND 59, TBV 1, INF 39 label mentions), the Reviewer notes (A 10, B 13, INV 8), the brief conflicts C1 to C9, the new points named in the task (Mask prefix and suffix wording, Terms numbering 14 versus 15, LLM limit per dataset versus per project, 500 entries versus words), main's cloak rows in the queue, and a cross-draft comparison of the four files." % (len(items), len(items)))
w("")
w("| Class | Count | of which H |")
w("|---|---|---|")
w("| a doc-answerable (incl. drafting fixes) | %d | %d |" % (cls["a"], cp[("a", "H")]))
w("| b needs testing, honest gap or CP1 decision | %d | %d |" % (cls["b"], cp[("b", "H")]))
w("| c licensing / terms | %d | %d |" % (cls["c"], cp[("c", "H")]))
w("| Total | %d | %d |" % (len(items), pri["H"]))
w("")
w("Priority totals: H %d, M %d, L %d." % (pri["H"], pri["M"], pri["L"]))
w("")
w("Class by priority: a: H %d, M %d, L %d; b: H %d, M %d, L %d; c: H %d, M %d, L %d." % tuple(cp[(c, p)] for c in "abc" for p in "HML"))
w("")
w("Items touching each source file (an item can touch several): cloak_cols_a.md (CK1) %d; cloak_cols_b.md CK2 %d, CK3 %d; cloak_inventory.md %d; brief / rulings / queue %d." % (files["CK1"], files["CK2"], files["CK3"], files["INV"], files["BR"]))
w("")
w("CP1 decision items counted in class b: %d (%s). Honest-gap items (class b, GAP): %d (%s). Licensing (class c) items: %d (%s)." % (len(cp1), ", ".join(cp1), len(gap), ", ".join(gap), len(licc), ", ".join(licc)))
w("")
w("Dedup note: the same open question appears in several rows and columns and is merged into one id with every location: the benchmarking clause (3 R7s, 3 R8s, INV(e), brief) is %s, the direction question (3 R3 Summaries, 3 R8s, INV(b)) is %s, the API schema family (R3, R5, R6, R8 in three columns plus INV(b) and INV(e)) is %s, the 500 limit (CK1 R6, CK2 R6, R8, INV(c), INV(e)) is %s and the LLM limit unit is %s. Items about login-gated pages are grouped as honest gaps rather than one id per page." % (T("t347"), T("dir"), T("apisch"), T("w500"), T("llmlim")))
w("")
w("Provenance note: A RN-8, B RN-10 and INV-RN 7 state that no summarising fetch was used: Cloak Guide pages by curl of the raw Markdown, portal, SITE and Sentinel pages by fetch_text.py, PDFs (TERMS, PRIV, DECK) by pypdf text, the playbook by raw GitHub at the full SHA. Facts that rest on something not read in full: the login-gated API Guide, OpenAPI pages, package guide and decryption helper script (HTTP facts only); the DECK slide 22 layout order (pypdf text layer, see %s); the Terms and Privacy PDFs were read as extracted text, so clause numbers and symbols (the backslash in Schedule 4.6) are as pypdf printed them. The form.gov.sg onboarding form, support links and the Web UI were never opened (R019)." % T("slide"))
w("")
w("Groups (id ranges): " + "; ".join(ranges) + ".\n")

# ---------------- CP1 section
w("## Items for CP1 (decision-bearing for the user)\n")
w("Q01 is the explorer's question carried in the brief (with a drafted default); the CK3 split is new and decision-bearing under R002. The terms item is listed because main routed it to class c and a P5 resolver; it reaches the user only at CP2 or before any bench run (R025 pattern). The prefix `Cloak:` and the CK2 and CK3 header wording were ruled by main and are not user decisions (%s). No bench-design choice is put to the user (R032).\n" % T("hdr"))

w("### CP1-1 Q01 column set (%s)\n" % T("q01"))
w("- Options: (a) three columns CK1 `Cloak: Free-text PII detection and anonymisation`, CK2 `Cloak: Custom entity detection in free text (lists, regex and LLM)`, CK3 `Cloak: Reversible anonymisation and decryption (encrypt and restore)`, free text only (drafted); (b) one column CK1, with custom entities and reversible anonymisation folded in as Detail bullets and inventory rows; (c) inventory only, no Table 3 columns.")
w("- Evidence the choice turns on:")
w("  - Size and shape: R1 to R7 hold 103 bullets in CK1, 96 in CK2 and 83 in CK3, each with its own mechanism and labels (CK2: list, regex and a Beta LLM entity; CK3: AES-256 CBC under managed secrets plus a restore step). Folding into one column would give about 280 bullets minus roughly a dozen repeated limit, access, maintenance and Terms bullets, and each Summary (45 words) would have to cover three functions. CK1 already carries 6 bullets that name a CK2 or CK3 mechanism (A:13, 50, 62, 63, 102, 107), so a fold is a copy and edit.")
w("  - Different dependencies and test inputs: CK2 needs custom lists, regex entities and the Beta LLM entity (1 per dataset, up to 8 hours; regex context words and per-pattern scores are API only); CK3 needs a secret in the Secrets Manager, a decrypt step and, for a sharing test, a second approved account (B:262). CK1 needs only text or files.")
w("  - Precedent and comparability: Presidio has six columns including PD6 custom recognisers and PD3 reversible anonymisation, and Sentinel has seven. Option (a) lines up CK1 with PD1 and PD2, CK2 with PD6 and CK3 with PD3 for sheet 4; under (b) the custom-entity and reversible comparisons sit inside one column.")
w("  - Option (c): CLAUDE.md scope guide puts functions usable on AI prompts or their data path into Table 3; the vendor documents the AI use (\"Anonymise before sending to LLMs\", portal use case, FAQ on GenAI). Login-gated pages and Terms 3.3 and 3.4.7 are access and bench-design matters (R032), not scope; Sentinel columns for closed-beta services are the precedent. Under (c) 73 of 81 Covered-by cells change, the three column drafts become audit trail only, and Cloak drops out of sheet 4 although the brief's objective is which functions can be evaluated together.")
w("  - Costs of (a): about a dozen bullets repeat across columns (file limits, data ceiling, access, maintenance, Terms in R7), and sheet 4 and the Covered-by panel count Cloak up to three times for service-wide rows (19 inventory rows list all three headers). The draft keeps CK2 and CK3 facts in separate, mechanism-named bullets, so (b) stays cheap.")
w("- Recommended default: (a), as drafted (explorer's recommendation and brief default). Choose (b) only if the user prefers one Cloak column for sheet 4; (c) conflicts with the scope guide and rests on access, which R032 keeps out of CP1.\n")

w("### CP1-2 CK3 by direction: anonymise side versus restore side (%s)\n" % T("split"))
w("- Question: under R002, does CK3 need an \"Input-level\" and an \"Output-level\" column (encrypt on the prompt, restore on the reply), or one column?")
w("- Options: (a) one column CK3 (drafted default); (b) split into an input-level encrypt column and an output-level restore column; (c) keep one column now and revisit at CP2 if the API schema, once read by an approved account, shows an input or output flag.")
w("- Evidence:")
w("  - R002's test is the product's own surface: separate rails, endpoints, flags, prompt roles or config sections for input versus output; a library or service that only receives a string is undifferentiated, and a wrapper with per-direction flows keeps its split (NeMo). No public Cloak page shows an input or output flag; the API schema is login-gated (%s), so the flag's absence in the API is [Not disclosed], not documented." % T("dir"))
w("  - What the public pages do show is a split by operation, not by direction: Encrypt is a technique chosen inside a free-text job (B:203), and decryption is a separate Web UI page, a Secrets Manager audit activity and an API helper script (B:206-210, B:224). That is an encrypt-versus-decrypt split of one key-managed function, and the restore step does not check the reply; it inverts what the prompt-side step did.")
w("  - R002's rationale (test inputs and ground truth differ: prompts against prompt-and-response pairs) does not fit: a restore test needs the output of the anonymise side as its input and the original value as ground truth, so one round trip spans both halves. The anonymise half is already in CK1 (Encrypt is a CK1 technique, A:63, A:102, INV(d) line 82), so a CK3 input-level column would duplicate CK1 bullets.")
w("  - Evidence thickness: of 83 CK3 R1 to R7 bullets only 13 are labelled anonymise-side and 10 restore-side (R1, R3, R5, R6; R2, R4 and R7 are unsplit, see %s). The restore half rests on a Web UI that decrypts one value at a time, a gated API helper, a release-note line (Reconstruct endpoint, %s) and a 2023 deck slide (%s, %s); an output-level column would be mostly [Not disclosed]." % (T("rn"), T("recon"), T("deck"), T("slide")))
w("  - Comparability: Presidio's PD3 `Presidio: Reversible anonymisation and deanonymisation (encrypt and decrypt)` is one column covering both halves; one CK3 keeps the one-to-one comparison for sheet 4.")
w("  - Cost of splitting later is low: CK3 keeps anonymise-side and restore-side bullets separate in R1, R3, R5 and R6 (B RN-2), and R2, R4 and R7 would need a side label added.")
w("- Recommended default: (a), one column, with option (c) as the revisit rule. If the user chooses (b), suggested header wording only: `Cloak: Input-level reversible anonymisation (encrypt with a managed secret)` and `Cloak: Output-level restoration of encrypted values (decrypt with a managed secret)`; this would also need rewording of the R1 and R3 Summaries and an INV Covered-by change for the Encrypt and Pseudonymise rows (Decrypt is already CK3 only).")
w("")

w("### CP1-3 Terms of Use and benchmarking (%s, %s, %s, %s; not a drafter decision)\n" % (T("t347"), T("t33"), T("t349"), T("sch22")))
w("- Routed by main as class c to a P5 resolver; permitted use stays an open R8 question decided before bench testing (R025 ruling 1 pattern). The user judges at CP2 or before any bench run only if the clauses stay unreconciled.")
w("- Facts on file (verbatim in INV(e) and R7 and R8): clause 3.3 (non-public-sector use only for a Purpose GovTech consented to in writing), 3.4.7 (no \"benchmarking tests or analyses of the Service\"), 3.4.9 and 3.4.11 (no sharing of licence keys or third-party access), Schedule 2.2 (use only on behalf of your Agency), Schedule 4.6 (data ceiling Confidential Cloud-Eligible and Sensitive High).")
w("- Options if a resolver cannot reconcile them: (a) leave the clauses as quoted and decide before any bench run (default); (b) rule now that Cloak is compared on documentation only until written consent is obtained (a bench-design statement, so only if the user volunteers it, R032); (c) ask GovTech (outside the read-only rules; not for agents).")
w("- Recommended default: (a). The resolver quotes the clauses, the defined terms and the Privacy Statement; nobody states a conclusion on permitted use as fact.\n")

w("### Smaller points for main (no user decision needed; listed so they are logged)\n")
w("- %s header text: the brief still carries the old CK2 and CK3 headers; update the brief note or record it in cloak_changes.md. The prefix is fixed at CP1 per R009 (`Cloak:`, main's ruling) and frozen after CP2." % T("hdr"))
w("- %s Covered-by: Decrypt becomes CK3 only (main); main or the merger also settles Pseudonymise, Templates, the Presidio row and the limit rows; %s Inclusion row: suggested `CK1; CK2`." % (T("cov"), T("incl")))
w("- %s planned Sentinel row: needs the planned marker in the inventory config and a row in INV(b); counts become 10, 8, 26, 9, 25, 4 = 82 (%s)." % (T("sentrow"), T("cnt")))
w("- %s add an R8 bullet for the LLM entity limit per dataset versus per project, and the FAQ wording to INV(e) (main: limit wording stays R8)." % T("llmlim"))
w("- %s P5 resolver scope for class c: Terms clauses 3.3, 3.4, 3.4.9, 3.4.11, Schedules 2.2 and 4.6, plus clauses 4.2, 6.1 and the definitions clause not yet read into any draft, and the Privacy Statement; R019 allows reading vendor terms pages." % T("t42"))
w("- Label convention for login-gated content: the drafts write [Not disclosed] with the HTTP fact (login redirect) for API pages that exist but are gated. R007 item 6 (closed government services: say not public) supports it; no change proposed, noted so the merger keeps it consistent across the three columns and INV(b).")
w("- No local-run or access consent is requested: R019 bars installs, API calls and sign-ins in research, so every b item stays open for the bench.\n")

# ---------------- table
w("## Triage table\n")
w("| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |")
w("|---|---|---|---|---|---|")
clsname = {"a": "a", "b": "b", "c": "c (licensing)"}
for d in items:
    c = clsname[d["c"]]
    if d["fl"] == "CP1":
        c = "b (CP1 decision)"
    elif d["fl"] == "GAP":
        c = "b (honest gap)"
    row = "| T%d | %s | %s | %s | %s | %s |" % (d["id"], sub(d["item"]), sub(d["loc"]), c, sub(d["src"]), d["p"])
    assert row.count("|") == 7, (d["id"], row.count("|"))
    w(row)
w("")

# ---------------- label hygiene
w("## Label hygiene\n")
w("Scope: the four files against `drafts/README.md` section 3 and the brief's label rules. Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Mechanical scan: every bracket label in A, B and INV is one of the allowed forms; no [Not found], no [To be verified: ...], no [Documented: develop/unreleased]. Repo labels are `govtech-responsibleai/playbook@45908b48` (A twice, B once) and, in INV(f), `explosion/spaCy@release-v3.8.16`, `explosion/spacy-models@ca6f473a`, `data-privacy-stack/presidio@2.2.364` and `Legrandin/pycryptodome@v3.24.0`. Every column bullet in R1 to R7 ends with a label (checker 0/0); every R8 bullet is unlabelled; R9 bullets are bare URLs. Spot checks: all 44 [Inferred] column bullets in R1 to R7 name their premise (R015 style for \"not built for\" statements at A:34 and B:35); the 36 [Not disclosed] column bullets name what was checked or give the HTTP fact, except the cases below.\n")
w("| Issue | Where | Proposed fix | T-id |")
w("|---|---|---|---|")
hy = [
 ("Two sides of a conflict under one label: the Mask page's Suffix and Prefix definitions against its example are one [Documented] fact with a parenthetical \"wording conflict\"; the confidence scope (portal \"per entity type\" against one slider) is one [Documented] bullet in CK1 R5", "INV(d) line 78; A:81", "Two bullets, one label each, each attributed (README rule 4, R007 item 4)", "%s, %s" % (T("maskhyg"), T("confscope"))),
 ("Same question, different labels across files: confidence scope [Documented] in A:81 and [Not disclosed] in INV(e); reversibility of Replace, Redact and Mask \"No [Inferred]\" in INV(d) but [Not disclosed] in CK3 R2 and R8; salts \"probably stale [Inferred]\" in INV(d), no conclusion in CK3", "A:81; INV(e) line 100; INV(d) lines 75-81; B:196, B:228-229, B:290", "One convention per fact (R020 for absences, R015 for conclusions drawn from a feature description) and align the files", "%s, %s, %s" % (T("confscope"), T("revlab"), T("salt"))),
 ("A positive fact under [Not disclosed]: \"Deployed version: the newest release note is v2.2.2\" states a fact and an absence in one bullet; the \"newest\" claim also conflicts with the release-note ordering", "B:234; B:67 (partly); A:64 (Documented)", "Split into a labelled fact and an [Not disclosed] absence bullet; reword \"newest\"", T("newest")),
 ("One bullet, two facts, one label (README rule 5): a quote plus an HTTP 404; three release facts; Mask defaults plus Alias", "B:232; A:64; A:98", "Split by the merger", T("multif")),
 ("A fact about another product inside an [Inferred] CK3 bullet: \"Presidio's token layout differs\" has no Presidio pin or label of its own, and the cross-reference count exceeds the brief's one per row", "B:221, B:233", "Reduce to one pointer to the Presidio header; keep only the Cloak-side arithmetic", T("presxref")),
 ("[Inferred] where a verbatim premise exists: 16 INV(c) cells \"On [Inferred] (premise P-ON)\" where the premise is a verbatim usage-guide sentence", "INV(c) lines 42-61", "Upgrade to [Documented] only with the resolution quote and URL (README rule 1)", T("defon")),
 ("Third-party facts under plain [Documented] with attribution: PyPI project page for pycrypto (owner not named, so not an owner's page); the rest of INV(f) cites owners' pages at pins and says \"not GovTech docs\" (compliant)", "INV(f) line 126", "Label the PyPI metadata as read from the PyPI page, or [Not disclosed] for owner and maintenance", T("licc")),
 ("Image-caption evidence under [Documented]: the 0.30 default, the 0 to 1 range, the Findings table columns and result captions are text on official pages and labelled [Documented] with the source type named in most CK1 and CK2 bullets (brief rule)", "A:80, A:77; B:81, B:83, B:79-80; B RN-8", "Keep; ensure each caption-based bullet says so", T("conf30")),
 ("Login-gated content: [Not disclosed] with the HTTP fact; 9 column ND bullets lack the word \"checked\" (most state the login redirect or the search run instead, B:234 is the release-note case) and about 15 INV mentions cite \"same checks\" or the redirect; consistent with the brief and R007 item 6", "A:86, A:101; B:45, B:91, B:211, B:235, B:250, B:260; INV(b) and others", "Keep; optionally add \"(login-gated)\" to each for uniform wording", T("apisch")),
 ("A statement of Terms content as [Documented] when the source is pypdf text: clause wording, the backslash in Schedule 4.6, and numbering are as extracted", "A:109, A:117-120; B:126, B:282-284; INV(e) lines 103-113", "Note \"as extracted\" once in the INV(e) intro (already says typographic quotes normalised); resolver re-reads the PDF", "%s, %s" % (T("sch46"), T("t15num"))),
 ("Deck facts labelled [Documented] without a version caveat in the bullet text in some places (\"may have changed\" appears in A:87 and B:186, not in A:49-50, B:209, B:245)", "A:49-50; B:209, B:245", "Add the date to each bullet that relies on the deck", T("deck")),
 ("Absence claims correctly [Not disclosed] with what was checked: spot-checked all 36 column bullets and the 59 INV mentions", "all three", "No change", "none"),
]
for a, b, c, t in hy:
    w("| %s | %s | %s | %s |" % (a, b, c, t))
w("")
w("Covered-by check: all 81 inventory rows carry a legal value. 41 cells equal CK1 alone ((a) 2, (c) 22, (d) 6, (e) 9, (f) 2), 7 equal CK2 alone ((a) 1, (c) 4, (e) 2), 3 equal CK3 alone ((a) 1, (f) 2), 3 equal `CK1; CK3` ((d)), 19 list all three headers ((b) 6, (e) 13), 7 use `— (inventory only, not in Table 3)` ((a) 5, (b) 1, (e) 1) and 1 uses `— (legacy, not in Table 3)` (enCRYPT). No `— (planned, not in Table 3)` yet (needed for %s). No stray values, bold, backticks or pipes in cells (the checker confirms the headers). The config needs BLOCKS counts 10, 7 (8 with the Sentinel row), 26, 9, 25, 4 and a markers tuple with legacy, inventory-only and planned markers. Reviewer-note sections (A 10 notes, B 13 notes, INV 8 items and a self-check) must be gone from the merged finals.\n" % T("sentrow"))

# ---------------- style
w("## Style issues in columns\n")
w("1. Summaries are within limits (words excluding the label; limit 45, R7 60). CK1: R1 42, R2 33, R3 44, R4 33, R5 43, R6 38, R7 53, R8 33, R9 26. CK2: 38, 32, 42, 34, 34, 42, 48, 39, 24. CK3: 42, 33, 44, 39, 34, 38, 45, 37, 26. Lesson 18 (the build counts the label) leaves CK1 R3 and CK3 R3 at exactly the cap with a one-word label; they pass, and any rewrite there must not grow (%s). R8 Summaries start `Key open questions.` with no label; R9 Summaries are plain; no underscores, backticks or `$` in any Summary; all ASCII." % T("headroom"))
w("2. Summary entailment: CK1 R4 \"GovTech's cloud\" (%s), CK2 R4 \"learns from 3 to 5 examples\" (%s), CK2 R5 Findings table for custom matches (%s), CK2 R6 \"500 words\" (%s), CK3 R4 \"Hosting is Government Commercial Cloud\" with no expansion in CK3 Detail (%s). The other Summaries were read against their Detail and are entailed." % (T("gcc1"), T("learns"), T("findings"), T("w500"), T("gcc3")))
w("3. Code-like identifiers in Summaries: none. Technical names such as AES-256 CBC, SHA-256, SHA-512, base64 and \"Replace (Unique)\" follow the brief's examples. Entity tags (SG_NRIC_FIN and others) appear only in Detail.")
w("4. Process language and internal ids in deliverable text: %s and %s (about 25 occurrences in A, B and INV). Instruction-like text to the reader: \"needs GovTech's answer before any bench run\" (A:129), \"see the conflict with the release notes below\" (B:228), \"this column covers only what Cloak's pages state\" (B:199)." % (T("proc"), T("ckids")))
w("5. Bullet length: one column bullet is over 380 characters (A:68, 383 characters, the Presidio tag-name cross-reference); no wrapped bullets. INV cells are long (the scope paragraph is about 3,100 characters and is not parsed; the longest cell is 922 characters, INV(a) line 12; 1 cell exceeds 800); allowed by README section 5 but hard to read; consider trimming the (a) cells.")
w("6. R8: each column has 14 bullets; the R8 Summaries name 7 to 8 topics each, so about half the bullets are not in the Summary. R8 bullets that restate Detail: CK1 A:129 (Terms 3.4.7, also A:118), CK2 B:126-127 (also B:116, B:115), CK3 B:282-284 (also B:272, B:271). The same Terms bullets are repeated in all three columns by design (service-wide), see %s." % T("cnt"))
w("7. Deliberate repetition: service-wide bullets (limits, access, maintenance, data ceiling) repeat in R6 and R7 of all three columns so a CP1 fold or split is a copy and edit; README allows it, and the merger may keep it. CK1 carries 6 CK2 or CK3 mechanism-named bullets for the same reason (brief Q01).")
w("8. R9: one URL per bullet in all three columns, all Cloak Guide URLs are `.md` pages (publicly readable), no repo pin applies except the playbook blob URL at the full SHA; R9 includes login-gated pages (A:174-175, B:166, B:312) and two aiguardian.gov.sg pages used only for an absence (A:184-185, B:171-172). See %s for the P9 exceptions list." % T("urls"))
w("9. Header: function parts are 6 to 9 words (README 4 to 12), sentence case, no trailing full stop, British spelling (\"anonymisation\"); CK2 and CK3 use main's tweaked parentheses. The text is identical in the three drafts and the 73 INV Covered-by cells that carry headers; the brief is stale (%s)." % T("hdr"))
w("10. Quote typography: straight quotes and ASCII digits are used (INV scope says typographic quotes in the Terms PDF were normalised); one Terms quote keeps a backslash as extracted (%s). Whitespace normalised, quotes under 40 words in the spot checks (a regex scan for longer quotes found only false pairings across cells).\n" % T("sch46"))

# ---------------- contradictions
w("## Contradictions\n")
w("Source conflicts and cross-draft inconsistencies, each with the ids that resolve them. \"Both written\" means the drafts already carry two labelled bullets or two cell facts (README rule 4).\n")
cons = [
 ("Entity count (C1): FTA intro and Features page \"20+\" against portal FAQs \"17+\"; the entity pages give 17 groups and 20 tags (drafter tally, [Inferred]). Both written; the R2 Summary uses 17 groups per main.", T("count")),
 ("Dates of birth and vehicle plate numbers (C2): named on the portal Features and FAQs pages; no Cloak Guide entity page, only DATE_TIME. Both written.", T("dob")),
 ("Access (C3): playbook \"GovTech's dedicated internal service\" against the Cloak Guide and portal \"open to select non-government entities\". Only in CK2 R8.", T("c3")),
 ("Salts (C4): Pseudonymisation page \"Custom salt values will be included in the future\" against release notes v2.1.0 and v2.1.4. Both written in CK3 and INV(d); INV adds a conclusion.", T("salt")),
 ("MDG ownership (C5): portal Features lists it under Cloak; Mirage says Mirage offers it and that it is available through the Cloak API; no Cloak Guide page. Both written; \"not reconciled\" is stronger than the quotes.", T("mdg")),
 ("Release-note ordering (C6): v2.2.2 (4 August 2024) above v2.2.1 (28 August 2024); v2.2.0 and v2.1.9 both 07 August 2024; the drafts call v2.2.2 the newest.", T("newest")),
 ("File-limit history (C7): v2.0.3 \"Maximum 10 columns\" and 100k rows against the current usage guide (500 MB per file) and FAQ (100 columns, tabular). Current guide stated as later ([Inferred]).", T("c7")),
 ("Broken links (C8, C9): home page link to /sections/decryption-secret-sharing/intro-to-decryption.md (404; the sidebar path is sections/decryption/intro-to-decryption.md); the Encrypt page's Presidio tutorial (404); the FAQ's www.cloak.gov.sg/terms (404). Recorded as HTTP facts.", "%s, %s" % (T("urls"), T("tver"))),
 ("Inside one official page (new): the Mask page defines Suffix as masking the starting characters and Prefix as masking the ending characters, while its example that keeps the first three digits is labelled \"suffix masked value\".", "%s, %s" % (T("maskhyg"), T("maskbeh"))),
 ("Inside one official page (new): the Terms PDF numbers the disputes clause 15 (15.1 to 15.3) while the SIAC clause refers to \"clause 14.2 above\".", T("t15num")),
 ("Between official pages (new): the LLM entity limit is \"per dataset (up to 5,000 documents)\" on the unstructured intro page and \"normally one per project\" in the FAQs. Both written in CK2 R4 and INV(c); INV(e) and CK2 R8 carry one side only.", T("llmlim")),
 ("Between official pages (new): the list limit is \"500 words\" (fixed-list page; Inclusion page \"first 500 words\") and \"500 entries\" (Inclusion page). CK2 R6 gives both quotes in Detail but the Summary says words; CK1 R6 mixes both.", T("w500")),
 ("Between official pages: portal \"Adjust detection sensitivity per entity type\" against the guide's single confidence slider. One [Documented] bullet in CK1, [Not disclosed] in INV(e).", T("confscope")),
 ("Cross-draft, Inclusion list: the brief puts per-entity Inclusion lists in CK1 (coverage text) and in CK2 (block (c)); INV(c) maps the row to CK2; CK1 R6 and CK2 R1 and R6 all carry it.", T("incl")),
 ("Cross-draft, Covered-by: the brief maps Decrypt, Encrypt and Pseudonymise to `CK1; CK3`, main moved Decrypt to CK3 only; the Templates, Presidio and limit rows disagree with what the columns say.", T("cov")),
 ("Cross-draft, headers: brief headers for CK2 and CK3 differ from the drafts and INV (main's tweaks).", T("hdr")),
 ("Cross-draft, reversibility: INV(d) \"No [Inferred]\" against CK3 \"[Not disclosed]\" for the same techniques.", T("revlab")),
 ("Cross-draft, Summary against Detail: CK1 R4 hosting wording; CK2 R4 \"learns\"; CK2 R5 Findings table against a [Not disclosed] bullet; CK3 R4 GCC expansion; CK2 R6 \"500 words\".", "%s, %s, %s, %s, %s" % (T("gcc1"), T("learns"), T("findings"), T("gcc3"), T("w500"))),
 ("Cross-draft, release notes: CK1 R4 \"v2.0.1 added Word support\" against the brief's and CK3's v2.0.1 \"Reconstruct endpoint\" (may both be true).", T("v201")),
 ("Cross-draft, brief estimates against findings: brief block targets 10, 7, 25, 9, 16, 3 against finals 10, 7, 26, 9, 25, 4; the brief's \"40-odd\" Credits entries against 32 (INV-RN 3); P0's \"endpoint names not disclosed\" against the three named API items. Recorded as corrections in INV-RN.", T("cnt")),
 ("Tension, not conflict: the vendor's \">97% recall\" claim and the FAQ's \"100% recall should not be assumed\" and Terms 9.1.1 (no warranty of accuracy). All three are written; no draft links them.", "%s, %s" % (T("recall"), T("t91"))),
 ("Tension, not conflict: the vendor's \"real-time via API\" use case against a Web UI that returns a download request and a documented API schema that is not public.", "%s, %s" % (T("lat"), T("dir"))),
 ("Reviewer-note accuracy: B RN-2 claims side-labelled bullets in CK3 R4; there are none.", T("rn")),
 ("Not conflicts, no item: the playbook's list of where PII can appear (prompts, outputs, retrieved documents, tool arguments and results) supports the column scope; the Sentinel docs do not mention Cloak (absence recorded); \"built on Presidio\" stays [Inferred] ({pres}).".replace("{pres}", T("pres")), "none"),
]
for i, (a, t) in enumerate(cons, 1):
    w("%d. %s See %s." % (i, a, t) if t != "none" else "%d. %s" % (i, a))
w("")
w("Cross-draft values compared and found consistent (by reading, not by execution): the three column headers across A, B and INV Covered-by cells (checker); cross-reference headers to Presidio (PD1, PD2, PD3, PD6) and Sentinel SN6 are exact text matches to `presidio_two_level.md` and `sentinel_two_level.md`; limits 20,000 characters, 500 MB, 200 MB, 100 files, 2 GB; retention (24 hours); maintenance window; the confidence default 0.30; release versions and dates for v2.0.1, v2.1.0, v2.1.4, v2.1.5 and v2.2.0 across CK2, CK3 and INV; Terms dates and clause numbers 3.3, 3.4.7, 3.4.9, 3.4.11, Schedule 2.2 and 4.6 across A, B and INV; the pinned playbook URL across A and B.")

txt = "\n".join(out) + "\n"
open("benchtest/drafts/cloak_triage.md", "w", encoding="utf-8").write(txt)
print(len(items), dict(cls), dict(pri), len(txt))
print("H:", [(d["id"], d["k"]) for d in H])
print(dict(files))
print(cp1, gap, licc)
