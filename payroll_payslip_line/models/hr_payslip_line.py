from odoo import fields, models


class HrPayslipLine(models.Model):
    _inherit = "hr.payslip.line"

    # date_from is very useful for pivoting. Shold be added to payroll.
    date_from = fields.Date("Date From", related="slip_id.date_from", store=True)
    payslip_run_id = fields.Many2one(
        "hr.payslip.run", related="slip_id.payslip_run_id", string="Payslip Batch"
    )
    credit_note = fields.Boolean(
        string="Credit Note",
        related="slip_id.credit_note",
    )
    net_quantity = fields.Float(
        string="Net Quantity",
        help="Quantity - opposite sign if credit note",
        digits="Payroll",
        default=1.0,
        compute="_compute_net",
        store=True,
    )
    net_rate = fields.Float(
        string="Net Rate (%)",
        help="Rate - opposite sign if credit note",
        digits="Payroll Rate",
        default=100.0,
        compute="_compute_net",
        store=True,
    )
    net_amount = fields.Float(
        string="Net Amount",
        help="Amount - opposite sign if credit note",
        digits="Payroll",
        compute="_compute_net",
        store=True,
    )
    net_total = fields.Float(
        string="Net Total",
        help="Total - opposite sign if credit note",
        digits="Payroll",
        compute="_compute_net",
        store=True,
    )

    def _compute_net(self):
        factor = -1 if self.credit_note else 1
        self.net_quantity = self.quantity * factor
        self.net_rate = self.rate * factor
        self.net_amount = self.amount * factor
        self.net_total = self.total * factor
