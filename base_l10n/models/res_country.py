import csv
import logging

_logger = logging.getLogger(__name__)

from odoo import fields, models

from .iso_3166_1 import iso_3166_1
from .iso_3166_1_values import address_format

# from .iso_3166_2 import iso_3166_2

# TODO: See __manifest__ description


class ResCountry(models.Model):
    _inherit = "res.country"

    region = fields.Char()

    def update_countries(self):
        regions = {
            c["alpha-2"]: " / ".join(
                filter(None, [c["region"], c["sub-region"], c["intermediate-region"]])
            )
            for c in csv.DictReader(iso_3166_1.splitlines())
        }

        for country in self.search([]):
            values = {}
            if country.code in address_format:
                values["address_format"] = address_format[country.code]
            if country.code in regions:
                values["region"] = (
                    regions[country.code] if regions[country.code] else None
                )

            country.write(values)
