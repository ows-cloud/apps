from odoo import api, fields, models


class AccountReport(models.Model):
    _inherit = "account.move.line"

    # TODO:
    # Change "account.move.line" to behave like a VIEW instead of a TABLE.
    # Then include_initial_balance may be non-stored but behave like stored.

    @api.depends('balance')
    def _compute_balance_pl(self):
        for line in self:
            line.balance_pl = -line.balance
    
    balance_pl = fields.Monetary(
        string='Profit/Loss',
        compute='_compute_balance_pl',
        store=True,
        precompute=True,
        currency_field='company_currency_id',
    )
    include_initial_balance = fields.Boolean(
        "Bring Accounts Balance Forward",
        store=True,
        related="account_id.user_type_id.include_initial_balance",
    )
    user_type_id = fields.Many2one(
        "account.account.type",
        string="Account Type",
        store=True,
        related="account_id.user_type_id",
    )
