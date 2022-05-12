from odoo import models, fields, api


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.run'
    _order = 'date_start desc'
