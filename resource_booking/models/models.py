# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    employee_ids = fields.Many2many('hr.employee', 'product_template_hr_employee_rel', 'product_template_id', 'hr_employee_id', string="Employees")
    resource_ids = fields.Many2many('resource.resource', 'product_template_resource_resource_rel', 'product_template_id', 'resource_resource_id', string="Resources")

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    product_ids = fields.Many2many('product.template', 'product_template_hr_employee_rel', 'hr_employee_id', 'product_template_id', string="Products")
    
class ResourceResource(models.Model):
    _inherit = 'resource.resource'
    
    resource_type = fields.Selection(selection_add=[('other', "Other")])
    product_ids = fields.Many2many('product.template', 'product_template_resource_resource_rel', 'resource_resource_id', 'product_template_id', string="Products")
    
class BookingTime(models.Model):
    _name = 'booking.time'
    _order = 'sequence'
    
    name = fields.Char("Name")
    time = fields.Float("Time")
    sequence = fields.Integer("Sequence")
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.context.get('default_company_id') or self.env.user.company_id)

    def name_get(self):
        booking_id = self.env.context.get('booking_id', None)
        if booking_id:
            result = []
            booking = self.env['booking.booking'].browse(booking_id)
            availability = booking.get_availability(self)
            for time, employees, resources in availability:
                e = len(employees)
                r = len(resources)
                name = "%s (%s %s, %s %s)" % (time.name, e, "employee" if e == 1 else "employees", r, "resource" if r == 1 else "resources")
                result.append((time.id, name))
            return result
        else:
            return super(BookingTime, self).name_get()
        

class BookingBooking(models.Model):
    _name = 'booking.booking'
    
    partner_id = fields.Many2one('res.partner', "Patient", required=True)
    product_id = fields.Many2one('product.template', "Service", required=True, domain=['|', ['employee_ids', '!=', False], ['resource_ids', '!=', False]])
    employee_id = fields.Many2one('hr.employee', "Responsible")
    employee_user_id = fields.Many2one('res.users', "Responsible User", related='employee_id.user_id')
    resource_id = fields.Many2one('resource.resource', "Resource")
    date = fields.Date("Date", required=True)
    time_id = fields.Many2one('booking.time', "Time")
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.context.get('default_company_id') or self.env.user.company_id)
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, str(record.id)))
        return result
    
    def schedule_time(self):
        context = dict(self.env.context)
        context['booking_date'] = self.date
        context['booking_product_id'] = self.product_id.id
        view_id = self.env.ref('resource_booking.view_booking_form2').id
        return {
            "type": "ir.actions.act_window",
            "res_model": "booking.booking",
            "views": [[view_id, "form"]],
            "res_id": self.id,
            "context": context,
            'target': 'new',
        }
        
    @api.onchange('time_id')
    def update_employee_and_resource(self):
        if self.time_id:
            time, employees, resources = self.get_availability(self.time_id)[0]
            employee_domain = [('id', 'in', list(employees))]
            resource_domain = [('id', 'in', list(resources))]
            return {'domain': {'employee_id': employee_domain, 'resource_id': resource_domain},
                    'value': {'employee_id': None, 'resource_id': None},
            }
        
    def get_availability(self, times):
        self.ensure_one()
        result = []
        product = self.product_id
        employees_list = [emp.id for emp in product.employee_ids]
        resources_list = [res.id for res in product.resource_ids]
        _logger.debug("self.id: %s, self.env.context: %s, self.__dict__: %s" % (self.id, self.env.context, self.__dict__))
        for time in times:
            id = self.env.context.get('active_id', False) or self.id
            booking_domain = [('id','!=',id), ('date','=',self.date), ('time_id','=',time.id), '|', ('employee_id','in',employees_list), ('resource_id','in',resources_list)]
            bookings = self.search(booking_domain)
            employees = set(employees_list)
            resources = set(resources_list)
            for booking in bookings:
                #_logger.debug("booking.employee_id: %s, booking.resource_id: %s, booking_domain: %s, bookings: %s" % (booking.employee_id, booking.resource_id, booking_domain, bookings))
                if booking.employee_id and booking.employee_id.id in employees:
                    employees.remove(booking.employee_id.id)
                if booking.resource_id and booking.resource_id.id in resources:
                    resources.remove(booking.resource_id.id)
            result.append((time, employees, resources))
        return result
