from odoo import api, fields, models


class Fields(models.Model):
    _inherit = "ir.model.fields"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        store=True,
        index=True,
        default=lambda self: self.env.company,
    )

    