from unittest import TestCase
from unittest.mock import patch
from app.data.query import Query


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

    @patch("app.service.business_service.SuperMan._request_get")
    def test_resolve_score(self, mock_superman_request_get):
        mock_superman_request_get.return_value.ok = True
        mock_superman_request_get.return_value.text = '{"id": "15","pointing": 68.6,"last_query": "2017-11-22T21:13:28Z"}'

        query = Query()

        actual = query.resolve_score({'teste': 'teste'}, '10387595612')

        mock_superman_request_get.assert_called_once_with(resource='5af099f2310000610096c6ee',
                                                          params={'CPF': '10387595612'})

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual._fields, tuple)

    @patch("app.service.business_service.SuperMan._request_get")
    @patch("app.service.business_service.TheFlash._request_get")
    @patch("app.service.business_service.SolomonGrundy._request_get")
    def test_resolve_client(self, mock_sg_request_get, mock_tf_request_get, mock_sm_request_get):
        mock_sg_request_get.return_value.ok = True
        mock_sg_request_get.return_value.text = '{"id": "1","name": "Thiago Dias", "CPF":"59865377691", ' \
                                                '"birth": "1991-05-21"}'

        mock_tf_request_get.return_value.ok = True
        mock_tf_request_get.return_value.text = '{"id": "15","financial_movement": 68.6,' \
                                                '"last_query": "2017-11-22T21:13:28Z",' \
                                                '"last_buy":{"id": "15","value": 60.6,"credit_card":{"id": 21,' \
                                                '"number": "5547-7221-7804-6353","validity":"07/11/2019"}}}'

        mock_sm_request_get.return_value.ok = True
        mock_sm_request_get.return_value.text = '{"id": "15","pointing": 68.6,"last_query": "2017-11-22T21:13:28Z"}'

        query = Query()

        actual = query.resolve_client({'teste': 'teste'}, '10387595612')

        mock_sm_request_get.assert_called_once_with(resource='5af099f2310000610096c6ee',
                                                    params={'CPF': '10387595612'})

        mock_tf_request_get.assert_called_once_with(resource='5af0bb973100004a0096c74d',
                                                    params={'CPF': '10387595612'})

        mock_sg_request_get.assert_called_once_with(resource='5af076bc3100004d0096c66b',
                                                    params={'CPF': '10387595612'})

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual._fields, tuple)


    @patch("app.service.business_service.TheFlash._request_get")
    def test_resolve_event(self, mock_tf_request_get):
        mock_tf_request_get.return_value.ok = True
        mock_tf_request_get.return_value.text = '{"id": "15","financial_movement": 68.6,' \
                                                '"last_query": "2017-11-22T21:13:28Z",' \
                                                '"last_buy":{"id": "15","value": 60.6,"credit_card":{"id": 21,' \
                                                '"number": "5547-7221-7804-6353","validity":"07/11/2019"}}}'

        query = Query()

        actual = query.resolve_event({'teste': 'teste'}, '10387595612')

        mock_tf_request_get.assert_called_once_with(resource='5af0bb973100004a0096c74d',
                                                    params={'CPF': '10387595612'})

        self.assertIsNotNone(actual)
        self.assertIsInstance(actual._fields, tuple)
