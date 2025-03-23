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

    # todo handle errors
    async def fetch(self, url: str, params: dict = None):
        async with self.session.get(url, params=params) as response:
            return await response.json()
