from odoo import _, fields, models
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval


class HrSalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    analytic_account_id = fields.Many2one(
        "account.analytic.account", "Analytic Account"
    )
    qty_rate_amount_from = fields.Selection(
        [("hr.contract", "Contract"), ("hr.payslip", "Payslip")],
        string="Salary Rule input from",
    )
    condition_python = fields.Text(
        string="Python Condition",
        required=True,
        default="""
                    # Available variables:
                    #----------------------
                    # payslip: object containing the payslips
                    # employee: hr.employee object
                    # contract: hr.contract object
                    # rule: hr.salary.rule object
                    # rules: object containing the rules code (previously computed)
                    # categories: object containing the computed salary rule categories (sum of amount of all rules belonging to that category).
                    # worked_days: object containing the computed worked days
                    # inputs: object containing the computed inputs

                    # Note: returned value have to be set in the variable 'result'

record = payslip.qty_rate_amount_ids
if record:
  record = record.filtered(lambda x: x.salary_rule_id.id == rule.id)
result = bool(record)""",
        help="Applied this rule for calculation if condition is true. You can specify condition like basic > 1000.",
    )
    amount_python_compute = fields.Text(
        string="Python Code",
        default="""
                    # Available variables:
                    #----------------------
                    # payslip: object containing the payslips
                    # employee: hr.employee object
                    # contract: hr.contract object
                    # rule: hr.salary.rule object
                    # rules: object containing the rules code (previously computed)
                    # categories: object containing the computed salary rule categories (sum of amount of all rules belonging to that category).
                    # worked_days: object containing the computed worked days.
                    # inputs: object containing the computed inputs.

                    # Note: returned value have to be set in the variable 'result'

result_list = []
records = payslip.qty_rate_amount_ids.filtered(lambda x: x.salary_rule_id.id == rule.id)
for record in records:
  result = 0 if result_qty == 0.0 or result_rate == 0.0 else record.amount
  result_list.append((result, record.quantity, record.rate, record.analytic_account_id.id))""",
    )

    # TODO should add some checks on the type of result (should be float)
    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the environement in which to compute the rule
        :return: returns a tuple build as the base/amount computed, the quantity and the rate
        :rtype: [(amount float, quantity float, rate float, analytic_account_id integer/False)]
        """
        self.ensure_one()
        if self.amount_select == "fix":
            try:
                return [
                    (
                        self.amount_fix,
                        float(safe_eval(self.quantity, localdict)),
                        100.0,
                        False,
                    )
                ]
            except:
                raise UserError(
                    _("Wrong quantity defined for salary rule %s (%s).")
                    % (self.name, self.code)
                )
        elif self.amount_select == "percentage":
            try:
                return [
                    (
                        float(safe_eval(self.amount_percentage_base, localdict)),
                        float(safe_eval(self.quantity, localdict)),
                        self.amount_percentage,
                        False,
                    )
                ]
            except:
                raise UserError(
                    _(
                        "Wrong percentage base or quantity defined for salary rule %s (%s)."
                    )
                    % (self.name, self.code)
                )
        else:
            try:
                localdict["rule"] = self
                safe_eval(
                    self.amount_python_compute, localdict, mode="exec", nocopy=True
                )
                if localdict["result_list"]:
                    return localdict["result_list"]
                else:
                    return [
                        {
                            "result": float(localdict["result"]),
                            "result_qty": localdict.get("result_qty") or 1.0,
                            "result_rate": localdict.get("result_rate") or 100.0,
                            "result_analytic": localdict.get("result_analytic")
                            or False,
                            "result_name": localdict.get("result_name") or False,
                        }
                    ]
            except Exception as ex:
                raise UserError(
                    _(
                        """
Wrong python code defined for salary rule %s (%s).
Here is the error received:

%s
"""
                    )
                    % (self.name, self.code, repr(ex))
                )

    def _satisfy_condition(self, localdict):
        """
        @param contract_id: id of hr.contract to be tested
        @return: returns True if the given rule match the condition for the given contract. Return False otherwise.
        """
        self.ensure_one()

        if self.condition_select == "none":
            return True
        elif self.condition_select == "range":
            try:
                result = safe_eval(self.condition_range, localdict)
                return (
                    self.condition_range_min <= result
                    and result <= self.condition_range_max
                    or False
                )
            except:
                raise UserError(
                    _("Wrong range condition defined for salary rule %s (%s).")
                    % (self.name, self.code)
                )
        else:  # python code
            try:
                localdict["rule"] = self
                safe_eval(self.condition_python, localdict, mode="exec", nocopy=True)
                return "result" in localdict and localdict["result"] or False
            except Exception as ex:
                raise UserError(
                    _(
                        """
Wrong python condition defined for salary rule %s (%s).
Here is the error received:

%s
"""
                    )
                    % (self.name, self.code, repr(ex))
                )

    def convert_rule(self):
        for rule in self:
            # result_list.append((amount, record.quantity, record.rate, record.analytic_account_id.id))
            text = rule.amount_python_compute
            last_line = text.split("\n")[-1]
            if "  result_list.append((" in last_line:
                new = last_line
                new = new.replace("  result_list.append((", "").replace("))", "")
                words = new.split(", ")
                assert len(words) == 4
                new_last_line = "  result_list.append({{'result': {}, 'result_qty': {}, 'result_rate': {}, 'result_analytic': {}}})".format(
                    words[0],
                    words[1],
                    words[2],
                    words[3],
                )
                last_line = last_line.replace("result_list", "# result_list")
                text_without_last_line = text[: text.rfind("\n")]
                rule.amount_python_compute = (
                    text_without_last_line + "\n" + last_line + "\n" + new_last_line
                )
