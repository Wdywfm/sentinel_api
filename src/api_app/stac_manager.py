from pystac_client import Client

EARTH_SEARCH_URL = "https://earth-search.aws.element84.com/v1"


class StacManager:
    def __init__(self, stac_api_url: str = EARTH_SEARCH_URL):
        self.client: Client = Client.open(stac_api_url)

    def get_image_info_from_polygon(self, polygon: dict) -> dict:
        response = self.client.search(
            max_items=1, collections=["sentinel-2-l2a"], intersects=polygon  # max_items=1 (most recent image)
        )
        items = list(response.items())
        item_info = items[0].to_dict()
        return item_info
