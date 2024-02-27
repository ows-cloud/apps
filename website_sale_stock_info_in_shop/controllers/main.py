from odoo.addons.website_sale_delivery.controllers.main import WebsiteSaleDelivery


class WebsiteSaleDonation(WebsiteSaleDelivery):

    def _get_mandatory_fields_billing(self, country_id=False):
        # return ["name", "email", "street", "city", "country_id"]
        return ["name"]

    def _get_mandatory_fields_shipping(self, country_id=False):
        # return ["name", "street", "city", "country_id"]
        return ["name"]

    def _get_shop_payment_values(self, order, **kwargs):
        values = super(WebsiteSaleDonation, self)._get_shop_payment_values(order, **kwargs)
        has_storable_products = any(
            line.product_id.type in ['consu', 'product'] and not line.product_id.is_donation
            for line in order.order_line
        )
        values['delivery_has_storable'] = has_storable_products
        if not has_storable_products:
            values.pop("deliveries", None)
            values.pop("delivery_action_id", None)
        return values
