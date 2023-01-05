from odoo import fields, models


class PayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    json = fields.Serialized()
    l10n_no_AgapliktUtenLoennsopplysningsplikt = fields.Integer(
        "Aga-plikt uten lønnsopplysningsplikt", sparse="json"
    )
