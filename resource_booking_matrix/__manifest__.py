# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Resource Booking Matrix',
    'summary': "Useful for scheduling",
    "version": "12.0.1.0.0",
    "author": "Henrik Norlin, "
              "Odoo Community Association (OCA)",
    "website": "https://github.com/apps2grow/apps",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        'resource_booking', # oca/calendar
        'web_widget_x2many_2d_matrix',
    ],
    "data": [
        'security/ir.model.access.csv',
        'wizard/x2m_matrix.xml',
        'views/views.xml',
    ],
    "installable": True,
}
