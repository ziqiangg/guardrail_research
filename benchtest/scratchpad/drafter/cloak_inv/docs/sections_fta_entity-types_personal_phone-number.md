# Phone Number  
*Local or Globally-covered Phone Number*

---

### Default setting:

- REPLACE all phone numbers with `<PHONE_NUMBER>` tag.

**Global coverage disabled:**  
Only Singapore numbers are detected by default. 

>Validation check is not included. Both **real** and **fake** phone numbers may be detected.

>Phone numbers (especially non-Singapore numbers) may sometimes be falsely detected as bank account numbers, or other numeric-type data fields. Users are advised to review to ensure the proper type is detected.

---

### Example

| Original Value                         | Anonymised Value            |
|--------------------------------------|-----------------------------|
| Jason's phone number is 9726 5234.   | Jason's phone number is `<PHONE_NUMBER>`. |
| She's from India and her number is +91 7513200000. | She's from India and her number is `<PHONE_NUMBER>`. |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
