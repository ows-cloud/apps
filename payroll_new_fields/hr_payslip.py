from odoo import models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"
    _order = "date_from desc"
