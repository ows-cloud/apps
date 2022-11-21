# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Norway - Payroll",
    "summary": "",
    "author": "AppsToGROW, " "Odoo Community Association (OCA)",
    "category": "Localization",
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "data/res.field.csv",
        "data/res.field.selection_value.csv",
        "execute_functions.xml",
    ],
    "demo": [
        "demo/hr.salary.rule.xml",
    ],
    "depends": [
        "hr_field_value",
        "payroll_account_analytic",
    ],
    "external_dependencies": {"python": ["pyxb"]},
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/server-tools",
}
