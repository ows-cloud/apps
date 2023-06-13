import os

from odoo import _, api, models
from odoo.exceptions import UserError


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    # source: base/ir/ir_attachment.py
    # - fname = sha[:3] + '/' + sha
    # + fname = 'company/' + str(self.company_id.id) + '/' + sha[:3] + '/' + sha
    # - fname = sha[:2] + '/' + sha
    # + fname = 'company/' + str(self.company_id.id) + '/' + sha[:2] + '/' + sha
    @api.model
    def _get_path(self, bin_data, sha):
        # retro compatibility
        fname = "company/" + str(self.env.company.id) + "/" + sha[:3] + "/" + sha
        full_path = self._full_path(fname)
        if os.path.isfile(full_path):
            return fname, full_path  # keep existing path

        # scatter files across 256 dirs
        # we use '/' in the db (even on windows)
        fname = "company/" + str(self.env.company.id) + "/" + sha[:2] + "/" + sha
        full_path = self._full_path(fname)
        dirname = os.path.dirname(full_path)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        # prevent sha-1 collision
        if os.path.isfile(full_path) and not self._same_content(bin_data, full_path):
            raise UserError(_("The attachment is colliding with an existing file."))
        return fname, full_path
