import logging

from odoo import fields, http, SUPERUSER_ID, _
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slugify


_logger = logging.getLogger(__name__)


class SMSController(http.Controller):

    @http.route(['/receive_sms/<string:sender>/<string:message>'], type='http', auth="public", website=True)
    def receive_sms(self, sender, message, **kwargs):

        Company = request.env['res.company']
        SMS = request.env['sms.receive_sms']
        ServerAction = request.env['ir.actions.server']

        company_ref = message.split(' ', maxsplit=1)[0]
        company = Company.search([('ref', '=', company_ref)])
        if not company:
            return http.Response("Company doesn't exist", status=200) #####
        sms_dict = {
            'company_id': company.id,
            'message': message,
            'sender': sender,
        }
        sms_record = SMS.sudo().create(sms_dict)
        #_logger.warning(sms_record)

        # TODO: user_tech_id is needed now to stay secure. Change later.
        company.sms_receive_action_id.sudo(company.user_tech_id.id
            ).with_context({
                'active_model': SMS._name, # SMS.sudo().model ?
                'active_id': sms_record.id,
            }).run()
        
        return http.Response("OK", status=200)