from odoo import models, fields, api


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    _order = 'date_from desc'
