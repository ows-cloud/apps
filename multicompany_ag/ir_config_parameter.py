from odoo import api, fields, models, tools, SUPERUSER_ID, _


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def force_set_param(self):
        set_param = self.sudo().set_param
        set_param('auth_signup.reset_password', repr(True))
        set_param('auth_signup.invitation_scope', 'b2c')
        #set_param('auth_signup.allow_uninvited', repr(True)) # Where is this setting used? In v10?
        set_param('auth_signup_with_phone', repr(False))
        set_param('auth_signup_with_address', repr(False))
        set_param('auth_signup_with_date_of_birth', repr(False))
        set_param('auth_signup_with_image', repr(False))
        set_param('auth_signup_with_captcha', repr(True))
        set_param('auth_login_with_captcha', repr(False))

        set_param('multicompany_base.force_security', '1')
        set_param('multicompany_base.force_config', '1')

        # OTHER

        # The system pricelist should be archived, so that websites will get the company's pricelist.
        self.env.ref('product.list0').active = False