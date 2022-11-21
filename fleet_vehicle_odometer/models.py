import logging
from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class FleetVehicleOdometer(models.Model):
    _inherit = "fleet.vehicle.odometer"

    analytic_account_id = fields.Many2one(
        "account.analytic.account", string="Analytic Account"
    )
    comment = fields.Char("Comment")
    distance = fields.Integer("Distance")

    @api.model
    def create(self, values):
        self._recompute_distance_before_create(values)
        return super().create(values)

    def _recompute_distance_before_create(self, values, record_id=0):
        below = self.search(
            [
                ("vehicle_id", "=", values["vehicle_id"]),
                ("value", "<", values["value"]),
                ("id", "!=", record_id),
            ],
            order="value desc",
            limit=1,
        )
        above = self.search(
            [
                ("vehicle_id", "=", values["vehicle_id"]),
                ("value", ">", values["value"]),
                ("id", "!=", record_id),
            ],
            order="value",
            limit=1,
        )

        try:
            values["date"] = datetime.strptime(values["date"], "%Y-%m-%d").date()
        except:
            pass

        if below and below.date > values["date"]:
            raise UserError(_("Date should not be lower than %s.") % str(below.date))
        if above and above.date < values["date"]:
            raise UserError(_("Date should not be higher than %s.") % str(above.date))

        if below:
            values["distance"] = values["value"] - below.value
        else:
            values["distance"] = 0
        if above:
            above.distance = above.value - values["value"]

    def unlink(self):
        for record in self:

            record._recompute_distance_before_unlink()
            return super(fleet_vehicle_odometer, self).unlink()

    def _recompute_distance_before_unlink(self):
        below = self.search(
            [("vehicle_id", "=", self.vehicle_id.id), ("value", "<", self.value)],
            order="value desc",
            limit=1,
        )
        above = self.search(
            [("vehicle_id", "=", self.vehicle_id.id), ("value", ">", self.value)],
            order="value",
            limit=1,
        )

        if below and above:
            above.distance = above.value - below.value
        elif above:
            above.distance = None

    def write(self, values):

        recompute_distance = False
        for value in values:
            if value in ("date", "vehicle_id", "value"):
                recompute_distance = True
        if recompute_distance:
            for record in self:
                record._recompute_distance_before_unlink()
                values["date"] = values.get("date") or record.date
                values["vehicle_id"] = values.get("vehicle_id") or record.vehicle_id.id
                values["value"] = values.get("value") or record.value
                record._recompute_distance_before_create(values, record.id)

        return super(fleet_vehicle_odometer, self).write(values)
