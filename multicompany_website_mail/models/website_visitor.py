from odoo import models


class WebsiteVisitor(models.Model):
    _inherit = "website.visitor"

    _sql_constraints = [
        (
            "partner_uniq",
            "unique(partner_id, company_id)",
            "A partner is linked to only one visitor.",
        ),
    ]
