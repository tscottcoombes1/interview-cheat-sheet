import pandas as pd
from pathlib import Path

def read_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path,
        dtype={
            "boolean_col": bool,
            "string_col": str,
            "int_col": int,
            "decimal_col": float,
            "json_col": str,
        },
        parse_dates=["date_col", "timestamp_col"],  # Parse date columns automatically
    )
    return df
