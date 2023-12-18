import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    language_ids = fields.Many2many("res.lang", string="Languages")


class IrTranslation(models.Model):
    _inherit = "ir.translation"

    company_id = fields.Many2one("res.company")

    @api.model
    def create(self, vals):
        # source method create: base\ir\ir_translation.py _set_ids
        # _logger.debug('ir.translation create: vals = ' + str(vals))
        if vals.get("company_id"):
            if type(vals["company_id"]) is tuple:
                vals["company_id"] = vals["company_id"][0]
        else:
            model, field = vals["name"].split(",")
            res = self.env[model].browse(vals["res_id"])
            vals["company_id"] = self._get_company_id(res)

        record = super(IrTranslation, self.sudo()).create(vals).with_env(self.env)
        return record

    #   copied from base/ir/ir_translation.py (v10)
    #   new: 'company_id', 'language_ids', 'model_has_company_id'
    @api.model
    def insert_missing(self, field, records):
        """Insert missing translations for `field` on `records`."""
        records = records.with_context(lang=None)
        external_ids = records.get_external_id()  # if no xml_id, empty string
        model_has_company_id = bool(
            self.env["ir.model.fields"].search_count(
                [("name", "=", "company_id"), ("model", "=", field.model_name)]
            )
        )

        if not model_has_company_id:
            pass
        elif callable(field.translate):
            # insert missing translations for each term in src
            query = """
INSERT INTO ir_translation (lang, type, name, res_id, src, value, module, company_id)
SELECT l.code, 'model_terms', %(name)s, %(res_id)s, %(src)s, %(src)s, %(module)s, %(company_id)s
FROM res_lang l
WHERE l.id IN %(language_ids)s AND l.active AND NOT EXISTS (
    SELECT 1 FROM ir_translation
    WHERE lang=l.code
    AND type='model'
    AND name=%(name)s
    AND res_id=%(res_id)s
    AND src=%(src)s
);
            """
            for record in records.filtered(lambda r: r.company_id.id > 1):
                module = external_ids[record.id].split(".")[0]
                src = record[field.name] or None
                language_ids = record.company_id.language_ids.ids
                for term in set(field.get_trans_terms(src)):
                    self._cr.execute(
                        query,
                        {
                            "name": "%s,%s" % (field.model_name, field.name),
                            "res_id": record.id,
                            "src": term,
                            "company_id": self._get_company_id(record),
                            "language_ids": tuple(language_ids)
                            if language_ids
                            else (0,),
                            "module": module,
                        },
                    )
        else:
            # insert missing translations for src
            query = """
INSERT INTO ir_translation (lang, type, name, res_id, src, value, module, company_id)
SELECT l.code, 'model', %(name)s, %(res_id)s, %(src)s, %(src)s, %(module)s, %(company_id)s
FROM res_lang l
WHERE l.id IN %(language_ids)s AND l.active AND NOT EXISTS (
    SELECT 1 FROM ir_translation
    WHERE lang=l.code AND type='model' AND name=%(name)s AND res_id=%(res_id)s
);
UPDATE ir_translation SET src=%(src)s
WHERE type='model' AND name=%(name)s AND res_id=%(res_id)s;
            """
            for record in records.filtered(lambda r: r.company_id.id > 1):
                module = external_ids[record.id].split(".")[0]
                language_ids = record.company_id.language_ids.ids
                self._cr.execute(
                    query,
                    {
                        "name": "%s,%s" % (field.model_name, field.name),
                        "res_id": record.id,
                        "src": record[field.name] or None,
                        "company_id": self._get_company_id(record),
                        "language_ids": tuple(language_ids) if language_ids else (0,),
                        "module": module,
                    },
                )

        self._modified_model(field.model_name)

    def _get_company_id(self, record):
        record.ensure_one()
        if hasattr(record, "company_id"):
            return record.company_id.id
        elif record._name == "res.company":
            return record.id
        return 1

    # - raise ValidationError(_("Translation is not valid:\n%s") % val)
    # + r = trans
    # + raise ValidationError(_("""Translation is not valid:
    @api.constrains("type", "name", "value")
    def _check_value(self):
        for trans in self.with_context(lang=None):
            if trans.type == "model" and trans.value:
                mname, fname = trans.name.split(",")
                record = trans.env[mname].browse(trans.res_id)
                field = record._fields[fname]
                if callable(field.translate):
                    src = trans.src
                    val = trans.value.strip()
                    # check whether applying (src -> val) then (val -> src)
                    # gives the original value back
                    value0 = field.translate(lambda term: None, record[fname])
                    value1 = field.translate({src: val}.get, value0)
                    # don't check the reverse if no translation happened
                    if value0 == value1:
                        continue
                    value2 = field.translate({val: src}.get, value1)
                    if value2 != value0:
                        r = trans
                        raise ValidationError(
                            _(
                                """Translation is not valid:
                                val: %s, \nlang: %s, \nname: %s,
                                \nres_id: %s, \nsource: %s,
                                \nsrc: %s, \ntype: %s, \nvalue: %s, \nvalue0: %s,
                                \nvalue1: %s, \nvalue2: %s
                                """
                            )
                            % (
                                val,
                                r.lang,
                                r.name,
                                r.res_id,
                                r.source,
                                r.src,
                                r.type,
                                r.value,
                                value0,
                                value1,
                                value2,
                            )
                        )
