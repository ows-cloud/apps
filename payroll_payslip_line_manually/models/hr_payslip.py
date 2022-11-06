from odoo import fields, models
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    line_manually_ids = fields.One2many(
        "hr.payslip.line.manually",
        "res_id",
        string="Manual Payslip Lines",
        domain=[("model", "=", "hr.payslip")],
        context={"default_model": "hr.payslip"},
        copy=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
    )

    def _get_lines_dict(
        self, rule, localdict, lines_dict, key, values, previous_amount
    ):
        if type(values) is list:
            for vals in values:
                key = "{code}-{contract}-{analytic}".format(
                    code=(rule.code or str(rule.id)),
                    contract=str(localdict["contract"].id),
                    analytic=vals["analytic_account_id"],
                )
                localdict, lines_dict = super()._get_lines_dict(
                    rule, localdict, lines_dict, key, vals, previous_amount
                )
            return localdict, lines_dict
        else:
            return super()._get_lines_dict(
                rule, localdict, lines_dict, key, values, previous_amount
            )
