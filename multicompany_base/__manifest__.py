# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'multicompany_base',
    'summary': '',

    'author': 'AppsToGROW',
    'auto_install': False,
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'views/ir.model.data.xml',
        'views/res.company.xml',
    ],
    'depends': [
        'base',
        'base_setup',
    ],
    'license': 'AGPL-3',
    'version': '14.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
