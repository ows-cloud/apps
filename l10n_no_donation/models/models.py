# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
from datetime import datetime
from io import StringIO
from lxml import etree
import sys
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from . import gavefrivilligorganisasjon_2_0 as gave

# mål: lage XML
# importer partner med navn, fødselsnr, gavebeløp 2020
# name, function, id_numbers.category_id id_numbers.name

class Company(models.Model):
    _inherit = 'res.company'

    l10n_no_partner_donation_id = fields.Many2one('res.partner', 'Donation Contact Person')

# TODO The wizard should download the donation XML file directly. Then this class may be deleted.
class Donation(models.Model):
    _name = 'l10n_no_donation.xml'

    @api.depends('year')
    def _compute_donation_filename(self):
        self.ensure_one()

        name = 'Skattefradrag {year}.xml'.format(year=self.year)
        self.donation_filename = name

    @api.depends('donation_xml')
    def _compute_donation_binary(self):
        self.donation_binary = base64.b64encode(bytes(self.donation_xml, 'utf-8'))
        #pass

    company_id = fields.Many2one('res.company', string='Company', required=True, store=True, index=True, default=lambda self: self.env.user.company_id)
    year = fields.Char()
    date_from = fields.Date()
    date_to = fields.Date()
    timestamp = fields.Datetime(readonly=True)
    donation_xml = fields.Text(readonly=True)
    donation_filename = fields.Char(compute=_compute_donation_filename)
    donation_binary = fields.Binary(compute=_compute_donation_binary, string="Donation Binary")


class DonationWizard(models.TransientModel):
    _name = 'l10n_no_donation.xml.wizard'

    year = fields.Char()

    def create_xml(self):
        # Verify periods
        try:
            date_from = datetime.strptime(self.year + '-01-01', '%Y-%m-%d')
            date_to = datetime.strptime(self.year + '-12-31', '%Y-%m-%d')
        except:
            raise UserError(_('The year should have this format: yyyy'))

        # Create record with xml
        d = {'year': self.year, 'date_from': date_from, 'date_to': date_to, }
        record = self.env['l10n_no_donation.xml'].create(d)
        donation_file_class = DonationFile(record)
        donation_file = donation_file_class.DonationFile()

        record.donation_xml = self._create_xml_generateds(donation_file)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_no_donation.xml',
            'res_id': record.id,
            'view_type': 'tree,form',
            'view_mode': 'form',
        }

    def _create_xml_generateds(self, donation_file):
        xml_io = StringIO()
        donation_file.export(xml_io, level=0)
        return xml_io.getvalue()


class DonationFile:

    def __init__(self, donation_record):
        self.company = donation_record.company_id
        self.year = donation_record.year
        self.date_from = donation_record.date_from
        self.date_to = donation_record.date_to

    def DonationFile(self):
        # saft_1_10.py#L1120 AuditFile
        # def export(self, outfile, level, namespaceprefix_='', namespacedef_=' xmlns="urn:StandardAuditFile-Taxation-Financial:NO" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:StandardAuditFile-Taxation-Financial:NO Norwegian_SAF-T_Financial_Schema_v_1.10.xsd" ', name_='AuditFile', pretty_print=True):
        donation_file = gave.Melding()
        donation_file.Leveranse = self.Leveranse()
        return donation_file

    def Leveranse(self):
        l = gave.Leveranse()
        l.kildesystem = 'Odoo 12.0'
        l.oppgavegiver = self.Oppgavegiver()
        l.inntektsaar = self.year
        # TODO: unique reference
        l.oppgavegiversLeveranseReferanse = 'unik_referanse'
        # TODO: select 'ordinaer' or 'ingenoppgaver'
        l.leveransetype = 'ordinaer'
        #for partner in self.company.env['res.partner'].search([('customer', '=', True)]):
        for partner in self.company.env['res.partner'].search([('id', '=', 50)]):
            l.add_oppgave(self.Oppgave(partner))

        return l

    def Oppgavegiver(self):
        og = gave.Oppgavegiver()
        og.organisasjonsnummer = self.company.vat
        og.organisasjonsnavn = self.company.name
        og.kontaktinformasjon = self.Kontaktinformasjon()
        return og

    def Kontaktinformasjon(self):
        k = gave.Kontaktinformasjon()
        partner = self.company.partner_id
        k.navn = partner.name
        k.telefonnummer = partner.phone
        k.varselEpostadresse = partner.email
        k.varselSmsMobilnummer = partner.mobile
        return k

    def Oppgave(self, partner):
        o = gave.OppgaveGave()
        o.oppgaveeier = self.Oppgaveeier(partner)
        # TODO: compute the total donation
        o.beloep = int(partner.function)
        return o

    def Oppgaveeier(self, partner):
        oe = gave.Oppgaveeier()
        # TODO: error handling
        oe.foedselsnummer = partner.id_numbers.filtered(lambda r: r.category_id.code == 'l10n_no_personid').name
        oe.navn = partner.name