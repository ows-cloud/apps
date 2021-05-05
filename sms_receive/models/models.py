from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'

    ref = fields.Char("Short Company Name")
    sms_receive_action_id = fields.Many2one('ir.actions.server', string="Incoming SMS Action")

    _sql_constraints = [
        ('ref_uniq', 'unique (ref)', "This name is already taken!"),
    ]

class SMS(models.Model):
    _name = 'sms.receive_sms'
    _description = 'SMS received'

    sender = fields.Char()
    message = fields.Text()
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.context.get('force_company') or self.env.context.get('company_id') or self.env.context.get('default_company_id') or self.env.user.company_id)