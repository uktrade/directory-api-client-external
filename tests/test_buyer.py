from unittest import TestCase

from directory_api_external.buyer import BuyerAPIClient


class BuyerAPIClientTest(TestCase):

    def setUp(self):
        self.registration_client = BuyerAPIClient(
            base_url='https://example.com', api_key='test'
        )
