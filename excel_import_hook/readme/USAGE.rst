In the xlsx.template, set:
post_import_hook = `"${object.excel_post_import('line_ids', ['action_1', 'action_2'])}"`

In python:

.. code-block:: xml

    def _excel_post_import_action_1(self):
        # do something

    def _excel_post_import_action_2(self):
        # do something
