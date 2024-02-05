from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    cart_quantity = fields.Integer(compute='_compute_cart_info')
    only_services = fields.Boolean(compute='_compute_cart_info')
    only_donations = fields.Boolean(compute='_compute_cart_info')

    @api.depends('order_line.product_uom_qty', 'order_line.product_id')
    def _compute_cart_info(self):
        for order in self:
            order.cart_quantity = int(
                sum(order.mapped('website_order_line.product_uom_qty'))
            )
            order.only_services = all(
                l.product_id.type in ('service', 'digital') or l.product_id.is_donation
                for l in order.website_order_line
            )
            order.only_donations = all(
                l.product_id.is_donation
                for l in order.website_order_line
            )

    is_all_service = fields.Boolean("Service Product", compute="_compute_is_service_products")

    @api.depends('order_line')
    def _compute_is_service_products(self):
        for so in self:
            so.is_all_service = all(
                line.product_id.type == 'service' or line.product_id.is_donation
                for line in so.order_line.filtered(lambda x: not x.display_type)
            )
