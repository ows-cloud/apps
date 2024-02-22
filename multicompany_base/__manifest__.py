# Copyright 2021 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "multicompany_base",
    "summary": "",
    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Uncategorized",
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/ir.actions.server.xml",
        "views/ir.model.data.xml",
    ],
    "depends": [
        "base",
        "base_set_record_values_mixin",
        "base_setup",
        "base_sparse_field",
        "web",
    ],
    "post_init_hook": "post_init_hook",
    "pre_init_hook": "pre_init_hook",
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "uninstall_hook": "WARNING_DELETE_RULES_uninstall_hook",
    "version": "16.0.1.0.0",
    "website": "https://github.com",
}
