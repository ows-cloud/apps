from datetime import datetime

from odoo import fields, models
from odoo.exceptions import UserError


class HrPayslipLine(models.Model):
    _inherit = "hr.payslip.line"

    l10n_no_man_months = fields.Float(
        "Man Months", compute="_compute_man_months", store=True
    )
    l10n_no_total_ytd = fields.Float(
        "Total, year to date", compute="_compute_l10n_no_total_ytd"
    )

    def _compute_man_months(self):
        for line in self:
            rule = line.salary_rule_id
            code_field = rule.field_value_ids.filtered(
                lambda x: x.field_code == "l10n_no_Loennsbeskrivelse"
            )
            if len(code_field) == 1:
                code = code_field.selection_value_id.code
                if code == "fastloenn":
                    line.l10n_no_man_months = line.quantity * line.rate / 100.0
                elif code == "timeloenn":
                    try:
                        hours_per_week = line.contract_id.field_value_ids.filtered(
                            lambda x: x.field_code
                            == "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer"
                        ).value
                    except:
                        raise UserError(
                            "Contract {} (id {}) is missing field l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer.".format(
                                line.contract_id.name, line.contract_id.id
                            )
                        )
                    weeks_per_year = 52.0
                    months_per_year = 12.0
                    hours_per_month = (
                        float(hours_per_week) * weeks_per_year / months_per_year
                    )
                    line.l10n_no_man_months = (
                        line.quantity * line.rate / 100.0 / hours_per_month
                    )

    def _compute_l10n_no_total_ytd(self):
        for line in self:
            date_from = line.slip_id.date_from
            lines_ytd = self.search(
                [
                    ("employee_id", "=", line.employee_id.id),
                    ("salary_rule_id", "=", line.salary_rule_id.id),
                    ("date_from", ">=", datetime(date_from.year, 1, 1).date()),
                    ("date_from", "<=", date_from),
                ]
            )
            line.l10n_no_total_ytd = sum(lines_ytd.mapped("total"))
