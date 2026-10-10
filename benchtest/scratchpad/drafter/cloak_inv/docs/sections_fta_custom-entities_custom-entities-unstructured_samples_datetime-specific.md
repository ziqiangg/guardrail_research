# DATE_TIME_SPECIFIC

## Scenario  
User wants to anonymise specific date and/or time expressions, but not other temporal references. The [DATE_TIME entity](/sections/fta/entity-types/intro.md) already exists in Cloak and common NLP models, but the user requires more control over what to and not to detect. 

---

## Prompts  

![datetime-specific-1](_resources/datetime-specific-1.png ':size=600x')

*Definition and first example for the DATE_TIME_SPECIFIC custom entity, showing how a date of birth is identified within an address block.*

![datetime-specific-2](_resources/datetime-specific-2.png ':size=600x')

*Additional examples demonstrating detection of specific dates and times while ignoring general temporal references like "every 3 months" and "during the weekend".*

---

## Output (Cloak with DATE_TIME_SPECIFIC custom entity)

![datetime-specific-3](_resources/datetime-specific-3.png)

*Anonymisation output using the DATE_TIME_SPECIFIC custom entity, replacing only explicit dates while preserving relative time expressions like "3 times a week" and "2 hours post-dinner".*

## Output (Cloak with base DATE_TIME entity) 

![datetime-specific-4](_resources/datetime-specific-4.png)

*Anonymisation output using the base DATE_TIME entity, which over-detects by also replacing relative temporal references such as "42-year-old" and "2 hours".*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
