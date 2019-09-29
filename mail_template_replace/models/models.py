# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class MailTemplate(models.Model):
    _inherit = 'mail.template'

    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
    replace_mail_template = fields.Char("Replace Mail Template (Ext.ID)")
    
    _sql_constraints = [('replace_mail_template_uniq', 'unique(replace_mail_template, company_id)', 'Replace Mail Template must be unique per company!')]


class IrModelData(models.Model):
    _inherit = 'ir.model.data'
    
    @api.model
    def xmlid_lookup(self, xmlid):
        id, model, res_id = super(IrModelData, self).xmlid_lookup(xmlid)
        if model == 'mail.template':
            company_id = self.env.context.get('default_company_id') or self.env.context.get('force_company') or self.env.user.company_id.id
            result = self.env['mail.template'].search([('replace_mail_template', '=', xmlid),('company_id', '=', company_id)])
            if result:
                res_id = result.id
        return id, model, res_id
