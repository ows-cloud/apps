from odoo import fields, models


class Payslip(models.Model):
    _name = "hr.payslip"
    _inherit = [_name, "custom.info"]

    custom_info_template_id = fields.Many2one(context={"default_model": _name})
    custom_info_ids = fields.One2many(context={"default_model": _name})

    def get_months(self, month_correction_field_name):
        """Method to use in hr.salary.rule python code"""
        months = 1
        m = self.field_value_ids
        if m:
            m = m.filtered(lambda x: x.field_code == month_correction_field_name)
        if m:
            months += float(m.value)
        return months
