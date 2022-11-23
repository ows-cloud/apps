# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Regex Fix",
    "summary": "Journal Sequence",
    "author": "AppsToGROW, Odoo Community Association (OCA)",
    "category": "Administration",
    "data": [
        "views/account.account.type.xml",
        "views/account.group.xml",  # depends on account_financial_report
        "views/account.journal.xml",
        "views/account.move.xml",
        "views/account.move.line.xml",
        "views/res.company.xml",
    ],
    "depends": [
        "account",
        "account_financial_report",
    ],
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "https://github.com/appstogrow/apps",
}
