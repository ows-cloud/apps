# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'hr_custom_info',
    'summary': 'Add custom HR fields',

    'author': 'AppsToGROW',
    'category': 'Uncategorized',
    'data': [
        'views/hr_contract_views.xml',
    ],
    'depends': [
        'base_custom_info',
        'hr',
        'hr_contract',
        'hr_holidays',
        'payroll',
        # 'payroll_analytic_qty_rate_amount',
    ],
    'license': 'AGPL-3',
    'version': '14.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
