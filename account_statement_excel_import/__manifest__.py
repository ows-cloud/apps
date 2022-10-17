# Copyright 2022 AppsToGROW
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "account_statement_excel_import",
    "summary": "using excel_import_export",
    "version": "14.0.1.0.0",
    "author": "AppsToGROW,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/server-tools",
    "category": "Tools",
    "depends": [
        "account_reconciliation_account",
        "base_sparse_field",
        "base_time_parameter",
        "excel_import_hook",
    ],
    "data": [
    ],
    "installable": True,
    "development_status": "Alpha",
    "maintainers": ["appstogrow"],
}
