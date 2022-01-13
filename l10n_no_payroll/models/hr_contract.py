from odoo import api, fields, models, _


class HrContract(models.Model):
    _inherit = 'hr.contract'

    leave_ids = fields.One2many('hr.leave', 'contract_id', string='Leaves')
    l10n_no_arbeidsforhold = fields.Char(help="A-melding: ArbeidsforholdId")
    l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer = fields.Float(compute='compute_l10n_no_fields')
    l10n_no_stillingsprosent = fields.Float(compute='compute_l10n_no_fields')

    def compute_l10n_no_fields(self):
        for record in self:
            record.l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer = float(record.field_value_ids.filtered(lambda x: x.field_code == "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer").value)
            record.l10n_no_stillingsprosent = float(record.field_value_ids.filtered(lambda x: x.field_code == "l10n_no_stillingsprosent").value)

    def copy(self, default=None):
        default = dict(default or {})
        if self.l10n_no_arbeidsforhold:
            default['l10n_no_arbeidsforhold'] = self.env['ir.sequence'].next_by_code(
                'l10n_no_payroll.arbeidsforhold')
        return super(HrContract, self).copy(default)

    def l10n_no_action_new_leave(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "hr.leave",
            "views": [[False, "form"]],
            "context": "{'default_employee_id': %d,'default_contract_id': %d}" % (self.employee_id.id, self.id),
        }