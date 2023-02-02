from odoo import models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    def get_months(self, month_correction_field_name):
        """Method to use in hr.salary.rule python code"""
        months = 1
        m = self.field_value_ids
        if m:
            m = m.filtered(lambda x: x.field_code == month_correction_field_name)
        if m:
            months += float(m.value)
        return months
