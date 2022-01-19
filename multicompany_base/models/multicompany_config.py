from odoo import models
import logging

_logger = logging.getLogger(__name__)
SYSTEM_COMPANY = 1
ADMIN_USER = 2

class MulticompanyConfig(models.AbstractModel):
    _name = 'multicompany.config'
    _description = 'Configuration of companies with forced security'

    """
    Sometimes Odoo assumes that a user has access to a specific record.
    With forced security, the user might not have access.
    The configuration will search for specific records, as admin user logged into one specific company.
    The search will include all records permitted by the security rules, including inactive records and parent/child companies.
    - Exception: Search for company website
    If not found, create (or copy) a new record for the company.
    """

    def _register_hook(self, update_module=False):
        if update_module:
            param = self.env['ir.config_parameter'].get_param('multicompany_base.force_config')
            if param in ('1', 't', 'true', 'True'):
                self.configure_all_companies()
                _logger.info('multicompany.config done')

    def configure_all_companies(self):
        # Returning an error value to _register_hook will be ignored (see loading.py).
        all_companies = self.env['res.company'].sudo().search([])
        self._configure(all_companies)
        return True

    def _configure(self, companies):
        for company in companies:
            self = self._prepare(company)
            # --------------------------------------------------
            self._create_a_company_mail_channel_for_all_employees()
            self._copy_system_sequences_with_code(company.id)
            self._create_default_user(company.id)
            public_user = self._create_public_user(company.id)
            self._create_website(company, public_user)
            # --------------------------------------------------

    def _prepare(self, company):
        self = self.with_user(
            self.env.user.browse(ADMIN_USER) # Cannot be SUPERUSER
        ).with_context(
            active_test=False,
            allowed_company_ids=[company.id],
        )
        self.env.company = company
        self.env.companies = company
        return self

    def _create_a_company_mail_channel_for_all_employees(self):
        imd_record = self._env('ir.model.data').search([('module', '=', 'mail'), ('name', '=', 'channel_all_employees')])
        if imd_record:
            assert imd_record.model == 'mail.channel'
            group_user_id = self.env.ref('base.group_user').id
            return self._insert_first_record(
                model='mail.channel',
                search=[('all_employees', '=', True)],
                values={
                    'name': 'general',
                    'description': 'General announcements for all employees.',
                    'group_ids': [(4, group_user_id), 0],
                    'all_employees': True,
                },
            )

    def _copy_system_sequences_with_code(self, company_id):
        system_sequences_with_code = self._env('ir.sequence').sudo().search([('code', 'like', '_'), ('company_id', '=', SYSTEM_COMPANY)])
        sequences_with_code = []
        for sequence in system_sequences_with_code:
            sequences_with_code.append(
                self._insert_first_record(
                    model='ir.sequence',
                    search=[('code', '=', sequence.code)],
                    values={
                        'number_next': 1,
                        'company_id': company_id,
                    },
                    copy='ir.sequence,' + str(sequence.id),
                )
            )
        return sequences_with_code

    def _create_default_user(self, company_id):
        return self._insert_first_record(
            model='res.users',
            search=[
                ('default_user', '=', True),
            ],
            values={
                'company_id': company_id,
                'company_ids': [(6, None, [company_id])],
                'login': 'default_user_for_company_' + str(company_id),
                'name': 'Default user for company ' + str(company_id),
                'active': False,
                'default_user': True,
            },
        )

    def _create_public_user(self, company_id):
        return self._insert_first_record(
            model='res.users',
            search=[
                ('groups_id', '=', self._ref('base.group_public').id),
            ],
            values={
                'company_id': company_id,
                'company_ids': [(6, None, [company_id])],
                'login': 'public_user_for_company_' + str(company_id),
                'name': 'Public user for company ' + str(company_id),
                'password': '',
                'active': False,
                'groups_id': [(6, None, [self._ref('base.group_public').id])],
                # <field name="image_1920" type="base64" file="base/static/img/public_user-image.png"/>
                # <field name="partner_id" ref="public_partner"/>
            },
        )

    def _create_website(self, company, public_user):
        website_user_field = self._ref('website.field_website__user_id')
        if not website_user_field:
            return self
        self._insert_first_record(
            model='ir.default',
            search=[('field_id', '=', website_user_field.id)],
            values={'company_id': company.id, 'field_id': website_user_field.id, 'json_value': public_user.id},
        )
        default_languages = [self.env.ref('base.lang_en').id]
        website = self._insert_first_record(
            model='website',
            search=[('company_id', '=', company.id)],
            values={'company_id': company.id, 'name': company.name, 'language_ids': [(6, None, default_languages)]},
            return_existing_record_if_one=False,
        )
        if website:
            company.write({'website_id': website.id})
        return website

    #
    # _insert_first_record and "blank" methods to use after failing to return a record(set).
    #

    def _insert_first_record(self, model, search, values, copy=False, return_existing_record_if_one=True):
        '''
        model (string): the model to insert the first record
        search (list):  the search domain to see if a record already exists
        values (dict):  values to insert into the first record
        copy (string):  optional external reference or 'model,res_id' of an existing record to 'copy' (otherwise 'create')
        '''
        records = self._env(model).search(search)
        if not records.exists():
            if copy == False:
                record = self._env(model).create(values)
                return record
            elif ',' in copy:
                model, res_id = copy.split(',')
                record = self._env(model).sudo().browse(int(res_id)).copy(values)
                return record
            else:
                record = self._ref(copy).sudo().copy(values)
                return record
        elif return_existing_record_if_one:
            record_count = self._env(model).with_context(active_test=False).search_count(search)
            if record_count == 1:
                return records # Other variables might be dependent on the record

    def _env(self, model):
        try:
            return self.env[model]
        except KeyError:
            return self

    def _ref(self, xmlid):
        try:
            return self.env.ref(xmlid)
        except ValueError:
            return self

    def browse(self, *args, **kwargs):
        return self

    def copy(self, *args, **kwargs):
        pass

    def create(self, *args, **kwargs):
        pass

    def search(self, *args, **kwargs):
        return self
