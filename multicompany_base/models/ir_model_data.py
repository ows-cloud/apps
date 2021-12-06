from odoo import api, fields, models


MODELS = [
    'mail.channel',
    'mail.template',
]


class IrModelData(models.Model):
    _inherit = 'ir.model.data'
    
    @api.model
    def xmlid_lookup(self, xmlid):
        id, model, res_id = super(IrModelData, self).xmlid_lookup(xmlid)
        if model in MODELS:
            try:
                # 'replace_record_id' might not exist
                result = self.env[model].search([('replace_record_id', '=', res_id)])
                if result:
                    result.ensure_one()
                    res_id = result.id
            except:
                pass
        return id, model, res_id
