from odoo import api, fields, models
from odoo.exceptions import UserError
from .tabelltrekk2021 import tabelltrekk2021 as tabelltrekk20xx
YEAR = 2021

import logging
_logger = logging.getLogger(__name__)

class Tabelltrekk(models.Model):
    _name = 'l10n_no_payroll.tabelltrekk'
    
    year = fields.Integer('Year')
    tabellnummer = fields.Char('Tabellnummer', size=4)
    trekkperiode = fields.Char('Trekkperiode', size=1)
    tabelltype = fields.Char('Tabelltype', size=1)
    trekkgrunnlag = fields.Integer('Trekkgrunnlag')
    trekk = fields.Integer('Trekk')
    
    def l10n_no_import_tax_deduction(self):
        year_exists = self.search([('year','=',YEAR)], limit=1)
        if not year_exists:
            lines = tabelltrekk20xx.splitlines()
            count = 0
            sql = sql_base = "INSERT INTO l10n_no_payroll_tabelltrekk (year, tabellnummer, trekkperiode, tabelltype, trekkgrunnlag, trekk) VALUES "
            for line in lines:
                sql += """
                    (%s, %s, %s, %s, %s, %s),""" % (YEAR, line[:4], line[4], line[5], line[6:][:5], line[11:][:5])
                    # execute sql[:-1] without the last comma
                count += 1
                if count >= 1000:
                    self.env.cr.execute(sql[:-1])
                    count = 0
                    sql = sql_base
            if sql != sql_base:
                self.env.cr.execute(sql[:-1])
            self.invalidate_cache()

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    def l10n_no_get_tax_deduction(self, year, trekkperiode, tabelltype, trekkgrunnlag, andel_av_trekk):
        #def l10n_no_get_tax_deduction(self, context, year=2018, trekkperiode='1', tabelltype='0', trekkgrunnlag=10000, andel_av_trekk=1):
        _logger.debug('l10n_no_get_tax_deduction')
        '''
        #year: Integer
        #trekkperiode: String [('1','maaned'),('2','14 dager'),('3','uke'),('4','4 dager'),('5','3 dager'),('6',2 dager'),('7','1 dag')]
        #tabelltype: String [('0','Loenn'),('1','Pensjon')]
        #trekkgrunnlag: Integer
        #andel_av_trekk: Float (halv skatt i desember)
        '''

        trekkprosent = self.env['res.field.value'].search(
            [('model','=','hr.employee'),('res_id','=',self.id),('field_code','=','l10n_no_trekkprosent')])
        if trekkprosent and trekkprosent.value:
            trekkprosent = float(trekkprosent.value) / 100.0
        else:
            trekkprosent = 0.0

        trekktabell = self.env['res.field.value'].search(
            [('model','=','hr.employee'),('res_id','=',self.id),('field_code','=','l10n_no_trekktabell')])
        if trekktabell and trekktabell.value:
            trekkgrunnlag = int(trekkgrunnlag / 100.0) * 100
            record = self.env['l10n_no_payroll.tabelltrekk'].search([('year','=',year),('tabellnummer','=',trekktabell.value),
                ('trekkperiode','=',trekkperiode),('tabelltype','=',tabelltype),('trekkgrunnlag','=',trekkgrunnlag)
            ], limit=1)
            if record:
                return -int(int(record.ensure_one().trekk) * andel_av_trekk)
            else:
                record = self.env['l10n_no_payroll.tabelltrekk'].search([
                    ('year','=',year),('tabellnummer','=',trekktabell.value),('trekkperiode','=',trekkperiode),('tabelltype','=',tabelltype)
                ], order='trekkgrunnlag DESC', limit=1)
                if trekkgrunnlag > record.trekkgrunnlag:
                    return -int( (record.trekk + (trekkgrunnlag - record.trekkgrunnlag) * trekkprosent) * andel_av_trekk)
                else:
                    return 0
        else:
            trekk = -int(trekkgrunnlag * trekkprosent * andel_av_trekk)
            return trekk
