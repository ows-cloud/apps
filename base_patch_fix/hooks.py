from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    """A user always has the same partner, except if 'multicompany_dependent_user_partner' is installed."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    module = env['ir.module.module'].search([('name', '=', 'multicompany_dependent_user_partner')])
    if not module.state == 'installed':
        field = env['ir.model.fields'].search([('model', '=', 'res.users'), ('name', '=', 'partner_id')]).ensure_one()
        properties = env['ir.property'].search([('fields_id', '=', field.id), ('company_id', '!=', False)])
        properties.write({'company_id': False})
