# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, fields


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    def _default_start_date(self):
        for record in self:
            # look for date, or create date
            date = record.start.date()

            record.start_date = 

    start_date = fields.Many2one('calendar.event.date', default='_default_start_date')


class CalendarEventDate(models.Model):
    _name = 'calendar.event.date'
    _description = 'calendar.event.date'
    

    date = fields.Date()

    # Ulike arrangementer (sabbat og middagsseminar) trenger ulike ansvarsområder.
    # calendar.event.type (sabbatsskole / middagsansvar)
    # calendar.event.type.group (sabbat / middagsseminar)
    # calendar.event.date