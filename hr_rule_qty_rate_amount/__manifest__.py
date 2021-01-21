# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'hr_rule_qty_rate_amount',
    'summary': 'Easily create and use salary rules',

    'author': 'AppsToGROW',
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'depends': ['hr_payroll', 'analytic'],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',
    'description': '''See the core changes in hr_payroll: https://github.com/apps2grow/odoo/commit/97fdeef09223338c5e3cf5c93149b7ca17219b62''',
}