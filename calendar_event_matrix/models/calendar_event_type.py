from odoo import _, api, fields, models


class CalendarEventType(models.Model):
    _inherit = 'calendar.event.type'

    group_id = fields.Many2one('calendar.event.type.group', string="Group")
    allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")
