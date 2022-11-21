from odoo import _, models
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    def open_default_user(self):
        action = self.env["ir.actions.actions"]._for_xml_id("base.action_res_users")
        default_user = self.env["res.users"].search(
            [("default_user", "=", True), ("company_id", "=", self.env.company.id)]
        )
        if not default_user:
            default_user = self.env["res.users"].search([("default_user", "=", True)])
        if default_user:
            if len(default_user) == 1:
                action["res_id"] = default_user.id
            else:
                raise UserError(
                    _(
                        "Multiple Default User Templates, in {}.".format(
                            ", ".join(
                                [
                                    c.name
                                    for c in default_user.mapped("company_id").mapped(
                                        "name"
                                    )
                                ]
                            )
                        )
                    )
                )
        else:
            raise UserError(_("Default User Template not found."))
        action["views"] = [[self.env.ref("base.view_users_form").id, "form"]]
        return action
