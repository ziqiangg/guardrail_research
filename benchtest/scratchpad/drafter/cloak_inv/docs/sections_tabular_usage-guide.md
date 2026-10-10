# Usage Guide

## Step 0: Upload your data

Get started by uploading your sensitive dataset that requires privacy treatment before sharing.

Currently, Cloak is able to process **tabular data** containing up to 100 data fields (i.e. columns) in **CSV or XLSX format**, up to **2 GB** per file. Users on COMET/GSIB devices may be blocked by SIS/Menlo for uploads exceeding **500 MB**. Data cleaning is not currently supported by Cloak, so a clean uploaded dataset will produce better results.

?> **Need automated or high-volume processing?** Cloak's API lets you integrate tabular anonymisation into your own pipelines and workflows without manual uploads. See the [API Guide](/sections/developer-api-guide.md) to get started.

![Upload your dataset](_resources/usage-guide-9.png)

*Upload your CSV file to begin.*

### Data and sensitivity classification

After uploading the data, select the appropriate **Data Classification** and **Sensitivity Classification** from the respective dropdown bars. Cloak supports datasets classified up to **Confidential (Cloud-Eligible)** and/or **Sensitive (High)**. Please make sure that data is processed in the proper environment (e.g. GSIB laptop) with proper security controls in place.

![Select data and sensitivity classification](_resources/usage-guide-10.png)

*Select data and sensitivity classification levels.*

### Column selection

After indicating the presence of file headers in your file, select which columns you would like to be anonymised.

![Select columns for anonymisation](_resources/usage-guide-11.png)

*Choose which columns require anonymisation.*

### Access mode

After indicating the use cases of the data to be anonymised, select the **access mode** for the dataset.

Access modes are based on [IM8 Data Access and Distribution](https://importal.mof.gov.sg/portal/home/ict-ss/im8-classic/data/migrated-version.html#data_access_and_distribution) (Clause 3) guidelines for data sharing beyond the public sector. By selecting an access mode, Cloak **automatically assesses your dataset against the corresponding IM8 k-anonymity guideline** and **recommends appropriate transformations** for each data field based on the policy requirements - removing the need to manually calculate compliance or determine which techniques to apply.

- **Mode A** (safe for public access) - for unrestricted access with little control over how the end-user accesses and uses data. IM8 guideline: k ≥ 5 (max re-identification risk ≤ 20%). Requires heavier anonymisation and a motivated intruder test.
- **Mode B** (conditional/restricted access) - for controlled access in a sanitised environment with good monitoring. IM8 guideline: k ≥ 3 (max re-identification risk ≤ 33%). Lighter anonymisation acceptable.
- **Custom Mode** - for cases where the IM8 modes do not apply or a different risk threshold is appropriate. You define your own target k-value.

These are guidelines rather than hard requirements - the appropriate threshold depends on the use case, data classification, access conditions and residual-risk decision. However, selecting Mode A or Mode B gives you a clear, policy-aligned benchmark: Cloak will recommend transformations in [Step 2](/sections/tabular/usage-guide?id=step-2-apply-transformation-techniques) and indicate in [Step 3](/sections/tabular/usage-guide?id=step-3-review-and-rectify-your-datas-re-identification-risk) whether your dataset passes.

See [Privacy Risk/Utility Score](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md) for a deeper explanation of the modes, k-anonymity, and how to interpret your risk scores.

![Select access mode](_resources/usage-guide-1.png)

*Select an access mode. Mode A and Mode B align to IM8 guidelines; Custom lets you set your own threshold.*

Optionally, you can [use a template](/sections/templates/templates.md?id=use-a-template) saved previously by selecting a tabular job template from the respective dropdown. Press the **Submit** button to proceed to the next step.

---

## Step 1: Tag your data

This step allows you to [tag](/sections/tabular/tagging/intro-to-tagging.md) each data field in your dataset according to the [information](/sections/tabular/tagging/information-types.md) and [sensitivity types](/sections/tabular/tagging/sensitivity-types.md), which are prefilled with **OTHERS** and **NON-SENSITIVE** as default values respectively.

Accurate [tagging](/sections/tabular/tagging/intro-to-tagging.md) of the data fields helps Cloak to provide you with the necessary recommendations on the [transformations](/sections/tabular/transformations/intro-to-transformations.md) to apply and assess your [privacy/utility score](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md).

![Tag your data fields](_resources/usage-guide-2.png)

*Tag each column with its information type and sensitivity type.*

---

## Step 2: Apply transformation techniques

In this step, choose a [transformation](/sections/tabular/transformations/intro-to-transformations.md) technique to be applied for each data field. The list of available techniques is dynamically generated based on the [Information Type](/sections/tabular/tagging/information-types.md), [Sensitivity Type](/sections/tabular/tagging/sensitivity-types.md) and data type of a data field.

If you selected Mode A or Mode B in Step 0, Cloak will pre-fill recommended transformations aligned to the IM8 policy requirements. For data fields where there are no policy-driven recommendations, please select a suitable transformation.

![Apply transformations](_resources/usage-guide-3.png)

*Choose or accept recommended transformation techniques for each data field.*

---

## Step 3: Review and rectify your data's re-identification risk

This step allows you to review your dataset's [risk/utility](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md) metrics and rectify if needed. Cloak assesses the anonymised dataset against your chosen access mode's k-anonymity threshold and presents the results.

### Risk scores

The risk score summary shows whether your dataset meets the guideline for your selected access mode and highlights the maximum re-identification risk across all records.

![Risk scores overview](_resources/usage-guide-4.png)

*Risk score summary showing compliance status against your selected access mode.*

### Detailed metrics

The advanced view provides detailed information on the [risk](/sections/tabular/privacy-risk-score/k-anonymity-test.md) and [utility](/sections/tabular/privacy-risk-score/utility-analysis.md) metrics for applying [k-anonymity](/sections/tabular/privacy-risk-score/k-anonymity-test.md). This view is intended to help you analyse the privacy-utility trade-off and **is not a necessity to proceed**.

![Risk metrics detail](_resources/usage-guide-5.png)

*Detailed risk metrics including k-anonymity, maximum and average re-identification risk, and percentage of unique records.*

![Utility metrics detail](_resources/usage-guide-6.png)

*Utility metrics showing information loss across data fields.*

---

## Step 4: Download your anonymised dataset

You may download your anonymised dataset and report in the final step. You will receive an **email notification** to **complete your download on the Jobs page** once it is ready. Your download will be **available for up to 8 hours** from the job creation time.

The report is self-contained and provides a summary on [policy compliance](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md), [transformation techniques](/sections/tabular/transformations/intro-to-transformations.md) applied, and [risk](/sections/tabular/privacy-risk-score/k-anonymity-test.md) and [utility](/sections/tabular/privacy-risk-score/utility-analysis.md) metrics. It also contains a glossary of privacy terms and a motivated intruder test checklist (required for [Mode A](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md)).

Cloak does not store your data. Data is routinely purged from the system after completion of transformation jobs.

![Download anonymised dataset](_resources/usage-guide-7.png)

*Download your anonymised dataset and compliance report.*

![Job report example](_resources/usage-guide-8.png)

*The downloadable report includes policy compliance status, transformations applied, and risk/utility metrics.*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
