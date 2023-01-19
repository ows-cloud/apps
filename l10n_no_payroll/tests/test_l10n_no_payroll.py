from odoo.tests.common import TransactionCase


class TestNoPayroll(TransactionCase):
    def setUp(self):
        super().setUp()

        self.TaxDeduction = self.env["l10n.no.tabelltrekk"]
        self.JobCode = self.env["l10n.no.job.code"]

    def test_post_init_hook(self):
        tax_deduction_count = self.TaxDeduction.search_count([])
        self.assertGreater(tax_deduction_count, 200000)

        job_code_count = self.JobCode.search_count([])
        self.assertGreater(job_code_count, 6000)
