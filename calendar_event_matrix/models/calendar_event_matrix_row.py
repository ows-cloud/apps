from odoo import _, api, fields, models


class CalendarEventMatrixRow(models.Model):
    _name = "calendar.event.matrix.row"
    _description = "Calendar Event Matrix Row"
    _order = "sequence"

    sequence = fields.Integer()
    name = fields.Char()
    matrix_id = fields.Many2one('calendar.event.matrix', string="Group")
    allday = fields.Boolean(help="If True, don't use default_start & default_stop")
    default_start = fields.Datetime("Default Start Time", help="Any date; only the time is relevant.")
    default_stop = fields.Datetime("Default Stop Time", help="Any date; only the time is relevant.")
    allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")
