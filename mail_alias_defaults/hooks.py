from openupgradelib import openupgrade


def pre_init_hook(cr):
    openupgrade.rename_columns(
        cr,
        {
            "mail_alias":
            [
                (
                    "alias_defaults",
                    "alias_defaults_input",
                )
            ]
        }
    )
