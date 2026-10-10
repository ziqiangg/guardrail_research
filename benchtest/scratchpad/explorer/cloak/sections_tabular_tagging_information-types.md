# Information Types 

An information type or info type is a type of sensitive data, such as NRIC, ZIP code, credit card number, and so on.

> The info types included in the toolkit take reference from the Anonymisation Guidelines, in which certain transformations are recommended for specific info types. 

These info types are: 
- Account number
- Address
- Contact number 
- Date of Birth
- Email
- IP Address 
- Name
- NRIC
- Occupation
- URL
- Vehicle identifier
- ZIP code
- Other (for info types that do not match the above)   

**Why Mark an Info Type?**

1. **Apply policy-defined transformation**: There are pre-defined info types listed by the government policy. Each of the info types has its own set of rules under the [WOG modes A and B](/sections/tabular/privacy-risk-score/intro-to-privacy-risk-score.md) for the privacy treatment to apply. For example, it is recommended to apply [pseudonymisation](/sections/tabular/transformations/pseudonymisation.md) to NRIC info types.

2. **For recommendation**: This can help apply info type-specific transformations; for example, recommending [email masking](/sections/tabular/transformations/masking/intro-to-masking.md) for emails, in which only the email domain name is retained. 

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
