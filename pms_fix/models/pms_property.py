from odoo import fields, models


class PmsProperty(models.Model):
    _inherit = 'pms.property'

    default_pricelist_id = fields.Many2one(
        default=None,
    )
