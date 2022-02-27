from odoo import api, fields, models, _


class MailMessage(models.Model):
    _inherit = 'mail.message'

    def create(self, vals_list):
        """
        Set correct company.

        14.0
        _mail_find_user_for_gateway() may find multiple portal users with the same email address.
        Then the selected user's company_id may be wrong.
        """
        if type(vals_list) is dict:
            vals_list = [vals_list]
        for vals_dict in vals_list:
            if not vals_dict.get('company_id'):
                model = vals_dict['model']
                res_id = vals_dict['res_id']
                record = self.env[model].browse(res_id)
                vals_dict['company_id'] = record.ensure_one().company_id.id
        return super(MailMessage, self).create(vals_list)
