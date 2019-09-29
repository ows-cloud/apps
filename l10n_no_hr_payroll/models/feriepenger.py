from collections import defaultdict
from odoo import api, fields, models
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)

class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    
    @api.model
    def l10n_no_feriepenger(self):

        # Get key variables
        fp_prosent = float(self.env['res.field.value'].search(
            [('model','=','res.company'),('field_id','=',self.env.ref('l10n_no_hr_payroll.res_field_l10n_no_fp_prosent').id)]
        ).ensure_one().value) / 100
        fp_prosent_senior = float(self.env['res.field.value'].search(
            [('model','=','res.company'),('field_id','=',self.env.ref('l10n_no_hr_payroll.res_field_l10n_no_fp_prosent_senior').id)]
        ).ensure_one().value) / 100
        loennsart_fp_i_aar_id = self.env['res.field.value'].search(
            [('model','=','res.company'),('field_id','=',self.env.ref('l10n_no_hr_payroll.res_field_l10n_no_loennsart_fp_i_aar').id)]
        ).ensure_one().reference_value.id
        loennsart_fp_i_fjor_id = self.env['res.field.value'].search(
            [('model','=','res.company'),('field_id','=',self.env.ref('l10n_no_hr_payroll.res_field_l10n_no_loennsart_fp_i_fjor').id)]
        ).ensure_one().reference_value.id
        loennsarter_beregn_fp_ids = [r.res_id for r in self.env['res.field.value'].search(
            [('model','=','hr.salary.rule'),('field_id','=',self.env.ref('l10n_no_hr_payroll.res_field_l10n_no_BeregnFP').id)]
        )]
        salary_rule_ids = loennsarter_beregn_fp_ids[:] # copy list by value
        salary_rule_ids.extend([loennsart_fp_i_aar_id, loennsart_fp_i_fjor_id])

        # Get info from the payslip lines into dictinary 'd'
        d = defaultdict(dict)
        payslip_lines = self.search([('salary_rule_id','in',salary_rule_ids)])
        for line in payslip_lines:
            employee_id = line.employee_id.id
            rule_id = line.salary_rule_id.id
            year = int(line.slip_id.date_to[:4])
            if rule_id == loennsart_fp_i_fjor_id:
                year -= 1

            if not employee_id in d:
                d[employee_id]['name'] = line.employee_id.name
                d[employee_id]['birthyear'] = int(line.employee_id.birthday[:4])
                d[employee_id]['year'] = {}
            if not year in d[employee_id]['year']:
                d[employee_id]['year'][year] = {'basis': 0, 'rate': 0, 'vacation_money': 0, 'paid': 0}
                # Senior rate the year before the worker becomes 60 years old
                if year - d[employee_id]['birthyear'] >= 59:
                    d[employee_id]['year'][year]['rate'] = fp_prosent_senior
                else:
                    d[employee_id]['year'][year]['rate'] = fp_prosent
            if rule_id in [loennsart_fp_i_fjor_id, loennsart_fp_i_aar_id]:
                d[employee_id]['year'][year]['paid'] += line.total
            else:
                d[employee_id]['year'][year]['basis'] += line.total

        # Create a CSV report
        csv = 'employee_id,employee_name,year,basis,rate,vacation_money,paid,unpaid\n'
        for employee_id in d:
            for year in d[employee_id]['year']:
                vacation_money = d[employee_id]['year'][year]['basis'] * d[employee_id]['year'][year]['rate']
                csv += '%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                    employee_id,
                    d[employee_id]['name'],
                    year,
                    d[employee_id]['year'][year]['basis'],
                    d[employee_id]['year'][year]['rate'],
                    vacation_money,
                    d[employee_id]['year'][year]['paid'],
                    vacation_money - d[employee_id]['year'][year]['paid'],
                )

        raise UserError(csv)
