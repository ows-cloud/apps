from odoo import api, fields, models
from odoo.addons.json_field.json import JsonField


class Company(models.Model):
    _inherit = 'res.company'

    json = JsonField(default={"xmlid":{}})

    @api.model
    def create(self, vals):
        new_company = super(Company, self.sudo()).create(vals)
        self.env['company.configure']._configure(new_company)
        return new_company

    def configure(self):
        companies = self
        self.env['company.configure']._configure(companies)
