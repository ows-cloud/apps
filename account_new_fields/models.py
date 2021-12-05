from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AccountAccount(models.Model):
    _inherit = "account.account"

    include_initial_balance = fields.Boolean("Bring Accounts Balance Forward", related="user_type_id.include_initial_balance", store=False, readonly=True)


class AccountAccountType(models.Model):
    _inherit = "account.account.type"
    _order = 'note'


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"
    _order = 'description'

    user_id = fields.Many2one('res.users', string='Manager', ondelete='restrict')
    
    
# fixed in 14.0?
# class AccountInvoiceLine(models.Model):
#     _inherit = "account.invoice.line"

#     # - @api.one
#     # - def _compute_price(self):
#     # + def _compute_price(s):
#     # +     for self in s:
#     # +         self.price_total = taxes['total_included'] if taxes else self.price_subtotal
#     # + price_total = fields.Monetary(string='Amount',
#     # +     store=True, readonly=True, compute='_compute_price', help="Total amount with taxes")
#     @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
#                  'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
#                  'invoice_id.date_invoice', 'invoice_id.date')
#     def _compute_price(s):
#         for self in s:
#             currency = self.invoice_id and self.invoice_id.currency_id or None
#             price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
#             taxes = False
#             if self.invoice_line_tax_ids:
#                 taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id,
#                                                               partner=self.invoice_id.partner_id)
#             self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.quantity * price
#             self.price_total10 = taxes['total_included'] if taxes else self.price_subtotal
#             if self.invoice_id.currency_id and self.invoice_id.company_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
#                 price_subtotal_signed = self.invoice_id.currency_id.with_context(
#                     date=self.invoice_id._get_currency_rate_date()).compute(price_subtotal_signed,
#                                                                             self.invoice_id.company_id.currency_id)
#             sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
#             self.price_subtotal_signed = price_subtotal_signed * sign

#     price_total10 = fields.Monetary(string='Amount',
#                                   store=True, readonly=True, compute='_compute_price', help="Total amount with taxes")
#     price_subtotal = fields.Monetary(compute='_compute_price')
#     price_subtotal_signed = fields.Monetary(compute='_compute_price')

#     company_id = fields.Many2one(related='', default=lambda self: self.env.company)


class AccountAnalyticGroup(models.Model):
    _inherit = 'account.analytic.group'
    _order = 'name'