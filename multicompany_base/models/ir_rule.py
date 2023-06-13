from odoo import fields, models


class Rule(models.Model):
    _inherit = "ir.rule"

    auto_secure = fields.Boolean()
