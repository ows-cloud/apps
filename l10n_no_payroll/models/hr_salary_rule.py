from odoo import fields, models


class SalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    json = fields.Serialized()
    l10n_no_BeregnAga = fields.Selection(
        selection=[],
        string="Beregn arbeidsgiveravgift",
        sparse="json",
    )
    l10n_no_BeregnFP = fields.Boolean(
        selection=[],
        string="Beregn feriepenger",
        sparse="json",
    )
    l10n_no_BeregnTrekk = fields.Selection(
        selection=[],
        string="Beregn skattetrekk",
        sparse="json",
    )
    l10n_no_Fordel = fields.Selection(
        selection=[],
        string="Fordel",
        sparse="json",
    )
    l10n_no_Forskuddstrekkbeskrivelse = fields.Selection(
        selection=[],
        string="Forskuddstrekkbeskrivelse",
        sparse="json",
    )
    l10n_no_Loennsbeskrivelse = fields.Selection(
        selection=[],
        string="Loennsbeskrivelse",
        sparse="json",
    )
    l10n_no_RegelType = fields.Selection(
        selection=[],
        string="Regeltype",
        sparse="json",
    )
    l10n_no_SkatteOgAvgiftsregel = fields.Selection(
        selection=[],
        string="SkatteOgAvgiftsregel",
        sparse="json",
    )
