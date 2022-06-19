from odoo import _, api, fields, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    matrix_row_id = fields.Many2one('calendar.event.matrix.row', string="Matrix Row")
    matrix_partner_attending = fields.Boolean(
        "Matrix Partner Attending",
        compute="_get_matrix_partner_attending",
        inverse="_set_matrix_partner_attending",
    )

    def _get_matrix_partner_attending(self):
        #partner_id = self.env.context.get("matrix_partner_id")
        #partner_id.ensure_one()
        for record in self:
            partner_id = record.matrix_row_id.matrix_id.matrix_partner_id
            if partner_id in record.partner_ids:
                record.matrix_partner_attending = True
            else:
                record.matrix_partner_attending = False

    def _set_matrix_partner_attending(self):
        #partner_id = self.env.context.get("matrix_partner_id")
        #partner_id.ensure_one()
        for record in self:
            partner_id = record.matrix_row_id.matrix_id.matrix_partner_id
            if record.matrix_partner_attending:
                record.write({"partner_ids": [(4, partner_id.id, 0)]})
            else:
                record.write({"partner_ids": [(3, partner_id.id, 0)]})

    partner_count = fields.Integer("No of attendees", compute='_get_partner_count')

    def _get_partner_count(self):
        for record in self:
            record.partner_count = len(record.partner_ids)

    start_date_str = fields.Char('Start Date (text)', compute='_get_start_date_str')

    def _get_start_date_str(self):
        for record in self:
            if record.start:
                record.start_date_str = str(record.start.date())
            else:
                record.start_date_str = str(record.start_date)
