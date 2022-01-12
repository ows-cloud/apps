# Copyright 2022 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Patch Fix',
    'summary': "xmlid with company_id, set user's partner",

    'author': 'AppsToGROW',
    'auto_install': True,
    'category': 'Administration',
    'data': [
        'views/ir.model.data.xml',
    ],
    'depends': ['base'],
    'license': 'AGPL-3',
    'post_init_hook': 'post_init_hook',
    'version': '14.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
