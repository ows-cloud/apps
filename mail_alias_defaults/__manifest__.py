# Copyright 2022 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Mail Alias Compute Defaults",
    "summary": "",
    "author": "AppsToGROW, Odoo Community Association (OCA)",
    "category": "Mail",
    "data": [
        "views/mail_alias_view.xml",
    ],
    "depends": [
        "base_time_parameter",
        "mail",
    ],
    "license": "AGPL-3",
    "maintainers": ["appstogrow"],
    "pre_init_hook": "pre_init_hook",
    "version": "14.0.1.0.0",
    "website": "https://github.com/appstogrow/apps",
}
