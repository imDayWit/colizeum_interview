import aiohttp

from .contsants import HEADERS, PAYLOAD


async def fetch_data():
    url = "https://www.citilink.ru/graphql/" # todo вынести в константы

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=PAYLOAD, headers=HEADERS) as response:
            if response.status == 200:
                print("CPU data fetched successfully.")  # noqa
                return await response.json()
            print(f"Error: {response.status}")  # noqa
