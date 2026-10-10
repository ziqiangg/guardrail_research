# Organization

---

### Organization

Detects names of companies, government bodies, and public organisations.

---

### Default setting:

- REPLACE all organisation names with the `<ORGANIZATION>` tag.

---

### Example:

| Original Value                                             | Anonymised Value                                    |
|------------------------------------------------------------|-----------------------------------------------------|
| She works at the Housing Development Board.                | She works at the `<ORGANIZATION>`.                  |
| Please contact GovTech for more information.               | Please contact `<ORGANIZATION>` for more information. |
| The project is a collaboration between MOH and HPB.        | The project is a collaboration between `<ORGANIZATION>` and `<ORGANIZATION>`. |

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
