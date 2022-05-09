from collections import defaultdict
import copy
import logging
from openupgradelib import openupgrade
import os

from odoo import models, fields, api, exceptions, SUPERUSER_ID
import odoo.addons.base.models.base as base
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# Module name for external IDs made with python.
# (Not in XML, so cannot be a module name.)
# Used for company_id fields, also in hooks.py.
EXTID_MODULE_NAME = '__multicompany_security__'

COMPANIES_MODEL = [
    'base_import.import', # Import write() compares company_id with stored user.company_id instead of context company_id.
]

COMPANY_READ_SYSTEM_MODEL = [
    'account.account.template',
    'account.account.type',
    'account.chart.template',
    'account.fiscal.position.template',
    'account.tax.template',
    'crm.team', # to avoid error: access_control() failed
    'ir.actions.act_url',
    'ir.actions.act_window',
    'ir.actions.act_window_close',
    'ir.actions.act_window.view',
    'ir.actions.actions',
    'ir.actions.client',
    'ir.actions.report',
    'ir.actions.server',
    'ir.actions.todo',
    'ir.attachment',
    'ir.filters',
    'ir.mail.server',
    'ir.model.data',
    'ir.module.module',
    'ir.translation', # temporarily disabled, see hardcoding below
    'ir.ui.menu',
    'ir.ui.view',
    'mail.template',
    'mis.report',
    'mis.report.kpi',
    'mis.report.kpi.expression',
    'mis.report.style',
    'mis.report.subreport',
    'res.field',                    # https://github.com/apps2grow/apps/tree/14.0/base_field_value
    'res.field.selection_value',    # https://github.com/apps2grow/apps/tree/14.0/base_field_value
    'res.partner', # to avoid error: access_control() failed
    'stock.location',
    'uom.uom',
    'website.menu',
]

NO_EDIT_MODEL = [
    # BASE, IR, RES
    'base.language.export',
    'base.language.import',
    'base.language.install',
    'base.module.uninstall',
    'base.module.update',
    'base.module.upgrade',
    'base.update.translations',
    'ir.cron',
    'ir.logging',
    'ir.model',
    'ir.model.access',
    'ir.model.constraint',
    'ir.model.fields',
    'ir.model.relation',
    'ir.module.category',
    'ir.module.module',
    'ir.module.module.dependency',
    'ir.module.module.exclusion',
    'ir.rule',
    'ir.server.object.lines',
    'mail.message.subtype',
    'res.bank',
    'res.country',
    'res.country.state',
    'res.country.group',
    'res.currency',
    'res.groups',
    'res.lang',
    'res.partner.industry',
    'res.request.link',
    # APPS
    'account.payment.method',
    'account.tax.group',
    'l10n_no_payroll.tabelltrekk',
    'mail.activity.type',
    'payment.icon',
    'report.layout',
    'report.paperformat',
    'uom.category',
    'web_tour.tour',
    'wizard.ir.model.menu.create',
]

NO_ACCESS_MODEL = [
    'ir.config_parameter',
    'res.config',
    'res.config.installer',
    'res.config.settings',
]

# TODO: _get_and_fix_name_and_find_model_of_all_sql_views (see code in the bottom)
IRREGULAR_SQL_VIEW_NAMES = {
    # 'view_name': 'model_name',
}

SECURITY_DOMAIN_WORD = {
    '(': 'BEGIN',
    ')': 'END',
    'AND': "'&'",
    'OR': "'|'",
    'false': "('{company_id}','=',False)",
    'in_companies': "('{company_id}','in',company_ids)",
    'in_companies/parent/child': "'|',('{company_id}','in',company_ids),'|',('{company_id}','parent_of',company_ids),('{company_id}','child_of',company_ids)",
    'in_company': "('{company_id}','=',company_id)",
    'in_company/parent/child': "'|',('{company_id}','=',company_id),'|',('{company_id}','parent_of',company_id),('{company_id}','child_of',company_id)",
    'system_company': "('{company_id}','=',1)",
    'company_ids_in_company_ids': "('company_ids','in',company_ids)",
    'user_id': "('user_id','=', user.id)",
}

COMPANY_FIELD = {
    'res.company': {
        'read_if': 'id',
        'edit_if': 'id',
    },
    'default': 'company_id',
}

"""
All records which a user can browse, are available on relational fields when the user is creating or editing a record.
A user may lose access to a record by setting another user as the owner.
If a manager can read another company than his own companies, the manager can switch to this company.
This is a security risk (specially for parent/child).
"""
SECURITY_RULE = {
    # It should be ok to have 'in_company' without 'in_companies'
    # since a user's company should always be one of the user's companies.
    # But it feels safer to include 'in_companies'.

    'BUS_PRESENCE_MODEL': {
        'edit_if': 'user_id',
    },
    # A company manager can change to any company which he/she can browse. Don't allow changing to parent/child company.
    'RES_COMPANY_MODEL': {
        'read_if': 'in_companies',
        'edit_if': 'in_company AND in_companies',
    },
    # read partners of users with access to the company, otherwise cannot read the users
    'RES_PARTNER_MODEL': {
        'read_if': 'company_ids_in_company_ids OR in_companies/parent/child',
        'edit_if': 'in_company AND in_companies',
    },
    # read users with access to the company
    'RES_USERS_MODEL': {
        'read_if': 'company_ids_in_company_ids',
        'edit_if': 'in_company AND in_companies',
    },
    'COMPANIES_MODEL': {
        'read_if': 'in_companies/parent/child',
        'edit_if': 'in_companies',
    },
    # default
    'COMPANY_MODEL': {
        'read_if': 'in_companies/parent/child',
        'edit_if': 'in_company AND in_companies',
    },
    'COMPANY_READ_SYSTEM_MODEL': {
        'read_if': 'system_company OR in_companies/parent/child',
        'edit_if': 'in_company AND in_companies',
    },
    'NO_EDIT_MODEL': {
        'edit_if': 'system_company AND ( in_company AND in_companies )',
    },
    'NO_ACCESS_MODEL': {
        'read_and_edit_if': 'system_company AND ( in_company AND in_companies )',
    },
}

SECURITY_DO_IF = {
    'read_if': {
        'perm_read': True,
        'perm_write': False,
        'perm_create': False,
        'perm_unlink': False,
    },
    'edit_if': {
        'perm_read': False,
        'perm_write': True,
        'perm_create': True,
        'perm_unlink': True,
    },
    'read_and_edit_if': {
        'perm_read': True,
        'perm_write': True,
        'perm_create': True,
        'perm_unlink': True,
    },
    'write_if': {
        'perm_read': False,
        'perm_write': True,
        'perm_create': False,
        'perm_unlink': False,
    },
    'create_if': {
        'perm_read': False,
        'perm_write': False,
        'perm_create': True,
        'perm_unlink': False,
    },
    'unlink_if': {
        'perm_read': False,
        'perm_write': False,
        'perm_create': False,
        'perm_unlink': True,
    },
}

def _get_security_type(model_name):
    if model_name == 'bus.presence':
        return 'BUS_PRESENCE_MODEL'
    elif model_name == 'res.company':
        return 'RES_COMPANY_MODEL'
    elif model_name == 'res.partner':
        return 'RES_PARTNER_MODEL'
    elif model_name == 'res.users':
        return 'RES_USERS_MODEL'
    elif model_name in NO_ACCESS_MODEL:
        return 'NO_ACCESS_MODEL'
    elif model_name in NO_EDIT_MODEL:
        return 'NO_EDIT_MODEL'
    elif model_name in COMPANY_READ_SYSTEM_MODEL:
        return 'COMPANY_READ_SYSTEM_MODEL'
    elif model_name in COMPANIES_MODEL:
        return 'COMPANIES_MODEL'
    else:
        return 'COMPANY_MODEL'

def _assert_security_domain_words_and_order(words_list):
    type = ''
    last_type = ''
    parenthesis_counter = 0
    first = 0
    last = len(words_list) - 1
    for count, word in enumerate(words_list):
        assert word in SECURITY_DOMAIN_WORD, word + " not in " + str(words_list)

        if word == '(':
            type = 'parenthesis'
            parenthesis_counter += 1
        elif word == ')':
            type = 'parenthesis'
            parenthesis_counter -= 1
        elif word in ('AND', 'OR'):
            type = 'operator'
        else:
            type = 'expression'

        assert parenthesis_counter >= 0
        assert type != last_type

        if count in (first, last):
            assert type in ('parenthesis', 'expression')

    # There should be max one operator type inside a parenthesis.
    # This assert is done in the _recursive_order_words method.

def _recursive_order_words(words_list):
    words_sub_list = {}
    parenthesis_counter = 0
    operator = ''
    last_operator = ''
    for word in words_list:
        if word == '(':
            if parenthesis_counter > 0:
                words_sub_list[parenthesis_counter].append(word)
            parenthesis_counter += 1
        elif word == ')':
            parenthesis_counter -= 1
            if parenthesis_counter > 0:
                words_sub_list[parenthesis_counter].append(word)
            else:
                words_sub_list.setdefault(parenthesis_counter, []).append(_recursive_order_words(words_sub_list[1]))
                words_sub_list[1] = []
                last_operator = ''
        else:
            if word in ('AND', 'OR'):
                operator = word
                assert (operator == last_operator) or (not last_operator)
            words_sub_list.setdefault(parenthesis_counter, []).append(word)
    words_sub_dict = {}
    for count, word in enumerate(words_sub_list[0]):
        if count % 2 == 0:
            words_sub_dict[count+1] = word
        else:
            words_sub_dict[count-1] = word
    ordered_words_list = []
    for count in range(0, len(words_sub_dict) + 1):
        if count in words_sub_dict:
            if type(words_sub_dict[count]) is list:
                ordered_words_list.extend(words_sub_dict[count])
            else:
                ordered_words_list.append(words_sub_dict[count])
    return ordered_words_list


class MulticompanySecurity(models.AbstractModel):
    _name = 'multicompany.security'
    _description = 'Force security between companies'

    def _register_hook(self, update_module=False):
        if update_module:
            true = ('1', 't', 'true', 'True')
            param = self.env['ir.config_parameter'].get_param('multicompany_base.force_security')
            if param in true:
                self.secure()
            # secure before configure
            param = self.env['ir.config_parameter'].get_param('multicompany_base.force_config')
            if param in true:
                self.env['multicompany.config'].configure_system_and_all_companies()

    # main methods

    def secure(self):
        # Returning an error value to _register_hook will be ignored (see loading.py).
        if not self.env.user.has_group('base.group_system'):
            return False
        # Takes a long time if there are many records without company_id
        self._set_company_id_where_null()
        self._update_rule_domains_to_1_where_false_except_partner()
        self._set_global_security_rules_on_all_models_except_ir_rule_and_ir_translation()
        self._update_code_to_comply_with_safe_eval()
        self._update_system_records()
        return True

    def set_company_manager_security(self):
        # So time consuming. Takes 23 seconds, while global rules take 5 seconds to update.
        self._set_read_and_edit_access_to_company_manager()

    def _set_global_security_rules_on_all_models_except_ir_rule_and_ir_translation(self):
        _logger.info('Starting _set_global_security_rules_on_all_models_except_ir_rule_and_ir_translation')
        models = self.env['ir.model'].search([('model', '!=', 'ir.rule'), ('model', '!=', 'ir.translation')])
        for model in models:
            SECURITY_TYPE = _get_security_type(model.model)
            for do_if, domain_words in SECURITY_RULE[SECURITY_TYPE].items():
                values = copy.deepcopy(SECURITY_DO_IF[do_if])
                values['groups'] = []
                values['model_id'] = model.id
                values['domain_force'] = self._words2domain(do_if=do_if, words=domain_words, model=model.model)
                values['name'] = '{model} - {security_type}, {do_if}'.format(
                    model=model.model, security_type=SECURITY_TYPE.lower(), do_if=do_if
                )
                domain = [('name', '=', values['name']), ('model_id', '=', values['model_id']), ('global', '=', True)]
                xmlid_name = '{model}_global_{do}_rule'.format(
                    model=model.model.replace('.','_'),
                    do=do_if[:-3],
                )
                self._set_record_values('ir.rule', domain, values, xmlid_name)

    def _set_read_and_edit_access_to_company_manager(self):
        # Read and edit access on models with company data.
        # Read access on NO_EDIT_MODELs.
        _logger.info('Starting _set_read_and_edit_access_to_company_manager')
        group_company_manager_id = self.env.ref('multicompany_base.group_company_manager').id
        models_to_exclude = NO_ACCESS_MODEL + ['ir.rule']
        models = self.env['ir.model'].search([('model', 'not in', models_to_exclude)])
        for model in models:
            if model.model in NO_EDIT_MODEL:
                security_do_if = 'read_if'
            else:
                security_do_if = 'read_and_edit_if'
            # ir.model.access
            values = copy.deepcopy(SECURITY_DO_IF[security_do_if])
            values['group_id'] = group_company_manager_id
            values['model_id'] = model.id
            values['name'] = '{model} - company manager, {security_do_if}'.format(model=model.model, security_do_if=security_do_if)
            domain = [('name', '=', values['name']), ('model_id', '=', values['model_id']), ('group_id', '=', values['group_id'])]
            xmlid_name = '{model}_company_manager_access'.format(
                model=model.model.replace('.','_'),
            )
            self._set_record_values('ir.model.access', domain, values, xmlid_name)
            # ir.rule
            if model.model in NO_EDIT_MODEL:
                # only system records, no need for company rule
                continue
            values = copy.deepcopy(SECURITY_DO_IF['read_and_edit_if'])
            values['groups'] = [(4, group_company_manager_id), 0]
            values['model_id'] = model.id
            values['domain_force'] = "[(1, '=', 1)]"
            values['name'] = '{model} - company manager'.format(model=model.model)
            domain = [('name', '=', values['name']), ('model_id', '=', values['model_id']), ('groups', 'in', [group_company_manager_id])]
            xmlid_name = '{model}_company_manager_rule'.format(
                model=model.model.replace('.','_'),
            )
            self._set_record_values('ir.rule', domain, values, xmlid_name)

    # low-level methods

    def _words2domain(self, do_if, words, model):
        words_list = words.split(' ')
        _assert_security_domain_words_and_order(words_list)
        ordered_words_list = _recursive_order_words(words_list)
        ordered_domain_list = [SECURITY_DOMAIN_WORD[word] for word in ordered_words_list]
        domain_draft = "[{}]".format(', ' . join(map(str, ordered_domain_list)))
        if model in COMPANY_FIELD:
            company_field = COMPANY_FIELD[model][do_if]
        else:
            company_field = COMPANY_FIELD['default']
        domain = domain_draft.format(company_id=company_field)
        return domain

    def _set_record_values(self, model_name, domain, values, xmlid_name=None):
        record = self.env[model_name].search(domain)
        if len(record) > 1:
            record = self._deduplicate_or_log_critical_error(domain, record, values.keys())

        if type(record) is ValueError:
            pass
        elif len(record) == 0:
            new_record = self.env[model_name].create(values)
            # Is this important? Rather save time
            # if xmlid_name:
            #     self._create_external_id(new_record, xmlid_name)
        elif len(record) == 1:
            old_values = record.read(fields=values.keys())
            old_values = self._delele_id_and_replace_tuple_with_first_tuple_item(old_values)
            old_values_and_new_values = old_values
            old_values_and_new_values.append(values)
            if not self._values_are_equal(old_values_and_new_values):
                record.write(values)

    def _deduplicate_or_log_critical_error(self, model_search_domain, records, field_names_which_should_have_same_record_values):
        model_name = records[0]._name
        log_critical = False
        list_of_values = records.read(fields=field_names_which_should_have_same_record_values)
        list_of_values = self._delele_id_and_replace_tuple_with_first_tuple_item(list_of_values)
        if not self._values_are_equal(list_of_values):
            log_critical = True
        if not log_critical:
            # Deduplicate ...
            record_ids = records.ids
            record_to_keep = records.browse(record_ids.pop(0))
            records.browse(record_ids).unlink()
            return record_to_keep
        else:
            # ... or log a critical error.
            error_msg = 'company.security deduplicate: There are {count} conflicting records of model {model_name}. Domain: "{domain}". Conflicing fields: "{fields}".'.format(
                count=len(records), model_name=model_name, domain=model_search_domain, fields=field_names_which_should_have_same_record_values
            )
            _logger.critical(error_msg)
            return ValueError(error_msg)

    def _delele_id_and_replace_tuple_with_first_tuple_item(self, list_of_dict):
        for dict in list_of_dict:
            if 'id' in dict:
                del dict['id']
            for key, value in dict.items():
                if type(value) is tuple:
                    dict[key] = value[0]
        return list_of_dict

    def _values_are_equal(self, list_of_values):
        for values in list_of_values:
            if values != list_of_values[0]:
                return False
        return True

    def _create_external_id(self, record, xmlid_name):
        xmlid_record = self.env['ir.model.data'].search([('module','=',EXTID_MODULE_NAME), ('name','=',xmlid_name)])
        if xmlid_record:
            if xmlid_record.model != record._name or xmlid_record.res_id != record.id:
                _logger.warning("xmlid {module}.{name} already exists with model {model}, res_id {res_id}!".format(
                    module=EXTID_MODULE_NAME,
                    name=xmlid_name,
                    model=xmlid_record.model,
                    res_id=xmlid_record.res_id,
                ))
        else:
            self.env['ir.model.data'].create({
                'module': EXTID_MODULE_NAME,
                'name': xmlid_name,
                'model': record._name,
                'res_id': record.id
            })

    def _set_company_id_where_null(self):
        _logger.info('Starting _set_company_id_where_null')

        all_models = self.env['ir.model'].search([])
        for model in all_models:
            if not self.env[model.model]._auto:
                continue
            if model.model == 'ir.model.fields':
                sql = "UPDATE {} SET company_id = 1 WHERE company_id IS NULL;".format(model.model.replace('.','_'))
                self.env.cr.execute(sql)
                continue

            records_with_no_company = self.env[model.model].with_context(active_test=False,).sudo().search([('company_id', '=', False)])
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
            #     records_with_no_company.sudo().write({'company_id': self.env.company.id})
            #     continue

            # relation_field = self.env[model.model]._fields[relation_field_name]
            # if relation_field.type == 'many2one_reference':
            #     relation_model_names = set(records_with_no_company.mapped(relation_field.model_field))
            #     for relation_model_name in relation_model_names:
            #         records_filtered_model = records_with_no_company.filtered(lambda r: getattr(r, relation_field.model_field) == relation_model_name)
            #         relation_ids = list(set(records_filtered_model.mapped(relation_field_name)))
            #         relations = self.env[relation_model_name].browse(relation_ids)
            #         for relation in relations:
            #             related_company = relation.company_id
            #             records_filtered = records_filtered_model.filtered(lambda r: getattr(r, relation_field_name) == relation.id)
            #             records_filtered.sudo().write({'company_id': related_company.id})
            # else:
            #     relations = records_with_no_company.mapped(relation_field_name)
            #     for relation in relations:
            #         related_company = relation.company_id
            #         records_filtered = records_with_no_company.filtered(lambda r: getattr(r, relation_field_name) == relation.id)
            #         records_filtered.sudo().write({'company_id': related_company.id})

            # C) Another way to loop

            related_field_name = base.FIELD_NAME_TO_GET_COMPANY.get(model.model)
            if not related_field_name:
                records_with_no_company.sudo().write({'company_id': self.env.company.id})
                continue

            related_field = self.env[model.model]._fields[related_field_name]
            related_models_and_record_ids = defaultdict(lambda: []) # {'res.partner': [(1001, 1), (1002, 2), (1003, 3)]}
            for record in records_with_no_company:
                [(related_model_name, related_record_id)] = base._get_model_name_and_res_id(related_field, record)
                if related_model_name and related_record_id:
                    related_models_and_record_ids[related_model_name].append((record.id, related_record_id))

            for related_model_name, ids in related_models_and_record_ids.items():

                related_record_ids =  [tup[1] for tup in ids if tup[1]]
                related_records = self.env[related_model_name].sudo().browse(related_record_ids)
                related_companies = related_records.mapped('company_id')
                for related_company in related_companies:
                    related_records_with_this_company = related_records.filtered(lambda r: r.company_id == related_company)
                    update_record_ids = [tup[0] for tup in ids if tup[1] in related_records_with_this_company.ids]
                    # Option 1
                    # records_with_no_company.filtered(lambda r: id in update_record_ids).sudo().write({'company_id': related_company.id})
                    # Option 2
                    self.env[model.model].sudo().browse(update_record_ids).write({'company_id': related_company.id})

                record_ids_with_no_related_record = [tup[0] for tup in ids if not tup[1]]
                # Option 1
                # records_with_no_company.filtered(lambda r: id in record_ids_with_no_related_record).sudo().write({'company_id': self.env.company.id})
                # Option 2
                self.env[model.model].sudo().browse(record_ids_with_no_related_record).write({'company_id': self.env.company.id})

    def _update_rule_domains_to_1_where_false_except_partner(self):
        _logger.info('Starting _update_rule_domains_to_1_where_false_except_partner')
        ir_model_contact = self.env.ref('base.model_res_partner')
        rules = self.env['ir.rule'].search([('domain_force', 'like', 'company%False'), ('model_id', '!=', ir_model_contact.id)])
        for rule in rules:
            domain = rule.domain_force.strip('] [')
            domain_list = domain.split(',')
            false_in_domain_list = [count for count, str in enumerate(domain_list) if 'False' in str]
            for false_position in false_in_domain_list:
                look_for_company = false_position - 2
                if "'company_id'" in domain_list[look_for_company]:
                    domain_list[false_position] = domain_list[false_position].replace('False', '1')
                    new_domain = "[{}]".format(', '.join(domain_list))
                    rule.domain_force = new_domain

    def _update_code_to_comply_with_safe_eval(self):
        _logger.info('Starting _change_code_to_comply_with_safe_eval')
        xmlid_and_code_to_remove = [
            ('website.ir_actions_server_website_google_analytics', ['.sudo()']),
        ]
        for tup in xmlid_and_code_to_remove:
            xmlid, removes = tup
            try:
                action = self.env.ref(xmlid)
            except:
                continue
            for remove in removes:
                action.code = action.code.replace(remove, '')

    def _update_system_records(self):
        try:
            self.env.ref('mail.channel_all_employees').all_employees = True
        except:
            pass

    # TODO
    # def _get_and_fix_name_and_find_model_of_all_sql_views(self):
    #     # Get views
    #     self.env.cr.execute("select table_name from information_schema.views where table_schema = 'public';")
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
    #             raise UserError("There is no model corresponding with view '%s'! \n Cancelling _get_and_fix_name_and_find_model_of_all_sql_views" % (view))

    #     return views_fixed
