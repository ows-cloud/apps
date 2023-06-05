# Copyright 2023 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


"""
When the user saves a time parameter that is used by mail aliases,
Plan A is to take the user to a list with these mail aliases.
        But write() cannot return an action.
        Only write() knows which aliases have the OLD parameter name/code.
Plan B is a button counting all mail aliases with "time_parameter".
        But the XML didn't show the button.
Plan C: Simple button to go to mail aliases with "time_parameter".
"""


class BaseTimeParameter(models.Model):
    _inherit = "base.time.parameter"

    # Plan A
    # def write(self, vals):
    #     self.ensure_one()

    #     mail_aliases = []
    #     if "name" in vals.keys() or "code" in vals.keys():
    #         mail_aliases = self.env["mail.alias"].search(self._get_mail_alias_domain())

    #     result = super(BaseTimeParameter, self).write(vals)

    #     if mail_aliases:
    #         self.flush()
    #         THIS DOES NOT WORK -------------------------------------------------------
    #         return action_view_mail_alias(mail_aliases.ids)
    #         --------------------------------------------------------------------------
    #     else:
    #         return result

    # Plan B
    # def _count_mail_aliases(self):
    #     for record in self:
    #         record.count_mail_aliases = self.env["mail.alias"].search_count(
    #             record._get_mail_alias_domain()
    #         )

    # count_mail_aliases = fields.Integer(
    #     string="No of mail aliases",
    #     compute="_count_mail_aliases",
    # )

    def action_view_mail_alias(self, alias_ids=None):
        self.ensure_one()
        if not alias_ids:
            alias_ids = self.env["mail.alias"].search(
                self._get_mail_alias_domain()
            ).ids
        return {
            "name": "Please update the time parameter in these mail aliases!",
            "type": "ir.actions.act_window",
            "res_model": "mail.alias",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [("id", "in", alias_ids)],
        }

    def _get_mail_alias_domain(self):
        self.ensure_one()
        return [
            ("alias_defaults_hook", "like", "time_parameter"),
            # "|",
            # ("alias_defaults_input", "like", self.name),
            # ("alias_defaults_input", "like", self.code),
        ]


