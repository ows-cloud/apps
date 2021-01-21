from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')
    qty_rate_amount_from = fields.Selection([('hr.contract', 'Contract'), ('hr.payslip', 'Payslip')],
                                            string="Salary Rule input from")
    condition_python = fields.Text(string='Python Condition', required=True,
        default='''
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

                    result = rules.NET > categories.NET * 0.10''',
        help='Applied this rule for calculation if condition is true. You can specify condition like basic > 1000.')
    amount_python_compute = fields.Text(string='Python Code',
        default='''
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

                    result = contract.wage * 0.10''')

    #TODO should add some checks on the type of result (should be float)
    @api.multi
    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the environement in which to compute the rule
        :return: returns a tuple build as the base/amount computed, the quantity and the rate
        :rtype: [(amount float, quantity float, rate float, analytic_account_id integer/False)]
        """
        self.ensure_one()
        if self.amount_select == 'fix':
            try:
                return [(self.amount_fix, float(safe_eval(self.quantity, localdict)), 100.0, False)]
            except:
                raise UserError(_('Wrong quantity defined for salary rule %s (%s).') % (self.name, self.code))
        elif self.amount_select == 'percentage':
            try:
                return [(float(safe_eval(self.amount_percentage_base, localdict)),
                         float(safe_eval(self.quantity, localdict)),
                         self.amount_percentage,
                         False)]
            except:
                raise UserError(_('Wrong percentage base or quantity defined for salary rule %s (%s).') % (self.name, self.code))
        else:
            try:
                localdict['rule'] = self
                safe_eval(self.amount_python_compute, localdict, mode='exec', nocopy=True)
                if localdict['result_list']:
                    return localdict['result_list']
                else:
                    return [(float(localdict['result']), \
                        'result_qty' in localdict and localdict['result_qty'] or 1.0, \
                        'result_rate' in localdict and localdict['result_rate'] or 100.0, \
                        'result_analytic' in localdict and localdict['result_analytic'] or False
                    )]
            except:
                raise UserError(_('Wrong python code defined for salary rule %s (%s).') % (self.name, self.code))

    @api.multi
    def _satisfy_condition(self, localdict):
        """
        @param contract_id: id of hr.contract to be tested
        @return: returns True if the given rule match the condition for the given contract. Return False otherwise.
        """
        self.ensure_one()

        if self.condition_select == 'none':
            return True
        elif self.condition_select == 'range':
            try:
                result = safe_eval(self.condition_range, localdict)
                return self.condition_range_min <= result and result <= self.condition_range_max or False
            except:
                raise UserError(_('Wrong range condition defined for salary rule %s (%s).') % (self.name, self.code))
        else:  # python code
            try:
                localdict['rule'] = self
                safe_eval(self.condition_python, localdict, mode='exec', nocopy=True)
                return 'result' in localdict and localdict['result'] or False
            except:
                raise UserError(_('Wrong python condition defined for salary rule %s (%s).') % (self.name, self.code))
