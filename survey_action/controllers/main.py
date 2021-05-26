import json
import logging

from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slugify
from odoo.addons.survey.controllers.main import Survey as SurveyController


_logger = logging.getLogger(__name__)


class SurveyController2(SurveyController):

    # from survey
    
    # AJAX submission of a page
    @http.route(['/survey/submit/<model("survey.survey"):survey>'], type='http', methods=['POST'], auth='public', website=True)
    def submit(self, survey, **post):
        _logger.debug('Incoming data: %s', post)
        page_id = int(post['page_id'])
        questions = request.env['survey.question'].search([('page_id', '=', page_id)])

        # Answer validation
        errors = {}
        for question in questions:
            answer_tag = "%s_%s_%s" % (survey.id, page_id, question.id)
            errors.update(question.validate_question(post, answer_tag))

        ret = {}
        if len(errors):
            # Return errors messages to webpage
            ret['errors'] = errors
        else:
            # Store answers into database
            try:
                user_input = request.env['survey.user_input'].sudo().search([('token', '=', post['token'])], limit=1)
            except KeyError:  # Invalid token
                return request.render("survey.403", {'survey': survey})
            user_id = request.env.user.id if user_input.type != 'link' else SUPERUSER_ID

            for question in questions:
                answer_tag = "%s_%s_%s" % (survey.id, page_id, question.id)
                request.env['survey.user_input_line'].sudo(user=user_id).save_lines(user_input.id, question, post, answer_tag)

            go_back = post['button_submit'] == 'previous'
            next_page, _, last = request.env['survey.survey'].next_page(user_input, page_id, go_back=go_back)
            vals = {'last_displayed_page_id': page_id}
            if next_page is None and not go_back:
                vals.update({'state': 'done'})
            else:
                vals.update({'state': 'skip'})
            user_input.sudo(user=user_id).write(vals)
            ret['redirect'] = '/survey/fill/%s/%s' % (survey.id, post['token'])
            if go_back:
                ret['redirect'] += '/prev'

            # NEW ############################################################

            if user_input.state == 'done':
            
                action = survey.server_action_id
                user = survey.company_id.user_tech_id
                if action and user:
                    ret['redirect'] = action.with_context(active_id=user_input.id, active_model='survey.user_input', website_id=request.website.id).sudo(user).run()

            # END ############################################################

        return json.dumps(ret)