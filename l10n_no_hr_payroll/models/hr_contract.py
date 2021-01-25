from odoo import api, fields, models, _


class HrContract(models.Model):
    _inherit = 'hr.contract'

    leave_ids = fields.One2many('hr.leave', 'contract_id', string='Leaves')
    l10n_no_arbeidsforhold = fields.Char(help="A-melding: ArbeidsforholdId")

    def copy(self, default=None):
        default = dict(default or {})
        if self.l10n_no_arbeidsforhold:
            default['l10n_no_arbeidsforhold'] = self.env['ir.sequence'].next_by_code(
                'l10n_no_hr_payroll.arbeidsforhold')
        return super(HrContract, self).copy(default)

    def l10n_no_action_new_leave(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.leave",
            "views": [[False, "form"]],
            "context": "{'default_employee_id': %d,'default_contract_id': %d}" % (self.employee_id.id, self.id),
        }