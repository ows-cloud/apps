from odoo import fields, models
from odoo.release import major_version  # 14.0


class IrModuleMigrationInfo(models.Model):
    _inherit = "ir.module.migration.info"

    module_id = fields.Many2one("Module")
    module_name = fields.Char("Module Name")
    mig_version = fields.Char("Version")

    mig_title = fields.Char("Title")
    mig_url = fields.Char("URL")
    mig_state = fields.Selection(
        [("open", "Open"), ("merged", "Merged")], string="State"
    )
    mig_opened = fields.Date("Opened")
    mig_merged = fields.Date("Merged")
    mig_no_of_reviewers = fields.Integer("No of reviewers")
    mig_no_of_comments = fields.Integer("No of comments")
