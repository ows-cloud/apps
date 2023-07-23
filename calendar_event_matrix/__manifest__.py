# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Calendar Event Matrix",
    "summary": "Schedule attendees",
    "version": "14.0.1.0.0",
    "author": "AppsToGROW," "Odoo Community Association (OCA)",
    "website": "https://github.com/appstogrow/apps",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        "calendar",
        "web_widget_x2many_2d_matrix",
    ],
    "data": [
        "security/calendar_event_matrix_security.xml",
        "security/ir.model.access.csv",
        "views/calendar_attendee_report_views.xml",
        "views/calendar_event_matrix_views.xml",
        "views/calendar_event_views.xml",
        "views/res_partner_views.xml",
        "views/menus.xml",
        "report/report_templates.xml",
        "report/report_views.xml",
    ],
    "installable": True,
    "maintainers": ["appstogrow"],
}
