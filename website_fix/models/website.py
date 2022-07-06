from odoo import api, fields, models


class Website(models.Model):
    _inherit = 'website'

    @api.model
    def sale_get_payment_term(self, partner):
        """ Removed .sudo()"""
        pt = self.env.ref('account.account_payment_term_immediate', False)
        if pt:
            pt = (not pt.company_id.id or self.company_id.id == pt.company_id.id) and pt
        return (
            partner.property_payment_term_id or
            pt or
            self.env['account.payment.term'].sudo().search([('company_id', '=', self.company_id.id)], limit=1)
        ).id
