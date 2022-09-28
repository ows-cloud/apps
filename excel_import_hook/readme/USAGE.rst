In the xlsx.template, set:
post_import_hook = "${object.excel_post_import_hook(one2many_field_name)}"

In python, inherit:
_excel_post_import_hook_for_record()
_excel_post_import_hook_for_record_line()
