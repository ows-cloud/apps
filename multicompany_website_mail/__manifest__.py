# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Company Website",
    'summary': 'res_company.website_id',

    'author': 'AppsToGROW',
    'auto_install': True,
    'category': 'Uncategorized',
    'data': [
        'res.company.xml',
    ],
    'depends': [
        'website',
        'mail',
        'multicompany_base'
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
