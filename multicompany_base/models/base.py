from odoo import api, fields, models
from odoo.exceptions import UserError

MODELS_WITH_REPLACE_RECORD_ID = [
    'mail.template',
]


class Base(models.AbstractModel):
    _inherit = 'base'

    """
    Every model will have 'company_id' field.
    
    Preferrably, 'company_id' should be required.
    Becuase of:
    - clarity
    - later database sharding
    Challenges TODO:
    - New company first creates new partner without company_id.
    - ir.property with blank company_id applies to all (shouldn't be allowed...)
    - ir.default
    - res.users without partner_id needs to read res.partner where company_id is False (ir.rule)
    - Existing records should get company_id BEFORE applying the requirement (pre_init?).

    """

    # Also in multicompany_sudo.patch
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        store=True,
        index=True,
        # required=True,
        default=lambda self: self.env.company,
    )

    def sudo_bypass_global_rules(self):
        try:
            return self.sudo(bypass_global_rules=True)
        except:
            return self.sudo()

    def copy_data(self, default=None):
        vals = super(Base, self).copy_data(default)[0]

        if "website_id" in vals.keys():
            vals["company_id"] = self.sudo_bypass_global_rules().env["website"].browse(default["website_id"]).company_id.id
        elif "company_id" not in vals.keys():
            try:
                vals['company_id'] = self.env.company.id
            except:
                pass

        return [vals]

    """
    XMLID FOR MULTICOMPANY
    Replace res_id if 'replace_record_id' exists.
    """
    @api.model
    def xmlid_lookup(self, xmlid):
        id, model, res_id = super(Base, self).xmlid_lookup(xmlid)
        if model in MODELS_WITH_REPLACE_RECORD_ID:
            try:
                # 'replace_record_id' might not exist
                records = self.env[model].search([('replace_record_id', '=', res_id)])
                updated = False
                # First look for company record
                for record in records:
                    if record.company_id == self.env.company:
                        res_id = record.id
                        updated = True
                # Then look for any record
                if not updated:
                    if len(records) == 1:
                        res_id = records.id
                    else:
                        raise UserError(_("Multiple {model} records, in {companies}.".format(
                            model=model,
                            companies=', '.join([c.name for c in records.mapped('company_id').mapped('name')]),
                        )))
            except:
                pass
        return id, model, res_id
