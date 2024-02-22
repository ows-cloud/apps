# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Calendar Event Matrix",
    "summary": "Schedule attendees",
    "version": "16.0.1.0.0",
    "author": "Ows, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA",
    "license": "AGPL-3",
    "category": "Hidden/Dependency",
    "depends": [
        "calendar",
        "web_widget_x2many_2d_matrix",
        "website_partner",  # views/templates.xml
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
        "views/templates.xml",  # depends on website_partner
    ],
    "installable": True,
    "maintainers": ["ows-cloud"],
}
