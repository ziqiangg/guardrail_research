# SG Bank Account Number

---

### All available Singapore Bank Account Number

Detects Singapore bank account numbers based on common formats and patterns ([example](https://singapore-bank.net/sg-bank-and-branch-code-guide/)).

---

### Default setting:

- REPLACE bank account numbers with a `<SG_BANK_ACCOUNT_NUMBER>` tag.

>Phone numbers (especially non-SG numbers) may sometimes be falsely detected as bank account numbers, or other numeric-type data fields. Users are advised to review to ensure the proper type is detected.

---

### Example:

| Original Value                                  | Anonymised Value                    |
|------------------------------------------------|-----------------------------------|
| This is my POSB bank account number: 192-52215-9. | This is my POSB bank account number: `<SG_BANK_ACCOUNT_NUMBER>`. |
| Please transfer the funds to OCBC bank account 8275719283. | Please transfer the funds to OCBC bank account `<SG_BANK_ACCOUNT_NUMBER>`. |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
