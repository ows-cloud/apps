from odoo import api, fields, models


class TimeParameterVersion(models.Model):
    _inherit = "base.time.parameter.version"
    
    value_reference = fields.Reference(
        selection="_value_reference_selection",
    )

    @api.model
    def _value_reference_selection(self):
        models = self.env.context.get("selection_models", []).append("account.account")
        return super(
            TimeParameterVersion,
            self.with_context(selection_models=models)
        )._value_reference_selection()
