# Copyright 2019 AppsToGROW - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Survey Action",
    "summary": "Action after completed survey",
    "author": "AppsToGROW",
    "category": "Administration",
    "data": [
        "views/views.xml",
    ],
    "depends": [
        "survey",
        "base_technical_user",
    ],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "version": "14.0.1.0.0",
    "website": "http://www.appstogrow.co",
    "description": """
Successful event survey implementation depends on

1) Survey
Create the survey
On the event, select the survey

2) Mail Template
Admin Mail Templates: "Event: Registration": Duplicate and add a link to the survey: ${object.survey_user_input_id.fill_url}
On the event email schedule, select the mail template

2019) NEW WORKFLOW

BUG: Create new ticket -> registration_ticket_question_id is set to False!
    """,
}
