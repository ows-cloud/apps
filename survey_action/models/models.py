from odoo import models, fields, api

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    server_action_id = fields.Many2one('ir.actions.server', string="Server Action after survey")
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.context.get('default_company_id') or self.env.company)