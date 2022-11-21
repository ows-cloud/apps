from odoo import models


class HrPayslipLine(models.Model):
    _inherit = "hr.payslip.run"
    _order = "date_start desc"
