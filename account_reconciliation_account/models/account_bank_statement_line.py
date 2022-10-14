from odoo import api, fields, models, _


class BankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    counterpart_account_id = fields.Many2one("account.account",
        string="Counterpart Account",
        domain=[('deprecated', '=', False)],
        help="This field may be used at the statement line creation/import to suggest a reconciliation account.",
    )
