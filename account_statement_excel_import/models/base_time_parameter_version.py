from odoo import api, fields, models

""" Select account.account """


class TimeParameterVersion(models.Model):
    _inherit = "base.time.parameter.version"

    value_reference = fields.Reference(
        selection="_value_reference_selection",
    )

    @api.model
    def _value_reference_selection(self):
        selection_models = self.env.context.get("selection_models", [])
        selection_models.append("account.account")
        return super(
            TimeParameterVersion, self.with_context(selection_models=selection_models)
        )._value_reference_selection()
