Assign people to calendar event types in a matrix (calendar.event.type.group).

When a calendar event is assigned to a matrix,
attendees do not get an invitation email (overriding _send_mail_to_attendees).

A calendar event may have a parent event or child events.
A child event may only have attendees who are present in the parent event.
The use case for a child event is a responsibility related to the parent event,
e.g. a meal duty related to a meal.

The controllers are copied and not adapted to this module yet (work in progress).
