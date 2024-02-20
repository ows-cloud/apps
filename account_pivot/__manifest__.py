# Copyright 2019-2023 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Pivot",
    "summary": "Similar to account_move_line_report",
    "author": "Ows, " "Odoo Community Association (OCA)",
    "category": "account",
    "data": [
        "security/ir.model.access.csv",
        "security/ir.rule.csv",
        "views/account_account_views.xml",
        "views/account_pivot_views.xml",
    ],
    "depends": [
        "account",
    ],
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "version": "15.0.1.0.0",
    "website": "https://github.com/OCA",
}
