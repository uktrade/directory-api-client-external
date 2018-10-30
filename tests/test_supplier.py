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
            base_url='http://b.co/',
            api_key='test',
            sender_id='some-sender',
            timeout=5,
        )

    @stub_request('http://b.co/supplier-sso/', 'get')
    def test_list_supplier_sso_ids(self, stub):
        self.client.list_supplier_sso_ids()

    @stub_request('http://b.co/supplier/company/', 'get')
    def test_retrieve_supplier_company(self, stub):
        self.client.retrieve_supplier_company(1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 1'

    @stub_request('http://b.co/supplier/', 'get')
    def test_retrieve_supplier_bearer(self, stub):
        self.client.retrieve_supplier(bearer_token=1)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'Bearer 1'

    @stub_request('http://b.co/supplier/', 'get')
    def test_retrieve_supplier_sso_auth(self, stub):
        self.client.retrieve_supplier(sso_session_id=123)

        request = stub.request_history[0]
        assert request.headers['Authorization'] == 'SSO_SESSION_ID 123'
