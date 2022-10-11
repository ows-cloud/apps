from odoo import api, fields, models

class Base(models.AbstractModel):
    _inherit = "account.bank.statement.line"

    def _excel_post_import_time_parameter(self):
        # Replace label keyword with time-related value.
        params = self.env["base.time_parameter"].search([])
        for line in self:
            for param in params:
                if param.code in line.payment_ref:
                    param_value = self.get_time_dependent_parameter(param.code, line.date)
                    line.payment_ref.replace(param.code, param_value)
