import pandas as pd

__all__ = ["save_to_sheet"]


def save_to_sheet(file_path: str, sheet_name: str, dataframe: pd.DataFrame):
    with pd.ExcelWriter(
        file_path, engine="openpyxl", mode="a", if_sheet_exists="replace"
    ) as writer:
        dataframe.to_excel(writer, sheet_name=sheet_name, index=False)
