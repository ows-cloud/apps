import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DonationTaxReceipt(models.Model):
    _inherit = "donation.tax.receipt"

    def _compute_thanks_template_id(self):
        for rec in self:
            rec.thanks_template_id = rec.donation_ids.thanks_template_id.id or False

    thanks_template_id = fields.Many2one(
        "donation.thanks.template",
        string="Thanks Template",
        compute="_compute_thanks_template_id",
    )
    donor_newsletter_delivery_method = fields.Selection(
        "Newsletter Delivery",
        related="partner_id.donor_newsletter_delivery_method",
    )
    donor_receipt_delivery_method = fields.Selection(
        "Receipt Delivery",
        related="partner_id.donor_receipt_delivery_method",
    )
    donor_address_state = fields.Selection(
        "Address State", related="partner_id.donor_address_state"
    )



