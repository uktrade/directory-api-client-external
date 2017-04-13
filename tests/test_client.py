from unittest import TestCase

from directory_api_external.buyer import BuyerAPIClient
from directory_api_external.client import DirectoryAPIExternalClient


class DirectoryAPIExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://buyer.com'
        self.api_key = 'test'
        self.client = DirectoryAPIExternalClient(self.base_url, self.api_key)

    def test_buyer(self):
        assert isinstance(self.client.buyer, BuyerAPIClient)
        assert self.client.buyer.base_url == self.base_url
        assert self.client.buyer.request_signer.signer.secret == self.api_key
