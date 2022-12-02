from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})

    openupgrade.rename_tables(
        cr,
        [
            ("hr_rule_qty_rate_amount", "hr_payslip_line_manually"),
        ],
    )
    openupgrade.rename_fields(
        env,
        [
            (
                "hr.salary.rule",
                "hr_salary_rule",
                "qty_rate_amount_from",
                "line_manually_model",
            ),
        ],
    )


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    for rule in env["hr.salary.rule"].sudo_bypass_global_rules().search([]):
        if "qty_rate_amount_ids" in rule.condition_python:
            rule.condition_python = rule.condition_python.replace(
                "qty_rate_amount_ids", "line_manually_ids"
            )
        if "qty_rate_amount_ids" in rule.amount_python_compute:
            rule.amount_python_compute = rule.amount_python_compute.replace(
                "qty_rate_amount_ids", "line_manually_ids"
            )
