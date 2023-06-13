from odoo import api, models


class View(models.Model):
    _inherit = "ir.ui.view"

    @api.model
    def _get_inheriting_views_arch_domain(self, model):
        company_id_list = [1, self.env.company.id]
        parent_company = self.env.company.parent_id
        if parent_company:
            company_id_list.append(parent_company.id)
        return [
            ["model", "=", model],
            ["mode", "=", "extension"],
            ["active", "=", True],
            ["company_id", "in", tuple(company_id_list)],
        ]
