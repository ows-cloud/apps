Reconcile on `account_id` without any reconciliation model.
This would be **less flexible**, forcing `account_id` if it exists.
And currently, looping through the statement lines,
Javascript requires a reconciliation model per account.
https://github.com/OCA/account-reconcile/blob/14.0/account_reconciliation_widget/static/src/js/reconciliation/reconciliation_model.js#L680

Implementation draft

.. code-block:: python

    # THIS MIGHT (NOT?) BE USEFUL TOGETHER WITH
    #   NEW JAVASCRIPT CODE WHICH DOESN'T DEPEND ON RECONCILIATION MODEL.
    _inherit = "account.reconcile.model"

    def _get_write_off_move_lines_dict(self, st_line, residual_balance):
        lines_vals_list = super()._get_write_off_move_lines_dict(
            st_line, residual_balance
        )
        if not lines_vals_list and st_line.account_id and \
          self.match_account_id:
            balance = -st_line.amount
            lines_vals_list = [
                {
                    'name': st_line.payment_ref,
                    'balance': balance,
                    'debit': balance > 0 and balance or 0,
                    'credit': balance < 0 and -balance or 0,
                    'account_id': st_line.account_id.id,
                    'currency_id': False,
                    'analytic_account_id': False,
                    'analytic_tag_ids': [(6, 0, [])],
                    'reconcile_model_id': self.id,
                    'journal_id': False,
                    'tax_ids': [],
                }
            ]
        return lines_vals_list
