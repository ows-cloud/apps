from odoo import models
import logging

_logger = logging.getLogger(__name__)


class BaseSetRecordValuesMixin(models.AbstractModel):
    _name = "base.set.record.values.mixin"

    def _set_record_values(self, model_name, domain, values, xmlid=None):
        """ Create or update record.
            If multiple records are found, keep only one record, or log critical error.

            :param model_name: name of model to set record values
            :param domain: domain to search for existing record
            :param values: values to set on record
            DEPRECATED :param xmlid: external id for the record (only for creating new records)

            :return: record with correct values (if ValueError, return None)
        """
        record = self.env[model_name].search(domain)
        if len(record) > 1:
            record = self._deduplicate_or_log_critical_error(domain, record, values.keys())

        if type(record) is ValueError:
            return
        elif len(record) == 0:
            new_record = self.env[model_name].create(values)
            if xmlid:
                self._create_external_id(new_record, xmlid)
        elif len(record) == 1:
            old_values = record.read(fields=values.keys())
            old_values = self._delele_id_and_replace_tuple_with_first_tuple_item(old_values)
            old_values_and_new_values = old_values
            old_values_and_new_values.append(values)
            if not self._values_are_equal(old_values_and_new_values):
                record.write(values)
        return record

    def _deduplicate_or_log_critical_error(self, model_search_domain, records, field_names_which_should_have_same_record_values):
        model_name = records[0]._name
        log_critical = False
        list_of_values = records.read(fields=field_names_which_should_have_same_record_values)
        list_of_values = self._delele_id_and_replace_tuple_with_first_tuple_item(list_of_values)
        if not self._values_are_equal(list_of_values):
            log_critical = True
        if not log_critical:
            # Deduplicate ...
            record_ids = records.ids
            record_to_keep = records.browse(record_ids.pop(0))
            records.browse(record_ids).unlink()
            return record_to_keep
        else:
            # ... or log a critical error.
            error_msg = 'company.security deduplicate: There are {count} conflicting records of model {model_name}. Domain: "{domain}". Conflicing fields: "{fields}".'.format(
                count=len(records), model_name=model_name, domain=model_search_domain, fields=field_names_which_should_have_same_record_values
            )
            # For ir.model.access and ir.rule this is critical!
            _logger.critical(error_msg)
            return ValueError(error_msg)

    def _delele_id_and_replace_tuple_with_first_tuple_item(self, list_of_dict):
        for dict in list_of_dict:
            if 'id' in dict:
                del dict['id']
            for key, value in dict.items():
                if type(value) is tuple:
                    dict[key] = value[0]
        return list_of_dict

    def _values_are_equal(self, list_of_values):
        for values in list_of_values:
            if values != list_of_values[0]:
                return False
        return True

    def _create_external_id(self, record, xmlid):
        xmlid_module, xmlid_name = xmlid.split(".")
        xmlid_record = self.env['ir.model.data'].search([('module','=',xmlid_module), ('name','=',xmlid_name)])
        if xmlid_record:
            if xmlid_record.model != record._name or xmlid_record.res_id != record.id:
                _logger.warning("xmlid {module}.{name} already exists with model {model}, res_id {res_id}!".format(
                    module=xmlid_module,
                    name=xmlid_name,
                    model=xmlid_record.model,
                    res_id=xmlid_record.res_id,
                ))
        else:
            self.env['ir.model.data'].create({
                'module': xmlid_module,
                'name': xmlid_name,
                'model': record._name,
                'res_id': record.id
            })
