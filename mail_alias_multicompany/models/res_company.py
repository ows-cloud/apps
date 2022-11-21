from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    """
    User Interface TODO
        Company
            Select domain (separate model)
                Requries a major rewrite of mail.thread message_route.
                I developed almost all except the routing,
                    in the first commit of mail_alias_multicompany
            Change alias_company_name:
                Warning: This will change all the mail aliases of this company!
                (Make a list of the aliases and show what they will be like)
                Warning: Another company may take the previous alias_company_name
                    and receive the emails going to the old aliases!
                To prevent this, you may create a new company
                    and set the previous alias_company_name there.
    """

    alias_company_name = fields.Char(
        "Alias Company Name",
        help="Email Alias will get a dot plus the Alias Company Name, " + \
            "like alias_name.alias_company_name@alias_domain",
    )

    _sql_constraints = [
        (
            "alias_company_name_unique",
            "UNIQUE(alias_company_name)",
            "Unfortunately this company alias is already used, please choose a unique one",
        )
    ]
