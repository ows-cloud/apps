from odoo import fields, models


class BankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    account_id = fields.Many2one(
        "account.account",
        string="Account Suggestion",
        domain=[("deprecated", "=", False)],
        help="This field may be used at the statement line creation/import " + \
            "to suggest a reconciliation account.",
    )
