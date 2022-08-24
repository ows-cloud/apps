from odoo import api, fields, models


class HrRuleQtyRateAmount(models.Model):
    _inherit = 'hr.analytic.qty.rate.amount'

    def get_months(self, payslip, month_correction_field_name):
        """ Method to use in hr.salary.rule python code """
        months = 1
        m = payslip.field_value_ids
        if m:
            m = m.filtered(lambda x: x.field_code == month_correction_field_name)
        if m:
            months += float(m.value)
        return months
