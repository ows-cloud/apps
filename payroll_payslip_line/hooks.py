from openupgradelib import openupgrade

from odoo import SUPERUSER_ID, api

fields_to_add = [
    ('net_quantity', 'hr.payslip.line', 'hr_payslip_line', 'integer', 'int4', 'base'),
    ('net_rate', 'hr.payslip.line', 'hr_payslip_line', 'integer', 'int4', 'base'),
    ('net_amount', 'hr.payslip.line', 'hr_payslip_line', 'integer', 'int4', 'base'),
    ('net_total', 'hr.payslip.line', 'hr_payslip_line', 'integer', 'int4', 'base'),
]

sql_to_update_fields = """
    UPDATE hr_payslip_line l
    SET
        net_quantity = l.quantity * (CASE WHEN p.credit_note THEN -1 ELSE 1 END),
        net_rate = l.rate * (CASE WHEN p.credit_note THEN -1 ELSE 1 END),
        net_amount = l.amount * (CASE WHEN p.credit_note THEN -1 ELSE 1 END),
        net_total = l.total * (CASE WHEN p.credit_note THEN -1 ELSE 1 END)
    FROM hr_payslip p
    WHERE l.slip_id = p.id;
"""

def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # openupgrade.add_fields(env, fields_to_add)
    # openupgrade.logged_query(cr, sql_to_update_fields)
