from datetime import date, datetime, timedelta
from odoo import _, api, fields, models
from odoo.exceptions import UserError

def get_datetime(d):
    # d: date or datetime
    # delta: timedelta
    if type(d) is date:
        dt = datetime.combine(d, datetime.min.time())
    elif type(d) is datetime.datetime:
        dt = d
    else:
        raise
    return dt


class CalendarEventMatrix(models.Model):
    _name = 'calendar.event.matrix'
    _description = 'Calendar Event Matrix'

    name = fields.Char()
    date_from = fields.Date("Show From Date", default=datetime.now().date())
    date_to = fields.Date("Show To Date")
    date_action = fields.Date("Add Date", default=datetime.now().date())
    row_ids = fields.One2many('calendar.event.matrix.row', 'matrix_id', string="Types")
    event_ids = fields.Many2many('calendar.event')
    partner_ids = fields.Many2many('res.partner')
    matrix_partner_id = fields.Many2one(
        "res.partner",
        "Matrix Partner",
        required=True,
        default=lambda self: self.env.user.partner_id,
        help="Attend/unattend calendar events for this partner.",
    )

    def add_date(self):
        self.event_ids = self._default_event_ids(add_date=self.date_action)

    def remove_date(self):
        self.write({'event_ids': [
            (2, calendar_event.id)
            for calendar_event in self.event_ids
            if calendar_event.start_date == self.date_action or calendar_event.start.date() == self.date_action
        ]})
        self.event_ids = self._default_event_ids()

    def show_matrix(self):
        self.event_ids = self._default_event_ids(date_from=self.date_from, date_to=self.date_to)
        view_ref = self.env.context.get("view_ref")
        view = self.env.ref(view_ref)
        return {
            "type": "ir.actions.act_window",
            "res_model": "calendar.event.matrix",
            "views": [[view.id, "form"]],
            "res_id": self.id,
            "context": {"form_view_initial_mode": "edit"},
        }

    def _default_event_ids(self, add_date=None, date_from=None, date_to=None):
        """take care that the widget gets records passed for every combination
        of calendar.event.matrix.row and start/start_date involved"""

        # required: name, privacy, show_as, start, stop

        if not date_from:
            date_from = datetime(2000, 1, 1).date()
        if not date_to:
            date_to = datetime(2099, 1, 1).date()
        calendar_events = self.env['calendar.event'].search(
            [
                ('matrix_row_id', 'in', self.row_ids.ids),
                '|', 
                ('start', '>=', date_from),
                ('start_date', '>=', str(date_from)),
                '|', 
                ('stop', '<=', date_to),
                ('stop_date', '<=', str(date_to)),
            ]
        )
        calendar_event_dates_str = calendar_events.mapped('start_date_str')
        calendar_event_dates = {datetime.strptime(s, '%Y-%m-%d').date() for s in calendar_event_dates_str}

        if add_date:
            if add_date < date_from:
                raise UserError("Date cannot be smaller than date_from")
            if add_date > date_to:
                raise UserError("Date cannot be greater than date_to")
            if add_date in calendar_event_dates:
                raise UserError("Date already exists")

            calendar_event_dates.add(add_date)

        result = []
        for matrix_date in calendar_event_dates:
            for matrix_row in self.row_ids:
                allday = matrix_row.allday
                if allday:
                    ce = calendar_events.filtered(lambda x: x.matrix_row_id == matrix_row and x.start_date == matrix_date)
                else:
                    # TODO: get hours from timezone
                    ce = calendar_events.filtered(lambda x: x.matrix_row_id == matrix_row and (x.start + timedelta(hours=2)).date() == matrix_date)
                if ce:
                    result.append((4, ce.ensure_one().id))
                else:
                    dict = {
                        'name': "{}".format(matrix_row.name),
                        'matrix_row_id': matrix_row.id,
                        'privacy': 'public',
                        'show_as': 'busy',
                        'partner_ids': [],
                    }
                    if allday:
                        dict["allday"] = True
                        dict["start_date"] = matrix_date
                        dict["stop_date"] = matrix_date
                    else:
                        dict["allday"] = False
                        # TODO: get hours from timezone
                        start_day = -1 if matrix_row.default_start.hour >=22 else 0
                        dict["start"] = get_datetime(matrix_date) + timedelta(
                            days=start_day,
                            hours=matrix_row.default_start.hour,
                            minutes=matrix_row.default_start.minute,
                            seconds=matrix_row.default_start.second,
                        )
                        stop_day = -1 if matrix_row.default_stop.hour >= 22 else 0
                        dict["stop"] = get_datetime(matrix_date) + timedelta(
                            days=stop_day,
                            hours=matrix_row.default_stop.hour,
                            minutes=matrix_row.default_stop.minute,
                            seconds=matrix_row.default_stop.second,
                        )
                        if dict["stop"] < dict["start"]:
                            dict["stop"] = dict["stop"] + timedelta(days=1)
                    result.append((0, 0, dict))

        return [(5, 0, 0)] + result

    # def create(self, values):
    #     super(CalendarEventMatrix, self).create(values)
    #     if "partner_ids" in values:
    #         self._update_partner_ids(values["partner_ids"][0][2])

    # def write(self, values):
    #     super(CalendarEventMatrix, self).write(values)
    #     if "partner_ids" in values:
    #         self._update_partner_ids(values["partner_ids"][0][2])

    # def _update_partner_ids(self, partner_ids):
    #     """ remove partner not implemented """
    #     self.ensure_one()
    #     for row in self.row_ids:
    #         if row.default_all_matrix_partners:
    #             # search for calendar.event with this row without the partners
    #             calendar_events = self.env["calendar.event"].search([("matrix_row_id", "=", row.id)])
    #             for ce in calendar_events:
    #                 todo = "add partners"