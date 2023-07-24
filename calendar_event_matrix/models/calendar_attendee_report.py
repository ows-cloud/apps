import logging
from datetime import datetime
from io import StringIO

import pandas as pd
from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# VIEW depends on calendar.attendee
class CalendarAttendeeReport(models.Model):
    _name = "calendar.attendee.report"
    _description = "Calendar Attendee SQL Report"
    _auto = False

    STATE_SELECTION = [
        ('needsAction', 'Needs Action'),
        ('tentative', 'Uncertain'),
        ('declined', 'Declined'),
        ('accepted', 'Accepted'),
    ]

    # ATTENDEE FIELDS
    availability = fields.Selection(
        [('free', 'Free'), ('busy', 'Busy')],
        'Free/Busy',
        readonly=True
    )
    common_name = fields.Char('Common name', compute='_compute_common_name', store=True)
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )
    event_id = fields.Many2one(
        'calendar.event', 'Meeting linked', required=True, ondelete='cascade'
    )
    partner_id = fields.Many2one('res.partner', 'Contact', required=True, readonly=True)
    state = fields.Selection(STATE_SELECTION, string='Status', readonly=True, default='needsAction',
                             help="Status of the attendee's participation")
    # EVENT FIELDS
    duration = fields.Float('Hours')
    recurrence_id = fields.Many2one('calendar.recurrence')
    start_date = fields.Date("Start Date")
    stop_date = fields.Date("Stop Date")
    start = fields.Datetime("Start")
    stop = fields.Datetime("Stop")
    matrix_id = fields.Many2one("calendar.event.matrix")
    matrix_row_id = fields.Many2one("calendar.event.matrix.row")

    def init(self):
        tools.drop_view_if_exists(self._cr, "calendar_attendee_report")
        self._cr.execute(
            """
            CREATE OR REPLACE VIEW calendar_attendee_report AS
            SELECT a.id,
                a.availability,
                a.common_name,
                a.event_id,
                a.partner_id,
                a.state,
                a.company_id,
                e.duration,
                e.recurrence_id,
                e.start,
                e.start::DATE AS start_date,
                e.stop,
                e.stop::DATE AS stop_date,
                e.matrix_id,
                e.matrix_row_id
            FROM calendar_attendee a
            LEFT JOIN calendar_event e ON a.event_id = e.id
            """
        )

    @api.model
    def create(self, values):
        return self.env["calendar.attendee"].create(values)

    def write(self, values):
        return (
            self.env["calendar.attendee"]
            .browse([id for id in self._ids if id > 0])
            .write(values)
        )

    def unlink(self):
        return (
            self.env["calendar.attendee"]
            .browse([id for id in self._ids if id > 0])
            .unlink()
        )
