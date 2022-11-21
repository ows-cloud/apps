from collections import defaultdict

from odoo import _, api, models
from odoo.exceptions import UserError


class Journal(models.Model):
    _inherit = "account.journal"

    @api.model
    def create(self, vals_list):
        # Max 1 purchase journal with mail alias.
        company_purchase_journal_with_mail_alias = defaultdict(str)
        if type(vals_list) is dict:
            vals_list = [vals_list]
        for vals in vals_list:
            if vals.get("type") == "purchase" and vals.get("alias_name"):
                # Update company.invoice_import_email
                company_id = vals.get("company_id") or self.env.company.id
                existing = self.search(
                    [
                        ("company_id", "=", company_id),
                        ("type", "=", "purchase"),
                        ("alias_name", "like", "%"),
                    ]
                )
                company_purchase_journal_with_mail_alias[company_id] += (
                    existing[0].name if existing else ""
                )
                # create or write
                if company_purchase_journal_with_mail_alias[company_id]:
                    raise UserError(
                        _("You can only have one purchase journal with alias, and journal {} already has an alias.").format(
                            company_purchase_journal_with_mail_alias[company_id]
                        )
                    )
                self.env["res.company"].browse(
                    company_id
                ).invoice_import_email = vals.get("alias_name")
                company_purchase_journal_with_mail_alias["company_id"] += vals.get(
                    "name", "new"
                )

        return super(Journal, self).create(vals_list)

    def write(self, vals):
        if vals.get("alias_name"):
            # Update company.invoice_import_email
            self.ensure_one()
            journal_type = vals.get("type") or self.type
            if journal_type == "purchase":
                company_id = vals.get("company_id") or self.company_id.id
                company_purchase_journal_with_mail_alias = self.search(
                    [
                        ("company_id", "=", company_id),
                        ("type", "=", "purchase"),
                        ("alias_name", "like", "%"),
                        ("id", "!=", self.id),
                    ]
                ).name
                if company_purchase_journal_with_mail_alias:
                    raise UserError(
                        _("Journal {} already has an alias, and you can only have one purchase journal with alias.").format(
                            company_purchase_journal_with_mail_alias
                        )
                    )
                self.env["res.company"].browse(
                    company_id
                ).invoice_import_email = vals.get("alias_name")

        return super(Journal, self).write(vals)

    def _update_mail_alias(self, vals):
        self.ensure_one()
        if vals.get("alias_name"):
            return super(Journal, self)._update_mail_alias(vals)
        elif self.type == "purchase":
            pass
        else:
            pass
            # I don't like the default behaviour of auto-creating aliases
            # return super(Journal, self)._update_mail_alias(vals)
