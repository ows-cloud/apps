from odoo import api, fields, models, _


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    replace_record_id = fields.Many2one('mail.template', string='Replace Record')
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.company)
    
    _sql_constraints = [('replace_mail_template_uniq', 'unique(replace_record, company_id)', 'Replace Record must be unique per company!')]
