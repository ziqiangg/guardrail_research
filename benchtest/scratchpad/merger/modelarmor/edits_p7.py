"""P7 fix loop: verifier fixes 1-7 (modelarmor_review.md) + main rulings R021 and Q2/Q3."""
from lib import rep, edit, ins_after, ins_before, setsum, editsum, r9add, r9sum, iedit, iapp, IOPS

D = " **[Documented]**"
I = " **[Inferred]**"
ND = " **[Not disclosed]**"
A6 = ["MA1", "MA2", "MA3", "MA4", "MA7", "MA8"]
U_SEGS = "https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services"
U_SETE = "https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions"


def apply_cols(C):
    # fix 1
    for c in ("MA1", "MA2"):
        ins_after(C, c, 1, '• CSAM: "This filter is applied by default', 
                  '• With data residency enforcement on, the feature availability table lists CSAM support as "No" in all seven limited-support locations (asia-northeast1, asia-northeast3, asia-south1, asia-southeast1, australia-southeast2, europe-west2, northamerica-northeast2) (feature availability page, 2026-10-09)' + D,
                  "P7 fix 1 (Summary entailment)")
    # fix 2
    over = '• Over the 130,000-token limit a filter that finds a match returns MATCH_FOUND; otherwise it returns EXECUTION_SKIPPED with "Detection skipped as token limit exceeded." (quotas page, 2026-10-09)' + D
    ins_after(C, "MA5", 6, "Token limit: the table gives 130,000", over, "P7 fix 2 (Summary entailment)")
    ins_after(C, "MA6", 6, "Token limit: 130,000 for Sensitive Data Protection", over, "P7 fix 2 (Summary entailment)")
    # fix 3
    ins_before(C, "MA9", 4, "Extraction engine, parser identity", [
        '• Overview: "Model Armor can screen the following types of documents for safety, prompt injection and jailbreak attempts, sensitive data, and malicious URLs" (overview, 2026-10-09)' + D,
        '• The REST modality reference says the text modality will "sanitize text fields, and text extracted from rich text files (like PDFs, DOCs) and plain text files (like TXT)" (templates reference, 2026-10-09)' + D,
    ], "P7 fix 3 (Summary entailment)")
    ins_before(C, "MA10", 4, "OCR engine, image models, resolution handling", [
        '• Method 2: "Optical character recognition (OCR): Screens the text within images." (overview, 2026-10-09)' + D,
        '• The overview and templates pages label the feature Preview, subject to the Pre-GA terms (overview and templates page, 2026-10-09)' + D,
    ], "P7 fix 3 (Summary entailment)")
    # fix 4 + 5 (columns)
    for c in A6:
        rep(C, c, 4, "A GA date for other load balancers and for Secure Web Proxy",
            '• A GA date for load balancers other than GKE and for Secure Web Proxy (checked the release notes, the networking and integrations pages, and the Service Extensions guides "Configure an extension to call a Google service" and "Configure a traffic extension", neither of which carries a launch-stage label)' + ND,
            "P7 fix 4 (T21: page read verbatim by curl + stdlib HTML parse, R021; process language removed; label To be verified -> Not disclosed)")
        ins_after(C, c, 4, "Service Extensions on application load balancers: Preview",
                  '• The Service Extensions guide for a Model Armor traffic extension says "Consider that Model Armor has a latency of approximately 250 milliseconds" when setting the callout timeout of 10 to 1000 milliseconds; no measurement conditions are given (Service Extensions docs, not Model Armor docs, 2026-10-09)' + D,
                  "P7 fix 5 (latency figure; main ruling Q2)")
        rep(C, c, 8, "Latency per call: no figure published",
            '• Latency per call: the only figure found is "approximately 250 milliseconds" in the Service Extensions guide for load-balancer callouts, with no conditions or per-filter breakdown; the best practices page says "Enabling unnecessary detectors can increase latency" (needs testing)',
            "P7 fix 5 (R8 latency claim contradicted by an official page)")
        r9add(C, c, [U_SEGS, U_SETE], "P7 fix 4 / 5 (Service Extensions guides)")
        s = C[c]["rows"][9]["summary"]
        if c in ("MA1", "MA7"):
            new = s.replace("release notes, and Google's terms pages.", "release notes, Service Extensions guides, and Google's terms pages.")
        else:
            new = s.replace("Google's terms pages.", "Service Extensions guides and Google's terms pages.")
        assert new != s, c
        setsum(C, c, 9, new, "P7 fix 5 (R9 Summary mentions the Service Extensions guides)")
    # fix 6
    for c in A6:
        rep(C, c, 4, "The floor settings page still labels the Google Cloud MCP servers integration", [
            '• The floor settings page still labels the Google Cloud MCP servers integration "(Preview)" (floor settings page, 2026-10-09)' + D,
            '• The dated release note 2026-04-22 (General Availability, sub-bullet above) is taken as current because the page label is undated' + I,
        ], "P7 fix 6 (judgement labelled Documented -> split)")
    # fix 7
    rep(C, "MA9", 3, "Whether a document in a model response is accepted", [
        '• Whether a document can be sent in a model response is not stated (checked the overview, sanitize page, templates reference and release notes)' + ND,
        '• The overview\'s PDF example ("it can be used to compromise any downstream systems processing LLM outputs") concerns systems after the model, not a document sent to the response method' + I,
    ], "P7 fix 7 (absence claim labelled To be verified; test half stays in R8, T61)")
    edit(C, "MA10", 3, "No page shows a request body that sends an image", "**[To be verified]**", "**[Not disclosed]**", "P7 fix 7 (absence claim)")
    edit(C, "MA4", 2, "Release note 2025-09-23 lists vectors", "; the note does not say whether this applies to responses", "", "P7 fix 7 (absence split out of a Documented bullet)")
    ins_after(C, "MA4", 2, "Release note 2025-09-23 lists vectors",
              '• Whether the 2025-09-23 detection improvements apply to responses is not stated (checked the release note)' + ND, "P7 fix 7")


def apply_inv(pre, blocks):
    # fix 4 scope paragraph short names
    k = [i for i, l in enumerate(pre) if l.startswith("Scope:")][0]
    old = "GST = https://cloud.google.com/terms/service-terms."
    assert pre[k].count(old) == 1
    pre[k] = pre[k].replace(old, "GST = https://cloud.google.com/terms/service-terms; SEGS = https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services (Service Extensions docs, not Model Armor docs); SETE = https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions (Service Extensions docs, not Model Armor docs).", 1)
    IOPS.append(dict(loc="Scope paragraph (not parsed)", kind="edit", before=old, after="GST ...; SEGS ...; SETE ...", reason="P7 fix 4 (short names)"))
    SE = "Service Extensions on Cloud Load Balancing"
    iedit(blocks, "b", SE, "Status",
          "GA date for other load balancers and Secure Web Proxy [To be verified] (checked RN, NET and INT; the Service Extensions configuration page returned no text through the raw fetch, so it is unread)",
          "GA date for other load balancers and Secure Web Proxy [Not disclosed] (checked RN, NET, INT, SEGS and SETE; neither Service Extensions page carries a launch-stage label)",
          "P7 fix 4 (T21, R021)")
    iapp(blocks, "b", SE, "Source URL", U_SEGS, "P7 fix 4")
    iapp(blocks, "b", SE, "Source URL", U_SETE, "P7 fix 4")
    iapp(blocks, "b", SE, "Limitations",
         "SEGS, for GKE and OpenAI API endpoints: 'Streaming API responses aren't supported for any API. Model Armor sanitizes the non-streaming responses and ignores the streaming responses.' [Documented] (SEGS; Service Extensions docs, not Model Armor docs). 'any other operation is ignored and allowed to proceed without sanitization' [Documented] (SEGS). 'only the first item in the list of choices is sanitized' [Documented] (SEGS). 'By default, the Fail open option isn't selected', so an error stops request or response processing [Documented] (SEGS). SEGS says 'Consider that Model Armor has a latency of approximately 250 milliseconds' when setting the callout timeout of 10 to 1000 milliseconds, with no measurement conditions [Documented] (SEGS).",
         "main ruling Q3 (route limits) + Q2 (latency), P7")
    return pre
