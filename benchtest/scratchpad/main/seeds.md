# Product seeds (main fills before P0; explorers confirm and correct at P0)

Each entry gives the explorer a starting point. **UNVERIFIED** marks a starting guess that P0 must confirm or correct, after which main updates the entry and drops the mark. Seeds are not evidence. Cite only the official pages themselves.

## presidio (B1) — P0 DONE in the dry run, VERIFIED 2026-10-09
- **Owner:** created by Microsoft. Now the independent, community-governed `data-privacy-stack` org; the transition page states the move. Whether the successor is official, and the prefix, are open: Q01, user at CP1. Provisional prefix: `Presidio:`.
- **Docs:**
  - https://data-privacy-stack.github.io/presidio/
  - https://microsoft.github.io/presidio/ (now a redirect stub)
  - https://presidio.dataprivacystack.org (also 200; its relationship to the docs site is to be checked)
- **Repo:** `data-privacy-stack/presidio`. `microsoft/presidio` 301s to it. Pin: tag `2.2.364` (779dbd28, 2026-07-22). MIT licence. Docker images moved from MCR to ghcr.io.
- **Context7 (locator only):** `/data-privacy-stack/presidio`. Ignore `/websites/deepwiki_*` and the Guardrails AI validators.
- **P0 note:** `scratchpad/explorer/20261009_presidio_p0.md`. It proposes 6 columns PD1–PD6 and inventory blocks for components, recognizer families, operators and integrations.
- **Caveats:**
  - The supported-entities page lists country entities that `default_recognizers.yaml` disables.
  - Python 3.10–3.13 is stated on the install page, but 3.14 appears in the release notes.
  - No published accuracy, latency or threshold was found.
  - NeMo's PII columns wrap Presidio: two_level_v2.md "Column E" (input-level PII detection & masking, line 509) and "Column F" (output-level, line 611). K/L are tool-call/tool-result validation (corrected at presidio P1). Cross-reference; never duplicate.
  - Docs host chain (P1, 2026-10-09): data-privacy-stack.github.io/presidio/ → 301 → presidio.dataprivacystack.org/ (cite the final host). Deployed site ≠ docs/ at tag 2.2.364 (Python 3.10–3.13 live vs 3.10–3.14 at tag).
  - github.com via fetch_text.py returned 403 at P1; cite code from a shallow clone at the tag with blob URLs. Clone form that matches the allow-list: `git clone --depth 1 <url> /tmp/<name>`.

## modelarmor (B1) — VERIFIED at P0 2026-10-09
- **Owner:** Google Cloud. Own docs section: https://docs.cloud.google.com/model-armor/ (overview: /model-armor/overview). The old cloud.google.com/security-command-center/docs/model-armor-overview path 301s there; cloud.google.com/model-armor/docs is 404. No repo; pin docs by date read.
- **Pricing:** https://cloud.google.com/security/products/model-armor and https://cloud.google.com/security-command-center/pricing. **Quotas:** /model-armor/quotas. **Release notes:** /model-armor/release-notes. **Regions:** /model-armor/feature-availability-by-region, /model-armor/data-residency (asia-southeast1 is limited-support).
- **P0 note:** `scratchpad/explorer/20261009_modelarmor_p0.md` (S1–S24, 12 gaps, 9 conflicts). Proposes MA1–MA10; antivirus and MCP screening default to inventory (q01, CP1).
- **Caveats:** Vertex AI is now "Gemini Enterprise Agent Platform" in docs; release notes may carry next-day dates (C9); GoogleCloudPlatform GitHub samples 403 (R013).
- **Cross-reference:** SDP (R012).

## sdp (B1) — UNVERIFIED
- **Owner:** Google Cloud Sensitive Data Protection, formerly Cloud DLP. Docs start: https://cloud.google.com/sensitive-data-protection/docs (UNVERIFIED).
- **What to confirm:**
  - inspection (infoTypes, custom infoTypes, likelihood);
  - de-identification transformations (masking, tokenisation/FPE, date shifting, bucketing) and re-identification;
  - content methods (`content:inspect` and `content:deidentify`) vs storage jobs (scope guide: storage scanning → inventory only);
  - image redaction;
  - Singapore infoTypes;
  - client libraries;
  - pricing and quotas.
- **Cross-reference:** Model Armor; Presidio (PII); Sentinel AF (AWS PII).

## purplellama (B2) — UNVERIFIED (see R004)
- **Repo:** `meta-llama/PurpleLlama`. The baseline Llama Guard research pinned 172c1074; re-pin to the latest commit or tag. Sub-folders to confirm: Prompt Guard, LlamaFirewall, CodeShield, CyberSecEval.
- **Docs start:** https://www.llama.com/docs/ or https://dev.meta.ai/llama/ protections pages. The Llama Guard research used `dev.meta.ai/llama/llama-protections/` (UNVERIFIED current URL).
- **Hugging Face:** `meta-llama/Prompt-Guard-86M` (v1, legacy) and `meta-llama/Llama-Prompt-Guard-2-86M` / `-22M` (UNVERIFIED names). These are gated, so expect 401/403.
- **Papers:** a LlamaFirewall paper and the CyberSecEval series on arXiv (UNVERIFIED ids).
- **Existing work to reuse:** `drafts/lg_*` (Llama Guard columns V–Z, sheet 3d). The Llama Guard research noted Meta points to Prompt Guard 2 for jailbreak and injection.

## lionguard (B2) — VERIFIED from Sentinel research (R005)
- **Hugging Face:** `govtech/lionguard-v1` (legacy), `govtech/lionguard-2` (@be4e38c9), `govtech/lionguard-2.1` (@1c3a9ea7), `govtech/lionguard-2-lite` (@d56c17a0). Not gated. Licence: govtech-singapore (MIT + Singapore law/SIAC).
- **Papers:** arXiv 2407.10995 (LionGuard 1) and 2507.15339 (LionGuard 2). Blogs: blog.ai.gov.sg (LionGuard 2 post, 21 Aug 2026 retraining post, 28 Sep 2026 Jev/Kev 2.1 evaluation post).
- **Playbook:** https://govtech-responsibleai.github.io/playbook/tools/lionguard/ (source `govtech-responsibleai/playbook`, staging branch @45908b48).
- **Existing work to reuse:** `drafts/sentinel_*` (SN1, sheet 3e blocks (a) and (c)). Re-check at source; don't copy blindly.

## cloak (B3) — UNVERIFIED
- **Owner:** GovTech, a PII service. Known mention: the playbook privacy-improvements page says the Sentinel integration is "coming soon" (`sentinel_resolutions_2.md` T59).
- **What to confirm:** whether any public docs exist (developer.tech.gov.sg product pages, aiguardian.gov.sg, the playbook). Expect sparse docs; honest gaps (R007 item 6).

## litmus (B3) — UNVERIFIED (R003: eval sheet only)
- **Owner:** GovTech, described in Sentinel's docs as the "WOG AI Testing product" paired with Sentinel. Start from aiguardian.gov.sg (the Litmus pages next to the Sentinel docs; the Sentinel getting-started page mentions the "Litmus and Sentinel interest form") and developer.tech.gov.sg.
- **Expected outcome:** sparse public docs; honest gaps. Sheet format follows `drafts/eval_tooling.md`.
