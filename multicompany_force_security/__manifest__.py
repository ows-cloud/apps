# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Multicompany strict security',
    'summary': 'Strict security between companies',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/ir.model.data.xml',
    ],
    'depends': [
        'base',
    ],
    'license': 'AGPL-3',
    'version': '14.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
