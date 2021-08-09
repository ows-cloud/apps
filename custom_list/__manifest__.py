# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Custom List',
    'summary': 'For budget or statistics',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/views.xml',
        'views/granheim.xml',
    ],
    'depends': [
        'account',
        'analytic',
        'uom',
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.co',

    'description': '''

    ''',
}
