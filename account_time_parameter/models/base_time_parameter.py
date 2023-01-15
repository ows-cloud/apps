from odoo import fields, models


class TimeParameter(models.Model):
    _inherit = "base.time.parameter"

    record_model = fields.Selection(
        selection_add=[("account.account", "Account")],
    )

    def _get_value(self, version):
        if self.type == "record" and self.record_model == "account.account":
            return version.value_account_id
        else:
            return super()._get_value(version)
