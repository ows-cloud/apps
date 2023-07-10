import re

from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


def replace_lines(text, line_format):
    """Replace lines with new lines in text.
    NB! Make sure that old_line_format matches ONLY the desired lines!!!

    :param text: The text with lines to replace.
    :param line_format: A list of tuples with two elements:
      * Old line format
      * New line format

    Example: convert_line(
        "A cat has 4 legs.",
        [
            (
                "A {animal} has {no_of_legs} legs.",
                "{{'animal': '{animal}', 'no_of_legs': {no_of_legs}}}"
            ),
        ]
    )
    Output: "{'animal': 'cat', 'no_of_legs': 4}"
    """
    for old_line_format, new_line_format in line_format:
        old_regex = (
            old_line_format
            .replace("(", "\\(").replace(")", "\\)")
            .replace("{", "(?P<").replace("}", ">.*)")
        )
        new_text = []
        for old_line in text.split("\n"):
            match = re.search(old_regex, old_line)
            if match:
                new_line = new_line_format.format(**match.groupdict())
            else:
                new_line = old_line
            new_text.append(new_line)
        return "\n".join(new_text)


class HrSalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    analytic_account_id = fields.Many2one(
        "account.analytic.account", "Analytic Account"
    )
    line_manually_model = fields.Selection(
        [("hr.contract", "Contract"), ("hr.payslip", "Payslip")],
        string="Salary Rule input from",
    )

    @api.onchange("line_manually_model")
    def _amount_select_code(self):
        if self.line_manually_model:
            self.amount_select = "code"

    def _reset_localdict_values(self, localdict):
        localdict["rule"] = self
        localdict.pop("result_analytic", None)
        localdict.pop("result_list", None)
        return super(HrSalaryRule, self)._reset_localdict_values(localdict)

    def _satisfy_condition_python(self, localdict):
        localdict["rule"] = self
        return super(HrSalaryRule, self)._satisfy_condition_python(localdict)

    def _compute_rule_code(self, localdict):
        safe_eval(self.amount_python_compute, localdict, mode="exec", nocopy=True)
        if "result_list" in localdict:
            # Return list of values dictionary. Each dictionary will be a payslip line.
            result_list = []
            for result_dict in localdict["result_list"]:
                values = self._get_rule_dict(result_dict)
                values["analytic_account_id"] = result_dict.get("result_analytic")
                result_list.append(values)
            return result_list
        else:
            values = self._get_rule_dict(localdict)
            values["analytic_account_id"] = localdict.get("result_analytic")
            return values

    def replace_lines(self, line_format):
        for record in self:
            record.condition_python = replace_lines(
                record.condition_python, line_format
            )
            record.amount_python_compute = replace_lines(
                record.amount_python_compute, line_format
            )
