import asyncio

import pandas as pd

from ..constants import FilePath
from ..utils.save_to_sheet import save_to_sheet

__all__ = ["save_user_data"]


async def save_user_data():
    from ..utils import get_user

    data = await get_user(30)

    users = []
    for user in data["results"]:
        user_info = {
            "gender": user["gender"],
            "first_name": user["name"]["first"],
            "last_name": user["name"]["last"],
            "city": user["location"]["city"],
            "state": user["location"]["state"],
            "country": user["location"]["country"],
            "postcode": user["location"]["postcode"],
            "latitude": user["location"]["coordinates"]["latitude"],
            "longitude": user["location"]["coordinates"]["longitude"],
            "timezone": user["location"]["timezone"]["description"],
            "email": user["email"],
            "dob": user["dob"]["date"],
            "age": user["dob"]["age"],
            "phone": user["phone"],
            "cell": user["cell"],
            "picture": user["picture"]["medium"],
            "nationality": user["nat"],
        }
        users.append(user_info)

    df = pd.DataFrame(users)

    save_to_sheet(FilePath.FILE_PATH, "Users", df)
    print("Users data saved")  # noqa


# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(save_user_data())
