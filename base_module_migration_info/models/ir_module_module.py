from odoo import api, fields, models, _
from odoo.release import major_version # 14.0
from odoo.exceptions import UserError


class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    mig_info_ids = fields.One2many("ir.module.migration.info", "module_id", string="Migration Info")
    # In 14.0 database, the fields below should show the migration info of 15.0
    mig_title = fields.Char("Title")
    mig_url = fields.Char("URL")
    mig_state = fields.Selection([("open", "Open"), ("merged", "Merged")], string="State")
    mig_opened = fields.Date("Opened")
    mig_merged = fields.Date("Merged")
    mig_no_of_reviewers = fields.Integer("No of reviewers")
    mig_no_of_comments = fields.Integer("No of comments")
