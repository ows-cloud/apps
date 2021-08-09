from odoo import api, fields, models


class CustomList(models.Model):
    _name = 'custom.list'
    
    company_id = fields.Many2one('res.company', string="Company", index=True, default=lambda self: self.env.user.company_id)
    name = fields.Char()
    type = fields.Selection([('budget', 'Budget'), ('other', 'Other')])
    uom = fields.Many2one('uom.uom', string="Unit of Measure")


class CustomListItem(models.Model):
    _name = 'custom.list.item'

    name = fields.Char()
    uom = fields.Many2one('uom.uom', string="Unit of Measure", readonly=True, related='list_id.uom')

    account_id = fields.Many2one('account.account', string="Account")
    analytic_account_id = fields.Many2one('account.analytic.account', string="Anaytic Account")
    company_id = fields.Many2one('res.company', string="Company", index=True, default=lambda self: self.env.user.company_id)
    date=fields.Date()
    list_id = fields.Many2one('custom.list', string="Custom List")
    
    def compute_default_user(self):
        return self.env.user
    user_id = fields.Many2one('res.users', string="User", default=compute_default_user)

    #char = fields.Char()
    float = fields.Float()
    #integer = fields.Integer()
    #monetary = fields.Monetary()
