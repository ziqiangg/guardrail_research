# Welcome to Cloak!

Cloak offers tabular and free-text anonymisation to enable agencies to anonymise data safely before data sharing and utilisation. It is available through both a Web UI and API integration, for GSIB and internet devices, and is open to select non-government entities (e.g. public healthcare).

## Why Cloak

- **Safe for sensitive data** - approved to handle data classified up to Confidential Cloud-Eligible (CCE), Sensitive-High (SH)
- **Optimised for Singaporean data** - >97% recall for key PIIs like Name, NRIC and Email
- **Customisable** - add any custom entity using inclusion lists, pattern-matching (regex), or privately-hosted LLMs
- **Collaborative** - share encryption secrets across data owners so anonymisation can occur independently but still be fused using a common encrypted identifier
- **Policy-compliant** - designed to enable IM8 compliance, with k-anonymity testing against WOG Access Modes A and B
- **Scalable** - integrate via API into platforms, pipelines and workflows

## Use cases

| Use case | Example |
|----------|---------|
| Anonymise before sending to LLMs | Strip PII in real-time via API before data reaches external LLMs or other WOG products |
| Bulk anonymisation for analysis or sharing | Anonymise large volumes of data to fine-tune models, conduct policy analysis, or share safely with internal/external collaborators |
| Daily operations and dashboarding | Anonymise operational data so dashboards and reports do not expose PII |
| Consistent anonymisation across sources | Multiple data owners anonymise independently using the same secret, producing data that can still be linked on a common encrypted identifier |

## Features

### Free-Text Anonymisation

- Automatically detect PII from text, documents (.docx, .pdf) and CSV files
- Select what information to keep private or visible based on your use case
- Add custom entities for domain-specific terms not covered by default detection

*View the [Free-Text Anonymisation guide](/sections/fta/usage-guide.md)*

### Tabular Data Anonymisation

- Apply diverse transformation techniques (generalisation, masking, hashing, encryption, and more)
- Test and apply k-anonymity with IM8 access mode recommendations
- Review privacy risk and utility analysis before release

*View the [Tabular Data Anonymisation guide](/sections/tabular/usage-guide.md)*

### Encryption, Decryption and Secret Sharing

- Encrypt identifiers consistently across datasets using shared secrets
- Decrypt data when needed through the Web UI or API
- Enable multi-party collaboration without exposing raw data

*View the [Decryption and Secret Sharing guide](/sections/decryption-secret-sharing/intro-to-decryption.md)*

## How to access

| Channel | Best for | Notes |
|---------|----------|-------|
| **Web UI** | Manual or occasional upload-and-download jobs | No-code; includes k-anonymity recommendations. [Visit cloak.gov.sg](https://www.cloak.gov.sg) |
| **API** | Repeatable workflows, system integration, or high-volume jobs | Supports L2 (Analytics.gov), L3 (GCC), and L4 (internet). [View the API Guide](/sections/developer-api-guide.md) |
| **Package** | Cases where Web UI and API are not workable | Tabular only; provided as-is with no active maintenance. [View Packages](/sections/packages-anonymiser.md) |

## Pricing

Cloak is currently **free** for all approved users. Pricing for cost recovery may be introduced in future financial years, in line with standard GovTech product policy. For FY26, there is no charge.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
