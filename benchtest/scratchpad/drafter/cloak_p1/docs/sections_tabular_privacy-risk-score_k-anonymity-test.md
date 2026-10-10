# K-Anonymity

>**Note:** This page explains **what** k-anonymity and re-identification risk are, how they relate, and what thresholds to target.

Refer [here](/sections/tabular/transformations/k-anonymity.md) for detailed information on **how** Cloak's algorithm achieves k-anonymity, including an outline of the transformations applied.

---

## Why Does This Matter?

In 1997, by simply using the demographic data - ZIP code, gender, and date of birth - the Governor of Massachusetts was re-identified in the released hospital dataset with [de-identified](/sections/tabular/transformations/intro-to-transformations.md) records. This re-identification was possible due to:

- The presence of some **auxiliary (public) dataset** which contained the same demographic data  
- Governor was in **both the datasets**  
- The demographic data of the Governor was **unique within both datasets**: only one record had the demographic values of the governor.

In general, not limited to demographic data, the data owner should consider which data fields might be used by motivated intruders, based on commonly used fields or what the attacker might be specifically concerned about, and classify these fields as [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md). 

>**What data fields to tag as indirect identifiers?** 
>
>Indirect identifiers are the attributes that are assumed the attacker knows. However, there is no set standard for what constitutes indirect identifiers. Timestamps (e.g. driver's food delivery time), location (e.g. rider's drop location), physical characteristics (e.g. weight, height) and medical conditions (e.g. having COVID) can all be thought of as potentially re-identifying data fields in some situations. In other circumstances, it may appear reasonable to assume that someone attempting to attack a dataset would not have simple access to these values.

---

## What is K-Anonymity?

The auxiliary datasets are typically public datasets which cannot be altered. Thus, the onus lies on you to transform your data in a way that prevents such linkage attacks.

One of the ways to safeguard your data is to ensure that [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md) are no longer unique within the dataset without completely eliminating them from the dataset, which would be undesirable. This is the basic idea of k-anonymity.

**A dataset is said to be k-anonymous if every combination of values for [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md) in the dataset appears at least for k different records.** For example, if a [de-identified](/sections/tabular/transformations/intro-to-transformations.md) dataset contains indirect identifiers (gender, age, and ZIP code), such a dataset would have a property of k=3 if there were at least three individuals with the same combination of gender, age, and ZIP code.

>These groups of indistinguishable records sharing the same values on a set of indirect identifiers are termed **equivalence classes**.

An attacker might find out the [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md) of their target using an auxiliary dataset, but then these indirect identifiers will be linked to k different individuals, so it will increase the uncertainty of identifying the target.

![k-anonymity-test-1](_resources/k-anonymity-test-1.png)

*Linkage attack: shared indirect identifiers (green) across two datasets allow an attacker to link records and infer sensitive attributes.*

---

## What is Re-Identification Risk?

**Re-identification risk** is the probability of a record being assigned a correct identity, which may lead to the identity disclosure of an individual in the dataset. The re-identification risk is based on the assumption that an attacker knows that their target is in the dataset. The equivalence class sizes determine the probability that the identity of the target will be revealed.

The simplest way to compute re-identification probability is **`1 / (equivalence class size)`**. All the records in an equivalence class will have the same probability of re-identification.

>#### Can we have zero risk?
>
>The requirement for zero risk is non-realistic if one wants to release data. The only way to meet this requirement is not to disclose the data at all (or not collect it). Rather, the approach that needs to be taken is to define an acceptable probability of re-identification. If the actual probability of re-identification is below the acceptable values, then the dataset can be disclosed.

---

## How K-Anonymity and Re-Identification Risk Relate

K-anonymity and re-identification risk are a direct mathematical function of each other. They are not separate metrics - they express the same underlying protection in different terms:

- **K-anonymity** describes the group size: how many records share the same combination of indirect identifiers.
- **Re-identification risk** is its inverse: the probability that an attacker could single out one individual from that group.

The formula is: **max re-identification risk = 1 / k**

| K-anonymity | Max re-identification risk |
|-------------|---------------------------|
| k = 1 (unique record) | 1/1 = 100% |
| k = 2 | 1/2 = 50% |
| k = 3 | 1/3 = 33% |
| k = 5 | 1/5 = 20% |
| k = 10 | 1/10 = 10% |

When Cloak's report shows a maximum re-identification risk of 100%, this means there is at least one record with a unique combination of indirect identifiers (k = 1). When the risk drops to 33%, this means all records share their indirect identifiers with at least 2 others (k = 3).

---

## Example

The Ministry of Health wants to release healthcare data for researchers to do data analysis for the public good.

| Age | Disease     | Date of Diagnosis |
|------|-------------|------------------|
| 23   | COVID-19    | 12-08-2022       |
| 32   | Typhoid     | 21-09-2022       |
| 21   | COVID-19    | 21-09-2022       |
| 47   | Tuberculosis| 06-02-2021       |
| 51   | Tuberculosis| 11-02-2021       |
| 60   | Tuberculosis| 30-01-2021       |

Suppose this dataset needs to be 3-anonymised before its release. One possible 3-anonymisation of the dataset would be:

| Age     | Disease | Date of Diagnosis        |
|---------|---------|--------------------------|
| [20-35] | -       | [01-08-2022, 28-10-2022] |
| [20-35] | -       | [01-08-2022, 28-10-2022] |
| [20-35] | -       | [01-08-2022, 28-10-2022] |
| [45-60] | Severe  | [15-01-2021, 28-02-2022] |
| [45-60] | Severe  | [15-01-2021, 28-02-2022] |
| [45-60] | Severe  | [15-01-2021, 28-02-2022] |

Every combination of age, disease, and date of diagnosis now shares the same values. This dataset is now 3-anonymous, with a maximum re-identification risk of 33%.

Consider another example with varying equivalence class sizes:

| Age | ZIP code | Equivalence class size | Re-identification probability |
|------|----------|-----------------------|-------------------------------|
| 28   | 120414   | 3                     | 33.33%                        |
| 30   | 145890   | 4                     | 25%                           |
| 40   | 145890   | 5                     | 20%                           |

The rationale behind this method of estimating re-identification risk is that an attacker could learn the indirect identifiers of their target using an external dataset (auxiliary information), but since these indirect identifiers will be linked to different individuals (of equivalence class size), the risk for each individual in the dataset will be reduced. This helps to ensure that individuals have plausible deniability and prevents attacks from re-identifying an individual with 100% certainty.

---

## How to Achieve a K-Anonymised Dataset

[Generalisation](/sections/tabular/transformations/generalisation.md) and [suppression](/sections/tabular/transformations/suppression.md) are the two main building blocks used to convert a dataset into a k-anonymous dataset.

Let k > 1 be a fixed value. Suppose tabular private data needs to be released, and we can apply suppression and/or generalisation to various entries in the dataset. If the [suppression](/sections/tabular/transformations/suppression.md)/[generalisation](/sections/tabular/transformations/generalisation.md) of the indirect identifiers is done in such a way that every record becomes syntactically indistinguishable from k - 1 other records in the dataset, the modified dataset is k-**anonymised**.

---

## Metrics in Cloak

Cloak's risk and utility reports present the following re-identification metrics, derived from the sizes of the equivalence classes:

- **Maximum re-identification risk** is the worst-case scenario, in which the equivalence class with the highest re-identification probability is assumed to represent the entire dataset.

  Situations where this might be appropriate include:

  - When the data owner wants to err on the conservative side  
  - Assuming the adversary is smart and will focus attention on the records that have the highest re-identification probability

  In the example above, the maximum re-identification probability is 33.33% (the equivalence class of size 3).

- **Average re-identification risk** is the proportion of records that can be correctly re-identified on average.

  The average re-identification probability in the example above is 25% (average of each row's re-identification probability).

- **Percentage of unique records** is the percentage of records with an equivalence class size of one (meaning no other records have the same values). These records are at the highest risk of re-identification in the dataset.

---

## What K-Value Should I Target?

[IM8 Data Access and Distribution](https://importal.mof.gov.sg/portal/home/ict-ss/im8-classic/data/migrated-version.html#data_access_and_distribution) (Clause 3) provides guidelines on k-anonymity for data sharing beyond the public sector:

| Access Mode | Guideline | Max re-identification risk | Description |
|-------------|-----------|---------------------------|-------------|
| **Mode A** (safe for public access) | k ≥ 5 | ≤ 20% | Unrestricted access with little control over how the end-user accesses and uses data |
| **Mode B** (conditional/restricted access) | k ≥ 3 | ≤ 33% | Controlled access in a sanitised environment (e.g. through secure terminals) |

These are guidelines rather than hard requirements. k ≥ 3 is not a universal requirement for all data sharing - the appropriate threshold depends on the use case, data classification, access conditions and residual-risk decision. While primarily intended for data sharing beyond the public sector (where risks are typically higher), they are useful concepts for data protection in any context as a way to assess and benchmark the residual re-identification risk in a dataset.

>**Using Cloak to meet these guidelines:**
>
> 1. **Assess current risk** - Calculate existing k-anonymity and re-identification risk using Cloak. Since re-identification risk = 1/k, these tell you the same thing.
> 2. **Apply anonymisation** - Use Cloak's k-anonymity feature to apply transformations (generalisation, suppression) aligned to your target k-value.
> 3. **Re-assess residual risk** - Review the risk and [utility](/sections/tabular/privacy-risk-score/utility-analysis.md) metrics after anonymisation and determine if the resulting trade-off is acceptable.
> 4. **If further transformation would defeat the purpose**, consider a more controlled access environment (e.g. moving from Mode A to Mode B) and document the residual risk rather than forcing a numerical threshold.

[IM8 Data Access and Distribution](https://importal.mof.gov.sg/portal/home/ict-ss/im8-classic/data/migrated-version.html#data_access_and_distribution) also recommends considering a **motivated intruder test** for Mode A assessments. This involves assessing whether an individual could be re-identified by someone with access to public information (e.g. internet, social media, public records) but without specialist technical skills. Refer to Clause 3.2/G8 for more information.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
