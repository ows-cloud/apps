from odoo import fields, models


class TimeParameterVersion(models.Model):
    _inherit = "base.time.parameter.version"

    value_reference = fields.Reference(
        selection_add=[("account.account", "Account")],
    )
