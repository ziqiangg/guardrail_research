# Resolutions, agent 2 of 3: licensing and model identity

Date checked: 2026-10-07. Sources are official only (NVIDIA docs, NVIDIA model cards on Hugging Face and build.nvidia.com, vendor sites, publisher model cards, official GitHub repos). WebFetch returns summaries, so quotes are as returned by the fetch; the decisive ones were re-asked for verbatim text.

## Ids taken
- Class (a), model identity and taxonomy: a6, a7, a8, a9, a10, a18, a21. Llama Guard model type naming (`llama_guard` vs `llama_guard_2`) has no triage id, so it is reported as x1.
- Class (c), all: c1 to c13.
- Not taken (other agents): a1 to a5, a11 to a17, a19, a20, a22 to a51.

## Resolutions

id | old statement (short) | old label | finding (≤ 40 words) | new label | source URL | verbatim quote (≤ 25 words) | status

a6 | Authoritative content-safety category list (S1-S22 vs S1-S23) | TBV / R8 | Depends on model. Safety Guard v3 card lists S1-S23 (23 categories); Reasoning-4B card says S1-S22. The content-safety docs page enumerates no numbered categories. | [Documented: vendor site] (publisher model cards) | https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 ; https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B | "S22: Illegal Activity. S23: Immoral/Unethical." (v3 card); Reasoning-4B: 22 safety categories (S1-S22), as returned by fetch | resolved (per model; docs page itself silent, checked https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/content-safety.html, not stated)

a7 | Is Nemotron Safety Guard v3 named on the content-safety page | TBV / R8 | Yes. The page's model reference uses the v3 model id; it also names Nemotron Content Safety Reasoning, llama-3.1-nemoguard-8b-content-safety, Llama Guard, ShieldGemma and gpt-oss-safeguard. | [Documented] | https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/content-safety.html | `model: nvidia/llama-3.1-nemotron-safety-guard-8b-v3` | resolved

a8 | Jailbreak definition / taxonomy and model-flow coverage (NemoGuard JailbreakDetect) | ND+TBV / R8 | No taxonomy and no formal jailbreak definition on either the NVIDIA docs page or the model card. Model card only says it identifies attempts to jailbreak LLMs; classifier works on pre-computed embeddings. | keep [Not disclosed] | https://huggingface.co/nvidia/NemoGuard-JailbreakDetect ; https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/jailbreak-protection.html | Fetch result: model "identifies attempts to jailbreak large language models"; "no detailed taxonomy" (absence, not a quote) | still open (checked both URLs, not stated)

a9 | JailbreakDetect NIM decision threshold | ND | Model card gives F1/FPR/FNR but no decision threshold. Docs page gives defaults only for the heuristic perplexity thresholds, not for the model. | keep [Not disclosed] | https://huggingface.co/nvidia/NemoGuard-JailbreakDetect | Evaluation lists "False Positive Rate 0.0042"; no decision threshold stated (fetch summary) | still open (checked model card and jailbreak-protection docs page, not stated)

a10 | JailbreakDetect NIM training data | ND | Model card: combination of three open datasets, de-duplicated. Fetch of the card named Advbench, Wildjailbreak, jackhao/jailbreak-classification. NVIDIA docs page instead says AdvBench, ToxicChat, JailbreakChat plus 1000 Dolly-15k examples. The two NVIDIA sources disagree. | [Documented] (with conflict noted) | https://huggingface.co/nvidia/NemoGuard-JailbreakDetect ; https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/jailbreak-protection.html | "A combination of three open datasets, mixed together, de-duplicated, and reviewed for data quality." | partially (dataset lists conflict between model card and docs page; random forest confirmed by both)

a8b | (part of a8/a9 asks) Is JailbreakDetect a random forest | n/a | Yes. Model card architecture is Random Forest on 768-d snowflake-arctic-embed-m-long embeddings; docs page agrees. | [Documented] | https://huggingface.co/nvidia/NemoGuard-JailbreakDetect | "Architecture Type: Random Forest" | resolved

a18 | Content-safety model language coverage | R8 | Safety Guard v3: 9 languages (English, Spanish, Mandarin, German, French, Hindi, Japanese, Arabic, Thai), zero-shot over 20 more. Reasoning-4B: English only. llama-3.1-nemoguard-8b-content-safety NIM page states no languages. | [Documented: vendor site] | https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 | "It supports 9 languages: English, Spanish, Mandarin, German, French, Hindi, Japanese, Arabic, and Thai." | partially (NemoGuard 8B content-safety v1 languages not stated on https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html)

a21 | Custom topic-control models | R8 | Topic-control docs page names only llama-3.1-nemoguard-8b-topic-control and does not address custom models. The model card says it takes a custom system instruction of allowed or disallowed topics (custom topics, not custom models). | [Documented] (topics only) | https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control | "a system instruction which acts like a topical instruction with the rules that define the context" | partially (custom models: checked https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/topic-control.html, not stated)

x1 | Llama Guard model type naming (`llama_guard` vs `llama_guard_2`) | n/a (no triage id) | The content-safety docs page config example uses type `llama_guard_2` with Meta-Llama-Guard-2-8B. Whether `llama_guard` (v1) is still valid in v0.24.1 code was not checked (repo is another agent's scope). | [Documented] | https://docs.nvidia.com/nemo/guardrails/latest/configure-guardrails/guardrail-catalog/content-safety.html | `type: llama_guard_2 / engine: openai / model: meta-llama/Meta-Llama-Guard-2-8B` | partially (docs naming resolved; code-level `llama_guard` validity not checked)

c1 | NIM production licence terms (AI Enterprise needed or not): content-safety, topic-control, JailbreakDetect NIMs | R8 | NVIDIA states governing terms for the NIM container and model, but no page checked says AI Enterprise is required or not for production. NIM docs home says only "Part of NVIDIA AI Enterprise". | [Documented] (terms only) | https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety ; https://docs.nvidia.com/nim/llama-3-1-nemoguard-8b-contentsafety/latest/index.html | "Use of the NIM container is governed by the NVIDIA Software License Agreement and the Product-Specific Terms for NVIDIA AI Products" | partially (AI Enterprise requirement: checked https://docs.nvidia.com/nim/index.html and https://www.nvidia.com/en-us/data-center/products/ai-enterprise/, not stated; topic-control and JailbreakDetect NIM pages not separately checked)

c2 | Licence terms for Nemotron Safety Guard v3 and Reasoning-4B | R8 | v3: nvidia-open-model-license (card also references Llama 3.1 Community License per fetch). Reasoning-4B: NVIDIA Open Model License plus Gemma Terms of Use and Prohibited Use Policy. Open-weight, with terms. | [Documented: vendor site] | https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3 ; https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B | "Use of this model is governed by the NVIDIA Open Model License, Gemma Terms of Use and Gemma Prohibited Use Policy." (Reasoning-4B) | resolved

c3 | Paid status of content-safety vendors (ActiveFence, Cisco AI Defense, Prompt Security, Fiddler, CrowdStrike AIDR, Trend Micro, GCP Text Moderation) | TBV / R8 | NVIDIA docs show API keys only, no pricing. Vendor sites: ActiveFence (now alice.io) demo only; Cisco "Request a demo", no price; Prompt Security demo only; Fiddler has Free, $0.002 per trace Developer and Enterprise contact-sales tiers; CrowdStrike AIDR requires AIDR subscriptions, "contact us"; Trend: free trial and contact, no price shown. GCP price not retrieved. | [Documented: vendor site] | https://alice.io/ ; https://www.cisco.com/site/us/en/products/security/ai-defense/index.html ; https://prompt.security/ ; https://www.fiddler.ai/pricing ; https://aidr-docs.crowdstrike.com/docs/aidr/ ; https://www.trendaisecurity.com/en-us/platform | Fiddler: "$0.002 per trace" (Developer tier); Cisco CTA "Request a demo"; CrowdStrike: "Requires one or more of these subscriptions" | partially (GCP Text Moderation: https://cloud.google.com/natural-language/pricing fetch truncated, price not seen; Trend "AI Guard" not named on checked page)

c4 | Licensing of Clavata and PolicyAI | TBV | Not retrieved. clavata.ai fetch failed (SSL handshake error); PolicyAI vendor is Musubi (musubilabs.ai per search), site not fetched. | keep [To be verified] | https://www.clavata.ai/ (failed) | none | still open (checked https://www.clavata.ai/, fetch error; musubilabs.ai not fetched)

c5 | Guardrails AI and HF classifier confirmed open-source | TBV | Guardrails AI repo shows Apache-2.0. HF classifier depends on the chosen model; NVIDIA docs say only it runs locally via transformers or remote server. Model not chosen, so its licence is open. | [Documented: vendor site] | https://github.com/guardrails-ai/guardrails | "Apache-2.0" (repo badge) | partially (HF classifier model licence depends on chosen model)

c6 | GLiNER-PII NIM: paid status / licence, open or not | TBV / R8 | Model card: NVIDIA Open Model License. build.nvidia.com page also shows API Trial Terms for the hosted endpoint and "ready for commercial/non-commercial use". NIM container terms and AI Enterprise requirement not stated. NVIDIA PII docs page names the NIM with hosted or local container options. | [Documented: vendor site] | https://huggingface.co/nvidia/gliner-PII ; https://build.nvidia.com/nvidia/gliner-pii | "Use of this model is governed by the NVIDIA Open Model License Agreement." | partially (open-weight, NVIDIA Open Model License; container paid/AI Enterprise status: checked https://build.nvidia.com/nvidia/gliner-pii, not stated)

c7 | Private AI pricing / paid status | TBV / R8 | private-ai.com redirects to getlimina.ai (Limina). Pricing page shows Starter (free, up to 75 API calls daily), Batch (quote), Enterprise (custom). Proprietary SaaS with a limited free tier. | [Documented: vendor site] | https://getlimina.ai/en/pricing | "Up to 75 API calls daily" (Starter, Free) | resolved (as of redirect; brand now Limina)

c8 | Polygraf licensing and pricing | TBV / R8 | polygraf.ai returned HTTP 403 and platform-overview 403 to fetch. Search result snippets suggest custom enterprise pricing, but that was not read on the official page. | keep [To be verified] | https://www.polygraf.ai/platform-overview/ (403) | none | still open (checked https://polygraf.ai/ and platform-overview, HTTP 403)

c9 | Presidio open-source confirmation | TBV | Presidio repo is MIT-licensed. | [Documented: vendor site] | https://github.com/microsoft/presidio | MIT badge: `license-MIT-brightgreen` | resolved

c10 | YARA open-source confirmation | TBV | VirusTotal/yara repo shows BSD-3-Clause. yara-python licence not checked. | [Documented: vendor site] | https://github.com/VirusTotal/yara | "BSD-3-Clause" (fetch result of repo licence) | partially (yara-python licence not checked)

c11 | Paid status of fact-check vendors (Patronus API, Fiddler, AutoAlign, Cleanlab) | TBV / R8 | Fiddler: Free / $0.002 per trace / Enterprise tiers (see c3). AutoAlign site shows only demo CTAs and no price (page looks like an industrial-AI product, unconfirmed as the guardrails vendor). Cleanlab pricing page 404. Patronus docs pricing returned 401; search snippet (non-official) mentions usage-based pricing, not used. | [Documented: vendor site] (Fiddler only) | https://www.fiddler.ai/pricing | "$0.002 per trace" | partially (Fiddler resolved; AutoAlign: https://autoalign.ai/ no price; Cleanlab: https://www.cleanlab.ai/pricing/ 404; Patronus: https://docs.patronus.ai/docs/usage-based-pricing 401)

c12 | AlignScore licence (open-source self-hosted; model licence) | TBV / R8 | Repo is MIT-licensed. No separate checkpoint licence stated on the repo page. | [Documented: vendor site] | https://github.com/yuh-zha/AlignScore | Repo "licensed under the MIT License" (fetch summary of repo page) | partially (checkpoint licence: checked repo page, not stated; Hugging Face checkpoint card not checked)

c13 | Patronus Lynx open-weight licence | TBV | Lynx 8B card licence field is cc-by-nc-4.0 (Creative Commons Attribution-NonCommercial 4.0). Open-weight but non-commercial. | [Documented: vendor site] | https://huggingface.co/PatronusAI/Llama-3-Patronus-Lynx-8B-Instruct | `cc-by-nc-4.0` | resolved (8B Instruct card; other Lynx sizes not checked)

x2 | (extra, in scope list) Llama Guard and ShieldGemma licences | n/a | Llama Guard 3 8B: licence llama3.1 (Llama 3.1 Community License). ShieldGemma-2b: licence gemma (Gemma Terms, Prohibited Use Policy). | [Documented: vendor site] | https://huggingface.co/meta-llama/Llama-Guard-3-8B ; https://huggingface.co/google/shieldgemma-2b | "License: llama3.1" ; "License: gemma" | resolved (those two versions; Llama Guard 2 card not checked)

x3 | (extra) NemoGuard content-safety, topic-control, JailbreakDetect weight licences | n/a | Content-safety 8B LoRA weights: NVIDIA Open Model License Agreement (page also lists NVIDIA Community License for hosted API, and Llama 3.1 Community License as supplementary). Topic-control: NVIDIA Open Model License plus Llama 3.1 Community License. JailbreakDetect: NVIDIA Open Model License. | [Documented: vendor site] | https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety ; https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-topic-control ; https://huggingface.co/nvidia/NemoGuard-JailbreakDetect | "Use of this model is governed by the NVIDIA Open Model License Agreement." | resolved

## Vendor flag table

vendor | flag to use | source
---|---|---
NVIDIA NIM containers (content-safety, topic-control, JailbreakDetect, GLiNER-PII) | licensing to be verified (container under NVIDIA Software License Agreement; AI Enterprise requirement not stated on pages checked) | https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety
Nemotron Safety Guard v3 | open-weight NVIDIA Open Model License | https://huggingface.co/nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3
Nemotron Content Safety Reasoning 4B | open-weight NVIDIA Open Model License + Gemma terms | https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B
NemoGuard content-safety 8B / topic-control 8B / JailbreakDetect | open-weight NVIDIA Open Model License (Llama 3.1 terms also apply to the two Llama-based models) | URLs in x3
GLiNER-PII | open-weight NVIDIA Open Model License; NIM container terms to be verified | https://huggingface.co/nvidia/gliner-PII
Llama Guard 3 | open-weight Llama 3.1 Community License | https://huggingface.co/meta-llama/Llama-Guard-3-8B
ShieldGemma | open-weight Gemma Terms | https://huggingface.co/google/shieldgemma-2b
Patronus Lynx | open-weight cc-by-nc-4.0 (non-commercial) | https://huggingface.co/PatronusAI/Llama-3-Patronus-Lynx-8B-Instruct
AlignScore | open-source MIT (repo); checkpoint licence to be verified | https://github.com/yuh-zha/AlignScore
YARA | open-source BSD-3-Clause | https://github.com/VirusTotal/yara
Presidio | open-source MIT | https://github.com/microsoft/presidio
Guardrails AI | open-source Apache-2.0 | https://github.com/guardrails-ai/guardrails
ActiveFence (now alice.io) | paid / non-OSS service (demo only, no public price) | https://alice.io/
Cisco AI Defense | paid / non-OSS service (request a demo) | https://www.cisco.com/site/us/en/products/security/ai-defense/index.html
Prompt Security | paid / non-OSS service (demo; platform pricing via sales) | https://prompt.security/
Fiddler Guardrails | paid / non-OSS service with free tier (Free, $0.002 per trace, Enterprise custom) | https://www.fiddler.ai/pricing
CrowdStrike AIDR | paid / non-OSS service (subscription, contact) | https://aidr-docs.crowdstrike.com/docs/aidr/
Trend Micro Vision One (TrendAI) | paid / non-OSS service (free trial, contact; no price shown) | https://www.trendaisecurity.com/en-us/platform
Private AI (now Limina) | paid / non-OSS service with free Starter tier | https://getlimina.ai/en/pricing
GCP Text Moderation | licensing to be verified (price not retrieved) | https://cloud.google.com/natural-language/pricing
Polygraf | licensing to be verified (site returned 403) | https://polygraf.ai/
Clavata | licensing to be verified (site fetch failed) | https://www.clavata.ai/
PolicyAI (Musubi) | licensing to be verified | none
AutoAlign | licensing to be verified (no price on page checked) | https://autoalign.ai/
Cleanlab | licensing to be verified (pricing page 404) | https://www.cleanlab.ai/pricing/
Patronus API | licensing to be verified (official pricing doc returned 401) | https://docs.patronus.ai/docs/usage-based-pricing

## Counts per status (rows above, including a8b and x1 to x3)

- resolved: 9 (a6, a7, a8b, c2, c7, c9, c13, x2, x3)
- partially: 11 (a10, a18, a21, x1, c1, c3, c5, c6, c10, c11, c12)
- still open: 4 (a8, a9, c4, c8)
- contradicted: 0
- Total 24 rows.

Notes
- a10: the two NVIDIA sources disagree on training datasets; not labelled contradicted because the model card wording ("three open datasets") is generic, but the bench should cite the model card and flag the docs page.
- WebFetch summaries were used for most quotes; GCP, Polygraf, Clavata, Cleanlab and Patronus official pages were unreachable.
