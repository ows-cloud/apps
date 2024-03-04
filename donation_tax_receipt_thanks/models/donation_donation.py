import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Donation(models.Model):
    _inherit = "donation.donation"

    lang = fields.Selection(related="partner_id.lang")
