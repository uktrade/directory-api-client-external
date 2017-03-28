from directory_api_external.base import BaseAPIClient


class BuyerAPIClient(BaseAPIClient):

    endpoints = {
        'supplier-company': 'company/supplier/{sso_id}/company/'
    }

    def retrieve_supplier_company(self, sso_id):
        url = self.endpoints['supplier-company'].format(sso_id=sso_id)
        return self.get(url)
