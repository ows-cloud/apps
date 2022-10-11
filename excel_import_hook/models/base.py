from odoo import api, fields, models

class Base(models.AbstractModel):
    _inherit = "base"

    def excel_post_import(self, one2many_field_name, _excel_post_import_=[]):
        for record in self:
            lines = getattr(record, one2many_field_name)
            for name in _excel_post_import_:
                method = "_excel_post_import_{}".format(name)
                api.call_kw(lines, method, [lines.ids], {})
