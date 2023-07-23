from odoo import api, models, tools
from odoo.http import request


class Menu(models.Model):
    _inherit = "ir.ui.menu"

    """
    By default, the menu is the same for all companies.
    Now a company may create menuitems for the company.
    Selecting a new company combination ("sorted_cids") will "load_menus" again.
    This requires a change in the Odoo core:
        @api.model
        @tools.ormcache_context('self._uid', 'debug', keys=('lang', 'sorted_cids'))
        def load_menus(self, debug):
            ...
    """

    @classmethod
    def _browse(cls, env, ids, prefetch_ids):
        records = super()._browse(env, ids, prefetch_ids)
        cids = ""
        try:
            cids = request.httprequest.cookies.get("cids")
        except:
            # Failing on updating database
            pass
        if cids and not env.context.get("sorted_cids"):
            allowed_company_ids = [int(cid) for cid in cids.split(",")]
            sorted_cids = allowed_company_ids
            sorted_cids.sort()
            sorted_cids = tuple(sorted_cids)

            context = {key: value for key, value in env.context.items()}
            context["sorted_cids"] = sorted_cids
            context["allowed_company_ids"] = allowed_company_ids
            return records.with_env(records.env(context=context))
        else:
            return records
