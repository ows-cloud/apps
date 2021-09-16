# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class RersourceBookingMatrixWizard(models.TransientModel):
    _name = 'resource.booking.matrix.wizard'
    _description = 'Resource Booking Matrix Wizard'

    name = fields.Char()

    line_ids = fields.Many2many(
        'resource.booking', default=lambda self: self._default_line_ids())

    def _default_line_ids(self):
        """take care that the widget gets records passed for every combination
        of x2m.demo and res.users involved"""
        
        resource_bookings = self.env['resource.booking'].search([])
        resource_booking_dates = resource_bookings.mapped('start_date')
        resource_booking_types = self.env['resource.booking.type'].search([])
        return [
            (0, 0, {
                'name': "{} on {}".format(type.name, 'date'),
                'type_id': resource_booking_type.id,
                'date': resource_booking_date,
            })
            # if there isn't a resource.booking record for the resource.booking.type on the date, create a new one
            if not resource_bookings.filtered(lambda x: x.type_id == resource_booking_type and x.start_date == resource_booking_date) else
            # otherwise, return the line
            (4, resource_bookings.filtered(lambda x: x.type_id == resource_booking_type and x.start_date == resource_booking_date)[0].id)
            # loop
            for resource_booking_type in resource_booking_types
            for resource_booking_date in resource_booking_dates
        ]

    @api.multi
    def _open_matrix(self):
        wiz = self.create({})
        view_id = self.env.ref('resource_booking_matrix.view_resource_booking_matrix_wizard').id
        return {
            'name': 'Resource Booking Matrix',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'resource.booking.matrix.wizard',
            'target': 'new',
            'res_id': wiz.id,
            'view_id': view_id,
            'context': self.env.context,
        }
