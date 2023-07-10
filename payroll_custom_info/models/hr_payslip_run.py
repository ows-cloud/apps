from odoo import fields, models


class PayslipRun(models.Model):
    _name = "hr.payslip.run"
    _inherit = [_name, "custom.info"]

    custom_info_template_id = fields.Many2one(context={"default_model": _name})
    custom_info_ids = fields.One2many(context={"default_model": _name})
