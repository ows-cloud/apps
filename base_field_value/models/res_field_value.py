import logging
from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


def _validate(value, data_type, date_format=None):
    # All variables are strings
    new_value = ""

    if data_type == "x_":
        if not value:
            new_value = "x_"
        elif len(value) >= 2 and value[:2] == "x_":
            new_value = value
        else:
            new_value = "x_" + value

    elif data_type == "string":
        new_value = value

    elif data_type == "boolean":
        if value in ("True", "true", "TRUE", "1"):
            new_value = "True"
        elif value in ("False", "false", "FALSE", "0"):
            new_value = "False"

    elif data_type == "integer":
        try:
            new_value = str(int(value))
        except:
            pass

    elif data_type == "float":
        try:
            new_value = str(float(value))
        except:
            pass

    elif data_type == "date":
        formats = ["%Y-%m-%d", date_format]
        _logger.debug("formats: " + str(formats) + ", value = " + str(value))
        for my_format in formats:
            try:
                new_value = datetime.strptime(value, my_format).strftime("%Y-%m-%d")
                break
            except:
                pass

    return new_value


# TODO: base_custom_info should handle 'reference' data type.
data_type_selection = [
    ("string", "Text"),
    ("boolean", "True/False"),
    ("integer", "Number"),
    ("float", "Decimal"),
    ("date", "Date"),
    ("selection", "Selection"),
    ("reference", "Reference"),
]


class ResField(models.Model):
    """
    Create custom fields without changing the database structure.

    Field values will get the 'model' and 'res_id' of the object.
    ('model' is used rather than 'model_id' because the client cannot understand context={'default_model_id': self.env.ref('external_id')})

    'app' is Selection instead of Many2one, to work with 'field_id' domain in views.

    Fields can be assigned only to models with a field like e.g. field_value_ids = fields.One2many('res.field.value', copy=True).

    Fields assigned to a country, is available only if the company country_id belongs to that country.

    Fields created by users must begin with 'x_'.
    """

    _name = "res.field"
    _description = "Field"

    name = fields.Char(required=True)
    model = fields.Selection(
        selection="_get_models", string="Model Name", required=True
    )
    app = fields.Selection(selection="_get_apps", string="Application")
    data_type = fields.Selection(
        string="Data type", required=True, selection=data_type_selection
    )
    code = fields.Char(required=True, default="x_")
    selection_value_ids = fields.One2many(
        "res.field.selection_value", "field_id", string="Selection values"
    )
    reference_model = fields.Many2one(
        "ir.model",
        string="Reference Model",
        help="""TODO: javascript widget to select res_field_value.reference_value only from this model in dropdown menu.
        (object.one2many('res.field.value'): selection function runs only once for the object, not once per res.field.value.)""",
    )
    default_value = fields.Char("Default Value")
    auto_create = fields.Boolean("Create on new object")
    # property_auto_create = fields.Boolean("Create on new object", company_dependent=True)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        store=True,
        index=True,
        default=lambda self: self.env.company,
    )
    country_id = fields.Many2one("res.country", string="Country")
    active = fields.Boolean(default=True)
    # readonly = fields.Boolean(default=False) # How to enforce readonly on 'res.field.value' with python?

    @api.model
    def _get_apps(self):
        apps = (
            self.env["ir.module.module"]
            .sudo()
            .search(
                [("application", "=", True), ("state", "=", "installed")],
                order="shortdesc",
            )
        )
        return [(app.name, app.shortdesc) for app in apps] if apps else [("", "")]

    @api.model
    def _get_models(self):
        fields = self.env["ir.model.fields"].search(
            [("name", "=like", "field_value_%")]
        )
        models = self.env["ir.model"].search(
            [("id", "in", [field.model_id.id for field in fields])], order="name"
        )
        return [(model.model, model.name) for model in models]

    @api.onchange("code")
    def _validate_code(self):
        self.code = _validate(self.code, "x_")

    @api.onchange("default_value", "data_type")
    def _onchange_default_value(self):
        if self.data_type and self.default_value:
            date_format = None
            if self.data_type == "date":
                date_format = (
                    self.env["res.lang"]
                    .search([("code", "=", self.env.user.lang)])
                    .ensure_one()
                    .date_format
                )
            self.default_value = _validate(
                self.default_value, self.data_type, date_format
            )

    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get("code"):
            default["code"] = _("%s (copy)") % self.code
        if not default.get("name"):
            default["name"] = _("%s (copy)") % self.name
        return super(ResField, self).copy(default)

    _sql_constraints = [
        (
            "company_model_code_uniq",
            "unique (company_id, model, code)",
            "The model's code must be unique!",
        ),
    ]


class ResFieldSelectionValue(models.Model):

    _name = "res.field.selection_value"
    _description = "Field Selection Value"

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        readonly=True,
        store=True,
        index=True,
        default=lambda self: self.env.company,
    )
    field_id = fields.Many2one("res.field", string="Field", required=True, index=True)
    code = fields.Char("Code")
    name = fields.Char("Name")

    _sql_constraints = [
        (
            "field_code_uniq",
            "unique (field_id, code)",
            "The field's code must be unique!",
        ),
    ]

    # THIS CODE GIVES UnicodeEncodeError: 'ascii' codec can't encode character u'\xf8' in position 1: ordinal not in range(128)
    # Taken from 'account.account'
    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     domain = []
    #     if name:
    #         domain = ['|', ('code', '=ilike', name + '%'), ('name', operator, name)]
    #         if operator in expression.NEGATIVE_TERM_OPERATORS:
    #             domain = ['&', '!'] + domain[1:]
    #     records = self.search(domain + args, limit=limit)
    #     return records.name_get()
    #
    # @api.depends('name', 'code')
    # def name_get(self):
    #     result = []
    #     for record in self:
    #         name = ''
    #         if record.name: name += str(record.name)
    #         result.append((record.id, name))
    #     return result


class ResFieldValue(models.Model):

    _name = "res.field.value"
    _description = "Field Value"

    @api.model
    def _compute_default_model(self):
        try:
            return self.env.context["params"]["model"]
        except:
            raise UserError(_("Please save changes, then refresh the page (F5)."))

    field_id = fields.Many2one(
        "res.field", string="Field", required=True, index=True, ondelete="restrict"
    )
    field_code = fields.Char(
        string="Code", related="field_id.code", store=False, readonly=True
    )
    field_app = fields.Selection(
        string="Application", related="field_id.app", store=False, readonly=True
    )
    field_country_id = fields.Many2one(
        "res.country",
        string="Field Country",
        related="field_id.country_id",
        store=False,
        readonly=True,
    )
    field_data_type = fields.Selection(
        string="Data Type", related="field_id.data_type", store=False, readonly=True
    )
    selection_value_id = fields.Many2one(
        "res.field.selection_value", string="Selection"
    )
    reference_value = fields.Reference("_get_reference_model", string="Reference")
    value = fields.Char()
    model = fields.Char(
        required=True, readonly=True, index=True, default=_compute_default_model
    )
    # TODO: Replace this module with base_sparse_field?
    # Reference ok
    # Date error:

    # from odoo.addons.base_sparse_field.models.fields import Serialized
    # company_colors = fields.Serialized() # field to store JSON
    # color_navbar_bg = fields.Char("Navbar Background Color", sparse="company_colors") # no extra column in the database

    # TODO: res_id = fields.Many2oneReference(model_field="model")
    res_id = fields.Integer(
        required=True, readonly=True, index=True, ondelete="restrict"
    )  # '''ondelete SHOULD NOT be 'cascade', see the write method''')
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        readonly=True,
        store=True,
        index=True,
        default=lambda self: self.env.company,
    )
    company_country_id = fields.Many2one(
        "res.country",
        string="Company Country",
        related="company_id.country_id",
        store=False,
        readonly=True,
    )

    def _valid_field_parameter(self, field, name):
        return name == "ondelete" or super()._valid_field_parameter(field, name)

    @api.model
    def _get_apps(self):
        return self.env["res.field"]._get_apps()

    def _get_reference_model(self):
        models = self.env["ir.model"].search([], order="name")
        return [(model.model, model.name) for model in models]

    @api.onchange("field_id")
    def _onchange_field_id(self):
        self.value = self.field_id.default_value

    @api.onchange("value")
    def _onchange_value(self):
        if self.field_id and self.value:
            date_format = None
            if self.field_id.data_type == "date":
                date_format = (
                    self.env["res.lang"]
                    .search([("code", "=", self.env.user.lang)])
                    .ensure_one()
                    .date_format
                )
            self.value = _validate(self.value, self.field_id.data_type, date_format)

    def write(self, values):
        """
        For models where field_value_ids = fields.One2many('res.field.value', 'res_id'):
        The model assumes that res.field.value 'res_id' has a Many2one relationship to the model.
        When the model imports a new record (with csv/xml),
        it will enforce that the new record.id does not exist in res.field.value 'res_id',
        or give a ParseError if 'res_id' has no attribute 'ondelete'.
        See https://github.com/odoo/odoo/blob/10.0/odoo/fields.py#L2246
                    if inverse_field.ondelete == 'cascade':
                        comodel.search(domain).unlink()
                    else:
                        comodel.search(domain).write({inverse: False})
        res.field.value has records relating to many models, and the 'res_id' should not be changed!
        """
        if "res_id" in values and values["res_id"] == False:
            values.pop("res_id")
        return super(ResFieldValue, self).write(values)

    _sql_constraints = [
        (
            "object_field_uniq",
            "unique (model, res_id, field_id)",
            "The object's fields must be unique!",
        ),
    ]
