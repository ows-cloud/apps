This module provides post-import-hooks that may run after importing a bank statement.
It depends on excel_import_hook and excel_import_export from
https://github.com/OCA/server-tools

Available hooks
---------------

**set_partner**: Set `partner_name` and `partner_id` if empty,
with values from `import_first_name` and `import_last_name`.

**set_text**: Add `import_message` to `payment_ref`.

**time_parameter**: Do for each time parameter for `account.move`:

* Look for the parameter key (code or name) `payment_ref`,
  and replace with the parameter value.
* If the parameter value is an account:

  - Set `counterpart_account_id` on the statement line.
  - If no reconciliation model exists for the account, create it.
