from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["l10n.no.job.code"].post_init_hook_import_job_codes()
    env["l10n.no.tabelltrekk"].post_init_hook_import_tax_deduction_tables()
