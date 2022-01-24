# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Multicompany force security',
    'summary': 'Strict security between companies',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/multicompany.force.security.xml',
        'views/res.company.xml',
    ],
    'depends': [
        'multicompany_base',
        'mail',
    ],
    'license': 'AGPL-3',
    'uninstall_hook': 'WARNING_DELETE_RULES_uninstall_hook',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
