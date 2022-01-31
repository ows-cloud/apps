from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    """
    For each ir.property with res.users.partner_id:
        Set company_id
    TODO: If company_dependent is really new, migrate 'partner_id' from 'res_users' to 'ir_property' in the database.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    partner_field = env['ir.model.fields'].search([('model', '=', 'res.users'), ('name', '=', 'partner_id')]).ensure_one()
    ip_partners = env['ir.property'].search([('fields_id', '=', partner_field.id), ('company_id', '=', False)])
    for ip_partner in ip_partners:
        user_id = ip_partner.res_id.split(',')[1]
        user = env['res.users'].browse(int(user_id)).exists()
        ip_partner.company_id = user.company_id

def uninstall_hook(cr, registry):
    """
    For each ir.property with res.users.partner_id:
        If the company_id matches the user's company_id (assuming that all users have partner for their company_id):
            Make the user always have this partner, by removing company_id.
        Otherwise:
            Delete the property, as it is not relevant anymlre.
    TODO: If company_dependent is really removed, migrate 'partner_id' from 'ir_property' to 'res_users' in the database.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})
    all_users = env['res.users'].search([])
    user_company_id = {user.id: user.company_id.id for user in all_users}
    partner_field = env['ir.model.fields'].search([('model', '=', 'res.users'), ('name', '=', 'partner_id')]).ensure_one()
    ip_partners = env['ir.property'].search([('fields_id', '=', partner_field.id), ('company_id', '>', 0)])
    for ip_partner in ip_partners:
        user_id = ip_partner.res_id.split(',')[1]
        if ip_partner.company_id.id == user_company_id[user_id]:
            ip_partner.company_id = False
        else:
            ip_partner.unlink()
