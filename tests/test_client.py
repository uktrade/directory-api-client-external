from unittest import TestCase

from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.client import DirectoryAPIExternalClient
from tests import stub_request


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DirectoryAPIExternalClient(self.base_url, self.api_key)

    def test_supplier(self):
        assert isinstance(self.client.supplier, SupplierAPIClient)
        assert self.client.supplier.base_url == self.base_url
        assert self.client.supplier.request_signer.secret == (
            self.api_key
        )

    @stub_request('https://buyer.com/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()
