from odoo import fields, models


class LeaveType(models.Model):
    _inherit = "hr.leave.type"

    json = fields.Serialized()
    l10n_no_PermisjonsOgPermitteringsBeskrivelse = fields.Selection(
        selection=[],
        string="PermisjonsOgPermitteringsBeskrivelse",
        sparse="json",
    )
