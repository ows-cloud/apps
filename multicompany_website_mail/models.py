from odoo import api, exceptions, fields, models

import logging
_logger = logging.getLogger(__name__)


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_param(self, key, default=False):
        if key == 'web.base.url':
            website = self.env.company.website_id
            if website and website.domain:
                return 'http://' + str(self.env.company.website_id.domain)

        return super(IrConfigParameter, self).get_param(key, default)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _replace_local_links(self, html, base_url=None):
        if not base_url:
            website = self.env.company.website_id
            if website and website.domain:
                base_url = 'http://' + str(
                    self.env.company.website_id.domain)

        return super(MailThread, self)._replace_local_links(html, base_url)


class Company(models.Model):
    _inherit = 'res.company'

    website_id = fields.Many2one('website', string="Default Website")


class Partner(models.Model):
    _inherit = 'res.partner'

    def get_base_url(self):
        """Get the base URL for the current partner."""
        self.ensure_one()
        website = self.company_id.website_id
        if website and website.domain:
            if 'localhost:' in website.domain:
                return 'http://' + self.company_id.website_id.domain
            else:
                return 'https://' + self.company_id.website_id.domain

        return self.env['ir.config_parameter'].sudo().get_param('web.base.url')