# -*- coding: utf-8 -*-
from gen_a import *


def block_a():
    h = "| Module | What it is | Status | Surface | Data it handles | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|---|---|"]
    out.append(row([
     "Free-text anonymisation (FTA)",
     "Detects personal data in unstructured text and transforms it: \"It automatically detects and redacts/transforms sensitive information within unstructured text\" [Documented] (FTAI). It returns the transformed text or file and does not return a verdict or a risk score [Inferred] (premise: the FTAI and USE pages describe only an anonymised output and a findings table, no verdict field)",
     "Available [Inferred] (premise: listed as a current feature on the home page and the portal Features page, no beta or deprecation mark on the FTA pages). The portal overview page carries a PROOF OF VALUE badge [Documented] (PO, observed 2026-10-10). FTA first available in v1.2.0, 23 June 2023 [Documented] (REL)",
     "Web UI [Documented] (HOME: \"It is available through both a Web UI and API integration\"). API for batch processing of .csv, .docx and .pdf [Documented] (USE: \"Cloak's API supports batch file processing (.csv, .docx, .pdf), custom recognisers, and more\"). Request and response schemas of the API [Not disclosed] (APIG links the OpenAPI page, which redirects to a login page, HTTP 302 observed 2026-10-10)",
     "Pasted text, .csv, .pdf and .docx [Documented] (FTAI: \"The tool supports pasted text input as well as file uploads (.csv, .pdf, .docx)\"). Scanned PDFs and images are not processed [Documented] (FAQ)",
     CK1], "FTAI USE HOME PO REL APIG"))
    out.append(row([
     "Custom entities in FTA (fixed list, regex, LLM Beta)",
     "Lets the user add entity types the baseline does not cover: \"add any custom entity using inclusion lists, pattern-matching (regex), or privately-hosted LLMs\" [Documented] (HOME). Three approaches: a fixed list through the Inclusion feature, a regular expression (the Web UI calls it Pattern-matching based) and an LLM-based entity defined by a definition plus 3 to 5 examples [Documented] (FIXD, STRC, LLMI, FAQ)",
     "LLM-based entity: \"[Beta Feature] Currently, only 1 LLM-enabled custom entity is supported per dataset (up to 5,000 documents)\" [Documented] (LLMI). Regex entities: \"[FTA] Regex custom entities\" listed in v2.1.5, 3 July 2024 [Documented] (REL). Status mark on the fixed-list and regex pages [Not disclosed] (checked the FIXD and STRC pages: no beta or other status wording)",
     "Web UI, Custom entities tab of Anonymisation Settings [Documented] (CUST). API-only advanced settings (context words and per-pattern confidence scores): \"For full details on these API-level advanced settings, refer to the Cloak API Guide (sign-in required)\" [Documented] (STRC)",
     "Free text. LLM-based entities run on \"a language model within our own secure environment on the Government Commercial Cloud (GCC) on AWS\" [Documented] (LLMI). The language model name and size [Not disclosed] (checked LLMI, ADDE, PRMP, the sample pages, CRED and the portal pages)",
     CK2], "HOME FIXD STRC LLMI ADDE PRMP FAQ REL CUST"))
    out.append(row([
     "Secrets Manager and free-text decryption",
     "Secrets Manager: \"where you create, store, share, and audit the encryption keys and salts used in your anonymisation jobs\" [Documented] (SECR). Free-text decryption turns an encrypted value back into the original using a chosen secret [Documented] (FTDC: Step 1 input the encrypted value, Step 2 select your secret, Step 3 obtain the decrypted value)",
     "Decryption and secret sharing added in v2.1.0, 19 March 2024: \"[Decryption] Decrypt encrypted free-text or tabular data using secret keys\" [Documented] (REL)",
     "Web UI: \"The Web UI currently supports decrypting one value at a time\" [Documented] (FTDC). API: a helper script for looping through the rows of a CSV is linked [Documented] (FTDC); the linked page redirects to a login page (HTTP 302 observed 2026-10-10) so its content is [Not disclosed]",
     "Encrypted free-text values, secret keys, initial vector values and salts. \"Members of shared secrets will not be able to view or access the secret key and IV value, but will be able to use it to decrypt data\" [Documented] (SECR)",
     CK3], "SECR FTDC DECI REL"))
    out.append(row([
     "Tabular data anonymisation",
     "\"Tabular Data Anonymisation allows users to tag and transform data through transformation/anonymisation techniques and address re-identification risk through k-anonymity checks\" [Documented] (TABI). Includes data tagging, privacy-risk and utility analysis and tabular templates [Documented] (HOME, PF)",
     "Available [Inferred] (premise: first feature in the release history, v1.0.0 13 March 2023, and listed on the home page with no deprecation mark) [Documented] (REL)",
     "Web UI and API [Documented] (APIG: \"Cloak's API gives you the same anonymisation capabilities as the Web UI\"). Python package, tabular only [Documented] (HOME)",
     "\"tabular data containing up to 100 data fields (i.e. columns) in CSV or XLSX format, up to 2 GB per file\" [Documented] (TABU)",
     INV], "TABI TABU HOME PF APIG REL"))
    out.append(row([
     "Tabular decryption",
     "Decrypts encrypted columns of a tabular file with a shared secret; failed values are listed in a file named failed_cells.csv [Documented] (TABD)",
     "Added in v2.1.0, 19 March 2024 [Documented] (REL: \"[Decryption] Decrypt encrypted free-text or tabular data using secret keys\")",
     "Web UI [Documented] (TABD: Decryption in the sidebar, then Decrypt Tabular Data). API for tabular decryption [Not disclosed] (checked TABD, DECI, APIG, PF; only free-text decryption names an API helper script)",
     "Encrypted tabular dataset. \"Your download will be available for up to 24 hours from the job creation time\" [Documented] (TABD)",
     INV], "TABD REL DECI APIG PF"))
    out.append(row([
     "Templates (tabular and free text)",
     "Saved configurations to re-apply in later jobs. \"Templates are available for both tabular and free-text anonymisation\" [Documented] (TPL). A free-text template saves \"Entity types, anonymisation techniques, parameters, and score threshold\" [Documented] (TPL)",
     "Free-text templates added in v2.1.0, 19 March 2024: \"[FTA] Create and reuse project settings as templates\" [Documented] (REL)",
     "Web UI: Save as template in the toolbar and a template dropdown at Step 0 [Documented] (TPL). Free-text templates: \"Not shareable\" and \"Save new only\" (no versioning) [Documented] (TPL). Tabular templates can be shared and updated [Documented] (TPL)",
     "Settings only, not the data. The tabular template constraint is \"Dataset must have the same column names and access mode\" [Documented] (TPL)",
     CK1], "TPL REL"))
    out.append(row([
     "Mock Data Generation (MDG)",
     "Generates mock data. The Developer Portal Features page lists it as a Cloak feature: \"Generate mock data that mimics the structure and format of real datasets\" [Documented] (PF). The Mirage site describes it as a Mirage offering: \"Mirage offers mock and synthetic data generation\" [Documented] (MIR)",
     "Two official pages place MDG under different products and are not reconciled here: the portal lists it under Cloak [Documented] (PF) and the Mirage site lists it under Mirage [Documented] (MIR). The Cloak Guide has no MDG page [Not disclosed] (checked the 80 paths in the sidebar; MDG appears only in the release notes legend and entries, last MDG entry v2.0.4, 29 January 2024, and as video guide 4 Mock Data Generation) [Documented] (REL, VIDG)",
     "Mirage site: \"Mock Data Generation is available via API through Cloak (https://cloak.gov.sg)\" [Documented] (MIR). Cloak home page: \"Mirage is our sister product for Synthetic Data Generation\" [Documented] (SITE). Web UI route inside Cloak [Not disclosed] (checked the Cloak Guide pages and the home page)",
     "Generated records, not user data. The portal gives field categories: \"Person, location, business, healthcare, and custom\" [Documented] (PF). \"Mock data generation does not require any input data\" [Documented] (MIR)",
     INV], "PF MIR SITE REL VIDG SIDE"))
    out.append(row([
     "Cloak Anonymiser Python package",
     "\"Cloak Anonymiser is a Python package that provides offline access to Cloak's tabular anonymisation features (without k-anonymity)\" [Documented] (PKG)",
     "\"no longer actively maintained and is provided as-is, with no ongoing support, security updates, dependency updates, bug fixes, or compatibility guarantees\" [Documented] (PKG). Provided \"on a case-by-case basis\" [Documented] (PKG)",
     "Python package, offline. Apply at cloak.gov.sg/packages, which redirects to a sign-in page (HTTP 307 observed 2026-10-10) [Documented] (PKG, PKGP). The package guide redirects to a login page (HTTP 302 observed 2026-10-10) so its content is [Not disclosed]",
     "Tabular data: \"allows non-cloud eligible datasets or agency on-premise systems to apply policy-based data transformations\" [Documented] (PKG). No free-text function [Inferred] (premise: the PKG page and the HOME access table say tabular only)",
     INV], "PKG PKGP HOME PKGGUIDE"))
    out.append(row([
     "Mirage (sister product)",
     "\"Mirage is our sister product for Synthetic Data Generation — creating realistic, statistically faithful datasets without any real personal data\" [Documented] (SITE). Mirage's own page: \"A mock and synthetic data generation toolkit\" [Documented] (MIR)",
     "Separate product with its own site and support address [Documented] (MIR). \"Mirage is currently free for all approved users (no charge for FY26)\" [Documented] (MIR)",
     "Web UI for synthetic data generation: \"Synthetic Data Generation is currently available through the Web UI only\" [Documented] (MIR)",
     "Synthetic data generation \"requires uploading real data for model training\" [Documented] (MIR). Mirage is not mined further in this inventory [Inferred] (premise: scope decision for Cloak research, not a Mirage fact)",
     INV], "SITE MIR"))
    out.append(row([
     "enCRYPT (former name)",
     "Earlier name of the product: \"Rebranding of enCRYPT to Cloak\" in v2.0.0, 20 November 2023 [Documented] (REL)",
     "Superseded by the Cloak name [Documented] (REL). The first release, v1.0.0 of 13 March 2023, was a tabular flow \"for CSV files up to 20 columns and 100MB in size\" [Documented] (REL)",
     "Release notes still refer to enCRYPT in v1.2.2: \"export data feature from enCRYPT to Analytics.Gov\" [Documented] (REL)",
     "Tabular data in v1.0.0; free-text anonymisation first available in v1.2.0 [Documented] (REL)",
     LEG], "REL"))
    return "\n".join(out)


def block_b():
    h = "| Path | Audience | Security level or sign-in | Data classification ceiling | Applies to | Caveats and status | Covered by Table 3 column | Source URL |"
    out = [h, "|---|---|---|---|---|---|---|---|"]
    CEIL = "\"up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)\" [Documented] (HOME). Terms Schedule 4.6 [Documented] (TERMS, see block (e))"
    out.append(row([
     "Web UI for WOG users (WOG-AD)",
     "Whole-of-Government users: \"Cloak is available to Whole-Of-Government (WOG) users, who can log in at cloak.gov.sg using WOG-AD where supported\" [Documented] (FAQ)",
     "WOG-AD sign-in. \"For WOG users: Log in immediately at cloak.gov.sg using WOG-AD. No onboarding required for the Web UI.\" [Documented] (PGS)",
     CEIL,
     "Free-text and tabular anonymisation, templates, secrets and decryption [Documented] (HOME, FTDC, TPL). \"No-code; includes k-anonymity recommendations\" [Documented] (HOME)",
     "A job returns a download request and an emailed password to unzip the folder [Documented] (USE). cloak.gov.sg banner: \"Cloak will undergo scheduled maintenance every Wednesday from 6 PM to 12 AM. Please avoid running any jobs during this period.\" [Documented] (SITE, observed 2026-10-10). Real-time use through the Web UI [Not disclosed] (checked USE: jobs are download requests)",
     ALL3], "FAQ PGS HOME USE SITE TERMS"))
    out.append(row([
     "Web UI for non-WOG users (registration, TechPass, approval)",
     "Select non-government users: \"including public healthcare institutions and data contributors to agency projects\" [Documented] (FAQ). A Non-Government Entity (NGE) must \"Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step.\" [Documented] (FAQ)",
     "Register at cloak.gov.sg/register; \"it will submit the request to Cloak's Ops Team\" who approve or decline [Documented] (REGG). Vendors: \"you will receive an email from Techpass to complete the onboarding\" [Documented] (REGG). The register page returned HTTP 200 [Documented] (REGP, observed 2026-10-10)",
     CEIL,
     "Web UI features as for WOG users [Inferred] (premise: the FAQ describes one Web UI and says NGE users have \"the Web UI (available immediately upon registration)\") [Documented] (FAQ)",
     "Terms clause 3.3 limits non-public-sector use to a consented purpose (quoted in block (e)). The portal says access \"is approved on a case by case basis for entities in service for public sector outcomes\" [Documented] (PGS). The FAQ links the Terms at cloak.gov.sg/terms, which returned HTTP 404 on 2026-10-10; the live Terms are at go.gov.sg/cloak-terms [Documented] (FAQ, TERMS)",
     ALL3], "FAQ REGG REGP PGS TERMS"))
    out.append(row([
     "API L2 (personalised token)",
     "\"Individual users on platforms that have integrated with Cloak (e.g. MAESTRO). Access is scoped to authorised users on that platform.\" [Documented] (APIG)",
     "L2, personalised token [Documented] (APIG). Home page access table: \"Supports L2 (Analytics.gov), L3 (GCC), and L4 (internet)\" [Documented] (HOME). An API key for the chosen security level is required [Documented] (APIG)",
     "API-specific ceiling [Not disclosed] (checked APIG, HOME, FAQ; the API guide is behind a login). The FAQ states the general ceiling for Government data: \"up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)\" [Documented] (FAQ)",
     "\"the same anonymisation capabilities as the Web UI\" plus \"parameters not available in the Web UI, such as custom recognisers (regex patterns, context words), fine-grained confidence score tuning, or the allow list feature via code\" [Documented] (APIG)",
     "Release v2.2.0, 07 August 2024: \"Intranet API\" [Documented] (REL). The home page names the APIs as \"Intranet (from Analytics.gov or GCC) and Secure Internet API\" [Documented] (SITE). That Intranet API equals L2 plus L3 is [Inferred] (premise: Analytics.gov and GCC appear in both the intranet wording and the L2 and L3 rows)",
     ALL3], "APIG HOME FAQ REL SITE"))
    out.append(row([
     "API L3 (system token, GCC)",
     "\"Agency systems in GCC (AWS or Azure) that need system-to-system integration with Cloak.\" [Documented] (APIG)",
     "L3, system token [Documented] (APIG). An API key for the chosen security level is required [Documented] (APIG)",
     "API-specific ceiling [Not disclosed] (same checks as the L2 row)",
     "Same capabilities as the L2 row [Documented] (APIG)",
     "See the L2 row for the Intranet API note [Documented] (REL, SITE). Batch processing of .csv, .docx and .pdf at scale [Documented] (APIG)",
     ALL3], "APIG HOME REL SITE"))
    out.append(row([
     "API L4 Secure Internet API (signature-based)",
     "\"Users calling Cloak's API from any internet-connected device, where intranet access is not possible.\" [Documented] (APIG). NGE users: \"the Secure Internet API (submit an API onboarding form after registration)\" [Documented] (FAQ)",
     "L4, signature-based [Documented] (APIG). Release v2.1.5, 3 July 2024: \"Secure Internet API (L4)\" [Documented] (REL)",
     "API-specific ceiling [Not disclosed] (same checks as the L2 row)",
     "Same capabilities as the L2 row [Documented] (APIG). A free-text decryption helper script for the Secure Internet API is linked from FTDC [Documented]; its page is behind a login [Not disclosed]",
     "A video guide titled Secure Internet API exists [Documented] (VIDG). Signature scheme and request format [Not disclosed] (checked APIG, VIDG text, REL; the API guide is behind a login)",
     ALL3], "APIG FAQ REL VIDG FTDC"))
    out.append(row([
     "API onboarding and gated documentation",
     "Anyone needing an API key: \"To request API access, please complete our Cloak (API) Onboarding Form\" [Documented] (APIG). The form link was not opened (read-only rule)",
     "\"For API access, raise an onboarding request and you should be provisioned a key within 1-2 business days.\" [Documented] (FAQ). API Guide, API Specifications (OpenAPI) and the free-text decryption helper script each redirect to https://docs.developer.tech.gov.sg/auth/otp-login (HTTP 302, then HTTP 200 login page, redirect_reason not_logged_in, observed 2026-10-10) [Documented] (APIGUIDE, APISPEC)",
     "Not stated for the API route [Not disclosed] (see the L2 row)",
     "Public pages name three API items: a /analyze endpoint on the Replace (Unique) page [Documented] (RUNQ), a \"Reconstruct endpoint for FTA API\" in v2.0.1, 4 December 2023 [Documented] (REL) and the \"allow_list\" parameter in v2.0.5 [Documented] (REL)",
     "Endpoint definitions, request and response schemas, authentication header, rate limits and latency [Not disclosed] (checked APIG, FAQ, REL, RUNQ, STRC and the portal pages; the API guide and OpenAPI pages are behind a login). Whether the API has an input or output flag [Not disclosed] (same checks)",
     ALL3], "APIG FAQ APIGUIDE APISPEC RUNQ REL"))
    out.append(row([
     "Python package (application at cloak.gov.sg/packages)",
     "Teams for which \"the Web UI cannot be used due to security, operational, or data-handling constraints\" or local deployment is required; approval is \"generally granted for a specific use case\" [Documented] (PKG)",
     "Application through cloak.gov.sg/packages, which redirects (HTTP 307) to a sign-in page [Documented] (PKGP, observed 2026-10-10). Package documentation requires login [Documented] (PKG)",
     "\"allows non-cloud eligible datasets or agency on-premise systems to apply policy-based data transformations\" [Documented] (PKG)",
     "Tabular anonymisation only, without k-anonymity [Documented] (PKG)",
     "\"no longer actively maintained and is provided as-is\" [Documented] (PKG). Package added in v2.1.0, 19 March 2024 [Documented] (REL)",
     INV], "PKG PKGP HOME REL"))
    return "\n".join(out)
