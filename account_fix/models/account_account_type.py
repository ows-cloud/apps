from odoo import api, fields, models, _


class AnalyticGroup(models.Model):
    _inherit = 'account.account.type'
    _order = 'note'
