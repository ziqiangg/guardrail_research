from gen_common import *
HF = ["Topic","Detail","Applies to","Source URL"]
ROWS_F = [
["Global endpoint and global region",
 "All Sensitive Data Protection features are accessible globally without specifying a region [Documented] (DOCS locations). A request to the global endpoint with no location is processed in the global region [Documented] (DOCS api-endpoints). Resources created by a request that names the global region are stored under it [Documented] (DOCS specifying-location)",
 "All methods",urls("locations","endpoints","specloc")],
["Regional endpoints",
 "43 regions are listed, among them asia-southeast1 (Singapore) with regional endpoint support Yes [Inferred] (my count of region rows on the locations page; asia-southeast1 row read directly [Documented] (DOCS locations)). The REST reference page lists regional endpoints for 42 of them and omits asia-southeast3 (Bangkok), which the locations page lists [Documented] (DOCS locations, REST root). The two pages differ and are not reconciled",
 "Regional endpoint use",urls("locations","restroot")],
["Multi-regions",
 "asia (regional endpoint support No), europe (Yes, multi-regional endpoint eu; data is not processed in europe-west2 or europe-west6), in (India, Yes) and us (Yes) [Documented] (DOCS locations)",
 "Multi-region processing",urls("locations")],
["Image-scanning locations",
 "Image inspection and redaction are supported only in global, asia, asia-southeast1, europe, europe-north1, us, us-central1, us-east4 and us-west1 [Documented] (DOCS locations). In an unsupported region, images and documents containing images are scanned as binary files [Documented] (DOCS locations). The release notes record asia-southeast1, us-east4 and us-west1 being added on 2026-06-22, and europe-north1 and us-central1 on 2026-08-20 [Documented] (DOCS release-notes)",
 "image.redact; content.inspect on images",urls("locations","relnotes")],
["InfoType availability by location",
 "Of 261 infoTypes, 240 are ANY_LOCATION and 21 are REGIONAL [Inferred] (my count of the Availability column). The 8 DOCUMENT_TYPE/CONTEXT infoTypes list europe, global and us; DOCUMENT_TYPE/FINANCE/INVOICE and DOCUMENT_TYPE/MEDICAL/RECORD list asia, europe, global and us; image object and image context infoTypes list asia, asia-southeast1, europe, europe-north1, global, us, us-central1, us-east4 and us-west1 [Documented] (DOCS infotypes-reference, Availability column). The reference calls the document and invoice types limited-availability and warns of scanning issues in unsupported regions [Documented] (DOCS infotypes-reference)",
 "Built-in infoTypes",urls("infotypes")],
["Content policy location",
 "A content policy is created in a region or multi-region the administrator selects, and its resource path is projects.locations.contentPolicies [Documented] (DOCS manage-content-policies, REST contentPolicies). Gemini Enterprise supports the global, EU and US multi-regions for content policies [Documented] (Gemini Enterprise docs, not SDP docs). Where evaluation of content is processed [Not disclosed] (checked the content-policy, manage and Gemini Enterprise pages)",
 "Content policies",urls("managecp","rcp","gemini")],
["Data handling",
 "Request data is encrypted in transit and is not stored for content methods [Documented] (DOCS concepts-method-types). The results of content methods and image.redact are not stored in Google Cloud [Documented] (DOCS overview). Regional endpoints keep data at rest, in use and in transit in the named location, excluding Service Data [Documented] (DOCS api-endpoints). Use of customer content for product improvement and the data processing terms [To be verified] (not covered by the product docs read; terms pages were not read)",
 "Content methods",urls("methods","overview","endpoints")],
]
assert len(ROWS_F)==7
