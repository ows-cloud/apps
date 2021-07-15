from odoo import models, fields, api, exceptions

import logging
_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'

    donor_newsletter_delivery_method = fields.Char('Newsletter Delivery Method')
    donor_magazine_delivery_method = fields.Char('Magazine Delivery Method')
    donor_magazine_amount = fields.Integer('# of Magazines')
    donation_receipt_delivery_method = fields.Char('Donation Receipt Delivery Method')

    donation_address_state = fields.Char('Donation Address State')
    donation_country_group = fields.Char('Donation Country Group')
    donation_send_receipt = fields.Boolean('Send thank-you letter now')
    

class DonationCampaign(models.Model):
    _inherit = 'donation.campaign'

    image = fields.Binary()
    image_height = fields.Integer('Image Height')
    image_width = fields.Integer('Image Width')
    image_text = fields.Html()
    text1 = fields.Html()
    text2 = fields.Html()


class DonationTaxReceipt(models.Model):
    _inherit = 'donation.tax.receipt'

    campaign_id = fields.Many2one('donation.campaign', string='Donation Campaign')
    donor_newsletter_delivery_method = fields.Char('Newsletter Delivery Method', related='partner_id.donor_newsletter_delivery_method')
    donation_receipt_delivery_method = fields.Char('Donation Receipt Delivery Method', related='partner_id.donation_receipt_delivery_method')


class DonationLine(models.Model):
    _inherit = 'donation.line'

    description = fields.Char('Description')
