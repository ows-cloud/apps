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
        get_param = self.env["ir.config_parameter"].sudo().get_param
        user_support_ref = get_param("multicompany_base.support_user_ext_id")
        if user_support_ref and user_support_ref not in ('0', 'f', 'false', 'False'):
            try:
                support_user = self.env.ref(user_support_ref)
                support_user.sudo().write({'company_ids': [(4, new_company.id)]})
            except:
                message = 'Support user {} could not be added to company {}'.format(user_support_ref, new_company.name)
                _logger.warning(message)
                raise UserError(message)

        return new_company

    def configure(self):
        companies = self
        self.env['multicompany.config']._configure(companies)
