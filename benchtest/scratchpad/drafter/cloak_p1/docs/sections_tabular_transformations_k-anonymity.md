# K-anonymity

> **Note:** This page provides detailed information on how our algorithm achieves k-anonymity, including an outline of the transformations applied for its implementation.

Please refer [here](/sections/tabular/privacy-risk-score/k-anonymity-test.md) to learn about what k-anonymity is.

---

## Overview

K-anonymity applies automated **[generalisation](/sections/tabular/transformations/generalisation.md)** or **[suppression](/sections/tabular/transformations/suppression.md)** to data fields classified as *[indirect identifiers](/sections/tabular/tagging/sensitivity-types.md)* to ensure every combination of values for [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md) in the dataset appears in at least **𝑘** different records.

>Selecting k-anonymity in **[Step 2 (Transform your data)](/sections/tabular/usage-guide.md)** "passes over" the necessary [transformations](/sections/tabular/transformations/intro-to-transformations.md) to **[Step 3 (Check risk/utility scores)](/sections/tabular/usage-guide.md)**.
>
>Under the [access modes](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md), you **cannot skip Step 3** if k-anonymity is selected for any indirect identifiers; without this step, your data will remain entirely untransformed.

A [transformation](/sections/tabular/transformations/intro-to-transformations.md) is applied to satisfy [k-anonymous](/sections/tabular/privacy-risk-score/k-anonymity-test.md) data, leading to automatic [suppression](/sections/tabular/transformations/suppression.md) or [generalisation](/sections/tabular/transformations/generalisation.md) of unique values (depending on other [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md)) to mitigate [re-identification risk](/sections/tabular/privacy-risk-score/k-anonymity-test.md).

---

## Transformation Details

- For **numeric** or **date** types, **[generalisation](/sections/tabular/transformations/generalisation.md)** is applied, and values are replaced with dynamically generated intervals.
- For **text** types, [generalisation](/sections/tabular/transformations/generalisation.md) is applied using the respective **generalisation hierarchies**.  
  In the absence of a generalisation hierarchy, values will primarily be **suppressed** for that data field.

>**What is the difference between the generalisation hierarchy in k-anonymity and the generalisation mapping in Generalisation (Categorical)?**
>
>The generalisation hierarchy is a **tree-like structure** where each node represents a valid value for a data field. The leaf nodes specifically represent the unique values in the data field. As we move from leaf nodes to the root node, the precision of the values decreases. By default, the root node is assigned as the default [suppression](/sections/tabular/transformations/suppression.md) character. 
>
>The k-anonymity algorithm utilises the generalisation hierarchy to identify the optimal value from the tree nodes, aiming to achieve a k-anonymous dataset. Without a generalisation hierarchy, the only available option is to suppress the values.
>
>On the other hand, generalisation mapping involves a **one-to-one or many-to-one** mapping of unique values in a data field to less precise values, also known as recoded values, within the same field. The unmapped unique values are [retained](/sections/tabular/transformations/retention.md).

---

## Example

For example, the following data fields are classified as [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md): **Age**, **Height**, **Date of Diagnosis**, and **Disease**.

| Age | Height | Date of Diagnosis | Disease   |
|-----|--------|-------------------|-----------|
| 46  | 145    | 01-08-2021        | COVID     |
| 59  | 155    | 31-08-2021        | Typhoid   |
| 20  | 170    | 05-05-2022        | Diarrhoea |
| 25  | 189    | 18-06-2022        | Diarrhoea |

Applying **2-anonymity (k=2)** results in generalising age, height, and date of diagnosis into dynamic intervals:

| Age     | Height     | Date of Diagnosis         | Disease   |
|---------|------------|---------------------------|-----------|
| [45-60] | [145-160]  | [01-08-2021, 25-10-2021]  | COVID     |
| [45-60] | [145-160]  | [01-08-2021, 25-10-2021]  | Typhoid   |
| [19-25] | [170-190]  | [01-04-2022, 30-06-2022]  | Diarrhoea |
| [19-25] | [170-190]  | [01-04-2022, 30-06-2022]  | Diarrhoea |

The dataset is now **2-anonymous**.

---

## Benefits of K-anonymity

With k-anonymity, data fields can potentially preserve more [utility](/sections/tabular/privacy-risk-score/utility-analysis.md) by preventing complete [suppression](/sections/tabular/transformations/suppression.md) or generation of wider [generalisation](/sections/tabular/transformations/generalisation.md) intervals (reduced discernability) of values, while removing unique values.

---

#

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
