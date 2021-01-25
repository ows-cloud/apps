from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
from . import amelding_logic
import base64
import pyxb
import logging
_logger = logging.getLogger(__name__)

pyxb.RequireValidWhenGenerating(True)

class Amelding(models.Model):
    _name = 'l10n_no_hr_payroll.amelding'

    @api.depends('meldingsId', 'kalendermaaned')
    def _compute_amelding_filename(self):
        self.ensure_one()
        name = 'A-melding for {kalendermaaned} - id {meldingsId}.xml'.format(kalendermaaned=self.kalendermaaned, meldingsId=self.meldingsId)
        self.amelding_filename = name

    @api.depends('amelding')
    def _compute_amelding_xml(self):
        self.amelding_xml = base64.b64encode(bytes(self.amelding, 'utf-8'))

    company_id = fields.Many2one('res.company', string='Company', required=True, store=True, index=True, default=lambda self: self.env.user.company_id)
    meldingsId = fields.Integer(readonly=True)
    erstatterMeldingsId = fields.Integer(readonly=True)
    kalendermaaned = fields.Char()
    leveringstidspunkt = fields.Datetime(readonly=True)
    state = fields.Selection([('new','New'),('done','Done')], default='new')
    amelding = fields.Text(readonly=True)
    amelding_filename = fields.Char(compute=_compute_amelding_filename)
    amelding_xml = fields.Binary(compute=_compute_amelding_xml, string="A-melding xml")

    def set_state_done(self):
        self.write({'state': 'done'})
        return True

class AmeldingWizard(models.TransientModel):
    _name = 'l10n_no_hr_payroll.amelding.wizard'

    kalendermaaned = fields.Char()

    def lag_amelding(self):
        # Verify period
        try:
            date_from = datetime.strptime(self.kalendermaaned + '-01', '%Y-%m-%d')
        except:
            raise UserError(_('The period should have this format: yyyy-mm'))

        # Look for existing amelding record
        company_id = self.env.user.company_id.id
        record = self.env['l10n_no_hr_payroll.amelding'].search([
            ('kalendermaaned','=',self.kalendermaaned),('company_id','=',company_id)], order='id desc', limit=1)
        if record and record.state == 'new':
            record.leveringstidspunkt = datetime.now()
        else:
            # Create amelding record
            d = {}
            if record:
                d['erstatterMeldingsId'] = record.meldingsId
            d['meldingsId'] = self.env['ir.sequence'].next_by_code('l10n_no_hr_payroll.amelding')
            d['kalendermaaned'] = self.kalendermaaned
            d['leveringstidspunkt'] = datetime.now()

            record = self.env['l10n_no_hr_payroll.amelding'].create(d)

        logic = amelding_logic.AmeldingLogikk(record)
        record.amelding = logic.melding_xml()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_no_hr_payroll.amelding',
            'res_id': record.id,
            'view_type': 'tree,form',
            'view_mode': 'form',
        }