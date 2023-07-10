from datetime import date

from odoo.tests.common import TransactionCase


class TestTimeParameter(TransactionCase):
    def setUp(self):
        super(TestTimeParameter, self).setUp()

        self.account_adra = self.env["account.account"].create(
            {
                "code": "123001",
                "name": "Donations for ADRA",
                "user_type_id": self.env.ref(
                    "account.data_account_type_other_income"
                ).id,
            }
        )
        self.account_church = self.env["account.account"].create(
            {
                "code": "123002",
                "name": "Donations for the local church",
                "user_type_id": self.env.ref(
                    "account.data_account_type_other_income"
                ).id,
            }
        )
        version_adra = {
            "date_from": date(2022, 12, 3),
            "value_reference": "account.account,{}".format(self.account_adra.id),
        }
        version_church = {
            "date_from": date(2022, 12, 10),
            "value_reference": "account.account,{}".format(self.account_church.id),
        }
        self.reference_parameter = self.env["base.time.parameter"].create(
            {
                "name": "Donations",
                "model_id": self.env.ref("account.model_account_move").id,
                "type": "record",
                "version_ids": [(0, 0, version_adra), (0, 0, version_church)],
            }
        )
        acc_version_adra = {
            "date_from": date(2023, 1, 7),
            "value_account_id": self.account_adra.id,
        }
        acc_version_church = {
            "date_from": date(2023, 1, 14),
            "value_account_id": self.account_church.id,
        }
        self.account_parameter = self.env["base.time.parameter"].create(
            {
                "name": "Donations",
                "model_id": self.env.ref("account.model_account_move").id,
                "type": "record",
                "record_model": "account.account",
                "version_ids": [(0, 0, acc_version_adra), (0, 0, acc_version_church)],
            }
        )

    def test_00_get(self):
        value = self.reference_parameter._get(date(2022, 12, 3))
        self.assertEqual(value, self.account_adra, "Account for ADRA donations")

        value = self.reference_parameter._get(date(2022, 12, 12))
        self.assertEqual(value, self.account_church, "Account for church donations")

        value = self.account_parameter._get(date(2023, 1, 7))
        self.assertEqual(value, self.account_adra, "Account for ADRA donations")

        value = self.account_parameter._get(date(2023, 1, 20))
        self.assertEqual(value, self.account_church, "Account for church donations")
