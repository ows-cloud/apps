from odoo import api, fields, models, _
from odoo.release import major_version # 14.0
from odoo.exceptions import UserError


class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    mig_url = fields.Char("URL")
    mig_state = fields.Selection([("open", "Open"), ("merged", "Merged")], string="State")
    mig_opened = fields.Date("Opened")
    mig_merged = fields.Date("Merged")
    mig_last_commented = fields.Date("Last Commented")
