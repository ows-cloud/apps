from odoo import api, fields, models


class Account(models.Model):
    _inherit = "account.account"

    include_initial_balance = fields.Boolean(
        "Bring Accounts Balance Forward",
        related="user_type_id.include_initial_balance",
    )
