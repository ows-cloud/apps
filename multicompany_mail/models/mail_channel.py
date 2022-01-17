from odoo import api, fields, models, _


class MailChannel(models.Model):
    _inherit = 'mail.channel'

    all_employees = fields.Boolean('Channel for all employees')    
    _sql_constraints = [('all_employees_uniq', 'unique(all_employees, company_id)', 'Channel for all emloyees must be unique per company!')]