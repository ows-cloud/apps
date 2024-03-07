import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class DonationLine(models.Model):
    _inherit = "donation.line"

    def _compute_analytic_description(self):
        for line in self:
            line.analytic_description = line.analytic_account_id.with_context(
                lang=line.donation_id.partner_id.lang
            ).donation_description

    analytic_description = fields.Char(
        string="Description",
        compute="_compute_analytic_description",
    )
