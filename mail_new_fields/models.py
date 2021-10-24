from odoo import models, fields, api


class MailMessage(models.Model):
    _inherit = 'mail.message'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.company)
