from unittest import TestCase
from unittest.mock import MagicMock

from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.dummy_client import DummyDirectoryAPIExternalClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.client = DummyDirectoryAPIExternalClient(
            base_url='http://1.com/',
            api_key='test',
            sender_id='some-sender',
            timeout=5,
        )

    def test_supplier(self):
        supplier = self.client.supplier
        assert isinstance(supplier, SupplierAPIClient)
        assert supplier.base_url == 'http://1.com/'
        assert supplier.request_signer.secret == 'test'

    def test_supplier_send_mocked(self):
        response = self.client.supplier.send(method='get', url='http://1.com')

        assert isinstance(response.json(), MagicMock)
