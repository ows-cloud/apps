import base64
import logging

import pyxb

from odoo import _, api, fields, models


pyxb.RequireValidWhenGenerating(True)


class Amelding(models.Model):
    _name = "l10n.no.amelding"
    _description = "A-melding"

    @api.depends("meldingsId", "kalendermaaned")
    def _compute_amelding_filename(self):
        self.ensure_one()
        name = "A-melding for {kalendermaaned} - id {meldingsId}.xml".format(
            kalendermaaned=self.kalendermaaned, meldingsId=self.meldingsId
        )
        self.amelding_filename = name

    @api.depends("amelding")
    def _compute_amelding_xml(self):
        self.amelding_xml = base64.b64encode(bytes(self.amelding, "utf-8"))

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        store=True,
        index=True,
        default=lambda self: self.env.company,
    )
    meldingsId = fields.Integer(readonly=True)
    erstatterMeldingsId = fields.Integer(readonly=True)
    kalendermaaned = fields.Char()
    leveringstidspunkt = fields.Datetime(readonly=True)
    state = fields.Selection([("new", "New"), ("done", "Done")], default="new")
    amelding = fields.Text(readonly=True)
    amelding_filename = fields.Char(compute=_compute_amelding_filename)
    amelding_xml = fields.Binary(compute=_compute_amelding_xml, string="A-melding xml")

    def set_state_done(self):
        self.write({"state": "done"})
        return True
