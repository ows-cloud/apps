from odoo import api, fields, models, _
import re


class AccountMove(models.Model):
    _inherit = "account.move"

    # def update_invoice(self):
    #     self.ensure_one()
    #     attachment = self.message_main_attachment_id
    #     wizard = self.env['account.invoice.import'].create({
    #         'invoice_id': self.id,
    #         'invoice_filename': attachment.name,
    #         'invoice_file': attachment.datas
    #     })
    #     wizard.update_invoice()

    @api.model
    def message_new(self, msg_dict, custom_values=None):
        journal = self.env['account.journal'].browse(custom_values.get('journal_id'))
        if journal and journal.type == 'purchase':
            return self.env['account.invoice.import'].message_new(msg_dict, custom_values)

        return super(AccountMove, self).message_new(msg_dict, custom_values)

