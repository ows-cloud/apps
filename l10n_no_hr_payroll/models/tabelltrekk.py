from odoo import api, fields, models
from odoo.exceptions import UserError
from .tabelltrekk2019 import tabelltrekk2019

# 2018: url to download from Skatteetaten
# 2019: tabelltrekk2019.py (new environment with no direct access to the internet)
# Useful to download from url:
# from urllib.request import urlopen
# from io import StringIO

import logging
_logger = logging.getLogger(__name__)

class Tabelltrekk(models.Model):
    _name = 'l10n_no_hr_payroll.tabelltrekk'
    
    year = fields.Integer('Year')
    tabellnummer = fields.Char('Tabellnummer', size=4)
    trekkperiode = fields.Char('Trekkperiode', size=1)
    tabelltype = fields.Char('Tabelltype', size=1)
    trekkgrunnlag = fields.Integer('Trekkgrunnlag')
    trekk = fields.Integer('Trekk')
    
    def l10n_no_import_tax_deduction(self):
        filename = "tabelltrekk2019.txt"
        years = [
            {
                'year': 2019,
                'url': 'https://www.skatteetaten.no/contentassets/135c4f9318684c5ab87704641a4ab078/trekktabeller_2019.zip',
            },
        ]

        for year_dict in years:
            url = year_dict['url']
            year_exists = self.search([('year','=',year_dict['year'])], limit=1)
            if not year_exists:
                #response = urlopen(url)
                #compressedFile = StringIO()
                #compressedFile.write(response.read())
                #compressedFile.seek(0)
                #decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
                #lines = decompressedFile.read().splitlines()
                lines = tabelltrekk2019.splitlines()
                count = 0
                sql = sql_base = "INSERT INTO l10n_no_hr_payroll_tabelltrekk (year, tabellnummer, trekkperiode, tabelltype, trekkgrunnlag, trekk) VALUES "
                for line in lines:
                    sql += """
                        (%s, %s, %s, %s, %s, %s),""" % (year_dict['year'], line[:4], line[4], line[5], line[6:][:5], line[11:][:5]) 
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
            record = self.env['l10n_no_hr_payroll.tabelltrekk'].search([('year','=',year),('tabellnummer','=',trekktabell.value),
                ('trekkperiode','=',trekkperiode),('tabelltype','=',tabelltype),('trekkgrunnlag','=',trekkgrunnlag)
            ], limit=1)
            if record:
                return -int(int(record.ensure_one().trekk) * andel_av_trekk)
            else:
                record = self.env['l10n_no_hr_payroll.tabelltrekk'].search([
                    ('year','=',year),('tabellnummer','=',trekktabell.value),('trekkperiode','=',trekkperiode),('tabelltype','=',tabelltype)
                ], order='trekkgrunnlag DESC', limit=1)
                if trekkgrunnlag > record.trekkgrunnlag:
                    return -int( (record.trekk + (trekkgrunnlag - record.trekkgrunnlag) * trekkprosent) * andel_av_trekk)
                else:
                    return 0
        else:
            trekk = -int(trekkgrunnlag * trekkprosent * andel_av_trekk)
            return trekk
