from unittest import TestCase

from directory_api_external.buyer import BuyerAPIClient
from tests import stub_request


class BuyerAPIClientTest(TestCase):

    def setUp(self):
        self.client = BuyerAPIClient(
            base_url='https://buyer.com', api_key='test'
        )

    @stub_request('https://buyer.com/api/external/company/supplier/1/', 'get')
    def test_retrieve_supplier_company(self, stub):
        self.client.retrieve_supplier_company(1)
