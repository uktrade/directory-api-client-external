from unittest import TestCase
from unittest.mock import MagicMock

from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.dummy_client import DummyDirectoryAPIExternalClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DummyDirectoryAPIExternalClient(
            self.base_url, self.api_key
        )

    def test_supplier(self):
        supplier = self.client.supplier
        assert isinstance(supplier, SupplierAPIClient)
        assert supplier.base_url == self.base_url
        assert supplier.request_signer.signer.secret == self.api_key

    def test_supplier_send_mocked(self):
        response = self.client.supplier.send(method='get', url='http://1.com')

        assert isinstance(response.json(), MagicMock)
