from odoo import tools
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    tools.drop_view_if_exists(env.cr, "account_budget_report")
