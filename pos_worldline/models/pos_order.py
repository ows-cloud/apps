import requests

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def create_from_ui(self, orders, draft=False):
        # assert len(orders) == 1, "Just one order please"
        if len(orders) == 1:
            pricelist = self.env["product.pricelist"].browse(orders[0]["data"]["pricelist_id"])
            currency = pricelist.currency_id
            for statement in orders[0]["data"]["statement_ids"]:
                payment_method = self.env["pos.payment.method"].browse(statement[2]["payment_method_id"])
                if payment_method.use_payment_terminal == "worldline":
                    json = {
                        "payload": {
                            "amounts": {
                                "currencySymbol": currency.name,
                                "base": round(statement[2]["amount"], currency.decimal_places),
                            }
                        }
                    }
                    request = requests.post(
                        "{}/pay".format(payment_method.worldline_host), json=json, # headers=headers
                    )
                    if request.status_code == 200:
                        json = request.json()
                        # Store print message
                        if True:
                            return super().create_from_ui(orders, draft)
                    else:
                        raise Exception(
                            "Worldline payment failed to run by returning code of {}.".format(
                                request.status_code
                            )
                        )
        return super().create_from_ui(orders, draft)
