from odoo import fields, models


class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    code = fields.Char()
