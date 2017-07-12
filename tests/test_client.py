from unittest import TestCase

from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.client import DirectoryAPIExternalClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DirectoryAPIExternalClient(self.base_url, self.api_key)

    def test_supplier(self):
        assert isinstance(self.client.supplier, SupplierAPIClient)
        assert self.client.supplier.base_url == self.base_url
        assert self.client.supplier.request_signer.signer.secret == (
            self.api_key
        )
