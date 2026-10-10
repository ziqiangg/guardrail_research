# Sensitivity Types 

![sensitivity-types-1](_resources/sensitivity-types-1.png)

*Venn diagram illustrating how data fields from medical and housing datasets are classified into direct identifiers, indirect identifiers, and sensitive attributes.*

**The data fields can be classified into the following sensitivity types:**

Direct identifiers are the data fields that can directly and uniquely identify an individual. Identifying data fields are associated with a high risk of re-identification. They are mostly de-identified (using [pseudonymisation](/sections/tabular/transformations/pseudonymisation.md) or [transposition](/sections/tabular/transformations/transposition.md), for example) or [removed](/sections/tabular/transformations/removal.md) from the dataset. Typical examples include NRIC numbers and names.

Indirect identifiers (also known as quasi-identifiers) are the data fields that can potentially lead to the re-identification of individuals when multiple data fields: 
- can uniquely identify an individual OR  
- combined and cross-referenced with auxiliary information or readily accessible (such as public datasets) datasets. 

Generally, some transformation is applied to reduce the precision of a data field's values ([generalisation](/sections/tabular/transformations/generalisation.md), [perturbation](/sections/tabular/transformations/perturbation.md), [masking](/sections/tabular/transformations/masking/intro-to-masking.md) for example). Date of birth, gender, location, and zip code are common examples.

>Indirect identifiers are primarily used to apply k-anonymity. Accuracy in tagging the indirect-identifiers can help in better estimation of risk and utility. 


>What data fields to tag as indirect identifiers? 
>
>Indirect identifiers are the attributes that are assumed the attacker knows. However, there is no set standard for what constitutes of indirect-identifiers. Timestamps (e.g. driver's food delivery time), location (e.g. rider's drop location), physical characteristics (e.g. weight, height) and medical conditions (e.g. having COVID) can all be thought of as potentially re-identifiying data fields in some situations. In other circumstances, it may appear reasonable to assume that someone attempting to attack a dataset would not have simple access to these values.

Sensitive data fields are the data fields that on disclosure can harm an individual or are protected by law and regulations. They encode characteristics that people don't want to be associated with. They may therefore be of interest to an attacker and, should they be disclosed, could harm data subjects. For instance, a person's sexual orientation, political views, salary, and disability status can be deemed as sensitive data fields.

>In the near future, Cloak will support anonymisation models designed to protect sensitive data fields such as [l-diversity](https://en.wikipedia.org/wiki/L-diversity) and [t-closeness](https://en.wikipedia.org/wiki/T-closeness). 

Non-sensitive data fields are the data fields excluding direct identifiers, indirect identifiers and sensitive data fields. They typically do not pose a threat to privacy and can be kept unchanged (i.e. [retained](/sections/tabular/transformations/retention.md)).

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
