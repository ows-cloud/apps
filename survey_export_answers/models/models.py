import json
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    def export_answers(self):
        self.ensure_one()
        survey = self
        questions = self.env['survey.question'].search([('survey_id','=',survey.id)])
        all_answers = [[input.id, json.loads(self.prefill(survey, input.access_token))] for input in survey.user_input_ids]

        question_list = []
        for q in questions:
            question_list.append(('%s_%s_%s' % (q.survey_id.id, q.page_id.id, q.id), q.title, q.question_type, q.page_id.sequence, q.page_id.id, q.sequence, q.id))
        question_list.sort(key=lambda t: (t[3], t[4], t[5], t[6]))
        
        csv = '"id",' + ','.join(['"%s"' % tup[1] for tup in question_list]) + '\n'
        
        for id, user_answers in all_answers:
            csv_answers = ['"%s"' % id]
            for key, question, type, t3, t4, t5, t6 in question_list:
                csv_answer = ''
                question_answer = user_answers.get(key, [])
                if question_answer:
                    if type in ('simple_choice','multiple_choice','matrix'):
                        answer_labels = self.env['survey.question.answer'].browse(question_answer)
                        csv_answer = '"%s"' % ', '.join([label.value for label in answer_labels])
                    else:
                        assert len(question_answer) == 1, "%s answers to the question %s" % (len(question_answer), question)
                        csv_answer = '"%s"' % question_answer[0]
                csv_answers.append(csv_answer)
            csv += ','.join(csv_answers) + '\n'

        raise UserError(csv)
    
    # copied from survey.controllers.main, 'request' -> 'self'
    # odoo.addons.survey.controllers.main.WebsiteSurvey().prefill(survey, input.token) does not return JSON but <Response 61 bytes [200 OK]> because of @http.route()
    def prefill(self, survey, token, page=None, **post):
        UserInputLine = self.env['survey.user_input.line']
        ret = {}

        # Fetch previous answers
        if page:
            previous_answers = UserInputLine.sudo().search([('user_input_id.access_token', '=', token), ('page_id', '=', page.id)])
        else:
            previous_answers = UserInputLine.sudo().search([('user_input_id.access_token', '=', token)])

        # Return non empty answers in a JSON compatible format
        for answer in previous_answers:
            if not answer.skipped:
                answer_tag = '%s_%s_%s' % (answer.survey_id.id, answer.page_id.id, answer.question_id.id)
                answer_value = None
                if answer.answer_type == 'text_box':
                    answer_value = answer.value_text_box
                elif answer.answer_type == 'char_box' and answer.question_id.question_type == 'char_box':
                    answer_value = answer.value_char_box
                elif answer.answer_type == 'suggestion':
                    # here come comment answers for matrices, simple choice and multiple choice
                    answer_tag = "%s_%s" % (answer_tag, 'comment')
                    answer_value = answer.value_char_box
                elif answer.answer_type == 'number':
                    answer_value = answer.value_number.__str__()
                elif answer.answer_type == 'date':
                    answer_value = answer.value_date
                elif answer.answer_type == 'suggestion' and not answer.matrix_row_id:
                    answer_value = answer.suggested_answer_id.id
                elif answer.answer_type == 'suggestion' and answer.matrix_row_id:
                    answer_tag = "%s_%s" % (answer_tag, answer.matrix_row_id.id)
                    answer_value = answer.suggested_answer_id.id
                if answer_value:
                    ret.setdefault(answer_tag, []).append(answer_value)
                else:
                    _logger.warning("[survey] No answer has been found for question %s marked as non skipped" % answer_tag)
        _logger.warning('prefill: ret = %s, json.dumps(ret) = %s' % (ret, json.dumps(ret)))
        return json.dumps(ret)