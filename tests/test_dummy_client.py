from unittest import TestCase
from unittest.mock import MagicMock

from directory_api_external.buyer import BuyerAPIClient
from directory_api_external.dummy_client import DummyDirectoryAPIExternalClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DummyDirectoryAPIExternalClient(
            self.base_url, self.api_key
        )

    def test_buyer(self):
        assert isinstance(self.client.buyer, BuyerAPIClient)
        assert self.client.buyer.base_url == self.base_url
        assert self.client.buyer.request_signer.signer.secret == self.api_key

    def test_buyer_send_mocked(self):
        response = self.client.buyer.send(method='get', url='http://1.com')

        assert isinstance(response.json(), MagicMock)
