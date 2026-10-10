# Packages - Tabular Anonymisation

?> The Anonymiser package is provided on a case-by-case basis for use cases where the Web UI or APIs are not suitable. To apply for access, visit [cloak.gov.sg/packages](https://www.cloak.gov.sg/packages). For complete package documentation, [access it here](https://docs.developer.tech.gov.sg/docs/cloak-anonymiser-package-guide/?product=Cloak) (requires login).

## What is Cloak Anonymiser?

Cloak Anonymiser is a Python package that provides **offline access** to Cloak’s tabular anonymisation features (without k-anonymity). It allows non-cloud eligible datasets or agency on-premise systems to apply policy-based data transformations using a standalone library.

The package determines appropriate transformations based on each column’s information type, sensitivity type and data type, supporting compliance with IM WOG Access Control Modes or custom user-defined rules.

> **When should I use the package vs. the Web UI or API?**
>
> Use the Web UI for manual or occasional upload-and-download jobs. Use the API for repeatable workflows or system integration. Consider the package only where the Web UI and API are not workable for your use case (e.g. local deployment is required, or there are security/operational constraints preventing cloud access). The Web UI or API remains the recommended option where feasible.

## Maintenance and Support

The Cloak Anonymiser package is no longer actively maintained and is provided as-is, with no ongoing support, security updates, dependency updates, bug fixes, or compatibility guarantees. Users are responsible for operating, maintaining, securing, and supporting their own implementation. New capabilities are prioritised for the Cloak platform (Web UI / API) and are unlikely to be added to the package.

## Access

Before granting access, the Cloak team may assess whether the Web UI or APIs can meet your requirements. Access may be considered where:

- The Web UI cannot be used due to security, operational, or data-handling constraints.
- The APIs are unsuitable for the intended deployment model or workload.
- Local deployment is required within your own environment.
- The required functionality is supported by the package.

To apply for access, visit [cloak.gov.sg/packages](https://www.cloak.gov.sg/packages).

## Sharing the Package

Approval is generally granted for a specific use case. If the package is used as part of the same approved implementation or reusable component, it may be reused across multiple applications within that use case.

If another team wishes to use the package for a different use case, they should apply separately via [cloak.gov.sg/packages](https://www.cloak.gov.sg/packages) rather than obtaining the package through redistribution.