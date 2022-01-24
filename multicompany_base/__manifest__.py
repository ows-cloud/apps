# Copyright 2021 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'multicompany_base',
    'summary': '',

    'author': 'AppsToGROW',
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/support_user.xml', # after security
        'views/ir.actions.server.xml',
        'views/ir.model.data.xml',
        'views/res.company.xml',
    ],
    'depends': [
        'base',
        'base_setup',
        # 'mail',
    ],
    'post_init_hook': 'post_init_hook',
    'license': 'AGPL-3',
    'uninstall_hook': 'WARNING_DELETE_RULES_uninstall_hook',
    'version': '13.0.1.0.0',
    'website': 'http://www.appstogrow.co',
}
