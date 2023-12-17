from odoo.addons.website_sale.controllers.main import WebsiteSale



class WebsiteSale2(WebsiteSale):


    def _get_mandatory_billing_fields(self):
        # return ["name", "email", "street", "city", "country_id"]
        return ["name"]

    def _get_mandatory_shipping_fields(self):
        # return ["name", "street", "city", "country_id"]
        return ["name"]
