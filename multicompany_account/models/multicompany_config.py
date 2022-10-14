from odoo import models


class MulticompanyConfig(models.AbstractModel):
    _inherit = "multicompany.config"

    def _configure_company(self):
        super(MulticompanyConfig, self)._configure_company()
        self._group_show_line_subtotals()

    def _group_show_line_subtotals(self):
        company = self.env.company
        user_values = {
            "groups_id": [
                (3, self.env.ref("account.group_show_line_subtotals_tax_excluded").id, 0),
                (3, self.env.ref("account.group_show_line_subtotals_tax_included").id, 0),
                (4, self.env.ref("account.group_show_line_subtotals_{}".format(company.group_show_line_subtotals)).id, 0),
            ]
        }
        User = self.env["res.users"].with_context(active_test=False)
        default_user = User.search([("default_user", "=", True), ("company_id", "=", company.id)]).ensure_one()
        default_user.write(user_values)
        public_user = User.search([("groups_id", "=", self._ref("base.group_public").id), ("company_id", "=", company.id)]).ensure_one()
        public_user.write(user_values)
