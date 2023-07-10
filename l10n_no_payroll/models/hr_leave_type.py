from odoo import fields, models


class LeaveType(models.Model):
    _inherit = "hr.leave.type"

    json = fields.Serialized()
    l10n_no_PermisjonsOgPermitteringsBeskrivelse = fields.Selection(
        string="PermisjonsOgPermitteringsBeskrivelse",
        sparse="json",
        selection=[
            ("permittering", "Permittering"),
            ("permisjonMedForeldrepenger", "Permisjon med foreldrepenger"),
            ("permisjonVedMilitaertjeneste", "Permisjon ved militærtjeneste"),
            ("utdanningspermisjonLovfestet", "Utdanningspermisjon, lovfestet"),
            ("utdanningspermisjonIkkeLovfestet", "Utdanningspermisjon, ikke lovfestet"),
            ("andreLovfestedePermisjoner", "Andre lovfestede permisjoner"),
            ("andreIkkeLovfestedePermisjoner", "Andre ikke lovfestede permisjoner"),
        ],
    )
