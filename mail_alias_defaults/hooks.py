from openupgradelib import openupgrade


def pre_init_hook(cr):
    try:
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
    except Exception:
        # alias_defaults_input may already exist.
        pass
