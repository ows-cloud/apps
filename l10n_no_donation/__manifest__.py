# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Skattefradrag for gaver",
    "summary": "",
    "version": "14.0.1.0.0",
    "author": "AppsToGROW",
    "category": "Localization",
    "data": [
        "security/ir.rule.csv",
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/views.xml",
    ],
    "depends": [
        "donation",  # OCA/donation
        "partner_identification",  # OCA/partner-contact
    ],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "website": "http://www.appstogrow.co",
    "description": """
Documentation

https://www.skatteetaten.no/bedrift-og-organisasjon/rapportering-og-bransjer/tredjepartsopplysninger/gaver-og-tilskudd/gaver-til-organisasjoner/formater-og-tekniske-spesifikasjoner/

PDF https://www.skatteetaten.no/contentassets/3bcbe50b50924c4297c2b62eb89a38da/v2_0_3/filformat-for-gaver-til-organisasjoner-v2_0_3_20161005.pdf

XSD https://www.skatteetaten.no/contentassets/3bcbe50b50924c4297c2b62eb89a38da/v2_0_3/gavefrivilligorganisasjon_v2_0.xsd

XML https://www.skatteetaten.no/contentassets/3bcbe50b50924c4297c2b62eb89a38da/v2_0_3/gavefrivilligorganisasjon_v2_eksempel_normal.xml
""",
}
