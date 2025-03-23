from ..clients import APIClient
from ..constants import APIKeysEnum, APIURLEnum

__all__ = ["get_news"]


async def get_news(q: str):
    async with APIClient() as client:
        url = APIURLEnum.NEWS_URL
        params = {
            "q": q,
            "apiKey": APIKeysEnum.NEWS_API,
        }
        return await client.fetch(url, params=params)
