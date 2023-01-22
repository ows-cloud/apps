from odoo.tests.common import TransactionCase

from odoo.addons.l10n_no_payroll.models.amelding_logic import AmeldingLogikk
from .common import TestNoPayrollBase


class TestNoPayroll(TestNoPayrollBase):
    def setUp(self):
        super().setUp()

        self.TaxDeduction = self.env["l10n.no.tabelltrekk"]
        self.JobCode = self.env["l10n.no.job.code"]

    def test_00_post_init_hook(self):
        tax_deduction_count = self.TaxDeduction.search_count([])
        self.assertGreater(tax_deduction_count, 200000)

        job_code_count = self.JobCode.search_count([])
        self.assertGreater(job_code_count, 6000)

    def test_10_amelding(self):
        a = AmeldingLogikk()
        a.

        self.assertEqual()
