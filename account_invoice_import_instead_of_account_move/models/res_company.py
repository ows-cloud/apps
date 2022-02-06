from odoo import api, fields, models, _
import re


class Company(models.Model):
    _inherit = "res.company"

    invoice_import_email = fields.Char(readonly=True)
