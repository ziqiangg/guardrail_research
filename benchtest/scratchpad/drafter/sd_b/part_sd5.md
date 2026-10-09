## Column SD5: Sensitive Data Protection: Sensitive-data detection and redaction in images
### R1
Summary: **Finds and blanks sensitive text and objects in images.** The service reads text in an image with OCR and also detects objects such as passports, photo ID cards, faces and licence plates. It returns bounding boxes, or the image with opaque rectangles over the matches. **[Documented]**
Detail:
• "Using infoType detectors, Sensitive Data Protection inspects a base64-encoded image and detects sensitive data within the image." {{D:concepts-image-redaction}} **[Documented]**
• "Inspection and redaction are two distinct operations:" and the page defines both, so one image can be inspected without being changed {{D:concepts-image-redaction}} **[Documented]**
• Inspection "returns the detected InfoTypes, along with one or more set of pixel coordinates and dimensions." {{D:concepts-image-redaction}} **[Documented]**
• Redaction "returns the redacted base64-encoded image in the same image format as the original image." {{D:concepts-image-redaction}} **[Documented]**
• "In the returned image, the detected sensitive data elements are obscured by an opaque rectangle." {{D:redacting-sensitive-data-images}} **[Documented]**
• "By default, Sensitive Data Protection uses black rectangles to obscure the redacted content, but you can specify a color for each infoType in your image redaction configuration." {{D:redacting-sensitive-data-images}} **[Documented]**
• "Sensitive Data Protection uses optical character recognition (OCR) to detect text within images." {{D:concepts-image-redaction}} **[Documented]**
• "Sensitive Data Protection can classify and redact objects in images." {{D:concepts-image-redaction}} **[Documented]**
• An option redacts every piece of text found: "Sensitive Data Protection also contains an option to redact all detected text in an image." {{D:redacting-sensitive-data-images}} **[Documented]**
• The release notes of 2025-07-04 add object redaction: "Sensitive Data Protection can detect and redact the following object infoTypes in images:" barcode, licence plate, person and whiteboard {{D:release-notes}} **[Documented]**
• Later object detectors: passport and photo ID card (2025-11-03), face in Preview (2025-12-15) and signature (2026-06-08) {{D:release-notes}} **[Documented]**
• The Python client at v3.40.0 exposes `redact_image` and `inspect_content` ({{L:C|def redact_image(}} and {{L:C|def inspect_content(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Image safety classification uses the same two methods and is covered by the SD6 column **[Inferred]**
### R2
Summary: **Sensitive text and ID-type objects in pictures.** Text infoTypes run on text read from the image, and object detectors cover faces, passports, photo ID cards, signatures, licence plates, barcodes and whiteboards. **[Documented]**
Detail:
• "To detect text in images, specify any text-based infoType, such as PERSON_NAME and CREDIT_CARD_NUMBER in your inspection or redaction configuration." {{D:concepts-image-redaction}} **[Documented]**
• "all other infoType detectors are text-based; when analyzing images, they first extract text from images and then analyze the text." {{D:infotypes-reference}} **[Documented]**
• The reference lists eight object infoTypes that "analyze image pixels and features directly" and describes them {{D:infotypes-reference}} **[Documented]**
  – `OBJECT_TYPE/PERSON/PASSPORT`: "Image of a person's passport card or passport booklet, which is often used for identification and travel purposes. Note that images of the inner visa-stamped pages might not be identified."
  – `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`: "Image of a person's photo ID card, which can be government-issued (for example, driver's license) or non-government-issued (for example, school ID or employee ID)."
  – `OBJECT_TYPE/PERSON/SIGNATURE`: "Image of a signature which is done by a human on some document for their identity verification."
  – `OBJECT_TYPE/PERSON/FACE`: "Image of a person's face." and `OBJECT_TYPE/PERSON`: "Image of a human-like figure, which can include a full body, a face, or other body parts."
  – `OBJECT_TYPE/LICENSE_PLATE`: "Image of a license plate, which is a government-issued vehicle identifier."
  – `OBJECT_TYPE/BARCODE`: "Image of a 1D or 2D barcode, which is a machine-readable image that represents a piece of data." and `OBJECT_TYPE/WHITEBOARD`: "Image of a whiteboard."
• The face detector is not generally available: "This infoType detector is in Preview." {{D:infotypes-reference}} **[Documented]**
• "Default infoTypes don't include objects in images." so object detectors must be requested by name {{D:redacting-sensitive-data-images}} **[Documented]**
• Documented use case: "Sanitize customer support uploads: Automatically redact account numbers and personal contact details in user-submitted screenshots before tickets are routed to support agents." {{D:concepts-image-redaction}} **[Documented]**
• Documented use case: "Obfuscate sensitive data in scanned documents: Mask driver's licenses, national identity cards, and credit card numbers from uploaded PDF or image attachments before processing in downstream workflows." {{D:concepts-image-redaction}} **[Documented]**
• The redaction walkthrough uses an image with a handwritten Social Security number and notes "Sensitive Data Protection also redacted the year." (a match the author did not ask for) {{D:redacting-sensitive-data-images}} **[Documented]**
• Default sensitivity scores of the object infoTypes {{D:infotypes-reference}} **[Documented]**
  – SENSITIVITY_HIGH: `OBJECT_TYPE/PERSON/FACE`, `OBJECT_TYPE/PERSON/PASSPORT`, `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`, `OBJECT_TYPE/PERSON/SIGNATURE`
  – SENSITIVITY_MODERATE: `OBJECT_TYPE/PERSON`, `OBJECT_TYPE/LICENSE_PLATE`
  – SENSITIVITY_LOW: `OBJECT_TYPE/BARCODE`, `OBJECT_TYPE/WHITEBOARD`
• Singapore: the text infoTypes `SINGAPORE_NATIONAL_REGISTRATION_ID_NUMBER` and `SINGAPORE_PASSPORT` are available in all locations {{D:infotypes-reference}} **[Documented]**
• A Singapore NRIC printed in an image is therefore reachable by OCR followed by the text detector; this needs a test because no Singapore image example is given **[Inferred]**
• The object detectors for passports and photo ID cards are global; the docs do not say whether they recognise Singapore passports or NRIC cards (checked the infoType reference, release notes and image pages) **[Not disclosed]**
• OCR language and script coverage, handwriting accuracy and rotated or low-resolution text: not stated (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages) **[Not disclosed]**
• "Sensitive Data Protection helps you discover, classify, and de-identify sensitive data inside and outside Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• Prompt injection or jailbreak text inside an image is not described as something the service looks for (checked the same image pages); OCR text is matched only against the infoTypes requested **[Not disclosed]**
### R3
Summary: **Image bytes only, with no input or output flag.** The caller sends one image per call, whether it came from a prompt, a response, a retrieved file or a tool result. Results are not stored in Google Cloud. Only the first frame of a multiframe image is processed. **[Inferred]**
Detail:
• "To inspect an image for sensitive data, you submit a base64-encoded image to the content.inspect method." {{D:inspecting-images}} **[Documented]**
• "To redact sensitive data from an image, submit the image to the DLP API's image.redact method." {{D:redacting-sensitive-data-images}} **[Documented]**
• The client type is described as "Container for bytes to inspect or redact." and `ContentItem` carries it as `byte_item` beside `value` and `table` ({{L:T|Container for bytes to inspect or redact.}} and {{L:T|byte_item (google.cloud.dlp_v2.types.ByteContentItem):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The `projects.image.redact` request body has `locationId`, `inspectConfig`, `imageRedactionConfigs[]`, `includeFindings`, `byteItem`, `inspectTemplate` and `deidentifyTemplate` {{D:REST projects.image.redact}} **[Documented]**
• None of these fields marks direction, role or prompt type, so the same call is used for images from prompts, responses, retrieved files and tool inputs or outputs, with the caller supplying the bytes **[Inferred]**
• "Only the first frame of each multiframe image is redacted. Metadata and other frames are omitted in the response." {{D:REST projects.image.redact}} **[Documented]**
• For inspection the client enum says "Only the first frame of each multiframe image is inspected. Metadata" ({{L:T|Only the first frame of each multiframe image is inspected. Metadata}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "The results of content methods and the image.redact method aren't stored in Google Cloud." {{D:sensitive-data-protection-overview}} **[Documented]**
• "Content methods are synchronous, stateless methods." and "Request data is encrypted in transit and is not stored." {{D:concepts-method-types}} **[Documented]**
• Documents with embedded images are a different route: the inspect guide says other formats such as PDF, DOCX, XLSX and PPTX "may generate mixed findings" and the redact guide says "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." {{D:inspecting-images}} and {{D:redacting-sensitive-data-images}} **[Documented]**
• Image scanning runs only in listed locations (see R6); in other regions images and documents with images are scanned as binary files {{D:locations}} **[Documented]**
• No system prompt or conversation context is read; the service sees the image and the configuration only **[Inferred]**
### R4
Summary: **OCR for text, direct pixel analysis for objects.** Text infoTypes run on text extracted from the image; object detectors look at pixels and return a box. Both go through the DLP API over REST or client libraries, on a global or regional endpoint. **[Documented]**
Detail:
• "In regions that support image scanning, Sensitive Data Protection uses OCR to find text-based infoTypes in images." {{D:supported-file-types}} **[Documented]**
• Object scanning: "This scanning mode focuses on locating a specific item within the image and produces a bounding box around it." {{D:supported-file-types}} **[Documented]**
• "Sensitive Data Protection uses this scanning mode for any object infoTypes that are specified in the inspection or redaction configuration." {{D:supported-file-types}} **[Documented]**
• Names, versions, architecture and training data of the OCR and object-detection models (checked the image concepts, inspect, redact, supported-file-types and infoType reference pages and the release notes) **[Not disclosed]**
• "Image redaction is similar to image inspection, with one additional step." {{D:concepts-image-redaction}} **[Documented]**
• Redaction targets are set per entry in `imageRedactionConfigs[]`: an `infoType`, or `redactAllText`, plus an optional `redactionColor` ({{L:T|redact_all_text: bool = proto.Field(}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• With no infoType listed and redact-all-text false, the docstring says the API "will redact all text that it matches against all info_types" found ({{L:T|will redact all text that it matches against all info_types}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• "Note: If you include infoTypes in the imageRedactionConfigs object, Sensitive Data Protection ignores them." when `redactAllText` is set {{D:redacting-sensitive-data-images}} **[Documented]**
• Colours are RGB values from 0 to 1: "Each value is between 0 and 1, inclusive." {{D:redacting-sensitive-data-images}} **[Documented]**
• Templates can drive redaction: `deidentifyTemplate` "The request fails if the type of the template's deidentifyConfig is not imageTransformations." {{D:REST projects.image.redact}} **[Documented]**
• An image transformation holds a colour and one of selected infoTypes, all infoTypes or all text: `selectedInfoTypes`, `allInfoTypes`, `allText` {{D:REST organizations.deidentifyTemplates}} **[Documented]**
• Image-based rules refine results by position: "Image-based exclusion rules, which let you refine your image inspection results by excluding findings based on their spatial relationships with other findings." (general availability 2026-02-23) {{D:release-notes}} **[Documented]**
• Such a rule "is silently ignored if the content being inspected is not an image" (docstring) ({{L:T|This rule is silently ignored if the content being inspected is}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Access: `POST https://dlp.googleapis.com/v2/{parent=projects/*}/image:redact` and the location form `{parent=projects/*/locations/*}/image:redact`; regional endpoint form `dlp.REGION.rep.googleapis.com` {{D:REST projects.locations.image.redact}} and {{D:api-endpoints}} **[Documented]**
• Regional endpoint support for `asia-southeast1` (Singapore) is listed as Yes {{D:locations}} **[Documented]**
• API keys are accepted: "The image.redact method also supports API keys." {{D:redacting-sensitive-data-images}} **[Documented]**
• Python client: package `google-cloud-dlp` 3.40.0 ({{L:G|__version__ = "3.40.0"}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Cross-reference, Model Armor docs, not SDP docs: Model Armor image screening (see the Model Armor column `Model Armor: Image screening with OCR and visual scanning`) says "Visual scanning: Screens the visual content within images only using the advanced Sensitive Data Protection filter." {{O:Model Armor overview page}} **[Documented]**
• Cross-reference, Gemini Enterprise docs, not SDP docs: content policies "can inspect various content types, including textual content (with OCR for images), image object detection, image safety"; content policies are an inventory-only item, not part of this column {{O:Gemini Enterprise protect-sensitive-data page}} **[Documented]**
### R5
Summary: **Bounding boxes or a redacted image, with a likelihood.** Inspection returns each detected infoType with a likelihood bucket and pixel boxes. Redaction returns the image with rectangles drawn and, if asked, the findings. There is no allow or block verdict. **[Documented]**
Detail:
• "The output of an inspection operation includes the detected infoTypes, the likelihood of the match, and pixel coordinates and length values that indicate the areas within which Sensitive Data Protection found the sensitive data." {{D:inspecting-images}} **[Documented]**
• A finding in the guide's sample holds `infoType` (with `sensitivityScore`), `likelihood`, `location.contentLocations[].imageLocation.boundingBoxes[]` (`top`, `left`, `width`, `height`), `createTime` and `findingId` {{D:inspecting-images}} **[Documented]**
• "Be aware that Sensitive Data Protection often uses multiple boxes to indicate where a single instance of sensitive data is in the image." {{D:inspecting-images}} **[Documented]**
• For object infoTypes "the inspection result doesn't include a quote for the detected object." {{D:inspecting-images}} **[Documented]**
• Bounding-box origin, statement 1 (REST reference and client): "Top coordinate of the bounding box. (0,0) is upper left." {{D:REST InspectResult}} **[Documented]**
• Bounding-box origin, statement 2: "The coordinates at the bottom left corner of an image are (0,0)." {{D:inspecting-images}} **[Documented]**
• Bounding-box origin, statement 3: boxes are described by "the bottom-left corner and the dimensions of bounding boxes, respectively." {{D:concepts-image-redaction}} **[Documented]**
• The client agrees with statement 1: {{L:T|Top coordinate of the bounding box. (0,0) is}} **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• No match, inspection: "it returns an empty, successful HTTP 200 response." {{D:concepts-image-redaction}} **[Documented]**
• No match, redaction: "it returns the base64-encoded image unchanged." {{D:concepts-image-redaction}} **[Documented]**
• Redaction response `redactedImage`: "The redacted image. The type will be the same as the original image." {{D:REST RedactImageResponse}} **[Documented]**
• Redaction response `extractedText`: "If an image was being inspected and the InspectConfig's includeQuote was set to true, then this field will include all text, if any, that was found in the image." {{D:REST RedactImageResponse}} **[Documented]**
• Redaction response `inspectResult`: "The findings. Populated when includeFindings in the request is true." {{D:REST RedactImageResponse}} **[Documented]**
• Setting `includeQuote` returns all recognised text to the caller, so the response itself holds the sensitive text that redaction was meant to hide **[Inferred]**
• Threshold: findings below `minLikelihood` are dropped and "returns only the findings with a likelihood of POSSIBLE and higher" when it is unset; five levels from VERY_UNLIKELY to VERY_LIKELY, no numeric score {{D:likelihood}} **[Documented]**
• The likelihood page describes each level (for example "Useful if you want a balance of precision and recall." for POSSIBLE) but gives no recommended level for images {{D:likelihood}} **[Not disclosed]**
• The redaction guide shows a request with `minLikelihood` set to LIKELY inside `inspectConfig` ("Code example with likelihood setting") {{D:redacting-sensitive-data-images}} **[Documented]**
• Redaction responses carry no allow or block field, only the image, optional text and optional findings ({{L:T|class RedactImageResponse(proto.Message):}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• Published precision, recall, false-positive rate, OCR error rate or per-object detection accuracy (checked the image concepts, inspect, redact, likelihood and infoType reference pages and the release notes; the likelihood page only defines the terms) **[Not disclosed]**
### R6
Summary: **Image bytes in a supported location, up to 4 MB; formats disagree.** The docs name PNG, JPEG and BMP most often, while SVG, GIF and TIFF appear on only some pages. Redaction requests are capped at 4 MB and other content requests at 0.5 MB. **[Documented]**
Detail:
• Format conflict, statement 1 (REST reference for `byteItem`): "The content must be PNG, JPEG, SVG or BMP." {{D:REST projects.image.redact}} **[Documented]**
• Format conflict, statement 2 (redaction guide): "Sensitive Data Protection can redact sensitive data from many image types, including JPEG, BMP, and PNG." and "Content redaction is not supported for SVG, PDF, XLSX, PPTX, or DOCX files." {{D:redacting-sensitive-data-images}} **[Documented]**
• Format conflict, statement 3 (supported file types, inspection and de-identification table, image row): extensions "bmp, gif, jpe, jpeg, jpg, png", scanning modes OCR, image content detection and image content classification, transformation support Redaction {{D:supported-file-types}} **[Documented]**
• Format conflict, statement 4 (inspect guide): "Sensitive Data Protection can inspect many image types for sensitive data, including JPEG, BMP, PNG, and SVG." {{D:inspecting-images}} **[Documented]**
• Format conflict, statement 5 (method-types page): "Redact sensitive data from uploaded images: Obfuscate sensitive text in image formats (such as JPEG, PNG, or TIFF)" {{D:concepts-method-types}} **[Documented]**
• Format conflict, statement 6 (client enum, surface only): `IMAGE` ("Any image type."), `IMAGE_JPEG`, `IMAGE_BMP`, `IMAGE_PNG` and `IMAGE_SVG`, and no GIF value ({{L:T|IMAGE_SVG = 4}}) **[Documented: repo googleapis/google-cloud-python@google-cloud-dlp-v3.40.0]**
• The supported-file-types page also has a discovery table whose Images cluster lists "bmp, gif, heic, ico, jpe, jpeg, jpg, pm, png, svg, tiff, webp" and says "Supported images (bmp, gif, jpe, jpeg, jpg, and png) smaller than 4 MiB are scanned using OCR"; this table is for discovery, not content methods {{D:supported-file-types}} **[Documented]**
• PNG, JPEG and BMP are the formats named by the REST reference, the redaction guide, the inspect guide and the client enum; SVG, GIF and TIFF are disputed, so tests should use PNG, JPEG and BMP first **[Inferred]**
• Size: "Maximum size of each projects.image.redact request | 4 MB" and "Maximum size of each request, except projects.image.redact | 0.5 MB" {{D:limits}} **[Documented]**
• The 0.5 MB limit therefore appears to apply to images sent to `content.inspect`, so larger images need `image.redact` or a storage inspection job **[Inferred]**
• "If you need to inspect files that are larger than these limits, store those files on Cloud Storage and run an inspection job." {{D:limits}} **[Documented]**
• Locations: "Image inspection and redaction are supported only in the following locations:" global, asia, asia-southeast1, europe, europe-north1, us, us-central1, us-east4, us-west1 {{D:locations}} **[Documented]**
• "If you attempt to inspect images or documents that contain images in a region that doesn't support image scanning, Sensitive Data Protection scans those files as binary files." {{D:locations}} **[Documented]**
• Singapore: image scanning was added for `asia-southeast1` on 2026-06-22 {{D:release-notes}} **[Documented]**
• "When you redact data from images, you can't include limits in your inspection configuration." and "If you set the limits field in your request, Sensitive Data Protection generates an error." {{D:redacting-sensitive-data-images}} **[Documented]**
• Default detectors, statement 1: "Unless you specify specific information types (infoTypes) to search for, Sensitive Data Protection searches for the most common infoTypes." {{D:redacting-sensitive-data-images}} **[Documented]**
• Default detectors, statement 2: "When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time." {{D:REST projects.image.redact}} **[Documented]**
• Advice from the infoType concepts page: "Always specify infoType detectors explicitly. Don't use an empty infoTypes list." {{D:concepts-infotypes}} **[Documented]**
• Encoding and parameters: REST callers base64-encode the image; client libraries take bytes; optional `includeFindings`, `inspectConfig`, `imageRedactionConfigs`, `inspectTemplate` and `deidentifyTemplate` {{D:redacting-sensitive-data-images}} **[Documented]**
• Auth and roles: a role with `serviceusage.services.use` such as DLP User (`roles/dlp.user`); an API key also works for `image.redact` {{D:redacting-sensitive-data-images}} **[Documented]**
• "You can use a Google Cloud console API key to authenticate to the DLP API for some methods, including all projects.content.* and projects.image.* methods." {{D:auth}} **[Documented]**
• Rate quotas: 10,000 requests per minute in total, 600 per minute per region for the global endpoint with a location, 100 per minute per region for a regional endpoint; values "are subject to change" {{D:limits}} **[Documented]**
• Billing: `projects.image.redact` is billed for content inspection and not for content transformation; the first 1 gibibyte per month is free, minimum 1 KB per request {{O:Sensitive Data Protection pricing page}} **[Documented]**
• The SLA covers only content.inspect and content.deidentify requests, so `image.redact` has no published uptime objective {{O:Sensitive Data Protection SLA page}} **[Inferred]**
### R7
Summary: **Minimum setup:** a Google Cloud project with billing and the DLP API enabled, the DLP User role, the Python client, and a regional endpoint such as Singapore. Prepare synthetic images with known text and objects and hand-drawn box coordinates, send each to inspect and redact, and score matches and boxes. **[Inferred]**
Detail:
• **Minimum setup:** a Google Cloud project with billing and the DLP API enabled; Application Default Credentials with DLP User; `pip install google-cloud-dlp`; calls to `inspect_content` and `redact_image` in a supported location such as `asia-southeast1` through `dlp.asia-southeast1.rep.googleapis.com` **[Inferred]**
• Labelled set: synthetic images with the text type and pixel box marked for each item (names, emails, phone numbers, synthetic NRIC-style numbers, card numbers) and the object type and box marked for each passport, photo ID card, face, signature, licence plate, barcode and whiteboard **[Inferred]**
• Conditions to vary: screenshots, scans, photographs, rotated and skewed text, low resolution, small fonts, handwriting, non-English text, and AI-generated images **[Inferred]**
• Negative images with no sensitive content, and look-alikes (play money, sample ID cards, fake plates), to measure false positives **[Inferred]**
• Score boxes by overlap with the ground-truth box, because the docs say several boxes can describe one instance **[Inferred]**
• Formats: PNG, JPEG and BMP first, then SVG, GIF and TIFF, and an image just above and below 0.5 MB and 4 MB, to settle the format and size conflicts **[Inferred]**
• Compare `content.inspect` boxes with `image.redact` output, and check the coordinate origin of returned boxes (upper left or bottom left) **[Inferred]**
• Run the same images in a supported and an unsupported region to see what a non-supporting location returns **[Inferred]**
• Use only synthetic or consented images; the request data is not stored but is processed by Google, and bytes inspected count towards the free first gibibyte per month **[Inferred]**
• No emulator or offline mode was found, so every test needs network access to Google Cloud (checked the libraries, method-types and image pages and the client README) **[Not disclosed]**
### R8
Summary: **Key open questions.** Which image formats really work, how accurate OCR and object detection are, which box origin is correct, whether Singapore IDs and non-English text are read, and what a non-supporting region does.
Detail:
• Which image formats `content.inspect` and `image.redact` accept (PNG, JPEG, BMP, SVG, GIF, TIFF); six statements disagree (needs testing)
• Whether the 4 MB and 0.5 MB limits apply to the base64 text or to the decoded bytes (checked the limits page and the REST references; not stated)
• Which bounding-box origin the API returns, upper left or bottom left (needs testing)
• Accuracy, recall and false-positive rates for text in images and for each object detector (checked the image and infoType reference pages and the release notes; none published)
• OCR languages and scripts, handwriting, rotated text and minimum text size (checked the same pages; not stated)
• Whether the passport and photo ID card detectors recognise Singapore passports and NRIC cards, and whether FIN cards are covered (needs testing with synthetic images)
• What `content.inspect` or `image.redact` returns in a region without image scanning: an error, a binary scan, or silently empty results (the locations page describes files, not content calls)
• Whether redaction of overlapping or adjacent findings leaves partial text visible, and how box padding is chosen (needs testing)
• Latency and throughput for images of different sizes (checked the limits, pricing and SLA pages; none published)
• Launch stage of image redaction by object infoType: only the face detector is marked Preview (checked the infoType reference and release notes)
• Whether the redacted image strips metadata such as EXIF; the REST text says metadata is omitted for multiframe images only (needs testing)
• How a content policy or Model Armor image screening differs in practice from calling `image.redact` directly (cross-reference only; content policies are inventory-only)
• Customer data terms for images sent to the API (not read)
### R9
Summary: Sensitive Data Protection docs (image concepts, inspect and redact guides, supported file types, locations, infoType reference, REST references, limits), pricing and SLA pages, release notes, and the Python client source at tag 3.40.0.
Detail:
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction
• https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images
• https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/locations
• https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes
• https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types
• https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
• https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood
• https://docs.cloud.google.com/sensitive-data-protection/docs/auth
• https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints
• https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RedactImageResponse
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult
• https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates
• https://docs.cloud.google.com/sensitive-data-protection/limits
• https://cloud.google.com/sensitive-data-protection/pricing
• https://cloud.google.com/sensitive-data-protection/sla
• https://docs.cloud.google.com/model-armor/overview
• https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/types/dlp.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp_v2/services/dlp_service/client.py
• https://github.com/googleapis/google-cloud-python/blob/google-cloud-dlp-v3.40.0/packages/google-cloud-dlp/google/cloud/dlp/gapic_version.py
