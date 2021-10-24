from odoo import api, fields, models, _


class HrRuleQtyRateAmount(models.Model):
    _name = 'hr.rule.qty_rate_amount'
    _description = 'hr.rule.qty_rate_amount'

    salary_rule_id = fields.Many2one('hr.salary.rule', string="Salary Rule", ondelete='restrict')
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account", ondelete='restrict')
    quantity = fields.Float(default=1.0)
    rate = fields.Float("Rate (%)", default=100.0)
    amount = fields.Float()
    total = fields.Float(compute='_compute_total')
    model = fields.Char(required=True, readonly=True, index=True)
    res_id = fields.Integer(required=True, readonly=True, index=True,
                            ondelete='''Should NOT be 'cascade', see the write method''')
    company_id = fields.Many2one('res.company', string='Company', required=True, store=True, index=True,
                                 default=lambda self: self.env.company)

    def _valid_field_parameter(self, field, name):
        return name == 'ondelete' or super()._valid_field_parameter(field, name)

    @api.depends('quantity', 'rate', 'amount')
    def _compute_total(self):
        for rec in self:
            rec.total = rec.quantity * rec.rate / 100 * rec.amount

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
