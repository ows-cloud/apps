from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    @api.model
    def create(self, vals):
        new_company = super(Company, self.sudo()).create(vals)
        new_company.sudo().partner_id.write({'company_id': new_company.id})
        return new_company
