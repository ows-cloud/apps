from odoo import api, fields, models, _
from odoo.exceptions import UserError

"""Migration before uninstall l10n_multilang"""

FIELDS = [
    ('account.account', 'name'),
    ('account.account.tag', 'name'),
    ('account.account.template', 'name'),
    ('account.analytic.account', 'name'),
    ('account.chart.template', 'name'),
    ('account.chart.template', 'spoken_languages'),
    ('account.fiscal.position', 'name'),
    ('account.fiscal.position', 'note'),
    ('account.fiscal.position.template', 'name'),
    ('account.fiscal.position.template', 'note'),
    ('account.group', 'name'),
    ('account.group.template', 'name'),
    ('account.journal', 'name'),
    ('account.tax', 'description'),
    ('account.tax', 'name'),
    ('account.tax.report.line', 'name'),
    ('account.tax.report.line', 'tag_name'),
    ('account.tax.template', 'description'),
    ('account.tax.template', 'name'),
    ('res.country.state', 'name'),
]


class Company(models.Model):
    _inherit = "res.company"

    def before_uninstall_l10n_multilang(self):
        def get_translations(model_name, field_name):
            table_name = model_name.replace('.', '_')
            column_name = field_name
            translation_name = model_name + ',' + field_name
            sql = """
                SELECT r.id, r.company_id, c.name, '{translation_name}', r.{column_name}, t.src, t.lang, t.value
                FROM {table_name} r left join ir_translation t on r.id = t.res_id left join res_company c on r.company_id = c.id
                WHERE t.name = '{translation_name}'
                ORDER BY company_id, id;
                """.format(table_name=table_name, column_name=column_name, translation_name=translation_name)
            self.env.cr.execute(sql)
            data = self.env.cr.fetchall()
            return data
        
        def set_new_value(model_name, field_name, record_id, new_value):
            table_name = model_name.replace('.', '_')
            column_name = field_name
            new_value = new_value.replace("'", "''")
            sql = """
                UPDATE {table_name}
                SET {column_name} = '{new_value}'
                WHERE id = {record_id}
                """.format(table_name=table_name, column_name=column_name, new_value=new_value, record_id=record_id)
            self.env.cr.execute(sql)

        #csv = 'r.id, r.company_id, c.name, model_field, r.name, t.src, t.lang, t.value\n'
        for model_name, field_name in FIELDS:
            translations = get_translations(model_name, field_name)
            for t in translations:
                record_id = t[0]
                company_id = t[1]
                field_value = t[4]
                lang = t[6]
                translated_value = t[7]
                use_lang = 'en_GB' if company_id in (1,5,8) else 'nb_NO'
                if lang != use_lang:
                    continue
                if not translated_value:
                    continue
                if translated_value != field_value:
                    new_value = "{} ({})".format(translated_value, field_value)
                    set_new_value(model_name, field_name, record_id, new_value)

                    
            #    csv += '"{}","{}","{}","{}","{}","{}","{}","{}"\n'.format(t[0],t[1],t[2],t[3],t[4],t[5],t[6],t[7])
        #raise UserError(csv)
