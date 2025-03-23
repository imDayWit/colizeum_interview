from ..clients import APIClient
from ..constants import APIURLEnum

__all__ = ["get_user"]


async def get_user(num_users: int):
    async with APIClient() as client:
        url = APIURLEnum.RANDOM_USER_URL
        params = {"results": num_users, "exc": "coordinates,login"}
        return await client.fetch(url, params=params)
