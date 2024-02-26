from datetime import datetime

from odoo import api, fields, models


class Users(models.Model):
    _inherit = "res.users"

    def _default_groups(self):
        default_user = self.with_context(active_test=False).search(
            [("default_user", "=", True), ("company_id", "=", self.env.company.id)]
        )
        return default_user.groups_id if default_user else []

    default_user = fields.Boolean("Default User Template")
    groups_id = fields.Many2many(default=_default_groups)

    # TODO: Allow multiple non-default users per company!
    _sql_constraints = [
        (
            "default_user_uniq",
            "unique(default_user, company_id)",
            "Default User must be unique per company!",
        )
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals = self._remove_admin_access(vals)
            if "default_user" in vals and vals["default_user"] == False:
                vals.pop("default_user")
        return super(Users, self).create(vals)

    def write(self, vals):
        vals = self._remove_admin_access(vals)
        vals = self._if_other_company_and_not_su_set_only_name_lang_partner(vals)
        return super(Users, self).write(vals)

    def _remove_admin_access(self, vals):
        self_sudo = self.sudo().bypass_company_rules()
        admin_access = "sel_groups_{erp}_{system}".format(
            erp=str(self_sudo.env.ref("base.group_erp_manager").id),
            system=str(self_sudo.env.ref("base.group_system").id),
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
                if key not in ("name", "lang", "partner_id"):
                    del vals[key]
        return vals

    @api.model
    def _update_last_login(self):
        # Security rules combined with website module causes a loop.
        # We create res.users.log directly with SQL to avoid the loop.
        user_id = str(self.env.user.id)
        now = str(datetime.now())
        company_id = str(self.env.company.id)
        sql = """INSERT INTO res_users_log (
            id, create_uid, create_date, write_uid, write_date, company_id
        ) VALUES (nextval('res_users_log_id_seq'), {}, '{}', {}, '{}', {});""".format(
            user_id, now, user_id, now, company_id
        )
        self.env.cr.execute(sql)
