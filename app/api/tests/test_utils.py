from django.test import SimpleTestCase
from rest_framework import exceptions

from ..utils import custom_exception_handler


class CustomExceptionHandlerTest(SimpleTestCase):

    def setUp(self):
        self.error = exceptions.APIException({'field': 'Some Error'})

    def test_return_json(self):
        resp = custom_exception_handler(self.error, None)
        self.assertEqual(resp.content_type, 'application/json')

    def test_return_status(self):
        resp = custom_exception_handler(self.error, None)
        self.assertEqual(resp.status_code, 500)

    def test_return_data_error(self):
        resp = custom_exception_handler(self.error, None)
        self.assertEqual(str(resp.data['error']), 'Some Error')

    def test_return_data_status(self):
        error = exceptions.APIException()
        resp = custom_exception_handler(error, None)
        self.assertEqual(resp.data['status'], 500)
