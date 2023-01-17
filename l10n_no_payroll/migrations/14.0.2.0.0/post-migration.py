from collections import defaultdict
from openupgradelib import openupgrade


x_codes = [
    "x_month_salary",
    "x_month_houserent",
    "x_meals",
    "x_month_food",
    "x_house_tax_value",
    "x_years_from_date",
    "x_percent_more_salary",
]


def create_custom_info(env):
    dict_of_fields = defaultdict(lambda: [])
    for fld in env["res.field"].sudo_bypass_global_rules().search([("code", "in", x_codes)]):
        dict_of_fields[(fld.company_id.id, fld.model)].append(fld)
    # res.field loop
    for (company_id, model), list_of_fields in dict_of_fields.items():
        properties = [
            (0, 0, {"name": fld.name, "code": fld.code, "widget": fld.data_type, "company_id": fld.company_id.id})
            for fld in list_of_fields
        ]
        template = fld.env["custom.info.template"].create(
            {
                "name": "{} for {}".format(model, fld.company_id.name),
                "model": model,
                "model_id": env["ir.model"].search([("model", "=", model)]).id,
                "company_id": company_id,
                "property_ids": properties,
            }
        )
        # res.field.value loop
        for val in env["res.field.value"].sudo_bypass_global_rules().search(
            [("field_code", "in", x_codes), ("company_id", "=", company_id)]
        ):
            record = val.env[val.model].browse(val.res_id)
            if not record.custom_info_template_id:
                # Setting the template will auto-create custom.info.value records.
                record.custom_info_template_id = template.id
            custom_info_value = val.env["custom.info.value"].search(
                [
                    ("model", "=", val.model),
                    ("res_id", "=", val.res_id),
                    ("property_id", "=", template.property_ids.filtered(lambda p: p.code == val.field_code)),
                ]
            )
            custom_info_value.value = val.value


def update_fields(env):
    for val in env["res.field.value"].sudo_bypass_global_rules().search(
        [("field_code", "not like", "x_%")]
    ):
        if val.field_type == "reference":
            value = val.reference_value
        elif val.field_type == "selection":
            value = val.selection_value_id.code
        else:
            value = val.value
        record = val.env[val.model].browse(val.res_id)
        setattr(record, val.field_code, value)


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr
    create_custom_info(env)
    update_fields(env)


"""
This code was written previously to get from regular field to res.field.
In the migration we want to do the opposite.
"""


# def _compute_l10n_no_fields(self):
#     for record in self:
#         record.l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer = float(
#             record.field_value_ids.filtered(
#                 lambda x: x.field_code
#                 == "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer"
#             ).value
#         )
#         record.l10n_no_stillingsprosent = float(
#             record.field_value_ids.filtered(
#                 lambda x: x.field_code == "l10n_no_stillingsprosent"
#             ).value
#         )
