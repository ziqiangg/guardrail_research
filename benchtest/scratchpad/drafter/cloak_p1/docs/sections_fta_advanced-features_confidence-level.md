# Confidence Level (Score)

## Restricting Anonymised Content Using Confidence Level

**Confidence Level (Score)** denotes the level of certainty / probability that a particular entity type is accurately detected by the algorithm. Entities **below the specified threshold** will **not be anonymised**, helping you balance between **over-anonymisation** and **missed detections**.

>The **higher** the Confidence Level set, the **less** Entities will be anonymised. Likewise, setting a **lower** Confidence Level allows more Entities to be anonymised. 
>
>Users may wish to **increase** the Confidence Level if the tool is yielding inaccurate results (e.g. false positives), or **decrease** the Confidence Level if PII entities are not being anonymised (e.g. false negatives). 

After creating a new free text anonymisation project, click on the **Anonymisation Settings** button to open a drawer containing the **Adjust Confidence level** dropdown bar.

![confidence-level-3](_resources/confidence-level-3.png)

*The Anonymisation Settings button on the Free Text Anonymisation project page.*

![confidence-level-2](_resources/confidence-level-2.png)

*The Anonymisation Settings drawer showing the Adjust Confidence level dropdown.*

Click the Adjust Confidence level dropdown to reveal the slider to adjust the analyser's confidence level.

![confidence-level-4](_resources/confidence-level-4.png)

*The expanded confidence level slider, set to the default value of 0.30.*

Press the **Apply Anonymisation Settings** button to save your changes.

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
