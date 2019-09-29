# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Field Value',
    'summary': 'Add field/value to any object',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/views.xml',
    ],
    'depends': ['base'],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': '''
        See implementation example in res_field_value.py and views.xml
    ''',
}
