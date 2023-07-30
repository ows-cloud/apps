import werkzeug

import odoo.http as http

from odoo.http import request
from odoo.tools.misc import get_lang


class CalendarController(http.Controller):


    @http.route('/calendar/meeting/view', type='http', auth="calendar")
    def view_meeting(self, token, id, **kwargs):
        attendee = request.env['calendar.attendee'].sudo().search([
            ('access_token', '=', token),
            ('event_id', '=', int(id))])
        if not attendee:
            return request.not_found()
        timezone = attendee.partner_id.tz
        lang = attendee.partner_id.lang or get_lang(request.env).code
        event = request.env['calendar.event'].with_context(tz=timezone, lang=lang).sudo().browse(int(id))
        company = event.user_id and event.user_id.company_id or event.create_uid.company_id

        # If user is internal and logged, redirect to form view of event
        # otherwise, display the simplifyed web page with event informations
        if request.session.uid and request.env['res.users'].browse(request.session.uid).user_has_groups('base.group_user'):
            return werkzeug.utils.redirect('/web?db=%s#id=%s&view_type=form&model=calendar.event' % (request.env.cr.dbname, id))

        # NOTE : we don't use request.render() since:
        # - we need a template rendering which is not lazy, to render before cursor closing
        # - we need to display the template in the language of the user (not possible with
        #   request.render())
        response_content = request.env['ir.ui.view'].with_context(lang=lang)._render_template(
            'calendar.invitation_page_anonymous', {
                'company': company,
                'event': event,
                'attendee': attendee,
            })
        return request.make_response(response_content, headers=[('Content-Type', 'text/html')])

