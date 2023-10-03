# Copyright 2019 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Regex Fix",
    "summary": "Journal Sequence",
    "author": "Ows, Odoo Community Association (OCA)",
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
    "maintainers": ["ows-cloud"],
    "version": "15.0.1.0.0",
    "website": "https://github.com/OCA",
}
