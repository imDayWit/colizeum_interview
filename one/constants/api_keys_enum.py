from enum import StrEnum

__all__ = ["APIKeysEnum"]


# todo - лучше использовать env-ы, но в ТЗ не было условий
class APIKeysEnum(StrEnum):
    OPEN_WEATHER_API = "api_key_here"
    NEWS_API = "api_key_here"
