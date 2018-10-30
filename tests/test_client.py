from unittest import TestCase

from directory_api_external.client import DirectoryAPIExternalClient
from directory_api_external.supplier import SupplierAPIClient
from directory_api_external.version import __version__
from tests import stub_request


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.client = DirectoryAPIExternalClient(
            base_url='https://buyer.com',
            api_key='test',
            sender_id='some-sender',
            timeout=5,
        )

    @stub_request('https://buyer.com/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()

    def test_supplier(self):
        assert isinstance(self.client.supplier, SupplierAPIClient)
        assert self.client.supplier.base_url == 'https://buyer.com'
        assert (
            self.client.supplier.request_signer.secret == 'test'
        )

    def test_timeout(self):
        assert self.client.timeout == 5

    def test_sender_id(self):
        assert self.client.request_signer.sender_id == 'some-sender'

    def test_version(self):
        assert DirectoryAPIExternalClient.version == __version__
