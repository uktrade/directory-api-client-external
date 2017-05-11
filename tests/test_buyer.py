from unittest import TestCase

from directory_api_external.buyer import BuyerAPIClient
from tests import stub_request


class BuyerAPIClientTest(TestCase):

    def setUp(self):
        self.client = BuyerAPIClient(
            base_url='http://b.co/', api_key='test'
        )

    @stub_request('http://b.co/company/supplier/1/company/', 'get')
    def test_retrieve_supplier_company(self, stub):
        self.client.retrieve_supplier_company(1)

    @stub_request('http://b.co/external/supplier/1/', 'get')
    def test_retrieve_supplier(self, stub):
        self.client.retrieve_supplier(1)
