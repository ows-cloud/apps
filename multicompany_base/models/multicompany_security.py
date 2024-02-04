import copy
import logging
from collections import defaultdict

from odoo import models

_logger = logging.getLogger(__name__)

# Module name for external IDs made with python.
# (Not in XML, so cannot be a module name.)
# Used for company_id fields, also in hooks.py.
EXTID_MODULE_NAME = "__multicompany_security__"

COMPANIES_MODEL = [
    "base_import.import",  # Import write() compares company_id with
    # stored user.company_id instead of context company_id.
]

COMPANY_READ_SYSTEM_MODEL = [
    "account.account.template",
    "account.account.type",
    "account.chart.template",
    "account.fiscal.position.template",
    "account.payment.term",  # to avoid error with
    # ref('account.account_payment_term_immediate').sudo() in website_sale
    "account.tax.template",
    "crm.team",  # to avoid error: access_control() failed
    "ir.actions.act_url",
    "ir.actions.act_window",
    "ir.actions.act_window_close",
    "ir.actions.act_window.view",
    "ir.actions.actions",
    "ir.actions.client",
    "ir.actions.report",
    "ir.actions.server",
    "ir.actions.todo",
    "ir.attachment",
    "ir.filters",
    "ir.mail.server",
    "ir.model.data",
    "ir.module.module",
    "ir.translation",  # temporarily disabled, see hardcoding below
    "ir.ui.menu",
    "ir.ui.view",
    "mail.template",
    "mis.report",
    "mis.report.kpi",
    "mis.report.kpi.expression",
    "mis.report.style",
    "mis.report.subreport",
    "py3o.template",
    "res.field",  # Will be replaced by base_custom_info
    "res.field.selection_value",  # Will be replaced by base_custom_info
    "stock.location",
    "uom.uom",
    "website.menu",
    "xlsx.template",
    "xlsx.template.export",
    "xlsx.template.import",
]

NO_EDIT_MODEL = [
    # BASE, IR, RES
    "base.automation",  # create:    self._update_cron()    self._update_registry()
    "base.language.export",
    "base.language.import",
    "base.language.install",
    "base.module.uninstall",
    "base.module.update",
    "base.module.upgrade",
    "base.update.translations",
    "decimal.precision",
    "ir.cron",
    "ir.logging",
    "ir.model",
    "ir.model.access",
    "ir.model.constraint",
    "ir.model.fields.selection",
    "ir.model.relation",
    "ir.module.category",
    "ir.module.module",
    "ir.module.module.dependency",
    "ir.module.module.exclusion",
    "ir.rule",
    "ir.server.object.lines",  # base.automation
    "mail.message.subtype",
    "res.country",
    "res.country.state",
    "res.country.group",
    "res.currency",
    "res.groups",
    "res.lang",
    # APPS
    "account.payment.method",
    "account.tax.group",
    "l10n.no.tabelltrekk",
    "l10n.no.job.code",
    "mail.activity.type",
    "payment.icon",
    "report.layout",
    "report.paperformat",
    "uom.category",
    "web_tour.tour",
    "wizard.ir.model.menu.create",
]

NO_ACCESS_MODEL = [
    "ir.config_parameter",
    "res.config",
    "res.config.installer",
    "res.config.settings",
]

# TODO: _get_and_fix_name_and_find_model_of_all_sql_views (see code in the bottom)
IRREGULAR_SQL_VIEW_NAMES = {
    # 'view_name': 'model_name',
}

SECURITY_DOMAIN_WORD = {
    "(": "BEGIN",
    ")": "END",
    "AND": "'&'",
    "OR": "'|'",
    "false": "('{company_id}','=',False)",
    "in_companies": "('{company_id}','in',company_ids)",
    "in_companies/parent/child": """
        '|',
        ('{company_id}','in',company_ids),
        '|',
        ('{company_id}','parent_of',company_ids),
        ('{company_id}','child_of',company_ids)""",
    "in_company": "('{company_id}','=',company_id)",
    "in_company/parent/child": """
        '|',
        ('{company_id}','=',company_id),
        '|',
        ('{company_id}','parent_of',company_id),
        ('{company_id}','child_of',company_id)""",
    "json": "('serialization_field_id', '>', 0)",
    "system_company": "('{company_id}','=',1)",
    "system_user": "('id','=',1)",
    "system_partner": "('user_ids','=',1)",
    "company_ids_in_company_ids": "('company_ids','in',company_ids)",
    "user_id": "('user_id','=', user.id)",
}

COMPANY_FIELD = {
    "res.company": {
        "read_if": "id",
        "edit_if": "id",
    },
    # "mis.report.instance": {
    #     "read_if": "edit_company_id",
    #     "edit_if": "edit_company_id",
    # },
    "default": "company_id",
}

"""
All records which a user can browse, are available on relational fields
when the user is creating or editing a record.
A user may lose access to a record by setting another user as the owner.
If a manager can read another company than his own companies,
the manager can switch to this company.
This is a security risk (specially for parent/child).
"""
SECURITY_RULE = {
    # It should be ok to have 'in_company' without 'in_companies'
    # since a user's company should always be one of the user's companies.
    # But it feels safer to include 'in_companies'.
    "BUS_PRESENCE_MODEL": {
        "edit_if": "user_id",
    },
    # A company manager can change to any company which he/she can browse.
    # Don't allow changing to parent/child company.
    "RES_COMPANY_MODEL": {
        "read_if": "in_companies",
        "edit_if": "in_company AND in_companies",
    },
    # read users with access to the company
    # 2022-10-06: Can read users of parent company only in vscode debug.
    # Why not in vscode normal?
    "RES_USERS_MODEL": {
        "read_if": "system_user OR company_ids_in_company_ids OR in_companies/parent/child",
        "edit_if": "in_company AND in_companies",
    },
    # read partners of users with access to the company, otherwise cannot read the users
    # system_partner ('user_ids','=',1) seems not to work.
    "RES_PARTNER_MODEL": {
        "read_if": "system_company OR company_ids_in_company_ids OR in_companies/parent/child",
        "edit_if": "in_company AND in_companies",
    },
    "COMPANIES_MODEL": {
        "read_if": "in_companies/parent/child",
        "edit_if": "in_companies",
    },
    # default
    "COMPANY_MODEL": {
        "read_if": "in_companies/parent/child",
        "edit_if": "in_company AND in_companies",
    },
    "COMPANY_READ_SYSTEM_MODEL": {
        "read_if": "system_company OR in_companies/parent/child",
        "edit_if": "in_company AND in_companies",
    },
    # Relevant if some fields will use JSON format
    "IR_MODEL_FIELDS_MODEL": {
        "read_if": "system_company OR in_companies/parent/child",
        "edit_if": "in_company AND in_companies AND json",
    },
    "NO_EDIT_MODEL": {
        "edit_if": "system_company AND ( in_company AND in_companies )",
    },
    "NO_ACCESS_MODEL": {
        "read_and_edit_if": "system_company AND ( in_company AND in_companies )",
    },
}

SECURITY_DO_IF = {
    "read_if": {
        "perm_read": True,
        "perm_write": False,
        "perm_create": False,
        "perm_unlink": False,
    },
    "edit_if": {
        "perm_read": False,
        "perm_write": True,
        "perm_create": True,
        "perm_unlink": True,
    },
    "read_and_edit_if": {
        "perm_read": True,
        "perm_write": True,
        "perm_create": True,
        "perm_unlink": True,
    },
    "write_if": {
        "perm_read": False,
        "perm_write": True,
        "perm_create": False,
        "perm_unlink": False,
    },
    "create_if": {
        "perm_read": False,
        "perm_write": False,
        "perm_create": True,
        "perm_unlink": False,
    },
    "unlink_if": {
        "perm_read": False,
        "perm_write": False,
        "perm_create": False,
        "perm_unlink": True,
    },
}


def _get_security_type(model_name):
    if model_name == "bus.presence":
        return "BUS_PRESENCE_MODEL"
    elif model_name == "ir.model.fields":
        return "IR_MODEL_FIELDS_MODEL"
    elif model_name == "res.company":
        return "RES_COMPANY_MODEL"
    elif model_name == "res.partner":
        return "RES_PARTNER_MODEL"
    elif model_name == "res.users":
        return "RES_USERS_MODEL"
    elif model_name in NO_ACCESS_MODEL:
        return "NO_ACCESS_MODEL"
    elif model_name in NO_EDIT_MODEL:
        return "NO_EDIT_MODEL"
    elif model_name in COMPANY_READ_SYSTEM_MODEL:
        return "COMPANY_READ_SYSTEM_MODEL"
    elif model_name in COMPANIES_MODEL:
        return "COMPANIES_MODEL"
    else:
        return "COMPANY_MODEL"


def _assert_security_domain_words_and_order(words_list):
    this_type = ""
    last_type = ""
    parenthesis_counter = 0
    first = 0
    last = len(words_list) - 1
    for count, word in enumerate(words_list):
        assert word in SECURITY_DOMAIN_WORD, word + " not in " + str(words_list)

        if word == "(":
            this_type = "parenthesis"
            parenthesis_counter += 1
        elif word == ")":
            this_type = "parenthesis"
            parenthesis_counter -= 1
        elif word in ("AND", "OR"):
            this_type = "operator"
        else:
            this_type = "expression"

        assert parenthesis_counter >= 0
        assert this_type != last_type

        if count in (first, last):
            assert this_type in ("parenthesis", "expression")

    # There should be max one operator type inside a parenthesis.
    # This assert is done in the _recursive_order_words method.


def _recursive_order_words(words_list):
    words_sub_list = {}
    parenthesis_counter = 0
    operator = ""
    last_operator = ""
    for word in words_list:
        if word == "(":
            if parenthesis_counter > 0:
                words_sub_list[parenthesis_counter].append(word)
            parenthesis_counter += 1
        elif word == ")":
            parenthesis_counter -= 1
            if parenthesis_counter > 0:
                words_sub_list[parenthesis_counter].append(word)
            else:
                words_sub_list.setdefault(parenthesis_counter, []).append(
                    _recursive_order_words(words_sub_list[1])
                )
                words_sub_list[1] = []
                last_operator = ""
        else:
            if word in ("AND", "OR"):
                operator = word
                assert (operator == last_operator) or (not last_operator)
            words_sub_list.setdefault(parenthesis_counter, []).append(word)
    words_sub_dict = {}
    for count, word in enumerate(words_sub_list[0]):
        if count % 2 == 0:
            words_sub_dict[count + 1] = word
        else:
            words_sub_dict[count - 1] = word
    ordered_words_list = []
    for count in range(0, len(words_sub_dict) + 1):
        if count in words_sub_dict:
            if type(words_sub_dict[count]) is list:
                ordered_words_list.extend(words_sub_dict[count])
            else:
                ordered_words_list.append(words_sub_dict[count])
    return ordered_words_list


class MulticompanySecurity(models.AbstractModel):
    _name = "multicompany.security"
    _inherit = "base.set.record.values.mixin"
    _description = "Force security between companies"

    def _register_hook(self, update_module=False):
        if update_module:
            true = ("1", "t", "true", "True")
            param = self.env["ir.config_parameter"].get_param(
                "multicompany_base.force_security"
            )
            if param in true:
                self.secure()
            # secure before configure
            param = self.env["ir.config_parameter"].get_param(
                "multicompany_base.force_config"
            )
            if param in true:
                self.env["multicompany.config"].configure_system_and_all_companies()

    # main methods

    def secure(self):
        # Returning an error value to _register_hook will be ignored (see loading.py).
        if not self.env.user.has_group("base.group_system"):
            return False
        # Takes a long time if there are many records without company_id
        self._set_company_id_to_1_where_null()
        self._update_rule_domains_to_1_where_false_except_partner()
        self._set_global_security_rules_on_all_models_except_ir_rule_and_ir_translation()
        self._update_code_to_comply_with_safe_eval()
        self._update_system_records()
        param = "multicompany_base.force_security_company_manager"
        if self.env["ir.config_parameter"].get_param(param) in ("1", repr(True)):
            self.set_company_manager_security()
        return True

    def set_company_manager_security(self):
        # Time consuming
        self._set_read_and_edit_access_to_company_manager()

    def _set_company_id_to_1_where_null(self):
        _logger.info('Starting _set_company_id_to_1_where_null')
        self.env.cr.execute("""
            SELECT t.table_name FROM information_schema.tables t
            INNER JOIN information_schema.columns c ON t.table_name = c.table_name
            WHERE t.table_type='BASE TABLE' AND c.column_name='company_id'
            ORDER BY table_name;""")
        tables = self.env.cr.fetchall()
        for table in tables:
            sql = "UPDATE " + table[0] + " SET company_id = 1 WHERE company_id IS NULL;"
            self.env.cr.execute(sql)


    def _set_global_security_rules_on_all_models_except_ir_rule_and_ir_translation(
        self,
    ):
        _logger.info(
            """Starting _set_global_security_rules_on_all_models_except_ir_rule_..."""
        )
        models = self.env["ir.model"].search(
            [("model", "!=", "ir.rule"), ("model", "!=", "ir.translation")]
        )
        for model in models:
            SECURITY_TYPE = _get_security_type(model.model)
            for do_if, domain_words in SECURITY_RULE[SECURITY_TYPE].items():
                values = copy.deepcopy(SECURITY_DO_IF[do_if])
                values["auto_secure"] = True
                values["groups"] = []
                values["model_id"] = model.id
                values["domain_force"] = self._words2domain(
                    do_if=do_if, words=domain_words, model=model.model
                )
                values["name"] = "{model} - {security_type}, {do_if}".format(
                    model=model.model, security_type=SECURITY_TYPE.lower(), do_if=do_if
                )
                domain = [
                    ("name", "=", values["name"]),
                    ("model_id", "=", values["model_id"]),
                    ("global", "=", True),
                ]
                self._set_record_values("ir.rule", domain, values)

    def _set_read_and_edit_access_to_company_manager(self):
        # Read and edit access on models with company data.
        # Read access on NO_EDIT_MODELs.
        _logger.info("Starting _set_read_and_edit_access_to_company_manager")
        group_company_manager_id = self.env.ref(
            "multicompany_base.group_company_manager"
        ).id
        models_to_exclude = NO_ACCESS_MODEL
        models = self.env["ir.model"].search([("model", "not in", models_to_exclude)])
        for model in models:

            if model.model in NO_EDIT_MODEL:
                security_do_if = "read_if"
            else:
                security_do_if = "read_and_edit_if"
            # ir.model.access
            values = copy.deepcopy(SECURITY_DO_IF[security_do_if])
            values["group_id"] = group_company_manager_id
            values["model_id"] = model.id
            values["name"] = "{model} - company manager, {security_do_if}".format(
                model=model.model, security_do_if=security_do_if
            )
            domain = [
                ("name", "=", values["name"]),
                ("model_id", "=", values["model_id"]),
                ("group_id", "=", values["group_id"]),
            ]
            self._set_record_values("ir.model.access", domain, values)
            # ir.rule
            if model.model in NO_EDIT_MODEL:
                # only system records -> no need for company-manager rule
                continue
            non_global_rules = self.env["ir.rule"].search(
                [("global", "=", False), ("model_id", "=", model.id)]
            )
            if not non_global_rules:
                # no non-global rules -> no need for company-manager rule
                continue
            other_non_global_rules = non_global_rules.filtered(
                lambda r: r.groups.ids != [group_company_manager_id]
            )
            if not other_non_global_rules:
                # no other non-global rules -> no need for company-manager rule, delete it
                assert non_global_rules.ensure_one().groups.ids == [group_company_manager_id]
                non_global_rules.unlink()
                continue
            values = copy.deepcopy(SECURITY_DO_IF["read_and_edit_if"])
            values["groups"] = [(4, group_company_manager_id), 0]
            values["model_id"] = model.id
            values["domain_force"] = "[(1, '=', 1)]"
            values["name"] = "{model} - company manager".format(model=model.model)
            domain = [
                ("name", "=", values["name"]),
                ("model_id", "=", values["model_id"]),
                ("groups", "in", [group_company_manager_id]),
            ]
            self._set_record_values("ir.rule", domain, values)

    # low-level methods

    def _words2domain(self, do_if, words, model):
        words_list = words.split(" ")
        _assert_security_domain_words_and_order(words_list)
        ordered_words_list = _recursive_order_words(words_list)
        ordered_domain_list = [
            SECURITY_DOMAIN_WORD[word] for word in ordered_words_list
        ]
        domain_draft = "[{}]".format(", ".join(map(str, ordered_domain_list)))
        if model in COMPANY_FIELD:
            company_field = COMPANY_FIELD[model][do_if]
        else:
            company_field = COMPANY_FIELD["default"]
        domain = domain_draft.format(company_id=company_field)
        return domain

    def _update_rule_domains_to_1_where_false_except_partner(self):
        _logger.info("Starting _update_rule_domains_to_1_where_false_except_partner")
        ir_model_contact = self.env.ref("base.model_res_partner")
        rules = self.env["ir.rule"].search(
            [
                ("domain_force", "like", "company%False"),
                ("model_id", "!=", ir_model_contact.id),
            ]
        )
        for rule in rules:
            domain = rule.domain_force.strip("[] \n")
            domain_list = domain.split(",")
            false_in_domain_list = [
                count for count, str in enumerate(domain_list) if "False" in str
            ]
            for false_position in false_in_domain_list:
                look_for_company = false_position - 2
                if "'company_id'" in domain_list[look_for_company]:
                    domain_list[false_position] = domain_list[false_position].replace(
                        "False", "1"
                    )
                    new_domain = "[{}]".format(", ".join(domain_list))
                    rule.domain_force = new_domain

    def _update_code_to_comply_with_safe_eval(self):
        _logger.info("Starting _change_code_to_comply_with_safe_eval")
        xmlid_and_code_to_remove = [
            ("website.ir_actions_server_website_google_analytics", [".sudo()"]),
        ]
        for tup in xmlid_and_code_to_remove:
            xmlid, removes = tup
            try:
                action = self.env.ref(xmlid)
            except:
                continue
            for remove in removes:
                action.code = action.code.replace(remove, "")

    def _update_system_records(self):
        try:
            self.env.ref("mail.channel_all_employees").all_employees = True
        except:
            pass

    # TODO
    # def _get_and_fix_name_and_find_model_of_all_sql_views(self):
    #     # Get views
    #     self.env.cr.execute(
    # "select table_name from information_schema.views where table_schema = 'public';")
    #     views = [v[0] for v in self.env.cr.fetchall()]
    #     # Fix view names
    #     views_fixed = []
    #     for view in views:
    #         if view in IRREGULAR_SQL_VIEW_NAMES:
    #             views_fixed.append(IRREGULAR_SQL_VIEW_NAMES[view])
    #         else:
    #             views_fixed.append(view)
    #     # Check that all views correspond with a model of the same name
    #     models = [m.model.replace('.','_') for m in self.env['ir.model'].search([])]
    #     for view in views_fixed:
    #         if view not in models:
    #             raise UserError(
    # "There is no model corresponding with view '%s'! \n
    # Cancelling _get_and_fix_name_and_find_model_of_all_sql_views" % (view))

    #     return views_fixed
