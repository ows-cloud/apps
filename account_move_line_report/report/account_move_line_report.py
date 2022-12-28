from odoo import api, fields, models


class AccountReport(models.Model):
    _name = "account.move.line.report"
    _inherit = ["account.invoice.report", "account.move.line"]
    _description = "Accounting Statistics"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'

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
    )
    user_type_id = fields.Many2one(
        "account.account.type",
        string="Account Type",
        store=True,
    )

    # Many2many fields in account.move.line
    analytic_tag_ids = fields.Many2many(
        relation="account_analytic_tag_account_move_line_rel",
        column1="account_move_line_id",
    )
    tax_ids = fields.Many2many(
        relation="account_move_line_account_tax_rel",
        column1="account_move_line_id",
        column2="account_tax_id",
    )
    tax_tag_ids = fields.Many2many(
        relation="account_account_tag_account_move_line_rel",
        column1="account_move_line_id",
        column2="account_account_tag_id",
    )

    @api.model
    def _select(self):
        return super()._select() + """,
        line.amount_currency,
        line.balance,
        -line.balance as balance_pl,
        line.credit,
        line.currency_id,
        line.date,
        line.date_maturity,
        line.debit,
        user_type.include_initial_balance,
        line.matching_number,
        line.name,
        line.parent_state,
        line.reconciled,
        line.reconcile_model_id,
        line.ref,
        line.statement_id,
        account.user_type_id"""

    @api.model
    def _where(self):
        return ""
