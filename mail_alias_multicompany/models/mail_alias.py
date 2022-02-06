from odoo import _, api, fields, models


class Alias(models.Model):
    _inherit = 'mail.alias'

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)

    @api.model
    def create(self, vals_list):
        if type(vals_list) is dict:
            vals_list = [vals_list]
        for vals_dict in vals_list:
            vals_dict = self._set_alias_name_with_alias_company_name_if_required(vals_dict, company_id=self.env.company.id)
        return super(Alias, self).create(vals_list)

    def write(self, vals_dict):
        if vals_dict.get('alias_name') or vals_dict.get('company_id'):
            aliases = self.env['mail.alias']
            for alias in self:
                vals_dict = self._set_alias_name_with_alias_company_name_if_required(
                    vals_dict, alias.alias_name, alias.company_id.id,
                )
                super(Alias, alias).write(vals_dict)
            return True
        else:
            return super(Alias, self).write(vals_dict)

    def _set_alias_name_with_alias_company_name_if_required(self, vals_dict, alias_name=None, company_id=None):
        alias_name = vals_dict.get('alias_name') or alias_name
        company_id = vals_dict.get('company_id') or company_id
        assert alias_name and company_id, "ERROR in _set_alias_name_with_alias_company_name_if_required. alias_name = {}, company_id = {}".format(alias_name, company_id)

        require_alias_company_name = self.env['ir.config_parameter'].sudo().get_param('mail_alias_multicompany.require_alias_company_name')
        if require_alias_company_name in ('1', 't', 'true', 'True'):
            company = self.env['res.company'].browse(company_id)
            assert company.alias_company_name, "ERROR in _set_alias_name_with_alias_company_name_if_required. Please set a company alias name."
            length = len(company.alias_company_name) + 1
            if not alias_name[-length:] == '.' + company.alias_company_name:
                vals_dict['alias_name'] = alias_name + '.' + company.alias_company_name
        return vals_dict
