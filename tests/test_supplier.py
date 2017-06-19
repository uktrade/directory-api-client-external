from unittest import TestCase

from directory_api_external.supplier import SupplierAPIClient
from tests import stub_request


class SupplierAPIClientTest(TestCase):
    """
    The tests dont' have any assert because the "magic" happens implicitly
    at the stub_request decorator level.

    The decorator results in an exception being thrown if the url
    being requested is not as defined in the decorator
    """

    def setUp(self):
        self.client = SupplierAPIClient(
            base_url='http://b.co/', api_key='test'
        )

    @stub_request('http://b.co/supplier-sso/', 'get')
    def test_list_supplier_sso_ids(self, stub):
        self.client.list_supplier_sso_ids()
