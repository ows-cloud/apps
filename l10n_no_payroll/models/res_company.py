from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    json = fields.Serialized()
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
