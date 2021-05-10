# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Duty List',
    'summary': '',

    'author': 'AppsToGROW',
    'category': 'Hidden/Dependency',
    'depends': [
        'mass_mailing',
        'web_widget_x2many_2d_matrix',
    ],
    'data': [
        'data/data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/views.xml',
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',
}
