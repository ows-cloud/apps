from odoo import models, fields, api


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'

    payslip_run_id = fields.Many2one('hr.payslip.run', related='slip_id.payslip_run_id', string="Payslip Batch")