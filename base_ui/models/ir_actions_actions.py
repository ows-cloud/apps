from odoo import api, models


class IrActionsActions(models.Model):
    _inherit = "ir.actions.actions"

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        ids = self._name_search(name, args, operator, limit=limit)
        records = self.browse(ids)
        return [(rec.id, "{} (id {})".format(rec.name, rec.id)) for rec in records]
