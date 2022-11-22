# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "hr_field_value",
    "summary": "Add custom HR fields",
    "author": "AppsToGROW, " "Odoo Community Association (OCA)",
    "category": "Uncategorized",
    "data": [
        "views/views.xml",
    ],
    "depends": [
        "base_field_value",
        "hr",
        "hr_contract",
        "hr_holidays",
        "payroll",
        # 'payroll_analytic_qty_rate_amount',
    ],
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/server-tools",
}
