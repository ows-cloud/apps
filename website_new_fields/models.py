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
            prefix = self.get_param('web.base.url.prefix') or 'http://'
            suffix = self.get_param('web.base.url.suffix') or ''
            return prefix + str(self.env.user.company_id.website_id.domain) + suffix
        else:
            return super(IrConfigParameter, self).get_param(key, default)

class Website(models.Model):
    _inherit = 'website'

    def read(self, fields=None, load='_classic_read'):
        dicts = super(Website, self).read(fields, load)
        for d in dicts:
            if d.get('domain'):
                d['domain'] += self.env['ir.config_parameter'].get_param('web.base.url.suffix') or ''
        return dicts