from directory_api_external.base import BaseAPIClient
from directory_api_external.authentication import (
    BearerAuthenticator, SessionSSOAuthenticator
)


class SupplierAPIClient(BaseAPIClient):

    endpoints = {
        'supplier-sso-ids': 'supplier-sso/',
        'supplier-company': 'supplier/company/',
        'supplier': 'supplier/'
    }

    def list_supplier_sso_ids(self):
        url = self.endpoints['supplier-sso-ids']
        return self.get(url)

    def retrieve_supplier_company(self, sso_session_id):
        url = self.endpoints['supplier-company']
        authenticator = SessionSSOAuthenticator(sso_session_id)
        return self.get(url, authenticator=authenticator)

    def retrieve_supplier(self, bearer_token):
        url = self.endpoints['supplier']
        authenticator = BearerAuthenticator(bearer_token)
        return self.get(url, authenticator=authenticator)
