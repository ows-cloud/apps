# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.addons.spec_driven_model.models import spec_models


# TODO The wizard should download the SAF-T XML file directly. Then this class may be deleted.
class Saft(models.Model):
    _name = 'l10n_no_account_saft.xml'

    @api.depends('month_from', 'month_to')
    def _compute_saft_filename(self):
        self.ensure_one()
        name = 'SAF-T from {month_from} to {month_to}.xml'.format(month_from=self.month_from, month_to=self.month_to)
        self.saft_filename = name

    @api.depends('saft_xml')
    def _compute_saft_binary(self):
        self.saft_binary = base64.b64encode(bytes(self.saft_xml, 'utf-8'))

    company_id = fields.Many2one('res.company', string='Company', required=True, store=True, index=True, default=lambda self: self.env.user.company_id)
    month_from = fields.Char()
    month_to = fields.Char()
    timestamp = fields.Datetime(readonly=True)
    saft_xml = fields.Text(readonly=True)
    saft_filename = fields.Char(compute=_compute_saft_filename)
    saft_binary = fields.Binary(compute=_compute_saft_binary, string="SAF-T Binary")


class SaftWizard(models.TransientModel):
    _name = 'l10n_no_account_saft.xml.wizard'

    month_from = fields.Char()
    month_to = fields.Char()

    def create_xml(self):
        # Verify periods
        try:
            date_from = datetime.strptime(self.month_from + '-01', '%Y-%m-%d')
            date_to = datetime.strptime(self.month_to + '-01', '%Y-%m-%d') # TODO get last day of the month or first day of next month
        except:
            raise UserError(_('The period should have this format: yyyy-mm'))

        # Create record with xml
        d = {'month_from': self.month_from, 'month_to': self.month_to, 'saft_xml': '<AuditFile></AuditFile>'}
        record = self.env['l10n_no_account_saft.xml'].create(d)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_no_account_saft.xml',
            'res_id': record.id,
            'view_type': 'tree,form',
            'view_mode': 'form',
        }

class SpecMixinSaft(models.AbstractModel):
    _description = "Abstract Model"
    _inherit = 'spec.mixin'
    _name = 'spec.mixin.saft'

    saft_company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        compute='_compute_saft_company_id',
        default=lambda self: self.env.ref('base.main_company').id,
    )

    def _compute_saft_company_id(self):
        for item in self:
            item.company_id = self.env.ref('base.main_company').id

    saft_currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        compute='_compute_saft_currency_id',
        default=lambda self: self.saft_company_id.currency_id.id,
    )

    def _compute_saft_currency_id(self):
        for item in self:
            item.currency_id = self.saft_company_id.currency_id.id


# saft.1.generalledgeraccounts ?
# class Account(spec_models.StackedModel):
#     _name = 'account.account'
#     _inherit = ["account.account", "saft.1.account"]
#     _inherit = ["saft.1.account"]
#     _stacked = 'saft.1.account'
#     _spec_module = 'odoo.addons.l10n_no_account_saft.models.saft_1_10_lib'

#     saft1_AccountID = fields.Char(related='code')
#     saft1_AccountDescription = fields.Char(related='name')

