# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Calendar Event Matrix",
    "summary": "Schedule attendees",
    "version": "14.0.1.0.0",
    "author": "AppsToGROW," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-tools",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        "calendar",
        "web_widget_x2many_2d_matrix",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/calendar.event.matrix.xml",
        "report/report_templates.xml",
        "report/report_views.xml",
    ],
    "installable": True,
}
