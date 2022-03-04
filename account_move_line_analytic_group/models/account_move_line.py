from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    analytic_group_id = fields.Many2one('account.analytic.group', related='analytic_account_id.group_id', string="Analytic Group")
