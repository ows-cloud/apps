from psycopg2 import sql
from odoo import _, api, fields, models

class APIKeys(models.Model):
    _inherit = 'res.users.apikeys'

    def init(self):
        # pylint: disable=sql-injection
        self.env.cr.execute(sql.SQL("""
            ALTER TABLE {table} 
                ADD COLUMN IF NOT EXISTS company_id INTEGER REFERENCES res_company(id)
            ;
            """).format(table=sql.Identifier(self._table))
        )
