# Copyright 2022 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Donation Tax Receipt Thanks",
    "summary": "",
    "author": "Henrik Norlin, Odoo Community Association (OCA)",
    "category": "Accounting & Finance",
    "data": [
        "data/report_paperformat_data.xml",
        "data/ir_actions_report_data.xml",
        "data/mail_template_data.xml",
        "data/templates.xml",
        "views/account_analytic_account_views.xml",
        "views/donation_donation_views.xml",
        "views/donation_line_views.xml",
        "views/donation_tax_receipt_views.xml",
        "views/donation_thanks_template.xml",
        "views/res_partner_views.xml",
    ],
    "depends": ["donation"],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "maintainers": ["norlinhenrik"],
    "version": "14.0.1.0.0",
    "website": "https://github.com/OCA/donation",
}
