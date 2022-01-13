import copy
import logging
from openupgradelib import openupgrade
import os

from odoo import models, fields, api, exceptions, SUPERUSER_ID

_logger = logging.getLogger(__name__)

# Module name for external IDs made with python.
# (Not in XML, so cannot be a module name.)
# Used for company_id fields, also in hooks.py.
EXTID_MODULE_NAME = '__multicompany_strict_security__'

COMPANIES_MODEL = [
    'res.company',
]

COMPANY_READ_SYSTEM_MODEL = [
    'account.account.type',
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
    'ir.translation',
    'ir.ui.menu',
    'ir.ui.view',
    'mail.template',
    'res.field',                    # https://github.com/apps2grow/apps/tree/14.0/base_field_value
    'res.field.selection_value',    # https://github.com/apps2grow/apps/tree/14.0/base_field_value
    'stock.location',
    'uom.uom',
]

READ_SYSTEM_MODEL = [
    # BASE, IR, RES
    'base.language.export',
    'base.language.import',
    'base.language.install',
    'base.module.uninstall',
    'base.module.update',
    'base.module.upgrade',
    'base.update.translations',
    'base_import.import',
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
    'res.bank',
    'res.config',
    'res.config.installer',
    'res.config.settings',
    'res.country',
    'res.country.state',
    'res.currency',
    'res.groups',
    'res.lang',
    'res.partner.industry',
    'res.request.link',
    # APPS
    'account.payment.method',
    'account.tax.group',
    'change.password.user',
    'change.password.wizard',
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
    'allowed_companies': "('{company_id}','in',company_ids)",
    'selected_company': "('{company_id}','=',company_id)",
    'selected_company/parent/child': "'|',('{company_id}','=',company_id),'|',('{company_id}','parent_of',company_id),('{company_id}','child_of',company_id)",
    'system_company': "('{company_id}','=',1)",
}

COMPANY_FIELD = {
    'res.company': {
        'read_if': 'id',
        'edit_if': 'id',
    },
    'res.users': {
        'read_if': 'company_ids',
        'write_if': 'company_ids', # if not company_id, write only name & lang & partner_id (???), see res_users.py
        'create_if': 'company_id',
        'unlink_if': 'company_id',
    },
    'default': 'company_id',
}

SECURITY_RULE = {
    # read user without partner
    'RES_PARTNER_MODEL': {
        'read_if': 'false OR ( allowed_companies AND selected_company/parent/child )',
        'edit_if': 'allowed_companies AND selected_company/parent/child',
    },
    # set user partner & language
    'RES_USERS_MODEL': {
        'read_if': 'allowed_companies',
        'write_if': 'allowed_companies',
        'create_if': 'allowed_companies AND selected_company/parent/child',
        'unlink_if': 'allowed_companies AND selected_company/parent/child',
    },
    'COMPANIES_MODEL': {
        'read_if': 'allowed_companies',
        'edit_if': 'allowed_companies AND selected_company/parent/child',
    },
    # default
    'COMPANY_MODEL': {
        'read_and_edit_if': 'allowed_companies AND selected_company/parent/child',
    },
    'COMPANY_READ_SYSTEM_MODEL': {
        'read_if': 'system_company OR ( allowed_companies AND selected_company/parent/child )',
        'edit_if': 'allowed_companies AND selected_company/parent/child',
    },
    'READ_SYSTEM_MODEL': {
        'read_if': 'system_company',
        'edit_if': 'system_company AND ( allowed_companies AND selected_company )',
    },
    'NO_ACCESS_MODEL': {
        'read_and_edit_if': 'system_company AND ( allowed_companies AND selected_company )',
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
    if model_name == 'res.partner':
        return 'RES_PARTNER_MODEL'
    elif model_name == 'res.users':
        return 'RES_USERS_MODEL'
    elif model_name in NO_ACCESS_MODEL:
        return 'NO_ACCESS_MODEL'
    elif model_name in READ_SYSTEM_MODEL:
        return 'READ_SYSTEM_MODEL'
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


class MulticompanyForceSecurity(models.AbstractModel):
    _name = 'multicompany.force.security'
    _description = 'Force security between companies'

    def _register_hook(self, update_module=False):
        if update_module:
            param = self.env['ir.config_parameter'].get_param('multicompany_force_security.force_security')
            if param in ('1', 't', 'true', 'True'):
                self.secure()
                _logger.info('multicompany.force.security done')

    # main methods

    def secure(self):
        # Returning an error value will be ignored (see loading.py).
        if not self.env.user.has_group('base.group_system'):
            return False
        self._set_global_security_rules_on_all_models_except_ir_rule()
        self._set_read_and_edit_access_to_company_manager_on_all_models_except_ir_rule()
        self._set_company_id_to_1_where_null()
        self._update_rule_domains_to_1_where_false()
        return True

    def _set_global_security_rules_on_all_models_except_ir_rule(self):
        models = self.env['ir.model'].search([('model', '!=', 'ir.rule')])
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

    def _set_read_and_edit_access_to_company_manager_on_all_models_except_ir_rule(self):
        group_company_manager_id = self.env.ref('multicompany_force_security.group_company_manager').id
        models = self.env['ir.model'].search([('model', '!=', 'ir.rule')])
        for model in models:
            # ir.model.access
            values = copy.deepcopy(SECURITY_DO_IF['read_and_edit_if'])
            values['group_id'] = group_company_manager_id
            values['model_id'] = model.id
            values['name'] = '{model} - company manager'.format(model=model.model)
            domain = domain = [('name', '=', values['name']), ('model_id', '=', values['model_id']), ('group_id', '=', values['group_id'])]
            xmlid_name = '{model}_company_manager_access'.format(
                model=model.model.replace('.','_'),
            )
            self._set_record_values('ir.model.access', domain, values, xmlid_name)
            # ir.rule
            values = copy.deepcopy(SECURITY_DO_IF['read_and_edit_if'])
            values['groups'] = [(4, group_company_manager_id), 0]
            values['model_id'] = model.id
            values['domain_force'] = "[(1, '=', 1)]"
            values['name'] = '{model} - company manager'.format(model=model.model)
            domain = domain = [('name', '=', values['name']), ('model_id', '=', values['model_id']), ('groups', 'in', [group_company_manager_id])]
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

    def _set_company_id_to_1_where_null(self):
        _logger.debug('set_company_id_to_1_where_null: start')
        self.env.cr.execute("SELECT t.table_name FROM information_schema.tables t INNER JOIN information_schema.columns c ON t.table_name = c.table_name WHERE t.table_type='BASE TABLE' AND c.column_name='company_id' ORDER BY table_name;")
        tables = self.env.cr.fetchall()
        _logger.debug('set_company_id_to_1_where_null: tables = ' + str(tables))
        for table in tables:
            sql = "UPDATE " + table[0] + " SET company_id = 1 WHERE company_id IS NULL;"
            self.env.cr.execute(sql)

        # TODO: set company_id correctly, not necessarily 1 on all records!
        #     records = env['ir.model.data'].search([('company_id', '=', None)])
        #     for record in records:
        #         company = record.reference.company_id
        #         record.write({'company_id': company.id})
        # class Rule(models.Model):
        #     _inherit = 'ir.rule'
        #     def post_init_hook(self):
        #         #env = api.Environment(cr, SUPERUSER_ID, {})
        #         records = self.env['ir.model.data'].search([('company_id', '=', None)])
        #         for record in records:
        #             #model, id = record.reference.split(',')
        #             real_record = self.env[record.model].search([('id', '=', record.res_id)])
        #             if real_record:
        #                 # company = self.env[model].browse(int(id)).company_id
        #                 record.write({'company_id': real_record.company_id.id})

    def _update_rule_domains_to_1_where_false(self):
        rules = self.env['ir.rule'].search([('domain_force', 'like', 'company%False')])
        for rule in rules:
            domain = rule.domain_force.strip('] [')
            domain_list = domain.split(',')
            false_in_domain_list = [count for count, str in enumerate(domain_list) if 'False' in str]
            for false_position in false_in_domain_list:
                look_for_company = false_position - 2
                if 'company' in domain_list[look_for_company]:
                    domain_list[false_position] = domain_list[false_position].replace('False', '1')
                    new_domain = "[{}]".format(', '.join(domain_list))
                    rule.domain_force = new_domain


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
