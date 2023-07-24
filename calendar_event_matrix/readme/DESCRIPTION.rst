Assign people to calendar event types in a matrix (calendar.event.type.group).

TODO: Synchronize these fields better.

calendar.event partner_ids many2many res.partner
calendar.event attendee_ids many2one calendar.attendee

calendar.attendee write(event_id / partner_id) -> Update calendar.event partner_ids.
