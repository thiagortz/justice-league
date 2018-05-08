from unittest import TestCase
from unittest.mock import patch
from app.service.business_service import SolomonGrundy


class TestSolomonGrundy(TestCase):
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

    @patch("app.service.business_service.SolomonGrundy._request_get", return_value="response")
    def test_request_get(self, mock_request_get):
        solomon_grundy = SolomonGrundy(CPF='10387595612')
        actual = solomon_grundy.to_call()
        mock_request_get.assert_called_once_with(resource='5af076bc3100004d0096c66b', params={'CPF': '10387595612'})

        self.assertEqual(actual, 'response')
