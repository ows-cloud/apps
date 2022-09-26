from odoo import fields, models


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    def post_import_vipps(self):
        for record in self:
            for line in record.line_ids:
                line._post_import_vipps()
