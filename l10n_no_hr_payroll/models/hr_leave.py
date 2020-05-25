from odoo import api, fields, models, _


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    contract_id = fields.Many2one('hr.contract', string='Contract')
    percent = fields.Float(help="For example, enter 50.0 to apply a percentage of 50%")
    sequence = fields.Integer(help="A-melding: PermisjonId")
