from odoo import api, models


class View(models.Model):
    _inherit = 'ir.ui.view'

    @api.model
    def _get_inheriting_views_arch_domain(self, model):
        return [
            ['model', '=', model],
            ['mode', '=', 'extension'],
            ['active', '=', True],
            ['company_id', 'in', (1, self.env.company.id)],
        ]
