from odoo import models, fields, api


class Tasks(models.Model):
    _inherit = 'project.task'

    recurring_fields = fields.Char("Recurring fields",
        compute='_compute_repeat',
        help="With ['user_id', 'date_deadline'] the next task will be assigned to the same user, with the next deadline.")

    @api.model
    def _get_recurrence_fields(self):
        task_recurrence_fields = super(Tasks, self)._get_recurrence_fields()
        task_recurrence_fields.append('recurring_fields')
        return task_recurrence_fields
