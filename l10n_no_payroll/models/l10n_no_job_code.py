import logging

from odoo import fields, models

from .hr_job_codes import hr_job_codes

_logger = logging.getLogger(__name__)


class JobCode(models.Model):
    _name = "l10n.no.job.code"

