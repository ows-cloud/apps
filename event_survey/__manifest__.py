# Copyright 2019-2023 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Event Registration Survey",
    "summary": "Registration Survey for attendees",
    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Administration",
    "data": [
        "security/security.xml",
        "views/views.xml",
        "views/templates.xml",
        "data/email_template_data.xml",
        "data/server_action.xml",
    ],
    "depends": [
        "website_event_sale",
        "survey_action",
    ],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "version": "15.0.1.0.0",
    "website": "https://github.com/OCA",
}
