from odoo import fields, models


class IrModelData(models.Model):
    _inherit = 'ir.model.data'

    company_id = fields.Many2one('res.company', string='Company')
