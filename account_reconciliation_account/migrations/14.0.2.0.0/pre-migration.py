from openupgradelib import openupgrade


def rename_fields(env):
    openupgrade.rename_fields(
        env,
        [
            (
                "account.bank.statement.line",
                "account_bank_statement_line",
                "counterpart_account_id",
                "account_id",
            ),
            (
                "account.reconcile.model",
                "account_reconcile_model",
                "match_counterpart_account_id",
                "match_account_id",
            ),
        ],
    )


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    rename_fields(env)
