import requests

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    worldline_host = fields.Char()
    worldline_key = fields.Char()

    def _get_payment_terminal_selection(self):
        return super(PosPaymentMethod, self)._get_payment_terminal_selection() + [("worldline", "Worldline")]
