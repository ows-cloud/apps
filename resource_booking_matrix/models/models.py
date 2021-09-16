# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, fields


class ResourceBooking(models.Model):
    _inherit = 'resource.booking'

    def _compute_start_date(self):
        for record in self:
            record.start_date = record.start.date()

    start_date = fields.Date("Start Date", compute='_compute_start_date')
