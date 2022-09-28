from odoo import fields, models

class Base(models.AbstractModel):
    _inherit = "base"

    def excel_post_import_hook(self, one2many_field_name):
        for record in self:
            for line in getattr(record, one2many_field_name):
                line.excel_post_import_hook_for_record_line()
            record.excel_post_import_hook_for_record()

    def _excel_post_import_hook_for_record(self):
        self.ensure_one()

    def _excel_post_import_hook_for_record_line(self):
        self.ensure_one()
