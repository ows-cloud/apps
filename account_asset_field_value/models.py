from odoo import models, fields, api

class AccountAsset(models.Model):
    _inherit = "account.asset"

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'account.asset'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False),
                                                ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'account.asset', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value,
                                  'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields',
                                      default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'account.asset')],
                                      context={'default_model': 'account.asset'}, copy=True)
