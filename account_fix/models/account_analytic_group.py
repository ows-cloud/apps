from odoo import api, fields, models, _


class AnalyticGroup(models.Model):
    _inherit = 'account.analytic.group'
    _order = 'name'
