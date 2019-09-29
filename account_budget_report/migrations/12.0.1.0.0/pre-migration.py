# Copyright 2019 Apps2GROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade
import psycopg2
import logging
logger = logging.getLogger('OpenUpgrade')

# model, new_module
models_to_update = [
    ('crossovered.budget', 'account_budget_report'),
]

xmlids_to_delete = [
    'account_budget_report.report_invoice_document',
]

# update ir.model.data, ir.model.contraint, ir.model.relation, ir.translation
def update_models(cr, models_to_update):
    for model, new_module in models_to_update:
        table = model.replace('.', '_')

        commands = [
            "update ir_model_data set module = '%s' where model = 'ir.model.fields' and name like '%s';" % (new_module, 'field_' + table + '_%'),
            #"update ir_model_data set module = '%s' where model = 'ir.model' and name = 'model_%s';" % (new_module, table),
            #"update ir_model_constraint set module = (select id from ir_module_module where name = '%s') where model = (select id from ir_model where model = '%s');" % (new_module, model),
            #"update ir_model_relation set module = (select id from ir_module_module where name = '%s') where model = (select id from ir_model where model = '%s');" % (new_module, model),
        ]
        execute_commands(cr, commands)

def execute_commands(cr, commands):
    for command in commands:
        try:
            #cr.execute(command)
            openupgrade.logged_query(cr, command)
        except (psycopg2.ProgrammingError, psycopg2.IntegrityError) as e:
            logger.warning(str(e))


@openupgrade.migrate()
def migrate(env, version):
    update_models(env.cr, models_to_update)
    openupgrade.delete_records_safely_by_xml_id(env, xmlids_to_delete)