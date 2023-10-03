from odoo import models


# From the module "analytic"
class AnalyticGroup(models.Model):
    _inherit = "account.analytic.group"
    _order = "name"
