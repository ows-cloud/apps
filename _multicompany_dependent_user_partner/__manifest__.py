# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Company-dependent partner for users",
    "summary": "For each company, set a partner",
    "author": "AppsToGROW, " "Odoo Community Association (OCA)",
    "category": "Administration",
    "data": [
        "views/res.users.xml",
    ],
    "depends": [
        "base",
    ],
    "license": "AGPL-3",
    "pre_init_hook": "pre_init_hook",
    "uninstall_hook": "uninstall_hook",
    "version": "14.0.1.0.0",
    "website": "https://github.com/appstogrow/apps",
}
