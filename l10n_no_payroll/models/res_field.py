import logging
from collections import defaultdict

from odoo import api, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

x_codes = [
    "x_month_salary",
    "x_month_houserent",
    "x_meals",
    "x_month_food",
    "x_house_tax_value",
    "x_years_from_date",
    "x_percent_more_salary",
]


class Field(models.Model):
    _inherit = "res.field"

    def set_standard_info_in_fields(self):
        for val in (
            self.env["res.field.value"]
            .sudo_bypass_global_rules()
            .search([("field_code", "not like", "x_%")])
        ):
            if val.field_data_type == "reference":
                value = val.reference_value
            elif val.field_data_type == "selection":
                value = val.selection_value_id.code
            else:
                value = val.value
            record = val.env[val.model].sudo_bypass_global_rules().browse(val.res_id)
            if record.exists():
                new_field_name = val.field_code
                if new_field_name == "l10n_no_profession_code":
                    new_field_name = "l10n_no_job_code"
                try:
                    setattr(record.with_record_company(), new_field_name, value)
                except:
                    raise UserError("{} | {} | {} | {} | id {}".format(record.company_id.name, record.display_name, new_field_name, value, val.id))

    def create_custom_info(self):
        i = 0
        dict_of_fields = defaultdict(lambda: [])
        for fld in self.sudo_bypass_global_rules().search([("code", "in", x_codes)], order="model"):
            dict_of_fields[(fld.company_id.id, fld.model)].append(fld)
        # res.field loop
        for (company_id, model), list_of_fields in dict_of_fields.items():
            # All fields in list_of_fields should have the same company.
            context = {key: value for key, value in self.env.context.items()}
            context['allowed_company_ids'] = [company_id]
            env = api.Environment(self.env.cr, self.env.uid, context, su=True)
            base = self.env["base"].with_env(env)

            properties = [
                (
                    0,
                    0,
                    {
                        "name": fld.name,
                        "code": fld.code,
                        "widget": fld.data_type,
                        "company_id": fld.company_id.id,
                    },
                )
                for fld in list_of_fields
            ]
            name = "{} for {}".format(model, base.env.company.name)
            template = base.env["custom.info.template"].search([("name", "=", name)])
            if not template:
                template = base.env["custom.info.template"].create(
                    {
                        "name": name,
                        "model": model,
                        "model_id": self.env["ir.model"]
                        .search([("model", "=", model)])
                        .id,
                        "company_id": company_id,
                        "property_ids": properties,
                    }
                )
            # res.field.value loop
            for val in (
                self.env["res.field.value"]
                .sudo_bypass_global_rules()
                .search(
                    [("field_code", "in", x_codes), ("company_id", "=", company_id), ("model", "=", model)]
                )
            ):
                record = val.env[val.model].browse(val.res_id)
                if not record.exists():
                    continue
                # record = record.sudo_bypass_global_rules()
                if not record.custom_info_template_id:
                    record.custom_info_template_id = template.id
                    # Create custom.info.value records
                    record = record.with_company(record.company_id)
                    record._onchange_custom_info_template_id()
                custom_info_value = record.env["custom.info.value"].search(
                    [
                        ("company_id", "=", val.company_id.id),
                        ("model", "=", val.model),
                        ("res_id", "=", val.res_id),
                        (
                            "property_id",
                            "=",
                            template.property_ids.filtered(
                                lambda p: p.code == val.field_code
                            ).id,
                        ),
                    ]
                )
                # if sum([1 for record in custom_info_value]) != 1:
                #     will = "debug"
                custom_info_value.ensure_one()
                custom_info_value.value = val.value
                i += 1
                _logger.info(i)
                if i >= 1079:
                    break
