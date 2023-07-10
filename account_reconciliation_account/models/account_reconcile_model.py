from odoo import api, fields, models


class ReconcileModel(models.Model):
    _inherit = "account.reconcile.model"

    match_account_id = fields.Many2one(
        "account.account", string="Account Suggestion"
    )

    @api.onchange("match_account_id")
    def set_counterpart_line(self):
        line = {
            "account_id": self.match_account_id.id,
            "amount_type": "percentage",
            "amount_string": "100",
        }
        self.write({"line_ids": [(5, 0, 0), (0, 0, line)]})

    def _is_applicable_for(self, st_line, partner):
        if (
            self.match_account_id
            and st_line.account_id != self.match_account_id
        ):
            return False
        else:
            return super()._is_applicable_for(st_line, partner)
