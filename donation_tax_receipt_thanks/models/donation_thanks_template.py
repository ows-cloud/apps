import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DonationThanksTemplate(models.Model):
    _inherit = "donation.thanks.template"

    image_height = fields.Integer("Image Height")
    image_width = fields.Integer("Image Width")
    image_text = fields.Html()
    # image2 = fields.Binary(attachment=True)
    # image2_height = fields.Integer("Image Height")
    # image2_width = fields.Integer("Image Width")
    # image2_text = fields.Html()
    text1 = fields.Html()
    text2 = fields.Html()
