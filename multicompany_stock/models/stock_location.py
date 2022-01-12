from odoo import api, fields, models


class Location(models.Model):
    _inherit = 'stock.location'

    replace_record_id = fields.Many2one('stock.location', string='Replace Record')
    
    _sql_constraints = [('replace_stock_location_uniq', 'unique(replace_record_id, company_id)', 'Replace Record must be unique per company!')]
