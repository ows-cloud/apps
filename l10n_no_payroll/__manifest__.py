# Copyright 2019-2023 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Norway - Payroll",
    "summary": "",
    "author": "AppsToGROW, " "Odoo Community Association (OCA)",
    "category": "Localization",
    "data": [
        "security/ir.model.access.csv",
        "views/hr_contract_views.xml",
        "views/hr_job_views.xml",
        "views/hr_leave_type_views.xml",
        "views/hr_leave_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_payslip_run_views.xml",
        "views/hr_salary_rule_views.xml",
        "views/l10n_no_amelding_views.xml",
        "views/l10n_no_amelding_wizard_views.xml",
        "views/res_company_views.xml",
        "views/menus.xml",
        "execute_functions.xml",
    ],
    "demo": [
        "demo/hr.salary.rule.xml",
    ],
    "depends": [
        "base_sparse_field",
        "hr_contract_leave",
        "payroll_account_analytic",
        "payroll_custom_info",
    ],
    "external_dependencies": {"python": ["pyxb"]},
    "license": "AGPL-3",
    "maintainers": ["appstogrow"],
    "version": "14.0.2.0.0",
    "website": "https://github.com/appstogrow/apps",
}
