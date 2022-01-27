from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    """Let company managers create users."""
    signup_token = fields.Char(copy=False, groups="base.group_erp_manager,multicompany_base.group_company_manager")
    signup_type = fields.Char(string='Signup Token Type', copy=False, groups="base.group_erp_manager,multicompany_base.group_company_manager")
    signup_expiration = fields.Datetime(copy=False, groups="base.group_erp_manager,multicompany_base.group_company_manager")
