from odoo import models
from collections import defaultdict


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

    def update_record_fields(self):
        for val in self.env["res.field.value"].sudo_bypass_global_rules().search(
            [("field_code", "not like", "x_%")]
        ):
            if val.field_data_type == "reference":
                value = val.reference_value
            elif val.field_data_type == "selection":
                value = val.selection_value_id.code
            else:
                value = val.value
            record = val.env[val.model].browse(val.res_id)
            setattr(record, val.field_code, value)

    def create_custom_info(self):
        dict_of_fields = defaultdict(lambda: [])
        for fld in self.sudo_bypass_global_rules().search([("code", "in", x_codes)]):
            dict_of_fields[(fld.company_id.id, fld.model)].append(fld)
        # res.field loop
        for (company_id, model), list_of_fields in dict_of_fields.items():
            properties = [
                (0, 0, {"name": fld.name, "code": fld.code, "widget": fld.data_type, "company_id": fld.company_id.id})
                for fld in list_of_fields
            ]
            name = "{} for {}".format(model, fld.company_id.name)
            template = fld.env["custom.info.template"].search([("name", "=", name)])
            if not template:
                template = fld.env["custom.info.template"].create(
                    {
                        "name": name,
                        "model": model,
                        "model_id": self.env["ir.model"].search([("model", "=", model)]).id,
                        "company_id": company_id,
                        "property_ids": properties,
                    }
                )
            # res.field.value loop
            for val in self.env["res.field.value"].sudo_bypass_global_rules().search(
                [("field_code", "in", x_codes), ("company_id", "=", company_id)]
            ):
                record = val.env[val.model].browse(val.res_id)
                if not record.custom_info_template_id:
                    record.custom_info_template_id = template.id
                    # Create custom.info.value records
                    record._onchange_custom_info_template_id()
                custom_info_value = val.env["custom.info.value"].search(
                    [
                        ("model", "=", val.model),
                        ("res_id", "=", val.res_id),
                        ("property_id", "=", template.property_ids.filtered(lambda p: p.code == val.field_code).id),
                    ]
                )
                custom_info_value.ensure_one()
                custom_info_value.value = val.value
