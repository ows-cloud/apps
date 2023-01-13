import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    @api.model
    def get_param(self, key, default=False):
        if key == "web.base.url":
            website = self.env.company.website_id
            if website and website.domain:
                return "http://" + str(self.env.company.website_id.domain)

        return super(IrConfigParameter, self).get_param(key, default)


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def _replace_local_links(self, html, base_url=None):
        if not base_url:
            website = self.env.company.website_id
            if website and website.domain:
                base_url = "http://" + str(self.env.company.website_id.domain)

        return super(MailThread, self)._replace_local_links(html, base_url)


class Company(models.Model):
    _inherit = "res.company"

    website_id = fields.Many2one("website", string="Default Website")


class Partner(models.Model):
    _inherit = "res.partner"

    def get_base_url(self):
        """Get the base URL for the current partner."""
        self.ensure_one()
        website = self.env.company.website_id
        if website and website.domain:
            if "localhost:" in website.domain:
                return "http://" + website.domain
            else:
                return "https://" + website.domain

        return self.env["ir.config_parameter"].sudo().get_param("web.base.url")


class Website(models.Model):
    _inherit = "website"

    def _default_social_facebook(self):
        return self.env.company.social_facebook

    def _default_social_github(self):
        return self.env.company.social_github

    def _default_social_linkedin(self):
        return self.env.company.social_linkedin

    def _default_social_youtube(self):
        return self.env.company.social_youtube

    def _default_social_instagram(self):
        return self.env.company.social_instagram

    def _default_social_twitter(self):
        return self.env.company.social_twitter

    social_twitter = fields.Char("Twitter Account", default=_default_social_twitter)
    social_facebook = fields.Char("Facebook Account", default=_default_social_facebook)
    social_github = fields.Char("GitHub Account", default=_default_social_github)
    social_linkedin = fields.Char("LinkedIn Account", default=_default_social_linkedin)
    social_youtube = fields.Char("Youtube Account", default=_default_social_youtube)
    social_instagram = fields.Char(
        "Instagram Account", default=_default_social_instagram
    )
