from odoo import models
from odoo.addons.base_sparse_field.models.fields import Serialized


class Base(models.AbstractModel):
    _inherit = "base"

    json = Serialized()
