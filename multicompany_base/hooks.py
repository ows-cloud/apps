from odoo import api, SUPERUSER_ID
from .models.multicompany_security import SECURITY_DO_IF

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    ICP = env['ir.config_parameter'].sudo()
    default_settings = {
        'multicompany_base.force_security': '0',
        'multicompany_base.force_config': '0',
        'multicompany_base.support_user': '__multicompany_base__.support_user',
    }
    for key, value in default_settings:
        if not ICP.get_param(key):
            ICP.set_param(key, value)

def WARNING_DELETE_RULES_uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for do_if in SECURITY_DO_IF:
        rules = env['ir.rule'].search([('name','ilike','% - %_model%{}'.format(do_if))])
        rules.unlink()
