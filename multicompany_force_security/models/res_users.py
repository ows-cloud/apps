from os import remove
from odoo import models, fields, api
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        vals = self._remove_admin_access(vals)
        #vals = self._only_allow_adding_these_features(vals)
        return super(Users, self).create(vals)

    def write(self, vals):
        vals = self._remove_admin_access(vals)
        #vals = self._only_allow_adding_these_features(vals)
        vals = self._if_other_company_set_only_name_lang_partner(vals)
        return super(Users, self).write(vals)

    def _remove_admin_access(self, vals):
        admin_access = "sel_groups_{erp}_{system}".format(
            erp=str(self.env.ref('base.group_erp_manager').id),
            system=str(self.env.ref('base.group_system').id),
        )
        vals.pop(admin_access, None)
        return vals

    # def _only_allow_adding_these_features(self, vals):
    #     compare_user = self.env.company.only_allow_these_features
    #     if compare_user:
    #         for key in vals:
    #             if 'in_group_' in key or 'sel_groups_' in key:
    #                 group_ids = key.split('_')[2:]
    #                 group_ids = map(int, group_ids)
    #                 allowed_ids = compare_user.groups_id.ids
    #                 if not any(id in allowed_ids for id in group_ids):
    #                     vals[key] = False
    #     return vals
    #     # allow = False
    #     # deny = False
    #     # for user in self:
    #     #     if user == user.sudo().company_id.only_allow_these_features:
    #     #         allow = True
    #     #     else:
    #     #         deny = True
    #     # if allow == True and deny == False:
    #     #     # Only if all users are assigned by companies to only allow certain features.
    #     #     return vals

    #     # def compare_access_rights(vals, compare_user):            
    #     #     if not compare_user:
    #     #         return vals
    #     #     for key in vals:
    #     #         if 'in_group_' in key or 'sel_groups_' in key:
    #     #             group_ids = key.split('_')[2:]
    #     #             group_ids = map(int, group_ids)
    #     #             allowed_ids = compare_user.groups_id.ids
    #     #             if not any(id in allowed_ids for id in group_ids):
    #     #                 vals[key] = False
    #     #     return vals

    #     # if len(self):
    #     #     # Update users
    #     #     for user in self:
    #     #         compare_user = user.sudo().company_id.only_allow_these_features
    #     #         vals = compare_access_rights(vals, compare_user)
    #     # else:
    #     #     # Create user
    #     #     compare_user = self.env['res.company'].browse(vals['company_id']).only_allow_these_features
    #     #     vals = compare_access_rights(vals, compare_user)

    #     # return vals

    def _if_other_company_set_only_name_lang_partner(self, vals):
        set_only = False
        for user in self:
            if not user.company_id.id == self.env.company.id:
                set_only = True
        if set_only:
            for key in vals.copy():
                if key not in ('name', 'lang', 'partner_id'):
                    del vals[key]
        return vals
