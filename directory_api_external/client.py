from directory_api_external.buyer import BuyerAPIClient
from directory_api_external.base import BaseAPIClient


class DirectoryAPIExternalClient(BaseAPIClient):

    def __init__(self, base_url=None, api_key=None):
        self.buyer = BuyerAPIClient(base_url, api_key)
        super().__init__(base_url, api_key)
