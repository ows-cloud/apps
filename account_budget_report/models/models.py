# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo import tools
from odoo.exceptions import UserError
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import pandas as pd
from io import StringIO

_logger = logging.getLogger(__name__)


# copied from https://github.com/odoo/odoo/blob/11.0/addons/account_budget/models/account_budget.py
class CrossoveredBudget(models.Model):
    _name = "crossovered.budget"
    _description = "Budget"
    #_inherit = ['mail.thread']

    name = fields.Char('Budget Name', required=True, states={'done': [('readonly', True)]})
    creating_user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user)
    date_from = fields.Date('Start Date', required=True, states={'done': [('readonly', True)]})
    date_to = fields.Date('End Date', required=True, states={'done': [('readonly', True)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('cancel', 'Cancelled'),
        ('confirm', 'Confirmed'),
        ('validate', 'Validated'),
        ('done', 'Done')
        ], 'Status', default='draft', index=True, required=True, readonly=True, copy=False)
    #crossovered_budget_line = fields.One2many('crossovered.budget.lines', 'crossovered_budget_id', 'Budget Lines',
    #    states={'done': [('readonly', True)]}, copy=True)
    company_id = fields.Many2one('res.company', 'Company', required=True,
        default=lambda self: self.env['res.company']._company_default_get('account.budget.post'))

    def action_budget_confirm(self):
        self.write({'state': 'confirm'})

    def action_budget_draft(self):
        self.write({'state': 'draft'})

    def action_budget_validate(self):
        self.write({'state': 'validate'})

    def action_budget_cancel(self):
        self.write({'state': 'cancel'})

    def action_budget_done(self):
        self.write({'state': 'done'})


class AccountBudgetLine(models.Model):
    _name = 'account.budget.line'

    @api.model
    def _compute_analytic_domain(self):
        if self.env.user.has_group('account.group_account_manager'):
            return []
        else:
            return [('user_id','=',self.env.user.id)]

    account_id = fields.Many2one('account.account', string='Account')
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', domain=_compute_analytic_domain)
    balance = fields.Monetary('Balance')
    balance_history = fields.Char('Balance History', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', index=True,
                                 default=lambda self: self.env.user.company_id)
    crossovered_budget_id = fields.Many2one('crossovered.budget', string='Budget')
    currency_id = fields.Many2one('res.currency', string='Currency')
    date = fields.Date(string='Date')
    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Partner')
    product_id = fields.Many2one('product.product', string='Product')
    user_id = fields.Many2one('res.users', string="User")

    @api.model
    def create(self, values):
        for field in ['accounting_or_budget', 'journal_id', 'move_id']:
            values.pop(field, None)
        if values.get('crossovered_budget_id'):
            date = values['date'] if values and 'date' in values else False
            budget = self.env['crossovered.budget'].browse(values['crossovered_budget_id'])
            self._check_date(date, budget)
        return super(AccountBudgetLine, self).create(values)

    def write(self, values):
        for field in ['accounting_or_budget', 'journal_id', 'move_id']:
            values.pop(field, None)
        for record in self:
            budget = record.crossovered_budget_id
            if values and 'crossovered_budget_id' in values:
                budget = self.env['crossovered.budget'].browse(values['crossovered_budget_id']) if values.get('crossovered_budget_id') else None
            if budget:
                date = values['date'] if values and 'date' in values else record.date
                self._check_date(date, budget)

            if 'balance' in values:
                if not record.balance_history:
                    values['balance_history'] = '%.2f' % record.balance
                else:
                    values['balance_history'] = record.balance_history + ', ' + '%.2f' % record.balance

        return super(AccountBudgetLine, self).write(values)

    @api.model
    def _check_date(self, date, crossovered_budget_id):
        lock_date = crossovered_budget_id and crossovered_budget_id.date_to or False
        if date <= (lock_date):
            message = _(
                "You cannot add/modify budget lines prior to and inclusive of the end date %s of the budget.") % (
                          lock_date)
            raise UserError(message)

    @api.model
    def replace_budget_lines_next_year(self, records):
        change_date = relativedelta(years=1, day=1)
        self._replace_budget_lines(records, change_date)

    @api.model
    def replace_budget_lines_next_11_months(self, records):
        for i in range(11):
            change_date = relativedelta(months=i + 1)
            self._replace_budget_lines(records, change_date)

    @api.model
    def replace_budget_lines_tomorrow(self, records):
        change_date = relativedelta(days=1)
        self._replace_budget_lines(records, change_date)

    @api.model
    def _replace_budget_lines(self, records, change_date):
        # change_date: relativedelta

        csv = 'date,account_id,analytic_account_id,crossovered_budget_id,balance\n'
        for record in records:
            budget_date = (datetime.strptime(record.date, '%Y-%m-%d') + change_date).strftime('%Y-%m-%d')
            csv += ','.join([budget_date, str(record.account_id.id), str(record.analytic_account_id.id),
                             str(record.crossovered_budget_id.id), str(record.balance)]) + '\n'

        # Group and aggregate the records with pandas DataFrame
        df = pd.read_csv(StringIO(csv)).groupby(['date', 'account_id', 'analytic_account_id', 'crossovered_budget_id'])[
            'balance'].sum()

        # Replace budget lines
        abl = self.env['account.budget.line']
        for index, balance in df.items():
            name = datetime.now().strftime('%Y-%m-%d') + " " + self.env.user.name
            abl.search([('date', '=', index[0]), ('account_id', '=', index[1]), ('analytic_account_id', '=', index[2]),
                         ('crossovered_budget_id', '=', index[3])]).unlink()
            abl.create({'date': index[0], 'account_id': index[1], 'analytic_account_id': index[2],
                         'crossovered_budget_id': index[3],
                         'balance': balance, 'name': name})


# VIEW depends on account.budget.line
class AccountBudgetReport(models.Model):
    _name = "account.budget.report"
    _auto = False

    @api.model
    def _compute_analytic_domain(self):
        if self.env.user.has_group('account.group_account_manager'):
            return []
        else:
            return [('user_id','=',self.env.user.id)]
    
    account_id = fields.Many2one('account.account', string='Account', store=True)
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', store=True, domain=_compute_analytic_domain)
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
    currency_id = fields.Many2one('res.currency', string='Currency', store=True)
    date = fields.Date(string='Date', store=True)
    journal_id = fields.Many2one('account.journal', string='Journal', store=True)
    move_id = fields.Many2one('account.move', string='Journal Entry', store=True)
    name = fields.Char(string='Name', store=True)
    partner_id = fields.Many2one('res.partner', string='Partner', store=True)
    product_id = fields.Many2one('product.product', string='Product', store=True)
    user_type_id = fields.Many2one('account.account.type', string='Account Type', store=True)

    analytic_group_id = fields.Many2one('account.analytic.group', string='Analytic Group', store=True)
    analytic_user_id = fields.Many2one('res.users', string='Analytic Manager', store=True)
    include_initial_balance = fields.Boolean('Bring Accounts Balance Forward', store=True)

    day = fields.Integer('Day', store=True)
    week = fields.Integer('Week', store=True)
    month = fields.Integer('Month', store=True)
    quarter = fields.Integer('Quarter', store=True)
    year = fields.Integer('Year', store=True)
    
    accounting_or_budget = fields.Selection(selection=[('accounting', 'Accounting'),('budget','Budget')], string='Source', store=True)
    crossovered_budget_id = fields.Many2one('crossovered.budget', string='Budget', store=True)
    
    balance_history = fields.Char('History(raw)', readonly=True, store=True)
    balance = fields.Monetary('Acc+Bud(raw)', store=True)
    balance_minus_budget = fields.Monetary('Acc-Bud(raw)', store=True)
    balance2 = fields.Monetary('Acc+Bud', store=True)
    balance2_minus_budget = fields.Monetary('Acc-Bud', store=True)
    
    def init(self):
        tools.drop_view_if_exists(self._cr, 'account_budget_report')
        self._cr.execute("""
            CREATE OR REPLACE VIEW account_budget_report AS
             SELECT -t0.id AS id, -- NB! Must be different from budget id!
                'accounting' AS accounting_or_budget,
                null AS crossovered_budget_id,
                t0.account_id,
                t0.analytic_account_id,
                null AS balance_history,
                t0.balance,
                t0.balance AS balance_minus_budget,
                -t0.balance AS balance2,
                -t0.balance AS balance2_minus_budget,
                t0.company_id,
                t0.currency_id,
                t0.date,
                date_part('day', t0.date) AS day,
                date_part('week', t0.date) AS week,
                date_part('month', t0.date) AS month,
                date_part('quarter', t0.date) AS quarter,
                date_part('year', t0.date) AS year,
                t0.journal_id,
                t0.move_id,
                t0.name,
                t0.partner_id,
                t0.product_id,
                t1.user_type_id AS user_type_id,
                t2.include_initial_balance AS include_initial_balance,
                t3.group_id AS analytic_group_id,
                t3.user_id AS analytic_user_id
               FROM account_move_line t0
                LEFT JOIN account_account t1 ON t0.account_id = t1.id 
                LEFT JOIN account_account_type t2 ON t1.user_type_id = t2.id
                LEFT JOIN account_analytic_account t3 ON t0.analytic_account_id = t3.id
             UNION
             SELECT t0.id,
                t4.name AS accounting_or_budget,
                t0.crossovered_budget_id,
                t0.account_id,
                t0.analytic_account_id,
                t0.balance_history,
                t0.balance,
                -t0.balance,
                -t0.balance,
                t0.balance,
                t0.company_id,
                t0.currency_id,
                t0.date,
                date_part('day', t0.date),
                date_part('week', t0.date),
                date_part('month', t0.date),
                date_part('quarter', t0.date),
                date_part('year', t0.date),
                null AS journal_id,
                null AS move_id,
                t0.name,
                t0.partner_id,
                t0.product_id,
                t1.user_type_id AS user_type_id,
                t2.include_initial_balance AS include_initial_balance,
                t3.group_id AS analytic_group_id,
                t3.user_id AS analytic_user_id
               FROM account_budget_line t0
                LEFT JOIN account_account t1 ON t0.account_id = t1.id 
                LEFT JOIN account_account_type t2 ON t1.user_type_id = t2.id
                LEFT JOIN account_analytic_account t3 ON t0.analytic_account_id = t3.id
                LEFT JOIN crossovered_budget t4 ON t0.crossovered_budget_id = t4.id;
            """)
    
    @api.model
    def create(self, values):
        # del values['accounting_or_budget'], values['journal_id'], values['move_id']
        return self.env['account.budget.line'].create(values)
        
    def write(self, values):
        return self.env['account.budget.line'].browse([id for id in self._ids if id > 0]).write(values)
        
    def unlink(self):  
        return self.env['account.budget.line'].browse([id for id in self._ids if id > 0]).unlink()
