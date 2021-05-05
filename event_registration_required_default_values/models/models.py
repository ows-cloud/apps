from odoo import models, fields, api, exceptions


class Event(models.Model):
    _inherit = 'event.event'

    require_email = fields.Boolean("Require email", default=True)
    require_phone = fields.Boolean("Require phone")


class Company(models.Model):
    _inherit = 'res.company'

    event_registration_default_values = fields.Boolean("Prefill attendees")
