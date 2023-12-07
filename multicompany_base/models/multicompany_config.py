import logging

from odoo import models

from ..tools import _prepare

_logger = logging.getLogger(__name__)
SYSTEM_COMPANY_ID = 1


class MulticompanyConfig(models.AbstractModel):
    _name = "multicompany.config"
    _inherit = "base.set.record.values.mixin"
    _description = "Configuration of companies with forced security"

    """
    Sometimes Odoo assumes that a user has access to a specific record.
    With forced security, the user might not have access.
    The configuration will search for specific records,
    as admin user logged into one specific company.
    The search will include all records permitted by the security rules,
    including inactive records and parent/child companies.
    - Exception: Search for company website
    If not found, create (or copy) a new record for the company.
    """

    def _register_hook(self, update_module=False):
        pass  # using multicompany.security

    def configure_system_and_all_companies(self):
        # Returning an error value to _register_hook will be ignored (see loading.py).
        if not self.env.user.has_group("base.group_system"):
            return False

        _logger.info("Starting multicompany.config configure_system_and_all_companies")

        self._configure_system()

        all_companies = self.env["res.company"].sudo().search([])
        self._configure_companies(all_companies)
        return

    def _configure_system(self):

        try:
            # New users auto-subscribe to the digest. AccessError or annoying emails.
            digest = self.env["digest.digest"].search([("company_id", "=", 1)])
            if digest:
                digest.unlink()
        except:
            pass

        product_module = self.env["ir.module.module"].search([("name", "=", "product")])
        if product_module and product_module.state == "installed":
            # Create a new pricelist so it is possible to archive the system pricelist.
            # Archive the system pricelist so websites will get the company's pricelist.
            Pricelist = self.env["product.pricelist"]
            product_list = self.env.ref("product.list0", raise_if_not_found=False)
            count_pricelists = Pricelist.with_context(active_test=False).search_count(
                [("company_id", "=", 1)]
            )
            if product_list and count_pricelists == 1:
                product_list.copy({"name": "Pricelist"})
            if product_list and product_list.active:
                product_list.active = False

        # If active, new websites will get default crm.team which is not accessable.
        # EDIT: Patch will check if multicompany_base is installed.
        # website_salesteam = self.env.ref(
        #   'sales_team.salesteam_website_sales', raise_if_not_found=False)
        # if website_salesteam:
        #     website_salesteam.active = False

        def _ref(xmlid):
            return self.env.ref(xmlid, raise_if_not_found=False)

        def _id(record):
            if record:
                return record.id

        def _set(record, values):
            if record:
                models.Model.write(record, values)

        def _set_record_values(*args, **kwargs):
            try:
                return self._set_record_values(*args, **kwargs)
            except Exception:
                pass

        # Hide some security rules
        # Read the system user/partner
        # (necessary when sudo() does not bypass global rules)
        _set(_ref("base.res_users_rule"), {"active": False})
        _set(_ref("base.res_partner_rule"), {"active": False})
        # website_sale rules include website.company_id.id which give errors.
        _set(_ref("website_sale.product_pricelist_item_comp_rule"), {"active": False})
        _set(_ref("website_sale.product_pricelist_comp_rule"), {"active": False})

        # Give access rights to company managers (including the Support User)
        company_manager = self.env.ref("multicompany_base.group_company_manager")

        # Access to change password
        _set(
            _ref("base.change_password_wizard_action"),
            {"groups_id": [(4, company_manager.id, 0)]},
        )

        #
        # Menu (move to multicompany_ag?)
        #
        # Website
        _set(
            _ref("website.menu_website_configuration"),
            {
                "groups_id": [
                    (3, _id(_ref("base.group_user")), 0),
                    (4, _id(_ref("website.group_website_publisher")), 0),
                ]
            },
        )
        # Employees
        _set(
            _ref("hr.menu_hr_root"),
            {
                "groups_id": [
                    (3, _id(_ref("base.group_user")), 0),
                    # (4, _id(_ref('hr.group_hr_user')), 0),
                ]
            },
        )
        # Settings
        _set(
            _ref("base.menu_administration"),
            {
                "groups_id": [
                    (4, company_manager.id, 0),
                ]
            },
        )

        # Public Group
        _set(
            _ref("base.group_public"),
            {
                "implied_ids": [
                    (3, _id(_ref("account.group_show_line_subtotals_tax_excluded")), 0),
                    (3, _id(_ref("account.group_show_line_subtotals_tax_included")), 0),
                ]
            },
        )
        # Portal Group
        _set(
            _ref("base.group_portal"),
            {
                "implied_ids": [
                    (3, _id(_ref("account.group_show_line_subtotals_tax_excluded")), 0),
                    (3, _id(_ref("account.group_show_line_subtotals_tax_included")), 0),
                ]
            },
        )
        # Internal User Group
        _set(
            _ref("base.group_user"),
            {
                "implied_ids": [
                    (3, _id(_ref("account.group_show_line_subtotals_tax_excluded")), 0),
                    (3, _id(_ref("account.group_show_line_subtotals_tax_included")), 0),
                    (3, _id(_ref("analytic.group_analytic_accounting")), 0),
                    (3, _id(_ref("sale.group_delivery_invoice_address")), 0),
                    (3, _id(_ref("website.group_multi_website")), 0),
                ]
            },
        )

        ################################################################################
        # Contract Officer
        # TODO: Make this configuration in XML, try to load each XML record, ignore errors, new section (or demo?) in __manifest__.py
        module = self.env['ir.module.module'].search([('name', '=', 'hr_contract')])
        if module.exists() and module.state == 'installed':
            contract_category = _ref("base.module_category_human_resources_contracts")
            contract_user_group = self._set_record_values(
                "res.groups",
                [("name", "=", "Officer"), ("category_id", "=", contract_category.id)],
                {
                    "name": "Officer",
                    "category_id": _id(contract_category),
                    "implied_ids": [(4, _id(_ref('hr.group_hr_user')))],
                },
                "__ag__.group_hr_contract_user",
            )
            contract_user_access = self._set_record_values(
                "ir.model.access",
                [
                    ("model_id", "=", _id(_ref("hr_contract.model_hr_contract"))),
                    ("group_id", "=", _id(_ref("__ag__.group_hr_contract_user"))),
                ],
                {
                    "name": "hr.contract user",
                    "model_id": _id(_ref("hr_contract.model_hr_contract")),
                    "group_id": _id(_ref("__ag__.group_hr_contract_user")),
                    "perm_read": 1,
                    "perm_write": 1,
                    "perm_create": 1,
                    "perm_unlink": 1,
                },
            )
            contract_user_rule = self._set_record_values(
                "ir.rule",
                [
                    ("model_id", "=", _id(_ref("hr_contract.model_hr_contract"))),
                    ("groups", "in", _id(_ref("__ag__.group_hr_contract_user"))),
                ],
                {
                    "name": "Department managers can access their employee contracts",
                    "model_id": _id(_ref("hr_contract.model_hr_contract")),
                    "groups": [(4, _id(_ref('__ag__.group_hr_contract_user')))],
                    "domain_force": "['|', ('department_id', '=', False), ('department_id.manager_id.user_id', '=', user.id)]",
                    "perm_read": 1,
                    "perm_write": 1,
                    "perm_create": 1,
                    "perm_unlink": 1,
                },
            )
            contract_manager_rule = self._set_record_values(
                "ir.rule",
                [
                    ("model_id", "=", _id(_ref("hr_contract.model_hr_contract"))),
                    ("groups", "in", _id(_ref("hr_contract.group_hr_contract_manager"))),
                ],
                {
                    "name": "Contract managers can access all contracts",
                    "model_id": _id(_ref("hr_contract.model_hr_contract")),
                    "groups": [(4, _id(_ref('hr_contract.group_hr_contract_manager')))],
                    "domain_force": "[(1, '=', 1)]",
                    "perm_read": 1,
                    "perm_write": 1,
                    "perm_create": 1,
                    "perm_unlink": 1,
                },
            )
            _set(
                _ref("payroll.hr_payroll_rule_officer"),
                {
                    "domain_force": """[
                    '|',
                    ('employee_id.department_id.manager_id.user_id', '=', user.id),
                    ('contract_id.department_id.manager_id.user_id', '=', user.id),
                    ]"""
                }
            )
            _set(
                _ref("payroll.group_payroll_user"),
                {
                    "implied_ids": [
                        (3, _id(_ref("hr_contract.group_hr_contract_manager"))),
                        (4, _id(_ref("__ag__.group_hr_contract_user"))),
                    ]
                }
            )
            _set(
                _ref("hr_contract.group_hr_contract_manager"),
                {
                    "implied_ids": [
                        (4, _id(_ref("__ag__.group_hr_contract_user"))),
                    ]
                }
            )
        ################################################################################

    def _configure_companies(self, companies):
        for company in companies:
            self = _prepare(self, company)
            self._configure_company()

    def _configure_company(self):
        # --------------------------------------------------
        # General company mail.channel may be confusing in a parent/child environment.
        #   Skipping this for now.
        # self._create_a_company_mail_channel_for_all_employees()
        # Bad idea to copy all system sequences with code
        # self._copy_system_sequences_with_code(company.id)
        self._create_default_user()
        public_user = self._create_public_user()
        self._create_website_and_crm_team(public_user)
        self._create_product_category()
        # --------------------------------------------------

    def _create_a_company_mail_channel_for_all_employees(self):
        imd_record = self._env("ir.model.data").search(
            [("module", "=", "mail"), ("name", "=", "channel_all_employees")]
        )
        if imd_record:
            assert imd_record.model == "mail.channel"
            group_user_id = self.env.ref("base.group_user").id
            all_employees = self.env["res.users"].search(
                [("groups_id", "=", group_user_id), ("default_user", "=", False)]
            )
            partner_ids = all_employees.mapped("partner_id").ids
            add_mail_channel_partners = [(0, 0, id) for id in partner_ids]
            return self._insert_first_record(
                model="mail.channel",
                search=[("all_employees", "=", True)],
                values={
                    "name": "general",
                    "description": "General announcements for all employees.",
                    "group_ids": [(4, group_user_id), 0],
                    "all_employees": True,
                    "channel_last_seen_partner_ids": add_mail_channel_partners,
                },
            )

    def _copy_system_sequences_with_code(self):
        system_sequences_with_code = (
            self._env("ir.sequence")
            .sudo()
            .search([("code", "like", "_"), ("company_id", "=", SYSTEM_COMPANY_ID)])
        )
        sequences_with_code = []
        for sequence in system_sequences_with_code:
            sequences_with_code.append(
                # self.sudo() ?
                self._insert_first_record(
                    model="ir.sequence",
                    search=[("code", "=", sequence.code)],
                    values={
                        "number_next": 1,
                    },
                    copy="ir.sequence," + str(sequence.id),
                )
            )
        return sequences_with_code

    def _create_default_user(self):
        company_id = self.env.company.id
        default_user = self._insert_first_record(
            model="res.users",
            search=[
                ("default_user", "=", True),
            ],
            values={
                "company_id": company_id,
                "company_ids": [(6, None, [company_id])],
                "login": "default_user_for_company_" + str(company_id),
                "name": "Default user for company " + str(company_id),
                "active": False,
                "default_user": True,
            },
        )
        return default_user

    def _create_public_user(self):
        company_id = self.env.company.id
        public_user = self._insert_first_record(
            model="res.users",
            search=[
                ("groups_id", "=", self._ref("base.group_public").id),
                ("company_id", "=", company_id),
            ],
            values={
                "company_id": company_id,
                "company_ids": [(6, None, [company_id])],
                "login": "public_user_for_company_" + str(company_id),
                "name": "Public user for company " + str(company_id),
                "password": "",
                "active": False,
                "groups_id": [(6, None, [self._ref("base.group_public").id])],
                # <field name="image_1920" type="base64"
                #   file="base/static/img/public_user-image.png"/>
                # <field name="partner_id" ref="public_partner"/>
            },
        )
        return public_user

    def _create_website_and_crm_team(self, public_user):
        company = self.env.company
        website_user_field = self._ref("website.field_website__user_id")
        if not website_user_field:
            return self
        self._insert_first_record(
            model="ir.default",
            search=[("field_id", "=", website_user_field.id)],
            values={
                "company_id": company.id,
                "field_id": website_user_field.id,
                "json_value": public_user.id,
            },
        )
        default_languages = [self.env.ref("base.lang_en").id]
        website = self._insert_first_record(
            model="website",
            search=[("company_id", "=", company.id)],
            values={
                "company_id": company.id,
                "name": company.name,
                "language_ids": [(6, None, default_languages)],
            },
        )
        if website:
            if not company.website_id.id:
                company = _prepare(company, company)
                company.write({"website_id": website.id})
            # crm.team
            crm_team_field = self._ref("website_crm.field_website__crm_default_team_id")
            if crm_team_field:
                crm_team = self._insert_first_record(
                    model="crm.team",
                    copy="sales_team.salesteam_website_sales",
                )
                if not website.crm_default_team_id:
                    website.crm_default_team_id = crm_team
        return website

    def _create_product_category(self):
        product_category = self._insert_first_record(
            model="product.category",
            copy="product.product_category_all",
        )
        return product_category

    #
    # _insert_first_record
    # and "blank" methods to use after failing to return a record(set).
    #

    def _insert_first_record(self, model, search=[(1, "=", 1)], values={}, copy=False):
        """
        model (string): the model to insert the first record
        search (list):  the search domain to see if a record already exists
        values (dict):  values to insert into the first record
        copy (string):  optional external reference
            or 'model,res_id' of an existing record
            to 'copy' (otherwise 'create')
        """
        company_id = self.env.company.id
        values["company_id"] = company_id
        search = (
            ["&"]
            + search
            + [
                "|",
                ("company_id", "=", company_id),
                "|",
                ("company_id", "parent_of", company_id),
                ("company_id", "child_of", company_id),
            ]
        )
        records = self._env(model).search(search)
        if not records.exists():
            if copy is False:
                record = self._env(model).create(values)
                return record
            elif "," in copy:
                model, res_id = copy.split(",")
                record = self._env(model).sudo().browse(int(res_id)).copy(values)
                return record
            else:
                record = self.sudo()._ref(copy).copy(values)
                return record
        else:
            record_count = (
                self._env(model).with_context(active_test=False).search_count(search)
            )
            if record_count == 1:
                return records  # Other variables might be dependent on the record

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
