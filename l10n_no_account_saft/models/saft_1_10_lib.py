# Copyright 2020 Akretion - Raphaël Valyi <raphael.valyi@akretion.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
# Generated Sun Feb  7 20:41:29 2021 by https://github.com/akretion/generateds-odoo
# and generateDS.py.
# Python 3.6.9 (default, Oct  8 2020, 12:12:24)  [GCC 8.4.0]
#
import textwrap
from odoo import fields, models

# Type of account. Set standard account in the StandardAccountID
# element. The only valid value is “GL” (General Ledger).
ACCOUNT_ACCOUNT = [
    ("GL", "GL"),
]

# Field to differentiate between multiple addresses and to indicate the
# type of address.
# Choose from the predefined enumerations
# StreetAddress, PostalAddress, BillingAddress, ShipToAddress,
# ShipFromAddress.
ADDRESS_ADDRESSSTRUCTURE = [
    ("StreetAddress", "StreetAddress"),
    ("PostalAddress", "PostalAddress"),
    ("BillingAddress", "BillingAddress"),
    ("ShipToAddress", "ShipToAddress"),
    ("ShipFromAddress", "ShipFromAddress"),
]

# Indicates whether the amounts on line-level are debit or credit
# amounts. Entry must correspond to entry reflected in General Ledger
# Entry. Signing of lineamounts is relative to this indicator. E.g. a
# return can lead to a negative amount.
DEBITCREDITINDICATOR_LINE = [
    ("D", "D"),
    ("C", "C"),
]

# Indicates whether the amounts on line-level are debit or credit
# amounts. Entry must correspond to entry reflected in General Ledger
# Entry. Signing of lineamounts is relative to this indicator. E.g. a
# return can lead to a negative amount.
DEBITCREDITINDICATOR_LINE = [
    ("D", "D"),
    ("C", "C"),
]

# Description of the Tax Type. “Merverdiavgift” is the only valid
# value.
DESCRIPTION_TAXTABLEENTRY = [
    ("Merverdiavgift", "Merverdiavgift"),
]

# Status of the analysis entry. Choose from the predefined enumerations
# Active, Closed, Observation, Passive.
STATUS_ANALYSIS = [
    ("Active", "Active"),
    ("Closed", "Closed"),
    ("Observation", "Observation"),
    ("Passive", "Passive"),
]

# Type of account.
# Enumerated
# Active, Observation, Passive.
STATUS_PARTYINFOSTRUCTURE = [
    ("Active", "Active"),
    ("Observation", "Observation"),
    ("Passive", "Passive"),
]

# Type of data in the audit file. The only valid value is “A”
# (Accounting).
TAXACCOUNTINGBASIS_HEADER = [
    ("A", "A"),
]

# Identification of the Revenue Body to which this TaxType refers.
# The only valid value is “Skatteetaten ”.
TAXAUTHORITY_TAXIDSTRUCTURE = [
    ("Skatteetaten", "Skatteetaten"),
]

# Tax type for look-up in tables. “MVA” is the only valid value.
TAX_TAXTABLEENTRY = [
    ("MVA", "MVA"),
]

# Tax type for look-up in tables.
# If used, then the only valid value is "MVA".
TAX_TAXINFORMATIONSTRUCTURE = [
    ("MVA", "MVA"),
]

# Type of party.
# Enumerated
# Private, Company, Government
_PARTYINFOSTRUCTURE = [
    ("Private", "Private"),
    ("Company", "Company"),
    ("Government", "Government"),
]


class Account(models.AbstractModel):
    "General ledger account information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.account'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AccountType'
    _concrete_rec_name = 'saft1_AccountID'

    saft1_Account_GeneralLedgerAccounts_id = fields.Many2one(
        "saft.1.generalledgeraccounts")
    saft1_choice4 = fields.Selection([
        ('saft1_OpeningDebitBalance', 'OpeningDebitBalance'),
        ('saft1_OpeningCreditBalance', 'OpeningCreditBalance')],
        "OpeningDebitBalance/OpeningCreditBalance")
    saft1_choice5 = fields.Selection([
        ('saft1_ClosingDebitBalance', 'ClosingDebitBalance'),
        ('saft1_ClosingCreditBalance', 'ClosingCreditBalance')],
        "ClosingDebitBalance/ClosingCreditBalance")
    saft1_AccountID = fields.Char(
        string="General ledger account code/number.",
        xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_AccountDescription = fields.Char(
        string="Name of individual general ledger account",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_StandardAccountID = fields.Char(
        string="StandardAccountID",
        xsd_type="SAFmiddle1textType",
        help="Standard general ledger account code/number from codelists"
        "\nfor mapping. Alternatively the elements"
        "\nGroupingCategory and GroupingCode can be used for"
        "\nmapping.")
    saft1_GroupingCategory = fields.Char(
        string="Use in conjunction with GroupingCode",
        xsd_type="SAFmiddle1textType",
        help="Use in conjunction with GroupingCode. Use category from"
        "\ncodelists.")
    saft1_GroupingCode = fields.Char(
        string="Use in conjunction with GroupingCategory",
        xsd_type="SAFmiddle1textType",
        help="Use in conjunction with GroupingCategory. Use code from"
        "\ncodelists.")
    saft1_AccountType = fields.Selection(
        ACCOUNT_ACCOUNT,
        string="Type of account",
        xsd_required=True,
        help="Type of account. Set standard account in the"
        "\nStandardAccountID element. The only valid value is"
        "\n“GL” (General Ledger).")
    saft1_AccountCreationDate = fields.Date(
        string="Date of when the general ledger account was created",
        xsd_type="date")
    saft1_OpeningDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='4',
        string="OpeningDebitBalance",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Debit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_OpeningCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='4',
        string="OpeningCreditBalance",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Credit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_ClosingDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='5',
        string="ClosingDebitBalance",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Debit balance at the end date of the selection period in the"
        "\nheader's default currency.")
    saft1_ClosingCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='5',
        string="ClosingCreditBalance",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Credit balance at the end date of the selection period in the"
        "\nheader's default currency.")


class AddressStructure(models.AbstractModel):
    "A common structure used wherever an address is required."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.addressstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AddressStructure'
    _concrete_rec_name = 'saft1_StreetName'

    saft1_Address_CompanyHeaderStructure_id = fields.Many2one(
        "saft.1.companyheaderstructure")
    saft1_Address_CompanyStructure_id = fields.Many2one(
        "saft.1.companystructure")
    saft1_StreetName = fields.Char(
        string="Address line 1",
        xsd_type="SAFmiddle2textType",
        help="Address line 1. Normally street name or post box. Can also"
        "\ninclude house number.")
    saft1_Number = fields.Char(
        string="Address line 1 (Number)",
        xsd_type="SAFshorttextType",
        help="Address line 1. House number if available.")
    saft1_AdditionalAddressDetail = fields.Char(
        string="Address line 2.",
        xsd_type="SAFmiddle2textType")
    saft1_Building = fields.Char(
        string="Not in use",
        xsd_type="SAFmiddle1textType")
    saft1_City = fields.Char(
        string="Name of the city/post district.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_PostalCode = fields.Char(
        string="Postal code for the relevant city/post district",
        xsd_required=True,
        xsd_type="SAFshorttextType")
    saft1_Region = fields.Char(
        string="Region",
        xsd_type="SAFmiddle1textType",
        help="Country specific code to indicate regions / provinces within"
        "\nthe tax authority.")
    saft1_Country = fields.Char(
        string="Two",
        xsd_type="ISOCountryCode",
        help="Two-letter country code according to ISO 3166-1 alpha 2"
        "\nstandard.")
    saft1_AddressType = fields.Selection(
        ADDRESS_ADDRESSSTRUCTURE,
        string="AddressType",
        help="Field to differentiate between multiple addresses and to"
        "\nindicate the type of address."
        "\nChoose from the predefined enumerations"
        "\nStreetAddress, PostalAddress, BillingAddress, ShipToAddress,"
        "\nShipFromAddress.")


class AmountStructure(models.AbstractModel):
    """A common structure used wherever an amount is required. Monetary amount
    with optional foreign currency exchange rate information."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.amountstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AmountStructure'
    _concrete_rec_name = 'saft1_Amount'

    saft1_Amount = fields.Float(
        currency_field="currency_id",
        string="Amount in the header’s default currency",
        xsd_required=True,
        xsd_type="SAFmonetaryType")
    saft1_CurrencyCode = fields.Char(
        string="Three",
        xsd_type="ISOCurrencyCode",
        help="Three-letter currency code according to ISO 4217 standard."
        "\nRequired if CurrencyAmount is used.")
    saft1_CurrencyAmount = fields.Float(
        currency_field="currency_id",
        string="Amount in foreign currency.",
        xsd_type="SAFmonetaryType",
        help="Amount in foreign currency."
        "\nRequired if CurrencyCode is used.")
    saft1_ExchangeRate = fields.Float(
        currency_field="currency_id",
        string="The exchange rate used.",
        xsd_type="SAFexchangerateType",
        help="The exchange rate used."
        "\nCurrencyAmount x ExchangeRate = Amount")


class AnalysisPartyInfoStructure(models.AbstractModel):
    "Analysis structure (restricted) for use in PartyInfoStructure."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.analysispartyinfostructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AnalysisPartyInfoStructure'
    _concrete_rec_name = 'saft1_AnalysisType'

    saft1_Analysis_AnalysisTableEntry_id = fields.Many2one(
        "saft.1.analysistableentry")
    saft1_Analysis_PartyInfoStructure_id = fields.Many2one(
        "saft.1.partyinfostructure")
    saft1_AnalysisType = fields.Char(
        string="Analysis type identifier/code for the dimension type",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Analysis type identifier/code for the dimension type (e.g."
        "\ndepartments, projects, journal types, cost centers,"
        "\netc.)")
    saft1_AnalysisID = fields.Char(
        string="Analysis ID of the specific dimension",
        xsd_required=True,
        xsd_type="SAFlongtextType")


class AnalysisStructure(models.AbstractModel):
    "General Ledger analysis codes."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.analysisstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AnalysisStructure'
    _concrete_rec_name = 'saft1_AnalysisType'

    saft1_Analysis_Line_id = fields.Many2one(
        "saft.1.line")
    saft1_Analysis_Line3_id = fields.Many2one(
        "saft.1.line3")
    saft1_Analysis_Line7_id = fields.Many2one(
        "saft.1.line7")
    saft1_AnalysisType = fields.Char(
        string="Analysis type identifier/code for the dimension type",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Analysis type identifier/code for the dimension type (e.g."
        "\ndepartments, projects, journal types, cost centers,"
        "\netc.)")
    saft1_AnalysisID = fields.Char(
        string="Analysis ID of the specific dimension",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_AnalysisAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Amount applying to the Analysis: f.i",
        help="Amount applying to the Analysis: f.i. the amount applying for"
        "\nthis dimension.")


class AnalysisTableEntry(models.AbstractModel):
    "Analysis entry information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.analysistableentry'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AnalysisTypeTableEntryType'
    _concrete_rec_name = 'saft1_AnalysisType'

    saft1_AnalysisTypeTableEntry_AnalysisTable_id = fields.Many2one(
        "saft.1.analysistable")
    saft1_AnalysisType = fields.Char(
        string="Analysis type identifier/code for the dimension type",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Analysis type identifier/code for the dimension type (e.g."
        "\ndepartments, projects, journal types, cost centers,"
        "\nemployees, etc.).")
    saft1_AnalysisTypeDescription = fields.Char(
        string="Description of the dimension type.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_AnalysisID = fields.Char(
        string="Analysis ID of the specific dimension entity",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_AnalysisIDDescription = fields.Char(
        string="Description of the specific dimension entity",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_StartDate = fields.Date(
        string="Start date.",
        xsd_type="date")
    saft1_EndDate = fields.Date(
        string="End date.",
        xsd_type="date")
    saft1_Status = fields.Selection(
        STATUS_ANALYSIS,
        string="Status of the analysis entry",
        help="Status of the analysis entry. Choose from the predefined"
        "\nenumerations"
        "\nActive, Closed, Observation, Passive.")
    saft1_Analysis = fields.One2many(
        "saft.1.analysispartyinfostructure",
        "saft1_Analysis_AnalysisTableEntry_id",
        string="Standard linked analysis codes for the analysis entry",
        help="Standard linked analysis codes for the analysis entry, such"
        "\nas project, department, cost center, groups, etc."
    )


class AnalysisTable(models.AbstractModel):
    """Table with the analysis code identifiers. Used for further specification
    of transaction data. Example: cost unit, cost center, project,
    department, provider, journal type, employees, etc. Journal type
    (bilagsart) should always be used on all transactions."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.analysistable'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AnalysisTypeTableType'
    _concrete_rec_name = 'saft1_AnalysisTypeTableEntry'

    saft1_AnalysisTypeTableEntry = fields.One2many(
        "saft.1.analysistableentry",
        "saft1_AnalysisTypeTableEntry_AnalysisTable_id",
        string="Analysis entry information.",
        xsd_required=True
    )


class AssetTransaction(models.AbstractModel):
    _description = 'assettransaction'
    _name = 'saft.1.assettransaction'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetTransactionType'
    _concrete_rec_name = 'saft1_AssetTransactionID'

    saft1_AssetTransaction_AssetTransactions_id = fields.Many2one(
        "saft.1.assettransactions")
    saft1_AssetTransactionID = fields.Char(
        string="Unique Identification of the transaction",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="Unique Identification of the transaction")
    saft1_AssetID = fields.Char(
        string="Unique identifier of the asset",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_AssetTransactionType = fields.Char(
        string="Code for the type of the transaction",
        xsd_required=True,
        xsd_type="SAFcodeType")
    saft1_Description = fields.Char(
        string="Description of the type of the transaction",
        xsd_type="SAFlongtextType")
    saft1_AssetTransactionDate = fields.Date(
        string="Recording date of the transaction type",
        xsd_required=True,
        xsd_type="date",
        help="Recording date of the transaction type (e. g. assets: date of"
        "\nthe addition of the asset)")
    saft1_Supplier = fields.Many2one(
        "saft.1.supplier5",
        string="Information about the supplier of the asset")
    saft1_TransactionID = fields.Char(
        string="Cross",
        xsd_type="SAFmiddle2textType",
        help="Cross-reference to GL posting in the journal. It can contain"
        "\nmany different levels to identify the transaction. It"
        "\ncould include cost centres such as company, division,"
        "\nregion, group and branch/department.")
    saft1_AssetTransactionValuations = fields.Many2one(
        "saft.1.assettransactionvaluations",
        string="AssetTransactionValuations",
        xsd_required=True,
        help="These amounts of the transaction can differ per asset"
        "\nvaluation type.")


class AssetTransactionValuation(models.AbstractModel):
    _description = 'assettransactionvaluation'
    _name = 'saft.1.assettransactionvaluation'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetTransactionValuationType'
    _concrete_rec_name = 'saft1_AssetValuationType'

    saft1_AssetTransactionValuation_AssetTransactionValuations_id = fields.Many2one(
        "saft.1.assettransactionvaluations")
    saft1_AssetValuationType = fields.Char(
        string="Describes the purpose for the reporting: f",
        xsd_type="SAFshorttextType",
        help="Describes the purpose for the reporting: f.i. commercial, tax"
        "\nin country 1, tax in country 2, etc.")
    saft1_AcquisitionAndProductionCostsOnTransaction = fields.Float(
        currency_field="currency_id",
        string="AcquisitionAndProductionCostsOnTransaction",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Costs of acquisition and/or production of related asset"
        "\ntransaction in the header's default currency at date"
        "\nof transaction.")
    saft1_BookValueOnTransaction = fields.Float(
        currency_field="currency_id",
        string="BookValueOnTransaction",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Bookvalue of related asset transaction in the header's"
        "\ndefault currency at date of transaction.")
    saft1_AssetTransactionAmount = fields.Float(
        currency_field="currency_id",
        string="AssetTransactionAmount",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Net Amount of related asset transaction in the header's"
        "\ndefault currency, for instance the net sales revenue.")


class AssetTransactionValuations(models.AbstractModel):
    """These amounts of the transaction can differ per asset valuation type."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.assettransactionvaluations'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetTransactionValuationsType'
    _concrete_rec_name = 'saft1_AssetTransactionValuation'

    saft1_AssetTransactionValuation = fields.One2many(
        "saft.1.assettransactionvaluation",
        "saft1_AssetTransactionValuation_AssetTransactionValuations_id",
        string="AssetTransactionValuation",
        xsd_required=True
    )


class AssetTransactions(models.AbstractModel):
    """Details of all transactions related to an asset during the
    Selectionperiod."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.assettransactions'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetTransactionsType'
    _concrete_rec_name = 'saft1_NumberOfAssetTransactions'

    saft1_NumberOfAssetTransactions = fields.Integer(
        string="Number of movementlines during selected period",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_AssetTransaction = fields.One2many(
        "saft.1.assettransaction",
        "saft1_AssetTransaction_AssetTransactions_id",
        string="AssetTransaction",
        xsd_required=True
    )


class Asset(models.AbstractModel):
    _description = 'asset'
    _name = 'saft.1.asset'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetType'
    _concrete_rec_name = 'saft1_AssetID'

    saft1_Asset_Assets_id = fields.Many2one(
        "saft.1.assets")
    saft1_AssetID = fields.Char(
        string="Unique identifier of the asset",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_AccountID = fields.Char(
        string="General Ledger Account code",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code. Can be including sub-account id."
        "\nIt can contain many different levels to identify the"
        "\nAccount. It could include cost centres such as"
        "\ncompany, division, region, group and"
        "\nbranch/department.")
    saft1_Description = fields.Char(
        string="Description of this asset",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_Supplier = fields.One2many(
        "saft.1.supplier1",
        "saft1_Supplier_Asset_id",
        string="Contains the information of all suppliers",
        help="Contains the information of all suppliers, including the"
        "\nhistorical suppliers."
    )
    saft1_PurchaseOrderDate = fields.Date(
        string="Date of the purchase order of this asset",
        xsd_type="date")
    saft1_DateOfAcquisition = fields.Date(
        string="Date of the acquisition of the asset",
        xsd_required=True,
        xsd_type="date",
        help="Date of the acquisition of the asset (usually the date of"
        "\ndelivery).")
    saft1_StartUpDate = fields.Date(
        string="Commissioning date of the asset.",
        xsd_type="date")
    saft1_Valuations = fields.Many2one(
        "saft.1.valuations",
        string="The data can be reported for different purposes",
        xsd_required=True,
        help="The data can be reported for different purposes. More than"
        "\none can be in this SAF.")


class Assets(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.assets'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AssetsType'
    _concrete_rec_name = 'saft1_Asset'

    saft1_Asset = fields.One2many(
        "saft.1.asset",
        "saft1_Asset_Assets_id",
        string="Asset", xsd_required=True
    )


class AuditFile(models.AbstractModel):
    "Root element of the Norwegian SAF-T file."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.auditfile'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'AuditFile'
    _concrete_rec_name = 'saft1_Header'

    saft1_Header = fields.Many2one(
        "saft.1.header",
        string="Header", xsd_required=True)
    saft1_MasterFiles = fields.Many2one(
        "saft.1.masterfiles",
        string="MasterFiles")
    saft1_GeneralLedgerEntries = fields.Many2one(
        "saft.1.generalledgerentries",
        string="GeneralLedgerEntries")
    saft1_SourceDocuments = fields.Many2one(
        "saft.1.sourcedocuments",
        string="SourceDocuments")


class BankAccountStructure(models.AbstractModel):
    """Bank account number information. IBAN number, or account number with
    optional information."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.bankaccountstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'BankAccountStructure'
    _concrete_rec_name = 'saft1_IBANNumber'

    saft1_BankAccount_CompanyHeaderStructure_id = fields.Many2one(
        "saft.1.companyheaderstructure")
    saft1_BankAccount_CompanyStructure_id = fields.Many2one(
        "saft.1.companystructure")
    saft1_choice2 = fields.Selection([
        ('saft1_IBANNumber', 'IBANNumber'),
        ('saft1_BankAccountNumber', 'BankAccountNumber'),
        ('saft1_BankAccountName', 'BankAccountName'),
        ('saft1_SortCode', 'SortCode')],
        "IBANNumber/BankAccountNumber/BankAccountName/SortC...")
    saft1_IBANNumber = fields.Char(
        choice='2',
        string="International Bank Account Number",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="International Bank Account Number, ISO 13616")
    saft1_BankAccountNumber = fields.Char(
        choice='2',
        string="BankAccountNumber",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="The number allocated to the account by the individual’s or"
        "\ncompany’s own bank.")
    saft1_BankAccountName = fields.Char(
        choice='2',
        string="BankAccountName",
        xsd_type="SAFmiddle2textType",
        help="The name of the individual or company holding the bank"
        "\naccount.")
    saft1_SortCode = fields.Char(
        choice='2',
        string="SortCode",
        xsd_type="SAFshorttextType",
        help="Identifier for the bank branch at which the account is held."
        "\nMay be needed to uniquely identify the account. Also"
        "\nknown as ABA Number or National Bank Code")
    saft1_BIC = fields.Char(
        string="Bank Identifier Code.",
        xsd_type="SAFshorttextType")
    saft1_CurrencyCode = fields.Char(
        string="Currency Code for the Bank Account from ISO 4217",
        xsd_type="ISOCurrencyCode")
    saft1_GeneralLedgerAccountID = fields.Char(
        string="Link to a General Ledger account.",
        xsd_type="SAFmiddle2textType")


class CompanyHeaderStructure(models.AbstractModel):
    """CompanyStructure with mandatory RegistrationNumber and Telephone
    (Contact)."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.companyheaderstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CompanyHeaderStructure'
    _concrete_rec_name = 'saft1_RegistrationNumber'

    saft1_RegistrationNumber = fields.Char(
        string="Organization number from The Brønnøysund Register Centre",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="Organization number from The Brønnøysund Register Centre"
        "\n(Brønnøysundregistrene) or other relevant government"
        "\nauthority. In case of private persons, the social"
        "\nsecurity number can be used.")
    saft1_Name = fields.Char(
        string="The name of the company.",
        xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_Address = fields.One2many(
        "saft.1.addressstructure",
        "saft1_Address_CompanyHeaderStructure_id",
        string="Addresses of the company.",
        xsd_required=True
    )
    saft1_Contact = fields.One2many(
        "saft.1.contactinformationstructure",
        "saft1_Contact_CompanyHeaderStructure_id",
        string="Contacts of the company.",
        xsd_required=True
    )
    saft1_TaxRegistration = fields.One2many(
        "saft.1.taxidstructure",
        "saft1_TaxRegistration_CompanyHeaderStructure_id",
        string="Tax registration of the company."
    )
    saft1_BankAccount = fields.One2many(
        "saft.1.bankaccountstructure",
        "saft1_BankAccount_CompanyHeaderStructure_id",
        string="Bank accounts of the company."
    )


class CompanyStructure(models.AbstractModel):
    "Name, address, contact and identification information of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.companystructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CompanyStructure'
    _concrete_rec_name = 'saft1_RegistrationNumber'

    saft1_RegistrationNumber = fields.Char(
        string="Organization number from The Brønnøysund Register Centre",
        xsd_type="SAFmiddle1textType",
        help="Organization number from The Brønnøysund Register Centre"
        "\n(Brønnøysundregistrene) or other relevant government"
        "\nauthority. In case of private persons, the social"
        "\nsecurity number can be used.")
    saft1_Name = fields.Char(
        string="The name of the company.",
        xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_Address = fields.One2many(
        "saft.1.addressstructure",
        "saft1_Address_CompanyStructure_id",
        string="Addresses of the company.",
        xsd_required=True
    )
    saft1_Contact = fields.One2many(
        "saft.1.contactinformationstructure",
        "saft1_Contact_CompanyStructure_id",
        string="Contacts of the company."
    )
    saft1_TaxRegistration = fields.One2many(
        "saft.1.taxidstructure",
        "saft1_TaxRegistration_CompanyStructure_id",
        string="Tax registration of the company."
    )
    saft1_BankAccount = fields.One2many(
        "saft.1.bankaccountstructure",
        "saft1_BankAccount_CompanyStructure_id",
        string="Bank accounts of the company."
    )


class ContactHeaderStructure(models.AbstractModel):
    "ContactInformationStructure with madatory TelephoneNumber."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.contactheaderstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ContactHeaderStructure'
    _concrete_rec_name = 'saft1_ContactPerson'

    saft1_ContactPerson = fields.Many2one(
        "saft.1.personnamestructure",
        string="The name of the contact person.",
        xsd_required=True)
    saft1_Telephone = fields.Char(
        string="Telephone number.",
        xsd_required=True,
        xsd_type="SAFshorttextType")
    saft1_Fax = fields.Char(
        string="Fax number.",
        xsd_type="SAFshorttextType")
    saft1_Email = fields.Char(
        string="E-mail address.",
        xsd_type="SAFmiddle2textType")
    saft1_Website = fields.Char(
        string="Website address.",
        xsd_type="anyURI")
    saft1_MobilePhone = fields.Char(
        string="The mobile phone number",
        xsd_type="SAFshorttextType",
        help="The mobile phone number (for SMS messages).")


class ContactInformationStructure(models.AbstractModel):
    "Contact information of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.contactinformationstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ContactInformationStructure'
    _concrete_rec_name = 'saft1_ContactPerson'

    saft1_Contact_CompanyHeaderStructure_id = fields.Many2one(
        "saft.1.companyheaderstructure")
    saft1_Contact_CompanyStructure_id = fields.Many2one(
        "saft.1.companystructure")
    saft1_ContactPerson = fields.Many2one(
        "saft.1.personnamestructure",
        string="The name of the contact person.",
        xsd_required=True)
    saft1_Telephone = fields.Char(
        string="Telephone number.",
        xsd_type="SAFshorttextType")
    saft1_Fax = fields.Char(
        string="Fax number.",
        xsd_type="SAFshorttextType")
    saft1_Email = fields.Char(
        string="E-mail address.",
        xsd_type="SAFmiddle2textType")
    saft1_Website = fields.Char(
        string="Website address.",
        xsd_type="anyURI")
    saft1_MobilePhone = fields.Char(
        string="The mobile phone number",
        xsd_type="SAFshorttextType",
        help="The mobile phone number (for SMS messages).")


class CreditNote(models.AbstractModel):
    _description = 'creditnote'
    _name = 'saft.1.creditnote'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CreditNoteType'
    _concrete_rec_name = 'saft1_Reference'

    saft1_Reference = fields.Char(
        string="Credit note reference",
        xsd_type="SAFmiddle1textType",
        help="Credit note reference (where applicable) to original invoice")
    saft1_Reason = fields.Char(
        string="Credit note reason or rationale",
        xsd_type="SAFlongtextType",
        help="Credit note reason or rationale")


class CustomerInfo(models.AbstractModel):
    _description = 'customerinfo'
    _name = 'saft.1.customerinfo'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CustomerInfoType'
    _concrete_rec_name = 'saft1_CustomerID'

    saft1_choice13 = fields.Selection([
        ('saft1_CustomerID', 'CustomerID'),
        ('saft1_Name', 'Name')],
        "CustomerID/Name")
    saft1_CustomerID = fields.Char(
        choice='13',
        string="Unique code for the customer",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_Name = fields.Char(
        choice='13',
        string="Name of the customer", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_BillingAddress = fields.Many2one(
        "saft.1.addressstructure",
        string="BillingAddress",
        xsd_required=True)


class Customer(models.AbstractModel):
    "Customer information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.customer'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CustomerType'
    _concrete_rec_name = 'saft1_CustomerID'

    saft1_Customer_Customers_id = fields.Many2one(
        "saft.1.customers")
    saft1_choice6 = fields.Selection([
        ('saft1_OpeningDebitBalance', 'OpeningDebitBalance'),
        ('saft1_OpeningCreditBalance', 'OpeningCreditBalance')],
        "OpeningDebitBalance/OpeningCreditBalance")
    saft1_choice7 = fields.Selection([
        ('saft1_ClosingDebitBalance', 'ClosingDebitBalance'),
        ('saft1_ClosingCreditBalance', 'ClosingCreditBalance')],
        "ClosingDebitBalance/ClosingCreditBalance")
    saft1_CustomerID = fields.Char(
        string="Unique account code/number for the customer",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="Unique account code/number for the customer.")
    saft1_SelfBillingIndicator = fields.Char(
        string="Indicator showing if a self",
        xsd_type="SAFcodeType",
        help="Indicator showing if a self-billing agreement exists between"
        "\nthe customer and the supplier.")
    saft1_AccountID = fields.Char(
        string="General ledger account code/number for this customer",
        xsd_type="SAFmiddle2textType",
        help="General ledger account code/number for this customer. This is"
        "\nthe account code/number into where this sub"
        "\naccount/accounts receivable is consolidated in the"
        "\nbalance sheet.")
    saft1_OpeningDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='6',
        string="OpeningDebitBalance",
        xsd_type="SAFmonetaryType",
        help="Debit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_OpeningCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='6',
        string="OpeningCreditBalance",
        xsd_type="SAFmonetaryType",
        help="Credit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_ClosingDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='7',
        string="ClosingDebitBalance",
        xsd_type="SAFmonetaryType",
        help="Debit balance at the end date of the selection period in the"
        "\nheader's default currency.")
    saft1_ClosingCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='7',
        string="ClosingCreditBalance",
        xsd_type="SAFmonetaryType",
        help="Credit balance at the end date of the selection period in the"
        "\nheader's default currency.")
    saft1_PartyInfo = fields.Many2one(
        "saft.1.partyinfostructure",
        string="Additional party information.")


class Customers(models.AbstractModel):
    "The customers of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.customers'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'CustomersType'
    _concrete_rec_name = 'saft1_Customer'

    saft1_Customer = fields.One2many(
        "saft.1.customer",
        "saft1_Customer_Customers_id",
        string="Customer information.",
        xsd_required=True
    )


class DeliveryPeriod(models.AbstractModel):
    "Timeframe of the deliveries"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.deliveryperiod'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'DeliveryPeriodType'
    _concrete_rec_name = 'saft1_FromDate'

    saft1_FromDate = fields.Date(
        string="Startdate of the deliveries",
        xsd_required=True,
        xsd_type="date")
    saft1_ToDate = fields.Date(
        string="Enddate of the deliveries",
        xsd_required=True,
        xsd_type="date")


class Delivery(models.AbstractModel):
    """Information about the date or timeframe of the delivery of the goods or
    services."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.delivery'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'DeliveryType'
    _concrete_rec_name = 'saft1_MovementReference'

    saft1_choice15 = fields.Selection([
        ('saft1_MovementReference', 'MovementReference'),
        ('saft1_DeliveryDate', 'DeliveryDate'),
        ('saft1_DeliveryPeriod', 'DeliveryPeriod')],
        "MovementReference/DeliveryDate/DeliveryPeriod")
    saft1_MovementReference = fields.Char(
        choice='15',
        string="Unique reference to the movement.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_DeliveryDate = fields.Date(
        choice='15',
        string="The date of the delivery",
        xsd_required=True,
        xsd_type="date")
    saft1_DeliveryPeriod = fields.Many2one(
        "saft.1.deliveryperiod",
        choice='15',
        string="Timeframe of the deliveries",
        xsd_required=True)


class DocumentReference(models.AbstractModel):
    _description = 'documentreference'
    _name = 'saft.1.documentreference'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'DocumentReferenceType'
    _concrete_rec_name = 'saft1_DocumentType'

    saft1_DocumentType = fields.Char(
        string="Type of document",
        xsd_required=True,
        xsd_type="SAFshorttextType")
    saft1_DocumentNumber = fields.Char(
        string="Reference number of the document",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_DocumentLine = fields.Char(
        string="Line number of the document",
        xsd_type="SAFshorttextType")


class DocumentTotals(models.AbstractModel):
    _description = 'documenttotals'
    _name = 'saft.1.documenttotals'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'DocumentTotalsType'
    _concrete_rec_name = 'saft1_TaxInformationTotals'

    saft1_TaxInformationTotals = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformationTotals_DocumentTotals_id",
        string="Control totals tax payable information",
        help="Control totals tax payable information. Per TaxType/TaxCode"
        "\nthe TaxBase and TaxAmount are summarised."
    )
    saft1_NetTotal = fields.Float(
        currency_field="currency_id",
        string="NetTotal",
        xsd_type="SAFmonetaryType",
        help="Total amount excluding tax in the header's default currency.")
    saft1_GrossTotal = fields.Float(
        currency_field="currency_id",
        string="GrossTotal", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Total amount including tax in the header's default currency.")


class DocumentTotals10(models.AbstractModel):
    _description = 'documenttotals10'
    _name = 'saft.1.documenttotals10'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'DocumentTotalsType10'
    _concrete_rec_name = 'saft1_TaxInformationTotals'

    saft1_TaxInformationTotals = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformationTotals_DocumentTotals10_id",
        string="Control totals tax payable information",
        help="Control totals tax payable information. Per TaxType/TaxCode"
        "\nthe TaxBase and TaxAmount are summarised."
    )
    saft1_ShippingCostsAmountTotal = fields.Float(
        currency_field="currency_id",
        string="Control total amount freight charges",
        xsd_type="SAFmonetaryType")
    saft1_NetTotal = fields.Float(
        currency_field="currency_id",
        string="Control total sales value excluding tax and shippingcosts",
        xsd_required=True,
        xsd_type="SAFmonetaryType")
    saft1_GrossTotal = fields.Float(
        currency_field="currency_id",
        string="Control total amount including tax and shippingcosts",
        xsd_required=True,
        xsd_type="SAFmonetaryType")


class ExtraordinaryDepreciationForPeriod(models.AbstractModel):
    _description = 'extraordinarydepreciationforperiod'
    _name = 'saft.1.extraordinarydepreciationforperiod'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ExtraordinaryDepreciationForPeriodType'
    _concrete_rec_name = 'saft1_ExtraordinaryDepreciationMethod'

    saft1_ExtraordinaryDepreciationForPeriod_ExtraordinaryDepreciationsForPeriod_id = fields.Many2one(
        "saft.1.extraordinarydepreciationsforperiod")
    saft1_ExtraordinaryDepreciationMethod = fields.Char(
        string="ExtraordinaryDepreciationMethod",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="Method of extraordinary depreciation during the"
        "\nSelectionperiod.")
    saft1_ExtraordinaryDepreciationForPeriod = fields.Float(
        currency_field="currency_id",
        string="ExtraordinaryDepreciationForPeriod",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Amouunt of extraordinary depreciation during the"
        "\nSelectionperiod in the header's default currency.")


class ExtraordinaryDepreciationsForPeriod(models.AbstractModel):
    """Extraordinary depreciations for this asset during the
    Selectionperiod."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.extraordinarydepreciationsforperiod'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ExtraordinaryDepreciationsForPeriodType'
    _concrete_rec_name = 'saft1_ExtraordinaryDepreciationForPeriod'

    saft1_ExtraordinaryDepreciationForPeriod = fields.One2many(
        "saft.1.extraordinarydepreciationforperiod",
        "saft1_ExtraordinaryDepreciationForPeriod_ExtraordinaryDepreciationsForPeriod_id",
        string="ExtraordinaryDepreciationForPeriod",
        xsd_required=True
    )


class GeneralLedgerAccounts(models.AbstractModel):
    "The general ledger accounts of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.generalledgeraccounts'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'GeneralLedgerAccountsType'
    _concrete_rec_name = 'saft1_Account'

    saft1_Account = fields.One2many(
        "saft.1.account",
        "saft1_Account_GeneralLedgerAccounts_id",
        string="General ledger account information.",
        xsd_required=True
    )


class GeneralLedgerEntries(models.AbstractModel):
    "Accounting transactions."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.generalledgerentries'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'GeneralLedgerEntriesType'
    _concrete_rec_name = 'saft1_NumberOfEntries'

    saft1_NumberOfEntries = fields.Integer(
        string="Number of entries",
        xsd_required=True,
        xsd_type="nonNegativeInteger",
        help="Number of entries. This is the total number of Transaction"
        "\nentries (accounting documents/vouchers) from all"
        "\nJournals included in the audit file.")
    saft1_TotalDebit = fields.Float(
        currency_field="currency_id",
        string="TotalDebit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all debit amounts in the header's default"
        "\ncurrency.")
    saft1_TotalCredit = fields.Float(
        currency_field="currency_id",
        string="TotalCredit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all credit amounts in the header's default"
        "\ncurrency.")
    saft1_Journal = fields.One2many(
        "saft.1.journal",
        "saft1_Journal_GeneralLedgerEntries_id",
        string="Journal information."
    )


class HeaderStructure(models.AbstractModel):
    "Overall information about this Standard Auditfile."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.headerstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'HeaderStructure'
    _concrete_rec_name = 'saft1_AuditFileVersion'

    saft1_AuditFileVersion = fields.Char(
        string="Version of standard audit file being used",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Version of standard audit file being used. The version number"
        "\nto be used is displayed in an XML annotation in top"
        "\nof the XSD schema file.")
    saft1_AuditFileCountry = fields.Char(
        string="Two", xsd_required=True,
        xsd_type="ISOCountryCode",
        help="Two-letter country code according to ISO 3166-1 alpha 2"
        "\nstandard.")
    saft1_AuditFileRegion = fields.Char(
        string="Not in use.",
        xsd_type="SAFcodeType")
    saft1_AuditFileDateCreated = fields.Date(
        string="Date of production of the audit file",
        xsd_required=True,
        xsd_type="date")
    saft1_SoftwareCompanyName = fields.Char(
        string="SoftwareCompanyName",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="Name of the software company whose product created the audit"
        "\nfile.")
    saft1_SoftwareID = fields.Char(
        string="Name of the software that generated the audit file",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_SoftwareVersion = fields.Char(
        string="Version of the software that generated the audit file",
        xsd_required=True,
        xsd_type="SAFshorttextType")
    saft1_Company = fields.Many2one(
        "saft.1.companyheaderstructure",
        string="Company's name and address details.",
        xsd_required=True)
    saft1_DefaultCurrencyCode = fields.Char(
        string="Three letter Currency Code",
        xsd_required=True,
        xsd_type="ISOCurrencyCode",
        help="Three letter Currency Code (ISO 4217) of local currency which"
        "\nis the default for the audit file.")
    saft1_SelectionCriteria = fields.Many2one(
        "saft.1.selectioncriteriastructure",
        string="Criteria set by the user to populate the audit files")
    saft1_HeaderComment = fields.Char(
        string="Space for any further generic comments on the audit file",
        xsd_type="SAFlongtextType")


class Header(models.AbstractModel):
    "Overall information about this Standard Audit file."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.header'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'HeaderType'
    _concrete_rec_name = 'saft1_TaxAccountingBasis'

    saft1_TaxAccountingBasis = fields.Selection(
        TAXACCOUNTINGBASIS_HEADER,
        string="Type of data in the audit file",
        xsd_required=True,
        help="Type of data in the audit file. The only valid value is “A”"
        "\n(Accounting).")
    saft1_TaxEntity = fields.Char(
        string="Company / Division / Branch reference",
        xsd_type="SAFmiddle2textType")
    saft1_UserID = fields.Char(
        string="ID of the user that generated the audit file",
        xsd_type="SAFmiddle1textType")
    saft1_AuditFileSender = fields.Many2one(
        "saft.1.companystructure",
        string="AuditFileSender",
        help="Information about the sender of the audit file if the sender"
        "\nis not the company that owns the data. This can be an"
        "\naccounting office, a parent company, etc.")


class InvoiceStructure(models.AbstractModel):
    """Containing all information about sales invoices and suppliers
    invoices."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.invoicestructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'InvoiceStructure'
    _concrete_rec_name = 'saft1_InvoiceNo'

    saft1_Invoice_PurchaseInvoices_id = fields.Many2one(
        "saft.1.purchaseinvoices")
    saft1_Invoice_SalesInvoices_id = fields.Many2one(
        "saft.1.salesinvoices")
    saft1_choice1 = fields.Selection([
        ('saft1_CustomerInfo', 'CustomerInfo'),
        ('saft1_SupplierInfo', 'SupplierInfo')],
        "CustomerInfo/SupplierInfo")
    saft1_InvoiceNo = fields.Char(
        string="InvoiceNo", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_CustomerInfo = fields.Many2one(
        "saft.1.customerinfo",
        choice='1',
        string="CustomerInfo")
    saft1_SupplierInfo = fields.Many2one(
        "saft.1.supplierinfo",
        choice='1',
        string="SupplierInfo")
    saft1_AccountID = fields.Char(
        string="General Ledger Account code of the customer / supplier",
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code of the customer / supplier. Can"
        "\nbe including sub-account id. It can contain many"
        "\ndifferent levels to identify the Account. It could"
        "\ninclude cost centres such as company, division,"
        "\nregion, group and branch/department.")
    saft1_BranchStoreNumber = fields.Char(
        string="Branch or Storenumber",
        xsd_type="SAFmiddle1textType",
        help="Branch or Storenumber, additional segregation of"
        "\ncustomer/supplier, used if not included as part of"
        "\nthe customer/supplier id.")
    saft1_Period = fields.Integer(
        string="Accounting Period",
        xsd_type="nonNegativeInteger")
    saft1_PeriodYear = fields.Integer(
        string="The year of the Accounting Period.",
        xsd_type="PeriodYearType6")
    saft1_InvoiceDate = fields.Date(
        string="InvoiceDate", xsd_required=True,
        xsd_type="date")
    saft1_InvoiceType = fields.Char(
        string="Type of invoice: Debit invoice",
        xsd_type="SAFcodeType",
        help="Type of invoice: Debit invoice, Credit invoice, Cash, Ticket,"
        "\netc.")
    saft1_ShipTo = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship To details")
    saft1_ShipFrom = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship from Details")
    saft1_PaymentTerms = fields.Char(
        string="Payments terms for this invoice",
        xsd_type="SAFmiddle2textType")
    saft1_SelfBillingIndicator = fields.Char(
        string="Indicator showing if self",
        xsd_type="SAFcodeType",
        help="Indicator showing if self-billing is used for this invoice.")
    saft1_SourceID = fields.Char(
        string="SourceID",
        xsd_type="SAFmiddle1textType",
        help="Details of person or application that entered the transaction")
    saft1_GLPostingDate = fields.Date(
        string="Date posting to GL",
        xsd_type="date")
    saft1_BatchID = fields.Char(
        string="Systems generated ID for batch",
        xsd_type="SAFmiddle1textType")
    saft1_SystemID = fields.Char(
        string="Unique number created by the system for the document",
        xsd_type="SAFmiddle1textType")
    saft1_TransactionID = fields.Char(
        string="Cross-reference to GL posting",
        xsd_type="SAFmiddle2textType",
        help="Cross-reference to GL posting. It can contain many different"
        "\nlevels to identify the transaction. It could include"
        "\ncost centres such as company, division, region, group"
        "\nand branch/department.")
    saft1_ReceiptNumbers = fields.Char(
        string="ReceiptNumbers",
        xsd_type="SAFlongtextType",
        help="The number(s) of the receipt(s) on this 'consolidated"
        "\ninvoicerecord'. Can be a single number, a range or a"
        "\nlist.")
    saft1_Line = fields.One2many(
        "saft.1.line7",
        "saft1_Line_InvoiceStructure_id",
        string="Line", xsd_required=True
    )
    saft1_Settlement = fields.Many2one(
        "saft.1.settlement9",
        string="Settlement")
    saft1_DocumentTotals = fields.Many2one(
        "saft.1.documenttotals10",
        string="DocumentTotals")


class Journal(models.AbstractModel):
    "Journal information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.journal'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'JournalType'
    _concrete_rec_name = 'saft1_JournalID'

    saft1_Journal_GeneralLedgerEntries_id = fields.Many2one(
        "saft.1.generalledgerentries")
    saft1_JournalID = fields.Char(
        string="Source GL journal identifier",
        xsd_required=True,
        xsd_type="SAFshorttextType",
        help="Source GL journal identifier, or invoices and payments in"
        "\nsingle ledger systems.")
    saft1_Description = fields.Char(
        string="Description of the Journal.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_Type = fields.Char(
        string="Grouping mechanism for journals",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Grouping mechanism for journals. Please use the examples in"
        "\nthe technical description when appropriate.")
    saft1_Transaction = fields.One2many(
        "saft.1.transaction",
        "saft1_Transaction_Journal_id",
        string="Accounting transactions."
    )


class Line(models.AbstractModel):
    "Transaction lines."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.line'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'LineType'
    _concrete_rec_name = 'saft1_RecordID'

    saft1_Line_Transaction_id = fields.Many2one(
        "saft.1.transaction")
    saft1_choice12 = fields.Selection([
        ('saft1_DebitAmount', 'DebitAmount'),
        ('saft1_CreditAmount', 'CreditAmount')],
        "DebitAmount/CreditAmount")
    saft1_RecordID = fields.Char(
        string="RecordID", xsd_required=True,
        xsd_type="SAFshorttextType",
        help="Identifier to trace entry to journal line or posting"
        "\nreference.")
    saft1_AccountID = fields.Char(
        string="General ledger account code/number",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="General ledger account code/number. If this Line is a"
        "\nledger/sub account (accounts payable or accounts"
        "\nreceivable) entry, then this is the account"
        "\ncode/number into where this ledger/sub account is"
        "\nconsolidated in the balance sheet.")
    saft1_Analysis = fields.One2many(
        "saft.1.analysisstructure",
        "saft1_Analysis_Line_id",
        string="General Ledger analysis codes"
    )
    saft1_ValueDate = fields.Date(
        string="Effective date from which interest charged",
        xsd_type="date",
        help="Effective date from which interest charged. To be reported"
        "\nwhen this date or this Line of the accounting"
        "\ndocument/voucher differs from the TransactionDate.")
    saft1_SourceDocumentID = fields.Char(
        string="Source document number to which line relates",
        xsd_type="SAFmiddle1textType")
    saft1_CustomerID = fields.Char(
        string="Unique account code/number for the customer",
        xsd_type="SAFmiddle1textType",
        help="Unique account code/number for the customer. Is only used if"
        "\nthis Line is a ledger/sub account (accounts payable"
        "\nor accounts receivable) entry. Must not be used in"
        "\nconjunction with SupplierID.")
    saft1_SupplierID = fields.Char(
        string="Unique account code/number for the supplier",
        xsd_type="SAFmiddle1textType",
        help="Unique account code/number for the supplier. Is only used if"
        "\nthis Line is a ledger/sub account (accounts payable"
        "\nor accounts receivable) entry. Must not be used in"
        "\nconjunction with CustomerID.")
    saft1_Description = fields.Char(
        string="Description of the Journal Line.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_DebitAmount = fields.Many2one(
        "saft.1.amountstructure",
        choice='12',
        string="Debit amount information for transaction",
        xsd_required=True)
    saft1_CreditAmount = fields.Many2one(
        "saft.1.amountstructure",
        choice='12',
        string="Credit amount information for transaction",
        xsd_required=True)
    saft1_TaxInformation = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformation_Line_id",
        string="Tax information for the accounting line"
    )
    saft1_ReferenceNumber = fields.Char(
        string="The reference number",
        xsd_type="SAFmiddle1textType",
        help="The reference number, such as invoice or credit note number.")
    saft1_CID = fields.Integer(
        string="The CID number.",
        xsd_type="nonNegativeInteger")
    saft1_DueDate = fields.Date(
        string="The due date.",
        xsd_type="date")
    saft1_Quantity = fields.Float(
        currency_field="currency_id",
        string="Quantity.",
        xsd_type="SAFquantityType")
    saft1_CrossReference = fields.Char(
        string="Cross-reference",
        xsd_type="SAFmiddle1textType",
        help="Cross-reference. Information about matched documents/records.")
    saft1_SystemEntryTime = fields.Datetime(
        string="Time captured by system",
        xsd_type="dateTime",
        help="Time captured by system. The time when the transaction was"
        "\nentered into the system - manual entry, imported"
        "\ntransaction, etc.")
    saft1_OwnerID = fields.Char(
        string="The unique ID code/number for the owner",
        xsd_type="SAFmiddle1textType")


class Line3(models.AbstractModel):
    _description = 'line3'
    _name = 'saft.1.line3'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'LineType3'
    _concrete_rec_name = 'saft1_LineNumber'

    saft1_Line_Payment_id = fields.Many2one(
        "saft.1.payment")
    saft1_LineNumber = fields.Char(
        string="Number of the paymentline",
        xsd_type="SAFshorttextType")
    saft1_SourceDocumentID = fields.Char(
        string="The source document to which the line relates",
        xsd_type="SAFmiddle1textType")
    saft1_AccountID = fields.Char(
        string="General Ledger Account code",
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code. Can be including sub-account id."
        "\nIt can contain many different levels to identify the"
        "\nAccount. It could include cost centres such as"
        "\ncompany, division, region, group and"
        "\nbranch/department.")
    saft1_Analysis = fields.One2many(
        "saft.1.analysisstructure",
        "saft1_Analysis_Line3_id",
        string="General Ledger analysis codes"
    )
    saft1_CustomerID = fields.Char(
        string="Unique code for the customer",
        xsd_type="SAFmiddle1textType")
    saft1_SupplierID = fields.Char(
        string="Unique code for the supplier",
        xsd_type="SAFmiddle1textType")
    saft1_TaxPointDate = fields.Date(
        string="TaxPointDate",
        xsd_type="date",
        help="Tax Point date where recorded or if not recorded then the"
        "\nInvoice date")
    saft1_Description = fields.Char(
        string="Description of the payment line.",
        xsd_type="SAFlongtextType")
    saft1_DebitCreditIndicator = fields.Selection(
        DEBITCREDITINDICATOR_LINE,
        string="Indicates whether the amounts on line",
        xsd_required=True,
        help="Indicates whether the amounts on line-level are debit or"
        "\ncredit amounts. Entry must correspond to entry"
        "\nreflected in General Ledger Entry. Signing of"
        "\nlineamounts is relative to this indicator. E.g. a"
        "\nreturn can lead to a negative amount.")
    saft1_PaymentLineAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Amount for transaction excluding taxes",
        xsd_required=True)
    saft1_TaxInformation = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformation_Line3_id",
        string="TaxInformation"
    )


class Line4(models.AbstractModel):
    "Not needed when UOM of this line equals UOMPhysicalStock"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.line4'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'LineType4'
    _concrete_rec_name = 'saft1_LineNumber'

    saft1_Line_StockMovement_id = fields.Many2one(
        "saft.1.stockmovement")
    saft1_LineNumber = fields.Char(
        string="Number of the movementline",
        xsd_required=True,
        xsd_type="SAFshorttextType")
    saft1_AccountID = fields.Char(
        string="General Ledger Account code",
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code. Can be including sub-account id.")
    saft1_TransactionID = fields.Char(
        string="Cross-reference to GL posting",
        xsd_type="SAFmiddle2textType",
        help="Cross-reference to GL posting. It can contain many different"
        "\nlevels to identify the transaction. It could include"
        "\ncost centres such as company, division, region, group"
        "\nand branch/department.")
    saft1_CustomerID = fields.Char(
        string="Unique code for the customer",
        xsd_type="SAFmiddle1textType")
    saft1_SupplierID = fields.Char(
        string="Unique code for the supplier",
        xsd_type="SAFmiddle1textType")
    saft1_ShipTo = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship To details")
    saft1_ShipFrom = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship from Details")
    saft1_ProductCode = fields.Char(
        string="Product code", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_StockAccountNo = fields.Char(
        string="Stock batch",
        xsd_type="SAFmiddle2textType",
        help="Stock batch, lot, serial identification. Not used when there"
        "\nis exactly 1 PhysicalStock entry per ProductCode")
    saft1_Quantity = fields.Float(
        currency_field="currency_id",
        string="Quantity of goods",
        xsd_required=True,
        xsd_type="SAFquantityType")
    saft1_UnitOfMeasure = fields.Char(
        string="Quantity unit of measure e.g",
        xsd_type="SAFcodeType",
        help="Quantity unit of measure e.g. pack of 12")
    saft1_UOMToUOMPhysicalStockConversionFactor = fields.Float(
        currency_field="currency_id",
        string="Conversion factor of the UOM to UOM Physical Stock",
        xsd_type="decimal")
    saft1_BookValue = fields.Float(
        currency_field="currency_id",
        string="BookValue",
        xsd_type="SAFmonetaryType",
        help="Value of the transaction line as registrerd in the general"
        "\nledger in the header's default currency.")
    saft1_MovementSubType = fields.Char(
        string="Indentify the type of the movement on line / article level",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Indentify the type of the movement on line / article level. A"
        "\nmovement(type) production contains f.i. use of"
        "\ncomponents, getting finished product, efficiencyloss"
        "\nas movementsubtypes. Predescribed TABLE is possible.")
    saft1_MovementComments = fields.Char(
        string="A reason for the movement",
        xsd_type="SAFlongtextType")
    saft1_TaxInformation = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformation_Line4_id",
        string="TaxInformation"
    )


class Line7(models.AbstractModel):
    _description = 'line7'
    _name = 'saft.1.line7'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'LineType7'
    _concrete_rec_name = 'saft1_LineNumber'

    saft1_Line_InvoiceStructure_id = fields.Many2one(
        "saft.1.invoicestructure")
    saft1_LineNumber = fields.Char(
        string="Number of the invoiceline",
        xsd_type="SAFshorttextType")
    saft1_AccountID = fields.Char(
        string="General Ledger Account code of the GL",
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code of the GL-revenue-account. Can be"
        "\nincluding sub-account id. It can contain many"
        "\ndifferent levels to identify the Account. It could"
        "\ninclude cost centres such as company, division,"
        "\nregion, group and branch/department.")
    saft1_Analysis = fields.One2many(
        "saft.1.analysisstructure",
        "saft1_Analysis_Line7_id",
        string="General Ledger analysis codes"
    )
    saft1_OrderReferences = fields.One2many(
        "saft.1.orderreferences",
        "saft1_OrderReferences_Line7_id",
        string="Relevant order references"
    )
    saft1_ShipTo = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship To details")
    saft1_ShipFrom = fields.Many2one(
        "saft.1.shippingpointstructure",
        string="Ship from Details")
    saft1_GoodsServicesID = fields.Char(
        string="Indicator showing if goods or service",
        xsd_type="SAFcodeType")
    saft1_ProductCode = fields.Char(
        string="Product code",
        xsd_type="SAFmiddle2textType")
    saft1_ProductDescription = fields.Char(
        string="Description of goods or services.",
        xsd_type="SAFlongtextType")
    saft1_Delivery = fields.Many2one(
        "saft.1.delivery",
        string="Delivery",
        help="Information about the date or timeframe of the delivery of"
        "\nthe goods or services.")
    saft1_Quantity = fields.Float(
        currency_field="currency_id",
        string="Quantity of goods and services supplied",
        xsd_type="SAFquantityType")
    saft1_InvoiceUOM = fields.Char(
        string="Quantity unit of measure e.g",
        xsd_type="SAFcodeType",
        help="Quantity unit of measure e.g. pack of 12")
    saft1_UOMToUOMBaseConversionFactor = fields.Float(
        currency_field="currency_id",
        string="Conversion factor of the InvoiceUOM to UOM Base",
        xsd_type="decimal",
        help="Conversion factor of the InvoiceUOM to UOM Base. Only needed"
        "\nwhen InvoiceUOM is reported and is different from the"
        "\nUOM Base.")
    saft1_UnitPrice = fields.Float(
        currency_field="currency_id",
        string="UnitPrice", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Unit price for the unit/group of units per UOM in the"
        "\nheader's default currency.")
    saft1_TaxPointDate = fields.Date(
        string="TaxPointDate", xsd_required=True,
        xsd_type="date",
        help="Tax Point date where recorded or if not recorded then the"
        "\nInvoice date")
    saft1_References = fields.Many2one(
        "saft.1.references",
        string="Credit Note references")
    saft1_Description = fields.Char(
        string="Description of Invoice Line.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_InvoiceLineAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Amount for transaction excluding taxes and freightcharges",
        xsd_required=True)
    saft1_DebitCreditIndicator = fields.Selection(
        DEBITCREDITINDICATOR_LINE,
        string="Indicates whether the amounts on line",
        xsd_required=True,
        help="Indicates whether the amounts on line-level are debit or"
        "\ncredit amounts. Entry must correspond to entry"
        "\nreflected in General Ledger Entry. Signing of"
        "\nlineamounts is relative to this indicator. E.g. a"
        "\nreturn can lead to a negative amount.")
    saft1_ShippingCostsAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Amount for shipping/freight charges.")
    saft1_TaxInformation = fields.One2many(
        "saft.1.taxinformationstructure",
        "saft1_TaxInformation_Line7_id",
        string="TaxInformation"
    )


class MasterFiles(models.AbstractModel):
    """Holds standing data about general ledger account, suppliers, customers,
    products, etc.. An extension point is provided to allow Revenue Bodies
    to specify additional elements or structures such as tax rate
    tables."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.masterfiles'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'MasterFilesType'
    _concrete_rec_name = 'saft1_GeneralLedgerAccounts'

    saft1_GeneralLedgerAccounts = fields.Many2one(
        "saft.1.generalledgeraccounts",
        string="The general ledger accounts of a company")
    saft1_Taxonomies = fields.Many2one(
        "saft.1.taxonomies",
        string="Not in use.")
    saft1_Customers = fields.Many2one(
        "saft.1.customers",
        string="The customers of a company.")
    saft1_Suppliers = fields.Many2one(
        "saft.1.suppliers",
        string="The suppliers of a company.")
    saft1_TaxTable = fields.Many2one(
        "saft.1.taxtable",
        string="The tax tables of a company.")
    saft1_UOMTable = fields.Many2one(
        "saft.1.uomtable",
        string="Not in use. (UOMTable)")
    saft1_AnalysisTypeTable = fields.Many2one(
        "saft.1.analysistable",
        string="Table with the analysis code identifiers",
        help="Table with the analysis code identifiers. Used for further"
        "\nspecification of transaction data. Example: cost"
        "\nunit, cost center, project, department, provider,"
        "\njournal type, employees, etc. Journal type"
        "\n(bilagsart) should always be used on all"
        "\ntransactions.")
    saft1_MovementTypeTable = fields.Many2one(
        "saft.1.movementtable",
        string="Not in use. (MovementTypeTable)")
    saft1_Products = fields.Many2one(
        "saft.1.products",
        string="Not in use. (Products)")
    saft1_PhysicalStock = fields.Many2one(
        "saft.1.physicalstock",
        string="Not in use. (PhysicalStock)")
    saft1_Owners = fields.Many2one(
        "saft.1.owners",
        string="The owners of a company.")
    saft1_Assets = fields.Many2one(
        "saft.1.assets",
        string="Not in use. (Assets)")


class MovementOfGoods(models.AbstractModel):
    _description = 'movementofgoods'
    _name = 'saft.1.movementofgoods'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'MovementOfGoodsType'
    _concrete_rec_name = 'saft1_NumberOfMovementLines'

    saft1_NumberOfMovementLines = fields.Integer(
        string="Number of movementlines in selected period",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_TotalQuantityReceived = fields.Float(
        currency_field="currency_id",
        string="Quantity of goods received",
        xsd_required=True,
        xsd_type="SAFquantityType")
    saft1_TotalQuantityIssued = fields.Float(
        currency_field="currency_id",
        string="Quantity of goods issued in selected period",
        xsd_required=True,
        xsd_type="SAFquantityType")
    saft1_StockMovement = fields.One2many(
        "saft.1.stockmovement",
        "saft1_StockMovement_MovementOfGoods_id",
        string="StockMovement",
        xsd_required=True
    )


class MovementTableEntry(models.AbstractModel):
    _description = 'movementtableentry'
    _name = 'saft.1.movementtableentry'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'MovementTypeTableEntryType'
    _concrete_rec_name = 'saft1_MovementType'

    saft1_MovementTypeTableEntry_MovementTable_id = fields.Many2one(
        "saft.1.movementtable")
    saft1_MovementType = fields.Char(
        string="Identify kind of movement or movement line",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Identify kind of movement or movement line. E.g. sale,"
        "\npurchase, adjustment, etc. Or efficiencyloss, use of"
        "\ncomponents in production, etc. Predescribed TABLE is"
        "\npossible.")
    saft1_Description = fields.Char(
        string="Description of the movement(sub)type",
        xsd_required=True,
        xsd_type="SAFlongtextType")


class MovementTable(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.movementtable'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'MovementTypeTableType'
    _concrete_rec_name = 'saft1_MovementTypeTableEntry'

    saft1_MovementTypeTableEntry = fields.One2many(
        "saft.1.movementtableentry",
        "saft1_MovementTypeTableEntry_MovementTable_id",
        string="MovementTypeTableEntry",
        xsd_required=True
    )


class OrderReferences(models.AbstractModel):
    "Relevant order references"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.orderreferences'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'OrderReferencesType'
    _concrete_rec_name = 'saft1_OriginatingON'

    saft1_OrderReferences_Line7_id = fields.Many2one(
        "saft.1.line7")
    saft1_OriginatingON = fields.Char(
        string="Origination Order Number",
        xsd_type="SAFmiddle2textType")
    saft1_OrderDate = fields.Date(
        string="Date of order",
        xsd_type="date")


class Owner(models.AbstractModel):
    "Owner information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.owner'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'OwnerType'
    _concrete_rec_name = 'saft1_OwnerID'

    saft1_Owner_Owners_id = fields.Many2one(
        "saft.1.owners")
    saft1_OwnerID = fields.Char(
        string="Unique ID code/number for the owner.",
        xsd_type="SAFmiddle1textType")
    saft1_AccountID = fields.Char(
        string="General ledger account code for this owner",
        xsd_type="SAFmiddle2textType",
        help="General ledger account code for this owner. Can be including"
        "\nsub-account id. It can contain many different levels"
        "\nto identify the Account.")


class Owners(models.AbstractModel):
    "The owners of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.owners'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'OwnersType'
    _concrete_rec_name = 'saft1_Owner'

    saft1_Owner = fields.One2many(
        "saft.1.owner",
        "saft1_Owner_Owners_id",
        string="Owner information.", xsd_required=True
    )


class PartyInfoStructure(models.AbstractModel):
    "Additional party information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.partyinfostructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PartyInfoStructure'
    _concrete_rec_name = 'saft1_PaymentTerms'

    saft1_PaymentTerms = fields.Many2one(
        "saft.1.paymentterms",
        string="Payment terms of the party.")
    saft1_NaceCode = fields.Char(
        string="NACE",
        xsd_type="SAFshorttextType",
        help="NACE (Nomenclature of Economic Activities) is the European"
        "\nstatistical classification of economic activities.")
    saft1_CurrencyCode = fields.Char(
        string="Three",
        xsd_type="ISOCurrencyCode",
        help="Three-letter currency code according to ISO 4217 standard.")
    saft1_Type = fields.Selection(
        _PARTYINFOSTRUCTURE,
        string="Type of party.",
        help="Type of party."
        "\nEnumerated"
        "\nPrivate, Company, Government")
    saft1_Status = fields.Selection(
        STATUS_PARTYINFOSTRUCTURE,
        string="Type of account.",
        help="Type of account."
        "\nEnumerated"
        "\nActive, Observation, Passive.")
    saft1_Analysis = fields.One2many(
        "saft.1.analysispartyinfostructure",
        "saft1_Analysis_PartyInfoStructure_id",
        string="Standard analysis codes for the party",
        help="Standard analysis codes for the party, such as project,"
        "\ndepartment, cost center, groups, etc."
    )
    saft1_Notes = fields.Char(
        string="Notes.",
        xsd_type="string")


class PaymentTerms(models.AbstractModel):
    "Payment terms of the party."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.paymentterms'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PaymentTermsType'
    _concrete_rec_name = 'saft1_Days'

    saft1_Days = fields.Integer(
        string="Days of respite before due date from invoice date",
        xsd_type="nonNegativeInteger")
    saft1_Months = fields.Integer(
        string="Months of respite before due date from invoice date",
        xsd_type="nonNegativeInteger")
    saft1_CashDiscountDays = fields.Integer(
        string="CashDiscountDays",
        xsd_type="nonNegativeInteger",
        help="Number of days from the invoice date the cash discount can be"
        "\ndeducted.")
    saft1_CashDiscountRate = fields.Float(
        currency_field="currency_id",
        string="Rate for calculating cash discount.",
        xsd_type="CashDiscountRateType")
    saft1_FreeBillingMonth = fields.Boolean(
        string="FreeBillingMonth",
        xsd_type="boolean",
        help="Indicator that states whether free billing month is used or"
        "\nnot. Free billing month sets the deadline to the last"
        "\ndate of the invoice month.")


class Payment(models.AbstractModel):
    _description = 'payment'
    _name = 'saft.1.payment'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PaymentType'
    _concrete_rec_name = 'saft1_PaymentRefNo'

    saft1_Payment_Payments_id = fields.Many2one(
        "saft.1.payments")
    saft1_PaymentRefNo = fields.Char(
        string="Unique reference number for payment",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_Period = fields.Integer(
        string="Accounting Period",
        xsd_type="nonNegativeInteger")
    saft1_PeriodYear = fields.Integer(
        string="The year of the Accounting Period.",
        xsd_type="PeriodYearType2")
    saft1_TransactionID = fields.Char(
        string="Cross-reference to GL posting",
        xsd_type="SAFmiddle2textType",
        help="Cross-reference to GL posting. It can contain many different"
        "\nlevels to identify the transaction. It could include"
        "\ncost centres such as company, division, region, group"
        "\nand branch/department.")
    saft1_TransactionDate = fields.Date(
        string="Document date",
        xsd_required=True,
        xsd_type="date")
    saft1_PaymentMethod = fields.Char(
        string="Cheque, Bank, Giro, Cash, etc.",
        xsd_type="SAFcodeType")
    saft1_Description = fields.Char(
        string="Description of the payment.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_BatchID = fields.Char(
        string="Systems generated ID for batch",
        xsd_type="SAFmiddle1textType")
    saft1_SystemID = fields.Char(
        string="Unique number created by the system for the document",
        xsd_type="SAFmiddle1textType")
    saft1_SourceID = fields.Char(
        string="SourceID",
        xsd_type="SAFmiddle1textType",
        help="Details of person or application that entered the transaction")
    saft1_Line = fields.One2many(
        "saft.1.line3",
        "saft1_Line_Payment_id",
        string="Line", xsd_required=True
    )
    saft1_Settlement = fields.Many2one(
        "saft.1.settlement",
        string="Settlement")
    saft1_DocumentTotals = fields.Many2one(
        "saft.1.documenttotals",
        string="DocumentTotals")


class Payments(models.AbstractModel):
    _description = 'payments'
    _name = 'saft.1.payments'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PaymentsType'
    _concrete_rec_name = 'saft1_NumberOfEntries'

    saft1_NumberOfEntries = fields.Integer(
        string="Number of entries",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_TotalDebit = fields.Float(
        currency_field="currency_id",
        string="TotalDebit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all debit amounts in the header's default"
        "\ncurrency")
    saft1_TotalCredit = fields.Float(
        currency_field="currency_id",
        string="TotalCredit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all credit amounts in the header's default"
        "\ncurrency")
    saft1_Payment = fields.One2many(
        "saft.1.payment",
        "saft1_Payment_Payments_id",
        string="Payment", xsd_required=True
    )


class PersonNameStructure(models.AbstractModel):
    "All information about the name of a natural person."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.personnamestructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PersonNameStructure'
    _concrete_rec_name = 'saft1_Title'

    saft1_Title = fields.Char(
        string="Not in use.",
        xsd_type="SAFcodeType")
    saft1_FirstName = fields.Char(
        string="First name of the person",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="First name of the person. If the name of the person is in an"
        "\nunstructured form, insert “NotUsed” in this element"
        "\nand enter the full unstructured name in the LastName"
        "\nelement.")
    saft1_Initials = fields.Char(
        string="Initials.",
        xsd_type="SAFshorttextType")
    saft1_LastNamePrefix = fields.Char(
        string="LastNamePrefix",
        xsd_type="SAFshorttextType",
        help="A textual expression of a prefix that precedes this person's"
        "\nfamily name such as Van, Von.")
    saft1_LastName = fields.Char(
        string="Last name of the person",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="Last name of the person. If the FirstName element has the"
        "\ntext “NotUsed” then this element should contain the"
        "\nfull unstructured name of the person.")
    saft1_BirthName = fields.Char(
        string="Birth name of the person.",
        xsd_type="SAFmiddle2textType")
    saft1_Salutation = fields.Char(
        string="A formal sign or expression of greeting",
        xsd_type="SAFshorttextType",
        help="A formal sign or expression of greeting, expressed as text,"
        "\nthat is appropriate for this person such as Right"
        "\nHonourable, Monsignor or Madam.")
    saft1_OtherTitles = fields.Char(
        string="Used for roles in the company",
        xsd_type="SAFshorttextType",
        help="Used for roles in the company, such as Daglig leder,"
        "\nStyreleder, Regnskapsfører, etc.")


class PhysicalStockEntry(models.AbstractModel):
    "Not needed when UOMPhysicalStock equals UOMBase"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.physicalstockentry'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PhysicalStockEntryType'
    _concrete_rec_name = 'saft1_WarehouseID'

    saft1_PhysicalStockEntry_PhysicalStock_id = fields.Many2one(
        "saft.1.physicalstock")
    saft1_WarehouseID = fields.Char(
        string="Warehouse where goods held",
        xsd_type="SAFmiddle1textType",
        help="Warehouse where goods held - possoble also to identify work-"
        "\nin-progress, or stock-in-transit")
    saft1_LocationID = fields.Char(
        string="Location of goods in warehouse",
        xsd_type="SAFshorttextType")
    saft1_ProductCode = fields.Char(
        string="Product code", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_StockAccountNo = fields.Char(
        string="Stock batch",
        xsd_type="SAFmiddle2textType",
        help="Stock batch, lot, serial identification. Not used when there"
        "\nis exactly 1 PhysicalStock entry per ProductCode")
    saft1_ProductType = fields.Char(
        string="ProductType",
        xsd_type="SAFshorttextType",
        help="To determine whether the product/stockaccount is raw"
        "\nmaterial, work-in-progress, finished good,"
        "\nmerchandise for resale, etc.")
    saft1_ProductStatus = fields.Char(
        string="ProductStatus",
        xsd_type="SAFshorttextType",
        help="To determine whether the product/stockaccount is"
        "\ndiscontinued, damaged, obsolete, active, etc.")
    saft1_StockAccountCommodityCode = fields.Char(
        string="Classification for import / export",
        xsd_type="SAFmiddle1textType")
    saft1_OwnerID = fields.Char(
        string="Reference to the owner Master File",
        xsd_type="SAFmiddle1textType")
    saft1_UOMPhysicalStock = fields.Char(
        string="Unit of Measurement for this Physical Stock position",
        xsd_type="SAFcodeType")
    saft1_UOMToUOMBaseConversionFactor = fields.Float(
        currency_field="currency_id",
        string="Conversion factor of the UOM to UOM Base",
        xsd_type="decimal")
    saft1_UnitPrice = fields.Float(
        currency_field="currency_id",
        string="UnitPrice",
        xsd_type="SAFmonetaryType",
        help="Base Unit price for this stock account in the header's"
        "\ndefault currency.")
    saft1_OpeningStockQuantity = fields.Float(
        currency_field="currency_id",
        string="In UOM Physical Stock for selection period",
        xsd_required=True,
        xsd_type="SAFquantityType")
    saft1_OpeningStockValue = fields.Float(
        currency_field="currency_id",
        string="In the header's currency code for selection period",
        xsd_type="SAFmonetaryType",
        help="In the header's currency code for selection period")
    saft1_ClosingStockQuantity = fields.Float(
        currency_field="currency_id",
        string="ClosingStockQuantity",
        xsd_required=True,
        xsd_type="SAFquantityType")
    saft1_ClosingStockValue = fields.Float(
        currency_field="currency_id",
        string="ClosingStockValue",
        xsd_type="SAFmonetaryType",
        help="Closing stock value in the header's default currency for"
        "\nselection period")
    saft1_StockCharacteristics = fields.Many2one(
        "saft.1.stockcharacteristics",
        string="StockCharacteristics")


class PhysicalStock(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.physicalstock'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PhysicalStockType'
    _concrete_rec_name = 'saft1_PhysicalStockEntry'

    saft1_PhysicalStockEntry = fields.One2many(
        "saft.1.physicalstockentry",
        "saft1_PhysicalStockEntry_PhysicalStock_id",
        string="PhysicalStockEntry",
        xsd_required=True
    )


class Product(models.AbstractModel):
    "Not needed when not applicable"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.product'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ProductType'
    _concrete_rec_name = 'saft1_ProductCode'

    saft1_Product_Products_id = fields.Many2one(
        "saft.1.products")
    saft1_ProductCode = fields.Char(
        string="Product code", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_GoodsServicesID = fields.Char(
        string="Indicator showing if goods or services",
        xsd_type="SAFcodeType",
        help="Indicator showing if goods or services (Predescribed TABLE is"
        "\npossible)")
    saft1_ProductGroup = fields.Char(
        string="ProductGroup",
        xsd_type="SAFmiddle2textType",
        help="Code identifying aggregated level at which similar products"
        "\nare grouped")
    saft1_Description = fields.Char(
        string="Description of goods or services.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_ProductCommodityCode = fields.Char(
        string="Classification for import / export",
        xsd_type="SAFmiddle1textType")
    saft1_ProductNumberCode = fields.Char(
        string="EAN or other code",
        xsd_type="SAFmiddle2textType")
    saft1_ValuationMethod = fields.Char(
        string="FIFO, LIFO, Average cost etc.",
        xsd_type="SAFcodeType")
    saft1_UOMBase = fields.Char(
        string="UOMBase", xsd_required=True,
        xsd_type="SAFcodeType",
        help="Unit of measure for Stock Administration for this product"
        "\nPredescribed TABLE is possible.")
    saft1_UOMStandard = fields.Char(
        string="A Standard Unit of Measure applicable for this product",
        xsd_type="SAFcodeType",
        help="A Standard Unit of Measure applicable for this product, f.i."
        "\nKilo, Metres, Litres (Predescribed TABLE is possible)")
    saft1_UOMToUOMBaseConversionFactor = fields.Float(
        currency_field="currency_id",
        string="Conversion factor of the UOM to UOM Base",
        xsd_type="decimal")
    saft1_Tax = fields.One2many(
        "saft.1.tax",
        "saft1_Tax_Product_id",
        string="Tax"
    )


class Products(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.products'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ProductsType'
    _concrete_rec_name = 'saft1_Product'

    saft1_Product = fields.One2many(
        "saft.1.product",
        "saft1_Product_Products_id",
        string="Product", xsd_required=True
    )


class PurchaseInvoices(models.AbstractModel):
    _description = 'purchaseinvoices'
    _name = 'saft.1.purchaseinvoices'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'PurchaseInvoicesType'
    _concrete_rec_name = 'saft1_NumberOfEntries'

    saft1_NumberOfEntries = fields.Integer(
        string="Number of entries",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_TotalDebit = fields.Float(
        currency_field="currency_id",
        string="TotalDebit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all debit amounts in the header's default"
        "\ncurrency")
    saft1_TotalCredit = fields.Float(
        currency_field="currency_id",
        string="TotalCredit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all credit amounts in the header's default"
        "\ncurrency")
    saft1_Invoice = fields.One2many(
        "saft.1.invoicestructure",
        "saft1_Invoice_PurchaseInvoices_id",
        string="Invoice", xsd_required=True
    )


class References(models.AbstractModel):
    "Credit Note references"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.references'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ReferencesType'
    _concrete_rec_name = 'saft1_CreditNote'

    saft1_CreditNote = fields.Many2one(
        "saft.1.creditnote",
        string="CreditNote")


class SalesInvoices(models.AbstractModel):
    _description = 'salesinvoices'
    _name = 'saft.1.salesinvoices'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SalesInvoicesType'
    _concrete_rec_name = 'saft1_NumberOfEntries'

    saft1_NumberOfEntries = fields.Integer(
        string="Number of entries",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_TotalDebit = fields.Float(
        currency_field="currency_id",
        string="TotalDebit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all debit amounts in the header's default"
        "\ncurrency")
    saft1_TotalCredit = fields.Float(
        currency_field="currency_id",
        string="TotalCredit", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="The total of all credit amounts in the header's default"
        "\ncurrency")
    saft1_Invoice = fields.One2many(
        "saft.1.invoicestructure",
        "saft1_Invoice_SalesInvoices_id",
        string="Invoice", xsd_required=True
    )


class SelectionCriteriaStructure(models.AbstractModel):
    """The selection criteria used to generate this Standard Auditfile.Allows
    for a choice between selection on calendar dates and periods according
    to the accounting system, e.g. 1 to 12 for a 12-months accounting
    system."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.selectioncriteriastructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SelectionCriteriaStructure'
    _concrete_rec_name = 'saft1_TaxReportingJurisdiction'

    saft1_choice3 = fields.Selection([
        ('saft1_SelectionStartDate', 'SelectionStartDate'),
        ('saft1_SelectionEndDate', 'SelectionEndDate'),
        ('saft1_PeriodStart', 'PeriodStart'),
        ('saft1_PeriodStartYear', 'PeriodStartYear'),
        ('saft1_PeriodEnd', 'PeriodEnd'),
        ('saft1_PeriodEndYear', 'PeriodEndYear')],
        "SelectionStartDate/SelectionEndDate/PeriodStart/Pe...")
    saft1_TaxReportingJurisdiction = fields.Char(
        string="TaxReportingJurisdiction",
        xsd_type="SAFmiddle1textType",
        help="Identifies the tax jurisdiction for whose purpose the SAF has"
        "\nbeen created. Principally for use where a single"
        "\nRevenue body covers more than one territory.")
    saft1_CompanyEntity = fields.Char(
        string="CompanyEntity",
        xsd_type="SAFmiddle2textType",
        help="For use where data has been extracted from the full data set"
        "\nby reference to a specific corporate entity.")
    saft1_SelectionStartDate = fields.Date(
        choice='3',
        string="The start date for the reporting period covered by the SAF",
        xsd_required=True,
        xsd_type="date")
    saft1_SelectionEndDate = fields.Date(
        choice='3',
        string="The end date for the reporting period covered by the SAF",
        xsd_required=True,
        xsd_type="date")
    saft1_PeriodStart = fields.Integer(
        choice='3',
        string="The first Accounting Period covered by the SAF",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_PeriodStartYear = fields.Integer(
        choice='3',
        string="The Accounting Year in which the PeriodStart falls",
        xsd_required=True,
        xsd_type="PeriodStartYearType")
    saft1_PeriodEnd = fields.Integer(
        choice='3',
        string="The last Accounting Period covered by the SAF",
        xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_PeriodEndYear = fields.Integer(
        choice='3',
        string="The Accounting Year in which the PeriodEnd falls",
        xsd_required=True,
        xsd_type="PeriodEndYearType")
    saft1_DocumentType = fields.Char(
        string="Type of documents selected",
        xsd_type="SAFlongtextType",
        help="Type of documents selected. For use where the data has been"
        "\nrestricted by reference to particular transaction"
        "\ntypes.")
    saft1_OtherCriteria = fields.Char(
        string="Any other criteria used in selecting data",
        xsd_type="SAFlongtextType",
        help="Any other criteria used in selecting data. Individual Revenue"
        "\nBodies may wish to draw up a list of other acceptable"
        "\nselection criteria for use within their jurisdiction.")


class Settlement(models.AbstractModel):
    _description = 'settlement'
    _name = 'saft.1.settlement'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SettlementType'
    _concrete_rec_name = 'saft1_SettlementDiscount'

    saft1_SettlementDiscount = fields.Char(
        string="Description Settlement / Other Discount",
        xsd_type="SAFmiddle1textType",
        help="Description Settlement / Other Discount")
    saft1_SettlementAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Settlement amount")
    saft1_SettlementDate = fields.Date(
        string="Date settled",
        xsd_type="date")
    saft1_PaymentMechanism = fields.Char(
        string="Payment mechanism",
        xsd_type="SAFcodeType")


class Settlement9(models.AbstractModel):
    _description = 'settlement9'
    _name = 'saft.1.settlement9'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SettlementType9'
    _concrete_rec_name = 'saft1_SettlementDiscount'

    saft1_SettlementDiscount = fields.Char(
        string="Description Settlement / Other Discount",
        xsd_type="SAFmiddle1textType",
        help="Description Settlement / Other Discount")
    saft1_SettlementAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Settlement amount",
        xsd_required=True)
    saft1_SettlementDate = fields.Date(
        string="Date settled",
        xsd_type="date")
    saft1_PaymentMechanism = fields.Char(
        string="Payment mechanism",
        xsd_type="SAFcodeType")


class ShippingPointStructure(models.AbstractModel):
    "A structure that holds all shipping point information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.shippingpointstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ShippingPointStructure'
    _concrete_rec_name = 'saft1_DeliveryID'

    saft1_DeliveryID = fields.Char(
        string="Identification of the delivery",
        xsd_type="SAFmiddle1textType")
    saft1_DeliveryDate = fields.Date(
        string="Date goods are delivered",
        xsd_type="date")
    saft1_WarehouseID = fields.Char(
        string="Warehouse where goods held",
        xsd_type="SAFmiddle1textType",
        help="Warehouse where goods held - also to identify work-in-"
        "\nprogress, or stock-in-transit")
    saft1_LocationID = fields.Char(
        string="Location of goods in warehouse",
        xsd_type="SAFshorttextType")
    saft1_UCR = fields.Char(
        string="Unique consignment reference number",
        xsd_type="SAFmiddle1textType")
    saft1_Address = fields.Many2one(
        "saft.1.addressstructure",
        string="Address")


class SourceDocuments(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.sourcedocuments'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SourceDocumentsType'
    _concrete_rec_name = 'saft1_SalesInvoices'

    saft1_SalesInvoices = fields.Many2one(
        "saft.1.salesinvoices",
        string="SalesInvoices")
    saft1_PurchaseInvoices = fields.Many2one(
        "saft.1.purchaseinvoices",
        string="PurchaseInvoices")
    saft1_Payments = fields.Many2one(
        "saft.1.payments",
        string="Payments")
    saft1_MovementOfGoods = fields.Many2one(
        "saft.1.movementofgoods",
        string="MovementOfGoods")
    saft1_AssetTransactions = fields.Many2one(
        "saft.1.assettransactions",
        string="AssetTransactions",
        help="Details of all transactions related to an asset during the"
        "\nSelectionperiod.")


class StockCharacteristics(models.AbstractModel):
    _description = 'stockcharacteristics'
    _name = 'saft.1.stockcharacteristics'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'StockCharacteristicsType'
    _concrete_rec_name = 'saft1_StockCharacteristic'

    saft1_StockCharacteristic = fields.Char(
        string="User definable characteristics of the goods",
        xsd_required=True,
        xsd_type="SAFshorttextType",
        help="User definable characteristics of the goods. Predescribed"
        "\nTABLE is possible.")
    saft1_StockCharacteristicValue = fields.Char(
        string="The weight, pack size, colour etc.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")


class StockMovement(models.AbstractModel):
    _description = 'stockmovement'
    _name = 'saft.1.stockmovement'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'StockMovementType'
    _concrete_rec_name = 'saft1_MovementReference'

    saft1_StockMovement_MovementOfGoods_id = fields.Many2one(
        "saft.1.movementofgoods")
    saft1_MovementReference = fields.Char(
        string="Unique reference to the movement.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_MovementDate = fields.Date(
        string="Document date",
        xsd_required=True,
        xsd_type="date")
    saft1_MovementPostingDate = fields.Date(
        string="MovementPostingDate",
        xsd_type="date",
        help="Date of posting of the movement if different to Movement Date")
    saft1_TaxPointDate = fields.Date(
        string="Date of supply of goods",
        xsd_type="date")
    saft1_MovementType = fields.Char(
        string="MovementType", xsd_required=True,
        xsd_type="SAFcodeType",
        help="The movementtype expresses the type of the process for the"
        "\nunderlaying lines. E.g. production, sales, purchase."
        "\nPredescribed TABLE is possible.")
    saft1_SourceID = fields.Char(
        string="SourceID",
        xsd_type="SAFmiddle1textType",
        help="Details of person or application that entered the transaction")
    saft1_SystemID = fields.Char(
        string="Unique number created by the system for the document",
        xsd_type="SAFmiddle1textType")
    saft1_DocumentReference = fields.Many2one(
        "saft.1.documentreference",
        string="DocumentReference")
    saft1_Line = fields.One2many(
        "saft.1.line4",
        "saft1_Line_StockMovement_id",
        string="Line", xsd_required=True
    )


class SupplierInfo(models.AbstractModel):
    _description = 'supplierinfo'
    _name = 'saft.1.supplierinfo'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SupplierInfoType'
    _concrete_rec_name = 'saft1_SupplierID'

    saft1_choice14 = fields.Selection([
        ('saft1_SupplierID', 'SupplierID'),
        ('saft1_Name', 'Name')],
        "SupplierID/Name")
    saft1_SupplierID = fields.Char(
        choice='14',
        string="Unique code for the supplier",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_Name = fields.Char(
        choice='14',
        string="Name of the supplier", xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_BillingAddress = fields.Many2one(
        "saft.1.addressstructure",
        string="BillingAddress",
        xsd_required=True)


class Supplier(models.AbstractModel):
    "Supplier information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.supplier'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SupplierType'
    _concrete_rec_name = 'saft1_SupplierID'

    saft1_Supplier_Suppliers_id = fields.Many2one(
        "saft.1.suppliers")
    saft1_choice8 = fields.Selection([
        ('saft1_OpeningDebitBalance', 'OpeningDebitBalance'),
        ('saft1_OpeningCreditBalance', 'OpeningCreditBalance')],
        "OpeningDebitBalance/OpeningCreditBalance")
    saft1_choice9 = fields.Selection([
        ('saft1_ClosingDebitBalance', 'ClosingDebitBalance'),
        ('saft1_ClosingCreditBalance', 'ClosingCreditBalance')],
        "ClosingDebitBalance/ClosingCreditBalance")
    saft1_SupplierID = fields.Char(
        string="Unique account code/number for the supplier",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_SelfBillingIndicator = fields.Char(
        string="Indicator showing if a self",
        xsd_type="SAFcodeType",
        help="Indicator showing if a self-billing agreement exists between"
        "\nthe customer and the supplier.")
    saft1_AccountID = fields.Char(
        string="General ledger account code/number for this supplier",
        xsd_type="SAFmiddle2textType",
        help="General ledger account code/number for this supplier. This is"
        "\nthe account code/number into where this sub"
        "\naccount/accounts payable is consolidated in the"
        "\nbalance sheet.")
    saft1_OpeningDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='8',
        string="OpeningDebitBalance",
        xsd_type="SAFmonetaryType",
        help="Debit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_OpeningCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='8',
        string="OpeningCreditBalance",
        xsd_type="SAFmonetaryType",
        help="Credit balance at the start date of the selection period in"
        "\nthe header's default currency.")
    saft1_ClosingDebitBalance = fields.Float(
        currency_field="currency_id",
        choice='9',
        string="ClosingDebitBalance",
        xsd_type="SAFmonetaryType",
        help="Debit balance at the end date of the selection period in the"
        "\nheader's default currency.")
    saft1_ClosingCreditBalance = fields.Float(
        currency_field="currency_id",
        choice='9',
        string="ClosingCreditBalance",
        xsd_type="SAFmonetaryType",
        help="Credit balance at the end date of the selection period in the"
        "\nheader's default currency.")
    saft1_PartyInfo = fields.Many2one(
        "saft.1.partyinfostructure",
        string="Additional party information.")


class Supplier1(models.AbstractModel):
    """Contains the information of all suppliers, including the historical
    suppliers."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.supplier1'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SupplierType1'
    _concrete_rec_name = 'saft1_SupplierName'

    saft1_Supplier_Asset_id = fields.Many2one(
        "saft.1.asset")
    saft1_SupplierName = fields.Char(
        string="Name of the supplier of the asset",
        xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_SupplierID = fields.Char(
        string="Unique code for the supplier",
        xsd_type="SAFmiddle1textType")
    saft1_PostalAddress = fields.Many2one(
        "saft.1.addressstructure",
        string="Address information of the supplier of the asset",
        xsd_required=True)


class Supplier5(models.AbstractModel):
    "Information about the supplier of the asset"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.supplier5'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SupplierType5'
    _concrete_rec_name = 'saft1_SupplierName'

    saft1_SupplierName = fields.Char(
        string="Name of the supplier of the asset",
        xsd_required=True,
        xsd_type="SAFmiddle2textType")
    saft1_SupplierID = fields.Char(
        string="Unique code for the supplier",
        xsd_type="SAFmiddle1textType")
    saft1_PostalAddress = fields.Many2one(
        "saft.1.addressstructure",
        string="Address information of the supplier of the asset",
        xsd_required=True)


class Suppliers(models.AbstractModel):
    "The suppliers of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.suppliers'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'SuppliersType'
    _concrete_rec_name = 'saft1_Supplier'

    saft1_Supplier = fields.One2many(
        "saft.1.supplier",
        "saft1_Supplier_Suppliers_id",
        string="Supplier information.",
        xsd_required=True
    )


class TaxCodeDetails(models.AbstractModel):
    "Tax code details of the tax table entry."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxcodedetails'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxCodeDetailsType'
    _concrete_rec_name = 'saft1_TaxCode'

    saft1_TaxCodeDetails_TaxTableEntry_id = fields.Many2one(
        "saft.1.taxtableentry")
    saft1_choice10 = fields.Selection([
        ('saft1_TaxPercentage', 'TaxPercentage'),
        ('saft1_FlatTaxRate', 'FlatTaxRate')],
        "TaxPercentage/FlatTaxRate")
    saft1_TaxCode = fields.Char(
        string="Tax Code for lookup in tables.",
        xsd_required=True,
        xsd_type="SAFcodeType")
    saft1_EffectiveDate = fields.Date(
        string="Representing the starting date for this entry",
        xsd_type="date")
    saft1_ExpirationDate = fields.Date(
        string="Representing the ending date for this entry",
        xsd_type="date")
    saft1_Description = fields.Char(
        string="Description of the Tax Code.",
        xsd_type="SAFlongtextType")
    saft1_TaxPercentage = fields.Float(
        currency_field="currency_id",
        choice='10',
        string="Tax percentage.",
        xsd_type="decimal")
    saft1_FlatTaxRate = fields.Many2one(
        "saft.1.amountstructure",
        choice='10',
        string="Not in use.")
    saft1_Country = fields.Char(
        string="Two", xsd_required=True,
        xsd_type="ISOCountryCode",
        help="Two-letter country code according to ISO 3166-1 alpha 2"
        "\nstandard.")
    saft1_Region = fields.Char(
        string="Not in use. (Region)",
        xsd_type="SAFcodeType")
    saft1_StandardTaxCode = fields.Char(
        string="Standard Tax Code.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType")
    saft1_Compensation = fields.Boolean(
        string="Indicates if the Tax Code is used for compensation",
        xsd_type="boolean")
    saft1_BaseRate = fields.Float(
        currency_field="currency_id",
        string="Base rates used for the tax code",
        xsd_required=True,
        xsd_type="BaseRateType",
        help="Base rates used for the tax code. Standard is 100 (the whole"
        "\namount is tax deductible). Example: 60 if only 60% of"
        "\nthe total amount is tax deductible. Enter all"
        "\nstandard base rates used for the tax code.")


class TaxIDStructure(models.AbstractModel):
    "Tax information of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxidstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxIDStructure'
    _concrete_rec_name = 'saft1_TaxRegistrationNumber'

    saft1_TaxRegistration_CompanyHeaderStructure_id = fields.Many2one(
        "saft.1.companyheaderstructure")
    saft1_TaxRegistration_CompanyStructure_id = fields.Many2one(
        "saft.1.companystructure")
    saft1_TaxRegistrationNumber = fields.Char(
        string="The company’s VAT (MVA) number.",
        xsd_required=True,
        xsd_type="SAFmiddle1textType",
        help="The company’s VAT (MVA) number."
        "\nThis is the unique number/organization number from The Brønnøysund"
        "\nRegister Centre (Brønnøysundregistrene) followed by the"
        "\nletters “MVA”. This element is mandatory if the company is"
        "\nsubject to VAT (MVA).")
    saft1_TaxType = fields.Char(
        string="Not in use.",
        xsd_type="SAFcodeType")
    saft1_TaxNumber = fields.Char(
        string="Not in use. (TaxNumber)",
        xsd_type="SAFmiddle1textType")
    saft1_TaxAuthority = fields.Selection(
        TAXAUTHORITY_TAXIDSTRUCTURE,
        string="TaxAuthority",
        help="Identification of the Revenue Body to which this TaxType"
        "\nrefers."
        "\nThe only valid value is “Skatteetaten ”.")
    saft1_TaxVerificationDate = fields.Date(
        string="TaxVerificationDate",
        xsd_type="date",
        help="The date that the tax registration details referred to above"
        "\nwere last checked or when the tax registration was"
        "\ncompleted in the VAT register"
        "\n(Merverdiavgiftsregisteret).")


class TaxInformationStructure(models.AbstractModel):
    "Tax Amount information structure."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxinformationstructure'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxInformationStructure'
    _concrete_rec_name = 'saft1_TaxType'

    saft1_TaxInformationTotals_DocumentTotals_id = fields.Many2one(
        "saft.1.documenttotals")
    saft1_TaxInformationTotals_DocumentTotals10_id = fields.Many2one(
        "saft.1.documenttotals10")
    saft1_TaxInformation_Line_id = fields.Many2one(
        "saft.1.line")
    saft1_TaxInformation_Line3_id = fields.Many2one(
        "saft.1.line3")
    saft1_TaxInformation_Line4_id = fields.Many2one(
        "saft.1.line4")
    saft1_TaxInformation_Line7_id = fields.Many2one(
        "saft.1.line7")
    saft1_TaxType = fields.Selection(
        TAX_TAXINFORMATIONSTRUCTURE,
        string="Tax type for look-up in tables.",
        help="Tax type for look-up in tables."
        "\nIf used, then the only valid value is 'MVA'.")
    saft1_TaxCode = fields.Char(
        string="Tax Code for lookup in tables.",
        xsd_type="SAFcodeType")
    saft1_TaxPercentage = fields.Float(
        currency_field="currency_id",
        string="Tax percentage.",
        xsd_type="decimal")
    saft1_TaxBase = fields.Float(
        currency_field="currency_id",
        string="The base on which the tax is calculated",
        xsd_type="decimal",
        help="The base on which the tax is calculated. This can be an"
        "\namount, or a quantity, eg. Litres.")
    saft1_TaxBaseDescription = fields.Char(
        string="Description of the value in the TaxBase",
        xsd_type="SAFmiddle2textType",
        help="Description of the value in the TaxBase. Eg. Litres for"
        "\nexcises on alcoholic bevarages.")
    saft1_TaxAmount = fields.Many2one(
        "saft.1.amountstructure",
        string="Tax amount information",
        xsd_required=True)
    saft1_TaxExemptionReason = fields.Char(
        string="Tax exemption or reduction reason or rationale",
        xsd_type="SAFmiddle2textType")
    saft1_TaxDeclarationPeriod = fields.Char(
        string="TaxDeclarationPeriod",
        xsd_type="SAFmiddle1textType",
        help="The identification of the declaration/return in which the"
        "\ntaxamount is reported to the Revenue body.")


class TaxTableEntry(models.AbstractModel):
    "Tax entry information."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxtableentry'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxTableEntryType'
    _concrete_rec_name = 'saft1_TaxType'

    saft1_TaxTableEntry_TaxTable_id = fields.Many2one(
        "saft.1.taxtable")
    saft1_TaxType = fields.Selection(
        TAX_TAXTABLEENTRY,
        string="Tax type for look-up in tables",
        xsd_required=True,
        help="Tax type for look-up in tables. “MVA” is the only valid"
        "\nvalue.")
    saft1_Description = fields.Selection(
        DESCRIPTION_TAXTABLEENTRY,
        string="Description of the Tax Type",
        xsd_required=True,
        help="Description of the Tax Type. “Merverdiavgift” is the only"
        "\nvalid value.")
    saft1_TaxCodeDetails = fields.One2many(
        "saft.1.taxcodedetails",
        "saft1_TaxCodeDetails_TaxTableEntry_id",
        string="Tax code details of the tax table entry",
        xsd_required=True
    )


class TaxTable(models.AbstractModel):
    "The tax tables of a company."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxtable'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxTableType'
    _concrete_rec_name = 'saft1_TaxTableEntry'

    saft1_TaxTableEntry = fields.One2many(
        "saft.1.taxtableentry",
        "saft1_TaxTableEntry_TaxTable_id",
        string="Tax entry information.",
        xsd_required=True
    )


class Tax(models.AbstractModel):
    _description = 'tax'
    _name = 'saft.1.tax'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxType'
    _concrete_rec_name = 'saft1_TaxType'

    saft1_Tax_Product_id = fields.Many2one(
        "saft.1.product")
    saft1_TaxType = fields.Char(
        string="Tax Type for lookup in tables",
        xsd_type="SAFcodeType")
    saft1_TaxCode = fields.Char(
        string="Tax Code for lookup in tables",
        xsd_type="SAFcodeType")


class Taxonomies(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.taxonomies'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxonomiesType'
    _concrete_rec_name = 'saft1_Taxonomy'

    saft1_Taxonomy = fields.One2many(
        "saft.1.taxonomy",
        "saft1_Taxonomy_Taxonomies_id",
        string="Taxonomy", xsd_required=True
    )


class TaxonomyElement(models.AbstractModel):
    _description = 'taxonomyelement'
    _name = 'saft.1.taxonomyelement'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxonomyElementType'
    _concrete_rec_name = 'saft1_TaxonomyCode'

    saft1_TaxonomyElement_Taxonomy_id = fields.Many2one(
        "saft.1.taxonomy")
    saft1_TaxonomyCode = fields.Char(
        string="Reference to specific taxonomy element",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_TaxonomyClusterID = fields.Char(
        string="Additional reference to specific taxonomy element",
        xsd_type="SAFlongtextType")
    saft1_TaxonomyClusterContextID = fields.Char(
        string="TaxonomyClusterContextID",
        xsd_type="SAFlongtextType")
    saft1_AccountID = fields.Char(
        string="AccountID", xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="General Ledger Account code for this"
        "\nTaxanomyReference/TaxonomyCode. Can be including sub-"
        "\naccount id. It can contain many different levels to"
        "\nidentify the Account. It could include cost centres"
        "\nsuch as company, division, region, group and"
        "\nbranch/department.")


class Taxonomy(models.AbstractModel):
    _description = 'taxonomy'
    _name = 'saft.1.taxonomy'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TaxonomyType'
    _concrete_rec_name = 'saft1_TaxonomyReference'

    saft1_Taxonomy_Taxonomies_id = fields.Many2one(
        "saft.1.taxonomies")
    saft1_TaxonomyReference = fields.Char(
        string="Reference to the taxonomy that applies to the GL Account",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_TaxonomyElement = fields.One2many(
        "saft.1.taxonomyelement",
        "saft1_TaxonomyElement_Taxonomy_id",
        string="TaxonomyElement"
    )


class Transaction(models.AbstractModel):
    "Accounting transactions."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.transaction'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'TransactionType'
    _concrete_rec_name = 'saft1_TransactionID'

    saft1_Transaction_Journal_id = fields.Many2one(
        "saft.1.journal")
    saft1_TransactionID = fields.Char(
        string="The number/ID of the accounting document/voucher",
        xsd_required=True,
        xsd_type="SAFmiddle2textType",
        help="The number/ID of the accounting document/voucher.")
    saft1_Period = fields.Integer(
        string="Accounting Period.", xsd_required=True,
        xsd_type="nonNegativeInteger")
    saft1_PeriodYear = fields.Integer(
        string="The year of the Accounting Period",
        xsd_required=True,
        xsd_type="PeriodYearType",
        help="The year of the Accounting Period. Restriction: 1970-2100.")
    saft1_TransactionDate = fields.Date(
        string="The date of the accounting document/voucher",
        xsd_required=True,
        xsd_type="date")
    saft1_SourceID = fields.Char(
        string="SourceID",
        xsd_type="SAFmiddle1textType",
        help="Details of person or application that entered the"
        "\ntransaction.")
    saft1_TransactionType = fields.Char(
        string="Type of journaltransaction: normal",
        xsd_type="SAFshorttextType",
        help="Type of journaltransaction: normal, (automated) periodically,"
        "\netc.")
    saft1_Description = fields.Char(
        string="Description of Journal Transaction.",
        xsd_required=True,
        xsd_type="SAFlongtextType")
    saft1_BatchID = fields.Char(
        string="Systems generated ID for batch.",
        xsd_type="SAFmiddle1textType")
    saft1_SystemEntryDate = fields.Date(
        string="Date captured by system",
        xsd_required=True,
        xsd_type="date",
        help="Date captured by system. The date when the transaction was"
        "\nentered into the system - manual entry, imported"
        "\ntransaction, etc. If this date is not available in"
        "\nyour system, use the TransactionDate.")
    saft1_GLPostingDate = fields.Date(
        string="Date posting to the general ledger account",
        xsd_required=True,
        xsd_type="date",
        help="Date posting to the general ledger account. The date when the"
        "\ntransaction was updated to the database. If this date"
        "\nis not available in your system, use the"
        "\nTransactionDate.")
    saft1_CustomerID = fields.Char(
        string="Not in use.",
        xsd_type="SAFmiddle1textType")
    saft1_SupplierID = fields.Char(
        string="Not in use. (SupplierID)",
        xsd_type="SAFmiddle1textType")
    saft1_SystemID = fields.Char(
        string="SystemID",
        xsd_type="SAFshorttextType",
        help="Unique ID/number created by the system for the accounting"
        "\ndocument/voucher.")
    saft1_Line = fields.One2many(
        "saft.1.line",
        "saft1_Line_Transaction_id",
        string="Transaction lines.", xsd_required=True
    )


class UOMTableEntry(models.AbstractModel):
    _description = 'uomtableentry'
    _name = 'saft.1.uomtableentry'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'UOMTableEntryType'
    _concrete_rec_name = 'saft1_UnitOfMeasure'

    saft1_UOMTableEntry_UOMTable_id = fields.Many2one(
        "saft.1.uomtable")
    saft1_UnitOfMeasure = fields.Char(
        string="Quantity unit of measure e.g",
        xsd_required=True,
        xsd_type="SAFcodeType",
        help="Quantity unit of measure e.g. pack of 12")
    saft1_Description = fields.Char(
        string="Description of the UOM",
        xsd_required=True,
        xsd_type="SAFlongtextType")


class UOMTable(models.AbstractModel):
    "Not in use."
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.uomtable'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'UOMTableType'
    _concrete_rec_name = 'saft1_UOMTableEntry'

    saft1_UOMTableEntry = fields.One2many(
        "saft.1.uomtableentry",
        "saft1_UOMTableEntry_UOMTable_id",
        string="UOMTableEntry",
        xsd_required=True
    )


class Valuation(models.AbstractModel):
    _description = 'valuation'
    _name = 'saft.1.valuation'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ValuationType'
    _concrete_rec_name = 'saft1_AssetValuationType'

    saft1_Valuation_Valuations_id = fields.Many2one(
        "saft.1.valuations")
    saft1_choice11 = fields.Selection([
        ('saft1_AssetLifeYear', 'AssetLifeYear'),
        ('saft1_AssetLifeMonth', 'AssetLifeMonth')],
        "AssetLifeYear/AssetLifeMonth")
    saft1_AssetValuationType = fields.Char(
        string="Describes the purpose for the reporting: f",
        xsd_type="SAFshorttextType",
        help="Describes the purpose for the reporting: f.i. commercial, tax"
        "\nin country 1, tax in country 2, etc.")
    saft1_ValuationClass = fields.Char(
        string="This describes the classification of the asset for",
        xsd_type="SAFshorttextType",
        help="This describes the classification of the asset for (tax)"
        "\nreporting purposes.")
    saft1_AcquisitionAndProductionCostsBegin = fields.Float(
        currency_field="currency_id",
        string="AcquisitionAndProductionCostsBegin",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Total costs of acquisition and/or production of the asset at"
        "\nSelectionStartDate in the header's default currency.")
    saft1_AcquisitionAndProductionCostsEnd = fields.Float(
        currency_field="currency_id",
        string="AcquisitionAndProductionCostsEnd",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Total costs of acquisition and/or production of the asset at"
        "\nSelectionEndDate in the header's default currency.")
    saft1_InvestmentSupport = fields.Float(
        currency_field="currency_id",
        string="InvestmentSupport",
        xsd_type="SAFmonetaryType",
        help="Total amount of investment support for this asset in the"
        "\nheader's default currency.")
    saft1_AssetLifeYear = fields.Float(
        currency_field="currency_id",
        choice='11',
        string="Periode of useful life in years",
        xsd_required=True,
        xsd_type="decimal")
    saft1_AssetLifeMonth = fields.Float(
        currency_field="currency_id",
        choice='11',
        string="Period of useful life in months",
        xsd_required=True,
        xsd_type="decimal")
    saft1_AssetAddition = fields.Float(
        currency_field="currency_id",
        string="AssetAddition",
        xsd_type="SAFmonetaryType",
        help="Bookvalue of the acquisition and/or production of the asset"
        "\nin the Selectionperiod in the header's default"
        "\ncurrency.")
    saft1_Transfers = fields.Float(
        currency_field="currency_id",
        string="Transfers",
        xsd_type="SAFmonetaryType",
        help="Book value of the transfers of the asset during the"
        "\nSelectionperiod in the header's default currency.")
    saft1_AssetDisposal = fields.Float(
        currency_field="currency_id",
        string="AssetDisposal",
        xsd_type="SAFmonetaryType",
        help="Book value of the disposals of the asset during the"
        "\nSelectionperiod in the header's default currency.")
    saft1_BookValueBegin = fields.Float(
        currency_field="currency_id",
        string="BookValueBegin",
        xsd_type="SAFmonetaryType",
        help="Bookvalue at the beginning of the Selectionperiod in the"
        "\nheader's default currency.")
    saft1_DepreciationMethod = fields.Char(
        string="Method of normal depreciation during the Selectionperiod",
        xsd_type="SAFmiddle1textType")
    saft1_DepreciationPercentage = fields.Float(
        currency_field="currency_id",
        string="The rate of the normal depreciation per year or month",
        xsd_type="decimal",
        help="The rate of the normal depreciation per year or month"
        "\n(depends on choice useful life periode)")
    saft1_DepreciationForPeriod = fields.Float(
        currency_field="currency_id",
        string="DepreciationForPeriod",
        xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Total amouunt of normal depreciation during the"
        "\nSelectionperiod in the header's default currency.")
    saft1_AppreciationForPeriod = fields.Float(
        currency_field="currency_id",
        string="AppreciationForPeriod",
        xsd_type="SAFmonetaryType",
        help="Total amouunt of appreciation during the Selectionperiod in"
        "\nthe header's default currency.")
    saft1_ExtraordinaryDepreciationsForPeriod = fields.Many2one(
        "saft.1.extraordinarydepreciationsforperiod",
        string="ExtraordinaryDepreciationsForPeriod",
        help="Extraordinary depreciations for this asset during the"
        "\nSelectionperiod.")
    saft1_AccumulatedDepreciation = fields.Float(
        currency_field="currency_id",
        string="Total amount of depreciation for this asset",
        xsd_type="SAFmonetaryType")
    saft1_BookValueEnd = fields.Float(
        currency_field="currency_id",
        string="BookValueEnd", xsd_required=True,
        xsd_type="SAFmonetaryType",
        help="Bookvalue at the end of the Selectionperiod in the header's"
        "\ndefault currency.")


class Valuations(models.AbstractModel):
    """The data can be reported for different purposes. More than one can be in
    this SAF."""
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = 'saft.1.valuations'
    _inherit = 'spec.mixin.saft'
    _generateds_type = 'ValuationsType'
    _concrete_rec_name = 'saft1_Valuation'

    saft1_Valuation = fields.One2many(
        "saft.1.valuation",
        "saft1_Valuation_Valuations_id",
        string="Valuation", xsd_required=True
    )
