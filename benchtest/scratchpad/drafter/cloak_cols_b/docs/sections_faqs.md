# Key FAQs

Welcome to our Frequently Asked Questions (FAQs) section. Here you will find answers to the most common questions about Cloak's services, features and access.

<details>
  <summary>Getting Started and Access</summary>

*How do I access Cloak?*

Cloak is available to Whole-Of-Government (WOG) users, who can log in at [cloak.gov.sg](https://www.cloak.gov.sg) using WOG-AD where supported.

Cloak is also available to select non-WOG users, including public healthcare institutions and data contributors to agency projects. If your organisation has already been approved for Cloak use, you can register for an account at [cloak.gov.sg](https://www.cloak.gov.sg).

If you are a non-approved non-WOG user or are unable to register, please contact Cloak support at [go.gov.sg/cloak-support](https://go.gov.sg/cloak-support) to request whitelisting.

→ [Registration Guide](/sections/registration-guide.md)

---

*How long does it take to get started?*

For the **Web UI**, there is no onboarding time - log in and start using Cloak immediately.

For **API access**, raise an onboarding request and you should be provisioned a key within 1-2 business days.

---

*Should I use the Web UI, API or package?*

| Channel | Best for | Notes |
|---|---|---|
| **Web UI** | Manual or occasional upload-and-download jobs | No-code; includes k-anonymity recommendations |
| **API** | Repeatable workflows or system integration | Supports batch processing, custom recognisers, advanced parameters |
| **Package** | Cases where Web UI and API are not workable | Tabular only; provided as-is with no active maintenance |

The Web UI or API is the recommended option where feasible. Consider the package only on an exception basis.

→ [API Guide](/sections/developer-api-guide.md) | [Packages](/sections/packages-anonymiser.md)

</details>

<details>
  <summary>Data Security and Classification</summary>

*Is it safe to pass data to Cloak for anonymisation?*

To use Cloak, users pass data transiently to Cloak's Government Commercial Cloud (GCC) environment. Cloak does not retain data beyond processing.

For Government data, Cloak has met IM8 requirements around Application Development Security and Risk Management for use of Government data classified up to **Confidential Cloud-Eligible (CCE)**, **Sensitive-High (SH)**. Key risk mitigation measures include:

1. Cloak does not retain data. Raw data is purged upon anonymisation and anonymised data is purged within 24 hours or upon user request.
2. All data is encrypted in transit and at rest.
3. Monthly review of privileged accounts.
4. Quarterly Vulnerability Assessment scan and Yearly Penetration Testing.
5. Salts and Secret Keys within Cloak are stored in encrypted format, and usage of salts/secret keys are audited.

This is a non-comprehensive summary. Users are welcome to contact the team for more details or issues not covered here.

!> The data owner remains responsible for use-case approval, output assessment and residual-risk acceptance.

---

*Does using Cloak mean that the output is automatically anonymised or safe to share?*

No. Cloak applies the transformations selected by the user, but the data owner must assess the final output for remaining direct identifiers, quasi-identifier combinations, missed free-text entities and linkage risk. Classification and sharing approval must be reassessed separately.

---

*Can I anonymise data before sending it to GenAI or an external vendor?*

Yes, this is a common use pattern, provided anonymisation happens before the data leaves the approved environment and the output is validated. Use of Cloak does not itself authorise the downstream platform or recipient. Confirm the downstream classification limit, sharing authority and residual risk.

</details>

<details>
  <summary>Pricing</summary>

Cloak is currently **free** for all approved users. Pricing for cost recovery may be introduced in future financial years, in line with standard GovTech product policy. For FY26, there is no charge.

If you have questions about future pricing, please raise a support ticket at [go.gov.sg/cloak-support](https://go.gov.sg/cloak-support).

</details>

<details>
  <summary>Supported File Formats</summary>

*Free-text anonymisation:*

| Format | Notes | Output |
|---|---|---|
| Direct text input | Paste or type into the editor | Text |
| .csv | Must have proper headers; preview shows first cell | .csv |
| .pdf (native) | Created from electronic files (e.g. Word, PPT) | .docx |
| .pdf (searchable) | Text content recognised as machine-readable text | .csv |
| .pdf (scanned) | Created by scanning physical documents/images | Not supported |
| .docx | Text within images will not be detected | .docx |

*Limits:* CSV files up to 500 MB per file; PDF/DOCX files up to 200 MB per file. Multi-file upload supports up to 100 files and 2 GB total. Users on COMET/GSIB devices may be blocked by SIS/Menlo for uploads exceeding 500 MB.

*Tabular anonymisation:*

| Format | Notes |
|---|---|
| .csv | Up to 100 selected columns, no limit on rows. Up to 2 GB per file. |
| .xlsx | Up to 100 selected columns, no limit on rows. Up to 2 GB per file. |

!> Cloak does not process scanned PDFs, screenshots, images or engineering drawings. Such content requires an approved OCR or text-extraction step before anonymisation.

→ [Free-text Usage Guide](/sections/fta/usage-guide.md) | [Tabular Usage Guide](/sections/tabular/usage-guide.md)

</details>

<details>
  <summary>Improving Free-Text Detection</summary>

*Why does Cloak not detect every name or sensitive entity in my text?*

Free-text detection is probabilistic, so 100% recall should not be assumed. Results can be weaker for:

- Uncommon formats, domain-specific terms, aliases or all-caps names
- Identifiers that resemble ordinary text or numbers
- Document formatting issues (HTML tags, markdown, encoding artefacts, entities split across lines)
- Contextual ambiguity (e.g. a name used as a column header, a phone number embedded in a URL)

Test the output against representative samples and use Cloak's customisation options where baseline detection is insufficient. For high-assurance use cases, pair Cloak with human spot-checking of a sample of the anonymised output.

---

*How do I improve detection?*

The general escalation path is:

1. Confirm the right entity type is enabled in your project settings.
2. Tune the available parameters: [Enhanced Detection](/sections/fta/entity-types/personal/name.md) (for names), [checksum](/sections/fta/entity-types/personal/nric.md) (for NRIC/UEN), global detection (for phone numbers), [score threshold](/sections/fta/advanced-features/confidence-level.md).
3. Add a custom entity ([inclusion list](/sections/fta/custom-entities/custom-entities-fixed-list.md), [regex pattern](/sections/fta/custom-entities/custom-entities-structured.md), or [LLM-enabled](/sections/fta/custom-entities/custom-entities-unstructured/intro.md)) for non-standard formats.
4. For high-assurance use cases, conduct human review on a sample of output.

→ [Entity Types](/sections/fta/entity-types/intro.md) | [Custom Entities](/sections/fta/custom-entities/custom-entities-structured.md)

---

*Should I use an inclusion list, pattern matching, or an LLM-enabled custom entity?*

| Approach | When to use |
|---|---|
| **Inclusion list** | The exact values are known (e.g. a staff list, building names) |
| **Pattern matching (regex)** | The identifier follows stable rules (length, prefix, suffix, separators) |
| **LLM-enabled custom entity** | The target is contextual or domain-specific and cannot be expressed as exact values or deterministic rules |

→ [Inclusion List](/sections/fta/custom-entities/custom-entities-fixed-list.md) | [Structured (Regex)](/sections/fta/custom-entities/custom-entities-structured.md) | [Unstructured (LLM)](/sections/fta/custom-entities/custom-entities-unstructured/intro.md)

---

*How do I reduce false positives?*

- **Allow list**: add specific values or phrases that should never be flagged (e.g. product names, department codes).
- **Score threshold**: increase the minimum confidence score required for detection.
- **Checksum validation** (NRIC, UEN): enable to reject matches that fail mathematical validation.
- **Disable overly broad entities**: if an entity type causes too many false positives and is not needed for your use case, disable it.

→ [Confidence Level](/sections/fta/advanced-features/confidence-level.md) | [Exceptions](/sections/fta/entity-types/others/exceptions.md)

---

*Can I use more than one LLM-enabled custom entity in a project?*

The Web UI normally allows one LLM-enabled custom entity per project because each entity adds processing time. For evaluation, create separate projects and reuse saved settings. If multiple entities are essential, contact the Cloak team.

</details>

<details>
  <summary>Improving Tabular Anonymisation</summary>

*How do I improve my k-anonymity score?*

1. **Review your sensitivity tags** - ensure columns are tagged correctly as direct identifiers, indirect identifiers, or sensitive attributes. Incorrect tags are the most common cause of unexpected scores.
   → [Sensitivity Types](/sections/tabular/tagging/sensitivity-types.md)

2. **Apply transformations before k-anonymity** - pre-applying generalisation or masking to high-cardinality columns (e.g. full addresses, dates of birth) reduces the suppression needed to achieve k-anonymity.
   → [Generalisation](/sections/tabular/transformations/generalisation.md) | [Masking](/sections/tabular/transformations/masking/intro-to-masking.md)

3. **Adjust your target k value** - a higher k means stronger privacy but more data loss. If utility is too low, consider whether a lower k is acceptable for your use case.
   → [K-Anonymity](/sections/tabular/transformations/k-anonymity.md) | [Risk Analysis](/sections/tabular/privacy-risk-score/k-anonymity-test.md) | [Utility Analysis](/sections/tabular/privacy-risk-score/utility-analysis.md)

---

*Why is my k-anonymity value still low after removing Name and NRIC?*

Removing direct identifiers does not remove uniqueness created by combinations of quasi-identifiers. Detailed geography, housing status, exact income, age, dates or rare attributes may still single out a record. Review the selected quasi-identifiers and calculate k on the exact dataset intended for release.

→ [Privacy Risk and Utility](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md)

---

*Is k >= 3 mandatory for inter-agency data sharing?*

k >= 3 is not a universal hard requirement for inter-agency sharing. The appropriate threshold depends on the use case, classification, access conditions and residual-risk decision. Document why a higher k is not achievable without unacceptable utility loss and obtain the required governance approval.

The IM8 access modes provide clear benchmarks:
- **Mode A** (public access): k >= 5, max re-identification risk <= 20%
- **Mode B** (restricted access): k >= 3, max re-identification risk <= 33%
- **Custom**: define your own target k-value

→ [IM8 Access Modes](/sections/tabular/usage-guide.md?id=access-mode) | [K-Anonymity Test](/sections/tabular/privacy-risk-score/k-anonymity-test.md)

</details>

<details>
  <summary>Templates</summary>

*Can I save, reuse or share anonymisation templates?*

Yes. Both tabular and free-text anonymisation support saving and reusing templates. Template **sharing** is available for tabular anonymisation only; free-text templates are personal and cannot be shared.

| | Tabular | Free Text |
|---|---|---|
| Save and reuse | Yes | Yes |
| Share with others | Yes | No |
| Update (versioning) | Yes | Save new only |

→ [Templates Guide](/sections/templates/templates.md)

</details>

<details>
  <summary>Troubleshooting</summary>

*My job appears to still be running - is something wrong?*

**Tabular anonymisation:** Most jobs complete within minutes. If a job has been running for more than 8 hours, it is likely that an error was encountered during processing.

**Free-text anonymisation:** The Web UI shows an estimated processing time. If the job exceeds the estimated time by more than twofold, it is likely that an error was encountered.

In either case, please raise a support ticket at [go.gov.sg/cloak-support](https://go.gov.sg/cloak-support) with your Job ID and a screenshot of the current job status.

---

*I'm having issues uploading or downloading files.*

Upload and download issues can be caused by device type, browser, network configuration, or file format. Please raise a support ticket at [go.gov.sg/cloak-support](https://go.gov.sg/cloak-support) with:

- What device you are using (e.g. GSIB, SIS, GFE, personal)
- Your browser (e.g. Chrome, Edge)
- Your Job ID (if applicable)
- A screenshot of the error or unexpected behaviour

</details>

<details>
  <summary>Guide for Non-Government Users</summary>

*Who is eligible?*

Cloak primarily serves Singapore public-sector users, enabled public healthcare users, and selected non-government users participating in collaboration with an agency or in service of public service objectives. If you or your organisation is not currently whitelisted, please raise a support ticket at [go.gov.sg/cloak-support](https://go.gov.sg/cloak-support) describing your use case and whether you have any agency collaborators.

---

*What is a Non-Government Entity (NGE)?*

Non-Government Entities (NGEs) are entities not covered under the Public Sector Governance Act and therefore not subject to IM8 Data. This includes MOHH entities and universities (e.g. NUS, NTU, SMU).

NGEs may be subject to other regulations that Cloak is not actively designed to fulfil. It is the NGE's responsibility to assess Cloak's suitability for their use case and applicable requirements.

---

*What should NGE users consider before using Cloak?*

Per Cloak's Terms of Use (Schedule 4.4), it is the user's responsibility to assess whether using Cloak complies with all applicable data laws, regulations, rules and guidelines. Two primary considerations:

1. **Is the anonymised output sufficiently safe for your purpose?** Run sample data through Cloak and assess the outputs against your requirements.
2. **Is it safe to pass your data to Cloak for processing?** Assess whether your data falls within Cloak's supported classification threshold.

---

*How do NGE users access Cloak?*

1. Contact the Cloak team to confirm purpose of use and obtain pre-approval. MOHH entities do not need this step.
2. Register for an account using your institution email at [cloak.gov.sg](https://www.cloak.gov.sg). You will receive an email within 2 business days from no-reply@cloak.gov.sg once registration is successful.
3. Log in using your credentials.

NGE users have two modes of access: the Web UI (available immediately upon registration) and the Secure Internet API (submit an API onboarding form after registration).

→ [Registration Guide](/sections/registration-guide.md)

---

*Do NGE users need to sign an agreement?*

Users do not sign a separate agreement or contract. All users are legally bound by Cloak's [Terms of Use](https://www.cloak.gov.sg/terms).

NGE users are additionally required to fulfil Clause 3.3: they must have agreed with the Cloak team on the purpose of use prior to access, and any change in purpose requires written consent (including via email).

</details>

---

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
