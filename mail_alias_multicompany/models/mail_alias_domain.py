from odoo import _, api, fields, models


class AliasDomain(models.Model):
    """
    mail.thread message_route is separating 'localparts' from the @domain.
    Using multiple domain will require a major rewrite of message_route.
    It is not as easy as this:
    Routing incoming email:
        alias_domain = self.env['mail.alias.domain'].search([('name', '=', email_domain)])
        alias = self.search([('alias_name', '=', email_alias), ('alias_domain_id', '=', alias_domain.id)])
    
    """
    _name = 'mail.alias.domain'
    _description = "Mail Alias Domain"

    name = fields.Char("Domain Name")
    company_id = fields.Many2one('res.company', string="Company")
    require_alias_company_name = fields.Boolean("Require Company Alias Name",
        help="Email aliases will be like alias_name.alias_company_name@alias_domain",
    )

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'This domain is already existing!')
    ]

    @api.model
    def create(self, vals):
        self._validate_domain()
        return super(AliasDomain, self).create(vals)

    def write(self, vals):
        self._validate_domain()
        return super(AliasDomain, self).write(vals)

    def _validate_domain(self):
        # TODO: Make a DNS challenge for the user, and check DNS to make sure that the company is the owner of the domain.
        # TODO: It should NOT be possible to change the name! Rather make a new domain record with a new name.
        pass
