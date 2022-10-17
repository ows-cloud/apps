from odoo import api, fields, models
from odoo.addons.base_sparse_field.models.fields import Serialized


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
                line.payment_ref = "{}, {}".format(line.payment_ref, line.import_message)

    def _excel_post_import_time_parameter(self):
        # Replace label keyword with time-related value.
        params = self.env["base.time.parameter"].search([])
        for line in self:
            for param in params:
                if not param.code in line.payment_ref:
                    continue
                value = param._get_value(line.date)
                if not value:
                    continue
                elif type(value) == type(self.env["account.account"]):
                    line.counterpart_account_id = value
                    value = line.counterpart_account_id.name
                line.payment_ref = line.payment_ref.replace(param.code, value)
