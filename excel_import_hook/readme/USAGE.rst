In the xlsx.template, set:
post_import_hook = "${object.excel_post_import('line_ids', ['name1', 'name2'])}"

In python, create:
_excel_post_import_name1()
_excel_post_import_name2()
