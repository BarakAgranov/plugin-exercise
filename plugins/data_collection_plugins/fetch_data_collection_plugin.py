import httpx
from . import DataCollector


class FetchData(DataCollector):
    @property
    def collector_type(self):
        return "fetch"

    async def collect_data(self, endpoint: str, headers: dict):
        async with httpx.AsyncClient() as client:
            response = await client.get(endpoint, headers=headers)
            response.raise_for_status()
            return response.json()

