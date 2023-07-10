from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    group_show_line_subtotals = fields.Selection(
        string="Line Subtotals",
        selection=[
            ("tax_excluded", "Show line subtotals without taxes (B2B)"),
            ("tax_included", "Show line subtotals with taxes (B2C)"),
        ],
        default="tax_excluded",
    )

    def write(self, values):
        super(Company, self).write(values)
        if values.get("group_show_line_subtotals"):
            Conf = self.env["multicompany.config"]
            for company in self:
                Conf = Conf._prepare(company)
                Conf._group_show_line_subtotals()
