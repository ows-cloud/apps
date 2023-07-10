import logging

from collections import defaultdict

from odoo import SUPERUSER_ID, api

import odoo.addons.base.models.base as base
from odoo.exceptions import UserError

from .models.multicompany_security import SECURITY_DO_IF, NO_ACCESS_MODEL, NO_EDIT_MODEL


_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    model_without_field_name_to_get_company = []
    model_names = env["ir.model"].search([]).mapped("model")
    for model_name in model_names:
        model = env["ir.model"].search([("model", "=", model_name)])
        if not env[model.model]._auto:
            pass
        elif "company_id" in model._fields:
            pass
        elif model_name in NO_ACCESS_MODEL or model_name in NO_EDIT_MODEL:
            pass
        elif model_name in base.FIELD_NAME_TO_GET_COMPANY:
            pass
        else:
            model_without_field_name_to_get_company.append(model_name)
    if model_without_field_name_to_get_company:
        raise UserError("Models without field name to get company: {}".format(
            model_without_field_name_to_get_company
        ))


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # SET DEFAULT USER
    env.ref("base.default_user").default_user = True
    # SET PARAMETERS
    ICP = env["ir.config_parameter"].sudo()
    default_settings = [
        ("multicompany_base.force_security", "1"),
        ("multicompany_base.force_security_company_manager", "1"),
        ("multicompany_base.force_config", "1"),
    ]
    for key, value in default_settings:
        if not ICP.get_param(key):
            ICP.set_param(key, value)
    # CREATE SUPPORT USER
    _create_support_user(env)
    # SET COMPANY ID WHERE NULL
    _set_company_id_where_null(env)


def WARNING_DELETE_RULES_uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Delete global rules
    for do_if in SECURITY_DO_IF:
        rules = env["ir.rule"].search(
            [("name", "ilike", "% - %_model%{}".format(do_if))]
        )
        rules.unlink()
    # Delete company manager access and rules
    group = env.ref("multicompany_base.group_company_manager")
    group.model_access.unlink()
    for rule in group.rule_groups:
        if rule.name == "res.partner.rule.private.group":
            pass
        if len(rule.groups) > 1:
            rule.write({"groups": [(3, group.id, 0)]})
        else:
            rule.unlink()


def _create_support_user(env):
    support_user = env.ref(
        "__multicompany_base__.support_user", raise_if_not_found=False
    )
    if not support_user:
        companies = env["res.company"].sudo().search([])
        support_user = (
            env["res.users"]
            .sudo()
            .create(
                {
                    "login": "support",
                    "lang": "en_US",
                    "name": "Support User",
                    "company_ids": [(6, 0, companies.ids)],
                    "groups_id": [
                        (4, env.ref("multicompany_base.group_company_manager").id),
                        (4, env.ref("base.group_partner_manager").id),
                    ],
                }
            )
        )
        env["ir.model.data"].create(
            {
                "module": "__multicompany_base__",
                "name": "support_user",
                "model": "res.users",
                "res_id": support_user.id,
            }
        )


def _set_company_id_where_null(env):
    self = env["base"].sudo_bypass_global_rules()
    _logger.info("Starting _set_company_id_where_null")

    last_model_names = ["ir.property", "ir.model.data"]
    model_names = (
        self.env["ir.model"]
        .search([("model", "not in", last_model_names)])
        .mapped("model")
    )
    model_names.extend(last_model_names)

    for model_name in model_names:
        model = self.env["ir.model"].search([("model", "=", model_name)])
        if not self.env[model.model]._auto:
            continue
        if model.model == "ir.model.fields":
            sql = "UPDATE {} SET company_id = 1 WHERE company_id IS NULL;".format(
                model.model.replace(".", "_")
            )
            self.env.cr.execute(sql)
            continue

        records_with_no_company = (
            self.env[model.model]
            .with_context(
                active_test=False,
            )
            .sudo_bypass_global_rules()
            .search([("company_id", "=", False)])
        )
        if not records_with_no_company:
            continue

        # WHICH WAY IS THE FASTEST?

        # A) For each record: write company_id
        # for record in records_with_no_company:
        #     company = self.env[model.model].related_company(record)
        #     if company:
        #         record.sudo().write({'company_id': company.id})

        # B) For each group of similar records: write_company_id

        # relation_field_name = RELATED_RECORD.get(model.model)
        # if not relation_field_name:
        #     records_with_no_company.sudo().write(
        #       {'company_id': self.env.company.id})
        #     continue

        # relation_field = self.env[model.model]._fields[relation_field_name]
        # if relation_field.type == 'many2one_reference':
        #     relation_model_names = set(
        #       records_with_no_company.mapped(relation_field.model_field))
        #     for relation_model_name in relation_model_names:
        #         records_filtered_model = records_with_no_company.filtered(
        #           lambda r: getattr(
        #               r, relation_field.model_field) == relation_model_name)
        #         relation_ids = list(set(
        #           records_filtered_model.mapped(relation_field_name)))
        #         relations = self.env[relation_model_name].browse(relation_ids)
        #         for relation in relations:
        #             related_company = relation.company_id
        #             records_filtered = records_filtered_model.filtered(
        #               lambda r: getattr(r, relation_field_name) == relation.id)
        #             records_filtered.sudo().write({'company_id': related_company.id})
        # else:
        #     relations = records_with_no_company.mapped(relation_field_name)
        #     for relation in relations:
        #         related_company = relation.company_id
        #         records_filtered = records_with_no_company.filtered(
        #           lambda r: getattr(r, relation_field_name) == relation.id)
        #         records_filtered.sudo().write({'company_id': related_company.id})

        # C) Another way to loop

        related_field_name = base.FIELD_NAME_TO_GET_COMPANY.get(model.model)
        if not related_field_name:
            if model_name in NO_ACCESS_MODEL or model_name in NO_EDIT_MODEL:
                records_with_no_company.sudo_bypass_global_rules().write(
                    {"company_id": self.env.company.id}
                )
            else:
                _logger.warning("No company -> 1 for {}".format(records_with_no_company))
            continue
        related_field = self.env[model.model]._fields[related_field_name]
        related_models_and_record_ids = defaultdict(
            lambda: []
        )  # {'res.partner': [(1001, 1), (1002, 2), (1003, 3)]}
        for record in records_with_no_company:
            [
                (related_model_name, related_record_id)
            ] = base._get_model_name_and_res_id(record, related_field, record)
            if related_model_name and related_record_id:
                related_models_and_record_ids[related_model_name].append(
                    (record.id, related_record_id)
                )

        for related_model_name, ids in related_models_and_record_ids.items():

            related_record_ids = [tup[1] for tup in ids if tup[1]]
            # Related records may not exist. Search for existing related records.
            related_records = (
                self.env[related_model_name]
                .sudo_bypass_global_rules()
                .search([("id", "in", related_record_ids)])
            )
            related_companies = related_records.mapped("company_id")
            for related_company in related_companies:
                related_records_with_this_company = related_records.filtered(
                    lambda r: r.company_id == related_company
                )
                update_record_ids = [
                    tup[0]
                    for tup in ids
                    if tup[1] in related_records_with_this_company.ids
                ]
                # Option 1
                # records_with_no_company.filtered(
                #   lambda r: id in update_record_ids
                # ).sudo().write({'company_id': related_company.id})
                # Option 2
                self.env[model.model].sudo_bypass_global_rules().browse(
                    update_record_ids
                ).write({"company_id": related_company.id})

            record_ids_with_no_related_record = [
                tup[0] for tup in ids if not tup[1]
            ]
            # Option 1
            # records_with_no_company.filtered(
            #   lambda r: id in record_ids_with_no_related_record
            # ).sudo().write({'company_id': self.env.company.id})
            # Option 2
            self.env[model.model].sudo_bypass_global_rules().browse(
                record_ids_with_no_related_record
            ).write({"company_id": self.env.company.id})
