import logging
from odoo import api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class Company(models.Model):
    _inherit = 'res.company'

    @api.model
    def create(self, vals):
        new_company = super(Company, self.sudo()).create(vals)
        new_company.sudo().partner_id.write({'company_id': new_company.id})

        # Give access to SUPPORT USER
        support_user = self.env.ref('__multicompany_base__.support_user')
        support_user.sudo().write({'company_ids': [(4, new_company.id)]})

        # Auto-configure company
        config = self.env['ir.config_parameter'].sudo().get_param('multicompany_base.force_config')
        if config in ('1', 't', 'true', 'True'):
            self.env['multicompany.config']._configure_companies(new_company)

        return new_company

    def configure(self):
        companies = self
        self.env['multicompany.config']._configure_companies(companies)
