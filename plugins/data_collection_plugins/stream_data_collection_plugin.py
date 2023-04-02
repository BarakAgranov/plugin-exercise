import httpx
from . import DataCollector


class StreamData(DataCollector):
    @property
    def collector_type(self):
        return "stream"

    async def collect_data(self, endpoint: str, headers: dict):
        async with httpx.AsyncClient() as client:
            async with client\
                    .stream("GET", endpoint, headers=headers) as response:
                response.raise_for_status()
                data = []
                async for chunk in response.aiter_bytes():
                    data.append(chunk)
                return data
