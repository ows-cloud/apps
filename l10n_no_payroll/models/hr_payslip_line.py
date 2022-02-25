from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    
    l10n_no_man_months = fields.Float("Man Months", compute='_compute_man_months', store=True)

    def _compute_man_months(self):
        for line in self:
            rule = line.salary_rule_id
            code_field = rule.field_value_ids.filtered(lambda x: x.field_code == "l10n_no_Loennsbeskrivelse")
            if len(code_field) == 1:
                code = code_field.selection_value_id.code
                if code == 'fastloenn':
                    line.l10n_no_man_months = line.quantity * line.rate / 100.0
                elif code == 'timeloenn':
                    try:
                        hours_per_week = line.contract_id.field_value_ids.filtered(lambda x: x.field_code == "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer").value
                    except:
                        raise UserError("Contract {} (id {}) is missing field l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer.".format(line.contract_id.name, line.contract_id.id))
                    weeks_per_year = 52.0
                    months_per_year = 12.0
                    hours_per_month = float(hours_per_week) * weeks_per_year / months_per_year
                    line.l10n_no_man_months = line.quantity * line.rate / 100.0 / hours_per_month
