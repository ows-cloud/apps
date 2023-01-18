from odoo import fields, models


class Job(models.Model):
    _inherit = "hr.job"

    json = fields.Serialized()
    l10n_no_job_code = fields.Many2one(
        comodel_name="l10n.no.job.code",
        string="Profession Code",
        sparse="json",
    )
