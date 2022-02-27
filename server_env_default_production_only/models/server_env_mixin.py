from odoo import api, fields, models
from odoo.tools.config import config as system_base_config


class ServerEnvMixin(models.AbstractModel):
    _inherit = "server.env.mixin"

    def _compute_server_env_from_default(self, field_name, options):
        """
        Get values from the database only if 

        [options]
        running_env = production

        In a non-production Odoo server, database values are ignored (for _server_env_fields).

        The module "mail_environment" applies _server_env_fields to mail configurations.
        Storing mail configurations in the database, the mail configurations are disabled in a non-produciton Odoo server.
        """
        if system_base_config["running_env"] == "production":
            super(ServerEnvMixin, self)._compute_server_env_from_default(field_name, options)
        else:
            self[field_name] = False
