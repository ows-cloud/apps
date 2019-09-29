# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api, fields
from lxml import etree
import logging

_logger = logging.getLogger(__name__)


"""
web_widget_x2many_2d_matrix would be a better solution
if the 'value' could be many2one to select users.
"""


def _get_dynamic_labels(arch, record):
    """
    This function is called from fields_view_get.
    fields_view_get cannot get the current record
    because it is impossible to retrieve the id from request or environment,
    except when loading x2many views.
    Therefore duty.availability and duty.list.line has dynamic labels from related fields.
    """
    doc = etree.XML(arch)

    node1 = doc.xpath("//field[@name='column1']")[0]
    if record.label1:
        node1.set('string', record.label1)
    else:
        node1.getparent().remove(node1)

    node2 = doc.xpath("//field[@name='column2']")[0]
    if record.label2:
        node2.set('string', record.label2)
    else:
        node2.getparent().remove(node2)

    node3 = doc.xpath("//field[@name='column3']")[0]
    if record.label3:
        node3.set('string', record.label3)
    else:
        node3.getparent().remove(node3)

    node4 = doc.xpath("//field[@name='column4']")[0]
    if record.label4:
        node4.set('string', record.label4)
    else:
        node4.getparent().remove(node4)

    node5 = doc.xpath("//field[@name='column5']")[0]
    if record.label5:
        node5.set('string', record.label5)
    else:
        node5.getparent().remove(node5)

    node6 = doc.xpath("//field[@name='column6']")[0]
    if record.label6:
        node6.set('string', record.label6)
    else:
        node6.getparent().remove(node6)

    node7 = doc.xpath("//field[@name='column7']")[0]
    if record.label7:
        node7.set('string', record.label7)
    else:
        node7.getparent().remove(node7)

    node8 = doc.xpath("//field[@name='column8']")[0]
    if record.label8:
        node8.set('string', record.label8)
    else:
        node8.getparent().remove(node8)

    node9 = doc.xpath("//field[@name='column9']")[0]
    if record.label9:
        node9.set('string', record.label9)
    else:
        node9.getparent().remove(node9)

    node10 = doc.xpath("//field[@name='column10']")[0]
    if record.label10:
        node10.set('string', record.label10)
    else:
        node10.getparent().remove(node10)

    node11 = doc.xpath("//field[@name='column11']")[0]
    if record.label11:
        node11.set('string', record.label11)
    else:
        node11.getparent().remove(node11)

    node12 = doc.xpath("//field[@name='column12']")[0]
    if record.label12:
        node12.set('string', record.label12)
    else:
        node12.getparent().remove(node12)

    node13 = doc.xpath("//field[@name='column13']")[0]
    if record.label13:
        node13.set('string', record.label13)
    else:
        node13.getparent().remove(node13)

    return etree.tostring(doc)


class DutyRole(models.Model):
    _name = 'duty.role'
    _description = 'duty.role'
    _order='sequence'

    name = fields.Char("Role Name")
    user_ids = fields.Many2many('res.users', string="Users")
    sequence = fields.Integer()
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)


class DutyAvailability(models.Model):
    _name = 'duty.availability'
    _description = 'duty.availability'

    list_id = fields.Many2one('duty.list', string="List")
    user_id = fields.Many2one('res.users', string="User")
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
    
    yes_no = [('yes','Available'),('no','Not available')]
    column1 = fields.Selection(selection=yes_no)
    column2 = fields.Selection(selection=yes_no)
    column3 = fields.Selection(selection=yes_no)
    column4 = fields.Selection(selection=yes_no)
    column5 = fields.Selection(selection=yes_no)
    column6 = fields.Selection(selection=yes_no)
    column7 = fields.Selection(selection=yes_no)
    column8 = fields.Selection(selection=yes_no)
    column9 = fields.Selection(selection=yes_no)
    column10 = fields.Selection(selection=yes_no)
    column11 = fields.Selection(selection=yes_no)
    column12 = fields.Selection(selection=yes_no)
    column13 = fields.Selection(selection=yes_no)
    label1 = fields.Char('1', related='list_id.label1')
    label2 = fields.Char('2', related='list_id.label2')
    label3 = fields.Char('3', related='list_id.label3')
    label4 = fields.Char('4', related='list_id.label4')
    label5 = fields.Char('5', related='list_id.label5')
    label6 = fields.Char('6', related='list_id.label6')
    label7 = fields.Char('7', related='list_id.label7')
    label8 = fields.Char('8', related='list_id.label8')
    label9 = fields.Char('9', related='list_id.label9')
    label10 = fields.Char('10', related='list_id.label10')
    label11 = fields.Char('11', related='list_id.label11')
    label12 = fields.Char('12', related='list_id.label12')
    label13 = fields.Char('13', related='list_id.label13')

    def name_get(self):
        return [(record.id, record.user_id.name) for record in self]

    _sql_constraints = [('list_user_uniq', 'unique(list_id, user_id, company_id)', 'List User must be unique per company!')]


class DutyListLine(models.Model):
    _name = 'duty.list.line'
    _description = 'duty.list.line'
    _order='sequence'

    list_id = fields.Many2one('duty.list', required=True, string="List")
    role_id = fields.Many2one('duty.role', required=True, string="Role")
    sequence = fields.Integer(related='role_id.sequence', readonly=True)
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
        
    column1 = fields.Many2one('res.users')
    column2 = fields.Many2one('res.users')
    column3 = fields.Many2one('res.users')
    column4 = fields.Many2one('res.users')
    column5 = fields.Many2one('res.users')
    column6 = fields.Many2one('res.users')
    column7 = fields.Many2one('res.users')
    column8 = fields.Many2one('res.users')
    column9 = fields.Many2one('res.users')
    column10 = fields.Many2one('res.users')
    column11 = fields.Many2one('res.users')
    column12 = fields.Many2one('res.users')
    column13 = fields.Many2one('res.users')
    domain_column1 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column1 availability")
    domain_column2 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column2 availability")
    domain_column3 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column3 availability")
    domain_column4 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column4 availability")
    domain_column5 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column5 availability")
    domain_column6 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column6 availability")
    domain_column7 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column7 availability")
    domain_column8 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column8 availability")
    domain_column9 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column9 availability")
    domain_column10 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column10 availability")
    domain_column11 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column11 availability")
    domain_column12 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column12 availability")
    domain_column13 = fields.Many2many('res.users', compute='_compute_domain_column', string="Column13 availability")
    label1 = fields.Char('1', related='list_id.label1')
    label2 = fields.Char('2', related='list_id.label2')
    label3 = fields.Char('3', related='list_id.label3')
    label4 = fields.Char('4', related='list_id.label4')
    label5 = fields.Char('5', related='list_id.label5')
    label6 = fields.Char('6', related='list_id.label6')
    label7 = fields.Char('7', related='list_id.label7')
    label8 = fields.Char('8', related='list_id.label8')
    label9 = fields.Char('9', related='list_id.label9')
    label10 = fields.Char('10', related='list_id.label10')
    label11 = fields.Char('11', related='list_id.label11')
    label12 = fields.Char('12', related='list_id.label12')
    label13 = fields.Char('13', related='list_id.label13')
    
    def _compute_domain_column(self):
        for record in self:
            role_users = record.role_id.user_ids
            record.domain_column1 = role_users - record.list_id.availability_ids.search([('column1','=','no')]).mapped('user_id')
            record.domain_column2 = role_users - record.list_id.availability_ids.search([('column2','=','no')]).mapped('user_id')
            record.domain_column3 = role_users - record.list_id.availability_ids.search([('column3','=','no')]).mapped('user_id')
            record.domain_column4 = role_users - record.list_id.availability_ids.search([('column4','=','no')]).mapped('user_id')
            record.domain_column5 = role_users - record.list_id.availability_ids.search([('column5','=','no')]).mapped('user_id')
            record.domain_column6 = role_users - record.list_id.availability_ids.search([('column6','=','no')]).mapped('user_id')
            record.domain_column7 = role_users - record.list_id.availability_ids.search([('column7','=','no')]).mapped('user_id')
            record.domain_column8 = role_users - record.list_id.availability_ids.search([('column8','=','no')]).mapped('user_id')
            record.domain_column9 = role_users - record.list_id.availability_ids.search([('column9','=','no')]).mapped('user_id')
            record.domain_column10 = role_users - record.list_id.availability_ids.search([('column10','=','no')]).mapped('user_id')
            record.domain_column11 = role_users - record.list_id.availability_ids.search([('column11','=','no')]).mapped('user_id')
            record.domain_column12 = role_users - record.list_id.availability_ids.search([('column12','=','no')]).mapped('user_id')
            record.domain_column13 = role_users - record.list_id.availability_ids.search([('column13','=','no')]).mapped('user_id')

    def name_get(self):
        return [(record.id, record.role_id.name) for record in self]

    _sql_constraints = [('list_role_uniq', 'unique(list_id, role_id, company_id)', 'List Role must be unique per company!')]


class DutyList(models.Model):
    _name = 'duty.list'
    _description = 'duty.list'
    
    name = fields.Char("List Name")
    availability_ids = fields.One2many('duty.availability', 'list_id', string="Availability")
    list_line_ids = fields.One2many('duty.list.line', 'list_id', string="Lines")
    company_id = fields.Many2one('res.company', string='Company', store=True, index=True, default=lambda self: self.env.user.company_id)
    
    label1 = fields.Char('1')
    label2 = fields.Char('2')
    label3 = fields.Char('3')
    label4 = fields.Char('4')
    label5 = fields.Char('5')
    label6 = fields.Char('6')
    label7 = fields.Char('7')
    label8 = fields.Char('8')
    label9 = fields.Char('9')
    label10 = fields.Char('10')
    label11 = fields.Char('11')
    label12 = fields.Char('12')
    label13 = fields.Char('13')
    
    def action_reload(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    @api.model
    def fields_view_get(self,view_id=None, view_type=None, toolbar=False, submenu=False):
        res = super(DutyList, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        
        list_id = self.env.context.get('params', {}).get('id')
        if list_id and view_type == 'form':
            record = self.browse(list_id)
            res['fields']['list_line_ids']['views']['tree']['arch'] = _get_dynamic_labels(res['fields']['list_line_ids']['views']['tree']['arch'], record)
            res['fields']['availability_ids']['views']['tree']['arch'] = _get_dynamic_labels(res['fields']['availability_ids']['views']['tree']['arch'], record)
            
        return res

    def action_mass_mailing_availability(self):
        url_except_id = 'https://' + self.company_id.website_id.domain + '/web#view_type=form&model=duty.availability&id='
        view = self.env.ref('mail.email_compose_message_wizard_form')
        mail_template = self.env.ref('duty_list.mail_template_duty_availability')

        self.ensure_one()
        for record in self:

            # Create duty.availability if missing
            role_users = record.mapped('list_line_ids.role_id.user_ids')
            availability_users = record.mapped('availability_ids.user_id')
            missing_users = role_users - availability_users
            for user in missing_users:
                self.env['duty.availability'].create({'list_id': record.id, 'user_id': user.id})

            # Return window action so the manager can send email (needs mail.template)
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'mail.compose.message',
                'view_mode': 'form',
                'view_id': view.id,
                'target': 'new',
                'key2': 'client_action_multi',
                'context': {
                    'default_composition_mode': 'mass_mail', 
                    'default_template_id' : mail_template.id,
                    'default_use_template': True,
                    'active_model': 'duty.availability',
                    'active_ids': record.availability_ids.ids,
                    'active_id': 0, # otherwise DutyList.id will trigger DutyAvailability.name_get and return "Record does not exist or is deleted."
                    'url_except_id': url_except_id,
                },
            }

    def action_availability(self):
        self.ensure_one()
        return {
            'name': 'Availability',
            'type': 'ir.actions.act_window',
            'res_model': 'duty.availability',
            'view_mode': 'tree,form',
            'context': {
                'search_default_list_id' : self.id,
            }
        }

    def action_duties(self):
        self.ensure_one()
        return {
            'name': 'Duties',
            'type': 'ir.actions.act_window',
            'res_model': 'duty.list.line',
            'view_mode': 'tree,form',
            'context': {
                'search_default_list_id' : self.id,
            }
        }
