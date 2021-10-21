from odoo import api, fields, models
from .profession_codes import profession_codes

import logging
_logger = logging.getLogger(__name__)

class Job(models.Model):
    _inherit = 'hr.job'
    
    def l10n_no_import_profession(self):
        SelectValue = self.env['res.field.selection_value']
        field_id = self.env.ref('l10n_no_payroll.res_field_l10n_no_profession_code').id
        records = SelectValue.search_count([('field_id','=',field_id)])
        if not records:
            for line in profession_codes.splitlines():
                SelectValue.create({'field_id': field_id, 'code': line[:4] + line[5:8], 'name': line[9:]})