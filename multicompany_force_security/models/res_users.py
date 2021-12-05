from odoo import models, fields, api
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        vals = self._remove_admin_access(vals)
        return super(Users, self).create(vals)

    def write(self, vals):
        vals = self._remove_admin_access(vals)
        return super(Users, self).write(vals)

    def _remove_admin_access(self, vals):
        admin_access = "sel_groups_{erp}_{system}".format(
            erp=str(self.env.ref('base.group_erp_manager').id),
            system=str(self.env.ref('base.group_system').id),
        )
        vals.pop(admin_access, None)
        return vals
