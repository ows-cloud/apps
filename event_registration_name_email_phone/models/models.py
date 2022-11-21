from odoo import fields, models


class Event(models.Model):
    _inherit = "event.event"

    require_email = fields.Boolean("Require email", default=True)
    require_phone = fields.Boolean("Require phone")
