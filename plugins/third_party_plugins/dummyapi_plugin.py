from . import ThirdPartyPlugin


class DummyapiPlugin(ThirdPartyPlugin):

    @property
    def name(self):
        return "dummyapi"

    @property
    def endpoints(self) -> dict:
        return {"user": "https://dummyapi.io/data/v1/user",
                "post": "https://dummyapi.io/data/v1/post",
                "comment": "https://dummyapi.io/data/v1/comment",
                "tag": "https://dummyapi.io/data/v1/tag"}

    @property
    def headers(self):
        return {
            "app-id": "6427452fc8083ceea5c75741",
            "Content-Type": "application/json",
        }

    async def process_response(self, response):
        print(response)
