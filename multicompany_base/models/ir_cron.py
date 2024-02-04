from odoo import fields, models
from ..tools import _prepare

class IrCron(models.Model):
    _inherit = "ir.cron"

    def method_direct_trigger(self):
        self.check_access_rights('write')
        companies = self.env["res.company"].sudo().bypass_company_rules().search([])

        for cron in self:
            for company in companies:
                cron_limited = _prepare(cron, company)
                cron_limited.with_context(lastcall=cron.lastcall).ir_actions_server_id.run()
            cron.lastcall = fields.Datetime.now()
        return True
