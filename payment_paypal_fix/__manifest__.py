# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'payment_paypal_fix',
    'summary': '',

    'author': 'AppsToGROW',
    'category': 'Uncategorized',
    'auto_install': False,
    'data': [
        'views.xml',
    ],
    'depends': [
        'payment_paypal',
        'website_new_fields', # because of get_param
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

}
