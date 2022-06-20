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
    # Not implemented
    # default_all_matrix_partners = fields.Boolean("Add all participants")
    # allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")

    # def create(self, values):
    #     if "default_all_matrix_partners" in values:
    #         self._update_default_all_matrix_partners(self, values["default_all_matrix_partners"])
    #     super().create(values)

    # # def write(self, values):
    # #     if "default_all_matrix_partners" in values:
    # #         self._update_default_all_matrix_partner(self, values["default_all_matrix_partners"])
    # #     super().write(values)

    # def _update_default_all_matrix_partners(self):
    #     self.ensure_one()
    #     if self.default_all_matrix_partners:
    #         # search for calendar.event with this row
    #         # for each calendar.event:
    #         #   add missing partners
    #         pass