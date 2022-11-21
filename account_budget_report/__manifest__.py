# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Budget Report",
    "summary": "",
    "author": "AppsToGROW",
    "category": "account",
    "data": [
        "security/ir.model.access.csv",
        "security/ir.rule.csv",
        "views/views.xml",
    ],
    "depends": [
        "account",
    ],
    "external_dependencies": {"python": ["numpy", "pandas"]},
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "http://www.appstogrow.co",
}
