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

    def unlink(self):
        self._recompute_distance_before_unlink()
        return super().unlink()

    @api.model
    def create(self, values):
        self._recompute_distance_before_create(values)
        return super().create(values)

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
                record._recompute_distance_before_create(values)
        return super().write(values)

    def _recompute_distance_before_unlink(self):
        for record in self:
            prev = self._get_record("prev")
            next = self._get_record("next")
            if prev and next:
                next.distance = next.value - prev.value
            elif next:
                next.distance = None

    def _recompute_distance_before_create(self, values):
        prev = self._get_record("prev")
        next = self._get_record("next")
        self.check_date(values, prev, next)
        self.set_distance(values, prev, next)

    def _check_date(self, values, prev, next):
        if prev and prev.date > values["date"]:
            raise UserError(_("Date should not be lower than %s.") % str(prev.date))
        if next and next.date < values["date"]:
            raise UserError(_("Date should not be higher than %s.") % str(next.date))

    def set_distance(self, values, prev, next):
        if prev:
            values["distance"] = values["value"] - prev.value
        else:
            values["distance"] = 0
        if next:
            next.distance = next.value - values["value"]

    @api.onchange("value")
    def _onchange_set_distance(self):
        prev = self._get_record("prev")
        if prev:
            self.distance = self.value - prev.value
        else:
            self.distance = 0

    def _get_record(self, which, values=None):
        if values:
            assert type(values) == dict
        else:
            self.ensure_one()

        def _get(field_name):
            if values:
                return values[field_name]
            else:
                value = getattr(self, field_name)
                if hasattr(value, "id"):
                    value = getattr(value, "id")
                return value

        sign = {"prev": "<", "next": ">"}
        order = {"prev": "value desc", "next": "value"}

        return self.search(
            [
                ("vehicle_id", "=", _get("vehicle_id")),
                ("value", sign[which], _get("value")),
                ("id", "!=", self.id),
            ],
            order=order[which],
            limit=1,
        )
