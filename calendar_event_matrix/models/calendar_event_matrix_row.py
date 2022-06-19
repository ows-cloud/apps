from odoo import _, api, fields, models


class CalendarEventMatrixRow(models.Model):
    _name = "calendar.event.matrix.row"
    _description = "Calendar Event Matrix Row"

    sequence = fields.Integer()
    name = fields.Char()
    matrix_id = fields.Many2one('calendar.event.matrix', string="Group")
    default_start = fields.Datetime("Default Start Time", help="Any date; only the time is relevant.")
    default_stop = fields.Datetime("Default Stop Time", help="Any date; only the time is relevant.")
    allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")
