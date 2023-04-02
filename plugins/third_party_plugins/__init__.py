from abc import ABC, abstractmethod


class ThirdPartyPlugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def endpoints(self) -> dict:
        pass

    @property
    @abstractmethod
    def headers(self) -> dict:
        pass

    @abstractmethod
    async def process_response(self, response) -> dict:
        pass
