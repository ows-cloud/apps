from odoo import fields, models


class TimeParameterVersion(models.Model):
    _inherit = "base.time.parameter.version"

    value_account_id = fields.Many2one("account.account", string="Account Value")

    value_reference = fields.Reference(
        selection_add=[("account.account", "Account")],
    )
