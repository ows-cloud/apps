# Users with company-dependent partner

This module implements company_dependent partner_id on model res.users.

## Why?

With strict security between companies, a user with access to multiple non-related companies should have a partner per company.
This could be e.g. a support user or an accountant.

## How to install?

Apply patches:
- git apply /path/to/multicompany_dependent_user_partner/multicompany_dependent_user_partner.patch
- git commit

For new database: Restart Odoo, create a new database, install the module
- python odoo-bin -i multicompany_dependent_user_partner -d MYDATABASE

For existing database:
- Run SQL: "UPDATE ir_module_module SET state = 'to install' WHERE name = 'base';"
(state must be 'to install', not 'uninstalled')
- python odoo-bin -i base,multicompany_dependent_user_partner -d MYDATABASE

## How to use?

Create a new company (ignore the security error).
Go to a list view, e.g. Companies or Users (to avoid another security error).
Select the new company in the top right dropdown menu.
Go to Users.
Do for each user:
- Edit
- A) Write a name and select a language (will create a new partner)
- B) Select an existing partner
- Save

## Bugs

res.users temp_partner_id should be deleted. I see no method in openupgradelib to completely delete a field! (Just the db column...)

In mail/models/mail_message.py check_access_rule(), I wanted to check if user partner exists, and if not, raise UserError.
But creating a user partner will trigger this very method, then I get error because the partner does not exist.

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
