from odoo import api, fields, models, _


class AccountType(models.Model):
    _inherit = 'account.account.type'
    _order = 'note'

    company_id = fields.Many2one('res.company', string="Company")
