# Custom Entities (Structured)

## Identifying Structured Data Patterns with Regular Expressions

**Custom Entities** are used to define entities with structured data patterns specific to your needs. These entities utilise **regular expressions** to recognise and anonymise data based on the patterns you configure.  

For help writing regular expressions, consider using tools like [regex101.com](https://regex101.com) or [pair.gov.sg](https://pair.gov.sg) (with mock data).

---

## 📌 Sample Use Cases

| **Custom Entity**     | **Examples**            | **Regular Expression**         |
|------------------------|--------------------------|--------------------------------|
| Car license number     | SMK1234A<br>SMU7654C      | `SM[A-Z]\d{4}[A-Za-z]`         |
| Unusual date format    | 1990/06-10<br>2019/01-20  | `\d{4}/\d{2}-\d{2}`            |
| Username               | User\gt-jdoe<br>User\gt-asmith | `User\\gt-[a-zA-Z]+`     |

---

## 🔧 How to Add a Custom Entity

1. On the **Free-Text Anonymisation** page, press the **Anonymisation Settings** button to open the drawer.

![custom-entities-structured-5](_resources/custom-entities-structured-5.png)

*The Free Text Anonymisation page with the Anonymisation Settings button highlighted.*

![custom-entities-structured-6](_resources/custom-entities-structured-6.png)

*The Anonymisation Settings drawer showing the Default entities tab and confidence level slider.*

2. Click the **Custom entities** tab.

![custom-entities-structured-7](_resources/custom-entities-structured-7.png)

*The Custom entities tab selected, showing an empty state with the "Add a custom entity" button.*

3. Click **"Add a Custom Entity"**. Fill in the name of your custom entity and select **Pattern-matching based**.

![custom-entities-structured-8](_resources/custom-entities-structured-8.png)

*The "Add a custom entity" dialog with the entity name field and the Pattern-matching based approach selected.*

4. Press the **Add Entity** button. Ensure your new custom entity appears in the **Custom entities** tab (you may have to use the search bar).

![custom-entities-structured-9](_resources/custom-entities-structured-9.png)

*The Custom entities tab showing the newly added "INDUSTRY" entity with its configuration fields.*

5. Describe your **custom entity** using a regular expression.

![custom-entities-structured-10](_resources/custom-entities-structured-10.png ':size=450x')

*A regular expression entered in the custom entity configuration to define the detection pattern.*

6. Save your changes by pressing **Apply anonymisation settings** at the top of the drawer.

7. ✅ Your custom entity is now detected!

> **Tip:** Once added, the custom entity will automatically be recognised and anonymised according to the pattern you've set.

---

## 🔀 Resolving Entity Detection Conflicts

If a value is being incorrectly detected as an existing entity, consider whether the intended entity can be distinguished more clearly. This can often be done by:

1. **Increasing the confidence threshold** of the incorrectly-triggered entity to reduce false positives.
2. **Defining a more specific custom entity** (e.g. regex, inclusion list, or LLM-based entity depending on the use case) that explicitly captures the intended pattern.
3. **Disabling the conflicting entity** if it is not required for the use case.

For example, if a case number is consistently detected as a bank account number, a custom regex for the case number format may provide more accurate detection than relying on the generic bank account entity.

---

### Example: Hospital Case Number vs Bank Account Number

Suppose a 10-digit hospital case number (e.g. `1234567890`) is consistently detected as a **Bank Account Number** because both values follow a similar numeric format.

To improve detection accuracy, you could:

- **Increase the confidence threshold** for the Bank Account Number entity if it is generating too many false positives.
- **Create a custom regex entity** for the hospital case number format (e.g. exactly 10 digits with known prefixes or surrounding keywords). This helps the system distinguish case numbers from genuine bank account numbers.
- **Disable the Bank Account Number entity** if bank account information does not appear in your dataset and does not need to be detected.

In general, if a value is repeatedly classified as the wrong entity type, consider whether the intended entity can be defined more specifically through a custom entity or by adjusting the detection settings of the conflicting entity.

---

## 🚀 Advanced Settings via API

For users who need finer control over custom entity detection — such as specifying **context words** to reduce false positives or **adjusting per-pattern confidence scores** — these advanced settings are available through the Cloak API.

These settings allow you to:
- Define custom context words that must appear near a regex match for detection to trigger (reducing false positives for general patterns).
- Set different confidence scores for each regex pattern (e.g. a stricter pattern can have a higher score than a looser one).
- Combine multiple patterns with different scores for a single entity.

> 📖 For full details on these API-level advanced settings, refer to the [Cloak API Guide](https://docs.developer.tech.gov.sg/docs/cloak-api-guide/?product=Cloak) (sign-in required).

---

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
