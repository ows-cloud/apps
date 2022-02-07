from odoo import api, fields, models, _
import re


class AccountMove(models.Model):
    _inherit = "account.move"

    @property
    def _sequence_fixed_regex(self):
        # From sequence_mixin
        _sequence_fixed_regex = r'^(?P<prefix1>.*?)(?P<seq>\d{0,9})(?P<suffix>\D*?)$'
        return _sequence_fixed_regex
