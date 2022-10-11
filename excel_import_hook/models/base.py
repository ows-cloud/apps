from odoo import api, fields, models

class Base(models.AbstractModel):
    _inherit = "base"

    def excel_post_import_hook(self, one2many_field_name, _excel_post_import_hook_=[]):
        for record in self:
            for line in getattr(record, one2many_field_name):
                for name in _excel_post_import_hook_:
                    method = "_excel_post_import_hook_{}".format(name)
                    api.call_kw(self, method, [line.ids], {})
