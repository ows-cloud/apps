from odoo import fields, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    json = fields.Serialized()
    l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer = fields.Float(
        "Antall timer per uke som en full stilling tilsvarer", sparse="json"
    )
    l10n_no_Arbeidsforholdtype = fields.Selection(
        selection=[],
        string="Type arbeidsforhold",
        sparse="json",
    )
    l10n_no_Arbeidstidsordning = fields.Selection(
        selection=[],
        string="Arbeidstidsordning",
        sparse="json",
    )
    l10n_no_FormForAnsettelse = fields.Selection(
        selection=[],
        string="Form for ansettelse",
        sparse="json",
    )
    l10n_no_loennsansiennitet = fields.Date("Dato for lønnsansiennitet", sparse="json")
    l10n_no_loennstrinn = fields.Char("Loennstrinn", sparse="json")
    l10n_no_sisteDatoForStillingsprosentendring = fields.Date(
        "Dato for siste stillingsprosentendring", sparse="json"
    )
    l10n_no_sisteLoennsendringsdato = fields.Date(
        "Dato for siste lønnsendring", sparse="json"
    )
    l10n_no_stillingsprosent = fields.Float("Stillingsprosent", sparse="json")
    l10n_no_AarsakTilSluttdato = fields.Selection(
        selection=[],
        string="Årsak til sluttdato",
        sparse="json",
    )
