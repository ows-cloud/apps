# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Replace Mail Template',
    'summary': 'Custom mail templates',

    'author': 'AppsToGROW',
    'auto_install': True,
    'category': 'Administration',
    'data': [
        'views/mail.template.xml',
    ],
    'depends': [
        'mail',
        'multicompany_base',
    ],
    'license': 'AGPL-3',
    'version': '13.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
