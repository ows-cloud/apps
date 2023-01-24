from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    env["l10n.no.job.code"].post_init_hook_import_job_codes()
    env["l10n.no.tabelltrekk"].post_init_hook_import_tax_deduction_tables()

    """ Manually migrate away from res.field - open record in form view, Action: Migrate"""
    # env["res.field"].set_standard_info_in_fields()
    # env["res.field"].create_custom_info()
