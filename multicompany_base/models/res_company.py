import logging

from odoo import api, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class Company(models.Model):
    _inherit = "res.company"

    @api.model
    def create(self, vals):
        new_company = super(Company, self.bypass_company_rules()).create(vals)
        new_company.partner_id.write({"company_id": new_company.id})

        # Give access to SUPPORT USER and CURRENT USER
        # Configure public/default user fails without sudo() here.
        support_user = self.sudo().bypass_company_rules().env.ref(
            "__multicompany_base__.support_user"
        )
        support_user.bypass_company_rules().write(
            {"company_ids": [(4, new_company.id)]}
        )
        self.flush()

        # Auto-configure company
        config = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("multicompany_base.force_config")
        )
        if config in ("1", "t", "true", "True"):
            new_company.env["multicompany.config"]._configure_companies(new_company)

        return new_company

    def configure(self):
        companies = self
        self.env["multicompany.config"]._configure_companies(companies)

    def count_records(self):
        csv = "company_id,table_name,year,no_of_records\n"
        for model_record in self.env["ir.model"].search([]):
            model_name = model_record.model
            model = self.env[model_name]
            company_id_field_record = self.env["ir.model.fields"].search(
                [("model", "=", model_name), ("name", "=", "company_id")]
            )
            create_date_field_record = self.env["ir.model.fields"].search(
                [("model", "=", model_name), ("name", "=", "create_date")]
            )
            if (
                not create_date_field_record
                or not company_id_field_record
                or not company_id_field_record.store
                or not model._auto
                or model._inherits
            ):
                continue
            table_name = model._table
            sql = """
                SELECT
                    company_id,
                    '{}' as table_name,
                    date_trunc('year', create_date) AS sql_year,
                    count(id) as no_of_records
                FROM {}
                GROUP BY company_id, sql_year;
                """.format(
                table_name, table_name
            )
            self.env.cr.execute(sql)
            sql_result = self.env.cr.fetchall()
            for row in sql_result:
                csv += "{},{},{},{}\n".format(row[0], row[1], str(row[2])[:4], row[3])
        raise UserError(csv)
