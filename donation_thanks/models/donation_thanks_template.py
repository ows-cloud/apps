import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DonationThanksTemplate(models.Model):
    _inherit = "donation.thanks.template"

    image_height = fields.Integer("Image Height")
    image_width = fields.Integer("Image Width")
    image_text = fields.Html(
        sanitize=False, # Gives the best UI for translation
        translate=True,
    )
    text1 = fields.Html(
        sanitize=False, # Gives the best UI for translation
        translate=True,
    )
    text2 = fields.Html(
        sanitize=False, # Gives the best UI for translation
        translate=True,
    )
