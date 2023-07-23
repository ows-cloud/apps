from odoo import _, fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    matrix_ids = fields.Many2many(
        "calendar.event.matrix",
        relation="matrix_partner_rel",
        column1="partner_id",
        column2="matrix_id",
    )

    def sign_up_for_all_events_which_allow_to_sign_up(self):
        matrix_id = self.env.context.get("active_id")
        if matrix_id:
            for record in self:
                events = self.env["calendar.event"].search(
                    [
                        ("matrix_id", "=", matrix_id),
                        ("allow_to_sign_up", "=", True),
                    ]
                )
                events.partner_ids = [(4, record.id)]

    def _compute_no_of_events_and_hours(self):
        for record in self:
            record.no_of_events = 0
            record.no_of_hours = 0
            matrix_id = self.env.context.get("active_id")
            if matrix_id:
                events = self.env["calendar.event"].search(
                    [
                        ("matrix_id", "=", matrix_id),
                        ("partner_ids", "=", record.id),
                    ]
                )
                record.no_of_events = len(events)
                record.no_of_hours = sum(events.mapped('duration'))

    no_of_events = fields.Integer("No of events", compute="_compute_no_of_events_and_hours")
    no_of_hours = fields.Float("No of hours", compute="_compute_no_of_events_and_hours")