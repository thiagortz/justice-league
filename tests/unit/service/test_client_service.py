from unittest import TestCase
from unittest.mock import patch
from app.service import business_delegate, client, business_service


class TestClient(TestCase):
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

    @patch("app.service.client.Client.to_call", return_value="response")
    def test_request_get(self, mock_to_call):
        client_service = client.Client(business_delegate.ServiceDelegate(business_service.SuperMan(CPF='10387595612')))
        actual = client_service.to_call()
        mock_to_call.assert_called_once_with()

        self.assertEqual(actual, 'response')
