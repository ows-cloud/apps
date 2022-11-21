In the xlsx.template, set:
post_import_hook = "${object.excel_post_import_hook('line_ids', ['hook1', 'hook2'])}"

Available hooks:
- 'time_parameter'
