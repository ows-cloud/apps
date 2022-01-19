from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    @api.model
    def create(self, vals):
        new_company = super(Company, self.sudo()).create(vals)
        new_company.sudo().partner_id.write({'company_id': new_company.id})

        # Give access to SUPPORT USER
        get_param = self.env["ir.config_parameter"].sudo().get_param
        user_support_ref = get_param("multicompany_base.support_user")
        if user_support_ref:
            support_user = self.env.ref(user_support_ref)
            support_user.sudo().write({'company_ids': [(4, new_company.id)]})

        return new_company

    def configure(self):
        companies = self
        self.env['multicompany.config']._configure(companies)
