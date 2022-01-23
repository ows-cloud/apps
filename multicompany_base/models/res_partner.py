from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.depends('user_ids.company_ids')
    def _compute_company_ids(self):
        for record in self:
            record.company_ids = record.user_ids.mapped('company_ids')
    
    company_ids = fields.Many2many('res.company', string="Companies", compute='_compute_company_ids', store=True)
