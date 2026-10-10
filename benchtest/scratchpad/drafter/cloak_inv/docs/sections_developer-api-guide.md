# API Guide

## When to use the API

Cloak's API gives you the same anonymisation capabilities as the Web UI, but designed for integration into your workflows. Consider the API if you:

- Have **large-volume or frequent jobs** that are impractical to process manually through the Web UI
- Need **parameters not available in the Web UI**, such as custom recognisers (regex patterns, context words), fine-grained confidence score tuning, or the allow list feature via code
- Want to **automate anonymisation** as part of a pipeline or scheduled workflow
- Need **batch file processing** (.csv, .docx, .pdf) at scale

## What you need

To use Cloak's API, you need:

1. **An environment that can call the API** - this varies by security level (see below)
2. **An API key** for your chosen security level

## Security levels

| Level | Access type | Who it's for |
|-------|------------|--------------|
| **L2** | Personalised token | Individual users on platforms that have integrated with Cloak (e.g. MAESTRO). Access is scoped to authorised users on that platform. |
| **L3** | System token | Agency systems in GCC (AWS or Azure) that need system-to-system integration with Cloak. |
| **L4** | Signature-based (internet) | Users calling Cloak's API from any internet-connected device, where intranet access is not possible. |

Your choice depends on your infrastructure and access.

## Get started

The full API guide covers environment setup, API key generation, quickstarts, and integration examples for each security level:

*[View the full API Guide →](https://docs.developer.tech.gov.sg/docs/cloak-api-guide/)*

## API Reference

For endpoint definitions, request/response schemas, and parameter details:

*[View the API Specifications (OpenAPI) →](https://docs.developer.tech.gov.sg/docs/cloak-api-specifications-openapi/)*

---

> To request API access, please complete our [Cloak (API) Onboarding Form](https://form.gov.sg/653a8c11a250030012d682c4).

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
