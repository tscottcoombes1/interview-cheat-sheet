import pandas as pd

from extract_play.pandas_playground import read_csv

def test_read_csv(csv_file):
    df = read_csv(csv_file)
    assert df.shape == (5, 7)  # 5 data rows, 7 columns
    print(df.dtypes)
    assert set(df.columns) == set(["boolean_col", "string_col", "date_col", "timestamp_col", "int_col", "decimal_col", "json_col"])
    assert df["boolean_col"].dtype == bool
    assert df["string_col"].dtype == object
    assert df["date_col"].dtype == 'datetime64[ns]'
    assert df["timestamp_col"].dtype == 'datetime64[ns, UTC]'  # Timezone-aware UTC timestamps
    assert df["int_col"].dtype == int
    assert df["decimal_col"].dtype == float
    assert df["json_col"].dtype == object 
