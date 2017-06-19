from directory_api_external.base import BaseAPIClient


class SupplierAPIClient(BaseAPIClient):

    endpoints = {
        'supplier-sso-ids': 'supplier-sso/',
    }

    def list_supplier_sso_ids(self):
        url = self.endpoints['supplier-sso-ids']
        return self.get(url)
