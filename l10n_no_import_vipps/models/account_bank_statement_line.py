from odoo import fields, models


class AccountBankStatementLine(models.Model):
    _inherit = "account.bank.statement.line"

    import_first_name = fields.Char()
    import_last_name = fields.Char()
    import_message = fields.Char()

    def _post_import_vipps(self):
        self._post_import_vipps_set_partner()
        self._post_import_vipps_set_payment_ref()
    
    def _post_import_vipps_set_partner(self):
        self.ensure_one()
        Partner = self.env["res.partner"]
        self.partner_name = "{} {}".format(self.import_first_name, self.import_last_name)
        partner = Partner.search([("name", "=", self.partner_name)])
        if not partner:
            partner = Partner.create(
                {
                    "name": self.partner_name,
                }
            )
        if len(partner) == 1:
            self.partner_id = partner.id

    def _post_import_vipps_set_payment_ref(self):
        # try to lookup time_dependent_parameter, replace text with time dependent text.
        if self.import_message:
            self.payment_ref = "{}, {}".format(self.payment_ref, self.import_message)
