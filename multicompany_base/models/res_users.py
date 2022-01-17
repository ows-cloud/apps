from odoo import api, fields, models


class Users(models.Model):
    _inherit = 'res.users'

    default_user = fields.Boolean('Default User')

    _sql_constraints = [('default_user_uniq', 'unique(default_user, company_id)', 'Default User must be unique per company!')]
