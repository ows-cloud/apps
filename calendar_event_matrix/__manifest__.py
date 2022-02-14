# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Calendar Event Matrix',
    'summary': "Schedule people for tasks",
    "version": "14.0.1.0.0",
    "author": "Henrik Norlin, "
              "Odoo Community Association (OCA)",
    "website": "https://github.com/apps2grow/apps",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        'calendar',
        'web_widget_x2many_2d_matrix',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/calendar.event.type.xml',
        'views/calendar.event.type.group.xml',
    ],
    "installable": True,
}
