import asyncio

from pandas import DataFrame

__all__ = ["get_all_city_coords"]

CITIES = [
    "Moscow",
    "Saint Petersburg",
    "Novosibirsk",
    "Yekaterinburg",
    "Zelenograd",
    "Chelyabinsk",
    "Bratsk",
    "Samara",
    "Rostov na Donu",
    "Ufa",
    "Krasnoyarsk",
    "Voronezh",
    "Vologda",
    "Volgograd",
    "Krasnodar",
    "Ulan Ude",
    "Tyumen",
    "Istra",
    "Esentuki",
    "Barnaul",
    "Ulyanovsk",
    "Irkutsk",
    "Khabarovsk",
    "Vladikavkaz",
    "Vladivostok",
    "Makhachkala",
    "Tomsk",
    "Orenburg",
    "Kemerovo",
    "Novokuznetsk",
]


async def get_all_city_coords():
    from ..utils import check_weather_data, get_city_coords

    if isinstance(data := check_weather_data(), DataFrame):
        return data
    coords_result = await asyncio.gather(*(get_city_coords(city) for city in CITIES))
    return check_weather_data(coords_result)
