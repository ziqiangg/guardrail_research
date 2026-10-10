# PERSON_NAME

## Scenario  
To detect a person's name, the user first tried using Cloak's existing [PERSON entity](/sections/fta/entity-types/intro.md). The user  wants to improve performance based on the unique features of their dataset and/or ways in which names are represented. For example, they observed that detection is affected when names are present in sections of their document that include XML tags. 

---

## Prompts  

![person-name-1](_resources/person-name-1.png ':size=600x')

*Custom entity definition for PERSON_NAME with the first example showing a name within XML tags.*

![person-name-2](_resources/person-name-2.png ':size=600x')

*Additional examples showing name detection in clinical notes, including partial names and names with honorifics.*

---

## Output  

![person-name-3](_resources/person-name-3.png)

*Anonymisation output showing person names replaced with the PERSON_NAME tag in a clinical record.*

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
