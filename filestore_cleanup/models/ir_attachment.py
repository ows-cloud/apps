import logging
import os
from pathlib import Path

from odoo import models
from odoo.exceptions import AccessError
from odoo.tools.config import config

_logger = logging.getLogger(__name__)


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    def _action_filestore_cleanup(self):
        if not self.env.user.has_group('base.group_system') :
            raise AccessError("Access Denied")

        cr = self.env.cr
        count_deleted = 0

        cr.execute("SELECT store_fname FROM ir_attachment;")
        attachments = {row[0] for row in cr.fetchall()}

        data_dir = config.get("data_dir")
        sep = separator = "/" if "/" in data_dir else "\\"
        db_path = "{}{}filestore{}{}".format(data_dir, sep, sep, cr.dbname)
        for root, dirs, files in os.walk(db_path):
            dirs = dirs  # use the variable to pass OCA pre-commit
            for file in files:
                file_path = "{}{}{}".format(root, sep, file)
                store_fname = file_path[len(db_path) + 1:]
                if sep == "\\":
                    store_fname = store_fname.replace("\\", "/")
                if store_fname not in attachments:
                    Path(file_path).unlink()
                    _logger.info("Deleted {}".format(store_fname))
                    count_deleted += 1

        _logger.info("{} files were deleted.".format(count_deleted))
        return count_deleted
