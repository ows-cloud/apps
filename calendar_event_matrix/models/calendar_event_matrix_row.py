from odoo import _, api, fields, models


class CalendarEventMatrixRow(models.Model):
    _name = "calendar.event.matrix.row"
    _description = "Calendar Event Matrix Row"

    name = fields.Char()
    matrix_id = fields.Many2one('calendar.event.matrix', string="Group")
    allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")
    sequence = fields.Integer()
