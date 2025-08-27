import polars as pl

from extract_play.polars_playground import read_csv

def test_read_csv(csv_file):
    df = read_csv(csv_file)
    assert df.shape == (5, 7)  # 5 data rows, 7 columns
    assert df.columns == ["boolean_col", "string_col", "date_col", "timestamp_col", "int_col", "decimal_col", "json_col"]
    assert df["boolean_col"].dtype == pl.Boolean
    assert df["string_col"].dtype == pl.Utf8
    assert df["date_col"].dtype == pl.Date
    assert df["timestamp_col"].dtype == pl.Datetime
    assert df["int_col"].dtype == pl.Int64
    assert df["decimal_col"].dtype == pl.Float64
