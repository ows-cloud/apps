from odoo import fields, models


class AccountType(models.Model):
    _inherit = "account.account.type"
    _order = "note"

    company_id = fields.Many2one("res.company", string="Company")
