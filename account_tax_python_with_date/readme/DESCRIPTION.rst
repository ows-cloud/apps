This module patch adds tax_date variable to python_compute field in account.tax.

IMPORTANT: tax_date = None if the use case is not implemented.

WHY tax_date?
Because the tax rate may depend on the date.

When the government changes a VAT rate from a specific date, without this module you have two bad alternatives:

Option a) Finish all account.move with an old date & old rate. Then change the VAT rate, and register all new account.move with a new date & new rate. CHALLENGE: When you receive an old supplier invoice late, you cannot use the old VAT rate anymore.

Option b) Create a new VAT. On account.move with old date, use old VAT. On account.move with new date, use new VAT. CHALLENGE: On the transition date for the new VAT rate, you need to update all products etc. replacing the old VAT with the new VAT.
