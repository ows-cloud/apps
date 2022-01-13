from odoo import api, SUPERUSER_ID
from .models.multicompany_force_security import EXTID_MODULE_NAME

def _WARNING_DELETE_RULES_uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    rules = env['ir.rule'].search([('name','ilike','#%')])
    rules.unlink()
    ext_ids = env['ir.model.data'].search([('module','=',EXTID_MODULE_NAME),('name','ilike','%_rule')])
    ext_ids.unlink()
