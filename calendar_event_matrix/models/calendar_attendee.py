from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Attendee(models.Model):
    _inherit = "calendar.attendee"

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

    def write(self, values):
        # Update event partner
        if "event_id" in values or "partner_id" in values:
            for attendee in self:
                # Delete event partner
                attendee.event_id.write({"partner_ids": [(3, attendee.partner_id.id)]})
                # Create event partner
                event = attendee.event_id
                if "event_id" in values:
                    event = self.env["calendar.event"].browse(values["event_id"])
                partner_id = attendee.partner_id.id
                if "partner_id" in values:
                    partner_id = values["partner_id"]
                event.write({"partner_ids": [(4, partner_id)]})
        return super().write(values)

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
        # Delete event partner
        for attendee in self:
            attendee.event_id.write({"partner_ids": [(3, attendee.partner_id.id)]})

        return super().unlink()

    def _send_mail_to_attendees(self, template_xmlid, force_send=False, ignore_recurrence=False):
        # Do not send invitation emails for events related to a matrix.
        self = self.filtered(lambda a: not a.event_id.matrix_id)
        super(Attendee, self)._send_mail_to_attendees(template_xmlid, force_send, ignore_recurrence)
