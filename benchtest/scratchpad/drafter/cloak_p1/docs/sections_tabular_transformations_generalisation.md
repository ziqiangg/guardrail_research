# Generalisation 

Generalisation reduces the level of detail or precision in data. For example, numerical values can be replaced with averages or randomly selected values within a given range. Date values can be generalised into broader intervals, such as years, months, or quarters. And, text values can be replaced with less granular values (e.g., replacing CEO with C-Suite). 

<b>Examples</b>

| Original value | Transformed value           | Description                        |
|----------------|----------------------------|----------------------------------|
| 23             | [20, 25)                   | Transforms into a generated interval |
| 23             | >= 20                      | Transforms into top-coded value  |
| 23             | < 25                       | Transforms into bottom-coded value |
| 23             | 22.5                       | Transforms into the mean of the generated interval [20, 25] |
| 23             | 24                         | Transforms into a random value from the generated interval [20, 25] |
| 06-12-2021     | 2021-12                    | Transforms into year-month       |
| 06-12-2021     | 2021                       | Transforms into year             |
| 06-12-2021     | 2021-Q4                    | Transforms into year-quarter     |
| 06-12-2021     | [01-11-2021, 31-12-2021]  | Transforms into days interval    |
| 06-12-2021     | >= 04-12-2021              | Transforms into top coded value  |
| 06-12-2021     | <= 25-12-2021              | Transforms into bottom coded value |
| COVID-19       | Mild                       | Transforms into less detailed value. |
| HIV            | Severe                     | Transforms into less detailed value. |

# Usage Guide

## Categorical Type

### Recoding (Generalisation mapping)

The generalisation mapping replaces the original categorical values (nested values as shown in the below figure) with less granular values by grouping them into broader categories, either through a one-to-one correspondence or a many-to-one association.

![generalisation-1](_resources/generalisation-1.png ':size=500x')

*The generalisation mapping interface showing a tree structure where original values (leaf nodes) are grouped under broader categories.*

Easy-to-use interface to create generalisation mapping in Cloak.

---

### What is the difference between the generalisation hierarchy in k-anonymity and the generalisation mapping in Generalisation (Categorical)?

- The **generalisation hierarchy** is a tree-like structure where each node represents a valid value for a data field. The leaf nodes specifically represent the unique values in the data field.  
- As we move from leaf nodes to the root node, the precision of the values decreases. By default, the root node is assigned as the default [suppression](/sections/tabular/transformations/suppression.md) character.  
- The **k-anonymity algorithm** utilises the generalisation hierarchy to identify the optimal value from the tree nodes, aiming to achieve a k-anonymous dataset. Without a generalisation hierarchy, the only available option is to suppress the values.  

On the other hand, the **generalisation mapping** is a process of mapping unique values in a data field to less precise values in the same field. This mapping can be either one-to-one or many-to-one. The unmapped unique values are [retained](/sections/tabular/transformations/retention.md).

---

### Sample output demonstrating generalisation mapping:

| Original value      | Transformed value              |
|---------------------|-------------------------------|
| Divorced            | Unmarried/Not currently married |
| Married-civ-spouse  | Married                       |
| Married-AF-spouse   | Married                       |
| Widowed             | Widowed                       |

---

## Numerical Type

| Input         | Description                               | Default |
|---------------|-------------------------------------------|---------|
| Lower bound   | Used for bottom coding the values         | Optional|
| Upper bound   | Used for top coding the values            | Optional|
| Bin size      | Used for setting the bin size of the intervals | 10      |

### Summary statistics

Used to replace a value with a summary statistic.

Valid values include:  

- **Interval** — replaces with generated intervals  
- **Random** — replaces with random value from generated intervals  
- **Mean** — replaces with mean of generated intervals (calculated using the bounds of the interval)  

---

## Date Type

| Input       | Description                                    | Default  |
|-------------|------------------------------------------------|----------|
| Lower bound | Used for bottom coding the values               | Optional |
| Upper bound | Used for top coding the values                   | Optional |
| Bin size    | Used for setting the bin size of the intervals in days | 10       |

---

### 2. Granularity

| Input       | Description                                     | Default |
|-------------|-------------------------------------------------|---------|
| Granularity | Used to replace a date with a coarser date      | Year    |

Valid values include:

- **Quarter** — replaces with year's quarter (year-Q[1-4])  
- **Year** — replaces with a year (year)  
- **Month** — replaces with a month (year-month)  

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
