from odoo import models


class View(models.Model):
    _inherit = "ir.ui.view"

    def action_add_child_view(self):
        self.ensure_one()
        context = {
            "default_name": self.name + " for " + self.env.company.name,
            "default_type": self.type,
            "default_model": self.model,
            "default_inherit_id": self.id,
            "default_mode": "extension",
        }
        return {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "ir.ui.view",
            "target": "current",
            "context": context,
        }

    def action_open_child_view(self):
        self.ensure_one()
        return {
            "name": self.display_name,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "ir.ui.view",
            "res_id": self.id,
            "target": "current",
        }
