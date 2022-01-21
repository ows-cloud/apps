from odoo import api, fields, models


class Users(models.Model):
    _inherit = 'res.users'

    default_user = fields.Boolean('Default User Template')

    _sql_constraints = [('default_user_uniq', 'unique(default_user, company_id)', 'Default User must be unique per company!')]

    @api.model
    def create(self, vals):
        vals = self._remove_admin_access(vals)
        return super(Users, self).create(vals)

    def write(self, vals):
        vals = self._remove_admin_access(vals)
        vals = self._if_other_company_and_not_su_set_only_name_lang_partner(vals)
        return super(Users, self).write(vals)

    def _remove_admin_access(self, vals):
        admin_access = "sel_groups_{erp}_{system}".format(
            erp=str(self.env.ref('base.group_erp_manager').id),
            system=str(self.env.ref('base.group_system').id),
        )
        vals.pop(admin_access, None)
        return vals

    def _if_other_company_and_not_su_set_only_name_lang_partner(self, vals):
        if self.env.su:
            return vals

        set_only = False
        for user in self:
            if not user.company_id.id == self.env.company.id:
                set_only = True
        if set_only:
            for key in vals.copy():
                if key not in ('name', 'lang', 'partner_id'):
                    del vals[key]
        return vals
