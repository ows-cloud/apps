# Copyright 2023 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# The General Ledger Standard Accounts code lists are Copyright Regnskap Norge AS, 2018.
# Henrik called on Jan. 23, 2023. They said that software developers may freely use it.
# Source: https://github.com/skatteetaten/saf-t

{
    "name": "Norway - Accounting",
    "summary": "",
    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Accounting",
    "data": [
        "data/account_chart_template_data.xml",
        "data/account.account.template.csv",  # Copyright Regnskap Norge AS
        "data/account.tax.template.csv",
        "data/account_chart_template_data_update.xml",
    ],
    "depends": [
        "account",
    ],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "version": "15.0.1.0.0",
    "website": "https://github.com/OCA",
}
