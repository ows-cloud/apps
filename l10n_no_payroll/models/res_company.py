from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    json = fields.Serialized()
    l10n_no_Arbeidsgiveravgiftsone = fields.Selection(
        selection=[],
        string="Sone",
        sparse="json",
    )
    l10n_no_BeregningskodeForArbeidsgiveravgift = fields.Selection(
        selection=[],
        string="Naeringskode",
        sparse="json",
    )
    l10n_no_fp_prosent = fields.Float("Feriepenger prosent", sparse="json")
    l10n_no_fp_prosent_senior = fields.Float(
        "Feriepenger prosent over 60 år", sparse="json"
    )
    l10n_no_Grunnlagsprosent = fields.Selection(
        selection=[],
        string="Prosentsats for a.g.a.",
        sparse="json",
    )
    l10n_no_pensjonsinnretning = fields.Char(
        "Pensjonsinnretning org.nr.", sparse="json"
    )
    l10n_no_Spraak = fields.Selection(
        selection=[],
        string="Spraak",
        sparse="json",
    )
    l10n_no_virksomhet = fields.Char("Virksomhetsnummer", sparse="json")

    l10n_no_aga_konto = fields.Many2one(
        "account.account",
        string="Arbeidsgiveravgift konto",
        sparse="json",
    )
    l10n_no_aga_motkonto = fields.Many2one(
        "account.account",
        string="Arbeidsgiveravgift motkonto",
        sparse="json",
    )
    l10n_no_fp_konto = fields.Many2one(
        "account.account",
        string="Feriepenger konto",
        sparse="json",
    )
    l10n_no_fp_motkonto = fields.Many2one(
        "account.account",
        string="Feriepenger motkonto",
        sparse="json",
    )
    l10n_no_aga_fp_konto = fields.Many2one(
        "account.account",
        string="A.g.a. av feriepenger konto",
        sparse="json",
    )
    l10n_no_aga_fp_motkonto = fields.Many2one(
        "account.account",
        string="A.g.a. av feriepenger motkonto",
        sparse="json",
    )
    l10n_no_loennsart_fp_i_aar = fields.Many2one(
        "hr.salary.rule",
        string="Lønnsart feriepenger i år",
        sparse="json",
    )
    l10n_no_loennsart_fp_i_fjor = fields.Many2one(
        "hr.salary.rule",
        string="Lønnsart feriepenger i fjor",
        sparse="json",
    )
