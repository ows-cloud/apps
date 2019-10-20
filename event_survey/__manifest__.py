# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Event Registration Survey',
    'summary': 'Registration Survey for attendees',

    'author': 'AppsToGROW',
    'category': 'Administration',
    'data': [
        'security/security.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/email_template_data.xml',
        'data/server_action.xml',
    ],
    'depends': [
        'website_event_sale',
        'survey_action',
    ],
    'license': 'AGPL-3',
    'version': '13.0.1.0.0',
    'website': 'http://www.appstogrow.org',

    'description': '''
Successful event survey implementation depends on

1) Survey
Create the survey
On the event, select the survey

2) Mail Template
Admin Mail Templates: 'Event: Registration': Duplicate and add a link to the survey: ${object.survey_user_input_id.fill_url}
On the event email schedule, select the mail template

2019) NEW WORKFLOW

BUG: Create new ticket -> registration_ticket_question_id is set to False!
    ''',
}
