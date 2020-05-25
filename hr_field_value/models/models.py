from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.contract'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.contract', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.contract')], context={'default_model': 'hr.contract'}, copy=True)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.employee'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.employee', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.employee')], context={'default_model': 'hr.employee'}, copy=True)


class HrJob(models.Model):
    _inherit = 'hr.job'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.job'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.job', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.job')], context={'default_model': 'hr.job'}, copy=True)


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.leave.type'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.leave.type', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.leave.type')], context={'default_model': 'hr.leave.type'}, copy=True)


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.payslip'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.payslip', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.payslip')], context={'default_model': 'hr.payslip'}, copy=True)


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'hr.salary.rule'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'hr.salary.rule', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                      domain=[('model', '=', 'hr.salary.rule')], context={'default_model': 'hr.salary.rule'}, copy=True)


class ResCompany(models.Model):
    _inherit = 'res.company'

    @api.model
    def _compute_default_field_value_ids(self):
        result = []
        records = self.env['res.field'].search([('model', '=', 'res.company'), ('auto_create', '=', True),
                                                '|', ('country_id', '=', False), ('country_id', '=', self.env.user.company_id.country_id.id)])
        for record in records:
            result.append((0, 0, {'model': 'res.company', 'company_id': self.env.user.company_id.id,
                                  'field_id': record.id, 'value': record.default_value, 'field_data_type': record.data_type}))
        return result

    field_value_hr_ids = fields.One2many('res.field.value', 'res_id', string='Fields', default=_compute_default_field_value_ids,
                                         domain=[('model', '=', 'res.company'), ('field_app', '=like', 'hr%')], context={'default_model': 'res.company', 'default_field_app': 'hr'}, copy=True)
