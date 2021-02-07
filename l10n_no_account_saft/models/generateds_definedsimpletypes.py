
# -*- coding: utf-8 -*-


class TypeDescriptor(object):
    def __init__(self, name, type_name=None, descr=None):
        self.name_ = name
        self.type_name_ = type_name
        self.type_obj_ = None
        self.descr_ = descr
    def __str__(self):
        return '<%s -- name: %s type: %s>' % (self.__class__.__name__,
            self.name, self.type_name,)
    def get_name_(self):
        return self.name_
    def set_name_(self, name):
        self.name_ = name
    name = property(get_name_, set_name_)
    def get_descr_(self):
        return self.descr_
    def get_type_name_(self):
        return self.type_name_
    def set_type_name_(self, type_name):
        self.type_name_ = type_name
    type_name = property(get_type_name_, set_type_name_)
    def get_type_obj_(self):
        return self.type_obj_
    def set_type_obj_(self, type_obj):
        self.type_obj_ = type_obj
    type_obj = property(get_type_obj_, set_type_obj_)

class ComplexTypeDescriptor(TypeDescriptor):
    def __init__(self, name):
        super(ComplexTypeDescriptor, self).__init__(name)
        self.elements_ = []
        self.attributes_ = {}
    def get_elements_(self):
        return self.elements_
    def set_elements_(self, elements):
        self.elements_ = elements
    elements = property(get_elements_, set_elements_)
    def get_attributes_(self):
        return self.attributes_
    def set_attributes_(self, attributes):
        self.attributes_ = attributes
    attributes = property(get_attributes_, set_attributes_)

class SimpleTypeDescriptor(TypeDescriptor):
    def __init__(self, name, type_name, enum=None, descr=None):
        self.enumeration_ = enum
        super(SimpleTypeDescriptor, self).__init__(name, type_name, descr)

    def get_enumeration_(self):
        return self.enumeration_
Defined_simple_type_table = {
    'SAFshorttextType': SimpleTypeDescriptor('SAFshorttextType', 'string'),
    'AccountTypeType': SimpleTypeDescriptor('AccountTypeType', 'SAFshorttextType',
        [('GL', 'GL')],
        """Type of account. Set standard account in the StandardAccountID element. The only valid value is “GL” (General Ledger)."""),
    'AddressTypeType': SimpleTypeDescriptor('AddressTypeType', 'string',
        [('StreetAddress', 'StreetAddress'), ('PostalAddress', 'PostalAddress'), ('BillingAddress', 'BillingAddress'), ('ShipToAddress', 'ShipToAddress'), ('ShipFromAddress', 'ShipFromAddress')],
        """Field to differentiate between multiple addresses and to indicate the type of address. 
Choose from the predefined enumerations
StreetAddress, PostalAddress, BillingAddress, ShipToAddress, ShipFromAddress."""),
    'BaseRateType': SimpleTypeDescriptor('BaseRateType', 'decimal'),
    'CashDiscountRateType': SimpleTypeDescriptor('CashDiscountRateType', 'decimal'),
    'SAFcodeType': SimpleTypeDescriptor('SAFcodeType', 'string'),
    'DebitCreditIndicatorType': SimpleTypeDescriptor('DebitCreditIndicatorType', 'SAFcodeType',
        [('D', 'D'), ('C', 'C')],
        """Indicates whether the amounts on line-level are debit or credit amounts. Entry must correspond to entry reflected in General Ledger Entry. Signing of lineamounts is relative to this indicator. E.g. a return can lead to a negative amount."""),
    'DebitCreditIndicatorType8': SimpleTypeDescriptor('DebitCreditIndicatorType8', 'SAFcodeType',
        [('D', 'D'), ('C', 'C')],
        """Indicates whether the amounts on line-level are debit or credit amounts. Entry must correspond to entry reflected in General Ledger Entry. Signing of lineamounts is relative to this indicator. E.g. a return can lead to a negative amount."""),
    'SAFlongtextType': SimpleTypeDescriptor('SAFlongtextType', 'string'),
    'DescriptionType': SimpleTypeDescriptor('DescriptionType', 'SAFlongtextType',
        [('Merverdiavgift', 'Merverdiavgift')],
        """Description of the Tax Type. “Merverdiavgift” is the only valid value."""),
    'ISOCountryCode': SimpleTypeDescriptor('ISOCountryCode', 'string'),
    'ISOCurrencyCode': SimpleTypeDescriptor('ISOCurrencyCode', 'string'),
    'PeriodEndYearType': SimpleTypeDescriptor('PeriodEndYearType', 'nonNegativeInteger'),
    'PeriodStartYearType': SimpleTypeDescriptor('PeriodStartYearType', 'nonNegativeInteger'),
    'PeriodYearType': SimpleTypeDescriptor('PeriodYearType', 'nonNegativeInteger'),
    'PeriodYearType2': SimpleTypeDescriptor('PeriodYearType2', 'nonNegativeInteger'),
    'PeriodYearType6': SimpleTypeDescriptor('PeriodYearType6', 'nonNegativeInteger'),
    'SAFexchangerateType': SimpleTypeDescriptor('SAFexchangerateType', 'decimal'),
    'SAFmiddle1textType': SimpleTypeDescriptor('SAFmiddle1textType', 'string'),
    'SAFmiddle2textType': SimpleTypeDescriptor('SAFmiddle2textType', 'string'),
    'SAFmonetaryType': SimpleTypeDescriptor('SAFmonetaryType', 'decimal'),
    'SAFquantityType': SimpleTypeDescriptor('SAFquantityType', 'decimal'),
    'SAFweightType': SimpleTypeDescriptor('SAFweightType', 'decimal'),
    'StatusType': SimpleTypeDescriptor('StatusType', 'SAFmiddle1textType',
        [('Active', 'Active'), ('Closed', 'Closed'), ('Observation', 'Observation'), ('Passive', 'Passive')],
        """Status of the analysis entry. Choose from the predefined enumerations
Active, Closed, Observation, Passive."""),
    'StatusType11': SimpleTypeDescriptor('StatusType11', 'SAFmiddle1textType',
        [('Active', 'Active'), ('Observation', 'Observation'), ('Passive', 'Passive')],
        """Type of account.
Enumerated
Active, Observation, Passive."""),
    'TaxAccountingBasisType': SimpleTypeDescriptor('TaxAccountingBasisType', 'SAFshorttextType',
        [('A', 'A')],
        """Type of data in the audit file. The only valid value is “A” (Accounting)."""),
    'TaxAuthorityType': SimpleTypeDescriptor('TaxAuthorityType', 'SAFmiddle1textType',
        [('Skatteetaten', 'Skatteetaten')],
        """Identification of the Revenue Body to which this TaxType refers.
The only valid value is “Skatteetaten ”."""),
    'TaxTypeType': SimpleTypeDescriptor('TaxTypeType', 'SAFcodeType',
        [('MVA', 'MVA')],
        """Tax type for look-up in tables. “MVA” is the only valid value."""),
    'TaxTypeType12': SimpleTypeDescriptor('TaxTypeType12', 'SAFcodeType',
        [('MVA', 'MVA')],
        """Tax type for look-up in tables.
If used, then the only valid value is "MVA"."""),
    'TypeType': SimpleTypeDescriptor('TypeType', 'SAFmiddle1textType',
        [('Private', 'Private'), ('Company', 'Company'), ('Government', 'Government')],
        """Type of party.
Enumerated
Private, Company, Government"""),
}

