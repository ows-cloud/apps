# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Norway - SAF-T',
    'summary': '',
    'version': '0.1',


    'author': 'AppsToGROW',
    'category': 'Localization',
    'data': [
        'security/ir.rule.csv',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'depends': [
        'account',
    ],
    'license': 'AGPL-3',
    'website': 'http://www.appstogrow.co',

    'description': '''
Docdumentation of SAF-T (Standard Audit File – Tax)
https://www.skatteetaten.no/bedrift-og-organisasjon/starte-og-drive/rutiner-regnskap-og-kassasystem/saf-t-regnskap/dokumentasjon/

XSD
https://raw.githubusercontent.com/Skatteetaten/saf-t/master/Norwegian_SAF-T_Financial_Schema_v_1.10.xsd
https://github.com/Skatteetaten/saf-t/blob/master/Example%20Files/ExampleFile%20SAF-T%20Financial_999999999_20161125213512.xml
https://github.com/Skatteetaten/saf-t/blob/master/Example%20Files/ExampleFile%20SAF-T%20Financial_888888888_20180228235959.xml

Generate Odoo asbtract model mixins and fields
https://github.com/akretion/generateds-odoo
I had to remove this element from the XSD:
<xs:element name="MovementPostingTime" type="xs:time" minOccurs="0">
python3 gends_run_gen_odoo.py -p /home/ag/.local/bin/generateDS.py -d ./saft -l saft -x 1 saft_1.10.xsd
replace 'brl_currency_id' with 'saft_currency_id'
''',
}
