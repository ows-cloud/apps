# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Booking',
    'summary': 'Booking of resources',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/views.xml',
    ],
    'depends': [
        'hr', 
        'product'
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',
}
