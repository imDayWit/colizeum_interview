import os

import pandas as pd

from ..constants import FilePath

__all__ = ["check_weather_data"]



def check_weather_data(coords_result=None):
    file_path = FilePath.FILE_PATH
    if os.path.exists(file_path):
        excel_data = pd.read_excel(file_path, sheet_name=None)
        if "Weather" in excel_data:
            weather_df = excel_data["Weather"]
            if not weather_df.empty and all(
                col in weather_df.columns for col in ["City", "Lat", "Lon"]
            ):
                if weather_df[["City", "Lat", "Lon"]].isnull().sum().sum() == 0:
                    print(  # noqa
                        "Coords data already exists in the file. Skipping the request."
                    )
                    return weather_df

    if coords_result:
        weather_df = pd.DataFrame(coords_result)
        weather_df.to_excel(file_path, sheet_name="Weather", index=False)
        print("New coords data written to data.xlsx")  # noqa
        return weather_df
    print("Coords data doesn't exist. Creating a new one.")  # noqa
    return None
