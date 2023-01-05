"""
This code was written previously to get from regular field to res.field.
In the migration we want to do the opposite.
"""


def _compute_l10n_no_fields(self):
    for record in self:
        record.l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer = float(
            record.field_value_ids.filtered(
                lambda x: x.field_code
                == "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer"
            ).value
        )
        record.l10n_no_stillingsprosent = float(
            record.field_value_ids.filtered(
                lambda x: x.field_code == "l10n_no_stillingsprosent"
            ).value
        )
