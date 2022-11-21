import logging

from odoo import models

_logger = logging.getLogger(__name__)
SYSTEM_COMPANY_ID = 1


class MulticompanyConfig(models.AbstractModel):
    _inherit = "multicompany.config"

    def special_config(self):
        if not self.env.user.has_group("base.group_system"):
            return False

        # after 14.0
        # self._special_website()
        # self._special_default_user()
        # self._special_support_user()

        # before 14.0
        # self._special_uom()
        # self._special_account_chart_template()

    def _special_website(self):
        websites = self.env["website"].sudo().search([])
        websites.sudo().write({"crm_default_team_id": False})

    def _special_default_user(self):
        default_users = (
            self.env["res.users"]
            .sudo()
            .with_context(active_test=False)
            .search(
                [
                    "|",
                    ("login", "=", "default"),
                    ("login", "=like", "default_user_for_company_%"),
                ]
            )
        )
        default_users.sudo().write({"default_user": True})

    def _special_support_user(self):
        support_user = self.env.ref(
            "__multicompany_base__.support_user", raise_if_not_found=False
        )
        if not support_user:
            companies = self.env["res.company"].sudo().search([])
            companies.ids
            support_user = (
                self.env["res.users"]
                .sudo()
                .create(
                    {
                        "login": "support",
                        "lang": "en_US",
                        "name": "Support User",
                        "company_ids": [(6, 0, companies.ids)],
                    }
                )
            )
            xmlid = self.env["ir.model.data"].create(
                {
                    "module": "__multicompany_base__",
                    "name": "support_user",
                    "model": "res.users",
                    "res_id": support_user.id,
                }
            )

    def _special_uom(self):
        """
        File "/o14/o14-server/addons/uom/models/uom_uom.py", line 85, in _check_category_reference_uniqueness
            raise ValidationError(_("UoM category %s should only have one reference unit of measure.")
        """
        all_uoms = self.env["uom.uom"].search([])
        ref_uoms = all_uoms.filtered(lambda u: u.uom_type == "reference")
        categories = ref_uoms.mapped("category_id")
        for category in categories:
            cat_ref_uoms = ref_uoms.filtered(lambda u: u.category_id == category)
            if len(cat_ref_uoms) == 1:
                continue
            # For reference uoms (except company_id 1):
            for cat_ref_uom in cat_ref_uoms.filtered(lambda u: u.company_id.id != 1):
                # Duplicate the category, and reference all the related company uoms to this category.
                company = cat_ref_uom.company_id
                new_category = category.sudo().copy(
                    {"company_id": company.id, "measure_type": ""}
                )
                company_cat_uoms = all_uoms.filtered(
                    lambda u: u.company_id == company and u.category_id == category
                )
                models.Model.write(
                    company_cat_uoms,
                    {"category_id": new_category.id, "measure_type": ""},
                )

    def _special_account_chart_template(self):
        """
        File "/o14/custom/openupgrade/openupgrade_scripts/scripts/account/14.0.1.1/post-migration.py", line 481, in fill_statement_lines_with_no_move
            "partner_id",
        File "/o14/o14-server/addons/account/models/account_bank_statement.py", line 994, in _synchronize_to_moves
            line_vals_list = self._prepare_move_line_default_vals()
        File "/o14/o14-server/addons/account/models/account_bank_statement.py", line 740, in _prepare_move_line_default_vals
            ) % self.journal_id.display_name)
        odoo.exceptions.UserError: You can't create a new statement line without a suspense account set on the Bank journal.
        """
        T = self.env["account.chart.template"]
        template_list = [
            # ('DK', 'Empty template for Denmark', 4),
            ("NO", "Empty template for Norway", 4),
            ("", "Empty template", 4),
        ]
        generic_template = self.env.ref("l10n_generic_coa.configurable_chart_template")
        for tup in template_list:
            country_code, name, code_digits = tup
            template = T.search([("name", "=", name)])
            if not template:
                template = generic_template.copy(
                    {"name": name, "code_digits": code_digits}
                )
            if country_code:
                companies = (
                    self.env["res.company"]
                    .sudo()
                    .search(
                        [
                            ("chart_template_id", "=", False),
                            ("partner_id.country_id.code", "=", country_code),
                        ]
                    )
                )
                companies.sudo().write({"chart_template_id": template.id})
            else:
                companies = (
                    self.env["res.company"]
                    .sudo()
                    .search([("chart_template_id", "=", False)])
                )
                companies.sudo().write({"chart_template_id": template.id})
