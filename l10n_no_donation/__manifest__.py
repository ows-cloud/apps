# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Skattefradrag for gaver",
    "summary": "",
    "version": "14.0.1.0.0",
    "author": "AppsToGROW, Odoo Community Association (OCA)",
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
}
