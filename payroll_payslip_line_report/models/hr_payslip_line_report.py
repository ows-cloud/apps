from odoo import fields, models, tools


class HrPayslipLineReport(models.Model):
    _name = "hr.payslip.line.report"
    _description = "hr.payslip.line.report"
    _auto = False

    # date_from is very useful for pivoting. Shold be added to payroll.
    date_from = fields.Date("Date From")
    payslip_run_id = fields.Many2one("hr.payslip.run", string="Payslip Batch")
    credit_note = fields.Boolean("Credit Note")

    def init(self):
        tools.drop_view_if_exists(self._cr, "hr_payslip_line_report")
        self._cr.execute(
            """
            CREATE OR REPLACE VIEW hr_payslip_line_report AS
             SELECT
                l.id,
                l.create_date,
                l.create_uid,
                l.write_date,
                l.write_uid,

                l.name,
                l.payslip_id,
                p.credit_note
                p.date_from
                p.payslip_run_id,
                    <field name="category_id" />
                    <field name="employee_id" />
                    <field name="sequence" />
                    <field name="name" />
                    <field name="code" />
                    <field name="quantity" />
                    <field name="rate" />
                    <field name="amount" />
                    <field name="total" sum="Total" />
                    <field name="amount_select" invisible="1" />
                    <field name="register_id" invisible="1" />
                    <field name="date_from" />
                    <field name="credit_note" />

               FROM hr_payslip_line l
                LEFT JOIN hr_payslip p ON l.payslip_id = p.id
                LEFT JOIN hr_payslip_run r ON p.payslip_run_id = r.id
            """
        )
