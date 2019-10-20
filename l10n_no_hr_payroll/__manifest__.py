# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Norway - Payroll',
    'summary': '',
    'version': '0.1',


    'author': 'AppsToGROW',
    'category': 'Localization',
    'data': [
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/views.xml',
        'data/data.xml',
        'data/res.field.csv',
        'data/res.field.selection_value.csv',
        'execute_functions.xml',
    ],
    'depends': [
        'hr_field_value',
        'hr_payroll_account_analytic',
    ],
    'external_dependencies': {'python': ['pyxb']},
    'license': 'AGPL-3',
    'version': '13.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': '''
IMPLEMENTATION:
ir.sequence with code = l10n_no_hr_payroll.amelding

Generate the csv files from l10n_no_hr_payroll.xlsm
''',
}
