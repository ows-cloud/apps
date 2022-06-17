from odoo import _, api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    matrix_row_id = fields.Many2one('calendar.event.matrix.row', string="Matrix Row")
    partner_count = fields.Integer("No of attendees", compute='_get_partner_count')
    start_date_str = fields.Char('Start Date (text)', compute='_get_start_date_str')

    def _get_partner_count(self):
        for record in self:
            record.partner_count = len(record.partner_ids)

    def _get_start_date_str(self):
        for record in self:
            if record.start:
                record.start_date_str = str(record.start.date())
            else:
                record.start_date_str = str(record.start_date)
