import aiohttp
from aiohttp import ClientSession

__all__ = ["APIClient"]


class APIClient:
    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def fetch(self, url: str, params: dict = None):
        try:
            async with self.session.get(url, params=params) as response:
                if response.status != 200:
                    raise Exception(
                        f"Something went wrong while fetching data, details:\nStatus Code: {response.status}\nBody: {await response.text()}"
                    )
                return await response.json()
        except aiohttp.ClientError as e:
            raise Exception(e)
