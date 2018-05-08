from unittest import TestCase
from unittest.mock import patch
from app.service import business_service, business_delegate



class TestServiceDelegate(TestCase):
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

    @patch("app.service.business_delegate.ServiceDelegate.set_business_service")
    @patch("app.service.business_delegate.ServiceDelegate.to_call",  return_value="response")
    def test_request_get(self, mock_to_call, mock_set_business_service):
        service_delegate = business_delegate.ServiceDelegate(business_service.TheFlash(CPF='10387595612'))
        actual = service_delegate.to_call()
        mock_to_call.assert_called_once_with()
        service_delegate.set_business_service(business_service.SuperMan(CPF='10387595612'))
        self.assertTrue(mock_set_business_service.called)
        self.assertEqual(actual, 'response')
