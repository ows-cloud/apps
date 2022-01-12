from odoo import fields, models


class Users(models.Model):
    _inherit = 'res.users'

    def create(self, vals):
        """A user always has the same partner, except if 'multicompany_dependent_user_partner' is installed."""
        user = super(Users, self).create(vals)
        if not self.env['ir.module.module'].search([('name', '=', 'multicompany_dependent_user_partner')]).state == 'installed':
            field = self.env['ir.model.fields'].search([('model', '=', 'res.users'), ('name', '=', 'partner_id')]).ensure_one()
            self.env['ir.property'].search([('fields_id', '=', field.id), ('company_id', '>', 0)]).write({'company_id': False})
