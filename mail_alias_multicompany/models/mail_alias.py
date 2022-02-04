from odoo import _, api, fields, models


class Alias(models.Model):
    _inherit = 'mail.alias'

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    alias_domain_id = fields.Many2one('mail.alias.domain', string="Alias Domain", required=True)

    _sql_constraints = [
        ('alias_unique', 'UNIQUE(alias_name, alias_domain_id)', 'Unfortunately this email alias is already used, please choose a unique one')
    ]

    @api.model
    def create(self, vals_list):
        for vals_dict in vals_list:
            vals_dict = self._set_alias_name_with_alias_company_name_if_required(vals_dict)
        return super(Alias, self).create(vals_list)

    def write(self, vals_dict):
        if vals_dict.get('alias_name') or vals_dict.get('company_id') or vals_dict.get('alias_domain_id'):
            aliases = self.env['mail.alias']
            for alias in self:
                vals_dict = self._set_alias_name_with_alias_company_name_if_required(
                    vals_dict, alias.alias_name, alias.company_id.id, alias.alias_domain_id.id,
                )
                aliases = aliases | super(Alias, self).write(vals_dict)
            return aliases
        else:
            return super(Alias, self).write(vals_dict)

    def _set_alias_name_with_alias_company_name_if_required(self, vals_dict, alias_name=None, company_id=None, alias_domain_id=None):
        alias_name = vals_dict.get('alias_name') or alias_name
        company_id = vals_dict.get('company_id') or company_id
        alias_domain_id = vals_dict.get('alias_domain_id') or alias_domain_id
        assert alias_name and company_id and alias_domain_id

        if self.env['mail.alias.domain'].browse(alias_domain_id).require_alias_company_name:
            company = self.env['res.company'].browse(company_id)
            assert company.alias_company_name
            length = len(company.alias_company_name) + 1
            if not alias_name[-length:] == '.' + company.alias_company_name:
                vals_dict['alias_name'] = alias_name + '.' + company.alias_company_name
        return vals_dict
