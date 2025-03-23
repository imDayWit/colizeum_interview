from enum import StrEnum

__all__ = ["APIURLEnum"]


class APIURLEnum(StrEnum):
    OPEN_WEATHER_URL = "http://api.openweathermap.org/"
    NEWS_URL = "https://newsapi.org/v2/everything"
    RANDOM_USER_URL = "https://randomuser.me/api/"
