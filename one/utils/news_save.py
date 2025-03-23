import pandas as pd

from ..constants import FilePath
from ..utils.save_to_sheet import save_to_sheet

__all__ = ["save_news"]


async def save_news():
    from ..utils import get_news

    data = await get_news("PC gaming")
    articles = data["articles"]

    data = []
    for article in articles:
        data.append(
            {
                "Source": article["source"]["name"],
                "Author": article["author"],
                "Title": article["title"],
                "Description": article["description"],
                "URL": article["url"],
                "URL To Image": article["urlToImage"],
                "Published At": article["publishedAt"],
                "Content": article["content"],
            }
        )
    df = pd.DataFrame(data)

    df["Published At"] = pd.to_datetime(df["Published At"])
    df["Published At"] = df["Published At"].dt.tz_localize(None)
    df = df.sort_values(by="Published At", ascending=False)

    save_to_sheet(FilePath.FILE_PATH, "News", df)
    print("News data saved")  # noqa
