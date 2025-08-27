import connectorx as cx
import pandas as pd
import polars as pl
import pyarrow as pa


def read_db_to_arrow(connection_url: str, query: str) -> pa.Table:
    table = cx.read_sql(connection_url, query, return_type="arrow")
    return table


def read_db_to_pandas(connection_url: str, query: str) -> pd.DataFrame:
    df = cx.read_sql(connection_url, query, return_type="pandas")
    return df


def read_db_to_polars(connection_url: str, query: str) -> pl.DataFrame:
    df = cx.read_sql(connection_url, query, return_type="polars")
    return df

