# Copyright 2021 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import calendar
from datetime import datetime
from io import StringIO
from lxml import etree
import sys
from odoo import api, fields, models, _
from odoo.exceptions import UserError

# from . import saft_no_validation as saft
from . import saft_1_10 as saft


def decimal_string(myfloat):
    return "{:.2f}".format(myfloat)


class Company(models.Model):
    _inherit = 'res.company'

    partner_saft_id = fields.Many2one('res.partner', 'SAF-T Contact Person')


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
    date_from = fields.Date()
    date_to = fields.Date()
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
            year = int(self.month_to[:4])
            month = int(self.month_to[-2:])
            date = calendar.monthrange(year, month)[1]
            date_to = datetime.strptime(self.month_to + '-' + str(date), '%Y-%m-%d')
        except:
            raise UserError(_('The period should have this format: yyyy-mm'))

        # Create record with xml
        d = {'month_from': self.month_from, 'month_to': self.month_to, 'date_from': date_from, 'date_to': date_to, }
        record = self.env['l10n_no_account_saft.xml'].create(d)
        audit_file_class = AuditFile(record)
        audit_file = audit_file_class.AuditFile()

        record.saft_xml = self._create_xml_generateds(audit_file)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_no_account_saft.xml',
            'res_id': record.id,
            'view_type': 'tree,form',
            'view_mode': 'form',
        }

    def _create_xml_generateds(self, audit_file):
        xml_io = StringIO()
        audit_file.export(xml_io, level=0)
        return xml_io.getvalue()

    def _create_xml_pyxb(self, audit_file):
        myxml = audit_file.toxml('utf-8')
        return myxml
    # def melding_xml(self):
    #     m = self.melding()
    #     myxml = m.toxml('utf-8')
    #     myetree = etree.fromstring(myxml)
        
    #     no_of_times = 5 # Do a few times to remove nested empty nodes
    #     for i in range(0, no_of_times):
    #         for element in myetree.xpath('//*[not(node())]'):
    #             element.getparent().remove(element)
        
    #     mypretty = etree.tostring(myetree, pretty_print=True)
    #     return mypretty

class AuditFile:

    def __init__(self, saft_record):
        self.company = saft_record.company_id
        self.date_from = saft_record.date_from
        self.date_to = saft_record.date_to

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
        c.RegistrationNumber = self.company.vat[2:]
        c.Name = self.company.name
        partner = self.company.partner_id
        #c.Address = self.Address(partner)
        #c.Contact = self.Contact(self.company.partner_id)
        #c.TaxRegistration = self.TaxRegistration(self.company.partner_id)
        #c.BankAccount = self.BankAccount(self.company.partner_id)
        # c.Address = saft.AddressStructure()
        # c.Address.StreetName = self.company.street
        # c.Address.AdditionalAddressDetail = self.company.street2
        # c.Address.City = self.company.city
        # c.Address.PostalCode = self.company.zip
        # c.Address.Region = self.company.state_id.name or ''
        # c.Address.Country = self.company.country_id.code or ''
        # c.Address.AddressType = 'PostalAddress'

        # c.Contact = saft.ContactHeaderStructure()
        # c.Contact.ContactPerson = saft.ContactInformationStructure()
        # c.Contact.ContactPerson.FirstName = self.company.user_tech_id.name.partition(' ')[0]
        # c.Contact.ContactPerson.LastName = self.company.user_tech_id.name.partition(' ')[-1]
        # # otherwise try this https://www.codespeedy.com/get-the-last-word-from-a-string-in-python/
        # c.Contact.Telephone = self.company.user_tech_id.phone
        # c.Contact.Email = self.company.user_tech_id.email
        # c.Contact.Website = self.company.user_tech_id.website
        # c.Contact.MobilePhone = self.company.user_tech_id.mobile
        
        # TODO should not depend on l10n_no_hr_payroll
        # c.TaxRegistration = saft.TaxInformationStructure()
        # # mvanr = self.company.field_value_hr_ids.filtered(lambda r: r.field_code == 'l10n_no_virksomhet').value
        # mvanr = self.company.vat # TODO probably not correct
        # c.TaxRegistration.TaxRegistrationNumber = mvanr + 'MVA' 
        # c.TaxRegistration.TaxAuthority = "Skatteetaten"
        # c.TaxRegistration.TaxVerificationDate = self.company.write_date

        # TODO BankAccount

        return c

    def MasterFiles(self):
        mf = saft.MasterFilesType()

        line_obj = self.company.env['account.move.line']
        opening_balance_records = line_obj.read_group(
            domain=[('date', '<', self.date_from)],
            fields=['account_id', 'balance'],
            groupby=['account_id'],
        )
        opening_balance = {r['account_id'][0]: r['balance'] for r in opening_balance_records}
        closing_balance_records = line_obj.read_group(
            domain=[('date', '<=', self.date_to)],
            fields=['account_id', 'balance'],
            groupby=['account_id'],
        )
        closing_balance = {r['account_id'][0]: r['balance'] for r in closing_balance_records}

        mf.GeneralLedgerAccounts = saft.GeneralLedgerAccountsType()
        for account in self.company.env['account.account'].search([]):
            mf.GeneralLedgerAccounts.add_Account(self.Account(account, opening_balance.get(account.id, 0), closing_balance.get(account.id, 0)))

        mf.Customers = saft.CustomersType()
        for customer in self.company.env['res.partner'].search([('customer', '=', True)]):
            mf.Customers.add_Customer(self.Customer(customer))

        mf.Suppliers = saft.SuppliersType()
        for supplier in self.company.env['res.partner'].browse().search([('supplier', '=', True)]):
            mf.Suppliers.add_Supplier(self.Supplier(supplier))

        mf.TaxTable = saft.TaxTableType()
        for tax in self.company.env['account.tax'].search([]):
            mf.TaxTable.add_TaxTableEntry(self.TaxTableEntry(tax))

        mf.AnalysisTypeTable = saft.AnalysisTypeTableType()
        for analytic in self.company.env['account.analytic.account'].search([]):
            mf.AnalysisTypeTable.add_AnalysisTypeTableEntry(self.AnalysisTypeTableEntry(analytic))

        mf.Owners = saft.OwnersType()
        # for owner in self.company.env[''].browse():
        #     mf.Owners.append(self.Owner(owner))

        return mf

    def Account(self, account, opening_balance, closing_balance):
        a = saft.AccountType()
        a.AccountID = account.code
        a.AccountDescription = account.name
        a.AccountType = "GL"
        a.AccountCreationDate = account.create_date
        if opening_balance >= 0:
            a.OpeningDebitBalance = decimal_string(opening_balance)
        else:
            a.OpeningCreditBalance = decimal_string(-opening_balance)
        if closing_balance >= 0:
            a.ClosingDebitBalance = decimal_string(closing_balance)
        else:
            a.ClosingCreditBalance = decimal_string(-closing_balance)
        return a

    def Customer(self, customer):
        return self.Partner(customer, 'customer')

    def Supplier(self, supplier):
        return self.Partner(supplier, 'supplier')

    def Partner(self, partner, partner_type):
        if partner_type == 'customer':
            p = saft.CustomerType()
            p.CustomerID = partner.id
        elif partner_type == 'supplier':
            p = saft.SupplierType()
            p.SupplierID = partner.id
        
        p.RegistrationNumber = partner.vat
        p.Name = partner.name
        p.add_Address(self.Address(partner))
        p.add_Contact(self.Contact(partner))
        #p.TaxRegistration = partner.vat # [2:] # TODO 'MVA'
        #p.BankAccount
        return p

    def Address(self, partner):
        a = saft.AddressStructure()
        a.StreetName = partner.street
        if partner.street2:
            a.AdditionalAddressDetail = partner.street2
        a.City = partner.city
        a.PostalCode = partner.zip
        a.Region = partner.state_id.name or ''
        a.Country = partner.country_id.code or ''
        a.AddressType = 'PostalAddress'
        return a

    def Contact(self, partner):
        c = saft.ContactInformationStructure()
        c.ContactPerson = saft.PersonNameStructure()
        c.ContactPerson.FirstName = self.company.partner_saft_id.name.partition(' ')[0]
        c.ContactPerson.LastName = self.company.partner_saft_id.name.partition(' ')[-1]
        # # otherwise try this https://www.codespeedy.com/get-the-last-word-from-a-string-in-python/
        c.Telephone = self.company.partner_saft_id.phone
        c.Email = self.company.partner_saft_id.email
        c.Website = self.company.partner_saft_id.website
        c.MobilePhone = self.company.partner_saft_id.mobile or ''
        return c

    def TaxRegistration(self, partner):
        t = saft.TaxIDStructure()
        # mvanr = self.company.field_value_hr_ids.filtered(lambda r: r.field_code == 'l10n_no_virksomhet').value
        t.TaxRegistrationNumber = partner.vat 
        # c.TaxRegistration.TaxAuthority = "Skatteetaten"
        # c.TaxRegistration.TaxVerificationDate = self.company.write_date
        return t

    def BankAccount(self, partner):
        b = saft.BankAccountStructure()
        if partner.bank_ids:
            bank_account = partner.bank_ids[0]
            b.BankAccountNumber = bank_account.acc_number
            b.BIC = bank_account.bank_bic
            b.CurrencyCode = bank_account.currency_id.name
            # b.GeneralLedgerAccountID
        return b

    def PartyInfo(self, partner, partner_type):
        p = saft.PartyInfoStructure()
        p.PaymentTerms = saft.PaymentTermsType()
        # if partner_type == 'customer':
        #     p.PaymentTerms.Days = partner.property_payment_term_id...
        # elif partner_type == 'supplier':
        #     p.PaymentTerms.Days = partner.property_supplier_payment_term_id...
        # p.PaymentTerms.CashDiscountDays = partner.
        # p.PaymentTerms.CashDiscountRate = partner.
        # p.PaymentTerms.FreeBillingMonth = partner.
        # p.NaceCode = '63.110'
        p.CurrencyCode = partner.currency_id.name
        p.Type = 'Company' if partner.is_company else 'Private'
        p.Status = 'Active' if partner.active else 'Archived'
        return p

    def TaxTableEntry(self, tax):
        t = saft.TaxTableEntryType()
        t.TaxType = 'MVA'
        t.Description = 'Merverdiavgift'
        t.add_TaxCodeDetails(saft.TaxCodeDetailsType(
            TaxPercentage = tax.amount,
            Country = 'NO',
            StandardTaxCode = 1, # TODO mandatory
            BaseRate = [100],
        ))
        return t

    def AnalysisTypeTableEntry(self, analytic):
        a = saft.AnalysisTypeTableEntryType()
        a.AnalysisType = 'A'
        a.AnalysisTypeDescription = 'Analytic Account'
        a.AnalysisID = analytic.id
        a.AnalysisIDDescription = analytic.name
        return a

    def Owner(self):
        o = saft.OwnerType()
        return o

    def GeneralLedgerEntries(self):
        e = saft.GeneralLedgerEntriesType()
        e.NumberOfEntries = self.company.env['account.move'].search_count([('date', '>=', self.date_from), ('date', '<=', self.date_to)])
        lines = self.company.env['account.move.line'].search([('date', '>=', self.date_from), ('date', '<=', self.date_to)])
        e.TotalDebit = decimal_string(sum(line.debit for line in lines))
        e.TotalCredit = decimal_string(sum(line.credit for line in lines))
        for journal in self.company.env['account.journal'].search([]):
            e.add_Journal(self.Journal(journal))
        return e

    def Journal(self, journal):
        j = saft.JournalType()
        j.JournalID = journal.code
        j.Description = journal.name
        j.Type = journal.code # ?
        for move in self.company.env['account.move'].search([('journal_id', '=', journal.id), ('date', '>=', self.date_from), ('date', '<=', self.date_to)]):
            j.add_Transaction(self.Transaction(move))
        return j

    def Transaction(self, move):
        t = saft.TransactionType()
        t.TransactionID = move.name
        t.Period = int(move.date.strftime("%m"))
        t.PeriodYear = int(move.date.strftime("%Y"))
        t.TransactionDate = move.date
        # t.SourceID = move.
        # t.TransactionType = move.
        t.Description = move.ref
        # t.BatchID = move.
        t.SystemEntryDate = move.create_date
        t.GLPostingDate = move.write_date
        # t.SystemID = move.
        for idx, line in enumerate(move.line_ids):
            t.add_Line(self.Line(idx, line))
        return t

    def Line(self, idx, line):
        l = saft.LineType()
        l.RecordID = idx + 1
        l.AccountID = line.account_id.code
        if line.analytic_account_id:
            l.add_Analysis(saft.AnalysisStructure(AnalysisType='A', AnalysisID=line.analytic_account_id.id))
        l.ValueDate = line.move_id.date
        # l.SourceDocumentID
        l.Description = line.name
        l.DebitAmount = saft.AmountStructure(Amount=line.debit)
        l.CreditAmount = saft.AmountStructure(Amount=line.credit)
        for tax in line.tax_ids:
            l.add_TaxInformation(self.TaxInformation(line, tax))
        # l.ReferenceNumber
        # l.CID
        l.SystemEntryTime = datetime.now()
        # l.ownerID
        return l

    def TaxInformation(self, line, tax):
        t = saft.TaxInformationStructure()
        t.TaxType = 'MVA'
        # t.TaxCode
        t.TaxPercentage = int(tax.amount)
        t.TaxBase = line.debit + line.credit
        t.TaxAmount = saft.AmountStructure(Amount = decimal_string(t.TaxBase * tax.amount / 100))
        return t

