import asyncio

from .utils import fetch_weather_data, init_excel_file, save_news, save_user_data


async def main():
    init_excel_file()
    await asyncio.gather(fetch_weather_data(), save_news(), save_user_data())


if __name__ == "__main__":
    asyncio.run(main())
