from odoo import api, fields, models


class Base(models.AbstractModel):
    _inherit = 'base'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.company)

    """
    When the active company is not the user's default company,
    controllers may not know the company of a record,
    and sudo() is necessary to find out.
    In patches to fix controllers,
    the methods .my_company() and .with_my_company() are often very useful,
    and sudo() is only one place here, not in every controller patch.
    """

    def with_my_company(self):
        return self.with_company(self.my_company())

    def my_company(self):
        company = self.sudo().mapped('company_id')
        assert len(company) == 1
        return company
