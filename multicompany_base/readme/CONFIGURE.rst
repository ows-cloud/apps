Only the administrator has access to the app settings.
Company settings should be configured in the company form.
User access rights should be configured in the user form.

TECHNICAL

The system parameters below are created by `post_init_hook`.
By default, they will trigger actions after install/update/uninstall a module:

- `multicompany_base.force_security`: Update the security.
- `multicompany_base.force_security_company_manager`: Update the company manager security.
- `multicompany_base.force_config`: Configure the system and companies to work properly.

In production, all actions should be triggered.
In development, it is sometimes useful to disable a blocking action.
They can be run manually from the Security / Technical / Security menu.

SECURITY IMPLEMENTATION

When the active company is not the user's default company,
controllers and "stored fields compute all" etc. may not know the company of a record.
Resolve it with these methods:

`record_company()` returns the company of the record.
It also works for a recordset if all records have the same company.

`with_record_company()` returns the recordset with the right company in the environment.

TODO:
Set the active company as env.company in a central place, so controllers will know the company by default?
request.httprequest.cookies.get("cids") - The first cid is the active company.

`sudo_bypass_global_rules()` will bypass the global rules in sudo mode.
Never use this method, except when there is no alternative.
