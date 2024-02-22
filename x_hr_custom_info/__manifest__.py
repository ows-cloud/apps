# Copyright 2019 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "hr_custom_info",
    "summary": "Add custom HR fields",

    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Uncategorized",
    "data": [
        "views/hr_contract_views.xml",
    ],
    "depends": [
        "base_custom_info",
        "hr",
        "hr_contract",
        "hr_holidays",
        "payroll",
    ],
    "license": "AGPL-3",
    "version": "15.0.1.0.0",
    "website": "https://github.com/OCA",
}
