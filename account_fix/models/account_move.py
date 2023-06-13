from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @property
    def _sequence_fixed_regex(self):
        # From sequence_mixin
        _sequence_fixed_regex = r"^(?P<prefix1>.*?)(?P<seq>\d{0,9})(?P<suffix>\D*?)$"
        return _sequence_fixed_regex

    @api.depends("posted_before", "state", "journal_id", "date")
    def _compute_name(self):
        state = self.mapped("state")
        if not "draft" in state:
            super(AccountMove, self)._compute_name()

    @api.onchange("invoice_date")
    def _onchange_invoice_date(self):
        self.date = self.invoice_date
