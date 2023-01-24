from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    json = fields.Serialized()
    l10n_no_Arbeidsgiveravgiftsone = fields.Selection(
        string="Sone",
        sparse="json",
        selection=[
            ("1", "1"),
            ("1a", "1a"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("4a", "4a"),
            ("5", "5"),

        ],
    )
    l10n_no_BeregningskodeForArbeidsgiveravgift = fields.Selection(
        string="Naeringskode",
        sparse="json",
        selection=[
            ("generelleNaeringer", "generelleNaeringer"),
            ("helseforetakOgDelerAvStatsforvaltningen", "helseforetakOgDelerAvStatsforvaltningen"),
            ("jordOgSkogbrukFiskeri", "jordOgSkogbrukFiskeri"),
            ("kunForskuddstrekk", "kunForskuddstrekk"),
            ("svalbard", "svalbard"),
            ("staalprodukterOgSkipsverft", "staalprodukterOgSkipsverft"),
            ("veitransport", "veitransport"),
            ("sektorunnattAktivitet", "sektorunnattAktivitet"),
            ("godstransportPaaVei", "godstransportPaaVei"),
        ],
    )
    l10n_no_fp_prosent = fields.Float("Feriepenger prosent", sparse="json")
    l10n_no_fp_prosent_senior = fields.Float(
        "Feriepenger prosent over 60 år", sparse="json"
    )
    l10n_no_Grunnlagsprosent = fields.Selection(
        string="Prosentsats for a.g.a.",
        sparse="json",
        selection=[
            ("14.1", "14.1"),
            ("10.6", "10.6"),
            ("7.9", "7.9"),
            ("6.4", "6.4"),
            ("5.1", "5.1"),
            ("0", "0"),
        ],
    )
    l10n_no_pensjonsinnretning = fields.Char(
        "Pensjonsinnretning org.nr.", sparse="json"
    )
    l10n_no_Spraak = fields.Selection(
        string="Spraak",
        sparse="json",
        selection=[
            ("bokmaal", "bokmaal"),
            ("engelsk", "engelsk"),
            ("nynorsk", "nynorsk"),
        ],
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
