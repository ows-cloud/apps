# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Base Localization',
    'summary': 'Address Format',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'views/views.xml',
        'data/data.xml',
        'execute_functions.xml',
    ],
    'depends': ['base'],
    'license': 'AGPL-3',
    'version': '12.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': '''
        Odoo 12 has res.country address_view_id and name_position and vat_label for better localization.
        address_format is for the reports.
        address_view_id is for the contact UI.
        
        TODO:
        address_format_domestic field: 1850 Mysen | NO-1850 Mysen, NORWAY
        country states always up-to-date worldwide
        zip -> prefill city
    ''',
}
