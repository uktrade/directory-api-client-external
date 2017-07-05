from directory_api_external.base import BaseAPIClient


class BuyerAPIClient(BaseAPIClient):

    endpoints = {
        'supplier-company': 'supplier/company/',
        'supplier': 'supplier/'
    }

    def retrieve_supplier_company(self, sso_session_id):
        url = self.endpoints['supplier-company']
        return self.get(url, sso_session_id=sso_session_id)

    def retrieve_supplier(self, sso_session_id):
        url = self.endpoints['supplier']
        return self.get(url, sso_session_id=sso_session_id)
