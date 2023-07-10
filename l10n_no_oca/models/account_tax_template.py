from odoo import fields, models

class TaxTemplate(models.Model):
    _inherit = "account.tax.template"

    l10n_no_account_id = fields.Many2one(
        "account.account.template",
        string="Account",
        help="Temporary field for the related account",
    )
    l10n_no_refund_account_id = fields.Many2one(
        "account.account.template",
        string="Refund Account",
        help="Temporary field for the related account",
    )
