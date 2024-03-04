import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    def _compute_donor_send_receipt(self):
        for partner in self:
            if partner.tax_receipt_ids.filtered(lambda r: not r.print_date):
                partner.donor_send_receipt = True
            else:
                partner.donor_send_receipt = False

    donor_newsletter_delivery_method = fields.Selection(
        selection=[("N", "Nei"), ("P", "Ja, per post"), ("E", "Ja, per e-post")],
        string="Newsletter Delivery",
    )
    donor_magazine_delivery_method = fields.Selection(
        selection=[("N", "Nei"), ("P", "Ja, per post"), ("E", "Ja, per e-post")],
        string="Magazine Delivery",
    )
    donor_magazine_amount = fields.Integer("# of Magazines")
    donor_receipt_delivery_method = fields.Selection(
        selection=[("N", "Nei"), ("P", "Ja, per post"), ("E", "Ja, per e-post")],
        string="Receipt Delivery Method",
    )

    donor_address_state = fields.Selection(
        selection=[
            ("AS", "Adresse midl. stopp"),
            ("OK", "Adresse OK"),
            ("AM", "Adresse ufullstendig"),
            ("AU", "Adresse ukjent"),
        ],
        string="Donor Address State",
    )
    donor_send_receipt = fields.Boolean(
        string="Send thank-you letter now",
        compute="_compute_donor_send_receipt",
    )
    tax_receipt_option = fields.Selection(default="annual")
