from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class ProductUomCateg(models.Model):
    _inherit = 'uom.category'

    # Delivery module needs to lookup weight category. See custom code in 'res.company' and 'stock.picking'.
    is_weight = fields.Boolean(string="Is Weight")


class StockMove(models.Model):
    _inherit = 'stock.move'

    # Inherited from delivery
    def _default_uom(self):
        uom_categ_id = self.env['uom.category'].search(
            [('is_weight', '=', True), ('company_id', '=', self.env.user.company_id.id)], limit=1).id
        weight_uom_id = self.env['uom.uom'].search([('category_id', '=', uom_categ_id), ('factor', '=', 1)],
                                                       limit=1)
        _logger.debug("StockMove _default_uom: " + str(weight_uom_id) + ', user_id = ' + str(self.env.user.id))
        return weight_uom_id

    weight_uom_id = fields.Many2one(default=_default_uom)


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Inherited from delivery
    def _default_uom(self):
        uom_categ_id = self.env['uom.category'].search(
            [('is_weight', '=', True), ('company_id', '=', self.env.user.company_id.id)], limit=1).id
        weight_uom_id = self.env['uom.uom'].search([('category_id', '=', uom_categ_id), ('factor', '=', 1)],
                                                       limit=1)
        _logger.debug("StockPicking _default_uom: " + str(weight_uom_id) + ', user_id = ' + str(self.env.user.id))
        return weight_uom_id

    weight_uom_id = fields.Many2one(default=_default_uom)
