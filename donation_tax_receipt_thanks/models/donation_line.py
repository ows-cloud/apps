import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DonationLine(models.Model):
    _inherit = "donation.line"

    description = fields.Char("Description")
