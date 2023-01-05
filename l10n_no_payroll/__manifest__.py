# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Norway - Payroll",
    "summary": "",
    "author": "AppsToGROW, " "Odoo Community Association (OCA)",
    "category": "Localization",
    "data": [
        "security/ir.model.access.csv",
        "views/res_company_view.xml",
        "views/views.xml",
        # "data/res.field.csv",
        # "data/res.field.selection_value.csv",
        # "execute_functions.xml",
    ],
    "demo": [
        "demo/hr.salary.rule.xml",
    ],
    "depends": [
        "base_sparse_field",
        "hr_contract_leave",
        "payroll_account_analytic",
    ],
    "external_dependencies": {"python": ["pyxb"]},
    "license": "AGPL-3",
    "maintainers": ["appstogrow"],
    "version": "14.0.2.0.0",
    "website": "https://github.com/appstogrow/apps",
}
