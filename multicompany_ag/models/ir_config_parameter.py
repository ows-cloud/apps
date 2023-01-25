from odoo import models


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    def force_set_param(self):
        if not self.env.user.has_group("base.group_system"):
            return False
        set_param = self.sudo().set_param
        set_param("auth_signup.reset_password", repr(True))
        set_param("auth_signup.invitation_scope", "b2c")
        # set_param('auth_signup.allow_uninvited', repr(True))
        # # Where is this setting used? In v10?
        set_param("auth_signup_with_phone", repr(False))
        set_param("auth_signup_with_address", repr(False))
        set_param("auth_signup_with_date_of_birth", repr(False))
        set_param("auth_signup_with_image", repr(False))
        set_param("auth_signup_with_captcha", repr(True))
        set_param("auth_login_with_captcha", repr(False))

        set_param("multicompany_base.force_security", "1")
        set_param("multicompany_base.force_config", "1")
