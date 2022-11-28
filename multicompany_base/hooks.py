from odoo import SUPERUSER_ID, api

from .models.multicompany_security import SECURITY_DO_IF


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # SET DEFAULT USER
    env.ref("base.default_user").default_user = True
    # SET PARAMETERS
    ICP = env["ir.config_parameter"].sudo()
    default_settings = [
        ("multicompany_base.force_security", "1"),
        ("multicompany_base.force_security_company_manager", "1"),
        ("multicompany_base.force_config", "1"),
    ]
    for key, value in default_settings:
        if not ICP.get_param(key):
            ICP.set_param(key, value)
    # SUPPORT USER
    support_user = env.ref(
        "__multicompany_base__.support_user", raise_if_not_found=False
    )
    if not support_user:
        companies = env["res.company"].sudo().search([])
        support_user = (
            env["res.users"]
            .sudo()
            .create(
                {
                    "login": "support",
                    "lang": "en_US",
                    "name": "Support User",
                    "company_ids": [(6, 0, companies.ids)],
                    "groups_id": [
                        (4, env.ref("multicompany_base.group_company_manager").id),
                        (4, env.ref("base.group_partner_manager").id),
                    ],
                }
            )
        )
        env["ir.model.data"].create(
            {
                "module": "__multicompany_base__",
                "name": "support_user",
                "model": "res.users",
                "res_id": support_user.id,
            }
        )


def WARNING_DELETE_RULES_uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Delete global rules
    for do_if in SECURITY_DO_IF:
        rules = env["ir.rule"].search(
            [("name", "ilike", "% - %_model%{}".format(do_if))]
        )
        rules.unlink()
    # Delete company manager access and rules
    group = env.ref("multicompany_base.group_company_manager")
    group.model_access.unlink()
    for rule in group.rule_groups:
        if rule.name == "res.partner.rule.private.group":
            pass
        if len(rule.groups) > 1:
            rule.write({"groups": [(3, group.id, 0)]})
        else:
            rule.unlink()
