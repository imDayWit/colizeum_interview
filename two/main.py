import asyncio

from .client import fetch_data
from .process import process_data


async def main():
    data = await fetch_data()
    process_data(data)


if __name__ == "__main__":
    asyncio.run(main())
