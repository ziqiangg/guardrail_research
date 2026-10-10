# IM8, Privacy Risk and Utility

The trade-off between [privacy risk](/sections/tabular/privacy-risk-score/k-anonymity-test.md) and loss of [data utility](/sections/tabular/privacy-risk-score/utility-analysis.md) seeks to minimise the latter. This also requires reducing the ***risk of identification* and sensitive data fields disclosure** to an acceptable level.

The risk-utility scale extends between two extremes:

- **Maximum privacy**, in which no data is released (zero risk of disclosure) leading to no utility from the data; and
- **Maximum utility**, in which data is released without any privacy protections, entails the maximum risk of disclosure but also offers the highest level of utility.

The goal of well-applied [anonymisation](/sections/tabular/transformations/intro-to-transformations.md) is to find the optimal point where utility for end users is maximised at an acceptable level of risk. What this **acceptable trade-off** is depends on factors such as the sensitivity of the data, the risk posture of the organisation, and what kind of environment the data is being handled in.

![privacy-risk-1](_resources/privacy-risk-1.png ':size=400x')

*The privacy-utility trade-off curve, illustrating how increasing data privacy reduces utility and vice versa, with the goal of finding an acceptable balance.*

---

## How K-Anonymity and Re-Identification Risk Relate

Cloak reports both [k-anonymity](/sections/tabular/privacy-risk-score/k-anonymity-test.md) and [re-identification risk](/sections/tabular/privacy-risk-score/k-anonymity-test.md). These are not separate concepts - they are a direct mathematical function of each other:

- **K-anonymity** describes the size of the group a record is hidden in: every record shares its indirect identifiers with at least (k - 1) others.
- **Re-identification risk** is the inverse: the probability that an attacker could correctly identify a specific individual from that group.

The formula is: **max re-identification risk = 1 / k**

| If k-anonymity is... | Max re-identification risk is... |
|-----------------------|---------------------------------|
| k = 1 (unique record) | 1/1 = 100% |
| k = 2 | 1/2 = 50% |
| k = 3 | 1/3 = 33% |
| k = 5 | 1/5 = 20% |
| k = 10 | 1/10 = 10% |

When Cloak's report shows a maximum re-identification risk of 100%, this means there is at least one record with a unique combination of indirect identifiers (k = 1). When the risk drops to 33%, this means all records share their indirect identifiers with at least 2 others (k = 3).

---

## Access Modes and WOG Guidelines

When you start a tabular anonymisation job in Cloak, the first decision is to select an **access mode**. This determines the level of anonymisation required based on how the data will be accessed after release.

| | Mode A | Mode B | Custom |
|---|---|---|---|
| **Access type** | Unrestricted access within specified environment | Controlled access in a sanitised environment | User-defined |
| **Level of control** | Little to no control over how end-user accesses and uses data | Good control and monitoring over how end-user accesses and uses data | N/A |
| **Use cases** | Datathons, light analytics, public release | Policy evaluation, programme evaluation | Ad-hoc implementation of specific techniques |
| **Treatment** | Heavy anonymisation; re-identification test required | Light anonymisation; re-identification test optional | As configured by user |
| **K-anonymity guideline** | k ≥ 5 (max re-ID risk ≤ 20%) | k ≥ 3 (max re-ID risk ≤ 33%) | User-defined |

These modes relate to [IM8 Data Access and Distribution](https://importal.mof.gov.sg/portal/home/ict-ss/im8-classic/data/migrated-version.html#data_access_and_distribution) (Clause 3) guidelines on k-anonymity for data sharing beyond the public sector. They are guidelines rather than hard requirements - the appropriate threshold depends on the use case, data classification, access conditions and residual-risk decision.

If you select Mode A or Mode B, Cloak will assess your dataset against the corresponding threshold in Step 3 and indicate whether your data meets the guideline. If you select Custom Mode, you define your own target k-value.

While these guidelines are primarily intended for data sharing beyond the public sector (where risks are typically higher), they are useful concepts for data protection in any context - including intra-agency sharing and internal data handling - as a way to assess and benchmark the residual re-identification risk in a dataset.

---

## The Iterative Process

Choosing [anonymisation techniques](/sections/tabular/transformations/intro-to-transformations.md) in practice entails a series of iterations:

1. **Assess current risk**: Calculate existing k-anonymity and re-identification risk using Cloak.
2. **Apply anonymisation measures**: Apply transformations (generalisation, suppression) to reduce risk. Cloak can recommend transformations aligned to WOG Mode A/Mode B requirements.
3. **Re-assess residual risk**: Review the risk and [utility metrics](/sections/tabular/privacy-risk-score/utility-analysis.md) after anonymisation and determine if the resulting trade-off is acceptable.

If the risk is not sufficiently reduced or the utility loss is too high, adjust the transformations and re-assess. If the anonymised dataset is satisfactory for the use case and context, it can be released.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
