from datetime import date, datetime, timedelta

from odoo import _, fields, models
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
    _name = "calendar.event.matrix"
    _description = "Calendar Event Matrix"

    name = fields.Char()
    date_from = fields.Date("Show From Date", default=datetime.now().date())
    date_to = fields.Date("Show To Date")
    date_action = fields.Date("Add Date", default=datetime.now().date())
    row_ids = fields.One2many("calendar.event.matrix.row", "matrix_id", string="Types")
    event_ids = fields.One2many("calendar.event", "matrix_id", string="Events")
    # event_ids = fields.Many2many("calendar.event", string="DEPRECATED", relation="event_ids_deprecated")
    show_in_matrix_event_ids = fields.Many2many("calendar.event")
    partner_ids = fields.Many2many(
        "res.partner",
        relation="matrix_partner_rel",
        column1="matrix_id",
        column2="partner_id",
    )
    matrix_partner_id = fields.Many2one(
        "res.partner",
        "Matrix Partner",
        required=True,
        default=lambda self: self.env.user.partner_id,
        help="Attend/unattend calendar events for this partner.",
    )

    def add_date(self):
        self._create_event_ids(add_date=self.date_action)

    def remove_date(self):
        for matrix in self:
            events = self.env["calendar.event"].search(
                [
                    ("matrix_id", "=", matrix.id),
                    ('start', '>=', matrix.date_action),
                    ('start', '<', (matrix.date_action + timedelta(days=1))),
                ]
            )
            events.unlink()

    def show_matrix(self):
        self.ensure_one()
        self._create_event_ids(
            date_from=self.date_from, date_to=self.date_to
        )
        event_ids = self.env["calendar.event"].search(
            [("matrix_row_id.matrix_id", "=", self.id)]
        )
        event_ids.update_parent_id()
        event_ids._update_allow_to_sign_up()
        view_ref = self.env.context.get("view_ref")
        view = self.env.ref(view_ref)
        return {
            "type": "ir.actions.act_window",
            "res_model": "calendar.event.matrix",
            "views": [[view.id, "form"]],
            "res_id": self.id,
            "context": {"form_view_initial_mode": "edit"},
        }

    def _create_event_ids(self, add_date=None, date_from=None, date_to=None):
        """
        (1) Create (if missing) a calendar.event for each combination of
            calendar.event.matrix.row and start/start_date.

        (2) Return the calendar events of the matrix rows which should show_in_matrix.

        More info: https://github.com/OCA/web/tree/16.0/web_widget_x2many_2d_matrix
        """
        # required: name, privacy, show_as, start, stop

        self.ensure_one()
        if not date_from:
            date_from = datetime(2000, 1, 1).date()
        if not date_to:
            date_to = datetime(2099, 1, 1).date()

        calendar_events = self.env["calendar.event"].with_context(
            active_test=False
        ).search(
            [
                ("matrix_row_id", "in", self.row_ids.ids),
                "|",
                ("start", ">=", date_from),
                ("start_date", ">=", str(date_from)),
                "|",
                ("stop", "<=", date_to),
                ("stop_date", "<=", str(date_to)),
            ]
        )
        calendar_events.filtered(lambda ce: not ce.active).active = True
        calendar_event_dates_str = calendar_events.mapped("start_date_str")
        calendar_event_dates = {
            datetime.strptime(s, "%Y-%m-%d").date() for s in calendar_event_dates_str
        }

        if add_date:
            if add_date < date_from:
                raise UserError(_("Date cannot be smaller than date_from"))
            if add_date > date_to:
                raise UserError(_("Date cannot be greater than date_to"))
            if add_date in calendar_event_dates:
                raise UserError(_("Date already exists"))

            calendar_event_dates.add(add_date)

        to_create = []
        to_show = []
        for matrix_date in calendar_event_dates:
            for matrix_row in self.row_ids:
                # EXISTS
                allday = matrix_row.allday
                if allday:
                    ce = calendar_events.filtered(
                        lambda ce: ce.matrix_row_id == matrix_row
                        and ce.start_date == matrix_date
                    )
                else:
                    # TODO: get hours from timezone
                    ce = calendar_events.filtered(
                        lambda ce: ce.matrix_row_id == matrix_row
                        and (ce.start + timedelta(hours=2)).date() == matrix_date
                    )
                if ce:
                    if ce.visible_matrix_row_id:
                        to_show.append((4, ce.ensure_one().id))
                # CREATE
                else:
                    my_dict = {
                        "name": "{}".format(matrix_row.name),
                        "matrix_id": self.id,
                        "matrix_row_id": matrix_row.id,
                        "privacy": "public",
                        "show_as": "busy",
                        "partner_ids": [],
                    }
                    if matrix_row.add_company_partner:
                        my_dict["partner_ids"] = [(4, self.env.company.partner_id.id)]
                    if allday:
                        my_dict["allday"] = True
                        my_dict["start_date"] = matrix_date
                        my_dict["stop_date"] = matrix_date
                    else:
                        my_dict["allday"] = False
                        # TODO: get hours from timezone
                        start_day = -1 if matrix_row.default_start.hour >= 22 else 0
                        my_dict["start"] = get_datetime(matrix_date) + timedelta(
                            days=start_day,
                            hours=matrix_row.default_start.hour,
                            minutes=matrix_row.default_start.minute,
                            seconds=matrix_row.default_start.second,
                        )
                        stop_day = -1 if matrix_row.default_stop.hour >= 22 else 0
                        my_dict["stop"] = get_datetime(matrix_date) + timedelta(
                            days=stop_day,
                            hours=matrix_row.default_stop.hour,
                            minutes=matrix_row.default_stop.minute,
                            seconds=matrix_row.default_stop.second,
                        )
                        if my_dict["stop"] < my_dict["start"]:
                            my_dict["stop"] = my_dict["stop"] + timedelta(days=1)
                    to_create.append(my_dict)
        new_ce = self.env["calendar.event"].create(to_create)
        self.show_in_matrix_event_ids = [(5, 0, 0)] + to_show + [
            (4, ce.id) for ce in new_ce if ce.visible_matrix_row_id
        ]

    def write(self, values):
        # Delete partners from matrix -> Delete partners from calendar events
        self.ensure_one()
        command = values.get("partner_ids")
        if command:
            assert len(command) == 1 and command[0][0] == 6  # SET command
            new_ids = command[0][2]
            old_ids = self.partner_ids.ids
            delete_partner_ids = set(old_ids) - set(new_ids)
            for delete_partner_id in delete_partner_ids:
                events = self.env["calendar.event"].search(
                    [
                        ("partner_ids", "=", delete_partner_id),
                        ("matrix_id", "=", self.id)
                    ]
                )
                events.partner_ids = [(3, delete_partner_id)]
        super(CalendarEventMatrix, self).write(values)
