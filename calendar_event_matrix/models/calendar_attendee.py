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
                event_id = attendee.event_id.id
                partner_id = attendee.partner_id.id
                # Delete event partner
                self.env.cr.execute(
                    "DELETE FROM calendar_event_res_partner_rel WHERE calendar_event_id = {} AND res_partner_id = {};".format(event_id, partner_id)
                )
                # Create event partner
                if "event_id" in values:
                    event_id = values["event_id"]
                if "partner_id" in values:
                    partner_id = values["partner_id"]
                self.env.cr.execute(
                    "INSERT INTO calendar_event_res_partner_rel (calendar_event_id, res_partner_id) VALUES ({}, {});".format(event_id, partner_id)
                )
        self._unsubscribe_partner()
        super(Attendee, self).write(values)
        self._subscribe_partner()

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
            self.env.cr.execute(
                "DELETE FROM calendar_event_res_partner_rel WHERE calendar_event_id = {} AND res_partner_id = {};".format(
                    attendee.event_id.id, attendee.partner_id.id
                )
            )

        return super().unlink()

    def _send_mail_to_attendees(self, template_xmlid, force_send=False, ignore_recurrence=False):
        # Do not send invitation emails for events related to a matrix.
        self = self.filtered(lambda a: not a.event_id.matrix_id)
        super(Attendee, self)._send_mail_to_attendees(template_xmlid, force_send, ignore_recurrence)
