from odoo import _, api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    categ_id = fields.Many2one('calendar.event.type', string="Main tag", compute='_get_categ_id') #, inverse='_set_categ_id')
    start_date_str = fields.Char('Start Date (text)', compute='_get_start_date_str')

    def _get_categ_id(self):
        for record in self:
            record.categ_id = record.categ_ids[0]

    def _set_categ_id(self):
        for record in self:
            record.categ_ids = [(4, record.categ_id.id)]

    def _get_start_date_str(self):
        for record in self:
            record.start_date_str = str(record.start_date)
