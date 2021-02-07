# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.addons.spec_driven_model.models import spec_models

# saft.1.generalledgeraccounts ?
class Account(spec_models.StackedModel):
    _name = 'l10n_no_account_saft.account'
    _inherit = ["account.account", "saft.1.account"]
    _stacked = 'saft.1.account'
    _spec_module = 'odoo.addons.l10n_no_account_saft.models.saft_1_10_lib'

    saft1_AccountID = fields.Char(related='code')
    saft1_AccountDescription = fields.Char(related='name')
