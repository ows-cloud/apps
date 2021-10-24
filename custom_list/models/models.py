from odoo import api, fields, models


class CustomList(models.Model):
    _name = 'custom.list'
    _description = 'Custom List'
    
    company_id = fields.Many2one('res.company', string="Company", index=True, default=lambda self: self.env.company)
    name = fields.Char()
    type = fields.Selection([('budget', 'Budget'), ('other', 'Other')])


class CustomListItem(models.Model):
    _name = 'custom.list.item'
    _description = 'Custom List Item'

    name = fields.Char()

    account_id = fields.Many2one('account.account', string="Account")
    analytic_account_id = fields.Many2one('account.analytic.account', string="Anaytic Account")
    company_id = fields.Many2one('res.company', string="Company", index=True, default=lambda self: self.env.company)
    date=fields.Date()
    list_id = fields.Many2one('custom.list', string="Custom List")
    
    def compute_default_user(self):
        return self.env.user
    user_id = fields.Many2one('res.users', string="User", default=compute_default_user)

    float = fields.Float()
