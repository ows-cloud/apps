# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Account Regex Fix",
    "summary": "Journal Sequence",
    "author": "AppsToGROW",
    "category": "Administration",
    "data": [
        "views/account.account.type.xml",
        "views/account.group.xml",  # depends on account_financial_report
        "views/account.journal.xml",
        "views/account.move.xml",
        "views/account.move.line.xml",
        "views/res.company.xml",
    ],
    "depends": [
        "account",
        "account_financial_report",
    ],
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "http://www.appstogrow.co",
    "description": r"""
        In debug mode, set journal regex, e.g.
        ^(?P<prefix1>.*?)(?P<year>\d{2})(?P<seq>\d*)(?P<suffix>\D*?)$

        https://github.com/OCA/OCB/pull/1110
    """,
}
