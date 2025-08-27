import polars as pl
from pathlib import Path

def read_csv(path: Path) -> pl.DataFrame:
    df = pl.read_csv(
        path,
        infer_schema_length=10000,
        ignore_errors=False,
        try_parse_dates=True,
    )
    return df
