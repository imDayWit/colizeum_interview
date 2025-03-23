from ..clients import APIClient
from ..constants import APIKeysEnum, APIURLEnum

__all__ = ["get_weather", "get_city_coords"]


async def get_weather(lat: str, lon: str):
    async with APIClient() as client:
        url = APIURLEnum.OPEN_WEATHER_URL + "data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": APIKeysEnum.OPEN_WEATHER_API,
            "units": "metric",
        }
        data = await client.fetch(url, params=params)
        return {
            "Temperature": data.get("main", {}).get("temp"),
            "Weather": data.get("weather", [{}])[0].get("description"),
        }


async def get_city_coords(city: str):
    async with APIClient() as client:
        url = APIURLEnum.OPEN_WEATHER_URL + "geo/1.0/direct"
        params = {
            "q": f"{city},RU",
            "appid": APIKeysEnum.OPEN_WEATHER_API,
        }
        data = await client.fetch(url, params=params)
        return {
            "City": data[0].get("local_names").get("ru"),
            "Lat": data[0].get("lat"),
            "Lon": data[0].get("lon"),
        }
