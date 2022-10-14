In the xlsx.template, set:
post_import_hook = "${object.excel_post_import_hook('line_ids', ['name1', 'name2'])}"

In python, create:
_excel_post_import_hook_name1()
_excel_post_import_hook_name2()
