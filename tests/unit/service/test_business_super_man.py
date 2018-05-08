from unittest import TestCase
from unittest.mock import patch
from app.service.business_service import SuperMan


class TestSuperMan(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("app.service.business_service.SuperMan._request_get", return_value="response")
    def test_request_get(self, mock_request_get):
        super_man = SuperMan(CPF='10387595612')
        actual = super_man.to_call()
        mock_request_get.assert_called_once_with(resource='5af099f2310000610096c6ee', params={'CPF': '10387595612'})

        self.assertEqual(actual, 'response')
