# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
from datetime import datetime
from io import StringIO
from lxml import etree
import sys
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from . import saft_1_10 as saft


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
        #pass

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
        d = {'month_from': self.month_from, 'month_to': self.month_to, 'saft_xml': self._create_xml()}
        record = self.env['l10n_no_account_saft.xml'].create(d)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_no_account_saft.xml',
            'res_id': record.id,
            'view_type': 'tree,form',
            'view_mode': 'form',
        }

    def _create_xml(self):
        audit_file = self.AuditFile()
        xml_io = StringIO()
        audit_file.export(xml_io, level=0)
        return xml_io.getvalue()

    def AuditFile(self):
        audit_file = saft.AuditFile()
        audit_file.Header = self.Header()
        audit_file.MasterFiles = self.MasterFiles()
        audit_file.GeneralLedgerEntries = self.GeneralLedgerEntries()
        return audit_file

    def Header(self):
        h = saft.HeaderStructure()
        h.AuditFileVersion = '1.0'
        h.AuditFileCountry = 'NO'
        h.AuditFileDateCreated = datetime.now() 
        h.SoftwareCompanyName = 'Norske Apps2GROW AS'
        h.SoftwareID = 'Odoo'
        h.SoftwareVersion = '12.0'
        h.Company = self.Company()
        h.DefaultCurrencyCode = 'NOK'
        h.SelectionCriteria = saft.SelectionCriteriaStructure()
        h.SelectionCriteria.PeriodStart = 1
        h.SelectionCriteria.PeriodStartYear = 2020
        h.SelectionCriteria.PeriodEnd = 12
        h.SelectionCriteria.PeriodEndYear = 2020
        h.HeaderComment = 'No comment'
        h.TaxAccountingBasis = 'A' # TODO not working
        return h

    def Company(self):
        c = saft.CompanyStructure()
        
        return c
    def (self):

    def (self):

    def MasterFiles(self):
        mf = saft.MasterFilesType()
        return mf

    def (self):

    def (self):

    def (self):

    def (self):

    def GeneralLedgerEntries(self):
        gle = saft.GeneralLedgerEntriesType()
        return gle

    def (self):

    def (self):

    def (self):

    def (self):