from odoo import api, fields, models


class Rule(models.Model):
    _inherit = "ir.rule"

    auto_secure = fields.Boolean()
