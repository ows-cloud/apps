from odoo import fields, models


class Base(models.AbstractModel):
    _inherit = "account.bank.statement.line"

    json = fields.Serialized(string="JSON")
    import_first_name = fields.Char(string="Import First Name", sparse="json")
    import_last_name = fields.Char(string="Import Last Name", sparse="json")
    import_message = fields.Char(string="Import Message", sparse="json")

    def _excel_post_import_set_partner(self):
        Partner = self.env["res.partner"]
        for line in self:
            if not line.partner_name:
                line.partner_name = "{} {}".format(
                    line.import_first_name,
                    line.import_last_name,
                )
            if not line.partner_id:
                partner = Partner.search([("name", "=", line.partner_name)])
                if not partner:
                    partner = Partner.create(
                        {
                            "name": line.partner_name,
                        }
                    )
                if len(partner) == 1:
                    line.partner_id = partner.id

    def _excel_post_import_set_text(self):
        for line in self:
            if line.import_message:
                line.payment_ref = "{}, {}".format(
                    line.payment_ref, line.import_message
                )

    def _excel_post_import_time_parameter(self):
        # Replace label keyword with time-related value.
        # If time-related account:
        # - Set counterpart_account_id.
        # - Create a reconciliation model for the account if it doesn't exist.

        def create_rec_model_if_not_exists(account):
            RecModel = self.env["account.reconcile.model"]
            rec_model = RecModel.search(
                [
                    ("rule_type", "=", "writeoff_suggestion"),
                    ("match_counterpart_account_id", "=", account.id),
                ]
            )
            if not rec_model:
                rec_model = RecModel.create(
                    {
                        "name": account.name,
                        "rule_type": "writeoff_suggestion",
                        "match_counterpart_account_id": account.id,
                    }
                )
                rec_model.set_counterpart_line()

        params = self.env["base.time.parameter"].search([])
        for line in self:
            for param in params:
                if param.code and param.code in line.payment_ref:
                    key = param.code
                elif param.name and param.name in line.payment_ref:
                    key = param.name
                else:
                    continue

                value = param._get_value(line.date)
                if not value:
                    continue
                elif isinstance(value, type(self.env["account.account"])):
                    line.counterpart_account_id = value
                    value = line.counterpart_account_id.name
                    # Create a reconciliation model
                    create_rec_model_if_not_exists(line.counterpart_account_id)

                line.payment_ref = line.payment_ref.replace(key, value)
