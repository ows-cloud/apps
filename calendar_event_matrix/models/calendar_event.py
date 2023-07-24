from datetime import timedelta

from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    partner_count = fields.Integer("No of attendees", compute="_compute_partner_count")

    def _compute_partner_count(self):
        for record in self:
            record.partner_count = len(record.partner_ids)

    start_date_str = fields.Char("Start Date (text)", compute="_compute_start_date_str")

    def _compute_start_date_str(self):
        for record in self:
            if record.start:
                # TODO: get hours from timezone
                record.start_date_str = str((record.start + timedelta(hours=+2)).date())
            else:
                record.start_date_str = str(record.start_date)

    @api.model
    def create(self, vals):
        records = super().create(vals)

        return records

    def write(self, values):
        # Don't allow matrix_row_id without the correct matrix_id.
        if "matrix_row_id" in values:
            values["matrix_id"] =  self.env["calendar.event.matrix.row"].browse(values["matrix_row_id"]).matrix_id.id
        elif "matrix_id" in values:
            if values["matrix_id"]:
                # Allow matrix_id with empty matrix_row_id
                if self.mapped("matrix_row_id"):
                    assert self.mapped("matrix_row_id").mapped("matrix_id").ids == [values["matrix_id"]]
            else:
                assert not self.mapped("matrix_row_id")
        super().write(values)
        # Set attendee company.
        for record in self:
            record.attendee_ids.company_id = record.company_id

    matrix_id = fields.Many2one(
        "calendar.event.matrix", string="Matrix", ondelete="cascade"
    )
    matrix_row_id = fields.Many2one(
        "calendar.event.matrix.row", string="Matrix Row", ondelete="cascade"
    )

    def _compute_visible_matrix_row_id(self):
        for record in self:
            if record.matrix_row_id and record.matrix_row_id.show_in_matrix:
                record.visible_matrix_row_id = record.matrix_row_id.id
            else:
                record.visible_matrix_row_id = None

    visible_matrix_row_id = fields.Many2one(
        "calendar.event.matrix.row",
        string="Visible Matrix Row",
        compute="_compute_visible_matrix_row_id",
    )
    matrix_row_sequence = fields.Integer(
        "Matrix Row Sequence", related="matrix_row_id.sequence"
    )
    matrix_available_partner_ids = fields.Many2many(
        "res.partner", compute="_compute_matrix_available_partner_ids"
    )

    def _compute_matrix_available_partner_ids(self):
        for record in self:
            partner_ids = self.env["res.partner"]
            for partner in record.matrix_row_id.matrix_id.partner_ids:
                domain = [
                    ("partner_ids", "in", [partner.id]),
                    ("id", "!=", record.id),
                    "|",
                    "&",
                    ("start", ">", record.start),
                    ("start", "<", record.stop),
                    "&",
                    ("stop", ">", record.start),
                    ("stop", "<", record.stop),
                ]
                overlapping_events = self.env["calendar.event"].search(domain)
                if not overlapping_events:
                    partner_ids += partner
            record.matrix_available_partner_ids = partner_ids

    matrix_partner_attending = fields.Boolean(
        "Matrix Partner Attending",
        compute="_compute_matrix_partner_attending",
        inverse="_inverse_matrix_partner_attending",
    )

    def _compute_matrix_partner_attending(self):
        # partner_id = self.env.context.get("matrix_partner_id")
        # partner_id.ensure_one()
        for record in self:
            partner_id = record.matrix_row_id.matrix_id.matrix_partner_id
            if partner_id in record.partner_ids:
                record.matrix_partner_attending = True
            else:
                record.matrix_partner_attending = False

    def _inverse_matrix_partner_attending(self):
        # partner_id = self.env.context.get("matrix_partner_id")
        # partner_id.ensure_one()
        for record in self:
            partner_id = record.matrix_row_id.matrix_id.matrix_partner_id
            if record.matrix_partner_attending:
                record.write({"partner_ids": [(4, partner_id.id, 0)]})
            else:
                record.write({"partner_ids": [(3, partner_id.id, 0)]})

    def _compute_is_attending(self):
        for record in self:
            # <filter string="My Meetings" help="My Meetings" name="mymeetings" domain="[('partner_ids.user_ids', 'in', [uid])]"/>
            if self.env.user in record.attendee_partner_ids.user_ids:
                record.is_attending = True
            else:
                record.is_attending = False

    def _inverse_is_attending(self):
        for record in self:
            partner_id = self.env.user.partner_id
            if record.allow_to_sign_up:
                if record.is_attending:
                    record.write({"attendee_partner_ids": [(4, partner_id.id, 0)]})
                else:
                    record.write({"attendee_partner_ids": [(3, partner_id.id, 0)]})

    is_attending = fields.Boolean(
        string="Attending",
        compute="_compute_is_attending",
        inverse="_inverse_is_attending",
    )

    def _update_allow_to_sign_up(self):
        for record in self:
            if record.matrix_row_id:
                record.allow_to_sign_up = record.matrix_row_id.allow_to_sign_up
            else:
                record.allow_to_sign_up = False

    allow_to_sign_up = fields.Boolean(
        string="Allow to sign up",
        help="Allow to sign up for this calendar event.",
        default=lambda self: self._update_allow_to_sign_up(),
    )
    parent_id = fields.Many2one(
        "calendar.event",
        string="Attendee filter",
    )
    child_ids = fields.One2many("calendar.event", "parent_id", string="Child events")

    @api.depends("parent_id")
    def _compute_available_partner_ids(self):
        for record in self:
            domain = []
            if record.parent_id:
                domain = [("id", "in", record.parent_id.partner_ids.ids)]
            record.available_partner_ids = self.env["res.partner"].search(domain).ids

    available_partner_ids = fields.Many2many(
        "res.partner",
        string="Available attendees",
        compute="_compute_available_partner_ids",
    )

    def open_form(self):
        self.ensure_one()
        action = {
          "type": "ir.actions.act_window",
          "view_mode": "form,tree",
          "res_model": self._name,
          "res_id": self.id,
        }
        return action

    def update_parent_id(self):
        for record in self:
            if record.matrix_row_id and record.matrix_row_id.parent_id:
                domain = [
                    ("matrix_row_id", "=", record.matrix_row_id.parent_id.id),
                    ("id", "!=", record.id),
                    "|",
                    "&",
                    ("start", ">=", record.start),
                    ("start", "<=", record.stop),
                    "&",
                    ("stop", ">=", record.start),
                    ("stop", "<=", record.stop),
                ]
                parent_event = self.search(domain)
                if parent_event and len(parent_event) == 1:
                    record.parent_id = parent_event.id
                else:
                    record.parent_id = None
            else:
                record.parent_id = None

    attendee_partner_ids = fields.Many2many(
        "res.partner",
        string="Invited Attendees",
        help="Invited attendee contacts (attendee_ids.partner_id)",
        relation="calendar_attendee",
        column1="event_id",
        column2="partner_id",
    )
