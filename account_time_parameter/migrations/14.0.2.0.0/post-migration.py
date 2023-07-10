from openupgradelib import openupgrade


def set_value_account_id(cr):
    openupgrade.logged_query(
        cr,
        """
            UPDATE base_time_parameter_version
            SET value_account_id = SPLIT_PART(value_reference,',',2)::int
            WHERE value_reference like 'account.account,%';
        """,
    )


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    set_value_account_id(cr)
