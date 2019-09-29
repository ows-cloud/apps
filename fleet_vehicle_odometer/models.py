from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class fleet_service_type(models.Model):
    _inherit = 'fleet.service.type'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle(models.Model):
    _inherit = 'fleet.vehicle'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_cost(models.Model):
    _inherit = 'fleet.vehicle.cost'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_contract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_fuel(models.Model):
    _inherit = 'fleet.vehicle.log.fuel'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_log_services(models.Model):
    _inherit = 'fleet.vehicle.log.services'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_model(models.Model):
    _inherit = 'fleet.vehicle.model'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_model_brand(models.Model):
    _inherit = 'fleet.vehicle.model.brand'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_odometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    comment = fields.Char('Comment')
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
    distance = fields.Integer('Distance')
    
    @api.model
    def create(self, values):
        self._recompute_distance_before_create(values)
        return super(fleet_vehicle_odometer, self).create(values)
        
    def _recompute_distance_before_create(self, values, record_id=0):
        below = self.search([('vehicle_id', '=', values['vehicle_id']), ('value', '<', values['value']), ('id', '!=', record_id)],
                            order='value desc', limit=1)
        above = self.search([('vehicle_id', '=', values['vehicle_id']), ('value', '>', values['value']), ('id', '!=', record_id)],
                            order='value', limit=1)

        if below and below.date > values['date']:
            raise UserError("Date should not be lower than %s." % str(below.date))
        if above and above.date < values['date']:
            raise UserError("Date should not be higher than %s." % str(above.date))

        if below:
            values['distance'] = values['value'] - below.value
        else:
            values['distance'] = 0
        if above:
            above.distance = above.value - values['value']

    @api.multi
    def unlink(self):
        for record in self:

            record._recompute_distance_before_unlink()
            return super(fleet_vehicle_odometer, self).unlink()
            
    def _recompute_distance_before_unlink(self):
        below = self.search([('vehicle_id', '=', self.vehicle_id.id), ('value', '<', self.value)],
                            order='value desc', limit=1)
        above = self.search([('vehicle_id', '=', self.vehicle_id.id), ('value', '>', self.value)],
                            order='value', limit=1)

        if below and above:
            above.distance = above.value - below.value
        elif above:
            above.distance = None

    @api.multi
    def write(self, values):

        recompute_distance = False
        for value in values:
            if value in ('date', 'vehicle_id', 'value'):
                recompute_distance = True
        if recompute_distance:
            for record in self:
                record._recompute_distance_before_unlink()
                values['date'] = values.get('date') or record.date
                values['vehicle_id'] = values.get('vehicle_id') or record.vehicle_id.id
                values['value'] = values.get('value') or record.value
                record._recompute_distance_before_create(values, record.id)
        
        return super(fleet_vehicle_odometer, self).write(values)
    

class fleet_vehicle_state(models.Model):
    _inherit = 'fleet.vehicle.state'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

class fleet_vehicle_tag(models.Model):
    _inherit = 'fleet.vehicle.tag'
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)

