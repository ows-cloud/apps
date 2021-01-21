from odoo import api, fields, models, _

class HrContract(models.Model):
    _inherit = 'hr.contract'

    qty_rate_amount_ids = fields.One2many('hr.rule.qty_rate_amount', 'res_id', string='Recurring Salary',
                                          domain=[('model', '=', 'hr.contract')],
                                          context={'default_model': 'hr.contract'},
                                          copy=True)
