from odoo import fields, models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    import_first_name = fields.Char()
    import_last_name = fields.Char()
    import_message = fields.Char()

    def _post_import_vipps(self):
        self._post_import_vipps_set_partner()
    
    def _post_import_vipps_set_partner(self):
        self.ensure_one()
        Partner = self.env["res.partner"]
        # name = "{} {}".format(self.import_first_name, self.import_last_name)
        name = self.partner_name
        partner = Partner.search([("name", "=", name)])
        if not partner:
            partner = Partner.create(
                {
                    "name": name,
                }
            )
        if len(partner) == 1:
            self.partner_id = partner.id
