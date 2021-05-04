# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "SMS event signup",
    'summary': 'Action triggered by incoming SMS',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'data/data.xml',
    ],
    'depends': [
        'event', # event_sale?
        'sms_action',
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': """
    """,
}
