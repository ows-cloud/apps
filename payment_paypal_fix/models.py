import json
import logging
from urllib import parse
from odoo import api, fields, models, _
from odoo.addons.payment_paypal.controllers.main import PaypalController

_logger = logging.getLogger(__name__)


class AcquirerPaypal(models.Model):
    _inherit = 'payment.acquirer'
    
    paypal_pdt_token = fields.Char(string='Paypal PDT Token', help='Payment Data Transfer allows you to receive notification of successful payments as they are made.', groups='base.group_user')

    # Source: payment_paypal/models/payment.py
    # The original paypal_form_generate_values returns the url defined in 'ir.config_parameter' 'web.base.url'
    @api.multi
    def paypal_form_generate_values(self, values):
        paypal_tx_values = super(AcquirerPaypal, self).paypal_form_generate_values(values)

        # get the port number
        url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = url.replace('://', '')
        colon = url.find(':')
        colon_port = ''
        if colon > -1:
            colon_port = url[colon:]

        # url = website + port
        website_id = self.env.context['website_id']
        website = self.env['website'].browse(self.env.context['website_id'])
        base_url = 'https://' + str(website.domain) + colon_port

        paypal_tx_values.update({
            'paypal_return': '%s' % parse.urljoin(base_url, self._return_url),
            'notify_url': '%s' % parse.urljoin(base_url, PaypalController._notify_url),
            'cancel_return': '%s' % parse.urljoin(base_url, PaypalController._cancel_url),
        })
        _logger.debug('paypal_form_generate_values: paypal_tx_values = ' + str(paypal_tx_values))
        return paypal_tx_values


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_param(self, key, default=False):
        if key == 'payment_paypal.pdt_token':
            result = self.env['payment.acquirer'].search([('provider', '=', 'paypal'), ('company_id', '=', self.env.user.company_id.id)])
            for res in result:
                return res.paypal_pdt_token

        return super(IrConfigParameter, self).get_param(key, default)