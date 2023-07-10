from odoo import models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # with_context is implemented in the patch
    def _get_price_total_and_subtotal(
        self,
        price_unit=None,
        quantity=None,
        discount=None,
        currency=None,
        product=None,
        partner=None,
        taxes=None,
        move_type=None,
    ):
        return super(
            AccountMoveLine,
            self.with_context(tax_date=self.date),
        )._get_price_total_and_subtotal(
            price_unit, quantity, discount, currency, product, partner, taxes, move_type
        )
