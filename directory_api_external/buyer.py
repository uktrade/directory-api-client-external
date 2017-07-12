from directory_api_external.base import BaseAPIClient

from directory_api_external.authentication import (
    BearerAuthenticator, SessionSSOAuthenticator
)


class BuyerAPIClient(BaseAPIClient):

    endpoints = {
        'supplier-company': 'supplier/company/',
        'supplier': 'supplier/'
    }

    def retrieve_supplier_company(self, sso_session_id):
        url = self.endpoints['supplier-company']
        authenticator = SessionSSOAuthenticator(sso_session_id)
        return self.get(url, authenticator=authenticator)

    def retrieve_supplier(self, bearer_token):
        url = self.endpoints['supplier']
        authenticator = BearerAuthenticator(bearer_token)
        return self.get(url, authenticator=authenticator)
