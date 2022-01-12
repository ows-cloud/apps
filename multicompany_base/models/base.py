from odoo import api, fields, models

MODELS_WITH_REPLACE_RECORD_ID = [
    'mail.channel',
    'mail.template',
    'res.users',
    'stock.location',
]


class Base(models.AbstractModel):
    _inherit = 'base'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.company)

    """
    XMLID FOR MULTICOMPANY
    Replace res_id if 'replace_record_id' exists.
    """

    @api.model
    def xmlid_lookup(self, xmlid):
        id, model, res_id = super(Base, self).xmlid_lookup(xmlid)
        if model in MODELS_WITH_REPLACE_RECORD_ID:
            try:
                # 'replace_record_id' might not exist
                result = self.env[model].search([('replace_record_id', '=', res_id)])
                if result:
                    result.ensure_one()
                    res_id = result.id
            except:
                pass
        return id, model, res_id
