from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    invoice_import_email = fields.Char(readonly=True)
