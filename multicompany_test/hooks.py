from odoo.api import SUPERUSER_ID, Environment

from odoo.addons.base.models.base_test import update_xmlids


def post_init_hook(cr, registry):
    """
    Test user cannot access
    - base.main_company
    - base.user_admin
    - base.partner_admin
    - product.list0 (post_init_hook in product module)
    because they link to records of SYSTEM company.
    For testing, we link them to test records which the test user can access.
    """
    env = Environment(cr, SUPERUSER_ID, {})
    test_company = env.ref("multicompany_test.test_company")
    test_admin_user = env.ref("multicompany_test.test_admin_user")
    test_admin_partner = test_admin_user.partner_id
    xmlids = [
        ("base", "main_company", test_company.id),
        ("base", "user_admin", test_admin_user.id),
        ("base", "partner_admin", test_admin_partner.id),
    ]
    update_xmlids(env.cr, xmlids)
