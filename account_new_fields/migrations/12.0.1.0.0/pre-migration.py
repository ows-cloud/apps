# Copyright 2019 Apps2GROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

def analytic_tag_to_analytic_group(cr):

    # account.analytic.tag
    cr.execute("SELECT id FROM account_analytic_tag ORDER BY id")
    tag_ids = [id[0] for id in cr.fetchall()]

    # account.analytic.group
    cr.execute("""
    INSERT INTO account_analytic_group (name, complete_name, company_id)
    SELECT name, name, company_id
    FROM account_analytic_tag
    ORDER BY id
    RETURNING id
    """)
    group_ids = [id[0] for id in cr.fetchall()]

    # account.analytic.account
    for tag_id, group_id in zip(tag_ids, group_ids):
        cr.execute("""
        UPDATE account_analytic_account
        SET group_id = %s
        WHERE tag_id = %s""" % (group_id, tag_id))


@openupgrade.migrate()
def migrate(env, version):
    analytic_tag_to_analytic_group(env.cr)