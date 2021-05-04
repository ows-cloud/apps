# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Receive SMS",
    'summary': 'Action triggered by incoming SMS',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/ir.model.access.csv', # TODO restrict access
        'views/views.xml',
    ],
    'depends': [
        'base_technical_user',
        'sms',
    ],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': """
    """,
}
