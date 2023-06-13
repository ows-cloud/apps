from odoo import models


class AnalyticGroup(models.Model):
    _inherit = "account.analytic.group"
    _order = "name"
