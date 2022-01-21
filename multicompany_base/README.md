# Multicompany Base

Base module to have one multicompany database instead of multiple databases.

The company with id 1 is considered the SYSTEM company.

For each model:
- Creating company_id field (except on company model).
- Assigning every record to a company (company_id 1 for system records).
- Creating security rules.

For each company:
- Creating some necessary records.
- To let users have a different partner for each company, install company_dependent_user_partner.

## Why?

With very small, very similar companies, it might be easier to manage them all in one database.

## The Security Action

The security action will make sure that:
- A user cannot access any data which is not belonging to the active company or its parent/child companies.
- A company manager can access all data in the active company and its parent/child companies.

## The Config Action

The configure company action will:
- create a company mail channel for all employees
- copy system sequences with code
- create default user
- create public user
- create website
See multicompany_config.py for updated info.

## How to install?

First apply the patch:
- git apply /path/to/multicompany_base/multicompany_base.patch
- git commit

Then install this module

Finally, you may want to set these parameters in Settings - Technical - Parameters - System parameters:
- multicompany_base.force_security = 1
-- Update the security every time Odoo is loaded or a module is installed or updated.
- multicompany_base.force_config = 1
-- Update for the configuration of all companies every time Odoo is loaded or a module is installed or updated. It will also auto-configure a new company.
- multicompany_base.support_user_ext_id = the external ID of a user or False. 
-- This user will get access to all new companies. The intention is to be able to give support.

## How to manually apply security & configuration?

There are two new menu items in Settings - Technical - Security:
- Force security
- Force configure all companies

In company form view, there is a button: Auto-Configure.

## How to manage companies and users?

Create a new company (ignore the security error).
Go to a list view, e.g. Companies or Users (to avoid another security error).
Select the new company in the top right dropdown menu.
Go to Users (if multicompany_dependent_user_partner is installed).
Do for each user:
- Edit
- A) Write a name and select a language (will create a new partner)
- B) Select an existing partner
- Save

## Security vulnerabilities

Users may run untrusted code in server actions, salary rules, tax rules etc.
Additional security for save_eval will forbid certain text phrases in the untrusted code.
Private methods are forbidden except in superuser mode.

If 'odoo.tools.safe_eval.wrap_module' exists in an Odoo module, a python module is whitelisted for safe_eval.
Check the security of the python module before using the Odoo module.

Below are some methods of the ORM. If they exist in an Odoo module, check the security of the code before using the module.
.sudo()
.with_company()
.with_context()
.with_env()
.with_prefetch()
.with_user()

## Bugs

Error in log just after creating a new company.
Add company id to URL cids to avoid access error.
(This doesn't work: self.env.companies = new_company # The new environment "stops" in the api.py call_kw_model_create.)

res.users temp_partner_id should be deleted. I see no method in openupgradelib to completely delete a field! (Just the db column...)

## Roadmap

Import company from another database.
Export company to another database.

## How to contribute?

You are very welcome to help with the tasks in the roadmap!
Please sign the OCA document (I would like to move the repo to OCA).

## Author

AppsToGrow
Contact: Henrik Norlin
Email: henrik@appstogrow.co
Mobile: +4791120745

## Supported versions

- 14.0
