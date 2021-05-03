import logging

from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slugify


_logger = logging.getLogger(__name__)


class SMSController(http.Controller):

    @http.route(['/incoming_sms/<string:sms>'], type='http', auth="public", website=True)
    def process_sms(self, sms, **kwargs):

        #_logger.warning(sms)
        #_logger.warning(kwargs['arg'])
        # %0A newline; %20 space
        Company = request.env['res.company']
        SMS = request.env['sms.receive_sms']
        ServerAction = request.env['ir.actions.server']

        company_ref, message = sms.split(maxsplit=1)
        company = Company.search([('ref', '=', company_ref)])
        sms_dict = {
            'company_id': company.id,
            'message': message,
        }
        sms_record = SMS.sudo().create(sms_dict)
        _logger.warning(sms_record)
        if not company:
            return http.Response("Company doesn't exist", status=200)

        company.sms_server_action_id.sudo(company.user_tech_id.id
            ).with_context({
                'active_model': SMS._name, # SMS.sudo().model ?
                'active_id': sms_record.id,
            }).run()
        
        return http.Response("OK", status=200)