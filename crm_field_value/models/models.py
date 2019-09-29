from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'res.partner'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'res.partner', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'res.partner')], context={'default_model': 'res.partner'}, copy=True)
