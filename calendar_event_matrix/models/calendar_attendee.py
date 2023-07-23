from odoo import _, fields, models
from odoo.exceptions import UserError


class Attendee(models.Model):
    _inherit = "calendar.attendee"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
    )

    _sql_constraints= [
        (
            "unique_event_partner",
            "unique(event_id, partner_id)",
            "A contact may be assigned to the same calendar event only once."
        )
    ]

    def _compute_start_date(self):
        for record in self:
            record.start_date = record.start.date()

    # start_date = fields.Date("Start Date", compute="_compute_start_date")
    # start = fields.Datetime("Start", related="event_id.start")
    # stop = fields.Datetime("Stop", related="event_id.stop")
    # matrix_row_id = fields.Many2one(
    #     "calendar.event.matrix.row",
    #     related="event_id.matrix_row_id",
    # )
    # # allow_to_sign_up = fields...

    def unlink(self):
        # Restrict: Raise error if there is any child event with the attendee partner.
        for record in self:
            events = record.event_id.child_ids
            if events:
                rp = record.partner_id
                emp = events.mapped("partner_ids")
                events = events.filtered(lambda e: record.partner_id in e.mapped("partner_ids"))
                if events:
                    raise UserError(_("'{partner}' exists in '{events}' and cannot be deleted from '{event}'.").format(
                        partner=record.partner_id.display_name,
                        events="' and '".join([e.display_name for e in events]),
                        event=record.event_id.display_name,
                    ))
        return super().unlink()

    def _send_mail_to_attendees(self, template_xmlid, force_send=False, ignore_recurrence=False):
        # Do not send invitation emails for events related to a matrix.
        self = self.filtered(lambda a: not a.event_id.matrix_id)
        super(Attendee, self)._send_mail_to_attendees(template_xmlid, force_send, ignore_recurrence)
