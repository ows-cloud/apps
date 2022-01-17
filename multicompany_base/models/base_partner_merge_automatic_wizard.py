from odoo import api, fields, models


class MergePartnerAutomatic(models.TransientModel):
    _inherit = 'base.partner.merge.automatic.wizard'

    def _merge(self, partner_ids, dst_partner=None, extra_checks=True):
        """Company Manager can merge contacts without extra checks."""
        if self.env.user.has_group('base_professional.group_company_manager'):
            extra_checks = False
        return super(MergePartnerAutomatic, self)._merge(
            partner_ids, dst_partner, extra_checks)
