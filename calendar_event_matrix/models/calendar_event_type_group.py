from datetime import datetime
from odoo import _, api, fields, models


class CalendarEventDate(models.Model):
    _name = 'calendar.event.type.group'
    _description = 'calendar.event.type.group'

    name = fields.Char()
    date = fields.Date("Date to add")
    type_ids = fields.One2many('calendar.event.type', 'group_id', string="Types")
    line_ids = fields.Many2many('calendar.event')

    def add_date(self):
        self.line_ids = self._default_line_ids(add_date=self.date)

    def remove_date(self):
        self.write({'line_ids': [
            (2, calendar_event.id) for calendar_event in self.line_ids if calendar_event.start_date == self.date
        ]})

    def show_from_date(self):
        self.line_ids = self._default_line_ids(show_from_date=self.date)

    def reload(self):
        self.line_ids = self._default_line_ids()

    def _default_line_ids(self, add_date=None, show_from_date=None):
        """take care that the widget gets records passed for every combination
        of calendar.event.type and start_date involved"""

        # required: name, privacy, show_as, start, stop
        
        calendar_events = self.env['calendar.event'].search([('categ_ids', 'in', self.type_ids.ids)])
        calendar_event_dates = calendar_events.mapped('start_date')
        if add_date:
            calendar_event_dates.append(add_date)
        if not show_from_date:
            show_from_date = datetime(2000, 1, 1).date()
        result = [(5, 0, 0)] + [
            (0, 0, {
                'name': "{} on {}".format(calendar_event_type.name, str(calendar_event_date)),
                'categ_ids': [(4, calendar_event_type.id)],
                'start_date': calendar_event_date,
                'stop_date': calendar_event_date,
                'start': calendar_event_date,
                'stop': calendar_event_date,
                'privacy': 'public',
                'show_as': 'busy',
                'partner_ids': [],
            })
            # if there isn't a calendar.event record for the calendar.event.type on the date, create a new one
            if not calendar_events.filtered(lambda x: x.categ_ids == calendar_event_type and x.start_date == calendar_event_date) else
            # otherwise, return the line
            (4, calendar_events.filtered(lambda x: x.categ_ids == calendar_event_type and x.start_date == calendar_event_date)[0].id)
            # loop
            for calendar_event_type in self.type_ids
            for calendar_event_date in calendar_event_dates
            if calendar_event_date >= show_from_date
        ]
        return result