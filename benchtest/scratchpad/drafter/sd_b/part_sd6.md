## Column SD6: Sensitive Data Protection: Image safety classification (sexual and violent content)
### R1
Summary: **Whole-image safety labels for sexual and violent content.** Three image context detectors judge the overall subject of an image rather than objects inside it. Inspection reports a finding for the image, and redaction based on them blanks the entire image. **[Documented]**
Detail:
• "Sensitive Data Protection can classify and redact images based on their thematic content. This feature helps you identify images that contain sensitive or harmful subject matter according to predefined safety categories." {{D:concepts-image-redaction}} **[Documented]**
• "Sensitive Data Protection analyzes an image's overall context and meaning to determine if it belongs to categories such as sexually explicit or violent content." {{D:concepts-image-redaction}} **[Documented]**
• "You can use this feature to support content moderation and enforce acceptable use policies." {{D:concepts-image-redaction}} **[Documented]**
• The reference lists three image context infoTypes: `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`, `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE` and `IMAGE_TYPE/CONTEXT/VIOLENCE`, introduced as detectors that "analyze an entire image for sensitive or harmful subject matter" {{D:infotypes-reference}} **[Documented]**
• "Unlike object detection, which identifies specific items within an image, this feature assesses the image's subject matter as a whole." {{D:concepts-image-redaction}} **[Documented]**
• "If you configure redaction based on image safety, this feature redacts the entire image." {{D:concepts-image-redaction}} **[Documented]**
• Release notes of 2026-01-16: "The following infoType detectors are available in global and the asia, europe, and us multi-regions:" the three image context detectors {{D:release-notes}} **[Documented]**
• Release notes of 2026-06-23: "Image safety classification infoTypes are now supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." {{D:release-notes}} **[Documented]**
• The calls are the image inspection and redaction methods of the SD5 column (`inspect_content` and `redact_image` in the Python client) ({{L:C|def redact_image(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
### R2
Summary: **Three image categories are listed.** They are sexually explicit, sexually suggestive and violent content, each with a one-sentence definition, and the docs describe the use as content moderation. Other harm categories are not listed. **[Documented]**
Detail:
• `IMAGE_TYPE/CONTEXT/SEXUALLY_EXPLICIT`: "A finding of this type indicates that an image contains adult content of a sexual nature." {{D:infotypes-reference}} **[Documented]**
• Same entry: "Adult content might include elements such as nudity, specific contours or shapes of reproductive body parts, sexual activities, or pornographic images including photo-realistic or cartoon in nature." {{D:infotypes-reference}} **[Documented]**
• `IMAGE_TYPE/CONTEXT/SEXUALLY_SUGGESTIVE`: "A finding of this type indicates that an image contains racy or sexually suggestive content. Racy content might include elements like revealing clothing, lewd or provocative poses or themes, or other sexually suggestive material." {{D:infotypes-reference}} **[Documented]**
• `IMAGE_TYPE/CONTEXT/VIOLENCE`: "A finding of this type indicates that an image contains violent or gory content either real or fictionalized." {{D:infotypes-reference}} **[Documented]**
• Same entry: "Violent content might include imagery related to death, serious injury, or harm to an individual or group of individuals or animals." {{D:infotypes-reference}} **[Documented]**
• All three carry the default sensitivity score SENSITIVITY_HIGH and the category CONTEXTUAL_INFORMATION in the reference tables {{D:infotypes-reference}} **[Documented]**
• The reference lists only these three image context detectors; categories such as hate symbols, self-harm, weapons or child safety are not named (checked the infoType reference, image concepts page and release notes) **[Not disclosed]**
• Generated images are a stated weak point: "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." {{D:concepts-image-redaction}} **[Documented]**
• "their effectiveness in detecting all types of policy-violating content in AI-generated images can vary" {{D:concepts-image-redaction}} **[Documented]**
• On AI-generated images the page says these might not be detected: nuanced or subtle content; context-dependent scenarios such as private settings; non-graphic depictions of sensitive themes {{D:concepts-image-redaction}} **[Documented]**
• "Don't rely solely on these classifiers for safety assurances in high-risk generative AI applications." {{D:concepts-image-redaction}} **[Documented]**
• "We recommend that you conduct thorough testing for your specific generative AI use cases to ensure that the results meet your safety requirements." {{D:concepts-image-redaction}} **[Documented]**
• The text-side analogues are document-category infoTypes of the SD1 column, for example `DOCUMENT_TYPE/CONTEXT/SEXUAL` ("Content contains sex-related topics."), `DOCUMENT_TYPE/CONTEXT/OFFENSIVE` ("Content contains offensive topics.") and `DOCUMENT_TYPE/CONTEXT/OBSCENE` ("Content contains obscene topics."); they classify text, not pixels {{D:infotypes-reference}} **[Documented]**
• The reference introduces document classification as "To help with document risk assessment and policy enforcement, Sensitive Data Protection can classify documents into enterprise, sensitive, and regulated content categories." {{D:infotypes-reference}} **[Documented]**
• Prompt injection, jailbreaks, toxicity in text and topic control are not part of this feature (checked the image concepts, inspect, redact and infoType reference pages; none mentions them) **[Not disclosed]**
• Languages: the classifier works on pixels, not on extracted text: "can analyze image pixels and features directly, rather than text extracted from images." {{D:supported-file-types}} **[Documented]**
### R3
Summary: **Whole images as bytes, with no input or output flag.** The same call can score a user upload or an image a model generated. The whole image is judged, multiframe images use the first frame only, and results are not stored in Google Cloud. **[Inferred]**
Detail:
• "When performing image safety classification, Sensitive Data Protection analyzes the entire image." {{D:concepts-image-redaction}} **[Documented]**
• The input is image bytes in the same `ByteContentItem` used by the SD5 column: "Container for bytes to inspect or redact." ({{L:T|Container for bytes to inspect or redact.}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The image methods have no direction, role or prompt-type field ({{D:REST projects.image.redact}}), so uploads, model-generated images, retrieved images and tool outputs go through the same call **[Inferred]**
• The docs name AI-generated images as an expected input, which is the response-side case: "If you use image context infoTypes on AI-generated images, the following might not be detected:" {{D:concepts-image-redaction}} **[Documented]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." {{D:REST projects.image.redact}} **[Documented]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• The classification mode "can analyze image pixels and features directly, rather than text extracted from images." {{D:supported-file-types}} **[Documented]**
• No system prompt or conversation context is read; the image and the configuration are the only inputs **[Inferred]**
### R4
Summary: **A classifier over the whole image, with unnamed models.** Image context detectors run an image content classification mode that assigns one theme or category. The models are described only as trained mainly on real-world images. Rules can use the findings from June 2026. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." {{D:supported-file-types}} **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any image context infoType detectors that are specified in the inspection or redaction configuration." {{D:supported-file-types}} **[Documented]**
• "The models that Sensitive Data Protection uses for image safety classification are primarily trained and evaluated on real-world images." {{D:concepts-image-redaction}} **[Documented]**
• Model names, architecture, training data and evaluation sets for the image safety classifiers (checked the image concepts, supported-file-types, infoType reference and release-note pages) **[Not disclosed]**
• Image safety findings can act as context in rules: the 2026-06-23 release note says they are "supported in ExcludeByImageFindings and AdjustByImageFindings detection rules." {{D:release-notes}} **[Documented]**
• "Sensitive Data Protection excludes a target infoType finding if the bounding box of a context infoType has the specified relationship with the target infoType finding." and "you must set the matchingType field to MATCHING_TYPE_RULE_SPECIFIC." {{D:creating-custom-infotypes-rules}} **[Documented]**
• The rules page shows no example that uses an image context infoType (checked the page for IMAGE_TYPE) **[Not disclosed]**
• Such a rule "is silently ignored if the content being inspected is not an image" ({{L:T|This rule is silently ignored if the content being inspected is}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access is the DLP API over REST (`POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and `content:inspect`), global or regional endpoint, or the client libraries {{D:REST projects.image.redact}} and {{D:api-endpoints}} **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 ({{L:G|__version__ = "3.40.0"}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column {{O:Gemini Enterprise protect-sensitive-data page}} **[Documented]**
### R5
Summary: **A rated finding for the image, or a fully blanked image.** The docs say classification produces a label, and give a likelihood bucket per finding rather than a number. They show no worked example of an image safety response. **[Documented]**
Detail:
• "This scanning mode analyzes the entire image to assign a single theme or category and produces a label or classification." {{D:supported-file-types}} **[Documented]**
• The scanning-modes table lists ImageLocation as the additional location detail for image content classification, as it does for OCR and object detection; what box a whole-image finding carries is not shown {{D:supported-file-types}} **[Documented]**
• A finding carries `infoType`, `likelihood`, `location` and, when requested, `quote` {{D:REST InspectResult}} **[Documented]**
• Each category is its own infoType, so one image can in principle produce one finding per category **[Inferred]**
• Redaction by image safety replaces the whole image: "this feature redacts the entire image." and the response holds `redactedImage` of the same type as the original {{D:concepts-image-redaction}} and {{D:REST RedactImageResponse}} **[Documented]**
• With `includeFindings` set, the redact response also holds `inspectResult`: "The findings. Populated when includeFindings in the request is true." {{D:REST RedactImageResponse}} **[Documented]**
• No allow or block field exists in the redact response ({{L:T|class RedactImageResponse(proto.Message):}}), so the caller maps findings to a decision **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Threshold: findings below `minLikelihood` are dropped, with POSSIBLE as the default; five levels, no numeric score {{D:likelihood}} **[Documented]**
• A recommended minimum likelihood for image safety, or a calibrated threshold per category (checked the likelihood, image concepts and infoType reference pages) **[Not disclosed]**
• Worked request or response samples for `IMAGE_TYPE/CONTEXT/*` (checked the inspect guide, redact guide, image concepts page, supported-file-types page and REST references; the infoType names appear only in the reference and release notes) **[Not disclosed]**
• Precision, recall, false-positive rate or latency for image safety classification, on real-world or AI-generated images **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location; categories must be named.** Image context detectors have to be requested in the configuration, and image scanning runs only in listed locations, including Singapore. Format and size rules are those of other image calls, whose format statements conflict. **[Inferred]**
Detail:
• "To perform image safety classification, specify image context infoTypes in your inspection or redaction configuration." {{D:concepts-image-redaction}} **[Documented]**
• Whether a request with no infoTypes also runs image context detectors: the redaction guide says only that "Default infoTypes don't include objects in images." and is silent on image context infoTypes (checked the redact, inspect and REST pages) **[Not disclosed]**
• Availability: "Availability indicates the regions or multi-regions where the infoType is supported." {{D:infotypes-reference}} **[Documented]**
• For the three image context infoTypes the availability column lists asia, asia-southeast1, europe, europe-north1, global, us, us-central1, us-east4 and us-west1 {{D:infotypes-reference}} **[Documented]**
• "Image inspection and redaction are supported only in the following locations:" the same nine locations {{D:locations}} **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22, and the locations page lists a regional endpoint for it {{D:release-notes}} and {{D:locations}} **[Documented]**
• Input handling uses the same methods and body as the SD5 column (image bytes, 4 MB for `image.redact`, 0.5 MB for other content requests, format statements that conflict), so those rules and that conflict carry over **[Inferred]**
• "When you redact data from images, you can't include limits in your inspection configuration." {{D:redacting-sensitive-data-images}} **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User; API keys are accepted for `projects.image.*` methods {{D:redacting-sensitive-data-images}} and {{D:auth}} **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection only; the pricing page lists no separate price for image safety classification {{O:Sensitive Data Protection pricing page}} **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint {{D:limits}} **[Documented]**
• Launch stage of the three detectors (general availability or Preview) is not stated beyond the release note that says they are "available" (checked the infoType reference and release notes) **[Not disclosed]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, the Python client, and an image-scanning location such as Singapore. Build a lawful, approved image set labelled by category, real and AI-generated, send each image asking for the three detectors, and compare findings with human labels at several thresholds. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; calls to `inspect_content` with the three `IMAGE_TYPE/CONTEXT/*` infoTypes in `asia-southeast1` or global **[Inferred]**
• Labelled set: images that a reviewer marks as sexually explicit, sexually suggestive, violent or gory, or none of these; with ground truth at image level, since the classifier assigns a whole-image category **[Inferred]**
• Borderline and look-alike images: medical and anatomical drawings, classical art, swimwear and sport, news and war photography, film stills, cartoons and game screenshots, to measure false positives **[Inferred]**
• Real versus AI-generated images in equal numbers, because the docs warn that results on generated images can differ **[Inferred]**
• Threshold sweep over `minLikelihood` (POSSIBLE, LIKELY, VERY_LIKELY) per category, since no recommended level is published **[Inferred]**
• Redaction check: send images through `redact_image` with each detector and confirm that the entire image is covered, and that unflagged images come back unchanged **[Inferred]**
• Image variants: cropped, resized, compressed, watermarked, rotated, and text-only images with offensive words, to see what the classifier reacts to **[Inferred]**
• Handling: use only lawful sample images approved for testing and store them with access controls; the request data is not stored but is processed by Google, and bytes inspected count towards the free first gibibyte per month **[Inferred]**
• No emulator or offline mode was found, so tests need network access to Google Cloud (checked the libraries and image pages and the client README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Accuracy and thresholds per category, what a whole-image finding looks like, how generated images and local norms affect results, and whether text in an image or a missing infoType list changes the outcome.
Detail:
• Accuracy, precision and recall of each category on real and AI-generated images (checked the image concepts, infoType reference and release-note pages; none published)
• How strictly "racy" and "sexually suggestive" are defined, and whether the labels reflect Singapore community norms (the reference gives a one-sentence definition only)
• What a whole-image finding returns for location: a box covering the image, no box, or another value (needs testing)
• A recommended `minLikelihood` for moderation use, and whether several categories can fire on one image (needs testing)
• Whether text printed in an image (offensive words, captions) affects the classifier (the docs say it uses pixels and features rather than extracted text; needs testing)
• Whether a request with no infoTypes runs the image context detectors (needs testing)
• Launch stage of the three detectors and whether more categories are planned (checked the infoType reference and release notes)
• Behaviour in a region without image scanning for a content call (the locations page describes files, not content calls)
• Latency and throughput of image classification (checked limits, pricing and SLA pages; none published)
• How the image format conflict recorded in the SD5 column applies here (needs testing)
• Whether findings on very small, very large or multi-subject images are reliable, including minimum image size (not stated)
• How content-policy rules over image safety, documented only in Gemini Enterprise docs, differ from calling the image methods directly (cross-reference; content policies are inventory-only)
• Customer data terms for images sent to the API (not read)
### R9
Summary: Sensitive Data Protection docs (image concepts, supported file types, infoType reference, redact and inspect guides, rules, locations, REST references, limits), pricing page, release notes, and the Python client source at tag 3.40.0.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/auth
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
