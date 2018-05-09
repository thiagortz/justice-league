from unittest import TestCase
from unittest.mock import patch
from app.service.business_service import TheFlash


class TestTheFlash(TestCase):
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

    @patch("app.service.business_service.TheFlash._request_get", return_value="response")
    def test_request_get(self, mock_request_get):
        the_flash = TheFlash(CPF='10387595612')
        actual = the_flash.to_call()
        mock_request_get.assert_called_once_with(resource='5af0bb973100004a0096c74d', params={'CPF': '10387595612'})

        self.assertEqual(actual, 'response')
