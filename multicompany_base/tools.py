# TODO: ir.cron should pass context to include in "with_context" for better performance.
def _prepare(self, company):
    self = self.with_user(
        self.env.ref("__multicompany_base__.support_user")
    ).with_context(
        active_test=False,
        allowed_company_ids=[company.id],
    )
    self.env.company = company
    self.env.companies = company
    return self
