from abc import ABC, abstractmethod

class DataCollector(ABC):
    @property
    @abstractmethod
    def collector_type(self) -> str:
        pass

    @abstractmethod
    async def collect_data(self, endpoint: str, headers: dict):
        pass
