# Utility Analysis

[Data utility](/sections/tabular/privacy-risk-score/utility-analysis.md) means the usefulness of the anonymised data for statistical analyses by data analysts as well as the validity of these analyses when performed on the anonymised data.

>**Equivalence class** refers to the group of indistinguishable records sharing the same values on a set of [indirect identifiers](/sections/tabular/tagging/sensitivity-types.md). Refer to [𝑘-anonymity](/sections/tabular/privacy-risk-score/k-anonymity-test.md) for a better understanding.

---

## Utility Metrics in Cloak

In Cloak, the following utility metrics are computed after applying [𝑘-anonymity](/sections/tabular/privacy-risk-score/k-anonymity-test.md):

- **Maximum equivalence class size**  
  The maximum size of the equivalence classes.

- **Average equivalence class size**  
  The average size of the equivalence classes.

- **Information loss**  
  The loss of utility due to a reduction in accuracy (with [generalisation](/sections/tabular/transformations/generalisation.md)) or complete loss (with [suppression](/sections/tabular/transformations/suppression.md)) of [indirect identifiers’](/sections/tabular/tagging/sensitivity-types.md) values.

- **Normalised average equivalence class size**  
  Measures how well the creation of the equivalence classes approaches the best case, where each record is generalised in an equivalence class of k records.  
  The objective is to minimise the penalty: a value of 1 would indicate the ideal anonymisation in which the size of the equivalence classes equals the given k value.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
