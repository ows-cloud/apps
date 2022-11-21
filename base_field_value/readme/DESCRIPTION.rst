# IMPLEMENTATION EXAMPLE
# field_value_ids must have copy=True, otherwise the field_value is moved from the original to the new record.

.. code-block:: python

    class ResCompany(models.Model):
        _inherit = 'res.company'

        @api.model
        def _compute_default_field_value_ids(self):
            result = []
            records = self.env['res.field'].search([('model','=','res.company'),('auto_create','=',True),
                '|',('country_id','=',False),('country_id','=',self.env.company.partner_id.country_id.id)])
            for record in records:
                result.append((0, 0, {'model': 'res.company', 'company_id': self.env.company.id,
                    'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
            return result

        field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
            domain=[('model','=','res.company')], copy=True)

    class ResUsers(models.Model):
        _inherit = 'res.users'

        @api.model
        def _compute_default_field_value_ids(self):
            result = []
            records = self.env['res.field'].search([('model','=','res.users'),('auto_create','=',True),
                '|',('country_id','=',False),('country_id','=',self.env.company.partner_id.country_id.id)])
            for record in records:
                result.append((0, 0, {'model': 'res.users', 'company_id': self.env.company.id,
                    'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
            return result

        field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
            domain=[('model','=','res.users')], copy=True)
