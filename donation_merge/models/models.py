from odoo import models, fields, api, exceptions

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    donor_newsletter_delivery_method = fields.Char('Newsletter Delivery Method')
    donor_magazine_delivery_method = fields.Char('Magazine Delivery Method')
    donation_receipt_delivery_method = fields.Char('Donation Receipt Delivery Method')

    donation_address_state = fields.Char('Donation Address State')
    donation_country_group = fields.Char('Donation Country Group')
    donation_send_receipt = fields.Boolean('Donation Send Receipt')
    

class DonationCampaign(models.Model):
    _inherit = 'donation.campaign'

    image = fields.Binary()
    letter = fields.Html()