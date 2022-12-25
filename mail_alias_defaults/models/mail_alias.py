# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from ast import literal_eval

from odoo import _, api, fields, models

import logging
_logger = logging.getLogger(__name__)


class Alias(models.Model):
    _inherit = "mail.alias"

    alias_defaults = fields.Text(compute="_compute_alias_defaults")
    alias_defaults_hook = fields.Char(
        string="Hook to compute defaults",
        help="List of keywords to call functions, e.g. ['time_parameter']"
    )
    alias_defaults_input = fields.Char(string="Default Input")
    
    api.onchange("alias_defaults_hook", "alias_defaults_input")  # TODO why not working
    def _compute_alias_defaults(self):
        for record in self:
            alias_defaults_input = record.alias_defaults_input or "{}"
            for name in literal_eval(record.alias_defaults_hook or "[]"):
                method = "_alias_defaults_{}".format(name)
                alias_defaults_input = api.call_kw(
                    record,
                    method,
                    [record.ids, alias_defaults_input],
                    {},
                )
            record.alias_defaults = alias_defaults_input
