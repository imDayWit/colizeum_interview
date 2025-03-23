import pandas as pd
import os

from ..constants import FilePath

__all__ = ["init_excel_file"]

def init_excel_file():
    df = pd.DataFrame()
    file_path = FilePath.FILE_PATH
    if not os.path.exists(file_path):
        with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, sheet_name="Users", index=False)