from dateutil.relativedelta import relativedelta

from odoo import fields, models


def str2list(str):
    if str:
        return str.strip("] [").split(",")
    else:
        return []


class Recurrences(models.Model):
    _inherit = "project.task.recurrence"

    recurring_fields = fields.Char(
        "Recurring fields",
        help="With ['user_id', 'priority', 'date_deadline'] the next task will be assigned to the same user, with the same priority, with the next deadline.",
    )

    # TODO: Fix: "Error, a partner cannot follow twice the same object."
    # TODO: Archive recurring tasks. "You cannot archive recurring tasks. Please, disable the recurrence first."
    # TODO: Check that the field names exist.
    # @api.model
    # def _get_recurring_fields(self):
    #     standard_recurring_fields = super(Recurrences, self)._get_recurring_fields()
    #     task_recurring_fields = str2list(self.recurring_fields)
    #     return standard_recurring_fields.extend(task_recurring_fields)

    # def _new_task_values(self, task):
    #     create_values = super(Recurrences, self)._new_task_values(task) # hardcoded: {'user_id': False}
    #     if 'user_id' in str2list(self.recurring_fields):
    #         create_values['user_id'] = self.user_id.id
    #     if 'date_deadline' in str2list(self.recurring_fields):
    #         tomorrow = fields.Date.today() + relativedelta(days=1)
    #         create_values['date_deadline'] = self._get_next_recurring_dates(tomorrow, self.repeat_interval, self.repeat_unit, self.repeat_type, self.repeat_until, self.repeat_on_month, self.repeat_on_year, self._get_weekdays(), self.repeat_day, self.repeat_week, self.repeat_month, count=1)
    #     return create_values

    # "'project.task.recurrence' object has no attribute 'user_id'"
    # psycopg2: "invalid input syntax for type date: "[datetime.datetime(2022, 1, 10, 0, 0)]"
    def _new_task_values(self, task):
        create_values = super(Recurrences, self)._new_task_values(task)
        # create_values['user_id'] = self.user_id.id
        tomorrow = fields.Date.today() + relativedelta(days=1)
        # create_values['date_deadline'] = self._get_next_recurring_dates(tomorrow, self.repeat_interval, self.repeat_unit, self.repeat_type, self.repeat_until, self.repeat_on_month, self.repeat_on_year, self._get_weekdays(), self.repeat_day, self.repeat_week, self.repeat_month, count=1)
        return create_values
