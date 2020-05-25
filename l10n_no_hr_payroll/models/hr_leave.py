from odoo import api, fields, models, _


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    contract_id = fields.Many2one('hr.contract', string='Contract')
    percent = fields.Float(help="For example, enter 50.0 to apply a percentage of 50%")
    sequence = fields.Integer(help="A-melding: PermisjonId")


class HrContract(models.Model):
    _inherit = 'hr.contract'

    leave_ids = fields.One2many('hr.leave', 'contract_id', string='Leaves')

    def l10n_no_action_new_leave(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.leave",
            "views": [[False, "form"]],
            "context": "{'default_employee_id': %d,'default_contract_id': %d}" % (self.employee_id.id, self.id),
        }