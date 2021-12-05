# JSON field type

This module implements a custom field type for JSON values.

## Why?

JSON can store flexible structured information.

## How to install?

Install the module.

## How to use?

This is a base module to be inherited by other modules.
The value of the JSON field cannot be "changed". Set to empty, then set new value.
Below is example code to use the JSON field type:


from odoo import models
from odoo.addons.json_field.json import 

class MyClass(models.Model)

    jsonfield = JsonField(default={})

    def add_key_value(self):

        jsonfield = dict(company.jsonfield or {})

        jsonfield['mykey'] = 'myvalue'

        company.json = {}
        company.json = company_json


## What to fix?

Would be good to do something in the javascript to format the JSON to be easily readable for the user.

## Author

AppsToGrow
Contact: Henrik Norlin
Email: henrik@appstogrow.co
Mobile: +4791120745

## Supported versions

- 14.0
