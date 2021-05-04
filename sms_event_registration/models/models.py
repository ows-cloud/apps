import logging

from datetime import datetime
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class SMS(models.Model):
    _inherit = 'sms.receive_sms'

    def send_sms(self, message):
        _logger.warning(message)

    def event_registration(self):
        """
        TESTS
        0) Wrong format
        1) Try with valid event
           Events with the same name
        2) Try with no ticket
           Try with valid ticket (2x)
           Tickets with the same name
        3) Ticket full
           Event full
        4) Success
        """
        company = self.company_id.ref
        # 0) The first line should have company & event (& ticket) details. The next lines have attendee names.
        try:
            details, attendees = self.message.split('\n', maxsplit=1)
            details_list = details.split(' ')
            search_event_name = details_list[1]
            attendees_list = attendees.split('\n')
            attendees_list = list(filter(None, attendees_list)) # removing empty lines TODO test this
            attendee_names = '\n'.join([name for name in attendees_list])
        except:
            return self.send_sms('Please try again. The SMS should have this format (ticket is optional):\n\n' \
                                    'Company Event Ticket\n' \
                                    'Person 1\n' \
                                    'Person 2 (optional))')

        # 1) Identify the future confirmed event (by name or twitter_hashtag)
        domain_mini = [('date_end', '>', datetime.now()), ('state', '=', 'confirm')]
        domain_full = domain_mini[:]
        domain_full.extend(
            ['|', ('twitter_hashtag', '=', search_event_name), ('name', '=', search_event_name)]
        )
        event = self.env['event.event'].search(domain_full)
        errormsg_try_valid_event = 'Please try again with a valid event. Here are the upcoming events:\n{2}'.format(company, search_event_name, event_names)
        errormsg_events_same_name = 'Please contact {0}. There are {1} upcoming events with the same name "{2}"!'.format(company, len(event), search_event_name)
        if not event:
            events = self.env['event.event'].search(domain_mini, order='date_end')
            event_names = '\n'.join(['{0} "{1}"'.format(e.twitter_hashtag or '', e.name) for e in events])
            return self.send_sms(errormsg_try_valid_event)
        elif len(event) > 1:
            return self.send_sms(errormsg_events_same_name)

        # 2) Identify the free ticket (optional)
        tickets = event.event_ticket_ids.filtered(lambda t: t.price == 0)
        ticket_names = '\n'.join([t.name for t in tickets])
        ticket = None
        search_ticket_name = ''
        errormsg_try_without_ticket = 'Please try again without any ticket for {0} {1}.' \
                                    ''.format(company, search_event_name)
        errormsg_try_valid_ticket = 'Please try again with a valid ticket.' \
                                    ' Here are the free ticket alternatives for {0} {1}:\n{2}' \
                                    ''.format(company, search_event_name, ticket_names)
        errormsg_tickets_same_name = 'Please contact {0}. For the event {3}, there are {1} tickets with the same name "{2}"!' \
                                    ''.format(company, len(ticket), search_ticket_name, search_event_name)
        if len(details_list) > 2:
            # Search for specific ticket name
            search_ticket_name = details_list[2]
            ticket = tickets.filtered(lambda t: t.name == search_ticket_name)
            if not ticket:
                if not tickets:
                    return self.send_sms(errormsg_try_without_ticket)
                else:
                    return self.send_sms(errormsg_try_valid_ticket)
            elif len(ticket) > 1:
                return self.send_sms(errormsg_tickets_same_name)
        else:
            # Do not search for specific ticket name
            if len(tickets) == 1:
                ticket = tickets
            elif len(tickets) > 1:
                return self.send_sms(errormsg_try_valid_ticket)

        # 3) Check for available seats
        if ticket and ticket.seats_availability == 'limited' and ticket.seats_available < len(attendees_list):
            return self.send_sms('Sorry, {0} has only {1} seats available for the event {2} with ticket {3}. Here are the ticket alternatives:\n{4}' \
                ''.format(company, ticket.seats_available, search_event_name, search_ticket_name, ticket_names))
        
        if event.seats_availability == 'limited' and event.seats_available < len(attendees_list):
            return self.send_sms('Sorry, {0} has only {1} seats available for the event {2}.' \
                ''.format(company, ticket.seats_available, search_event_name))
        
        # 4) Register attendees
        # TODO check if they are already registered
        for name in attendees_list:
            self.env['event.registration'].create({
                'name': name,
                'phone': self.sender,
                'event_id': event.id,
                'event_ticket_id': ticket and ticket.id or False,
                'state': 'open',
            })
        return self.send_sms('Registration completed:\n\n{0} {1} {2}\n{3}'.format(company, search_event_name, search_ticket_name, attendee_names))