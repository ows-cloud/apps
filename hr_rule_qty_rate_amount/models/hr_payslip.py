from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    qty_rate_amount_ids = fields.One2many(
        "hr.rule.qty_rate_amount",
        "res_id",
        string="Quantity Rate Amount",
        domain=[("model", "=", "hr.payslip")],
        context={"default_model": "hr.payslip"},
        copy=True,
    )

    # TODO: make payroll PR (set employee contract)
    # Maybe I should have kept the code? contract_id and struct_id are now missing on the payslips.

    # Changes are done only in the contracts loop
    @api.model
    def _get_payslip_lines(self, contract_ids, payslip_id):
        def _sum_salary_rule_category(localdict, category, amount):
            if category.parent_id:
                localdict = _sum_salary_rule_category(
                    localdict, category.parent_id, amount
                )

            if category.code in localdict["categories"].dict:
                localdict["categories"].dict[category.code] += amount
            else:
                localdict["categories"].dict[category.code] = amount

            return localdict

        class BrowsableObject(object):
            def __init__(self, employee_id, dict, env):
                self.employee_id = employee_id
                self.dict = dict
                self.env = env

            def __getattr__(self, attr):
                return attr in self.dict and self.dict.__getitem__(attr) or 0.0

        class InputLine(BrowsableObject):
            """a class that will be used into the python code, mainly for usability purposes"""

            def sum(self, code, from_date, to_date=None):
                if to_date is None:
                    to_date = fields.Date.today()
                self.env.cr.execute(
                    """
                    SELECT sum(amount) as sum
                    FROM hr_payslip as hp, hr_payslip_input as pi
                    WHERE hp.employee_id = %s AND hp.state = 'done'
                    AND hp.date_from >= %s AND hp.date_to <= %s AND hp.id = pi.payslip_id AND pi.code = %s""",
                    (self.employee_id, from_date, to_date, code),
                )
                return self.env.cr.fetchone()[0] or 0.0

        class WorkedDays(BrowsableObject):
            """a class that will be used into the python code, mainly for usability purposes"""

            def _sum(self, code, from_date, to_date=None):
                if to_date is None:
                    to_date = fields.Date.today()
                self.env.cr.execute(
                    """
                    SELECT sum(number_of_days) as number_of_days, sum(number_of_hours) as number_of_hours
                    FROM hr_payslip as hp, hr_payslip_worked_days as pi
                    WHERE hp.employee_id = %s AND hp.state = 'done'
                    AND hp.date_from >= %s AND hp.date_to <= %s AND hp.id = pi.payslip_id AND pi.code = %s""",
                    (self.employee_id, from_date, to_date, code),
                )
                return self.env.cr.fetchone()

            def sum(self, code, from_date, to_date=None):
                res = self._sum(code, from_date, to_date)
                return res and res[0] or 0.0

            def sum_hours(self, code, from_date, to_date=None):
                res = self._sum(code, from_date, to_date)
                return res and res[1] or 0.0

        class Payslips(BrowsableObject):
            """a class that will be used into the python code, mainly for usability purposes"""

            def sum(self, code, from_date, to_date=None):
                if to_date is None:
                    to_date = fields.Date.today()
                self.env.cr.execute(
                    """SELECT sum(case when hp.credit_note = False then (pl.total) else (-pl.total) end)
                            FROM hr_payslip as hp, hr_payslip_line as pl
                            WHERE hp.employee_id = %s AND hp.state = 'done'
                            AND hp.date_from >= %s AND hp.date_to <= %s AND hp.id = pl.slip_id AND pl.code = %s""",
                    (self.employee_id, from_date, to_date, code),
                )
                res = self.env.cr.fetchone()
                return res and res[0] or 0.0

        # we keep a dict with the result because a value can be overwritten by another rule with the same code
        result_dict = {}
        rules_dict = {}
        worked_days_dict = {}
        inputs_dict = {}
        blacklist = []
        payslip = self.env["hr.payslip"].browse(payslip_id)
        for worked_days_line in payslip.worked_days_line_ids:
            worked_days_dict[worked_days_line.code] = worked_days_line
        for input_line in payslip.input_line_ids:
            inputs_dict[input_line.code] = input_line

        categories = BrowsableObject(payslip.employee_id.id, {}, self.env)
        inputs = InputLine(payslip.employee_id.id, inputs_dict, self.env)
        worked_days = WorkedDays(payslip.employee_id.id, worked_days_dict, self.env)
        payslips = Payslips(payslip.employee_id.id, payslip, self.env)
        rules = BrowsableObject(payslip.employee_id.id, rules_dict, self.env)

        baselocaldict = {
            "categories": categories,
            "rules": rules,
            "payslip": payslips,
            "worked_days": worked_days,
            "inputs": inputs,
        }
        # get the ids of the structures on the contracts and their parent id as well
        contracts = self.env["hr.contract"].browse(contract_ids)
        if len(contracts) == 1 and payslip.struct_id:
            structure_ids = list(set(payslip.struct_id._get_parent_structure().ids))
        else:
            structure_ids = contracts.get_all_structures()
        # get the rules of the structure and thier children
        rule_ids = (
            self.env["hr.payroll.structure"].browse(structure_ids).get_all_rules()
        )
        # run the rules by sequence
        sorted_rule_ids = [id for id, sequence in sorted(rule_ids, key=lambda x: x[1])]
        sorted_rules = self.env["hr.salary.rule"].browse(sorted_rule_ids)

        for contract in contracts:
            employee = contract.employee_id
            localdict = dict(baselocaldict, employee=employee, contract=contract)
            for rule in sorted_rules:
                localdict["result"] = None  # amount
                localdict["result_qty"] = 1.0
                localdict["result_rate"] = 100
                localdict["result_analytic"] = None
                localdict["result_name"] = None
                localdict["result_list"] = None
                # check if the rule can be applied
                if rule._satisfy_condition(localdict) and rule.id not in blacklist:
                    # compute values for the payslip_line(s) of the rule
                    payslip_lines = rule._compute_rule(localdict)
                    for payslip_line in payslip_lines:
                        amount = payslip_line["result"]
                        qty = payslip_line.get("result_qty") or 1.0
                        rate = payslip_line.get("result_rate") or 100.0
                        analytic_account_id = (
                            payslip_line.get("result_analytic") or False
                        )
                        name = payslip_line.get("result_name") or rule.name

                        key = (
                            rule.code
                            + "-"
                            + str(contract.id)
                            + "-"
                            + str(analytic_account_id)
                        )
                        code_analytic = rule.code + "-" + str(analytic_account_id)
                        # check if there is already a rule computed with that code
                        previous_amount = (
                            code_analytic in localdict
                            and localdict[code_analytic]
                            or 0.0
                        )
                        # set/overwrite the amount computed for this rule in the localdict
                        tot_rule = amount * qty * rate / 100.0
                        localdict[code_analytic] = tot_rule
                        rules_dict[code_analytic] = rule
                        # sum the amount for its salary category
                        localdict = _sum_salary_rule_category(
                            localdict, rule.category_id, tot_rule - previous_amount
                        )
                        # create/overwrite the rule in the temporary results
                        result_dict[key] = {
                            "salary_rule_id": rule.id,
                            "contract_id": contract.id,
                            "analytic_account_id": analytic_account_id,
                            "name": name,
                            "code": rule.code,
                            "category_id": rule.category_id.id,
                            "sequence": rule.sequence,
                            "appears_on_payslip": rule.appears_on_payslip,
                            "condition_select": rule.condition_select,
                            "condition_python": rule.condition_python,
                            "condition_range": rule.condition_range,
                            "condition_range_min": rule.condition_range_min,
                            "condition_range_max": rule.condition_range_max,
                            "amount_select": rule.amount_select,
                            "amount_fix": rule.amount_fix,
                            "amount_python_compute": rule.amount_python_compute,
                            "amount_percentage": rule.amount_percentage,
                            "amount_percentage_base": rule.amount_percentage_base,
                            "register_id": rule.register_id.id,
                            "amount": amount,
                            "employee_id": contract.employee_id.id,
                            "quantity": qty,
                            "rate": rate,
                        }
                else:
                    # blacklist this rule and its children
                    blacklist += [id for id, seq in rule._recursive_search_of_rules()]

        return list(result_dict.values())
