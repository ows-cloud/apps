from odoo import api, exceptions, fields, models

import logging
_logger = logging.getLogger(__name__)

class Company(models.Model):
    _inherit = 'res.company'

    website_id = fields.Many2one('website', string="Default Website")


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_param(self, key, default=False):
        if key == 'web.base.url' and self.env.user.company_id.website_id:
            return 'http://' + str(self.env.user.company_id.website_id.domain)
        else:
            return super(IrConfigParameter, self).get_param(key, default)
