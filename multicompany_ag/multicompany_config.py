
from collections import defaultdict
import logging
from odoo import models

_logger = logging.getLogger(__name__)
SYSTEM_COMPANY_ID = 1


class MulticompanyConfig(models.AbstractModel):
    _inherit = 'multicompany.config'
    
    def special_config(self):
        self._special_uom()

    def _special_uom(self):
        """
        uom 
            File "/o14/o14-server/addons/uom/models/uom_uom.py", line 85, in _check_category_reference_uniqueness
                raise ValidationError(_("UoM category %s should only have one reference unit of measure.")
        """
        all_uoms = self.env['uom.uom'].search([])
        ref_uoms = all_uoms.filtered(lambda u: u.uom_type == 'reference')
        categories = ref_uoms.mapped('category_id')
        for category in categories:
            cat_ref_uoms = ref_uoms.filtered(lambda u: u.category_id == category)
            if len(cat_ref_uoms) == 1:
                continue
            # For reference uoms (except company_id 1): 
            for cat_ref_uom in cat_ref_uoms.filtered(lambda u: u.company_id.id != 1):
                # Duplicate the category, and reference all the related company uoms to this category.
                company = cat_ref_uom.company_id
                new_category = category.sudo().copy({'company_id': company.id, 'measure_type': ''})
                company_cat_uoms = all_uoms.filtered(lambda u: u.company_id == company and u.category_id == category)
                models.Model.write(company_cat_uoms, {'category_id': new_category.id, 'measure_type': ''})
