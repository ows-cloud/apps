# Copyright 2019 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Payroll Custom Info",
    "summary": "Add custom HR info",
    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Uncategorized",
    "data": [
        "views/hr_contract_view.xml",
        # "views/hr_employee_view.xml",
        # "views/hr_job_view.xml",
        # "views/hr_leave_type_view.xml",
        # "views/hr_payslip_run_view.xml",
        "views/hr_payslip_view.xml",
        # "views/hr_salary_rule_view.xml",
        # "views/res_company_view.xml",
    ],
    "depends": [
        "base_custom_info",
        "hr",
        "hr_contract",
        "hr_holidays",
        "payroll",
        # 'payroll_analytic_qty_rate_amount',
    ],
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "version": "16.0.1.0.0",
    "website": "https://github.com/OCA",
}
