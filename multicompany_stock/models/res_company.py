from odoo import api, fields, models


class Company(models.Model):
    _inherit = 'res.company'

    def configure_stock(self):
        companies = self
        self.env['multicompany.config']._configure_stock(companies)
