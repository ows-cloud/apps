from datetime import datetime

from odoo import fields, models


class CalendarEventMatrixRow(models.Model):
    _name = "calendar.event.matrix.row"
    _description = "Calendar Event Matrix Row"
    _order = "sequence"

    sequence = fields.Integer()
    name = fields.Char()
    matrix_id = fields.Many2one("calendar.event.matrix", string="Group")
    allday = fields.Boolean(
        string="All day",
        default=False,
        help="If True, don't use default_start & default_stop",
    )
    default_start = fields.Datetime(
        string="Default Start Time",
        help="Any date; only the time is relevant.",
        default=datetime(year=2000, month=1, day=1, hour=12, minute=15),
    )
    # default_duration = fields.Float("Default Duration")
    default_stop = fields.Datetime(
        string="Default Stop Time",
        help="Any date; only the time is relevant.",
        default=datetime(year=2000, month=1, day=1, hour=12, minute=45),
    )
    add_company_partner = fields.Boolean(
        string="Non-empty",
        help="To drag/drop attendees between events, the events must be non-empty. Therefore add the company partner.",
    )
    show_in_matrix = fields.Boolean("Show in Matrix", default=True)
    allow_to_sign_up = fields.Boolean(
        string="Allow to sign up",
        help="Allow to sign up for this calendar event."
    )
    parent_id = fields.Many2one(
        "calendar.event.matrix.row",
        string="Parent Row",
    )
    # child_ids = fields.One2many("calendar.event.matrix.row", "parent_id", string="Child Records")
    # show_in_matrix_event_ids = fields.One2many("calendar.event", "matrix_row_id", string="Calendar Events")

    # Not implemented
    # default_all_matrix_partners = fields.Boolean("Add all participants")
    # allowed_partner_ids = fields.Many2many('res.partner', string="Allowed contacts")

    # def create(self, values):
    #     if "default_all_matrix_partners" in values:
    #         self._update_default_all_matrix_partners(self,
    #           values["default_all_matrix_partners"])
    #     super().create(values)

    # # def write(self, values):
    # #     if "default_all_matrix_partners" in values:
    # #         self._update_default_all_matrix_partner(self,
    #               values["default_all_matrix_partners"])
    # #     super().write(values)

    # def _update_default_all_matrix_partners(self):
    #     self.ensure_one()
    #     if self.default_all_matrix_partners:
    #         # search for calendar.event with this row
    #         # for each calendar.event:
    #         #   add missing partners
    #         pass
