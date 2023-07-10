from odoo import api, models


class Base(models.AbstractModel):
    _inherit = "base"

    def excel_post_import(self, one2many_field_name, excel_post_import_=[]):
        for record in self:
            lines = getattr(record, one2many_field_name)
            for name in excel_post_import_:
                method = "excel_post_import_{}".format(name)
                api.call_kw(lines, method, [lines.ids], {})
