from odoo import models


class IrModelData(models.Model):
    _inherit = "ir.model.data"

    # TODO: make sure ir.model.data has company_id when ...
    # ... exporting records (__ensure_xml_id not running, use patch instead)
    # ... installing modules
    # TODO: test
    def create(self, values):
        if "company_id" not in values:
            record = self.env[values["model"]].browse(values["res_id"])
            values["company_id"] = record.company_id.id
        super(IrModelData, self).create(values)
