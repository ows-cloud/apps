from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval

class HrContract(models.Model):
    _inherit = 'hr.contract'

    qty_rate_amount_ids = fields.One2many('hr.rule.qty_rate_amount', 'res_id', string='Recurring Salary',
                                          domain=[('model', '=', 'hr.contract')], context={'default_model': 'hr.contract'}, copy=True)


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    qty_rate_amount_ids = fields.One2many('hr.rule.qty_rate_amount', 'res_id', string='Quantity Rate Amount',
                                          domain=[('model', '=', 'hr.payslip')], context={'default_model': 'hr.payslip'}, copy=True)


class HrRuleQtyRateAmount(models.Model):
    _name = 'hr.rule.qty_rate_amount'

    salary_rule_id = fields.Many2one('hr.salary.rule', string="Salary Rule", ondelete='restrict')
    quantity = fields.Float(default=1.0)
    rate = fields.Float("Rate (%)", default=100.0)
    amount = fields.Float()
    total = fields.Float(compute='_compute_total')
    model = fields.Char(required=True, readonly=True, index=True)
    res_id = fields.Integer(required=True, readonly=True, index=True, ondelete='''Should NOT be 'cascade', see the write method''')
    company_id = fields.Many2one('res.company', string='Company', required=True, store=True, index=True, default=lambda self: self.env.user.company_id)

    @api.depends('quantity', 'rate', 'amount')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.quantity * rec.rate / 100 * rec.amount

    @api.multi
    def write(self, values):
        '''
        SOURCE: base_field_value
        For models where field_value_ids = fields.One2many('res.field.value', 'res_id'):
        The model assumes that res.field.value 'res_id' has a Many2one relationship to the model.
        When the model imports a new record (with csv/xml),
        it will enforce that the new record.id does not exist in res.field.value 'res_id',
        or give a ParseError if 'res_id' has no attribute 'ondelete'.
        See https://github.com/odoo/odoo/blob/10.0/odoo/fields.py#L2246
                    if inverse_field.ondelete == 'cascade':
                        comodel.search(domain).unlink()
                    else:
                        comodel.search(domain).write({inverse: False})
        res.field.value has records relating to many models, and the 'res_id' should not be changed!
        '''

        if 'res_id' in values and values['res_id'] == False:
            values.pop('res_id')
        return super(HrRuleQtyRateAmount, self).write(values)


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    qty_rate_amount_from = fields.Selection([('hr.contract', 'Contract'), ('hr.payslip', 'Payslip')], string="Salary Rule input from")

    condition_python = fields.Text(default='''
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

                    result = rules.NET > categories.NET * 0.10''')

    amount_python_compute = fields.Text(default='''
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

    # compute_rule() should have access to self.id
    # + localdict['rule'] = self
    # TODO should add some checks on the type of result (should be float)
    @api.multi
    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the environement in which to compute the rule
        :return: returns a tuple build as the base/amount computed, the quantity and the rate
        :rtype: (float, float, float)
        """
        self.ensure_one()
        if self.amount_select == 'fix':
            try:
                return self.amount_fix, float(safe_eval(self.quantity, localdict)), 100.0
            except:
                raise UserError(_('Wrong quantity defined for salary rule %s (%s).') % (self.name, self.code))
        elif self.amount_select == 'percentage':
            try:
                return (float(safe_eval(self.amount_percentage_base, localdict)),
                        float(safe_eval(self.quantity, localdict)),
                        self.amount_percentage)
            except:
                raise UserError(_('Wrong percentage base or quantity defined for salary rule %s (%s).') % (self.name, self.code))
        else:
            try:
                localdict['rule'] = self
                safe_eval(self.amount_python_compute, localdict, mode='exec', nocopy=True)
                return float(localdict['result']), 'result_qty' in localdict and localdict['result_qty'] or 1.0, 'result_rate' in localdict and localdict['result_rate'] or 100.0
            except:
                raise UserError(_('Wrong python code defined for salary rule %s (%s).') % (self.name, self.code))

    # satisfy_condition() should have access to self.id
    # + localdict['rule'] = self
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
