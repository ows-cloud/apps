This is a base module aiming to apply full security between companies in a database.
Other security modules depend on this one to apply full security for a specific app. 

TECHNICAL

Every model has the `company_id` field. If empty, the company_id is set to 1.

Every model except ir.rule & ir.translation has global security rules. For most models:

- Only read records of the active company / parent companies / child companies.
- Only edit records of the active company.

Security rule domain sections like "company_id=False" are changed to "company_id=1".

By default, security rules are applied also in superuser mode.

A Company Manager can access all models except "ir.config_parameter" & "res.config*".

The Support User can access all companies.

create(), write() and ref() will check that the user can access the record & relations.
TODO: Implement also for x2many relations.
