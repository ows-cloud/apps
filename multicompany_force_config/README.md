# Force configuration for all companies

This module implements configuration for all companies.

## Why?

Some records are only installed for the first company.
With strict company security, they are hidden from other companies.

## Configurations

When you create a new company or install/update/uninstall a module,
some company configurations are set by Administrator (user id 2).
E.g. create a mail channel for all employees of the company (if needed).

## How to install?

To force the configuration on all companies after install/update/uninstall a module, apply the loading patch:
- git apply /path/to/multicompany_force_config/patches/core-loading.patch
- git commit

Install the module

## How to use?

To force the configuration manually on a company, open the company in form view, goto JSON tab and click Configure button.

## Author

AppsToGrow
Contact: Henrik Norlin
Email: henrik@appstogrow.co
Mobile: +4791120745

## Supported versions

- 14.0
