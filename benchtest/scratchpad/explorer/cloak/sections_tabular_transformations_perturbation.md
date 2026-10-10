# Perturbation

Perturbation adds noise to values to modify them into slightly different values. The supported methods include:

- **Noise addition from a custom range**: Adds a random number from the user-defined upper and lower bounds.  
  _Default bounds_: `[-0.05, 0.05]`.

- **Noise addition within the standard deviation**: Adds a random number within the standard deviation of the raw values.

- **Base rounding**: Rounds values to a user-defined base.  
  _Default base_: `10`.

- **Date shifting**: Adds a number of random days from the user-defined upper and lower bounds on days.  
  _Default bounds_: `[-10, 10]`. The negative values will transform raw dates into past dates. 

---

## Examples

| Original value | Transformed value | Description                                                                 |
|----------------|-------------------|-----------------------------------------------------------------------------|
| 23             | 23.5              | Transforms into a noisy value by adding a random value **within a custom range** |
| 23             | 30                | Transforms into a noisy value by adding a random value **within a standard deviation** |
| 23             | 25                | Transforms into a noisy value by **base rounding**                             |
| 06-12-2022     | 02-12-2022        | Transforms into a noisy date (past date) by adding a random negative value within a **custom range of days**        |
| 06-12-2022     | 08-12-2022        | Transforms into a noisy date (future date) by adding a random positive value within a **custom range of days**      |

---

## Usage Guide

### Numerical Type

#### Noise Addition Within the Custom Range

| Input       | Description                                      | Default  |
|-------------|--------------------------------------------------|----------|
| Lower bound | Used to set the lower bound on random values     | `-0.05`  |
| Upper bound | Used to set the upper bound on random values     | `0.05`   |

#### Base Rounding

| Input | Description                                            | Default |
|--------|--------------------------------------------------------|---------|
| Base   | Used to round values to the nearest multiple of base   | `10`    |

---

### Date Type

#### Date Shifting

| Input       | Description                                          | Default |
|-------------|------------------------------------------------------|---------|
| Lower bound | Used to set the lower bound on random days to add    | `-10`   |
| Upper bound | Used to set the upper bound on random days to add    | `10`    |
 

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
