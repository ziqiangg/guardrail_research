import re, sys, io
from collections import Counter, OrderedDict

ROOT = "C:/Users/cys-c/Desktop/gzqr/gitubrepo/misc/researchrail/guardrail_research/"
ITEMS = ROOT + "benchtest/scratchpad/triager/lionguard/items.txt"
OUT = ROOT + "benchtest/drafts/lionguard_triage.md"

# ---------- parse items ----------
groups = []   # (name, [item dicts])
cur = None
txt = open(ITEMS, encoding="utf-8").read()
blocks = re.split(r"^---\s*$", txt, flags=re.M)
# first block starts with a group heading
items = []
group_of = {}
gname = None
for b in blocks:
    lines = b.strip("\n").split("\n")
    d = {}
    for ln in lines:
        if ln.startswith("## "):
            gname = ln[3:].strip()
            groups.append([gname, []])
        elif re.match(r"^(key|item|loc|cls|tag|src|prio|files):", ln):
            k, v = ln.split(":", 1)
            d[k] = v.strip()
    if d:
        d["group"] = gname
        items.append(d)
        groups[-1][1].append(d)

for i, d in enumerate(items, 1):
    d["id"] = "T%d" % i
keymap = {d["key"]: d["id"] for d in items}
assert len(keymap) == len(items), "duplicate keys"


def ref(s):
    def f(m):
        k = m.group(1)
        if k in keymap:
            return keymap[k]
        raise KeyError(k)
    return re.sub(r"\{(\w+)\}", f, s)


def esc(s):
    return ref(s).replace("|", "/")


def clsname(d):
    c = d["cls"]
    if d["tag"] == "CP1":
        return c + " (CP1 decision)"
    if d["tag"] == "GAP":
        return c + " (honest gap)"
    return c


n = len(items)
cc = Counter(d["cls"] for d in items)
ch = Counter(d["cls"] for d in items if d["prio"] == "H")
cp = Counter(d["prio"] for d in items)
cls_prio = {(d["cls"], d["prio"]): 0 for d in items}
for d in items:
    cls_prio[(d["cls"], d["prio"])] += 1
cp1 = [d for d in items if d["tag"] == "CP1"]
gap = [d for d in items if d["tag"] == "GAP"]
fA = sum(1 for d in items if "A" in d["files"])
fI = sum(1 for d in items if "I" in d["files"])
fB = sum(1 for d in items if "B" in d["files"])
hs = [d for d in items if d["prio"] == "H"]

grange = []
idx = 1
for name, lst in groups:
    grange.append("%s T%d to T%d" % (name, idx, idx + len(lst) - 1))
    idx += len(lst)

T = keymap  # short alias

out = []
w = out.append

w("# LionGuard triage of open evidence items (DRAFT)")
w("")
w("Sources triaged: `lionguard_cols_a.md` (column LN1, CP1 default single column; 9 rows, 187 Detail bullets, 12 Reviewer notes), `lionguard_inventory.md` (sheet 3x draft: (a) variant table 4 rows, (b) output keys 11, (c) dependencies and access 8, (d) artefacts and references 10, (e) cross-reference to Sentinel 4; 37 rows, 9 Reviewer notes and a self-check), the brief `lionguard_brief.md` (scope, source list, facts to re-verify, conflicts C1 to C6, gaps 1 to 9, open questions Q01 to Q04), rulings R002, R005, R007, R009, R011, R015, R019, R020, R021 (R025 as the terms precedent), and main's lionguard routing in `scratchpad/main/queue.md` (Q01 to Q03 to CP1; Q04 licence conflict to class c and P5). No research done; source suggestions only. Nothing here is verified. Written 2026-10-09 by gr-triager. Mechanical checks re-run at the start (this triage run): `check_drafts.py columns lionguard_cols_a.md` gives 0 errors and 0 warnings (header `LN1=LionGuard: Localised harmful-content classification`); `check_drafts.py inventory lionguard_inventory.md --headers lionguard_cols_a.md` gives 0 errors and 0 warnings (tables 4, 11, 8, 10 and 4 rows; 12, 7, 7, 7 and 6 cells).")
w("")
w("## Legend")
w("")
w("- File short names: A = lionguard_cols_a.md, INV = lionguard_inventory.md, BR = lionguard_brief.md, queue = `scratchpad/main/queue.md`. Draft line numbers are as at 2026-10-09 and move when the merger edits (`A:85` = line 85 of cols_a; `INV(c) Gemma row (line 43)` = file line).")
w("- Location notation: `LN1 Rk` = the single column, row k (Summary, or Detail bullet by line); `INV(a)` to `INV(e)` = inventory block (a) lines 11-14, (b) 22-32, (c) 40-47, (d) 55-64, (e) 72-75; `A RN-n` = Reviewer note n of the column draft (12 notes); `INV-RN n` = inventory Reviewer note n (9 notes).")
w("- Labels: ND = [Not disclosed]; TBV = [To be verified]; INF = [Inferred]; R8 = unlabelled R8 bullet.")
w("- Class: a = answerable from an official page, a pinned repo file, a paper or a local file, or a drafting fix that needs no research; b = needs testing (stays open), or a CP1 decision item (closes when chosen, NeMo b22 and Presidio precedent); `honest gap` = closed or undisclosed vendor internals, plans, or third-party services, where no public document is expected to answer; c = licensing, terms or ownership.")
w("- Priority: H = changes an R1 to R7 Summary line, a Summary label, or a headline number (here the R5 Summary figure 77.0), or is a CP1 decision that rewrites a Summary. M = Detail level, or only an R8 Summary line (R8 Summaries list questions and are not counted as H, as in the Presidio and Sentinel triage; the SDP triage counted them, so its H total is not comparable). L = cosmetic or low impact.")
w("- Short source names: PB = playbook page `govtech-responsibleai/playbook` website/docs/tools/lionguard.md at 45908b48 (staging); G = Sentinel docs page \"Sentinel-Guardrails\" (cross-reference only); P2 = arXiv 2507.15339 (LionGuard 2); P1 = arXiv 2407.10995 (LionGuard 1); RB = arXiv 2507.05980 (RabakBench); B1, B2, B3 = blog posts of 29 Jul 2025, 21 Aug 2026 and 28 Sep 2026; HFAPI = Hugging Face Hub API; EG = Hugging Face page of google/embeddinggemma-300m.")
w("")
w("## Counts")
w("")
w("Total %d deduplicated items (T1 to T%d), drawn from the 13 R8 bullets (one column, so no per-column duplication), the explicit open labels (column bullets: ND 10, TBV 2, INF 23 of 187 Detail bullets; raw bracket text including Summaries and Reviewer notes: ND 12, TBV 2, INF 27; inventory: ND 20, TBV 6, INF 7 label mentions), the Reviewer notes (A 12 bullets, INV 9 items), the brief conflicts C1 to C6 and the two new conflicts in A RN-2 and RN-3, the queue items routed to triage (Q01 to Q03, Q04), and a cross-draft comparison of the two files and the brief." % (n, n))
w("")
w("| Class | Count | of which H |")
w("|---|---|---|")
w("| a doc-answerable (incl. drafting fixes) | %d | %d |" % (cc["a"], ch["a"]))
w("| b needs testing or CP1 decision | %d | %d |" % (cc["b"], ch["b"]))
w("| c licensing / terms | %d | %d |" % (cc["c"], ch["c"]))
w("| Total | %d | %d |" % (n, len(hs)))
w("")
w("Priority totals: H %d, M %d, L %d." % (cp["H"], cp["M"], cp["L"]))
w("")
w("Class by priority: a: H %d, M %d, L %d; b: H %d, M %d, L %d; c: H %d, M %d, L %d." % tuple(cls_prio.get((c, p), 0) for c in "abc" for p in "HML"))
w("")
w("Items touching each source file (an item can touch several): lionguard_cols_a.md %d; lionguard_inventory.md %d; brief / rulings / queue only or also %d." % (fA, fI, fB))
w("")
w("CP1 decision items counted in class b: %s (T-ids %s; the first three are Q01 to Q03, the others are new). Honest-gap items: %s. Licensing (class c) items: %s." % (len(cp1), ", ".join(d["id"] for d in cp1), ", ".join(d["id"] for d in gap), ", ".join(d["id"] for d in items if d["cls"] == "c")))
w("")
w("Dedup note: the same open question appears in several rows of the single column and in the inventory and is merged into one id with every location: the licence conflict (R1, R4, R8, inventory (a) four rows and (c)) is T%s, the threshold question (R5, R7, R8, inventory (a) three rows) is split into a document half T%s and a test half T%s, the embedder-terms questions are split by owner (Gemma T%s and T%s, OpenAI T%s, Gemini T%s) with the cross-draft mismatch in T%s, and maximum input length is split into T%s and T%s." % (T["q04"][1:], T["threshdoc"][1:], T["threshtest"][1:], T["gemma"][1:], T["gemmader"][1:], T["openai"][1:], T["gemini"][1:], T["termsalign"][1:], T["maxdoc"][1:], T["maxtest"][1:]))
w("")
w("Provenance note: A RN-9 and INV-RN 8 state that numbers and quotes come from raw text (fetch_text.py, curl, the Hub API), but that the three blog posts, the Sentinel page and the playbook text were re-read from saved P1 raw copies and not re-fetched a second time; no item is classed as depending on a summarising fetch. Facts that depend on something not read: the Gemma terms Appendix and Gemini API terms (A says not read, INV says read, see T%s), the OpenAI terms pages (HTTP 403, not worked around), map_benchmark_labels.ipynb (T%s), the paper's v1 html (T%s), and the RabakBench-full files (gated, not requested)." % (T["termsalign"][1:], T["notebook"][1:], T["f1head"][1:]))
w("")
w("Raw label census (whole-file occurrences of the exact bracket text, including Summaries and Reviewer notes): A: [Documented] 59, [Documented: repo ...] 62, [Inferred] 27, [To be verified] 2, [Not disclosed] 12. INV: [Documented] 68, [Documented: repo ...] 91, [Inferred] 7, [To be verified] 6, [Not disclosed] 20. Variant-specific bullets in A (R4 to R7): 55 of 111.")
w("")
w("Groups (id ranges): " + "; ".join(grange) + ".")
w("")

# ---------- CP1 ----------
w("## Items for CP1 (decision-bearing for the user)")
w("")
w("Q01 to Q03 are the explorer's questions carried in the brief (each with a default that is drafted); the others are new decision-bearing items found in triage. Q04 is not a drafter decision: main routed it to class c and a P5 resolver, and the user judges at CP1 or CP2 only if the sources stay unreconciled.")
w("")
w("### CP1-1 Q01 column split (%s)" % T["q01"])
w("")
w("- Options: (a) one column LN1 `LionGuard: Localised harmful-content classification` (drafted); (b) three columns LN1 to LN3, one per variant (headers fixed in BR: 2 with OpenAI embeddings, 2.1 with Gemini embeddings, 2 Lite with local EmbeddingGemma); (c) two columns, LN1 for 2 and 2.1 (external embedding call) and LN2 for Lite (no external call).")
w("- Evidence the choice turns on:")
w("  - Identical across the three variants: the 11 output keys and taxonomy table text (equal by checksum, INV-RN 3), the predict code (only comments and docstrings differ, INV(a) 2.1 row; A:99-105), the LICENSE file (same md5), the card opening sentence (A:13-15). R1, R2, R3 and R8 are variant-neutral: 9, 18, 12 and 13 bullets.")
w("  - Different: embedder (OpenAI, Gemini, Gemma), hosting (two external APIs, one local), input width 3072, 3072, 768, classifier size 848,942, 848,942, 259,118 parameters, package pins (openai, google-genai, sentence-transformers), access (own key, own key, gated download), terms (OpenAI, Google API, Gemma), published evidence (paper tables for 2; one blog table on a private split for 2.1; none for Lite). 55 of the 111 R4 to R7 bullets name one variant (R4 21 of 39, R5 17 of 33, R6 12 of 20, R7 5 of 19).")
w("  - The brief's objective asks \"what minimum architecture v1 needs\": with option (a) the external-call versus local boundary appears only inside R7 and inventory (c); option (c) is the only split that puts it in Table 3.")
w("  - R002 allows one column for an undifferentiated string classifier (Sentinel AA precedent); R005 says a single column is acceptable if justified at CP1.")
w("  - Costs of splitting: R1 to R3 copied into each column (about 40 duplicate bullets per extra column), 21 Covered-by cells and sheet 4 would count LionGuard once, twice or three times for the same function; the draft keeps variant bullets separate so the merger can split by copy and edit.")
w("- Recommended default: (a), as drafted (explorer's recommendation and BR default); the variant comparison belongs on the bench's variant axis. Choose (c) only if the user wants the API-versus-local architecture split visible in Table 3.")
w("")
w("### CP1-2 Q02 header prefix (%s)" % T["q02"])
w("")
w("- Options: (a) `LionGuard:`; (b) `GovTech LionGuard:`.")
w("- Evidence: R009 says the prefix is the product's own name as its owner writes it and includes the vendor only when part of the brand or needed to disambiguate. Every GovTech page read writes \"LionGuard\" (cards, playbook, papers, blogs; the Hugging Face org is `govtech`). The Sentinel precedent `GovTech Sentinel:` and CLAUDE.md's product name \"GovTech LionGuard\" point the other way. A disambiguation point for (b): `Llama Guard:` is already a prefix in the same sheet and the two names differ by a few letters; the Sentinel column AA header carries the same function wording, so with (b) the two GovTech columns read as one family.")
w("- Cost of change: the header in BR, `## Column` line A:5 and 21 INV Covered-by cells, until CP2; frozen after CP2 (R009).")
w("- Recommended default: (a) `LionGuard:` (R009 literal reading and the explorer's recommendation); (b) is reasonable if the user prefers a GovTech family prefix.")
w("")
w("### CP1-3 Q03 \"self-hosted\" framing (%s, with %s)" % (T["q03"], T["r1sum"]))
w("")
w("- Options: (a) keep all three variants in the one column and state the dependencies in R7 and inventory (c); (b) treat Lite as the self-host path and describe 2 and 2.1 as \"needs external API\" in R7 only; (c) exclude variants that need a paid third-party API.")
w("- Evidence: GovTech publishes only the head (3.4 MB for 2 and 2.1, 1.0 MB for Lite); 2 and 2.1 send every text to OpenAI or Google (INF premise: the usage code calls the embedding client, A:164-165); Lite is fully local (card, A:15, 68) but its embedder is gated behind Google's Gemma terms and a Hugging Face login (A:159-161; INV(c) rows 42-43); the playbook says all three are \"open-sourced for self-hosting\" (A:12); R005 says columns cover what you get when you run the models yourselves; R019 puts keys and Gemma acceptance in bench design. The R1 Summary currently says \"you run it yourself\" without the embedding caveat (%s)." % T["r1sum"])
w("- Recommended default: (a), as drafted, plus an R1 Summary that names the hosted embedding step for 2 and 2.1 (%s)." % T["r1sum"])
w("")
w("### CP1-4 New: embedder terms and harmful test text (%s; facts in %s, %s, %s, %s)" % (T["terms"], T["gemma"], T["gemmader"], T["openai"], T["gemini"]))
w("")
w("- Question: variants 2 and 2.1 send each test text to a third-party API, and the bench needs harmful, explicit and self-harm text. OpenAI says abuse-monitoring logs are kept up to 30 days (INV(c) row 40); the Gemini unpaid tier says not to submit sensitive, confidential or personal information (INV(c) row 41); Gemma's Prohibited Use Policy is cited (INV(c) row 43); the OpenAI terms page returned 403 and the column says the Gemini terms were not read (A:166-167), so the column and inventory disagree (%s)." % T["termsalign"])
w("- Options: (a) record only and decide at bench design (R019 precedent: sensitive test data is decided at bench design); (b) rule now that 2 and 2.1 are run on benign or synthetic text only, with harmful text confined to Lite; (c) drop 2 and 2.1 from the first bench pass (the Q03 option b/c effect).")
w("- Recommended default: (a), with the resolver reading the reachable owner pages (%s, %s, %s) so the user decides on facts at CP2; this is an R025-style question if the terms turn out to forbid red-team input." % (T["gemma"], T["openai"], T["gemini"]))
w("")
w("### CP1-5 New: demo Space data flow (%s)" % T["demo"])
w("")
w("- Question: the code of `govtech/lionguard-demo` appends submitted text and scores to a Google Sheet when one is configured and calls OpenAI on the chat path (INV(d) row 58). The R5 demo-band bullets carry the thresholds (A:109-111) but not this data flow.")
w("- Options: (a) the Space is a reference only: never used as a test target, and the data-flow fact is added to the R5 bullet or kept inventory only (default); (b) allow it for benign text only.")
w("- Recommended default: (a); main can rule it under R019 (no calls, no submissions), so it reaches the user only if they want (b).")
w("")
w("### CP1-6 Q04 licence conflict (%s; sub-items %s, %s)" % (T["q04"], T["licsub"], T["licdata"]))
w("")
w("- Not a drafter decision. Routed by main as class c to P5 (queue). The R1 Summary calls the weights \"open\" while the LICENSE (MIT subject to Singapore law and SIAC) and the paper (\"exclusively for research and public interest purposes only\") are unreconciled; no page read states how they relate.")
w("- Options for the user, if P5 cannot reconcile: (a) leave the conflict as two labelled bullets and judge permitted use at CP2 (default); (b) rule now that the bench is research use and note it; (c) ask GovTech (outside the read-only rules; not for agents).")
w("- Recommended default: (a). The resolver quotes the four texts and any reconciling page; nobody states a conclusion on permitted use as fact.")
w("")
w("### Smaller points for main (no user decision needed; listed so they are logged)")
w("")
w("- %s third-party embedder behaviour facts (dimension, max input) in cells: keep attributed \"not GovTech docs\" or drop." % T["thirdparty"])
w("- %s arXiv 2507.05980 (RabakBench paper) as an official GovTech-authored source; add to the brief list and to INV(d)." % T["arxiv2"])
w("- %s Covered-by convention for inventory (d) rows; %s sentinel finals FYI." % (T["covered"], T["sentfyi"]))
w("- Header function part has three words (hyphenated \"harmful-content\" counts as one) against the README's 4 to 12; BR keeps it for parity with Sentinel AA and sheet 4 and says it is not a drafter decision. Main may rule or add words at CP1.")
w("- %s which variant is the bench default (bench design, follows Q03 and CP1-4)." % T["defaultvar"])
w("- Local-run consent: none requested. R019 already bars installs, weight downloads and API calls in research, so the b items stay open for the bench.")
w("")

# ---------- table ----------
w("## Triage table")
w("")
w("| ID | Item (short) | Location(s) | Class | Source(s) to check / why testing | Priority |")
w("|---|---|---|---|---|---|")
for d in items:
    w("| %s | %s | %s | %s | %s | %s |" % (d["id"], esc(d["item"]), esc(d["loc"]), clsname(d), esc(d["src"]), d["prio"]))
w("")

# ---------- label hygiene ----------
w("## Label hygiene")
w("")
w("Scope: the two files against `drafts/README.md` section 3. Allowed forms: [Documented], [Documented: repo <repo>@<ref>], [Documented: develop/unreleased], [Inferred], [To be verified], [Not disclosed]. Mechanical scan: every bracket label in A and INV is one of the allowed forms; no [Not found], no [To be verified: ...], no [Documented: develop/unreleased] (see %s for the playbook branch question that could require one). Repo labels use `govtech/lionguard-2@be4e38c9`, `govtech/lionguard-2.1@1c3a9ea7`, `govtech/lionguard-2-lite@d56c17a0`, `govtech/lionguard-v1@92cc0491`, `govtech/lionguard-demo@4ade46d1`, `govtech/lionguard-2-synthetic-instruct@8aa43f61`, `govtech/RabakBench@3c02a5b8`, `govtech/RabakBench-full@2cbe90c9` and `govtech-responsibleai/playbook@45908b48`, one repo per label. No quote in A or INV is longer than 40 words (spot scan of the long quoted passages: A:24 taxonomy and A:85 LICENSE lines are within the limit). Column bullets: one label per bullet (0 multi-label bullets by the checker). First Detail bullet of R7 and the R7 Summary start `Minimum setup:` and carry [Inferred]: compliant." % T["playbookpin"])
w("")
w("| Issue | Where | Proposed fix | T-id |")
w("|---|---|---|---|")
hyg = [
    ("Inference inside a [Documented] or [Not disclosed] bullet: the blog's \"11 heads\" explained as \"counting output keys\"; \"no retrained model is published there\" drawn from a repository-level lastModified date; \"not obviously reconcilable and neither is a legal opinion\" and \"how they relate is not stated\" in one bullet", "A:61, 90, 92; A RN-2, RN-10", "Split into a labelled fact plus an [Inferred] bullet with its premise; keep the ND bullet to the absence only (README rule 5)", "{hygA}"),
    ("One label for two sources or for a computation: HF API sizes plus the paper's 0.85M/3.2 MB under one repo label; the md5 comparison of LICENSE files is our own check under [Documented: repo]; \"The cards'\" metadata (plural) under the lionguard-2 label only", "A:62, 86-88; INV(a) Licence cells", "Separate paper bullet; label the md5 comparison [Inferred] with the premise or plain text \"(checked by md5)\"; add per-repo labels for 2.1 and Lite", "{hygB}"),
    ("Same fact, different labels: the Table 1 versus Table 3 order is [Inferred] in A:116 and [To be verified] in INV(a) row 12", "A:116; INV(a) row 12", "One label convention; the premise (RabakBench paper Table 4 match) supports [Inferred] with the two tables kept as [Documented]", "{c3}"),
    ("Own computations: the layer-shape arithmetic is correctly [Inferred] (A:65), while the md5 comparison of LICENSE files (A:86-87) is a drafter check under [Documented: repo]", "A:65, 86-87", "As above", "{hygB}"),
    ("Third-party facts under [Documented] with plain-text attribution (OpenAI and Google default dimensions, max inputs, Gemma terms): compliant with the attribution rule, but the brief limits third-party facts to gating, licence, terms and embedder identity", "A:139, 141, 160-162; INV(c) rows 40-43; INV(e) row 75", "Main ruling on whether embedder behaviour facts stay", "{thirdparty}"),
    ("TBV bullets that are partly process facts: \"returned HTTP 403 to the fetch tool\" and \"Appendix was not read\" (A:163, 166, 167); the finals must not mention the session", "A:163, 166-167; INV(c) rows 40-41", "Resolve through the Gemma, OpenAI and Gemini items, or reword as product-neutral open questions", "{gemma}, {openai}, {gemini}"),
    ("Absence claims correctly [Not disclosed] with what was checked (spot check of the 10 column ND bullets and 20 inventory ND mentions): fine. Exceptions to review: \"Embedding dimension [Not disclosed]\" for LionGuard 1 (a third-party card would answer); \"A required Python version [Not disclosed]\" lists the files checked", "INV(a) row 11; INV(c) packages row", "Keep; optional upgrade from the BAAI card", "{lg1dim}"),
    ("Statement \"scores content harms only\" is [Inferred] with the premise named (key list), consistent with R015; the paper's annotator prompt-injection instruction (A:38) is [Documented] but not linked to the ND bullet", "A:36-38", "Add a pointer in the ND bullet or leave; see the jailbreak item", "{jailbreak}"),
    ("Cells that hold several facts with several labels and a long text (INV(a) row 12 Operating threshold and evaluation cell, more than 15 labelled facts)", "INV(a) row 12 (line 12)", "Allowed by README section 5; consider moving the comparator and benchmark-count facts to (d) to keep the cell readable", "{c4}"),
    ("Labels on conflicting official sources are two bullets each (C1, C3, C5, C6, new conflicts): compliant with README rule 4, except the R2 Summary that picks \"partial Tamil\"", "A:28-30, 19", "Fix the Summary", "{c5}"),
]
for a, b, c, d in hyg:
    w("| %s | %s | %s | %s |" % (esc(a), esc(b), esc(c), ref(d)))
w("")
w("Covered-by check: all 37 inventory rows carry a legal value. 21 cells equal the single header `LionGuard: Localised harmful-content classification` ((a) 3, (b) 11, (c) 7), 2 use `— (legacy, not in Table 3)` (LionGuard 1 and the BAAI embedder) and 14 use `— (inventory only, not in Table 3)` ((d) 10, (e) 4); no `planned` marker; no stray values, bold, backticks or pipes in cells (the checker confirms the header). The P8 config needs BLOCKS counts 4/11/8/10/4 and a markers tuple with the legacy and inventory-only markers. If CP1 changes Q01 or Q02 the 21 header cells change with it. Reviewer-note sections (A 12 notes, INV 9 notes and a self-check) must be gone from the merged finals.")
w("")

# ---------- style ----------
w("## Style issues in columns")
w("")
w("1. Summaries are within limits: word counts R1 37, R2 38, R3 39, R4 40, R5 39, R6 37, R7 50 (limit 60), R8 31, R9 27 (limit 45). None is within 4 words of the cap, so the Summary fixes in %s, %s, %s, %s and %s have room. R8 Summary starts `Key open questions.` with no label; R9 Summary is plain; no underscores, backticks or `$` in any Summary; all Summaries are ASCII." % (T["r1sum"], T["r4sum"], T["r7sum"], T["c5"], T["f1head"]))
w("2. Code-like identifiers in Summaries (brief forbids them): \"predict\" (R3 Summary \"The predict call\", R6 Summary \"pass the vectors to predict\"); package names \"transformers\", \"torch\", \"sentence-transformers\" (R7 Summary). Suggested: \"the classifier call\", and \"Python deep-learning libraries\" or keep the package names only in Detail. \"EmbeddingGemma\" and \"LionGuard 2 Lite\" follow the vendor spelling.")
w("3. Process language and ruling ids in deliverable text (finals must be clean): see %s (R019 in A:176 and INV scope; \"routed as a licensing item\"; \"a bench-design choice for the user\"; \"see R7\"; \"covered under the Sentinel column\"; \"was not read\" / \"was not worked around\"). Instruction-like text to the reader: \"Nothing is run during research; this is the plan for the bench\" (A:176)." % T["proc"])
w("4. One bullet over 420 characters: A:24 (the taxonomy bullet, 441 characters). Consider splitting by category; no wrapped bullets found.")
w("5. Internal conflict tags are not used in the column text (the C1 to C6 numbers appear only in Reviewer notes): good. The bullets starting \"Conflict:\" (A:69) and \"Source conflict:\" (A:95) are plain-language and acceptable.")
w("6. R8 Summary names 7 topics; 6 of the 13 R8 bullets are not in it (Table 1 versus Table 3 order, binary key versus maximum, Sentinel-hosted weights, embedder drift, default variant, and the Lite/2.1 split of the evaluation question). R8 bullets that restate Detail items already documented: A:186 (licence, also A:85-90), A:188 (retraining, also A:91-93), A:189 (hosted weights, also A:94). Low priority.")
w("7. Deliberate repetition: three near-identical per-variant bullets in R3 (A:46-48), R5 (A:99-101, 103-105) and R4 (A:62-64, 66-68, 75-77, 85-87), written so a CP1 split is a copy and edit (BR). If CP1 keeps one column, the merger may keep them (README rule: one repo label per bullet, so they cannot be merged into one bullet).")
w("8. Dates and fetch details inside Detail (\"read 2026-10-09\", \"Hugging Face API\") appear in many bullets; acceptable as HTTP facts and source hints, but the repeated \"(Sentinel docs, hosted API)\" and \"(OpenAI docs, not GovTech docs)\" attributions are plain text after the label and conform to README rule 3.")
w("9. Quote typography: straight apostrophes replace the curly ones in a few quotes (A RN-12) and ASCII digits are used throughout; normalisation only. The inventory has one very long scope paragraph (about 2,000 characters) which is not parsed.")
w("10. R9: one URL per bullet; it includes three Hub API JSON URLs (A:202-204), the 403 OpenAI terms URL (A:219, an HTTP-fact URL for P9) and an arXiv paper not in the brief list (A:210, %s). R9 lacks the Gemini terms and OpenAI data-controls URLs that INV(c) cites (%s)." % (T["arxiv2"], T["termsalign"]))
w("11. Header: function part is three words against the README's 4 to 12 (BR notes it; parity with Sentinel AA). The text `LionGuard: Localised harmful-content classification` is identical in BR, A:5 and 21 INV cells.")
w("12. Mixed units for size: 3,398,496 bytes (Hub API) beside the paper's 3.2 MB and the brief's 3.4 MB (the same file in MiB and MB). Not an error; a note helps the reader.")
w("")

# ---------- contradictions ----------
w("## Contradictions")
w("")
w("Source conflicts and cross-draft inconsistencies, each with the ids that resolve them. \"Both written\" means the drafts already carry two labelled bullets (README rule 4).")
w("")
cont = [
    "Licence (C2, Q04): the LICENSE (MIT subject to Singapore law and SIAC arbitration, identical in all four model repos and two datasets) and the card header (license other, govtech-singapore) versus the paper's \"exclusively for research and public interest purposes only\" versus the blog and playbook wording \"open-sourced\". Both written; the R1 Summary says \"open\". See {q04}, {licsub}, {licdata}, {r1sum}.",
    "Embedder name inside the repo (C1): docstring text-embedding-3-small (lines 97, 104) versus card, inference.py, config.json and paper text-embedding-3-large at 3072. Both written. See {c1}.",
    "Table order (C3): paper Table 1 (SS, ZH, MS, TA) versus Table 3 (SS, MS, ZH, TA) for the same numbers; the blog and RB Table 4 support Table 1. Both written; labels differ between A and INV. See {c3}, {c3rerun}, {arxiv2}.",
    "Benchmark count (C4): 17 in the abstract and playbook, 16 in the blog; reconciled by paper section 5.1 as [Inferred]. See {c4}.",
    "Tamil strength (C5): the card says Tamil, the playbook \"partial Tamil\", the paper \"remains moderate\". Both written, but the R2 Summary picks \"partial Tamil\". See {c5}, {testsets}.",
    "Embedder spelling (C6): Sentinel docs \"text-embedding-large-3\" versus the card's text-embedding-3-large. Both written. See {c6}.",
    "New (A RN-2): blog \"11 classification heads\" versus seven head modules and eleven output keys in the code. Both written, with an inference inside a Documented bullet. See {n1}, {hygA}.",
    "New (A RN-3): the playbook says the paper and blog \"describe how each version works\"; the paper html names no Gemini or Gemma embedder. Carried as a playbook bullet plus an ND bullet. See {n2}.",
    "Cross-draft, terms read: A says the Gemma Appendix and Gemini terms were not read and the OpenAI terms returned 403; INV(c) quotes the Appendix listing EmbeddingGemma, the Gemini terms and an OpenAI data-controls page. See {gemma}, {termsalign}, {openai}, {gemini}.",
    "Cross-draft, third-party limits: A R6 keeps the maximum input length [Not disclosed] (embedder-set) while INV(c) and INV(e) quote the embedders' limits; INV(e) says the self-hosted length is set by the embedder and no GovTech card states one, which agrees. See {thirdparty}, {maxdoc}.",
    "Cross-draft, Lite credentials: R7 Summary says Lite needs \"no API key\"; INV(c) says a Hugging Face login is needed to accept the gate. See {r7sum}.",
    "Cross-draft, Summary versus Detail: R4 Summary \"publishes only the small classifier\" versus the dataset subset, the blog's \"part of the training data\" and the code in the HF repos. See {r4sum}.",
    "Disagreement rate: \"about 4%\" (paper) versus 4.19% over-predict plus 0.70% under-predict in the same bullet. See {four}.",
    "Throughput: INV(a) says the 300 tokens/s includes the embedding call; R8 asks whether it includes the OpenAI round trip. See {tput}.",
    "Demo Space naming: the Space README says \"Demo for LionGuard 2.\" while its code defaults to model lionguard-2.1; thresholds shown are demo behaviour, not a recommendation ([Inferred]). See {demo}, {threshdoc}.",
    "Playbook pin: the labels cite the staging branch commit 45908b48 while main is 97338569; the site's source branch is unknown. See {playbookpin}.",
    "Sentinel final (frozen) versus this read: paper section 7.2 versus 4.2.2 for the binary head; a \"Tamil 66.5 in Table 8\" claim not verified. No edit to frozen sheets. See {sentfyi}, {smallnum}.",
    "Brief estimates versus findings: P0 read Table 1 \"RabakBench 88.1\" (wrong, 88.1 is Singlish); P0 file lists omitted a notebook; the licence file is in all four repos, not three; Sentinel docs are reachable now (200). Recorded in BR and INV-RN 2 as corrections. See {f1head}, {notebook}.",
    "Not conflicts, no item: the playbook's \"accessible through the Sentinel API\" and the blog's tldr are hosted facts that stay under Sentinel; the two datasets' licence fields (license other, govtech-singapore) match the model repos.",
]
for i, c in enumerate(cont, 1):
    w("%d. %s" % (i, ref(c)))
w("")
w("Cross-draft values compared and found consistent (by reading, not by execution): model pins and shas; created and last-modified dates; parameter counts 848,942 and 259,118 and file sizes; input widths 3072, 3072, 768; output keys (11) and taxonomy wording; package pins per variant; demo bands 0.4 and 0.7 and the 0.5 chat threshold; paper figures 77.0, 88.1, 87.8, 78.4, 66.6 and 87.1; blog 2.1 figures (0.7318, 0.8618, 0.8420, 0.7267, 0.8688, 1.0000, 0.7397); Sentinel token limits 8192, 2048, 2048; layer arithmetic (786,688 + 32,896 + 7 x 4,194 = 848,942; 196,864 + 32,896 + 29,358 = 259,118) re-derived in this triage; column header across BR, A and INV.")
w("")

open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("items", n, dict(cc), dict(ch), dict(cp), "cp1", len(cp1), "gap", len(gap), "H", len(hs))
for d in hs:
    print(d["id"], d["cls"], d["item"][:90])
