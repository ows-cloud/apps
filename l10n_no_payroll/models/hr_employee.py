from odoo import fields, models


class Employee(models.Model):
    _inherit = "hr.employee"

    json = fields.Serialized()
    l10n_no_fribeloep = fields.Integer("Fribeloep", sparse="json")
    l10n_no_trekkprosent = fields.Integer("Trekkprosent", sparse="json")
    l10n_no_trekktabell = fields.Char("Trekktabell", sparse="json")
