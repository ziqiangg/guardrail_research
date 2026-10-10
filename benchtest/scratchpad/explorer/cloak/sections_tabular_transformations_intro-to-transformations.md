# Data Transformations 

Data Transformation refers to the process of replacing the original sensitive values with the privacy-preserving sanitised values. For example, characters may be [changed](/sections/tabular/transformations/masking/intro-to-masking.md), identifiers may be replaced with [garbled text](/sections/tabular/transformations/transposition.md) or [pseudonyms](/sections/tabular/transformations/pseudonymisation.md), [random noise](/sections/tabular/transformations/perturbation.md) may be added, and so on.

Transformations are a valuable privacy-preserving tool that can help to de-identify and anonymise [identifiers and sensitive data fields](/sections/tabular/tagging/sensitivity-types.md).

>What is **de-identification** and **anonymisation**?
>
>Let us consider the below statement released in a news. 
>
>"Agnes Yuen is a 27-year-old female, suffering from depression, who presented herself for treatment on 6th December." (statement 1)
>
>Clearly, this statement contains information to identify Agnes.  But if we can transform that part of the information that can reveal Agnes's identity, then she will not be identifiable from the information, and her privacy risk will be reduced in this context. 
>
>Let us first try by [removing](/sections/tabular/transformations/removal.md) (or [replacing](/sections/tabular/transformations/pseudonymisation.md)) Agnes's name (a [direct identifier](/sections/tabular/tagging/sensitivity-types.md)) which can lead to her blatant identification. 
>
>"A 27-year-old female, suffering from depression presented herself for treatment on 6th December." (statement 2)
>
>*This process of removing or replacing [direct identifiers](sections/tabular/tagging/sensitivity-types.md) (such as NRIC, names) is known as de-identification.*
>
>Agnes's name was removed from statement 2, but a lot of the information that can be used to identify Agnes ([indirect identifiers](/sections/tabular/tagging/sensitivity-types.md) -- age and date of visit) or leak sensitive information about her ([sensitive data field](/sections/tabular/tagging/sensitivity-types.md) -- medical condition) is still present. This information can be exploited by an adversary to identify Agnes by using some auxillary information (such as background knowledge, public datasets). 
>
>We can make the statement less specific to Agnes: 
>
>"A female in her late twenties, suffering from a severe disease, presented herself for treament between 2nd to 8th December." (statement 3)
>
>With statement 3, the risk of identification of Agnes is reduced by hiding her in the crowd.
>
>Anonymisation is the conversion of personal data into data that cannot be used to identify any individual. 
>
>**De-identification is sometimes mistakenly equated to anonymisation, however, it is only the first step of anonymisation. A de-identified dataset may easily be re-identified when combined with data that is publicly or easily accessible (Source: [PDPC Guide](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/Guide-to-Basic-Anonymisation-31-March-2022.ashx)).**

![data-transformations-1](_resources/data-transformations-1.png)

*Overview of the transformation techniques available in Cloak, showing how each method transforms sample data values.*

The following transformations are currently supported by Cloak:
- [Encryption](/sections/tabular/transformations/encryption.md)
- [Generalisation](/sections/tabular/transformations/generalisation.md) 
- [K-anonymity](/sections/tabular/transformations/k-anonymity.md)
- [Masking](/sections/tabular/transformations/masking/intro-to-masking.md)
    - [Email Masking](/sections/tabular/transformations/masking/email-masking.md)
    - [NRIC Masking](/sections/tabular/transformations/masking/nric-masking.md)
    - [Landed Property Masking](/sections/tabular/transformations/masking/landed-property-masking.md)
- [Perturbation](/sections/tabular/transformations/perturbation.md)
- [Pseudonymisation](/sections/tabular/transformations/pseudonymisation.md)
- [Retention](/sections/tabular/transformations/retention.md)
- [Removal](/sections/tabular/transformations/removal.md)
- [Suppression](/sections/tabular/transformations/suppression.md)
- [Shuffling](/sections/tabular/transformations/shuffling.md)
- [Transposition](/sections/tabular/transformations/transposition.md)

In the future, Cloak will support more advanced transformations such as [format-preserving encryption](https://en.wikipedia.org/wiki/Format-preserving_encryption), substitution with [information types](https://cloud.google.com/dlp/docs/transformations-reference#replacement) or synthetic data and so on.

>Didn't find the transformation you were looking for? 
>
>Please contact us to support a transformation for your use case. We will be glad to help.  💙

