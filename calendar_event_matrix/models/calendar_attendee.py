from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Attendee(models.Model):
    _inherit = "calendar.attendee"

    """
    calendar.attendee is a relation table between calendar.event and res.partner.
    The many2many relation creates records with only event_id and partner_id.
    Multicompany implementations may also require company_id.
    calendar.event write() will update the company of the related attendees.
    """

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        store=True,
        index=True,
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
