# Llama Guard resolutions 2: chat templates, custom categories, tool-call format, integrations and code

Items covered: T13, T14, T18, T19, T23, T28, T29, T30, T31, T32, T33, T34, T35, T37, T38, T51, T54, T55 (18 items). Date of checks: 2026-10-08.

## Method and pins (read first)

No summarising fetch was used for any quote below. Every quote is from raw text.

- **GitHub repos**: whole-repo tarballs from codeload.github.com at pinned refs, then local grep and read. Blob pages on github.com and api.github.com (commits, trees, tags) were also reachable. raw.githubusercontent.com was not used.
- **Meta docs (dev.meta.ai)**: raw HTML fetched with curl and stripped to text (DOCS3 = llama-guard-3, DOCS4 = llama-guard-4, PROT = llama-protections).
- **Hugging Face**: raw files (README.md, tokenizer_config.json, chat_template.json) return HTTP 401 for all five gated repos. The public HF model-metadata API, https://huggingface.co/api/models/meta-llama/<model>, does return the repo's `tokenizer_config.json` content including `chat_template` (and `chat_template_jinja` for LG4). That is how the chat templates were read. Revisions seen: Llama-Guard-3-8B 7327bd9f6efbbe6101dc6cc4736302b3cbb6e425; Llama-Guard-3-8B-INT8 951579e66b562c4ca221903eaae3378f4abfa6af; Llama-Guard-3-1B acf7aafa60f0410f8f42b1fa35e077d705892029; Llama-Guard-3-11B-Vision 62d4275543ec7503de66c486de1c0c2103e365ac; Llama-Guard-4-12B 87acb4b94e930c3d679e6e7ee9d57e2feab9ea71. Label to use for these: [Documented] with "(HF repo tokenizer_config via HF metadata API; raw file 401)" in text after the bracket. The README text of the HF cards was NOT read (401), so "not shown on the card" claims rest on the PurpleLlama card mirror only.
- **Refs to substitute** (short forms for labels, full ids for R9 URLs):

| Repo | Label ref | Full commit |
|---|---|---|
| meta-llama/PurpleLlama | 172c1074 | 172c1074069eb88ec834124272c1b1c4f8893445 |
| meta-llama/llama-cookbook | 2f22a9eb | 2f22a9eb030f92d0e99227e57e9a1123af1f9532 (also the head of main on 2026-10-08) |
| ogx-ai/ogx tag v0.4.4 | v0.4.4 | 3b50471cf489397b8fd7c33a8685b2e9f05b1ede |
| ogx-ai/ogx main (pinned) | f8051dd6 | f8051dd655358415c6aee152c290622b607bf6ab (head of main on 2026-10-08, committed 2026-10-08T00:21Z) |
| NVIDIA-NeMo/Guardrails tag v0.24.1 | v0.24.1 | 5d81d6700e713018e3b74065f8b1f56d1051f290 (annotated tag object 4004122c...) |
| NVIDIA-NeMo/Guardrails develop (T35 only) | develop@9f793de5 | 9f793de53e432c4c9c765975f5dd54df175fcb6e |
| meta-llama/llama-models main (pinned, T51) | 0e0b8c51 | 0e0b8c519242d5833d8c11bffc1232b77ad7f301 |

---

## Per-item resolutions

### T13 - Custom categories via chat template for LG4
- Verdict: **CORRECTION** (draft says "not documented / not found for LG4"; the LG4 chat template does read both arguments. No Meta card or doc page shows an LG4 usage snippet).
- Evidence:
  - LG4 template, https://huggingface.co/api/models/meta-llama/Llama-Guard-4-12B (field `chat_template_jinja`; revision 87acb4b9): `{%- if categories is not defined -%}` ... default dicts follow ...; later `{%- for key in categories -%}{%- if key not in excluded_category_keys -%}{{ key + ": " + categories[key] + "\n" }}`.
  - Offline render of that template (jinja2 3.1.6, my own run, not Meta text): with `categories={"S1": "My custom category."}` the prompt category block is only `S1: My custom category.`; with `excluded_category_keys=["S6"]` S6 is dropped and the other 13 remain.
  - DOCS4, https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/llama-guard-4/ : "The default categories and their descriptions are shown below. These can be customized for zero-shot or few-shot prompting."
  - PurpleLlama LG4 MODEL_CARD.md @172c1074 has no `categories`, `excluded_category_keys` or `apply_chat_template` text (grep). The cookbook @2f22a9eb has no LG4 text at all (grep for Guard-4 / LLAMA_GUARD_4: no hit).
  - Template default for LG4 text-only: S1-S14. When any message has an image, the default list is S1-S13 (S14 omitted). Custom `categories` replace both defaults.
- Label to use: [Documented] (HF template file); the "no Meta card or doc shows it" part is [Not disclosed]; "works as intended on real inputs" stays [To be verified] (T15, needs a run).
- Draft impact:
  - **lg_cols_b.md LG5 R1 Summary (line 197) must change** (new text in the Summary section below).
  - lg_cols_b.md LG5 R4 line 218 (bullet "The 3-8B and LG4 HF pages (via summarising fetch)...") replace with these bullets:
    - "The 3-1B, 3-11B-Vision and Llama Guard 4 chat templates (tokenizer config, read through the Hugging Face metadata API) use an optional `categories` dict and an optional `excluded_category_keys` list **[Documented]**"
    - "The Llama Guard 4 template defaults to S1 to S14 for text-only conversations and S1 to S13 when an image is present; a custom `categories` dict replaces either default **[Documented]**"
    - "No Meta card or docs page shows a Llama Guard 4 snippet that passes `categories` or `excluded_category_keys`; the Hugging Face README was not readable (gated, 401) **[Not disclosed]**"
  - lg_cols_b.md LG5 R4 line 219 ("Whether the 3-8B or LG4 chat templates accept these arguments ... [To be verified]") delete (replaced by the bullets above and by T14).
  - lg_cols_b.md LG5 R7 line 250 (LG4 bullet) -> "Llama Guard 4: pass the same `categories` and `excluded_category_keys`; the template reads them, so record whether verdicts follow the custom text, and note the LG4 template expects message content as a list of typed parts (a plain string content renders an empty conversation) **[Inferred]**". The last clause is from my offline render.
  - lg_cols_b.md LG5 R8: delete lines 254-255 bullets "Support for categories ... on 3-8B and LG4 chat templates" and "Any documented LG4 custom-policy guidance or results (none found)"; add "Any Meta page or card showing Llama Guard 4 custom-category usage (the template supports it; no page shows it)". R8 Summary (line 252) changes.
  - lg_cols_a.md LG1 R8 line 105 ("Whether LG4 supports custom category text via the chat template (documented for LG3-1B, not found for LG4)") -> "Whether Meta documents LG4 custom categories on a card or docs page (the chat template accepts them; no page shows it)". lg_cols_a.md LG2 R8 line 217 (same bullet) same replacement.
  - lg_inventory.md (a) LG4 row, "Custom categories documented" cell: replace the "[Not found]" clause with "The chat template reads optional categories and excluded_category_keys [Documented] (HF template via metadata API). No card, cookbook or docs snippet shows their use for LG4 [Not disclosed]". Add in the Modality or Taxonomy cell: "template default is S1-S14 for text, S1-S13 when an image is present [Documented]".
  - lg_inventory.md (c) HF transformers row, "Categories configurable" cell: "1B, 11B-V and LG4: categories dict and excluded_category_keys read by the chat template [Documented]. 8B / INT8: not accepted (fixed list), see T14".
  - R9 of LG5 (B line 258 onwards): add https://huggingface.co/api/models/meta-llama/Llama-Guard-4-12B (template source).
  - Reviewer note to add: the LG4 template contains a literal backslash-n pair after each message text, outside any Jinja string, so a rendered prompt contains the two characters `\n` twice after the message text instead of newlines (seen in my offline render, jinja2 3.1.6; HF's own renderer not run). **[Inferred]**; worth a one-line check when testing.

### T14 - 3-8B and 3-8B-INT8 chat templates and custom categories
- Verdict: **RESOLVED** (the 3-8B and 3-8B-INT8 templates do NOT accept custom or excluded categories; the list is hard-coded).
- Evidence:
  - 3-8B template, https://huggingface.co/api/models/meta-llama/Llama-Guard-3-8B (revision 7327bd9f): the category block is inside one string literal: `S1: Violent Crimes.\nS2: Non-Violent Crimes.\nS3: Sex Crimes. ... S13: Elections.\nS14: Code Interpreter Abuse.\n<END UNSAFE CONTENT CATEGORIES>`. The words `categories` (as a variable) and `excluded_category_keys` do not occur in the template.
  - 8B-INT8 template (revision 951579e6) is byte-identical to the 8B template (cmp).
  - Offline render with `categories=` and `excluded_category_keys=["S6"]` passed: output still lists S1-S14 including S6 (my run).
  - 8B template expects string content: `content.strip()`; list-of-parts content raises an error in my render ("'list object' has no attribute 'strip'").
  - The supported way for 3-8B: cookbook notebook llama_guard_customization_via_prompting_and_fine_tuning.ipynb @2f22a9eb, cell 5: `model_id: str = "meta-llama/Llama-Guard-3-8B"` with `build_custom_prompt(... prompt_template = PROMPT_TEMPLATE_3, with_policy = True)`.
  - Bonus (T26): the INT8 template lists S14, which supports INV(a) 3-8B-INT8 S14 = Yes with an official repo file instead of a summarised intro.
- Label to use: [Documented] (HF template); cookbook route [Documented: repo meta-llama/llama-cookbook@2f22a9eb]; the "silently ignores" behaviour is [Inferred] (offline render).
- Draft impact:
  - lg_cols_b.md LG5 R4 line 219 [To be verified] bullet -> "The 3-8B and 3-8B-INT8 chat templates hard-code S1 to S14 and read no categories or excluded keys; extra arguments are ignored (offline render) **[Documented]**" (split: first clause [Documented], "ignored" clause [Inferred]). Add bullet: "For 3-8B, custom categories go through the cookbook builder with policy text (customization notebook uses Llama-Guard-3-8B) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**".
  - lg_cols_b.md LG5 R4 Summary and R7/R8: see Summary section; B R7 add "3-8B: confirm that `categories` passed to the chat template changes nothing, then use the cookbook builder **[Inferred]**".
  - lg_inventory.md (a) 3-8B row "Custom categories documented" cell: replace "`categories=` shown on the 1B card, not seen on the 8B card [To be verified]" with "The chat template has a fixed S1-S14 list and does not read categories or excluded_category_keys [Documented] (HF template via metadata API). Custom text only via the cookbook builder [Documented: repo meta-llama/llama-cookbook@2f22a9eb]". 3-8B-INT8 row cell: replace "Same generic statement as 3-8B" with "Same fixed template as 3-8B (identical file) [Documented]". INV(a) 3-8B-INT8 Taxonomy cell: `[Documented: HF intro, summarised]` -> "[Documented] (chat template lists S14)".
  - lg_inventory.md (c) HF row Categories cell: as in T13.

### T18 - Customization notebook contents and path
- Verdict: **RESOLVED**
- Evidence (notebook read in full at 2f22a9eb, getting-started/responsible_ai/llama_guard/llama_guard_customization_via_prompting_and_fine_tuning.ipynb):
  - It uses Llama Guard 3-8B: `model_id: str = "meta-llama/Llama-Guard-3-8B"`; prompts built with `build_custom_prompt(..., with_policy = True)`.
  - Sections: category list helper, category removal, custom category addition, evaluation on ToxicChat, fine-tuning on ToxicChat with PEFT.
  - Limit statement (cell 10): "unless fine-tuning is performed (see below) the category addition method will only work for topics closely related to existing categories."
  - Removal caveat (cell 8): "in some cases the model can still return unsafe when the corresponding category has is no longer part of the prompt."
  - Path: the 1B card (PurpleLlama @172c1074 line 12) links https://github.com/meta-llama/llama-recipes/blob/main/recipes/responsible_ai/llama_guard/llama_guard_customization_via_prompting_and_fine_tuning.ipynb , which returns HTTP 404 (checked 2026-10-08). The file exists at https://github.com/meta-llama/llama-cookbook/blob/2f22a9eb/getting-started/responsible_ai/llama_guard/llama_guard_customization_via_prompting_and_fine_tuning.ipynb (200). Its Colab badge points at `end-to-end-use-cases/responsible_ai/...`, which also 404s on cookbook main.
- Label to use: [Documented: repo meta-llama/llama-cookbook@2f22a9eb]
- Draft impact:
  - lg_cols_b.md LG5 R4 line 227 (3-1B card bullet; "its contents were not read") -> replace by:
    - "3-1B card links a customization notebook; the linked llama-recipes path returns 404 and the notebook now lives under getting-started/responsible_ai/llama_guard in the cookbook **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**"
    - "The customization notebook uses Llama Guard 3-8B with the cookbook builder: category removal, custom category addition, ToxicChat evaluation and PEFT fine-tuning **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**"
    - "Notebook caveat: without fine-tuning, an added category only works for topics close to existing categories (quote above) **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**"
  - lg_cols_b.md LG5 R8 line 256 (linked notebook path) delete. LG5 R9 add the notebook URL.

### T19 - Cookbook inference notebook (read in full)
- Verdict: **RESOLVED**
- Evidence (llama_guard_text_and_vision_inference.ipynb @2f22a9eb, all 13+ cells read):
  - Cell 0: "We showcase how to load the 1B text only and 11B vision models and run inference on simple inputs."
  - Cell 2: "The new templates support setting an arbitrary dictionary of categories or excluding the predefined categories by passing a list of the preexisting keys."
  - Cell 3: `tokenizer.apply_chat_template(prompt, return_tensors="pt", categories=categories, excluded_category_keys=excluded_category_keys)`; `max_new_tokens=20`, `output_scores=True`.
  - Cell 7 categories: `"S1": "Custom category 1. \n" + "AI models should not talk about custom category 1"`, `"S2": "This will be removed"`, `excluded_category_keys = ["S2"]`.
  - Cell 0 Colab badge path `end-to-end-use-cases/responsible_ai/llama_guard/...` does not exist in the repo.
  - Whole-repo grep at 2f22a9eb for `Llama-Guard-4`, `llama guard 4`, `LLAMA_GUARD_4`: no match, so no cookbook content covers LG4.
- Label to use: [Documented: repo meta-llama/llama-cookbook@2f22a9eb]
- Draft impact:
  - lg_cols_b.md LG5 R4 lines 220-221: change "has a Custom Categories section" wording to "read in full", and replace line 221 with "No file in the cookbook at this commit mentions Llama Guard 4 **[Documented: repo meta-llama/llama-cookbook@2f22a9eb]**".
  - lg_cols_b.md Reviewer notes line 280-282 sentence "The cookbook notebook was searched by pattern, not read in full" -> "was read in full".
  - lg_inventory.md (c) cookbook notebooks row: the three bare labels -> `[Documented: repo meta-llama/llama-cookbook@2f22a9eb]` (mapping table at the end); caveat "Notebook has no LG4 example" now whole-repo verified; keep Colab badge caveat.

### T23 - Serialisation of tool calls and tool outputs in the prompt
- Verdict: **STILL OPEN** (checked DOCS3 and DOCS4 raw, the five HF chat templates, PurpleLlama 8B/LG4 cards, cookbook prompt_format_utils.py and notebooks, llama-models, OGX v0.4.4 code, Llama API doc snapshot: no Meta source defines how a tool call or tool output is serialised for any Llama Guard version). The "Meta docs mention nothing about tools" statement is now confirmed from raw text, not a summary.
- Evidence:
  - DOCS3 and DOCS4 raw text (fetched 2026-10-08): case-insensitive search for "tool", "function call" and "ipython" finds nothing. Roles: "The possible roles can be  user and  assistant" (both pages). Prompt shows only `User:` and `Agent:` lines.
  - HF templates (all five): only `message['role'] == 'user'` -> `User` and `'assistant'` -> `Agent` are mapped. Offline render (my run): a `tool` message directly after the user turn is rendered with the previous role label ("Agent: result"); a `tool` message at index 2 raises "Conversation roles must alternate ...". 3-8B and INT8 call `content.strip()`, so list content or `content: None` (OpenAI assistant message with tool_calls) raises an error.
  - PurpleLlama 8B card (@172c1074): "For the tool use capability, we consider search tool calls and code interpreter abuse." (training data description only; no prompt format). LG4 card: "an additional category, Code Interpreter Abuse, for text-only tool-call use cases."
  - OGX v0.4.4 llama_guard.py line 353: `f"{m.role.capitalize()}: {interleaved_content_as_str(m.content)}"`. A tool message becomes a `Tool: <content>` line; assistant `tool_calls` arguments are not serialised, only `content`. Line 176-178: "since this might be a tool call, first role might not be user" then the first message is rewritten as a user message.
  - Llama API moderations doc (Wayback snapshot of the official Meta page, 2025-09-14, see T38): message types "UserMessage, SystemMessage, ToolResponseMessage, AssistantMessage"; tool message "Must be "tool" to identify this as a tool response". The doc does not say how those are rendered into the Llama Guard prompt.
- Label to use: [Not disclosed] for the serialisation; [Documented] for the role strings; [Documented: repo ogx-ai/ogx@v0.4.4] for OGX; [Inferred] for template behaviour on tool messages.
- Draft impact:
  - **lg_cols_b.md LG4 R1 Summary (line 112) and R6 Summary (line 160) must change** (new text in the Summary section).
  - lg_cols_b.md LG4 R3 line 135 (Meta docs ... via summarising fetch) -> two bullets: "Meta docs Llama Guard 3 and 4 pages (raw HTML): the roles listed are user and assistant; the words tool and function call do not appear **[Documented]**" ; "No Meta page, card, chat template or cookbook helper defines a tool role or the serialisation of tool calls or tool results for Llama Guard **[Not disclosed]**".
  - lg_cols_b.md LG4 R3 line 136 keep (the [Not disclosed] statement), append "; the Hugging Face templates map only user and assistant".
  - Add to LG4 R3 after line 137: "Hugging Face chat templates map only user to User and assistant to Agent; a tool-role message is not handled (offline render labels it with the previous role or raises an alternation error); 3-8B templates also require string content **[Inferred]**" and "Llama API moderations accepts system, user, assistant and tool messages; its prompt rendering is not described **[Documented]**".
  - lg_cols_b.md LG4 R6 line 164 keep [Not disclosed]; line 163 stays [Inferred].
  - lg_cols_b.md LG4 R8: line 184 ("Whether Meta docs mention a tool role (only a summarising fetch was available)") delete; line 180 keep, append "(raw Meta docs, templates, cookbook and OGX code checked; none defines it)".
  - lg_cols_b.md LG4 R7 line 173: keep the serialisation-variant test; add "include a Tool-label turn as OGX emits it ('Tool: ...') **[Inferred]**".

### T28 - OGX 1.0 `/v1/moderations`: replaced or removed
- Verdict: **CORRECTION** (A states "moderation is served by the OpenAI-compatible /v1/moderations endpoint" as OGX behaviour; OGX 1.x does not serve a moderations route).
- Evidence (all at ogx-ai/ogx@f8051dd6 unless noted):
  - docs/releases/RELEASE_NOTES_1.0.md (Release Date: May 2026): "The standalone Safety API has been removed. Content moderation is now served by the OpenAI-compatible `/v1/moderations` endpoint." and "Replace `run-shield` calls with `/v1/moderations`." The notes never mention Llama Guard (grep).
  - docs/blog/2026-06-23-guardrails-responses-api.md line 394-396: "seven safety providers (Llama Guard, Prompt Guard, Code Scanner, Bedrock, NVIDIA, SambaNova, Passthrough), and a standalone `/v1/moderations` proxy endpoint. All of that has been removed." Line 56: "This is the URL of any OpenAI-compatible `/v1/moderations` endpoint." Line 44: guardrails use "the configured moderation endpoint." (Blog line 50 says "six safety providers", line 394 says seven.)
  - Commit 5ad4753869 (2026-05-12), title: "refactor!: remove Safety API and replace with moderation_endpoint (#5291)".
  - Code on main: no `src/ogx/providers/inline/safety` or `src/ogx_api/safety` directory (tree listing of f8051dd6 has no path containing safety, moderation or llama_guard under src); grep of `src` for "/moderations" and "run_moderation" finds only the config description string and a docs link. At v0.4.4 the route existed: `src/llama_stack_api/safety.py` line 122 `@webmethod(route="/moderations", method="POST", level=LLAMA_STACK_API_V1)`.
  - Resolution of the apparent conflict: the release-notes sentence refers to an OpenAI-compatible `/v1/moderations` service that OGX calls (configured by `moderation_endpoint` on the builtin responses provider); the blog states OGX no longer serves its own `/v1/moderations`. `run_guardrails` in `src/ogx/providers/inline/responses/builtin/responses/utils.py` posts `{"input": messages}` to the configured URL.
- Label to use: [Documented: repo ogx-ai/ogx@f8051dd6] (all facts above); main pinned to f8051dd655358415c6aee152c290622b607bf6ab.
- Draft impact:
  - lg_cols_a.md LG1 R4 line 53 -> "OGX 1.0 (May 2026) removed the Safety API and the Llama Guard provider; the release notes say moderation moves to an OpenAI-compatible moderations endpoint, and the 2026-06-23 blog says OGX no longer serves that endpoint itself: Responses guardrails call an external endpoint set in config **[Documented: repo ogx-ai/ogx@f8051dd6]**".
  - lg_cols_a.md LG2 R4 line 170 second clause "OGX 1.0 (May 2026) removed the Safety API for `/v1/moderations`" -> split: keep the v0.4.4 facts in one bullet labelled `[Documented: repo ogx-ai/ogx@v0.4.4]`, and add "OGX 1.0 removed the Safety API; no moderations route or Llama Guard provider exists on main **[Documented: repo ogx-ai/ogx@f8051dd6]**".
  - lg_cols_a.md LG1 R9 line 124 and LG2 R9 line 237: replace URL with https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/releases/RELEASE_NOTES_1.0.md and add https://github.com/ogx-ai/ogx/blob/f8051dd655358415c6aee152c290622b607bf6ab/docs/blog/2026-06-23-guardrails-responses-api.md.
  - lg_inventory.md (c) OGX /v1/moderations row, Status cell (strip the bold and the embedded label): "removed from the OGX 1.x server. Release notes say the Safety API is replaced by an OpenAI-compatible /v1/moderations endpoint; the 2026-06-23 blog says the standalone endpoint was removed and Responses guardrails POST to a configured external endpoint; main has no moderations route [Documented: repo ogx-ai/ogx@f8051dd6]". Source cell: pin the three URLs to f8051dd6. Caveat cell stays.
  - lg_inventory.md (c) OGX provider row Status cell (line 50): strip bold; replace `[Documented: repo ogx-ai/ogx main, listing]` with `[Documented: repo ogx-ai/ogx@f8051dd6]`; fix "lists the Llama Guard provider among seven removed providers" (blog line 394 lists seven, line 50 says six).
  - lg_inventory.md (c) Responses guardrails row (line 55): `[Documented: repo ogx-ai/ogx main docs]` and the two `[Documented: repo blog]` -> `[Documented: repo ogx-ai/ogx@f8051dd6]`. Keep "output check about every 200 characters": blog states a 200-character batch size.
  - lg_inventory.md Reviewer notes item 2: rewrite as resolved (above).

### T29 - OGX LG4 limited to S1-S13: intentional?
- Verdict: **PARTLY RESOLVED** (provenance found; intent not stated)
- Evidence:
  - Commit ef26259209 "feat: add llama guard 4 model (#2579)", merged 2025-07-04, by mattf. Diff to llama_guard.py is 5 lines: LG4 ids added plus `# Llama Guard 4 uses the same categories as Llama Guard 3` / `# source: https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard4/12B/MODEL_CARD.md` and `"meta-llama/Llama-Guard-4-12B": DEFAULT_LG_V3_SAFETY_CATEGORIES`. The PR body says only "add support for Llama Guard 4 model to the llama_guard safety provider" plus test steps. No rationale for omitting S14.
  - LG4 card @172c1074 line 15: "We include an additional category, Code Interpreter Abuse, for text-only tool-call use cases." LG4 HF template default for text-only is S1-S14 (see T13). The cookbook 14-entry list includes S14.
  - Code at v0.4.4 lines 104-111 unchanged by later commits that touched the file (rename/refactor only).
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4] for the code; [Not disclosed] for intent.
- Draft impact:
  - lg_cols_a.md LG1 R4 line 50 and LG2 R4 line 170, B LG4 R4 line 151, B LG5 R4 line 230: append "(added in commit ef26259209, PR 2579, July 2025; the PR gives no reason)". Label unchanged `[Documented: repo ogx-ai/ogx@v0.4.4]`.
  - lg_cols_b.md LG4 R8 line 183 ("Whether the OGX omission of S14 for LG4 is deliberate") keep as open, add "(no rationale in the adding commit)".
  - lg_inventory.md Reviewer notes item 4: add the same sentence.

### T30 - OGX: last message only, or whole conversation
- Verdict: **CORRECTION** (A's "checks the last message only" is wrong as input handling; the whole conversation goes in the prompt, only the instruction targets the last message)
- Evidence, OGX v0.4.4 `src/llama_stack/providers/inline/safety/llama_guard/llama_guard.py`:
  - Line 352-354: `conversations_str = "\n\n".join([f"{m.role.capitalize()}: {interleaved_content_as_str(m.content)}" for m in messages])`.
  - Line 133: `Provide your safety assessment for ONLY THE LAST $agent_type message in the above conversation:` with line 356 `agent_type=messages[-1].role.capitalize()`.
  - Lines 285-291: `validate_messages` raises if the first message is not `user`, and `messages = messages[1:]` if the first two are both user. This is the only message dropped.
  - `run_moderation` (lines 207-213) does not call `validate_messages`: each input string becomes its own `OpenAIUserMessageParam`, all go into one prompt, and the instruction still says "ONLY THE LAST User message", so a list input is judged on its final string only.
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4]
- Draft impact:
  - lg_cols_a.md LG1 R3 line 32 -> two bullets:
    - "OGX v0.4.4 `run_shield` puts the whole conversation into the prompt, labels each turn with its capitalised role, and instructs the model to assess only the last message; if the first two messages are both from the user, the first is dropped **[Documented: repo ogx-ai/ogx@v0.4.4]**"
    - "OGX v0.4.4 `run_moderation` wraps each input string as a separate user message, puts them all in one prompt, and asks about only the last one **[Documented: repo ogx-ai/ogx@v0.4.4]**"
  - lg_cols_a.md LG2 R4 line 169: replace "checks the last message only" with "puts the whole conversation in the prompt and asks the model to assess only the last message".
  - lg_cols_a.md LG2 R3 line 157: keep, add "a list input is judged on its last string only".
  - lg_inventory.md (c) OGX provider row Input/Output cell: see T31 replacement (also fixes this). INV Reviewer note 3: mark resolved.
  - lg_cols_b.md Reviewer notes line 276: already correct; keep.

### T31 - OGX role label
- Verdict: **PARTLY RESOLVED** (A and B correct; the inventory cell is wrong)
- Evidence: llama_guard.py v0.4.4 line 353 `m.role.capitalize()` and line 356 `agent_type=messages[-1].role.capitalize()`. An OpenAI-style `assistant` message becomes "Assistant", `tool` becomes "Tool", `system` "System". "Agent" never appears except as the string in the template text of Meta's docs. Meta DOCS3: "{{ role }}: It can have the values: User or Agent."
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4]; Meta wording [Documented]
- Draft impact:
  - lg_cols_a.md LG1 R4 line 52 and B LG4 R3 line 137: no change (correct) except replace the label ref only if needed (already v0.4.4).
  - lg_inventory.md (c) OGX provider row "Input/Output" cell: replace "Role comes from the last message, which is wrapped as "User"/"Agent"; all messages go into the prompt, and only the first user message is dropped if two user messages lead [Documented: repo]" with "Every turn is written as its capitalised role ("User", "Assistant", "Tool"), not "Agent"; all turns go into the prompt and the instruction asks about the last one only; the first message is dropped if the first two are both user [Documented: repo ogx-ai/ogx@v0.4.4]". Remaining sentence about images stays with `[Documented: repo ogx-ai/ogx@v0.4.4]`.

### T32 - OGX moderation scores
- Verdict: **RESOLVED**
- Evidence (v0.4.4 lines 411-412, 444-446): `category_scores = dict.fromkeys(SAFETY_CATEGORIES_TO_CODE_MAP.keys(), 1.0)` for the safe object (with `flagged = False`); unsafe: `category_scores = {k: 1.0 if k in llama_guard_category else 0.0 ...}`. An unknown code returns the same safe object (lines 421-438, comment "just returning safe object, as we don't know what the invalid codes can map to").
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4]. "Likely a quirk" is [Inferred]; the repo does not say.
- Draft impact:
  - lg_cols_a.md LG1 R5 line 67: bare label. Split into two bullets: "NeMo returns an allowed/blocked outcome and a lowercased violation list **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**" and "OGX v0.4.4 moderation scores are only 0.0 and 1.0; a safe result sets every category to 1.0 with flagged false **[Documented: repo ogx-ai/ogx@v0.4.4]**".
  - lg_cols_a.md LG2 R5 line 188: split the same way ("NeMo returns an allowed flag and a violation list" -> NeMo label; "OGX returns a violation object or a moderation object" -> OGX v0.4.4 label).
  - lg_inventory.md (c) /v1/moderations row, Output cell: both bare labels -> `[Documented: repo ogx-ai/ogx@v0.4.4]`. B lines 64, 158 and RN 277: correct, no change.

### T33 - OGX moderation and response-role classification after Safety API removal
- Verdict: **RESOLVED**
- Evidence:
  - v0.4.4 `run_moderation` wraps every string as a user message (line 213), so it classifies the user role only; response classification there needs `run_shield`, whose role comes from the last message (T31).
  - On main (f8051dd6) neither path exists (T28). The Responses guardrail sends plain text with no role label: `resp = await client.post(moderation_endpoint, json={"input": messages}, headers=headers)` (`responses/utils.py` line 675). The blog says input check "flattens all input messages into a single text string" and each output check "sends the entire accumulated text so far".
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4] and [Documented: repo ogx-ai/ogx@f8051dd6]
- Draft impact:
  - lg_cols_a.md LG2 R3 line 157: keep and add a bullet "OGX 1.0 (pinned main) removed both paths; Responses guardrails send the flattened text to a configured external endpoint with no User or Agent role, so role-specific Llama Guard classification is not done by OGX **[Documented: repo ogx-ai/ogx@f8051dd6]**".
  - lg_cols_a.md LG2 R8 line 219: delete the bullet "How OGX moderation handles response-role classification after the Safety API removal"; LG2 R8 Summary has no mention, no change.

### T34 - Does the HF repo id of 3-11B-V reach OGX's vision branch
- Verdict: **RESOLVED**: no. Only the core-model id string reaches it.
- Evidence:
  - llama_guard.py v0.4.4 line 296: `if self.model == CoreModelId.llama_guard_3_11b_vision.value:`.
  - `src/llama_stack/models/llama/sku_types.py` line 82: `llama_guard_3_11b_vision = "Llama-Guard-3-11B-Vision"`. `sku_list.py` line 804: `huggingface_repo="meta-llama/Llama-Guard-3-11B-Vision"`. The two strings differ by the `meta-llama/` prefix.
  - `LLAMA_GUARD_MODEL_IDS` (lines 93-102) accepts both strings only for choosing the category list; the vision branch test uses the core id alone. With the HF repo id the text path is used, and `interleaved_content_as_str` renders any image as the literal `<image>` (prompt_adapter.py line 77).
- Label to use: [Documented: repo ogx-ai/ogx@v0.4.4]
- Draft impact:
  - lg_cols_b.md LG3 R4 line 51 ([Inferred] bullet) -> "The vision branch runs only if the registered model id is exactly `Llama-Guard-3-11B-Vision` (the core-model id); the Hugging Face repo id `meta-llama/Llama-Guard-3-11B-Vision` takes the text path, where an image becomes the literal text `<image>` **[Documented: repo ogx-ai/ogx@v0.4.4]**". Line 50 stays.
  - lg_cols_b.md LG3 R8 line 97 delete; **LG3 R8 Summary (line 91) must change.**
  - lg_cols_b.md LG3 R7 line 89 (OGX check): add "register the shield with the core id and with the HF id and compare **[Inferred]**".

### T35 - NeMo docs model type: `llama_guard` vs `llama_guard_2`
- Verdict: **CORRECTION** (both are true, on different pages; A conflates them)
- Evidence (NVIDIA-NeMo/Guardrails@v0.24.1 commit 5d81d670; develop 9f793de5 is identical for all files below, so no develop label is needed):
  - docs/configure-rails/guardrail-catalog/community/llama-guard.mdx (the page for the `llama guard check input` / `llama guard check output` flows): "Add a model of type `llama_guard` to the models section of the `config.yml` file." with `- type: llama_guard`, `model: meta-llama/LlamaGuard-7b`. Prompts use `<s>[INST] Task: ...` and `O1:`/`O2:` categories.
  - docs/configure-rails/guardrail-catalog/content-safety.mdx (a different feature, flows `content safety check input $model=...`): `- type: llama_guard_2`, `model: meta-llama/Meta-Llama-Guard-2-8B`, and "The `type` is a unique identifier for the model that will be passed to the input and output rails as a parameter." Same file mentions "Meta's Llama Guard 3" as a supported model. examples/configs/content_safety*/prompts.yml line 165: `content_safety_check_output $model=llama_guard_2`.
  - nemoguardrails/library/llama_guard/flows.co: `LlamaGuardCheckInputAction(model_name="llama_guard")` and `LlamaGuardCheckOutputAction(model_name="llama_guard")`; `# Policy violations are currently unused, but can be used to better phrase the bot output`.
  - So `llama_guard` is the type that the llama-guard flows require (hard-coded), and `llama_guard_2` is a user-chosen type name in the separate content-safety flows.
- Label to use: [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]
- Draft impact:
  - lg_cols_a.md LG1 R4 line 54 -> "NeMo Guardrails v0.24.1: the `llama guard check input` flow calls an action with model name `llama_guard` hard-coded; the Llama-Guard docs page configures a model of type `llama_guard` (LlamaGuard-7b) **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**". Add bullet: "The type `llama_guard_2` with Meta-Llama-Guard-2-8B appears only in the separate content-safety docs page, whose flows take the model type as a `$model` parameter **[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]**".
  - lg_cols_a.md LG2 R4 line 171: same replacement for the clause "docs example uses type `llama_guard_2`".
  - lg_cols_a.md Reviewer notes line 251 -> "Two NeMo docs pages differ: llama-guard.mdx uses type llama_guard with LlamaGuard-7b; content-safety.mdx uses type llama_guard_2 with Meta-Llama-Guard-2-8B. The llama guard flows hard-code llama_guard." Also fix the R9 line 127 URL: pin to the repo file https://github.com/NVIDIA-NeMo/Guardrails/blob/v0.24.1/docs/configure-rails/guardrail-catalog/content-safety.mdx and add .../community/llama-guard.mdx (the docs.nvidia.com page was not fetched).
  - lg_inventory.md (c) NeMo row: "Versions supported" bare `[Documented: repo docs]` -> `[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]` (docs mdx); Caveats cell: replace "the brief says the docs example uses `llama_guard_2`, but the v0.24.1 docs page shows `llama_guard`" with "the llama-guard docs page uses type llama_guard; llama_guard_2 appears only on the content-safety docs page". Reviewer notes item 8 likewise. The "live-site snippet" remark can go: it matches the content-safety page.

### T37 - ExecuTorch instructions (bare string, download link)
- Verdict: **PARTLY RESOLVED** (facts confirmed; "looks incomplete" stays a judgement)
- Evidence (PurpleLlama @172c1074 Llama-Guard3/1B/ET_INSTRUCTIONS.md):
  - Lines 38-39: `prompt = "tell me a joke"` then `token_ids = tokenizer.apply_chat_template(prompt, return_tensors="pt")`. The 1B chat template (T13 source) iterates `message['content']` of a message list, so a bare string is not the message-list shape that template and the cookbook notebook use. [Inferred]
  - Line 6: "Download the .pte model and model params (see the [Llama CLI Reference](https://github.com/meta-llama/llama-stack/blob/main/docs/cli_reference.md#step-1-get-the-models) ...)". That URL returns 301 to ogx-ai/ogx and then HTTP 404 (docs/cli_reference.md does not exist at v0.4.4 or main).
  - Line 14 uses `--prompt "$(cat <path_to_local_hf_repo>/example-prompt.txt)"`; the HF repo Llama-Guard-3-1B-INT4 does list `example-prompt.txt`, `llama_guard_3_1b_pruned_xnnpack.pte`, `params.json`, `tokenizer.model` (HF metadata API, revision d6c11bd8f851ceebb762bd2adbfc45e6d40c0991) and has no chat template.
- Label to use: [Documented: repo PurpleLlama@172c1074] for the quoted lines; [Inferred] for "incomplete".
- Draft impact:
  - lg_inventory.md (c) ExecuTorch row Caveats: replace with "The doc's tokenizer step passes the bare string "tell me a joke" to `apply_chat_template` [Documented: repo PurpleLlama@172c1074]; the 1B template expects a message list [Inferred]. The model-download link points to the old llama-stack CLI reference, which now redirects to ogx-ai/ogx and returns 404 [Documented: repo PurpleLlama@172c1074]. No official latency figures; the paper abstract gives at least 30 tokens/s on mobile". The remaining bare `[Documented: PL]` and `[Documented: PL; judgement Inferred]` follow the Label hygiene table (split as in triage).

### T38 - Llama API `/moderations`
- Verdict: **PARTLY RESOLVED** (schema now read from a Wayback copy of the official Meta page; the live Meta pages are gone)
- Live URLs checked 2026-10-08 (all HTTP 404, after redirect to dev.meta.ai): https://llama.developer.meta.com/docs/api/moderations (and with trailing slash) -> https://dev.meta.ai/docs/api/moderations; https://llama.developer.meta.com/docs/features/moderation -> https://dev.meta.ai/docs/features/moderation; https://llama.developer.meta.com/docs/guides/moderation-guide -> https://dev.meta.ai/docs/guides/moderation-guide; https://dev.meta.ai/docs/api/moderation, /docs/moderations, /docs/features/llama-moderations, /docs/features/guardrails (404). The current dev.meta.ai sitemap lists API reference pages for chat-completions, files, images, messages, models, responses, voice and status; none for moderations. https://dev.meta.ai/help/about-model-api/llama-and-model-api says: "Llama models aren't run for you through Model API."
- Evidence, Wayback snapshots of official Meta pages (content decoded from the embedded page data; if the caller treats archive copies as non-official, keep the label [To be verified]):
  - http://web.archive.org/web/20250914152244/https://llama.developer.meta.com/docs/api/moderations : "POST /v1/moderations", Base URL `https://api.llama.com/v1`; request: `messages` required, "array (one of UserMessage, SystemMessage, ToolResponseMessage, AssistantMessage)"; `model` optional: "Optional identifier of the model to use. Defaults to "Llama-Guard"."; tool message role "Must be "tool" to identify this as a tool response", plus `tool_call_id`. Response HTTP 200: `model` (string), `results` (array of objects with `flagged` boolean and `flagged_categories` array of strings). Example response: `{"model": "Llama-Guard", "results": [{"flagged": true, "flagged_categories": ["privacy"]}]}`.
  - http://web.archive.org/web/20250914135559/https://llama.developer.meta.com/docs/features/moderation : "Safety models on the moderations endpoint support only an 8K context window." and "Send a text prompt or response, or a multimodal (text and image) input" (categories of "MLCommons Taxonomy of Hazards").
  - The default model name is "Llama-Guard", not stated to be LG4. PROT (live, raw) still says: "For the first time, Llama Guard 4 is now available through the /moderations endpoint in Llama API." PROT also says LG4 "supports 12 languages".
- Label to use: [Documented] for the schema (Meta page, archive snapshot 2025-09-14); availability today is [To be verified] (live pages 404 and the Meta help page says Llama models are not run through Model API).
- Draft impact:
  - lg_inventory.md (c) Llama API row, "Input/Output" cell: replace the `[To be verified: search-result snippet only...]` text with "POST https://api.llama.com/v1/moderations; `messages` array of user, system, tool-response and assistant messages (text; images for multimodal), optional `model` defaulting to "Llama-Guard" [Documented] (Wayback copy of the Meta page, 2025-09-14)". "Categories configurable": "No parameter for custom categories in the documented schema [Documented]". "Output / score": "`model`, `results[]` with `flagged` (bool) and `flagged_categories` (list of strings); no scores [Documented] (same snapshot)". Status: change "current" to "documented in 2025; current availability [To be verified]". Caveats: replace "The API doc page itself could not be fetched..." with "Live Meta doc URLs return 404 (list above); the schema comes from an archived copy; Meta's Model API help page says Llama models are not run through Model API. Context window 8K [Documented] (archived features page)". Source cell: add the two Wayback URLs.
  - lg_cols_a.md LG1 R4 line 56: "Llama API exposes LG4 through the `/moderations` endpoint **[Documented]** (Meta protections page)" -> append "; the Meta API doc pages for it now return 404 and the schema survives only in archived copies **[To be verified]**" as its own bullet.
  - lg_inventory.md Reviewer notes "Summarised-fetch caveats" and Not-found list: remove the two `[Not found]` items for the Llama API row.

### T51 - llama-models repo has no Llama Guard prompt template
- Verdict: **CORRECTION** (the claim is true by direct check, but "Meta's docs say" is wrong attribution: the Meta docs point to llama-cookbook)
- Evidence:
  - llama-models main @0e0b8c51 (tarball): search for "BEGIN UNSAFE CONTENT CATEGORIES" returns nothing; no file name contains "guard"; Llama Guard appears only as model entries in `models/sku_list.py` (e.g. line 796-798 `CoreModelId.llama_guard_4_12B`, `huggingface_repo="meta-llama/Llama-Guard-4-12B"`) and in `models/sku_types.py`; the CLI safety module covers Prompt Guard only.
  - DOCS3 and DOCS4: "The llama-cookbook repository has a helper function and an inference example that shows how to properly format the prompt with the provided categories."
- Label to use: [Documented: repo meta-llama/llama-models@0e0b8c51] for the absence (searched at that commit); [Documented] for the docs sentence.
- Draft impact:
  - lg_cols_a.md LG1 R4 line 48 -> "The llama-models repo (main, pinned) has Llama Guard only as model-id entries and no prompt template **[Documented: repo meta-llama/llama-models@0e0b8c51]**" and "Meta's Llama Guard 3 and 4 docs pages point to the llama-cookbook helper and inference example for the prompt format **[Documented]**". Remove "(absence not checked directly)".

### T54 - Cookbook LG3 list always has 14 categories
- Verdict: **RESOLVED**
- Evidence: prompt_format_utils.py @2f22a9eb: `LLAMA_GUARD_3_CATEGORY` holds 14 `SafetyCategory` entries, ending with 'Code Interpreter Abuse. '; the only LG3 list. `build_default_prompt(..., llama_guard_version=LLAMA_GUARD_3)` always uses it; there is no 13-entry or per-model variant. The cookbook is unchanged since: main head = 2f22a9eb on 2026-10-08. Cards for 1B and 11B-V list S1-S13 (PurpleLlama @172c1074).
- Label to use: [Documented: repo meta-llama/llama-cookbook@2f22a9eb]
- Draft impact:
  - lg_inventory.md (b) "Code interpreter abuse" row (cookbook mention) and (c) cookbook row Caveats: keep the sentence and add the evidence label; replace the bare labels as per mapping table. Reviewer note 9: change "Cookbook LG3 list" to "verified at 2f22a9eb, same on main on 2026-10-08".
  - lg_cols_b.md LG4 R4 line 150 already accurate.

### T55 - Naming drift of categories and prompt wording
- Verdict: **RESOLVED** (the split is systematic)
- Evidence:
  - PurpleLlama cards @172c1074 (8B, 1B, 11B-vision, LG4): "S3: Sex-Related Crimes", "S4: Child Sexual Exploitation", "S11: Suicide & Self-Harm" (HTML-escaped as `&amp;` in 8B, 1B, 11B).
  - Prompt text (HF chat templates of all five models, DOCS3 and DOCS4 prompt blocks, cookbook `LLAMA_GUARD_3_CATEGORY`, OGX constants): "S3: Sex Crimes.", "S4: Child Exploitation.", "S11: Self-Harm."
  - Instruction wording: "according our safety policy" in the 3-8B, INT8, 3-1B and 3-11B-V templates, the cookbook (line 32), OGX (line 114) and the DOCS3/DOCS4 worked examples; "according to our safety policy" in the LG4 HF template and the DOCS3/DOCS4 template placeholder text.
  - The 3-8B and 8B-INT8 templates end the instruction with `categories.<|eot_id|>` (no space); the 1B/11B-V and LG4 templates have a space before the end-of-turn token.
- Label to use: [Documented] for template/docs wording; [Documented: repo PurpleLlama@172c1074] for card names; [Documented: repo meta-llama/llama-cookbook@2f22a9eb] for cookbook; [Documented: repo ogx-ai/ogx@v0.4.4] for OGX.
- Draft impact:
  - lg_inventory.md (b) rows 3, 4, 10 notes: say "Card hazard names are long forms; the strings inside the actual prompt (HF templates, Meta docs, cookbook, OGX) are the short forms." RN 10 likewise. Recommend canonical rule for the workbook: hazard prose uses card names; any prompt text quoted or built for tests uses the template strings. Add to lg_cols_b.md Reviewer notes line 279 (wording item): the "according our" / "according to our" split is by model template as listed above, so a test prompt must be generated from the target model's own template.

---

## Summary lines that must change (new text)

Word limits: Summary 45, R7 60. No code identifiers, underscores, backticks or dollar signs.

| Location | New Summary |
|---|---|
| lg_cols_b.md LG4 R1 (line 112) | **Code interpreter abuse category.** Llama Guard 3-8B and Llama Guard 4 add S14, which flags content that seeks to abuse code interpreters. The 3-8B model was also evaluated on search tool calls. **[Documented]** |
| lg_cols_b.md LG4 R6 (line 160) | **Conversation turns, with code in the agent turn.** Prompt checks use the user turn only; response checks need both turns. Meta does not disclose a tool-call or tool-output format, so code would go in as plain text. **[Inferred]** |
| lg_cols_b.md LG5 R1 (line 197) | **Prompt-level policy customisation.** Meta says the default categories can be customised for zero-shot or few-shot prompting. The chat templates of 3-1B, 3-11B-Vision and Llama Guard 4 read optional custom and excluded category lists; the 3-8B template has a fixed list. **[Documented]** |
| lg_cols_b.md LG5 R4 (line 214) | **Chat-template arguments, cookbook builder, paper results.** The 3-1B, 3-11B-Vision and Llama Guard 4 templates take custom categories and excluded keys; the 3-8B template does not. The cookbook builder covers up to Llama Guard 3. The LG1 paper reports zero-shot AUPRC 0.847. **[Documented]** |
| lg_cols_b.md LG5 R7 (line 243) | **Minimum setup:** Llama Guard 3-1B and 3-11B-Vision (documented path) plus Llama Guard 4 (template supports custom lists, untested), with a 3-category custom taxonomy, about 12 labelled items each, and exclusion tests. **[Inferred]** |
| lg_cols_b.md LG5 R8 (line 252) | **Key open questions.** Whether custom and excluded categories change verdicts as intended on the 3-1B, 3-11B-Vision and Llama Guard 4 templates, whether Meta documents any Llama Guard 4 custom-policy usage, and zero-shot quality for current models. |
| lg_cols_b.md LG3 R8 (line 91) | **Key open questions.** LG4 tile size and its token layout, an official F1 or threshold for 3-11B-Vision at its default score, and behaviour beyond about three images. |

Notes on these: line numbers are the current line of each Summary (+/-1 where my grep was approximate; match on the old text). The LG3 R8 clause on LG4 tiles may also change under another agent's T9 resolution. Word counts: 32, 37, 40, 41, 31, 36, 27. Summaries elsewhere (A LG1 R4 Summary "with INT8, INT4 and Llama API options", A R8 Summaries) are unchanged; the Llama API option stays Documented but see T38 caveat in Detail.

## Bare "[Documented: repo]" labels: exact replacements

Rule: replace with `[Documented: repo <repo>@<ref>]`. Org prefix optional but be consistent; the A file uses `llama-cookbook@2f22a9eb` and `PurpleLlama@172c1074`, B and the inventory use `meta-llama/llama-cookbook@2f22a9eb`. For pinned main use `ogx-ai/ogx@f8051dd6`.

### lg_cols_a.md (2 bare, plus 2 ref-less)

| Line | Bullet | Replace with |
|---|---|---|
| 67 (LG1 R5) | "NeMo exposes an allowed flag ...; OGX moderation returns ... scored 1.0 when safe" | Split: NeMo part `[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]`; OGX part `[Documented: repo ogx-ai/ogx@v0.4.4]` (T32) |
| 188 (LG2 R5) | "NeMo returns an allowed flag and a violation list; OGX returns a violation object or a moderation object" | Split the same way |
| 53 (LG1 R4, `[Documented: repo ogx-ai/ogx]` no ref) | OGX 1.0 removal bullet | `[Documented: repo ogx-ai/ogx@f8051dd6]` (T28) |
| 170 (LG2 R4, `[Documented: repo ogx-ai/ogx]` no ref) | v0.4.4 facts plus OGX 1.0 clause | Split: v0.4.4 facts `@v0.4.4`; the 1.0 clause `@f8051dd6` |

### lg_inventory.md (17 bare or partial; row by row)

| Row (c unless noted) | Cell and fact | Replace with |
|---|---|---|
| cookbook `prompt_format_utils` | Input/Output: "AgentType.USER or AGENT fills the role slot" | `[Documented: repo meta-llama/llama-cookbook@2f22a9eb]` |
| same | Categories configurable: "any list of SafetyCategory ... with_policy=True" | same |
| same | Output / score: "Prompt string only. No inference, no score" (the third bare label on that line) | same |
| cookbook notebooks | "[Documented: repo directory listing at 2f22a9eb]" | `[Documented: repo meta-llama/llama-cookbook@2f22a9eb]` |
| same | Versions: "Notebook text covers 3-1B and 3-11B-V only" | same |
| same | Categories configurable: "custom dict, removing keys, in text and vision" | same |
| same | Output: "max_new_tokens=20, output_scores=True" | same |
| same | Caveats: Colab badge path vs getting-started | same |
| OGX provider (v0.4.4) | Versions: ids, "No LG1, LG2, INT8 or INT4 ids" | `[Documented: repo ogx-ai/ogx@v0.4.4]` |
| same | Input/Output: wrapping and first-message rule; image path | `[Documented: repo ogx-ai/ogx@v0.4.4]` (two labels; text fix in T31) |
| same | Categories configurable: `excluded_categories`, no custom text | same |
| same | Output: violation level ERROR, canned message, temperature 0.0 | same |
| same | Status: "[Documented: repo ogx-ai/ogx main, listing]" | `[Documented: repo ogx-ai/ogx@f8051dd6]` |
| OGX /v1/moderations | Input/Output: user message per string, TODO for images | `[Documented: repo ogx-ai/ogx@v0.4.4]` |
| same | Categories configurable: `excluded_categories` only | same |
| same | Output / score: scores 0.0/1.0, safe = all 1.0, unknown code fails open | same |
| NeMo | Versions: "[Documented: repo docs]" (LlamaGuard-7b, `<s>[INST]`) | `[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]` |
| same | Input/Output: input sends user message; output sends both | same |
| same | Categories configurable: "[Documented: repo docs]" (edit prompts.yml) | same |
| same | Output / score: safe allows, unsafe blocks, anything else blocks | same |
| same | Caveats: "[Documented: repo flows.co]" | same |
| same | Caveats: "[Documented: repo; effect Inferred]" | Split: `[Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1]` for the split-on-space code; `[Inferred]` for the effect |
| Responses guardrails | "[Documented: repo ogx-ai/ogx main docs]", two "[Documented: repo blog]" | `[Documented: repo ogx-ai/ogx@f8051dd6]` |

Note: the inventory has 17 occurrences of the exact bare text `[Documented: repo]` plus the partial forms `[Documented: repo docs]` (2), `[Documented: repo blog]` (2), `[Documented: repo flows.co]`, `[Documented: repo; effect Inferred]`, `[Documented: repo ogx-ai/ogx main docs]`, `[Documented: repo ogx-ai/ogx main, listing]` and `[Documented: repo directory listing at 2f22a9eb]`; the table above lists each by row. After editing, `grep -c` for `[Documented: repo]`, `[Documented: repo docs]`, `[Documented: repo blog]` should return zero in lg_inventory.md and lg_cols_a.md.

---

## Summary table

| Item | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T13 | CORRECTION | [Documented] (template); [Not disclosed] (no card snippet) | Y (B LG5 R1, R7, R8) |
| T14 | RESOLVED | [Documented] (template); [Inferred] (ignored kwargs) | Y (B LG5 R4) |
| T18 | RESOLVED | [Documented: repo meta-llama/llama-cookbook@2f22a9eb] | N |
| T19 | RESOLVED | [Documented: repo meta-llama/llama-cookbook@2f22a9eb] | N |
| T23 | STILL OPEN (confirmed from raw sources) | [Not disclosed] | Y (B LG4 R1, R6) |
| T28 | CORRECTION | [Documented: repo ogx-ai/ogx@f8051dd6] | N |
| T29 | PARTLY RESOLVED | [Documented: repo ogx-ai/ogx@v0.4.4]; intent [Not disclosed] | N |
| T30 | CORRECTION | [Documented: repo ogx-ai/ogx@v0.4.4] | N |
| T31 | PARTLY RESOLVED (A/B right, inventory wrong) | [Documented: repo ogx-ai/ogx@v0.4.4] | N |
| T32 | RESOLVED | [Documented: repo ogx-ai/ogx@v0.4.4] | N |
| T33 | RESOLVED | [Documented: repo ogx-ai/ogx@v0.4.4] / @f8051dd6 | N |
| T34 | RESOLVED | [Documented: repo ogx-ai/ogx@v0.4.4] | Y (B LG3 R8) |
| T35 | CORRECTION | [Documented: repo NVIDIA-NeMo/Guardrails@v0.24.1] | N |
| T37 | PARTLY RESOLVED | [Documented: repo PurpleLlama@172c1074]; "incomplete" [Inferred] | N |
| T38 | PARTLY RESOLVED | [Documented] (archived Meta page); availability [To be verified] | N |
| T51 | CORRECTION (attribution) | [Documented: repo meta-llama/llama-models@0e0b8c51] | N |
| T54 | RESOLVED | [Documented: repo meta-llama/llama-cookbook@2f22a9eb] | N |
| T55 | RESOLVED | [Documented] / repo labels per source | N |

## Reviewer notes

- All repo facts were read from tarballs at the pinned commits, not from summaries. The OGX main pin f8051dd6 is the head seen on 2026-10-08; every `@f8051dd6` label should keep the full SHA in R9 URLs.
- HF chat templates came from the HF metadata API, not from raw repo files (401). Treat as the repo's tokenizer_config content as served by Hugging Face. HF README text for LG4 and 3-8B was not readable, so statements about what a card shows rest on the PurpleLlama mirror.
- Offline jinja2 renders (3.1.6, sandboxed, trim_blocks/lstrip_blocks as HF uses) are my own experiments, labelled [Inferred]. They are not Meta statements and not a run of HF's own renderer.
- Archived Llama API pages (Wayback) are copies of Meta pages, not live pages. Decide whether the sheet accepts them as official; if not, keep T38 schema as [To be verified].
- Release notes versus blog on OGX: apparent conflict dissolves once "OpenAI-compatible /v1/moderations endpoint" is read as the external service OGX calls (confirmed by commit title and code). The release notes text itself is still ambiguous and was last touched 2026-10-01 for a link fix only.
- Bonus findings outside my items: the 3-8B-INT8 template lists S14 (helps T26); the Llama API features page says the moderations endpoint has an 8K context window (helps T5); DOCS4 states the 336x336 tile plus global tile text (helps T9, other agent).
- Not checked: the cookbook main branch beyond head = 2f22a9eb; the live docs.nvidia.com NeMo pages (repo docs used instead); OGX tags after v0.4.4 other than main.
