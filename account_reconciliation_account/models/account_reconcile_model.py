from odoo import api, fields, models


class ReconcileModel(models.Model):
    _inherit = "account.reconcile.model"

    match_counterpart_account_id = fields.Many2one(
        "account.account", string="Counterpart Account"
    )

    @api.onchange("match_counterpart_account_id")
    def set_counterpart_line(self):
        line = {
            "account_id": self.match_counterpart_account_id.id,
            "amount_type": "percentage",
            "amount_string": "100",
        }
        self.write({"line_ids": [(5, 0, 0), (0, 0, line)]})

    def _is_applicable_for(self, st_line, partner):
        if (
            self.match_counterpart_account_id
            and st_line.counterpart_account_id != self.match_counterpart_account_id
        ):
            return False
        else:
            return super()._is_applicable_for(st_line, partner)

    # I tried to reconcile on counterpart_account_id without any reconciliation model.
    # But javascript requires a reconciliation model per account,
    # looping through model account-lines.
    # https://github.com/OCA/account-reconcile/blob/14.0/account_reconciliation_widget/static/src/js/reconciliation/reconciliation_model.js#L680
    # THIS MIGHT (NOT?) BE USEFUL TOGETHER WITH NEW JAVASCRIPT CODE WHICH DOESN'T DEPEND ON RECONCILIATION MODEL.
    # def _get_write_off_move_lines_dict(self, st_line, residual_balance):
    #     lines_vals_list = super()._get_write_off_move_lines_dict(
    #         st_line, residual_balance
    #     )
    #     if not lines_vals_list and st_line.counterpart_account_id and self.match_counterpart_account_id:
    #         balance = -st_line.amount
    #         lines_vals_list = [
    #             {
    #                 'name': st_line.payment_ref,
    #                 'balance': balance,
    #                 'debit': balance > 0 and balance or 0,
    #                 'credit': balance < 0 and -balance or 0,
    #                 'account_id': st_line.counterpart_account_id.id,
    #                 'currency_id': False,
    #                 'analytic_account_id': False,
    #                 'analytic_tag_ids': [(6, 0, [])],
    #                 'reconcile_model_id': self.id,
    #                 'journal_id': False,
    #                 'tax_ids': [],
    #             }
    #         ]
    #     return lines_vals_list
