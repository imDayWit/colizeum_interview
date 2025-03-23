import asyncio

from ..constants import FilePath
from ..utils.save_to_sheet import save_to_sheet

__all__ = ["fetch_weather_data"]


async def fetch_weather_data():
    from ..utils import get_all_city_coords, get_weather

    city_coords = await asyncio.gather(get_all_city_coords())
    weather_results = await asyncio.gather(
        *[
            get_weather(city["Lat"], city["Lon"])
            for index, city in city_coords[0].iterrows()
        ]
    )
    city_coords[0]["Temperature"] = [
        weather["Temperature"] for weather in weather_results
    ]
    city_coords[0]["Weather"] = [weather["Weather"] for weather in weather_results]

    save_to_sheet(FilePath.FILE_PATH, "Weather", city_coords[0])
    print("Weather data saved")  # noqa
