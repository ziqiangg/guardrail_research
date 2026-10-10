# Custom

If no entity type matches the data you are trying to anonymise, you may add a **Custom Entity**. This function is similar to the "Find and Replace" feature offered on some text editors, with additional anonymisation features available.  

To do this, first press the **Anonymisation Settings** button to open the drawer.

![custom-3](_resources/custom-3.png)

*The Anonymisation Settings button on the Free Text Anonymisation page.*

![custom-4](_resources/custom-4.png)

*The Anonymisation Settings drawer showing the Default entities tab.*

Click the **Custom entities** tab.

![custom-5](_resources/custom-5.png)

*The Custom entities tab with the option to add a custom entity.*

Continue with these steps to create your own custom entity.

---

### Step 1: Create and Name New Entity

Fill in the name of your custom entity and select your preferred approach between **Pattern-matching based**,

![custom-6](_resources/custom-6.png)

*The Add a custom entity dialog with the Pattern-matching based approach selected.*

and **Large Language Model (LLM) based**.

![custom-8](_resources/custom-8.png)

*The Add a custom entity dialog with the Large Language Model (LLM) based approach selected.*

---

### Step 2: Add word(s) and choose anonymisation technique

If your approach is **Pattern-matching based**,

- Fill in the regular expression representing your custom entity
- Select your anonymisation technique of choice.
- Fill in the word(s) or phase(s) which you wish to detect. You may add multiple tokens under this category.

![custom-7](_resources/custom-7.png ':size=450x')

*Configuration fields for a pattern-matching based custom entity, including regular expressions, transformation type, and inclusion words.*

> Click [here](../custom-entities/custom-entities-structured.md) for more information on Pattern-matching based custom entities.

If your approach is **Large Language Model (LLM) based**,

- Define your custom entity
- Give some examples

![custom-9](_resources/custom-9.png ':size=450x')

*Configuration fields for an LLM-based custom entity, including definition and examples.*

> Click [here](../custom-entities/custom-entities-structured/intro.md) for more information on LLM based custom entities.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
