from odoo import models, fields, api


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'

    # date_from is very useful for pivoting. Shold be added to payroll.
    date_from = fields.Date("Date From", related='slip_id.date_from', store=True)
    payslip_run_id = fields.Many2one('hr.payslip.run', related='slip_id.payslip_run_id', string="Payslip Batch")
