# TEST ALLE NOEDVENDIGE LOENNSARTER: fastloenn, timeloenn, km, telefon, pensjon(aga), sykepenger(aga), feriepenger forrige aar, feriepenger dette aar
# hr_professional hr.employee: tax_table, tax_percent
# ag_4_professional: new company implement HR: base.key.value.field

from odoo.fields import Date
from odoo.tests.common import TransactionCase


class TestPayslipBase(TransactionCase):
    def setUp(self):
        super(TestPayslipBase, self).setUp()

        # Company
        #
        self.company = self.env["res.company"].create(
            [
                {
                    "l10n_no_Grunnlagsprosent": "14.1",
                    "vat": "NO913860128",
                    "l10n_no_virksomhet": "913864042",
                    "l10n_no_Spraak": "bokmaal",
                    "l10n_no_BeregningskodeForArbeidsgiveravgift": "generelleNaeringer",
                    "l10n_no_Arbeidsgiveravgiftsone": "1",
                }
            ],
        )
        self = self.with_company(self.company)

        self.Amelding = self.env["l10n.no.amelding"]
        self.Contract = self.env["hr.contract"]
        self.Employee = self.env["hr.employee"]
        self.job = self.env["hr.job"]
        self.Payslip = self.env["hr.payslip"]
        self.PayslipLine = self.env["hr.payslip.line"]
        # self.PayrollStructure = self.env["hr.payroll.structure"]
        # self.RuleInput = self.env["hr.rule.input"]
        self.SalaryRule = self.env["hr.salary.rule"]
        # self.SalaryRuleCateg = self.env["hr.salary.rule.category"]

        # A-melding
        #
        # self.amelding = self.Amelding.create(
        #     [
        #         {
        #             "leveringstidspunkt": "2008-09-29 03:49:45",
        #             "kalendermaaned": "2018-01",
        #             "meldingsId": "2",
        #             "erstatterMeldingsId": False,
        #         },
        #     ],
        # )


        # Employee
        #
        self.employee = self.Employee.create(
            [
                {
                    "name": "Ola Nordmann",
                    "birthday": "2000-01-01",
                }
            ],
        )

        # Contract
        #
        self.contract = self.Contract.create(
            [
                {
                    "employee_id": self.employee.id,
                    "date_start": "2020-01-01",
                    "l10n_no_Arbeidsforholdtype": "ordinaertArbeidsforhold",
                    "l10n_no_antallTimerPerUkeSomEnFullStillingTilsvarer": 37.5,
                    "l10n_no_Arbeidstidsordning": "ikkeSkift",
                }
            ],
        )

        # Payslip
        #
        self.payslip = self.Payslip.create(
            [
                {
                    "id": 0,
                    "employee_id": ("hr.employee", 0),
                }
            ],
        )

        # PayslipLine
        #
        self.payslip_line = self.PayslipLine.create(
            [
                {
                    "id": 0,
                    "slip_id": ("hr.payslip", 0),
                    "salary_rule_id": ("hr.salary.rule", 0),
                    "total": 5000.0,
                },
                {
                    "id": 1,
                    "slip_id": ("hr.payslip", 0),
                    "salary_rule_id": ("hr.salary.rule", 1),
                    "total": 1000.0,
                },
                {
                    "id": 2,
                    "slip_id": ("hr.payslip", 0),
                    "salary_rule_id": ("hr.salary.rule", 2),
                    "total": 500.0,
                },
                {
                    "id": 3,
                    "slip_id": ("hr.payslip", 0),
                    "salary_rule_id": ("hr.salary.rule", 3),
                    "total": -2000.0,
                },
                {
                    "id": 4,
                    "slip_id": ("hr.payslip", 0),
                    "salary_rule_id": ("hr.salary.rule", 4),
                    "total": -900.0,
                },
            ],
        )

        # SalaryRule
        #
        self.salary_rule = self.SalaryRule.create(
            [
                {
                    "id": 0,
                    "l10n_no_RegelType": "loennsinntekt",
                    "l10n_no_Fordel": "kontantytelse",
                    "l10n_no_Loennsbeskrivelse": "fastloenn",
                    "l10n_no_BeregnAga": "loennOgGodtgjoerelse",
                    "l10n_no_BeregnTrekk": "tabelltrekk",
                    "l10n_no_SkatteOgAvgiftsregel": "skattefriOrganisasjon",
                },
                {
                    # IKKE LOENN!
                    "id": 1,
                    "l10n_no_RegelType": "loennsinntekt",
                    "l10n_no_Fordel": "naturalytelse",
                    "l10n_no_Loennsbeskrivelse": "annet",
                    "l10n_no_BeregnAga": "tilskuddOgPremieTilPensjon",
                    "l10n_no_BeregnTrekk": False,
                },
                {
                    "id": 2,
                    "l10n_no_RegelType": "loennsinntekt",
                    "l10n_no_Fordel": "utgiftsgodtgjoerelse",
                    "l10n_no_Loennsbeskrivelse": "kilometergodtgjoerelseBil",
                },
                {
                    # IKKE LOENN!
                    "id": 3,
                    "l10n_no_RegelType": "loennsinntekt",
                    "l10n_no_Fordel": "naturalytelse",
                    "l10n_no_Loennsbeskrivelse": "kilometergodtgjoerelseBil",
                    "l10n_no_BeregnAga": "fradragIGrunnlagetForSone",
                    "l10n_no_BeregnTrekk": False,
                },
                {
                    "id": 4,
                    "l10n_no_RegelType": "forskuddstrekk",
                },
            ],
        )

        # Job
        #
        self.job = self.Job.create(
            [
                {
                    "name": "Assistent",
                    "l10n_no_profession_code": "1234567",
                }
            ],
        )
