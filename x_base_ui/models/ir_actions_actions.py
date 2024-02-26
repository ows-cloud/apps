from odoo import api, models


class IrActionsActions(models.Model):
    _inherit = "ir.actions.actions"

    # Migration to version 16.0
    # If you are overriding name_search method in your module, you may make use now of new _rec_names_search
    # class variable to expose the fields to search for without requiring the method override.
    # More details at https://github.com/odoo/odoo/commit/3155c3e425581b71491844e7f9a3dd76a9f245a4.
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        ids = self._name_search(name, args, operator, limit=limit)
        records = self.browse(ids)
        return [(rec.id, "{} (id {})".format(rec.name, rec.id)) for rec in records]
