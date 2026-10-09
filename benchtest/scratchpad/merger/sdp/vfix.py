"""P7 verifier fixes applied in place to the final files (sdp_review.md fixes 1-7, optional items taken, main's rulings Q1 and Q2)."""
import json, sys
sys.path.insert(0, "/home/user/guardrail_research/benchtest/scratchpad/merger/sdp")
import engine
from engine import Doc, ROOT, LOG

cols = Doc("cols", open(ROOT + "sdp_two_level.md", encoding="utf-8").read().rstrip("\n").split("\n"), "col")
inv = Doc("inv", open(ROOT + "sdp_inventory_final.md", encoding="utf-8").read().rstrip("\n").split("\n"), "inv")
REPO = "**[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**"
d = cols

# ---- Fix 1 (inventory f)
inv.cell("(f)", "Data handling", 1,
         old="Sensitive Data Protection is listed among the Google Cloud Platform Services and the Service Specific Terms have no section for it [Documented] (Google Cloud terms services list and Service Specific Terms, not SDP docs).",
         repl="Sensitive Data Protection is listed among the Google Cloud Platform Services [Documented] (Google Cloud terms services list, not SDP docs). A Sensitive Data Protection section in the Service Specific Terms [Not disclosed] (checked the Service Specific Terms for Sensitive Data Protection, Data Loss Prevention and DLP; the name appears only in the page navigation).",
         tid="V1", reason="absence claim was labelled [Documented]; now [Not disclosed] naming what was checked (README section 3 rule 2, R020)")

# ---- Fix 2 (SD6 R2, R8)
d.rep("SD6 R2", "Summary: ",
      "Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a short two-sentence description, and the docs describe the use as content moderation. **[Documented]**",
      "V2", "each image-context entry has two sentences in the reference, not one; the 'content moderation' claim needs an R2 bullet", full=True)
d.ins_before("SD6 R2", "• `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`: \"A finding of this type",
             '• Stated use: "You can use this feature to support content moderation and enforce acceptable use policies." (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**',
             "V2", "supports the 'content moderation' clause of the R2 Summary from inside R2")
d.sub("SD6 R8", "How strictly \"racy\" and \"sexually suggestive\" are defined", "(the reference gives a one-sentence definition only)",
      "(the reference gives a two-sentence description only)", "V2", "matches the reference")

# ---- Fix 3, 4 (SD4 Summaries)
d.rep("SD4 R4", "Summary: ",
      "Summary: **Standard keyed encryption.** AES-SIV gives base64 tokens, and the docs disagree on whether the length is kept; format-preserving encryption keeps length and a chosen alphabet, though the docs steer users to AES-SIV. Keys can be wrapped by Cloud KMS. **[Documented]**",
      "V3", "the lead 'not a model' rested on an [Inferred] bullet under a [Documented] label", full=True)
d.rep("SD4 R6", "Summary: ",
      "Summary: **Needs a key, a surrogate name and a supported input.** The documented setup uses a Cloud KMS wrapped key in a matching region, a surrogate annotation for free text, and values within AES-SIV or FPE limits. API keys cannot be used with wrapped keys. **[Documented]**",
      "V4", "the Summary said a wrapped key is required, but SD4 R4 documents three key types (wrapped, transient, unwrapped); the wrapped key is the quickstart setup", full=True)

# ---- Fix 5 (inference inside [Documented] bullets)
d.rep("SD1 R7", "• The first gibibyte of content inspected each month per account is free", [
    '• The first gibibyte of content inspected each month per account is free, and billing information is still required: "Sensitive Data Protection requires billing information for all accounts before you can start using the service." (SDP pricing page, read 2026-10-09) **[Documented]**',
    "• A small labelled test set therefore stays within the free tier (premise: the free first gibibyte per month on the pricing page) **[Inferred]**",
], "V5a", "inference 'so a small labelled test set costs nothing' split from the quoted fact (README section 3 rule 5)")
d.rep("SD4 R1", "• Cryptographic hashing is the one-way contrast", [
    '• Cryptographic hashing is the one-way contrast: "Unlike other types of crypto-based transformations, this type of transformation isn\'t reversible." (SDP docs, transformations-reference page, read 2026-10-09) **[Documented]**',
    "• The hash row is covered by the masking and de-identification in text column, not here (premise: a pointer to the owning column, not a source fact) **[Inferred]**",
], "V5b", "scope pointer split from the quoted fact")
d.rep("SD5 R1", "• \"Inspection and redaction are two distinct operations:\"", [
    '• "Inspection and redaction are two distinct operations:" and the page defines each (SDP docs, concepts-image-redaction page, read 2026-10-09) **[Documented]**',
    "• One image can therefore be inspected without being changed (premise: inspection is defined separately from redaction and returns only infoTypes and pixel coordinates) **[Inferred]**",
], "V5c", "inference split from the quoted fact")
d.rep("SD5 R2", "• \"Default infoTypes don't include objects in images.\" so object detectors", [
    '• "Default infoTypes don\'t include objects in images." (SDP docs, redacting-sensitive-data-images page, read 2026-10-09) **[Documented]**',
    "• Object detectors must therefore be requested by name (premise: the sentence above) **[Inferred]**",
], "V5d", "inference split from the quoted fact")

# ---- Fix 6 (SD6 R5)
d.rep("SD6 R5", "• Precision, recall, false-positive rate or latency for image safety classification",
      "• Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images (checked the image concepts, supported-file-types, infoType reference and likelihood pages and the release notes) **[Not disclosed]**",
      "V6", "absence claim now names the pages checked (README section 3 rule 2)")

# ---- Fix 7 (SD3 T12 reading was false)
s1 = ("• On the transformation reference page, the time-extraction samples and five of the six date-shift samples use record (table) transformations, and the bucketing section gives only a JSON configuration fragment with no code sample (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**")
s2 = ('• The Go date-shift sample applies `dateShiftConfig` inside an infoType transformation to a plain string item with `DATE` inspection; its comments read `input := "2016-01-10"` and `Will print "2016-01-09"` (SDP docs, transformation reference page, read 2026-10-09) **[Documented]**')
d.rep("SD3 R1", "Summary: ",
      "Summary: **Masks or replaces sensitive text and returns the cleaned item.** The de-identify method redacts, replaces, masks or hashes detected values; one sample also date-shifts a plain string. Bucketing and time extraction are not shown on free text. It returns the item and a change summary. **[Documented]**",
      "V7", "the 'shown only on table fields' claim (T12) was false at source: the Go date-shift sample works on a plain string; bucketing has no code sample", full=True)
d.rep("SD3 R1", "• The date-shift, time-extraction and bucketing code samples on the transformation reference page", [s1, s2], "V7",
      "false [Documented] fact replaced by what the page shows (raw page re-read by the verifier)")
d.rep("SD3 R4", "Summary: ",
      "Summary: **Detect first, then transform each finding.** The call has three parts: the data, the detection settings and the transformation settings. Detected values are redacted, replaced, masked or hashed, and one sample date-shifts a plain string; bucketing and time extraction are not shown on free text. **[Documented]**",
      "V7", "same correction as the R1 Summary", full=True)
d.rep("SD3 R4", "• The date-shift, time-extraction and bucketing code samples use record (table) transformations and a context field", [s1, s2], "V7",
      "false [Documented] fact replaced by what the page shows")
d.rep("SD3 R4", "• Whether the bucketing, date-shift and time-extraction transformations work on infoType findings",
      "• Whether the bucketing and time-extraction transformations work on infoType findings in free text is not stated (checked the transformation reference; the docs table says Any or Dates/Times) **[To be verified]**",
      "V7", "date shifting on free text is shown by the Go sample; the open part is bucketing and time extraction")
d.rep("SD3 R8", "• Whether `FixedSizeBucketingConfig`, `BucketingConfig`, `DateShiftConfig` and `TimePartConfig` apply to infoType findings in free text",
      "• Whether `FixedSizeBucketingConfig`, `BucketingConfig` and `TimePartConfig` apply to infoType findings in free text, and whether date shifting on free text behaves as the Go sample shows (checked the transformation reference; needs testing)",
      "V7", "R8 bullet matches the corrected reading")

# ---- Optional items
inv.cell("(b)", "Health (global)", 2,
         old="the old behaviour is available with version legacy for 90 days [Documented] (DOCS release-notes). The legacy window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)",
         repl="and the note offered the old behaviour with version legacy for the next 90 days [Documented] (DOCS release-notes). That window ends about 2026-10-11 [Inferred] (premise: 90 days counted from the note date)",
         tid="V-opt (past tense)", reason="the window closes on about 2026-10-11, before P9; past tense avoids a stale present-tense claim")
d.sub("SD5 R4", "REST organizations.deidentifyTemplates page", "REST organizations.deidentifyTemplates page", "REST projects.deidentifyTemplates page",
      "V-opt (301)", "organizations.deidentifyTemplates answers HTTP 301 to projects.deidentifyTemplates; the final URL is cited")
d.rep("SD5 R9", "rest/v2/organizations.deidentifyTemplates",
      "• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates",
      "V-opt (301)", "final URL of the 301")

# ---- Main's rulings on the verifier's questions
inv.cell("(d)", "Apigee", 6, new="— (legacy, not in Table 3)", tid="V-Q1 (main ruling)",
         reason="the Apigee extension is deprecated ('no longer supported'); legacy marker instead of the SD3 and SD5 headers. The P8 config markers must include the legacy marker")
d.rep("SD6 R7", "• Test images must not be illegal content or non-consensual explicit imagery", [
    "• The Acceptable Use Policy bars using the services for illegal activity, including child sexual exploitation, and for unlawful purposes including Non-consensual Explicit Imagery (Google Cloud Acceptable Use Policy, read 2026-10-09) **[Documented]**",
    "• The bench's test images should stay within those limits (premise: the bench is a customer using the service under the Acceptable Use Policy; which explicit or violent test images are acceptable is decided in the bench design) **[Inferred]**",
], "V-Q2 (main ruling)", "the AUP bullet keeps to the policy's own wording [Documented]; applying it to the bench is a separate [Inferred] bullet")

open(ROOT + "sdp_two_level.md", "w", encoding="utf-8").write("\n".join(cols.lines) + "\n")
open(ROOT + "sdp_inventory_final.md", "w", encoding="utf-8").write("\n".join(inv.lines) + "\n")
json.dump(LOG, open("/home/user/guardrail_research/benchtest/scratchpad/merger/sdp/vfix_log.json", "w"), indent=1, ensure_ascii=False)
print("v-fix edits:", len(LOG))
