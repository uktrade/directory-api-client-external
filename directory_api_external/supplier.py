from directory_client_core.authentication import (
    AuthenticatorNegotiator, SessionSSOAuthenticator
)
from directory_client_core.base import AbstractAPIClient

from directory_api_external.version import __version__


class SupplierAPIClient(AbstractAPIClient):

    endpoints = {
        'supplier-sso-ids': 'supplier-sso/',
        'supplier-company': 'supplier/company/',
        'supplier': 'supplier/'
    }
    version = __version__

    def list_supplier_sso_ids(self):
        url = self.endpoints['supplier-sso-ids']
        return self.get(url)

    def retrieve_supplier_company(self, sso_session_id):
        url = self.endpoints['supplier-company']
        authenticator = SessionSSOAuthenticator(sso_session_id)
        return self.get(url, authenticator=authenticator)

    def retrieve_supplier(self, bearer_token=None, sso_session_id=None):
        authenticator = AuthenticatorNegotiator(
            bearer_token=bearer_token, sso_session_id=sso_session_id
        )
        return self.get(
            self.endpoints['supplier'],
            authenticator=authenticator
        )
