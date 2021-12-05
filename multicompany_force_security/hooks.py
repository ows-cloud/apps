from odoo import api, SUPERUSER_ID
from openupgradelib import openupgrade
from .models.multicompany_force_security import EXTID_MODULE_NAME

def _WARNING_DELETE_RULES_uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    rules = env['ir.rule'].search([('name','ilike','#%')])
    rules.unlink()
    ext_ids = env['ir.model.data'].search([('module','=',EXTID_MODULE_NAME),('name','ilike','%_rule')])
    ext_ids.unlink()

def _pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _create_initial_company_id_fields(env)

def _create_initial_company_id_fields(env):
    field_spec = [
        ('company_id', 'ir.rule', False, 'many2one', 'int4', EXTID_MODULE_NAME, 1),
        ('company_id', 'ir.model', False, 'many2one', 'int4', EXTID_MODULE_NAME, 1),
        ('company_id', 'ir.model.fields', False, 'many2one', 'int4', EXTID_MODULE_NAME, 1),
        ('company_id', 'res.lang', False, 'many2one', 'int4', EXTID_MODULE_NAME, 1),
    ]
    openupgrade.add_fields(env, field_spec)
