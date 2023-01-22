from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env["l10n.no.job.code"].post_init_hook_import_job_codes()
