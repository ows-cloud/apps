from odoo import fields, models


class JobCode(models.Model):
    _name = "l10n.no.job.code"
    _description = "Norwegian Profession Codes"

    name = fields.Char()
    code = fields.Char()

    def import_job_codes(self):

        import_record = self.env['base_import.import'].create({
            # "file": file.read(),
            "file": b"name,code\nHenrik Norlin,+4791120745\n",
            "file_name": "l10n.no.job.code.csv",
            "file_type": "text/csv",
        })
        import_record.do(
            columns="name,code",
            fields="name,code",
            options={
                'headers': True,
                'advanced': False,
                'keep_matches': False,
                'name_create_enabled_fields': {},
                'skip': 0,
                'limit': 2000,
                'encoding': 'ascii',
                'separator': ',',
                'quoting': '"',
                'sheet': '',
                'date_format': '',
                'datetime_format': '',
                'float_thousand_separator': ',',
                'float_decimal_separator': '.',
                'fields': [],
            },
        )
