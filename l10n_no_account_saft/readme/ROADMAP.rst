Let the user download the SAF-T XML file directly from the wizard,
and delete the "l10n_no_account_saft.xml" model.


Documentation of SAF-T (Standard Audit File – Tax)
--------------------------------------------------

https://www.skatteetaten.no/bedrift-og-organisasjon/starte-og-drive/rutiner-regnskap-og-kassasystem/saf-t-regnskap/dokumentasjon/

XSD

* https://raw.githubusercontent.com/Skatteetaten/saf-t/master/Norwegian_SAF-T_Financial_Schema_v_1.10.xsd
* https://github.com/Skatteetaten/saf-t/blob/master/Example%20Files/ExampleFile%20SAF-T%20Financial_999999999_20161125213512.xml
* https://github.com/Skatteetaten/saf-t/blob/master/Example%20Files/ExampleFile%20SAF-T%20Financial_888888888_20180228235959.xml

How to generate Odoo asbtract model mixins and fields
-----------------------------------------------------

* https://github.com/akretion/generateds-odoo
* Remove this element from the XSD:
  <xs:element name="MovementPostingTime" type="xs:time" minOccurs="0">
* python3 gends_run_gen_odoo.py -p /home/ag/.local/bin/generateDS.py
  -d ./saft -l saft -x 1 saft_1.10.xsd
* Replace 'brl_currency_id' with 'saft_currency_id'
