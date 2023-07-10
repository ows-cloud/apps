from odoo import _, models
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = "res.users"

    def write(self, vals):
        if "partner_id" in vals or ("name" in vals and "lang" in vals):
            vals = self._set_partner(vals)
        return super(Users, self).write(vals)

    def _set_partner(self, vals):
        users = self
        for user in users:
            if not user.partner_id:
                if len(users) > 1:
                    raise UserError(
                        _(
                            "You cannot update multiple users when not all users have " + \
                            "a related partner for the company."
                        )
                    )
                vals = user._create_partner(vals)
                user.flush()
        if "partner_id" in vals and vals["partner_id"]:
            if len(users) > 1:
                raise UserError(
                    _("You cannot update multiple users with the same partner.")
                )
        return vals

    def _create_partner(self, vals):
        self.ensure_one()
        partner = self.env["res.partner"].create(
            {
                "name": vals["name"],
                "lang": vals["lang"],
            }
        )
        vals.pop("name")
        vals.pop("lang")
        vals["partner_id"] = partner
        return vals
