# Copyright 2021-2023 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class MailAlias(models.Model):
    _inherit = "mail.alias"

    def _alias_defaults_time_parameter(self, alias_defaults_input):
        self.ensure_one()
        model = self.alias_model_id
        params = self.env["base.time.parameter"].search([("model_id", "=", model.id)])
        for param in params:
            replace = None
            if param.code and param.code in alias_defaults_input:
                replace = param.code
            elif param.name and param.name in alias_defaults_input:
                replace = param.name
            if replace:
                new_value = param._get()
                if param.type == "reference":
                    new_value = new_value.id
                alias_defaults_input = alias_defaults_input.replace(
                    replace, str(new_value)
                )

        return alias_defaults_input
