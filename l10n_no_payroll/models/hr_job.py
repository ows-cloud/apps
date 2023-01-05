import logging

from odoo import fields, models

from .hr_job_codes import hr_job_codes

_logger = logging.getLogger(__name__)


class Job(models.Model):
    _inherit = "hr.job"

    json = fields.Serialized()
    l10n_no_profession_code = fields.Selection(
        selection=[],
        string="Yrkeskode",
        sparse="json",
    )

    def l10n_no_import_profession(self):
        SelectValue = self.env["res.field.selection_value"]
        field_id = self.env.ref("l10n_no_payroll.res_field_l10n_no_profession_code").id
        records = SelectValue.search_count([("field_id", "=", field_id)])
        if not records:
            for line in hr_job_codes.splitlines():
                SelectValue.create(
                    {
                        "field_id": field_id,
                        "code": line[:4] + line[5:8],
                        "name": line[9:],
                    }
                )
