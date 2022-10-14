from odoo import api, fields, models, _


class ReconcileModel(models.Model):
    _inherit = "account.reconcile.model"

    rule_type = fields.Selection(selection_add = [("", "")])