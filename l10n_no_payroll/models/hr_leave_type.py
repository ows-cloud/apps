from odoo import fields, models


class LeaveType(models.Model):
    _inherit = "hr.leave.type"

    json = fields.Serialized()
    l10n_no_PermisjonsOgPermitteringsBeskrivelse = fields.Selection(
        string="PermisjonsOgPermitteringsBeskrivelse",
        sparse="json",
        selection=[
            ("permittering", "permittering"),
            ("permisjonMedForeldrepenger", "permisjonMedForeldrepenger"),
            ("permisjonVedMilitaertjeneste", "permisjonVedMilitaertjeneste"),
            ("utdanningspermisjon", "utdanningspermisjon"),
            ("velferdspermisjon", "velferdspermisjon"),
        ],
    )
