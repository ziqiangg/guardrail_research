# SDP resolutions 1 (P5, items T1 to T49, classes a and c, plus class D items settled by rulings)

Date: 2026-10-09 (all pages read on this date). Resolver: gr-resolver. Triage: `benchtest/drafts/sdp_triage.md`.

Items handled (26): T1, T2, T3, T4, T5, T6, T7, T8, T9, T11, T12, T14, T16, T17, T18, T19, T20, T21, T22, T23, T24, T42, T44, T46, T47, T49.
Class c items: none fall in T1 to T49 (T92 to T95 belong to resolutions_2).
Class b items in this range left open as the triage says (no doc re-read can settle them): T10, T13, T15, T25 to T41, T43, T45, T48. Only T36 to T41 were not touched at all; none of these changes any text below.

Short names: DOCS = `https://docs.cloud.google.com/sensitive-data-protection/docs`; LIM = `https://docs.cloud.google.com/sensitive-data-protection/limits`; PRC = `https://cloud.google.com/sensitive-data-protection/pricing`; SLA = `https://cloud.google.com/sensitive-data-protection/sla`; REST = `DOCS/reference/rest/v2`; DISC = `https://dlp.googleapis.com/$discovery/rest?version=v2` (revision 20261006).

## Method and access notes

- Every number or quote below comes from raw text fetched with `python benchtest/tools/fetch_text.py` (no summarising fetch), saved under `benchtest/scratchpad/resolver/` and `benchtest/scratchpad/resolver/r1/`. The page footers carry "Last updated" dates (2026-10-02 to 2026-10-07 for the pages used); docs pages are not pinned, so they stay plain `[Documented]` with the read date.
- The DLP API discovery document was read as raw JSON (HTTP 200, 737,711 bytes, `"revision": "20261006"`), per the main ruling that it is an official Google source.
- Code was read from the vendor repo at the pinned tag through `https://raw.githubusercontent.com/googleapis/google-cloud-python/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/...` (HTTP 200 through fetch_text.py). Canonical repo: `googleapis/google-cloud-python`; tag `google-cloud-dlp-v3.40.0` is still the latest `google-cloud-dlp-v*` tag (`git ls-remote --tags`, v3.37.0 to v3.40.0 listed). A `git clone` was denied by the permission system and was not retried; raw file reads replaced it. Note for main: raw.githubusercontent.com is reachable although github.com pages are not (R013/R015 only mention clones).
- Not read: Cloud Audit Logs and KMS pages (not in my range), the Gemini Enterprise console steps (T10 is class b).
- Line numbers cited as `file@tag:N` count from line 1 of the repo file.

---

### T1 — Header prefix (CP1)
- Verdict: RESOLVED
- Evidence: Ruling R018 item 1: "Prefix `Sensitive Data Protection:`; "formerly Cloud DLP" and the API name `DLP API` noted in cells." (decided_by user, 2026-10-09). The docs say the same: "Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same" (DOCS release notes, read 2026-10-09).
- Label to use: not applicable (decision); the name note in cells is `[Documented]`.
- Draft impact: none. The six `## Column` lines and the Covered-by strings already use `Sensitive Data Protection:`. Style item (triage "Style issues" 2): the SD1 R4 Summary sentence "The service was formerly called Cloud DLP." conflicts with R018 only in that the brief puts "formerly Cloud DLP" in Detail; SD1 R1 and R4 Detail already carry it. Remove that sentence from the SD1 R4 Summary if it keeps the Summary at or under 45 words (merger to check).

### T2 — Content policy as a column or inventory only
- Verdict: RESOLVED (inventory only; the R018 upgrade condition was checked and is not met, see T9)
- Evidence: Ruling R018 item 3: "Content policies (SD7) are inventory only; upgrade to a column only if a documented direct apply/evaluate method is found". T9 below found no such method.
- Label to use: not applicable.
- Draft impact: none. The content policies row in INV(a) keeps `— (inventory only, not in Table 3)`. Text changes for the row are in T9.

### T3 — Fold SD2 into SD1 and SD4 into SD3
- Verdict: RESOLVED
- Evidence: Ruling R018 item 2: "Six columns SD1–SD6 as drafted (no fold of SD2→SD1 or SD4→SD3; SD5 not split)."
- Label to use: not applicable.
- Draft impact: none. T65 (hash row Covered-by, resolutions_2) can now be decided with SD4 kept as its own column.

### T4 — Split SD5; keep SD6 separate
- Verdict: RESOLVED
- Evidence: Ruling R018 item 2 (as T3): SD5 not split; SD6 stays a column of its own.
- Label to use: not applicable.
- Draft impact: none.

### T5 — Covered-by marker for integration-path rows
- Verdict: RESOLVED by precedent (R011 and R012); not covered by R018 itself, so main should record it
- Evidence: R011: marker `— (inventory only, not in Table 3)` is for rows that are "current and available but deliberately not Table 3 columns". R012: "SDP columns describe the SDP API itself and list Model Armor as an integration path in the SDP inventory", and the Model Armor columns stay under Model Armor.
- Label to use: not applicable.
- Draft impact: none. INV(d) Model Armor basic and advanced rows, Gemini Enterprise, Data Fusion and BigQuery rows keep the R011 marker. The Model Armor columns are named in the row text, not in Covered-by.

### T6 — Provisional cross-product headers in Detail bullets
- Verdict: RESOLVED
- Evidence: Compared by grep on 2026-10-09 with the sibling drafts. `modelarmor_brief.md`: "`MA5` `Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)`", "`MA6` `Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)`", "`MA10` `Model Armor: Image screening with OCR and visual scanning`". `presidio_brief.md`: "`PD1` `Presidio: PII detection in text (Analyzer)`", "`PD2` `Presidio: PII anonymisation and masking in text (Anonymizer)`". `sentinel_two_level.md` line 650: "## Column SN6: GovTech Sentinel: PII detection and masking (AWS Bedrock)". Rulings R016 item 1 ("Header prefix `Presidio:` is frozen"), R016 item 2 (PD1 to PD6 as drafted), R017 item 1 (MA1 to MA10 as drafted) and item 4 (prefix `Model Armor:`).
- Label to use: the cross-reference bullets stay `[Inferred]` (they are pointers, not source facts).
- Draft impact: all five headers match exactly and are now frozen by R016 and R017.
  - `sdp_cols_a.md` SD1 R4 (line 97): replace with `• For how Model Armor calls SDP, see the Model Armor columns "Model Armor: Input-level sensitive data detection and de-identification (Sensitive Data Protection)" and "Model Armor: Output-level sensitive data detection and de-identification (Sensitive Data Protection)"; ruling R012 keeps those internals out of this column **[Inferred]**` (drop "provisional headers"; written out in full, which also fills the unwritten Output-level header).
  - SD3 R4 (line 459): same replacement, ending "; ruling R012".
  - SD1 R4 (line 98) and SD3 R4 (line 460): delete "(provisional header)".
  - `sdp_cols_b.md` SD5 R4 (line 270): the header is correct; no change.

### T7 — Google-owned pages outside the brief's source list (Apigee, Data Fusion, BigQuery tutorial, demo page)
- Verdict: RESOLVED by precedent (R007 item 1 and CLAUDE.md rule 1); main should record it as a ruling
- Evidence: R007 item 1: "Official sources are the vendor's docs…". The pages are Google Cloud documentation (docs.apigee.com and docs.cloud.google.com for Data Fusion and the BigQuery tutorial; cloud.google.com/dlp/demo is a Google page). The cells already flag them "not SDP docs".
- Label to use: facts from these pages stay `[Documented]` with the plain-text hint "(Google Cloud docs, not SDP docs)".
- Draft impact: none beyond T79 and T94 (resolutions_2).

### T8 — Google Cloud blog and Context7 not used
- Verdict: STILL OPEN (decision for main or user; not covered by R018 or R019). Default stands: not used.
- Evidence: no draft depends on a blog source (triage T8). Nothing researched.
- Label to use: not applicable.
- Draft impact: none.

### T9 — Is there a documented direct apply or evaluate method for content policies? (PRIORITY)
- Verdict: STILL OPEN (checked the DLP API discovery document, the RPC reference, the REST root and resource pages, the IAM roles and permissions page, the content-policy and manage pages, the release notes, the Gemini Enterprise page and API reference, and the Python client at v3.40.0: no apply or evaluate method is documented). **R018's upgrade condition is not met, so the column question is not reopened for the user.** The permission and the role exist, but no public method uses them.
- Evidence (all verbatim):
  - Discovery document, `https://dlp.googleapis.com/$discovery/rest?version=v2`, revision 20261006: the resource `projects.locations.contentPolicies` has exactly five methods, ids `dlp.projects.locations.contentPolicies.delete`, `.create`, `.get`, `.patch`, `.list`. No method id in the whole document contains "appl", "check", "verdict" or "polic" other than the five above (regex search of every `dlp.` method id), and the schema has no Apply or Evaluate request type. The only appearances of the word "verdict" are the `defaultAction` description "Defaults to returning an ALLOW verdict if not set." and the `returnVerdict` field. The `ContentPolicy.errors` description reads "A stream of errors encountered when the policy was applied."
  - RPC reference, `DOCS/reference/rpc/google.privacy.dlp.v2` (footer: Last updated 2026-10-02): the DlpService RPC list has 60 `rpc` entries; the content policy ones are `CreateContentPolicy`, `DeleteContentPolicy`, `GetContentPolicy`, `ListContentPolicies`, `UpdateContentPolicy`. There is no `ApplyContentPolicy` or similar.
  - REST resource page, `REST/projects.locations.contentPolicies` (Methods table): "create | Create a ContentPolicy. delete | Delete a ContentPolicy. get | Get a ContentPolicy. list | Lists ContentPolicies in a parent." plus patch. The REST root page lists the same five under `projects.locations.contentPolicies`.
  - IAM, `DOCS/access-control/roles-permissions`: "DLP Content Policies Consumer (roles/dlp.contentPoliciesConsumer) Apply content policies. | dlp.contentPolicies.apply | dlp.contentPolicies.get". `DLP User (roles/dlp.user)`: "Inspect, Redact, and De-identify Content | dlp.contentPolicies.apply | dlp.kms.encrypt | dlp.locations.* …". The permission list also holds `dlp.contentPolicies.create/delete/get/list/update`. The page maps no permission to a method.
  - `DOCS/manage-content-policies`: "If you plan to apply content policies to your Gemini Enterprise connectors and apps or Gemini Notebook Enterprise notebooks, then you must also grant the DLP User (roles/dlp.user) role to your Gemini Enterprise service account." (the only stated consumer of `apply`).
  - `DOCS/content-policy`: "a content policy doesn't return a list of findings. Instead, a content policy returns a single ALLOW or BLOCK verdict. The client application can then act on the verdict" and "Get immediate, synchronous verdicts on content to enforce organizational data policies." Neither names a call.
  - Gemini Enterprise API, `https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/DataProtectionPolicy`: `SensitiveDataProtectionPolicy.policy` is "Optional. Specifies the resource name of the Sensitive data Protection content policy." Applying a policy is done by attaching its name to a connector, not by submitting content.
  - Release note 2026-08-31: "Sensitive Data Protection content policies are in General Availability. You can use content policies to evaluate content and return an ALLOW or BLOCK verdict based on data sensitivity." No method named.
  - Python client, `https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py`: `def create_content_policy(` (line 7363), `def update_content_policy(` (7488), `def get_content_policy(` (7620), `def list_content_policies(` (7727), `def delete_content_policy(` (7850). A search of the file for "apply_" and "evaluate" found nothing. `CHANGELOG.md` at the tag has no content-policy apply entry.
- Label to use: the methods list is `[Documented]` (docs) and `[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]` (client). The absence of an apply or evaluate method is `[Not disclosed]` naming what was checked. The statement that the permission is exercised by the Gemini Enterprise service account is `[Inferred]` (premise: the manage page tells the administrator to grant `roles/dlp.user` to that account in order to apply policies).
- Draft impact:
  - `sdp_inventory.md` INV(a) "Content policies" row, "Method or resource" cell (replace the whole cell text): `projects.locations.contentPolicies with create, delete, get, list and patch [Documented] (REST contentPolicies, REST root, API discovery document revision 20261006). The DlpService RPC reference lists CreateContentPolicy, DeleteContentPolicy, GetContentPolicy, ListContentPolicies and UpdateContentPolicy [Documented] (RPC reference). The Python client has create_content_policy, update_content_policy, get_content_policy, list_content_policies and delete_content_policy [Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0] (client.py). A method that submits content to a policy for a verdict [Not disclosed] (checked the discovery document, RPC reference, REST root and resource pages, the content-policy and manage pages, release notes and client.py at the tag)`
  - Same row, "What it does" or notes cell (the sentence beginning "The call that submits content for a verdict is not exposed"): replace with `IAM has a permission dlp.contentPolicies.apply, inside roles/dlp.user and the role DLP Content Policies Consumer (Apply content policies) [Documented] (DOCS access-control/roles-permissions). The Gemini Enterprise service account is told to hold roles/dlp.user to apply policies [Documented] (DOCS manage-content-policies). The apply permission is what that service account uses, with no public method for other callers [Inferred] (premise: the manage page names this as the only consumer and no method is listed)`. Remove the old "an apply operation exists somewhere in the service [Inferred]" fact.
  - INV(a) intro paragraph (line 6): replace "its evaluation call is not exposed in the REST resource or the Python client" with "no call that submits content to a policy is documented in the REST resource, the RPC reference or the Python client".
  - INV(d) Gemini Enterprise row, Notes: add `Gemini Enterprise attaches a policy through its own API field sensitiveDataProtectionPolicy.policy, the content policy resource name [Documented] (Gemini Enterprise docs, not SDP docs; REST DataProtectionPolicy)`.
  - `sdp_cols_a.md` SD1 R4 line 94 (source 2b): keep, correct the cite to `client.py@google-cloud-dlp-v3.40.0:7363`; keep the label.
  - SD1 R4 line 95: replace with `• No documented way to submit an arbitrary string to a content policy was found (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages, release notes and the client methods) **[Not disclosed]**`
  - SD1 R4, add after line 95: `• The roles page defines the permission `dlp.contentPolicies.apply` and the role DLP Content Policies Consumer ("Apply content policies."), and the manage page tells the administrator to grant `roles/dlp.user` to the Gemini Enterprise service account to apply policies (SDP docs, roles and permissions page and manage content policies page, read 2026-10-09) **[Documented]**`
  - SD1 R8 #11 (line 184): replace with `• Content-policy evaluation: the discovery document, RPC reference, REST resource and client list no apply or evaluate method, although the roles page defines the permission `dlp.contentPolicies.apply` and a role "Apply content policies."; how a caller outside Gemini Enterprise submits a string is not documented (checked the discovery document, RPC reference, content-policy, manage-policies, roles and REST resource pages and the client; needs a Gemini Enterprise check)`
  - SD1 R8 Summary (line 172): no change needed ("no verified way to apply a content policy to a string" still holds).
  - SD1 R6 line 130: no change.

### T11 — Content-policy price, SLO, evaluation region and storage
- Verdict: STILL OPEN (checked the pricing page, SLA page, limits page, locations page, content-policy page, manage page and the Gemini Enterprise page: the facts are not stated, the one cost sentence is on the Gemini Enterprise page)
- Evidence:
  - Pricing page (`PRC`, raw text, 64 KB): the method table lists "projects.image.redact | projects.content.inspect | projects.content.deidentify | projects.content.reidentify" and no content-policy row; a search for "polic" finds only unrelated lines.
  - SLA page (`SLA`): ""Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests." No content-policy service.
  - Limits page (`LIM`): a "Content policy limits" table exists ("Maximum size of a single PDF | 50 MB … Maximum size of a single plain text or image file | 10 MB").
  - Gemini Enterprise page `https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data`: "There's no additional cost to use Sensitive Data Protection." and "Sensitive Data Protection supports the global, EU, and US multi-regions." and "Make sure to create the policy in the same region as the apps you want to apply it to."
  - Locations page (`DOCS/locations`): no content-policy entry (matches only on navigation links). Content-policy and manage pages: no statement on storage of evaluated content; the manage page says "Select the region or multi-region where you want to store the content policy".
- Label to use: price, SLO, evaluation location, storage of evaluated content: `[Not disclosed]` naming the pages. Gemini Enterprise cost and regions: `[Documented]` (Gemini Enterprise docs, not SDP docs).
- Draft impact: none to text (INV(a) storage cell, INV(e) content policy row, INV(f) content policy location already say this). Add "SLA page" to the "checked" list in INV(e) content policy row price cell: `Content policy price and availability objective: no row on the pricing page or the SLA page [Not disclosed] (checked PRC, SLA)`. The file limit values in that row match the limits page exactly.

### T12 — SD3 R1 and R4 Summaries claim bucketing, date shift and time part on detected values
- Verdict: PARTLY RESOLVED (the API accepts these primitives for infoType findings; whether they work on free-text findings stays open for the test, T13) and the Summaries must be narrowed
- Evidence:
  - DISC schema `GooglePrivacyDlpV2InfoTypeTransformation`: "A transformation to apply to text that is identified as a specific info_type." with `primitiveTransformation`, and `GooglePrivacyDlpV2PrimitiveTransformation` has the fields `bucketingConfig`, `fixedSizeBucketingConfig`, `dateShiftConfig`, `timePartConfig`, `cryptoHashConfig` and the rest. So the schema allows them in an infoType transformation.
  - The type descriptions limit the data: `FixedSizeBucketingConfig` "This can be used on data of type: double, long."; `BucketingConfig` "This can be used on data of type: number, long, string, timestamp."; `TimePartConfig` "For use with `Date`, `Timestamp`, and `TimeOfDay`, extract or preserve a portion of the value."; `DateShiftConfig.cryptoKey` "Can only be applied to table items." (REST pages carry the same text).
  - Transformations reference (`DOCS/transformations-reference`), Input Type column: Redaction, Replacement and the bucketing rows "Any"; Date Shifting and Extract time data "Dates/Times"; hash "Strings or integers"; bucketing text: "The bucketing transformations serve to de-identify numerical data".
- Label to use: Summaries may say redact, replace, mask and hash for detected values `[Documented]`; bucketing and date shifting for free-text findings stay `[To be verified]` (bullet already in R4).
- Draft impact:
  - `sdp_cols_a.md` SD3 R1 Summary (line 393), replace with (44 words): `Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method finds sensitive values, then redacts, replaces, masks or hashes them. Bucketing and date shifting are offered but shown only on table fields. It returns the item and a summary of changes. **[Documented]**`
  - SD3 R4 Summary (line 435), replace with (40 words): `Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Each detected value is then redacted, replaced, masked or hashed; bucketing and date shifting are shown only on table fields. **[Documented]**`
  - SD3 R4 [To be verified] bullet (line 452): add a preceding `[Documented]` bullet: `• The API accepts `fixedSizeBucketingConfig`, `bucketingConfig`, `dateShiftConfig` and `timePartConfig` inside an infoType transformation, and describes them for numeric, timestamp and date values; `dateShiftConfig.cryptoKey` "Can only be applied to table items." (API discovery document revision 20261006, schemas PrimitiveTransformation, DateShiftConfig, TimePartConfig) **[Documented]**` Keep the [To be verified] bullet.
  - `sdp_inventory.md` INV(c) bucketing (2), date shifting and time extraction rows: keep `[To be verified]` for free text; no change.

### T14 — SD4 R4 Summary says AES-SIV tokens are of "any length" against a documented conflict
- Verdict: RESOLVED (drafting fix; the conflict is real and confirmed, the test is T15)
- Evidence: three sources re-read on 2026-10-09. (1) Transformations reference table, AES-SIV row: "Replaces an input value with a token, or surrogate value, of the same length using AES in Synthetic Initialization Vector mode (AES-SIV)." (2) Same page, deterministic section: "Does not preserve the character set ("alphabet") or length of the input value post-encryption." (3) `DOCS/pseudonymization`: "This method produces a hashed value, so it does not preserve the character set or the length of the input value." API: `CryptoDeterministicConfig` "Outputs a base64 encoded representation of the encrypted output." (DISC). None says "any length".
- Label to use: two `[Documented]` bullets, one per source (already in R4); the Summary stays `[Documented]` once it states the disagreement.
- Draft impact: `sdp_cols_b.md` SD4 R4 Summary (line 54), replace with (42 words): `Summary: **Standard keyed encryption, not a model.** AES-SIV gives base64 tokens, and the docs disagree on whether the length is kept; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. **[Documented]**` In INV(c) AES-SIV row add the length conflict: `Transformations table row says the token has the same length as the input, while the same page's deterministic section and the pseudonymization page say length is not preserved [Documented] (DOCS transformations-reference, DOCS pseudonymization)` (T15 in the same row stays open).

### T16 — Three SD6 Summaries labelled [Documented] rest partly on [Not disclosed] bullets
- Verdict: RESOLVED (drafting fix, no research; rule: README section 3 rule 5)
- Evidence: SD6 R2 Summary sentence "Other harm categories are not listed." rests on the bullet "The reference lists only these three image context detectors … **[Not disclosed]**"; R4 Summary "with unnamed models" rests on "Model names, architecture, training data … **[Not disclosed]**"; R5 Summary "They show no worked example of an image safety response." rests on "Worked request or response samples … **[Not disclosed]**". The first sentence of each Summary and its remaining sentences rest on `[Documented]` bullets.
- Label to use: Summaries keep `[Documented]` once the absence sentences are removed; the absences stay as `[Not disclosed]` Detail bullets and in R8.
- Draft impact (`sdp_cols_b.md`):
  - SD6 R2 Summary, replace with (28 words): `Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a one-sentence definition, and the docs describe the use as content moderation. **[Documented]**`
  - SD6 R4 Summary, replace with (39 words): `Summary: **A classifier over the whole image.** Image context detectors run an image content classification mode that assigns one theme or category. The models are described as trained mainly on real-world images. Rules can use the findings from June 2026. **[Documented]**`
  - SD6 R5 Summary, replace with (29 words): `Summary: **A rated finding for the image, or a fully blanked image.** The docs say classification produces a label, and give a likelihood bucket per finding rather than a number. **[Documented]**`
  - The R8 Summary and R8 bullets already carry the omitted questions; no R8 change.

### T17 — "No verdict" in SD2 R5 and SD4 R5 Summaries under [Documented] with [Inferred] support
- Verdict: RESOLVED (documented response fields found; the Summaries can be reworded to a positive, documented statement)
- Evidence: REST `InspectContentResponse` (`REST/InspectContentResponse`, Last updated 2025-04-30): the only field is "result … The findings." REST `ReidentifyContentResponse`: "item … The re-identified item." and "overview … An overview of the changes that were made to the item." REST `DeidentifyContentResponse`: "item … The de-identified item." and "overview". The same fields are in the discovery document schemas.
- Label to use: the response-field facts are `[Documented]`. "There is no verdict" is an absence claim and is not written as a Summary fact; the existing `[Inferred]` bullets stay for it.
- Draft impact:
  - `sdp_cols_a.md` SD2 R5 Summary (line 304), replace with (36 words): `Summary: **Same findings as inspection, under your detector name.** A custom match returns the name you chose and a likelihood you set, Very likely unless changed, after any rules have run. The response holds only the findings. **[Documented]**`
  - SD2 R5, add a bullet before the [Inferred] "No verdict" bullet (line 313): `• The inspect response has the single field `result`, "The findings." (SDP docs, REST InspectContentResponse page, read 2026-10-09) **[Documented]**` Keep the [Inferred] "No verdict is produced" bullet.
  - `sdp_cols_b.md` SD4 R5 Summary (line of "### R5" Summary), replace with (40 words): `Summary: **Transformed text plus a summary of changes.** The response returns the item with tokens or restored values and an overview listing each transformation with success or error counts. A token is a surrogate name, a length and the encrypted value. **[Documented]**`
  - SD4 R5, add before the final [Inferred] bullet: `• The REST response for `content.reidentify` has the fields `item` ("The re-identified item.") and `overview` ("An overview of the changes that were made to the item.") (SDP docs, REST ReidentifyContentResponse page, read 2026-10-09) **[Documented]**` and add the REST ReidentifyContentResponse, DeidentifyContentResponse and InspectContentResponse URLs to the R9 of SD4 and SD2 (`https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ReidentifyContentResponse`, `.../DeidentifyContentResponse`, `.../InspectContentResponse`).
  - SD3 R5: Summary is silent on verdict; no change.

### T18 — SD5 R1 and R2 Summaries list "faces" without the Preview status
- Verdict: RESOLVED
- Evidence: Infotype reference (`DOCS/infotypes-reference`, Last updated 2026-10-07): "OBJECT_TYPE/PERSON/FACE | Image of a person's face. This infoType detector is in Preview." No other object or image-context infoType carries a stage mark on that page. Release notes: December 15, 2025 "The OBJECT_TYPE/PERSON/FACE infoType detector is available in Preview in global and the asia, europe, and us multi-regions."; November 03, 2025 "The OBJECT_TYPE/PERSON/PASSPORT and OBJECT_TYPE/PERSON/PHOTO_ID_CARD infoType detectors are available in global and the asia, europe, and us multi-regions."; June 08, 2026 the same wording for OBJECT_TYPE/PERSON/SIGNATURE; January 16, 2026 the same for the three IMAGE_TYPE/CONTEXT detectors (without a stage word).
- Label to use: Face detector in Preview `[Documented]`. The other object detectors have no stage stated: `[Not disclosed]` (checked the reference and release notes; "available" without a stage word).
- Draft impact (`sdp_cols_b.md`):
  - SD5 R1 Summary, replace with (44 words): `Summary: **Finds and blanks sensitive text and objects in images.** The service reads text in an image with OCR and also detects objects such as passports, photo ID cards, licence plates and faces (Preview). It returns boxes, or the image with opaque rectangles over matches. **[Documented]**`
  - SD5 R2 Summary, replace with (32 words): `Summary: **Sensitive text and ID-type objects in pictures.** Text infoTypes run on text read from the image, and object detectors cover faces (Preview), passports, photo ID cards, signatures, licence plates, barcodes and whiteboards. **[Documented]**`
  - SD5 R8 #10: replace with `• Launch stage of the other object detectors and of the three image-context detectors: the reference marks only the face detector as Preview and the release notes say "available" without a stage (checked the reference and release notes of 2025-11-03, 2025-12-15, 2026-01-16 and 2026-06-08)`.
  - `sdp_inventory.md` INV(b) image object detectors row: add `OBJECT_TYPE/PERSON/FACE is in Preview [Documented] (DOCS infotypes-reference)`; other detectors' stage `[Not disclosed]` (checked the reference and release notes).

### T19 — One label pattern for the "out of purpose" statement (R015: [Inferred])
- Verdict: RESOLVED (ruling R015 item 1 applied)
- Evidence: R015: "`[Inferred]`, with the premise named in the bullet … applied consistently in every column. Upgrade to `[Documented]` only with a URL and a verbatim vendor sentence stating the scope." Premise sentence, `DOCS/sensitive-data-protection-overview`: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." That sentence states purpose, not a ban on other functions, so the out-of-purpose conclusion stays `[Inferred]`.
- Label to use: `[Inferred]` for the out-of-purpose statement in all six columns; the purpose sentence itself `[Documented]`.
- Draft impact:
  - `sdp_cols_b.md` SD4 R2 (line 33), replace with: `• Out of purpose: prompt injection, jailbreaks, toxicity and topic control are not named on any page checked (overview, method-types, pseudonymization, transformation-reference and quickstart); this is a scope judgement (premise: the purpose sentence in the overview, "discover, classify, and de-identify sensitive data") **[Inferred]**`
  - SD5 R2 (line 234), replace with: `• Out of purpose: prompt injection or jailbreak text inside an image is not named as something the service looks for (premise: the overview's purpose sentence and the image pages checked, which name only infoType detection and redaction) **[Inferred]**` (the clause "OCR text is matched only against the infoTypes requested" is dropped; re-add it as its own bullet only with a quote).
  - SD6 R2 (line 409), replace with: `• Out of purpose: prompt injection, jailbreaks, toxicity in text and topic control are not named on the image concepts, inspect, redact and infoType reference pages (premise: the overview's purpose sentence) **[Inferred]**`
  - `sdp_cols_a.md` SD1 R2 (line 47): split into two bullets: `• Purpose: "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." (SDP docs, overview page, read 2026-10-09) **[Documented]**` and `• Out of purpose: the docs name no prompt-injection, jailbreak, toxicity or topic-drift detector (checked the overview, infoTypes concepts and reference pages); a scope judgement (premise: the purpose sentence above) **[Inferred]**`. SD2 R2 (line 260) and SD3 R2 (line 420) already state their premise; no change.
  - Summaries: SD3 R2 stays `[Inferred]`; no other Summary changes.

### T20 — Limits-page numbers that appear in Summaries
- Verdict: PARTLY RESOLVED, with two corrections (a unit not stated by the page; a "cap" that the REST page calls not hard)
- Evidence (`LIM`, raw text, Last updated 2026-10-07): "Maximum size of each request, except projects.image.redact | 0.5 MB"; "Maximum size of each projects.image.redact request | 4 MB"; "Maximum number of findings per request | 3,000"; "Maximum number of transformations per request | 100"; "Maximum number of custom infoTypes per request | 30"; "Maximum number of regular custom dictionaries per request | 10"; "Maximum number of inspection rule sets per inspection configuration | 10"; "Maximum number of inspection rules per set | 10"; "Maximum length of regular expressions | 1000". The page says "Quotas and limits specified in this document are subject to change." The two rate-quota rows both carry the name "Number of requests to a regional endpoint per minute per region" with 600 ("Requests made to the global endpoint (dlp.googleapis.com) where a location is specified") and 100 ("Requests made to a regional endpoint (dlp.REGION.rep.googleapis.com)"). The cloud.google.com copy (`https://cloud.google.com/sensitive-data-protection/limits`) returned HTTP 200 and an empty body again. REST `InspectConfig.limits.maxFindingsPerRequest` (`REST/InspectConfig`, Last updated 2026-09-05): "If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower. This value isn't a hard limit."
- Label to use: all table values `[Documented]` (LIM, read 2026-10-09). "Regex length of 1000" with no unit `[Documented]`. The REST "isn't a hard limit" wording is a second `[Documented]` fact; the two sources are kept as two bullets.
- Draft impact:
  - CORRECTION `sdp_cols_a.md` SD2 R6 Summary (line 318): the page gives no unit for the regex limit ("1000-character" is not stated). Replace with (41 words): `Summary: **A CustomInfoType object inside the inspect request.** Give a name, a dictionary, regex or stored reference, an optional base likelihood and rules. Limits per request include 30 custom detectors, 10 regular dictionaries, 10 rule sets and a regex length of 1000. **[Documented]**` The hotword-window bullet (line 276) is a different limit ("cannot exceed 1000 characters") and stays.
  - CORRECTION `sdp_cols_a.md` SD1 R6 Summary (line 120): "capped at … 3,000 findings" is contradicted in part by the REST page. Replace with (45 words): `Summary: **A project, a location and a list of infoTypes.** Send the text, the infoTypes and an optional minimum likelihood. The caller needs billing, the API enabled and the DLP User role. Requests are capped at 0.5 MB; REST calls the 3,000-finding limit not hard. **[Documented]**`
  - SD1 R6, add a bullet after the content limits table (after line 138): `• Findings limit, second source: "If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower. This value isn't a hard limit." (SDP docs, REST InspectConfig page, read 2026-10-09) **[Documented]**` and add `https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig` to SD1 R9 if absent.
  - SD3 R6 Summary ("3,000 findings"): no change; for de-identification the cap is a stated error ("Too many findings to de-identify. Retry with a smaller request.", DOCS deidentify-sensitive-data) and `FindingLimits` is "not used for de-identification" per the drafts' own bullet.
  - SD3 R6 and SD5 R6 Summaries (100 transformations; 4 MB and 0.5 MB): match the page; no change.
  - INV(e): row 100 (maximum findings per request) already carries the REST text; add the sentence `The REST page says this value is not a hard limit [Documented] (REST InspectConfig)`. Row 104: no change (all numbers match, including "regular expression length 1000").

### T21 — INV(e) applies the 0.5 MB and 100-transformation limits to content.reidentify as [Documented]
- Verdict: RESOLVED (the column draft is right, the inventory overstates)
- Evidence (`LIM`): the section is headed "Content inspection and de-identification limits" and reads "Sensitive Data Protection enforces the following usage limits for inspecting and de-identifying content sent directly to the DLP API as text or images". The page contains no occurrence of "reidentify" or "re-identif". REST `projects.content.reidentify` method page: description "Re-identifies content that has been de-identified."; unlike the inspect and deidentify pages ("This method has limits on input size…") it states no limits.
- Label to use: `[Inferred]` for "the same limits apply to content.reidentify" (premise: re-identification takes the same ContentItem request shape).
- Draft impact: `sdp_inventory.md` INV(e) rows 1 (0.5 MB) and 6 (100 transformations): change "Applies to" to `content.inspect, content.deidentify` and append to the Value cell: `The limits table is headed as covering inspecting and de-identifying content and does not name content.reidentify [Documented] (LIM). Whether it applies to content.reidentify [Inferred] (premise: the request carries the same item and configuration types)`. `sdp_cols_b.md` SD4 R6 line 127 is correct as drafted; no change.

### T22 — SLA coverage of content.reidentify and image.redact: Inferred in columns, Not disclosed in the inventory
- Verdict: RESOLVED (one pattern chosen: documented definition plus Not disclosed absence)
- Evidence (`SLA`, raw text): ""Covered Service" means Cloud Data Loss Prevention (DLP) content.inspect API requests or content.deidentify API requests." The uptime tables list only "content.inspect API requests" and "content.deidentify API requests" (99.5% and 99%).
- Label to use: the definition `[Documented]`; "no objective for content.reidentify or image.redact" `[Not disclosed]` (checked the SLA page).
- Draft impact:
  - `sdp_cols_b.md` SD4 R6 line 133 (`[Inferred]` "Because the SLA names only inspect and deidentify requests…"): replace with `• No uptime objective for `content.reidentify` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**`
  - SD5 R6 line 320, replace with: `• No uptime objective for `image.redact` (checked the SLA page, whose covered services are `content.inspect` and `content.deidentify`) **[Not disclosed]**` (the existing [Documented] covered-service bullet in SD4 R6 line 132 is the source; add the same bullet in SD5 R6 before it).
  - INV(e) Availability SLO row: already `[Not disclosed]` (checked the SLA page); no change.
  - SD4 R8 #10 and SD5 R8: no change.

### T23 — Pricing figures and free-tier wording
- Verdict: RESOLVED
- Evidence (`PRC`, raw text): inspection "0 byte to 1 gibibyte | $0.00 (Free) / 1 gibibyte, per 1 month / account", "1 gibibyte to 1 tebibyte | $3.00 / 1 gibibyte, per 1 month / account", "1 tebibyte and above | $2.00 / 1 gibibyte, per 1 month / account"; transformation "$0.00 (Free)", "$2.00", "$1.00" for the same tiers; "A minimum of 1 KB is billed per content inspect or transform request."; "Simple redaction, which includes the RedactConfig and ReplaceWithInfoTypeConfig transformations, is not counted against the number of bytes transformed when infoType inspection is also configured."; method table: image.redact Yes/No, content.inspect Yes/No, content.deidentify Yes/Yes, content.reidentify Yes/Yes (inspection/transformation). "per month per account" is on the page.
- Label to use: `[Documented]` (PRC, read 2026-10-09; the page is under cloud.google.com, not docs.cloud.google.com).
- Draft impact: none. All quoted figures in SD1 R6/R7, SD3 R5 to R7, SD4 R6/R7, SD5 R6, SD6 R6 and INV(e) match.

### T24 — INV(e) omits the stored-infoType file and row limits
- Verdict: RESOLVED
- Evidence (`LIM`, "Stored infoType limits"): "Maximum size of a single input file stored in Cloud Storage | 200 MB"; "Maximum combined size of all input files stored in Cloud Storage | 1 GB"; "Maximum number of input files stored in Cloud Storage | 100"; "Maximum size of an input column in BigQuery | 1 GB"; "Maximum number of input table rows in BigQuery | 5,000,000"; "Maximum size of output files | 500 MB".
- Label to use: `[Documented]` (LIM).
- Draft impact: `sdp_inventory.md` INV(e) "Custom dictionary size" row (no new row; block (e) stays at 16 rows): append to the Value cell `; stored infoType creation: input file in Cloud Storage 200 MB each, 1 GB combined, 100 files; BigQuery input column 1 GB and 5,000,000 rows; output files 500 MB [Documented] (LIM)`. Optional for `sdp_cols_a.md` SD2 R6 stored-infoType sub-bullets (lines 337 to 341): add the three missing rows (1 GB combined, 100 files, 1 GB BigQuery column) as sub-bullets of the same group.

### T42 — Which infoTypes run when none are given
- Verdict: PARTLY RESOLVED (all wordings re-confirmed verbatim; ALL_BASIC is defined on no page; one new fact for images; membership is T43)
- Evidence:
  - `DOCS/concepts-infotypes`: "If you don't specify any infoTypes, Sensitive Data Protection uses a default infoTypes list that is intended for testing purposes only. The default list might not be suitable for your use cases."
  - REST `InspectConfig` (`REST/InspectConfig`, Last updated 2026-09-05): "When no InfoTypes or CustomInfoTypes are specified in a request, the system may automatically choose a default list of detectors to run, which may change over time."
  - REST method pages `projects.content.inspect`, `projects.content.deidentify`, `projects.image.redact` (all three, same text): "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated."
  - `DOCS/deidentify-sensitive-data`: "Otherwise, Sensitive Data Protection scans for a default set of infoTypes (ALL_BASIC), some of which you might not need." and "causes the transformation to apply to all built-in infoTypes that don't have a transformation provided."
  - `DOCS/redacting-sensitive-data-images`: "Unless you specify specific information types (infoTypes) to search for, Sensitive Data Protection searches for the most common infoTypes. Default infoTypes don't include objects in images." `DOCS/inspecting-images`: "If you don't specify specific information types (infoTypes) to search for, Sensitive Data Protection searches for the most common infoTypes."
  - Release notes February 11, 2019: "Updated the default list of infotypes included in ALL_BASIC." and "Clarified the documentation as to what behavior users can expect for the ALL_BASIC."
  - ALL_BASIC: the term appears only on the de-identify page and the 2019 release note in the pages read (concepts, InspectConfig, the three method pages, both image guides, inspecting-text, infoTypes reference, REST infoTypes.list, which defaults to `supportedBy=INSPECT`). No page defines its members.
- Label to use: each wording `[Documented]` as its own bullet; ALL_BASIC membership `[Not disclosed]` (checked the pages above); membership at run time is T43.
- Draft impact:
  - `sdp_cols_a.md` SD1 R6: add after the "source 3" bullet (line 127): `• Default list, source 4: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated." (SDP docs, REST projects.content.inspect page, read 2026-10-09) **[Documented]**` and `• The members of ALL_BASIC are not defined on any page checked (concepts, REST InspectConfig, content.inspect, content.deidentify and image.redact method pages, image guides, infoType reference, infoTypes.list page, release notes) **[Not disclosed]**`
  - `sdp_cols_b.md` SD5 R6 default bullets and SD6 R6 [Not disclosed] bullet: add `• For images, the redaction guide says "Default infoTypes don't include objects in images." (SDP docs, redacting sensitive data in images page, read 2026-10-09) **[Documented]**` (an image-context or object detector therefore has to be named; SD6 R6 already says categories must be named, and its [Not disclosed] bullet about defaults can be replaced by this one if its subject is the same).
  - SD3 R4 no-infoType bullet: add the quote "applies to all built-in infoTypes that don't have a transformation provided" and the ALL_BASIC quote if absent.
  - SD1 R8 #6 and the R8 Summary ("unclear default infoTypes"): keep.

### T44 — PERSON_NAME version change and promotion date
- Verdict: PARTLY RESOLVED (state on 2026-10-09 recorded; promotion not yet due; one CORRECTION in the inventory)
- Evidence: release notes (Last updated 2026-10-07), top entry October 03, 2026: "A new version with an updated name dictionary is available for the PERSON_NAME infoType detector. You can try it out by setting InfoType.version to latest … In 30 days, the new version will be promoted to stable." There is no newer entry than 2026-10-03 on the read date, so no promotion note yet (30 days from 2026-10-03 is 2026-11-02). Earlier precedent in the same notes: July 19, 2022 "In 30 days, the new model will be promoted to stable." followed by August 29, 2022 "has been promoted to be the default detection model". `InfoType.version` is described as "Optional version name for this InfoType." (`REST/InfoType`). CORRECTION source, release note July 13, 2026: "If you leave InfoType.version unset or set it to stable when setting the MEDICAL_ID infoType in your InspectConfig, Sensitive Data Protection includes MEDICAL_RECORD_NUMBER findings as type MEDICAL_ID in the scan results. You can still use the old functionality by setting InfoType.version to legacy for the next 90 days."
- Label to use: release-note facts `[Documented]`; the expected promotion date about 2026-11-02 and the legacy window ending about 2026-10-11 are `[Inferred]` (premise: 30 and 90 days counted from the note date).
- Draft impact:
  - CORRECTION `sdp_inventory.md` INV(b) Health row, infoType-count cell: "A MEDICAL_ID behaviour change took effect for InfoType.version latest, with the old behaviour on stable [Documented] (DOCS release-notes)" is wrong (the note applies to unset and stable, and the old behaviour is reached with legacy). Replace with `Since 2026-07-13, MEDICAL_ID with InfoType.version unset or stable also reports MEDICAL_RECORD_NUMBER findings as MEDICAL_ID; the old behaviour is available with version legacy for 90 days [Documented] (DOCS release-notes). The legacy window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)`.
  - `sdp_cols_a.md` SD1 R4 line 83 (versioning bullet) and R7 line 168: no change to facts; append to R7 line 168 `no promotion note had appeared by 2026-10-09 (SDP docs, release notes, read 2026-10-09)`. Split the existing line 83 bullet: it carries three facts; make `stable`, `latest` and `legacy` one bullet and the "In 30 days" quote another, both `[Documented]`.
  - Re-read the release notes on the P7 and P9 dates (a further `PERSON_NAME` or `MEDICAL_ID` entry would change these facts). T45 (effect on a fixed test set) stays open.

### T46 — Dated counts made by the drafters
- Verdict: RESOLVED (recount on 2026-10-09 agrees with the drafts)
- Evidence: `DOCS/infotypes-reference`, Last updated 2026-10-07. Table "InfoType descriptions": 522 cells in the Name/Description table, 261 distinct names. Table "InfoType categories": the same 261 names, of which 240 have availability `ANY_LOCATION` and 21 do not. Location filter list: GLOBAL plus 50 countries = 51 entries (the list then continues with six category filters). `DOCS/locations`: 43 distinct region names in the table. The page says: "The Sensitive Data Protection team releases new infoType detectors and groups periodically. To get the latest list of built-in infoTypes, call the infoTypes.list method of Sensitive Data Protection." (counted by script from the raw text; script logic in `benchtest/scratchpad/resolver/r1`).
- Label to use: `[Inferred]` with the counting rule named, as drafted (Google gives no totals).
- Draft impact: none to the numbers (261, 240, 21, 51, 43 stand). Replace the process wording "(my count of …)" per T89 (resolutions_2). Keep the page's "periodically" sentence as a `[Documented]` bullet next to the counts in SD1 R2.

### T47 — Regex engine for custom regex detectors
- Verdict: PARTLY RESOLVED (the REST reference points to RE2 syntax; supported constructs stay a test item)
- Evidence: REST `Regex` page (`REST/Regex`) and discovery schema `GooglePrivacyDlpV2Regex`: "pattern: Pattern defining the regular expression. Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub." The custom regex guide (`DOCS/creating-custom-infotypes-regex`) and the custom infoType overview name no engine (searched for "RE2" and "syntax": no match). The limits page gives only "Maximum length of regular expressions | 1000".
- Label to use: `[Documented]` for "the API reference points to the google/re2 syntax page"; whether every RE2 construct is accepted, and what happens with unsupported ones, `[To be verified]` (needs a test).
- Draft impact: `sdp_cols_a.md` SD2 R4 line 286: replace with `• Regex syntax: the REST Regex reference says "Its syntax (https://github.com/google/re2/wiki/Syntax) can be found under the google/re2 repository on GitHub." (SDP docs, REST Regex page, read 2026-10-09) **[Documented]**` and add `• A docs code sample comment also says "Refer https://github.com/google/re2/wiki/Syntax for creating regular expression." (SDP docs, customize match likelihood page, read 2026-10-09) **[Documented]**` Add `https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex` to SD2 R9. SD2 R8 #1 (line 361): reword to `Which RE2 constructs are accepted by the service and what happens with unsupported ones (the reference names RE2 syntax only; needs testing)`. SD2 R8 Summary keeps "regex engine" only if it still fits ("unsupported regex constructs").

### T49 — Rule order: guide, REST text and the 2026-02-23 release note
- Verdict: PARTLY RESOLVED (the guide and its worked example support order-as-written; the REST sentence about exclusion rules running last is still on a page updated after the release note, so the conflict stays; behaviour test is T50)
- Evidence:
  - Guide (`DOCS/creating-custom-infotypes-rules`, Last updated 2026-10-07): "Sensitive Data Protection applies the rules in the order you specify them in the ruleset. Therefore, the order of your rules can affect the results of the Sensitive Data Protection operation." Worked example: "If you specify the exclusion rule first, then the DOCUMENT_TYPE/CONTEXT/HEALTH findings are excluded from the result set before they can be used to provide context to the adjustment rule."
  - REST `InspectionRuleSet.rules` (`REST/InspectConfig`): "The rules are applied in order." REST `CustomInfoType.detectionRules`: "Rules are applied in the order that they are specified."
  - REST `InspectConfig.ruleSet` (same page, Last updated 2026-09-05): "Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type."
  - Release notes February 23, 2026: "The following features are in General Availability: … Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset."
- Label to use: all four statements `[Documented]` as separate bullets; the draft's inference that the REST text "may be older" is weakened (the REST page footer, 2026-09-05, is later than the release note, 2026-02-23) and stays `[Inferred]` only with that premise.
- Draft impact: `sdp_cols_a.md` SD2 R4, replace the three order bullets (lines 288 to 291 region: "Rule order, source 1", "source 2", "context"): keep source 1 and 2 unchanged; add `• Rule order, worked example: "If you specify the exclusion rule first, then the DOCUMENT_TYPE/CONTEXT/HEALTH findings are excluded from the result set before they can be used to provide context to the adjustment rule." (SDP docs, creating custom infoTypes rules page, read 2026-10-09) **[Documented]**`; replace the "context" bullet with `• Rule order, release note 2026-02-23 puts "Enhanced rule ordering, which lets you chain rules based on the order you specify them in the ruleset" at general availability; the REST page that says exclusion rules run last has a later footer date (2026-09-05), so it may be unchanged text rather than older text (premise: footer dates; they do not prove edits) **[Inferred]**`. SD2 R5 line 306 ("Rules are applied in the order that they are specified") stays. SD2 R8 #3 and R8 Summary: keep the rule-order question (needs testing, T50).

---

## Summary table

| Tn | Verdict | Label | Changes Summary? |
|---|---|---|---|
| T1 | RESOLVED (R018) | n/a | optional: SD1 R4 Summary (drop "formerly called" sentence) |
| T2 | RESOLVED (R018 + T9) | n/a | no |
| T3 | RESOLVED (R018) | n/a | no |
| T4 | RESOLVED (R018) | n/a | no |
| T5 | RESOLVED (R011, R012 precedent; main to log) | n/a | no |
| T6 | RESOLVED | [Inferred] | no |
| T7 | RESOLVED (R007.1 precedent; main to log) | [Documented] | no |
| T8 | STILL OPEN (main decision; default not used) | n/a | no |
| T9 | STILL OPEN (no apply or evaluate method documented; R018 upgrade condition not met) | [Documented] methods; [Not disclosed] absence; [Inferred] consumer | no (R8 bullet only) |
| T11 | STILL OPEN (checked pricing, SLA, limits, locations, content-policy, manage, Gemini pages) | [Not disclosed] | no |
| T12 | PARTLY RESOLVED | [Documented] / [To be verified] | yes: SD3 R1, SD3 R4 |
| T14 | RESOLVED | [Documented] | yes: SD4 R4 |
| T16 | RESOLVED | [Documented] | yes: SD6 R2, R4, R5 |
| T17 | RESOLVED | [Documented] | yes: SD2 R5, SD4 R5 |
| T18 | RESOLVED | [Documented] / [Not disclosed] | yes: SD5 R1, SD5 R2 |
| T19 | RESOLVED (R015) | [Inferred] | no |
| T20 | PARTLY RESOLVED + 2 CORRECTIONS | [Documented] | yes: SD1 R6, SD2 R6 |
| T21 | RESOLVED | [Inferred] (reidentify) | no |
| T22 | RESOLVED | [Documented] / [Not disclosed] | no |
| T23 | RESOLVED | [Documented] | no |
| T24 | RESOLVED | [Documented] | no |
| T42 | PARTLY RESOLVED | [Documented] / [Not disclosed] | no |
| T44 | PARTLY RESOLVED + CORRECTION (INV(b) Health row) | [Documented] / [Inferred] | no |
| T46 | RESOLVED | [Inferred] | no |
| T47 | PARTLY RESOLVED | [Documented] / [To be verified] | no |
| T49 | PARTLY RESOLVED | [Documented] / [Inferred] | no |

## Report

Counts (26 items): RESOLVED 17 (T1, T2, T3, T4, T5, T6, T7, T14, T16, T17, T18, T19, T21, T22, T23, T24, T46), PARTLY RESOLVED 6 (T12, T20, T42, T44, T47, T49), STILL OPEN 3 (T8, T9, T11), CORRECTION 0 as a stand-alone verdict. Corrections found inside items: T20 (two Summaries), T44 (one inventory cell).

CORRECTION items:
- T20: SD2 R6 Summary says "1000-character regexes"; the limits page gives "Maximum length of regular expressions | 1000" with no unit.
- T20: SD1 R6 Summary says requests are "capped" at 3,000 findings; the REST InspectConfig page says "This value isn't a hard limit."
- T44: INV(b) Health row says the MEDICAL_ID change applies to version `latest` with the old behaviour on `stable`; the 2026-07-13 note says unset or `stable` get the change and `legacy` (for 90 days) gets the old behaviour.

Summaries that must change: SD3 R1, SD3 R4 (T12); SD4 R4 (T14); SD6 R2, SD6 R4, SD6 R5 (T16); SD2 R5, SD4 R5 (T17); SD5 R1, SD5 R2 (T18); SD1 R6, SD2 R6 (T20). Optional: SD1 R4 (T1, drop the "formerly called Cloud DLP" sentence). New text, with word counts, is in the entries above.

T9 headline: no direct apply or evaluate method for content policies is documented (discovery document revision 20261006, RPC reference, REST pages, IAM page, Gemini Enterprise API and docs, release notes, Python client v3.40.0). The column question is not reopened.
